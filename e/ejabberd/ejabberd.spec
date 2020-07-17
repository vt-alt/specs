%define _unpackaged_files_terminate_build 1

%def_disable hipe
%def_enable stun
%def_enable sip
%def_enable mysql
%def_enable pgsql
%def_enable sqlite
%def_enable pam
%def_enable zlib
%def_enable tools

Name: ejabberd
Version: 20.04
Release: alt1
Summary: Fault-tolerant distributed Jabber server written in Erlang
License: GPL-2.0 with OpenSSL-exception
Group: System/Servers
Url: https://www.process-one.net/en/ejabberd/

BuildArch: noarch

# https://github.com/processone/ejabberd.git
Source: %name-%version.tar

Source1: %name-%version-alt.tar

Source2: %name.watch

# Use ejabberd as an example for PAM service name
Patch4: ejabberd-fedora-enable-systemd-notification-if-available.patch

Patch11: ejabberd-alt-version.patch
# https://github.com/processone/ejabberd/issues/1037
Patch12: ejabberd-alt-erllibs-path.patch

BuildRequires(pre): jabber-common >= 0.2
BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-devel erlang-otp-devel libcom_err-devel libexpat-devel libssl-devel zlib-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-lager
BuildRequires: erlang-p1_utils
BuildRequires: erlang-cache_tab
BuildRequires: erlang-fast_tls
BuildRequires: erlang-stringprep
BuildRequires: erlang-fast_xml
BuildRequires: erlang-xmpp
BuildRequires: erlang-fast_yaml
BuildRequires: erlang-jiffy
BuildRequires: erlang-p1_oauth2
BuildRequires: erlang-jose
BuildRequires: erlang-eimp
BuildRequires: erlang-sd_notify
BuildRequires: erlang-pkix
BuildRequires: erlang-mqtree
BuildRequires: erlang-idna
BuildRequires: erlang-yconf
BuildRequires: erlang-p1_acme
%{?_enable_stun:BuildRequires: erlang-stun}
%{?_enable_sip:BuildRequires: erlang-esip}
%{?_enable_mysql:BuildRequires: erlang-p1_mysql}
%{?_enable_pgsql:BuildRequires: erlang-p1_pgsql}
%{?_enable_sqlite:BuildRequires: erlang-sqlite3 libsqlite3-devel}
%{?_enable_pam:BuildRequires: erlang-epam}
%{?_enable_zlib:BuildRequires: erlang-ezlib}
%{?_enable_tools:BuildRequires: erlang-luerl}

Requires: erlang
Requires: jabber-common >= 0.2
Requires: su

# workaround for bug #36925
Requires: erlang-lager

Provides: %name-pam = %EVR
Obsoletes: %name-pam

%add_erlang_req_modules_skiplist Elixir.Ejabberd.Config
%add_erlang_req_modules_skiplist Elixir.Ejabberd.Config.Store
%add_erlang_req_modules_skiplist Elixir.Ejabberd.ConfigUtil
%add_erlang_req_modules_skiplist Elixir.Kernel.ParallelCompiler
%add_erlang_req_modules_skiplist Elixir.Logger
%add_erlang_req_modules_skiplist Elixir.Logger.Config
%add_erlang_req_modules_skiplist Elixir.Logger.Utils
%add_erlang_req_modules_skiplist eredis
%add_erlang_req_modules_skiplist eredis_sub

%description
ejabberd is a Free and Open Source distributed fault-tolerant Jabber
server. It writen mostly in Erlang.

The main features of ejabberd is:

* Truly portable
* Distributed
* Fault-tolerance
* Built-in Multi-User Chat service
* Built-in IRC transport
* Built-in Publish-Subscribe service
* Built-in Jabber Users Directory service based on users vCards
* Built-in web-based administration interface
* Built-in HTTP Polling service
* SSL support
* Support for LDAP authentification
* Ability to interface with external components (JIT, MSN-t, Yahoo-t, etc)
* Migration from jabberd14 is possible
* Mostly XMPP-compliant
* Support for JEP-0030 (Service Discovery).
* Support for JEP-0039 (Statistics Gathering).
* Support for xml:lang

%prep
%setup -a 1
%patch4 -p1
%patch11 -p1
%patch12 -p1

# Upstream seems to import erlang-xmpp and erlang-fast_xml in a way that isn't compatible with them
# being system libraries. We need to patch the include statements to fix this.
# https://github.com/processone/ejabberd/pull/1446/
find . -name "*.hrl" | xargs sed -i \
    "s/include(\"fxml.hrl/include_lib(\"fast_xml\/include\/fxml.hrl/"
