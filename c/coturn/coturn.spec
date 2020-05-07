%define coturn_user	_coturn
%define coturn_group	_coturn
%define coturn_sharedir %_datadir/%name
%define coturn_examplesdir %_datadir/%name/examples

%define unpackaged_files_terminate_build 1

Name:		coturn
Version:	4.5.1.1
Release:	alt2
Summary:	Coturn TURN Server

License:	BSD
Group:		Networking/Other
URL:		https://github.com/coturn/coturn/

Source0:	%name-%version.tar
Patch0:		%name-%version-%release.patch

BuildRequires:	libsqlite3-devel
BuildRequires:	openssl-devel, libevent-devel >= 2.0.0
Requires:	openssl, sqlite3, libevent >= 2.0.0
BuildRequires:	postgresql-devel
Requires:	libpq5
BuildRequires:	libmariadb-devel
Requires: 	libmariadb3
BuildRequires:	libhiredis-devel
Requires:	libhiredis0.13
BuildRequires:	perl-DBI, perl-libwww-perl


%description
The TURN Server is a VoIP media traffic NAT traversal server and gateway. It
can be used as a general-purpose network traffic TURN server/gateway, too.

This implementation also includes some extra features. Supported RFCs:

TURN specs:
- RFC 5766 - base TURN specs
- RFC 6062 - TCP relaying TURN extension
- RFC 6156 - IPv6 extension for TURN
- Experimental DTLS support as client protocol.

STUN specs:
- RFC 3489 - "classic" STUN
- RFC 5389 - base "new" STUN specs
- RFC 5769 - test vectors for STUN protocol testing
- RFC 5780 - NAT behavior discovery support

The implementation fully supports the following client-to-TURN-server protocols:
- UDP (per RFC 5766)
- TCP (per RFC 5766 and RFC 6062)
- TLS (per RFC 5766 and RFC 6062); TLS1.0/TLS1.1/TLS1.2
- DTLS (experimental non-standard feature)

Supported relay protocols:
- UDP (per RFC 5766)
- TCP (per RFC 6062)

Supported user databases (for user repository, with passwords or keys, if
authentication is required):
- SQLite
- MySQL
- PostgreSQL
- Redis (disabled in ALT package)

Redis can also be used for status and statistics storage and notification.

Supported TURN authentication mechanisms:
- long-term
- TURN REST API (a modification of the long-term mechanism, for time-limited
  secret-based authentication, for WebRTC applications)

The load balancing can be implemented with the following tools (either one or a
combination of them):
- network load-balancer server
- DNS-based load balancing
- built-in ALTERNATE-SERVER mechanism.


%package 	utils
Summary:	coturn: TURN client utils
Group:		System/Libraries
Requires:	%name-client-libs = %{version}-%{release}

%description 	utils
This package contains coturn's TURN client utils.

%package 	client-libs
Summary:	coturn: TURN client library
Group:		System/Libraries
Requires:	openssl, libevent >= 2.0.0

%description	client-libs
This package contains coturn's TURN client library.

%package 	client-devel
Summary:	coturn: TURN client development headers
Group:		Development/C
Requires:	%name-client-libs = %{version}-%{release}

%description 	client-devel
This package contains coturn's TURN client development headers.

%prep
%setup
%patch -p1

%add_findreq_skiplist %coturn_sharedir/*
%add_findreq_skiplist %coturn_examplesdir/*
%add_findreq_skiplist %coturn_examplesdir/scripts/*

%build
export PREFIX=%_prefix
export LIBDIR=%_libdir
export CONFDIR=%_sysconfdir/%name
export EXAMPLESDIR=%_datadir/%name/examples
export DOCSDIR=%_docdir/%name-%version
# The home-brewn configure script interprets mandir in a peculiar way: it puts
# man pages in $mandir/man/man1/.
%configure \
	--disable-rpath \
	--portname='%name' \
	--mandir='%_datadir' --schemadir='%_datadir/%name' --turndbdir='/var/db' \
	#
%make_build

%install
%makeinstall_std

mkdir -p %buildroot/%_sysconfdir/%name
mv %buildroot%_sysconfdir{,/%name}/turnserver.conf.default
#sed -i -e "s/#syslog/syslog/g" \
#    -e "s/#no-stdout-log/no-stdout-log/g" \
#    %buildroot/%{_sysconfdir}/%{name}/turnserver.conf.default

mkdir -p %buildroot/%{_sysconfdir}/sysconfig
install -m644 rpm/turnserver.sysconfig \
		%buildroot/%{_sysconfdir}/sysconfig/%name

### The upstream gives us a RedHat-style init script which is broken in ALT.
### We might adapt it for ALT in the future, if we need svinit support.
### Also look for "init script" in the %%files section.
#mkdir -p %buildroot/%{_sysconfdir}/rc.d/init.d
#install -m755 rpm/turnserver.init.el \
#		%buildroot/%{_sysconfdir}/rc.d/init.d/%name

sed -i -e "s/#pidfile/pidfile/g" \
	-e "s:%_runtimedir/turnserver.pid:%_runtimedir/%name/turnserver.pid:g" \
	%buildroot/%{_sysconfdir}/%{name}/turnserver.conf.default
mv %buildroot/%{_sysconfdir}/%{name}/turnserver.conf.default %buildroot/%{_sysconfdir}/%{name}/turnserver.conf

sed -e "s/@coturn_user@/%coturn_user/; s/@coturn_group@/%coturn_group/;" \
	-e "s/@coturn_package_name@/%name/" altlinux/coturn.service.in > altlinux/coturn.service
install -D -m644 altlinux/coturn.service \
		%buildroot/%{_unitdir}/%name.service

sed -e "s/@coturn_user@/%coturn_user/; s/@coturn_group@/%coturn_group/" \
	altlinux/coturn-tmpfiles.conf.in > altlinux/coturn-tmpfiles.conf
install -D -m644 altlinux/coturn-tmpfiles.conf \
		%{buildroot}%{_tmpfilesdir}/%name.conf
mkdir -p %{buildroot}/run/%name

%pre
%{_sbindir}/groupadd -r %coturn_group 2> /dev/null || :
%{_sbindir}/useradd -r -g %coturn_group -s /bin/false -c "coturn server daemon" \
		-d %{_datadir}/%{name} %coturn_user 2> /dev/null || :

%post
%post_service %name

%preun
%preun_service %name

%files
%defattr(-,root,root)
%{_bindir}/turnserver
%{_bindir}/turnadmin
# %attr(0640,%coturn_user,%coturn_group) /var/db/turndb
%{_man1dir}/coturn.1*
%{_man1dir}/turnserver.1*
%{_man1dir}/turnadmin.1*
%dir %attr(-,%coturn_user,%coturn_group) %{_sysconfdir}/%{name}
%config(noreplace) %attr(0644,%coturn_user,%coturn_group) %{_sysconfdir}/%{name}/turnserver.conf
%ghost %attr(0750,%coturn_user,%coturn_group) /run/%name
%config(noreplace) %{_sysconfdir}/sysconfig/%name
### The init script is not ready.
# %config %{_sysconfdir}/rc.d/init.d/%name
%{_unitdir}/%name.service
%{_tmpfilesdir}/%name.conf
%doc LICENSE
%doc INSTALL
%doc postinstall.txt
%doc README.turnadmin
%doc README.turnserver
%dir %coturn_sharedir
%coturn_sharedir/schema.sql
%coturn_sharedir/schema.mongo.sh
%coturn_sharedir/schema.stats.redis
%coturn_sharedir/schema.userdb.redis
%coturn_sharedir/testredisdbsetup.sh
%coturn_sharedir/testmongosetup.sh
%coturn_sharedir/testsqldbsetup.sql
%dir %coturn_examplesdir
%dir %coturn_examplesdir/etc
%coturn_examplesdir/etc/turn_server_cert.pem
%coturn_examplesdir/etc/turn_server_pkey.pem
%coturn_examplesdir/etc/turnserver.conf

%files 		utils
%defattr(-,root,root)
%{_bindir}/turnutils_peer
%{_bindir}/turnutils_stunclient
%{_bindir}/turnutils_uclient
%{_bindir}/turnutils_oauth
%{_bindir}/turnutils_natdiscovery
%{_man1dir}/turnutils.1*
%{_man1dir}/turnutils_peer.1*
%{_man1dir}/turnutils_stunclient.1*
%{_man1dir}/turnutils_uclient.1*
%{_man1dir}/turnutils_oauth.1*
%{_man1dir}/turnutils_natdiscovery.1*
%doc LICENSE
%doc README.turnutils
%dir %coturn_examplesdir
%dir %coturn_examplesdir/etc
%coturn_examplesdir/etc/turn_client_cert.pem
%coturn_examplesdir/etc/turn_client_pkey.pem
%dir %coturn_examplesdir/scripts
%coturn_examplesdir/scripts/peer.sh
%coturn_examplesdir/scripts/oauth.sh
%coturn_examplesdir/scripts/readme.txt
%coturn_examplesdir/scripts/pack.sh
%dir %coturn_examplesdir/scripts/basic
%coturn_examplesdir/scripts/basic/dos_attack.sh
%coturn_examplesdir/scripts/basic/relay.sh
%coturn_examplesdir/scripts/basic/tcp_client.sh
%coturn_examplesdir/scripts/basic/tcp_client_c2c_tcp_relay.sh
%coturn_examplesdir/scripts/basic/udp_c2c_client.sh
%coturn_examplesdir/scripts/basic/udp_client.sh
%dir %coturn_examplesdir/scripts/loadbalance
%coturn_examplesdir/scripts/loadbalance/master_relay.sh
%coturn_examplesdir/scripts/loadbalance/slave_relay_1.sh
%coturn_examplesdir/scripts/loadbalance/slave_relay_2.sh
%coturn_examplesdir/scripts/loadbalance/tcp_c2c_tcp_relay.sh
%coturn_examplesdir/scripts/loadbalance/udp_c2c.sh
%dir %coturn_examplesdir/scripts/longtermsecure
%coturn_examplesdir/scripts/longtermsecure/secure_dos_attack.sh
%coturn_examplesdir/scripts/longtermsecure/secure_dtls_client.sh
%coturn_examplesdir/scripts/longtermsecure/secure_dtls_client_cert.sh
%coturn_examplesdir/scripts/longtermsecure/secure_tls_client_cert.sh
%coturn_examplesdir/scripts/longtermsecure/secure_relay.sh
%coturn_examplesdir/scripts/longtermsecure/secure_relay_cert.sh
%coturn_examplesdir/scripts/longtermsecure/secure_tcp_client.sh
%coturn_examplesdir/scripts/longtermsecure/secure_tcp_client_c2c_tcp_relay.sh
%coturn_examplesdir/scripts/longtermsecure/secure_tls_client.sh
%coturn_examplesdir/scripts/longtermsecure/secure_tls_client_c2c_tcp_relay.sh
%coturn_examplesdir/scripts/longtermsecure/secure_udp_c2c.sh
%coturn_examplesdir/scripts/longtermsecure/secure_udp_client.sh
%coturn_examplesdir/scripts/longtermsecure/secure_sctp_client.sh
%dir %coturn_examplesdir/scripts/longtermsecuredb
%coturn_examplesdir/scripts/longtermsecuredb/secure_relay_with_db_mysql.sh
%coturn_examplesdir/scripts/longtermsecuredb/secure_relay_with_db_mysql_ssl.sh
%coturn_examplesdir/scripts/longtermsecuredb/secure_relay_with_db_mongo.sh
%coturn_examplesdir/scripts/longtermsecuredb/secure_relay_with_db_psql.sh
%coturn_examplesdir/scripts/longtermsecuredb/secure_relay_with_db_redis.sh
%coturn_examplesdir/scripts/longtermsecuredb/secure_relay_with_db_sqlite.sh
%dir %coturn_examplesdir/scripts/restapi
%coturn_examplesdir/scripts/restapi/secure_relay_secret.sh
%coturn_examplesdir/scripts/restapi/secure_relay_secret_with_db_mysql.sh
%coturn_examplesdir/scripts/restapi/secure_relay_secret_with_db_psql.sh
%coturn_examplesdir/scripts/restapi/secure_relay_secret_with_db_redis.sh
%coturn_examplesdir/scripts/restapi/secure_relay_secret_with_db_mongo.sh
%coturn_examplesdir/scripts/restapi/secure_relay_secret_with_db_sqlite.sh
%coturn_examplesdir/scripts/restapi/secure_udp_client_with_secret.sh
%coturn_examplesdir/scripts/restapi/shared_secret_maintainer.pl
%dir %coturn_examplesdir/scripts/selfloadbalance
%coturn_examplesdir/scripts/selfloadbalance/secure_dos_attack.sh
%coturn_examplesdir/scripts/selfloadbalance/secure_relay.sh
%dir %coturn_examplesdir/scripts/mobile
%coturn_examplesdir/scripts/mobile/mobile_relay.sh
%coturn_examplesdir/scripts/mobile/mobile_dtls_client.sh
%coturn_examplesdir/scripts/mobile/mobile_tcp_client.sh
%coturn_examplesdir/scripts/mobile/mobile_tls_client_c2c_tcp_relay.sh
%coturn_examplesdir/scripts/mobile/mobile_udp_client.sh

%files		client-libs
%doc LICENSE
%{_libdir}/libturnclient.a

%files		client-devel
%doc LICENSE
%dir %{_includedir}/turn
%{_includedir}/turn/ns_turn_defs.h
%dir %{_includedir}/turn/client
%{_includedir}/turn/client/ns_turn_ioaddr.h
%{_includedir}/turn/client/ns_turn_msg_addr.h
%{_includedir}/turn/client/ns_turn_msg_defs.h
%{_includedir}/turn/client/ns_turn_msg_defs_experimental.h
%{_includedir}/turn/client/ns_turn_msg.h
%{_includedir}/turn/client/TurnMsgLib.h

%changelog
* Sun Apr 05 2020 Arseny Maslennikov <arseny@altlinux.org> 4.5.1.1-alt2
- Applied upstream fixes for CVE-2020-6062/TALOS-2020-0985.
- Applied upstream fixes for CVE-2020-6061/TALOS-2020-0984.

* Fri Mar 20 2020 Arseny Maslennikov <arseny@altlinux.org> 4.5.1.1-alt1
- First build for ALT Sisyphus.