find . -name "*.erl" | xargs sed -i "s/include(\"jid.hrl/include_lib(\"xmpp\/include\/jid.hrl/"
find . -name "*.hrl" | xargs sed -i "s/include(\"ns.hrl/include_lib(\"xmpp\/include\/ns.hrl/"
find . -name "*.erl" | xargs sed -i "s/include(\"xmpp.hrl/include_lib(\"xmpp\/include\/xmpp.hrl/"
find . -name "*.hrl" | xargs sed -i \
    "s/include(\"xmpp_codec.hrl/include_lib(\"xmpp\/include\/xmpp_codec.hrl/"

# A few dependencies are configured to be found in the deps folder instead of in system libs
# https://github.com/processone/ejabberd/issues/1850
perl -p -i -e "s|deps/p1_utils/include|$(rpm -ql erlang-p1_utils | grep -E '/include$' )|g" rebar.config
perl -p -i -e "s|deps/fast_xml/include|$(rpm -ql erlang-fast_xml | grep -E '/include$' )|g" rebar.config
perl -p -i -e "s|deps/xmpp/include|$(rpm -ql erlang-xmpp | grep -E '/include$' )|g"   rebar.config

sed -i -e "s:@version@:%version:g" configure.ac

# additional update for patch 12
sed -i -e "s|@ERL_LIBS@|%_erllibdir/%name-%version:|g" ejabberdctl.template

%build
%autoreconf
%configure \
	--datarootdir=%_datadir \
	--libdir=%_erllibdir \
	--localstatedir=%_var \
	--enable-system-deps \
	--enable-odbc \
	%{subst_enable hipe} \
	%{subst_enable stun} \
	%{subst_enable sip} \
	%{subst_enable mysql} \
	%{subst_enable pgsql} \
	%{subst_enable sqlite} \
	%{subst_enable pam} \
	%{subst_enable zlib} \
	%{subst_enable tools}

#--enable-user=ejabberd

%rebar_compile

%install
%makeinstall DESTDIR=%buildroot

rm -rf %buildroot%_defaultdocdir/%name

(cd %name-%version-alt && find . -type f |cpio -pumd %buildroot)

mkdir -p %buildroot%_localstatedir/ejabberd %buildroot%_logdir/ejabberd \
	%buildroot%_sysconfdir/sysconfig/ %buildroot%_lockdir/ejabberd
mv %buildroot%_sysconfdir/%name/ejabberdctl.cfg %buildroot%_sysconfdir/sysconfig/ejabberd

install -p -m 0644 sql/mysql.sql %buildroot%_erllibdir/%name-%version/priv/sql/
install -p -m 0644 sql/pg.sql    %buildroot%_erllibdir/%name-%version/priv/sql/

%pre
%_sbindir/groupadd -r -f ejabberd &>/dev/null
%_sbindir/useradd -r -g ejabberd  -d %_localstatedir/ejabberd -s /dev/null \
    -c 'ejabberd server' -M -n ejabberd &>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name

%files
%doc COPYING README.md examples

%dir %_sysconfdir/ejabberd
%config(noreplace) %_sysconfdir/ejabberd/inetrc
%attr(640,root,ejabberd) %config(noreplace) %_sysconfdir/ejabberd/ejabberd.yml
%attr(0640,root,ejabberd) %config(noreplace) %_sysconfdir/sysconfig/ejabberd
%attr(0640,root,root) %config %_sysconfdir/logrotate.d/ejabberd
%config(noreplace) %_sysconfdir/pam.d/ejabberd
%config(noreplace) %_sysconfdir/pam.d/ejabberdctl

%_initdir/ejabberd
%_unitdir/%name.service
%attr(0755,root,ejabberd) %_sbindir/ejabberdctl

%_datadir/polkit-1/actions/ejabberdctl.policy
%_datadir/polkit-1/rules.d/51-ejabberdctl.rules

%_erllibdir/%name-%version

%_jabber_server_dir/ejabberd

%_man5dir/*
%_man8dir/*

%attr(1770,root,ejabberd) %dir %_localstatedir/ejabberd
%attr(1770,root,ejabberd) %dir %_logdir/ejabberd
%attr(1770,root,ejabberd) %dir %_lockdir/ejabberd

%changelog
* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20.04-alt1
- Updated to upstream version 20.04.

* Tue Mar 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 20.03-alt1
- Updated to upstream version 20.03.

* Thu Jun 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 19.05-alt1
- Updated to upstream version 19.05.

* Fri Mar 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 19.02-alt3
- ejabberd.service: service type was changed to notify again (was changed by
  mistake in the previous release).

* Fri Mar 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 19.02-alt2
- Fixed and refactored SysVinit script and systemd service files.
- Added reload command for ejabberd service.

* Tue Mar 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 19.02-alt1
- Updated to upstream version 19.02.

* Mon Jan 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 18.12.1-alt1
- Updated to upstream version 18.12.1.

* Mon Jul 02 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 18.03-alt3
- Fixed SysVInit script.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 18.03-alt2
- Fixed LDAP module (upstream issue #1037).

* Fri Apr 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 18.03-alt1
- Updated to upstream version 18.03.

* Wed Apr 06 2016 Denis Medvedev <nbr@altlinux.org> 2.1.13-alt1
- 2.1.13

* Tue Apr 05 2016 Denis Medvedev <nbr@altlinux.org> 2.1.10-alt1.1
- removed strict requirement to erlang version.

* Sat Mar 31 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.10-alt1
- 2.1.10 (Closes: #26762).

* Thu Nov 17 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.9-alt1
- 2.1.9.

* Mon Jun 06 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.8-alt1
- 2.1.8 (fixes mod_pubsub broken in previous release).

* Fri Jun 03 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.7-alt1
- 2.1.7, fixes CVE-2011-1753 (The vulnerability is caused due to an
  error within the parsing of certain XML input, which can be exploited
  to e.g. cause a high CPU and memory consumption via heavily nested XML
  entities), please update immediately.
- Add PostgreSQL support (pma).

* Thu Dec 16 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.6-alt1
- 2.1.6

* Mon Oct 11 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.5-alt2
[ Mikhail A Pokidko]
- Update modules:
  + mod_statsdx
  + mod_admin_extra
- Fix permissions of captcha.sh
[ Vladimir V. Kamarzin ]
- Update mod_shared_roster_ldap to 0.5.3

* Tue Oct 05 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.5-alt1
- 2.1.5

* Thu Apr 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.3-alt1
[ Mikhail A Pokidko]
- 2.1.3 (Closes: #23264)
- Add some extra modules:
  + mod_asterisk
  + mod_admin_extra
- Remove modules:
  + mod_ctlextra
  + ejabberd_http_bind
  + mod_http_bind
  + mod_http_fileserver
- Disable mod_stats
- Move Extra modules into ejabberd-extra subpackage
- Initscript: add delay at restart
[ Afanasov Dmitry ]
- Fix mod_shared_roster_ldap
[ Vladimir V. Kamarzin ]
- Package captcha script as separate subpackage ejabberd-captcha
- Use /var/lock/ejabberd for ejabberdctl locks

* Fri Apr 10 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.5-alt1
[ Sergey Bolshakov ]
- 2.0.5 release
[ Mikhail A Pokidko]
- Added some extra modules:
  + mod_ctlextra
  + mod_rest
  + mod_stats2file
  + mod_statsdx
  + ejabberd_http_bind
  + mod_http_bind
  + mod_http_fileserver
- Modified default config
[ Vladimir V. Kamarzin ]
- Added dependency on su(1)

* Wed Jan 21 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.3-alt2
[ Michael Shigorin ]
- Added PAM support as a subpackage (enabled by default)

* Mon Jan 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.3-alt1
[ Sergey Bolshakov ]
- 2.0.3 release

* Thu Dec 18 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.2-alt2
[ Sergey Bolshakov ]
- Updated to 1734 svn revision of branches/ejabberd-2.0.x

* Mon Oct 06 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.2-alt1
[ Sergey Bolshakov ]
- 2.0.2 release (Closes: #16093)
- ODBC enabled (Closes: #13598)
- PostgreSQL module added
- Initscript rewritten
- Added /etc/ejabberd/inetrc (Closes: #13618)
[ Vladimir V. Kamarzin ]
- Added mod_shared_roster_ldap with gray_graff patch (Closes: #16485)

* Sun Nov 11 2007 Mikhail Yakshin <greycat@altlinux.org> 1.1.4-alt1
- 1.1.4

* Sun Nov 11 2007 Mikhail Yakshin <greycat@altlinux.org> 1.1.3-alt3
- newer jabber-config support

* Wed Mar 14 2007 Mikhail Yakshin <greycat@altlinux.org> 1.1.3-alt2
- jabber-config support
- added mod_passrecover (#11065)

* Sun Feb 18 2007 Mikhail Yakshin <greycat@altlinux.org> 1.1.3-alt1
- 1.1.3

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.1-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Aug 24 2006 Mikhail Yakshin <greycat@altlinux.org> 1.1.1-alt1
- 1.1.1

* Mon Jan 09 2006 Mikhail Yakshin <greycat@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sat Aug 27 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.9.8-alt1
- 0.9.8
- added w3c standards compliance patch

* Wed Apr 20 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.9-alt1
- 0.9
- modified ejabberd init to support 'status' command

* Tue Mar 08 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.7.5-alt2
- fixed #6135 with patch from teo (Sergei Golovan)

* Wed Jan 12 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Sun Aug 22 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.7-alt1
- Initial build for ALT Linux

