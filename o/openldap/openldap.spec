%define _sover 2.4
%define _bname openldap
### Build switches for enable or disable fiture ###
%def_enable doc
%def_enable sql
%def_enable perl
%def_disable shell
%def_enable sasl
### Disable, because while build by rpm is not passed
%def_disable debug
%def_disable slapi
%def_enable slp
%def_enable overlay
%def_enable aci
%def_enable yielding
%def_enable ntlm

Name: openldap
Version: %_sover.48
Release: alt2

Provides: openldap2.4 = %version-%release
Obsoletes: openldap2.4 < %version-%release

%define so_maj %_sover
%define ldap_ssl_dir %_sysconfdir/%name/ssl
%define ssl_dir %_localstatedir/ssl/certs
%define ldap_dir %_localstatedir/ldap

Summary: LDAP libraries and sample clients
License: OpenLDAP Public License
Group: System/Servers
Url: http://www.openldap.org/

Packager: OpenLDAP Maintainers Team <openldap@packages.altlinux.org>

# ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
Source: %name-%version.tar

# Docs for this products
#Source2: %name-README.upgrading
Source3: %_bname-README.ALT
Source4: %_bname-config-README.ALT

# System Specific source
Source11: %_bname.sysconfig
Source12: %_bname-slapd.init
Source13: %_bname.logrotate
Source14: %_bname-slapd.service

## Chroot config
Source15: %_bname-ldap.all
Source16: %_bname-ldap.conf
Source17: %_bname-ldap.lib
# This file we need to build from original dynamic
Source18: %_bname-slapd.conf
Source19: %_bname-bdb-DB_CONFIG
Source20: %_bname-slapd-access.conf
Source21: %_bname-slapd-mdb-db01.conf
Source22: %_bname-slapd-hdb-db01.conf
Source23: %_bname-slapd-hdb-db02.conf
# OLC config directory backup/restore scripts
Source40: %_bname-olc-backup
Source41: %_bname-olc-restore

# Extended OpenLDAP schemas
Source50: %_bname-addon-schemas.tar
Source51: %_bname-ALT-rootdse.ldif

### PATCHES
Patch1: %_bname-alt-defaults.patch

## Patch created by Alexander Bokovoy <ab@altlinux.ru>
Patch2: %_bname-2.3.34-alt-pid.patch
Patch3: %_bname-2.3.12-autoconf-2.5-alt.patch

Patch4: %_bname-2.3.20-alt-makefile.patch

Patch7: %_bname-2.3.34-alt-meta-backend.patch

Patch8: %_bname-2.3.37-alt-ntlm.patch

Patch11: %_bname-2.3.43-fix-ucred.patch

Patch13: %_bname-2.4.25-rh-ldaprc-currentdir.patch
Patch14: %_bname-2.4.25-rh-reentrant-gethostby.patch
Patch18: %_bname-2.4.31-rh-nss-allow-ca-dbdir-pemfile.patch
Patch19: %_bname-2.4.31-rh-tls-unbind-shutdown-order.patch
Patch20: %_bname-2.4.31-rh-nss-dont-overwrite-verify-cert-error.patch
Patch21: %_bname-2.4.31-rh-nss-clean-memory-for-token-pin.patch
Patch22: %_bname-2.4.31-rh-cve-nss-cipher-suite-ignored.patch
Patch23: %_bname-2.4.31-rh-nss-default-cipher-suite-always-selected.patch
Patch24: %_bname-2.4.31-rh-nss-multiple-tls-contexts.patch
Patch25: openldap-2.4.32-alt-gcc5.1.patch
Patch27: openldap-2.4.42-CVE-2015-3276.patch

### REQUIRE Section

%if_enabled doc
# For compile documentations need "sdf".
BuildRequires: sdf >= 2
%endif
%if_enabled sasl
# due to SASL_AUXPROP_PLUG_VERSION
BuildRequires: libsasl2-devel >= 2.1.24-alt1.cvs.20090508
%endif
%if_enabled sql
BuildRequires: libunixODBC-devel
%endif
%if_enabled perl
BuildRequires: perl-devel
%endif
%if_enabled slp
BuildRequires: libopenslp-devel
%endif

# Automatically added by buildreq on Tue Oct 18 2011 (-bi)
BuildRequires: chrooted groff-base libdb4-devel libltdl-devel libssl-devel shtool

%package -n libldap
Summary: OpenLDAP libraries
Group: System/Libraries
Provides: libldap2.4 = %version-%release
Obsoletes: libldap2.4 < %version-%release

%package -n libldap-devel
Summary: OpenLDAP development libraries and header files
Group: Development/C
Requires: libldap = %version-%release

Provides: openldap-devel = %version-%release
Obsoletes: openldap-devel < %version-%release

%package -n libldap-devel-static
Summary: OpenLDAP development static libraries
Group: Development/C
Requires: libldap-devel = %version-%release
Provides: openldap-devel-static = %version-%release
Obsoletes: openldap-devel-static < %version-%release

%package servers
Summary: LDAP servers
Group: System/Servers
Requires: libldap = %version-%release, %name = %version-%release

Provides: openldap2.4-servers = %version-%release
Obsoletes: openldap2.4-servers < %version-%release

%package clients
Summary: LDAP utilities, tools and sample clients
Group: Networking/Remote access
Requires: libldap = %version-%release, %name = %version-%release

Provides: openldap2.4-clients = %version-%release
Obsoletes: openldap2.4-clients < %version-%release

%if_enabled doc
%package -n %_bname-doc
Summary: OpenLDAP administration guide
Group: Books/Computer books
BuildArch: noarch

Provides: openldap2.4-doc = %version-%release
Obsoletes: openldap2.4-doc < %version-%release
%endif

%description
OpenLDAP is an open source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools.  LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet.  The suite includes a stand-alone LDAP server
(slapd), libraries for implementing the LDAP protocol, utilities, 
tools, and sample clients.

Install %_bname if you need to run LDAP-based applications and tools.

%description -n libldap
OpenLDAP is an open source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools.  LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet.  The suite includes a stand-alone LDAP server
(slapd), libraries for implementing the LDAP protocol, utilities, 
tools, and sample clients.

This package contains shared libraries needed for make works %_bname-based softare.

%description -n libldap-devel
OpenLDAP is an open source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools.  LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet.  The suite includes a stand-alone LDAP server
(slapd), libraries for implementing the LDAP protocol, utilities, 
tools, and sample clients.

This package includes the development libraries and header files needed
for developing applications that use LDAP internals. Install this package
only if you plan to develop or will need to compile customized LDAP clients.

%description -n libldap-devel-static
OpenLDAP is an open source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools.  LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet.  The suite includes a stand-alone LDAP server
(slapd), libraries for implementing the LDAP protocol, utilities, 
tools, and sample clients.

This package includes the static libraries needed for developing statically
linked applications that use LDAP internals.

%description servers
OpenLDAP is an open source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools.  LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet.  The suite includes a stand-alone LDAP server
(slapd), libraries for implementing the LDAP protocol, utilities, 
tools, and sample clients.

Install %_bname-servers if you need LDAP servers.

%description clients
OpenLDAP is an open source suite of LDAP (Lightweight Directory Access
Protocol) applications and development tools.  LDAP is a set of
protocols for accessing directory services (usually phone book style
information, but other information is possible) over the Internet,
similar to the way DNS (Domain Name System) information is propagated
over the Internet.  The suite includes a stand-alone LDAP server
(slapd), libraries for implementing the LDAP protocol, utilities, 
tools, and sample clients.

Install %_bname-client if you need LDAP applications and tools.

%if_enabled doc
%description -n %_bname-doc
OpenLDAP Administration Guide
HTML and TXT versions
%endif

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%%patch7 -p1

%if_enabled ntlm
%patch8 -p1 -b .ntlm
%endif

%patch11 -p1

%patch13 -p1
%patch14 -p1

%patch27 -p1

# Add some more schema for the sake of migration scripts and others
pushd servers/slapd
tar -xf %SOURCE50
popd


%build

# Options -lresolv in line below need for some bad configure scripts like in auth_ldap package
#export LDFLAGS="$LDFLAGS -lresolv"
export CPPFLAGS="$CPPFLAGS -DLOG_DAEMON=1"

shtoolize all
aclocal
autoconf
libtoolize --force --install

%configure \
	--enable-syslog \
	--enable-proctitle \
	--enable-dynamic \
	--with-tls=openssl \
	--with-threads \
	--enable-slapd \
	--enable-lmpasswd \
	--enable-crypt \
	--enable-cleartext \
	--enable-modules \
	--enable-rewrite \
	--enable-bdb=mod \
	--enable-hdb=mod \
	--enable-dnssrv=mod \
	--enable-ldap=mod \
	--enable-relay=mod \
	--enable-memberof=mod \
	--enable-meta=mod \
	--enable-monitor=mod \
	--enable-null=mod \
	--enable-passwd=mod \
	\
%if_enabled yielding
	--with-yielding-select \
%else
	--without-yielding-select \
%endif
%if_enabled aci
	--enable-aci \
%else
	--disable-aci \
%endif
%if_enabled slapi
	--enable-slapi \
%else
	--disable-slapi \
%endif
%if_enabled slp
	--enable-slp \
%else
	--disable-slp \
%endif
%if_enabled shell
	--enable-shell=mod \
	--without-threads \
%else
	--disable-shell \
	--with-threads \
%endif
%if_enabled sql
	--enable-sql=mod \
%else
	--disable-sql \
%endif
%if_enabled sasl
	--with-cyrus-sasl \
	--enable-spasswd \
%else
	--without-cyrus-sasl \
%endif
%if_enabled perl
	--enable-perl=mod \
%else
	--disable-perl \
%endif
%if_enabled overlay
	--enable-accesslog=mod \
	--enable-auditlog=mod \
	--enable-dyngroup=mod \
	--enable-dynlist=mod \
	--enable-ppolicy=mod \
	--enable-proxycache=mod \
	--enable-refint=mod \
	--enable-retcode=mod \
	--enable-rwm=mod \
	--enable-syncprov=mod \
	--enable-translucent=mod \
	--enable-unique=mod \
	--enable-valsort=mod \
%else
	--disable-accesslog \
	--disable-auditlog \
	--disable-dyngroup \
	--disable-dynlist \
	--disable-ppolicy \
	--disable-proxycache \
	--disable-refint \
	--disable-retcode \
	--disable-rwm \
	--disable-syncprov \
	--disable-translucent \
	--disable-unique \
	--disable-valsort \
%endif
%if_enabled debug
	--enable-debug \
%endif


%__subst 's/^AC_CFLAGS.*/& %optflags_shared/' libraries/librewrite/Makefile

%make depend
export NPROCS=1
%make_build

pushd libraries/liblutil
rm -f libldif.la
MOD_LIBS="-L../liblber/.libs/ -L../libldap/.libs/ -llber -lldap" make
popd

%if_enabled doc
# Build Administrator Guide in html and text mode
pushd doc/guide/admin
sdf -2topics index.sdf
sdf -2txt guide.sdf
popd
%endif

%check
%make_build test

%install

%make DESTDIR=%buildroot install

###
## Install all slapd's file
###

# Create the /var/lib data directory and chroot enviroment.
mkdir -p -m750 %buildroot%ldap_dir
#__mkdir_p -m750 %buildroot%ldap_dir/bases
mkdir -p -m770 %buildroot%ldap_dir/dblogs
#__mkdir_p -m750 %buildroot%ldap_dir/replica
mkdir -p -m755 %buildroot%ldap_dir/dev
mkdir -p -m750 %buildroot%ldap_dir/%_sysconfdir/ssl
mkdir -p -m750 %buildroot%ldap_dir/%_sysconfdir/schema
ln -s . %buildroot%ldap_dir/%_sysconfdir/%_bname
mkdir -p -m775 %buildroot%ldap_dir/lib
ln -s lib %buildroot%ldap_dir/lib64
mkdir -p -m755 %buildroot%ldap_dir/usr/lib/%_bname
mkdir -p -m755 %buildroot%ldap_dir/usr/lib/sasl2
ln -s lib %buildroot%ldap_dir/usr/lib64
mkdir -p -m775 %buildroot%ldap_dir/var/run
mkdir -p -m775 %buildroot%ldap_dir%ldap_dir
ln -s ../../../bases %buildroot%ldap_dir%ldap_dir/
ln -s ../../../dblogs %buildroot%ldap_dir%ldap_dir/
mksock %buildroot%ldap_dir/dev/log

# Install init scripts.
install -pD -m644 %SOURCE11 %buildroot/%_sysconfdir/sysconfig/ldap
install -pD -m755 %SOURCE12 %buildroot/%_initdir/slapd
mkdir -p -m750 %buildroot/%_sysconfdir/chroot.d
install -pD -m750 %SOURCE15 %buildroot/%_sysconfdir/chroot.d/ldap.all
install -pD -m750 %SOURCE16 %buildroot/%_sysconfdir/chroot.d/ldap.conf
install -pD -m750 %SOURCE17 %buildroot/%_sysconfdir/chroot.d/ldap.lib
install -pD -m644 %SOURCE14 %buildroot/%systemd_unitdir/slapd.service

# Install OLC (cn=config) directory backup/restore scripts
install -pD -m750 %SOURCE40 %buildroot%_sbindir/slapd-olc-backup
install -pD -m750 %SOURCE41 %buildroot%_sbindir/slapd-olc-restore

# log repository and logrotate config
#__mkdir_p -m750 %buildroot/%_logdir/ldap
#__install -pD -m644 %SOURCE13 %buildroot/%_sysconfdir/logrotate.d/ldap

# syslog.d
mkdir -pm700 %buildroot%_sysconfdir/syslog.d
ln -s %ldap_dir/dev/log %buildroot%_sysconfdir/syslog.d/ldap

# config files
mkdir -p -m750 %buildroot/%_sysconfdir/%_bname/ssl
install -pD -m640 %SOURCE18 %buildroot/%_sysconfdir/%_bname/slapd.conf
install -pD -m640 %SOURCE19 %buildroot%ldap_dir/bases/DB_CONFIG
install -pD -m640 %SOURCE20 %buildroot/%_sysconfdir/%_bname/slapd-access.conf
install -pD -m640 %SOURCE21 %buildroot/%_sysconfdir/%_bname/slapd-mdb-db01.conf
install -pD -m640 %SOURCE22 %buildroot/%_sysconfdir/%_bname/slapd-hdb-db01.conf
install -pD -m640 %SOURCE23 %buildroot/%_sysconfdir/%_bname/slapd-hdb-db02.conf
install -pD -m644 %SOURCE51 %buildroot/%_sysconfdir/%_bname/rootdse.ldif

# We don't need the default files - let's move it.
mkdir -p %buildroot/%_docdir/%_bname-servers-%version/default
mv %buildroot/%_sysconfdir/%_bname/*.default \
	%buildroot/%_docdir/%_bname-servers-%version/default/
mv %buildroot/%_sysconfdir/%_bname/*.example \
	%buildroot/%_docdir/%_bname-servers-%version/
rm -f %buildroot%ldap_dir/bases/*.example

# Documentations for servers
mkdir -p %buildroot/%_docdir/%_bname-servers-%version/{back-{null,perl,sql},schema,slapi,overlays}/
install -D -m644 servers/slapd/back-ldap/TODO.proxy \
	%buildroot/%_docdir/%_bname-servers-%version/back-ldap/TODO.proxy
install -D -m644 servers/slapd/back-monitor/README \
	%buildroot/%_docdir/%_bname-servers-%version/back-monitor/README
install -D -m644 servers/slapd/back-null/README \
	%buildroot/%_docdir/%_bname-servers-%version/back-null/README
%if_enabled perl
install -D -m644 servers/slapd/back-perl/{README,SampleLDAP.pm} \
	%buildroot/%_docdir/%_bname-servers-%version/back-perl/
%endif
%if_enabled shell
install -D -m644 servers/slapd/back-shell/searchexample.{conf,sh} \
	%buildroot/%_docdir/%_bname-servers-%version/back-shell/
%endif

%if_enabled sql
install -D -m644 servers/slapd/back-sql/docs/* \
	%buildroot/%_docdir/%_bname-servers-%version/back-sql/
cp -r servers/slapd/back-sql/rdbms_depend \
	%buildroot/%_docdir/%_bname-servers-%version/back-sql/
%endif

%if_enabled slapi
install -pD -m644 servers/slapd/slapi/TODO \
        %buildroot/%_docdir/%_bname-servers-%version/slapi/TODO
%endif

%if_enabled overlay
install -pD -m644 servers/slapd/overlays/README \
        %buildroot/%_docdir/%_bname-servers-%version/overlays/README
install -pD -m644 servers/slapd/overlays/slapover.txt \
        %buildroot/%_docdir/%_bname-servers-%version/overlays/slapover.txt
%endif

install -p -m644 servers/slapd/schema/README \
	%buildroot/%_docdir/%_bname-servers-%version/schema/README
##slapd
install -p -m644 %SOURCE3 \
	%buildroot/%_docdir/%_bname-servers-%version/README.ALT
install -p -m644 %SOURCE4 \
	%buildroot/%_docdir/%_bname-servers-%version/config-README.ALT

%if_enabled doc
## Install Administration Guide 
mkdir -p %buildroot/%_docdir/%_bname-doc-%version/images
install -pD -m644 doc/guide/images/*.gif \
	%buildroot/%_docdir/%_bname-doc-%version/images
mkdir -p %buildroot/%_docdir/%_bname-doc-%version/admin-guide
#install -pD -m644 doc/guide/admin/*.gif \
#	%buildroot/%_docdir/%_bname-doc-%version/admin-guide/
install -pD -m644 doc/guide/admin/*.html \
	%buildroot/%_docdir/%_bname-doc-%version/admin-guide/
install -p -m644 doc/guide/admin/guide.txt \
	%buildroot/%_docdir/%_bname-doc-%version/
%endif

# Purge dependency_libs from .la files.
%__subst -p 's/^\(dependency_libs=\).*/\1'\'\'/ \
	%buildroot/%_libexecdir/%_bname/*.la

#======
# Relocate some shared libraries from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for n in ldap lber; do
	for f in %buildroot/%_libdir/lib$n.so; do
		t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
		[ -n "$t" ]
		ln -s -nf ../../%_lib/"$t" "$f"
	done
    mv %buildroot/%_libdir/lib$n-*.so.* %buildroot/%_lib/
done

%pre servers
# Take care to only do ownership-changing if we're adding the user.
/usr/sbin/groupadd -rf ldap
/usr/sbin/useradd  -rM -c "LDAP User" -g ldap -u 55 -s /dev/null -d %ldap_dir ldap &>/dev/null
if [ -d "$ldap_ssl_dir" -a ! -L "$ldap_ssl_dir" ]; then
	echo "Your certificates are moved to $ldap_ssl_dir.rpmsave, please CHECK!"
	mv "$ldap_ssl_dir" "$ldap_ssl_dir".rpmsave
fi	

%post servers
# remove old libs from chroot
rm -f /var/lib/ldap/%_libdir/openldap/*
rm -f /var/lib/ldap/%_libdir/sasl2/*
rm -f /var/lib/ldap/%_libdir/*.so*
rm -f /var/lib/ldap/%_lib/*.so*

%post_service slapd


%preun servers
%preun_service slapd


%files -n libldap
/%_lib/*.so.*
%_libdir/*.so.*
# libldap/client config
%_man5dir/ldap.conf.*
# the common format
%_man5dir/ldif.*

%files -n libldap-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*
%doc doc/{drafts,rfc,devel}

%files -n libldap-devel-static
%_libdir/*.a

%files
%doc ANNOUNCEMENT CHANGES COPYRIGHT LICENSE README
%dir %_sysconfdir/%_bname
%config(noreplace) %_sysconfdir/%_bname/ldap.conf

%files servers
%_sysconfdir/chroot.d/ldap.all
%_sysconfdir/chroot.d/ldap.conf
%_sysconfdir/chroot.d/ldap.lib
%_sysconfdir/syslog.d/ldap
#config(noreplace) %_sysconfdir/logrotate.d/ldap

%dir %_sysconfdir/%_bname/schema
%_sysconfdir/%_bname/schema
%attr(750,root,ldap) %dir %_sysconfdir/%_bname/ssl

%config(noreplace) %_sysconfdir/%_bname/rootdse.ldif
%attr(-,root,ldap)%config(noreplace) %_sysconfdir/%_bname/slapd-access.conf
%attr(-,root,ldap)%config(noreplace) %_sysconfdir/%_bname/slapd-mdb-db01.conf
%attr(-,root,ldap)%config(noreplace) %_sysconfdir/%_bname/slapd-hdb-db01.conf
%attr(-,root,ldap)%config(noreplace) %_sysconfdir/%_bname/slapd-hdb-db02.conf
%attr(-,root,ldap)%config(noreplace) %_sysconfdir/%_bname/slapd.conf

%_initdir/slapd
%systemd_unitdir/slapd.service
%config(noreplace) %_sysconfdir/sysconfig/ldap

%_sbindir/slapacl
%_sbindir/slapadd
%_sbindir/slapauth
%_sbindir/slapcat
%_sbindir/slapd
%_sbindir/slapdn
%_sbindir/slapindex
%_sbindir/slappasswd
%_sbindir/slaptest
%_sbindir/slapschema
%_sbindir/slapd-olc-backup
%_sbindir/slapd-olc-restore

%_libexecdir/%_bname

%_man5dir/*
%_man8dir/*
# Not server-related file formats:
# libldap/client config
%exclude %_man5dir/ldap.conf.*
# the common format
%exclude %_man5dir/ldif.*

%doc %_docdir/%_bname-servers-%version
#attr(0775,root,ldap) %dir %_logdir/ldap

%attr(0750,root,ldap) %dir %ldap_dir
%attr(1770,root,ldap) %dir %ldap_dir/bases
%attr(0640,root,ldap) %ldap_dir/bases/DB_CONFIG
%attr(1770,root,ldap) %ldap_dir/dblogs
%attr(0775,root,ldap) %ldap_dir/dev
%attr(0755,root,ldap) %ldap_dir/etc
%attr(0750,root,ldap) %ldap_dir/lib
%ldap_dir/lib64
%ldap_dir/usr
%ldap_dir/var
%attr(0775,root,ldap) %dir %ldap_dir/var/run

##### CLIENTS
%files clients
%_bindir/ldapadd
%_bindir/ldapcompare
%_bindir/ldapdelete
%_bindir/ldapmodify
%_bindir/ldapmodrdn
%_bindir/ldappasswd
%_bindir/ldapsearch
%_bindir/ldapwhoami
%_bindir/ldapexop
%_bindir/ldapurl
%_man1dir/*

%if_enabled doc
##### GUIDE
%files -n %_bname-doc
%_docdir/%_bname-doc-%version/*
%dir %_docdir/%_bname-doc-%version/
%endif

###
# TODO for 2.2.x
#
#[global] correct install all docs to %_docdir
#[global] Correct build with SASL(+++) Need tests
#[FR] Translate Admin Guide
#[FR] Translate LDAP Tools and add working in LOCALE Run-Time envirement.
#[FR] Make load modules correctly by dlopen without *.la files
#[global] Copy or not in back-meta/data directory (may be need to copy this data to Docs dir).
#[NeedBugFix] Remove TEXTREL from back-{modules}
#[global] What is back-tcl ?? man is here, but back modules isn't.
#[global] Generate slapd.conf according slapd.conf in source and man pages back-*
#[global] Create new config shema
#[FR] Import, may be, backup shema from MDK
#[global] Work on SSL/TLS cert dir!(+++) Need tests. 
#[FR] Correct patch for aacls for latest version
#[FR] Create separate package with OpenLDAP test for ALT Specific chroot env
#[FR] Create chroot-scripts dynamic while build package 

%changelog
* Fri Oct 04 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.48-alt2
- sasl in chroot fixed

* Wed Aug 28 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.48-alt1
- 2.4.48 (Fixes: CVE-2019-13057, CVE-2019-13565)

* Fri Jun 14 2019 Stanislav Levin <slev@altlinux.org> 2.4.47-alt2
- Fixed LDAPI with SASL_NOCANON (RH BZ: #960222).

* Sun Apr 21 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.47-alt1
- 2.4.47

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.4.46-alt1.1
- rebuild with new perl 5.28.1

* Wed Aug 29 2018 Alexey Shabalin <shaba@altlinux.org> 2.4.46-alt1
- 2.4.46
- build with openssl-1.1
- build without tcp_wrappers

* Thu Jul  5 2018 Leonid Krivoshein <klark@altlinux.org> 2.4.45-alt5
- /etc/sysconfig/ldap: use SLAPD_BACKEND= for ldap-dn create calls.

* Thu Jan 18 2018 Stanislav Levin <slev@altlinux.org> 2.4.45-alt4
- fix default value of TLS_REQCERT (NEVER -> DEMAND) in ldap.conf
  accoding to upstream. Some of applications expect to use the default
  DEMAND behavior.

* Tue Dec 19 2017 Leonid Krivoshein <klark@altlinux.org> 2.4.45-alt3
- added support OLC (cn=config or /etc/openldap/slapd.d);
- added backup/restore scripts for slapd.d directory;
- now used mdb backend by default.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.45-alt2.1
- rebuild with new perl 5.26.1

* Tue Oct 24 2017 Dmitry V. Levin <ldv@altlinux.org> 2.4.45-alt2
- slapd:
  + dropped bogus chown from %%pre script;
  + fixed ldapi:/// (closes: #34023).

* Mon Sep 11 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.45-alt1
- updated to 2.4.45 (Fixes: CVE-2017-9287)

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.42-alt4.1
- rebuild with new perl 5.24.1

* Wed Aug 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.42-alt4
- general libldap manpages moved out of %name-servers (ALT#32385).

* Wed Jun 08 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.42-alt3
- ssl keys generation added to service file

* Fri Jun 03 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.4.42-alt2
- support for multiple LDAP URLs in systemd service

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.42-alt1.1
- rebuild with new perl 5.22.0

* Wed Sep 30 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.4.42-alt1
- updated to 2.4.42
- obsolete patches removed
- CVE-2015-6908 fixed

* Mon Jun 01 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.4.32-alt2.1.1.1
- build with gcc 5.1 fixed

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.32-alt2.1.1
- rebuild with new perl 5.20.1

* Thu Oct 31 2013 Sergey Y. Afonin <asy@altlinux.ru> 2.4.32-alt2.1
- NMU: rebuilt with cyrus-sasl 2.1.26 (ALT #29485)

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.4.32-alt2
- built for perl 5.18

* Thu Sep 13 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.4.32-alt1
- 2.4.32

* Mon Sep 10 2012 Alexey Shabalin <shaba@altlinux.ru> 2.4.31-alt7
- fix files for libldap on i586 (ALT #27713)

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.4.31-alt6
- rebuilt for perl-5.16

* Sat Jun 30 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.31-alt5
- update rh patches
- CVE-2012-2668

* Wed May 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.31-alt4
- remove TimeoutSec from unit file

* Mon May 14 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.31-alt3
- fix systemd unit file

* Fri May 04 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.31-alt2
- add systemd unit file
- rename to openldap

* Wed Apr 25 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.31-alt1
- 2.4.31

* Tue Mar 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.30-alt1
- 2.4.30 with Fedora patches

* Wed Feb 15 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.29-alt1
- 2.4.29

* Thu Dec 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.28-alt1
- 2.4.28 with Fedora patches

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 2.4.26-alt1.1
- rebuilt for perl-5.14

* Tue Aug 02 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.26-alt1
- 2.4.26 with Fedora patches

* Mon Mar 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.25-alt1
- 2.4.25 with Fedora patches
- enable ipv6 (ALT #25829)

* Fri Mar 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.24-alt5
- add libgcc_s.so.1 to chroot (ALT #25280)

* Fri Mar 18 2011 Alexey Tourbin <at@altlinux.ru> 2.4.24-alt4
- libldap-devel: removed dependencies on libopenslp-devel libsasl2-devel

* Tue Mar 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.24-alt3
- disable samba3 schema by default (ALT #25153)

* Wed Feb 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.24-alt2
- openldap-2.4.24-rh-export-ldif.patch

* Sun Feb 13 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.24-alt1
- 2.4.24

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.4.23-alt3.1
- rebuilt with perl 5.12

* Wed Oct 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.23-alt3
- Automate figureing out required libs in chroot

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 2.4.23-alt2
- Rebuilt with libcrypto.so.10.

* Wed Jun 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.23-alt1
- 2.4.23
- security fixes: CVE-2010-0212 and CVE-2010-0211

* Wed May 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.22-alt1
- 2.4.22

* Tue Mar 09 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.21-alt1
- 2.4.21
- strcpy-memcpy patch to fix fraud overflow

* Mon Nov 09 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.19-alt1
- new upstream version

* Tue Aug 18 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt4.4
- fixed Provides from %%_bname to %%_bname = %%version-%%release

* Mon Aug 17 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt4.3
- corrected openldap version provides (thanks ldv)

* Mon Aug 17 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt4.2
- enabled test

* Mon Aug 17 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt4.1
- simple fixes around openldap package

* Mon Aug 03 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt4
- added suffix '2.4' for packages
- deleted database auto migration
- removed lib*2.3 provides

* Thu Jul 09 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt3
- renamed backup dir from .rpmorig to .rpmsave
- added symlink for libldap_r-2.3.so.0

* Tue Jun 30 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt2.2
- installation fix 

* Tue Jun 30 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt2.1
- fixed x86_64 compat lib support

* Mon Jun 29 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt2
- added database automigration from 2.3 to 2.4

* Tue Jun 02 2009 Lebedev Sergey <barabashka@altlinux.org> 2.4.16-alt1
- new upstream version 2.4.16
- removed ldbm backend
- removed slurpd daemon
- fixed configure options
- fixed default config
- disabled openldap-2.3.34-alt-meta-backend.patch
- fixed #20271 #20392

* Mon May 18 2009 Dmitry V. Levin <ldv@altlinux.org> 2.3.43-alt2.2
- NMU.
- Backported upstream build fixes with fresh toolchain (closes: #20035).
- Rebuilt slapd with libsasl2-2.1.24-alt1.cvs.20090508 (closes: #20036).
- Packaged openldap-doc as noarch package.

* Sat May 02 2009 Alexey I. Froloff <raorn@altlinux.org> 2.3.43-alt2.1
- NMU (closes: #19714):
  + Use cert-sh-functions for SSL cerificate generation
  + Point TLS* option examples to /var/lib/ssl/
  + Copy public certificates and slapd.key to chroot

* Fri Dec 12 2008 OpenLDAP Maintainers Team <eostapets@altlinux.org> 2.3.43-alt2
- fix build with new glibc-kernheaders

* Mon Aug 11 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.43-alt1
- 2.3.43

* Wed Jul 02 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.41-alt2
- fix for CVE-2008-2952 (patch from OpenLDAP CVS)
- set more specific BuildRequires:
  + libdb4.4-devel

* Mon Feb 25 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.41-alt1
- 2.3.41
  + fix for CVE-2008-0658 (#14431)

* Mon Oct 29 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.39-alt1
- 2.3.39
- #8241 add support for GSSAPI to slapd chroot

* Thu Oct 11 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.38-alt1
- 2.3.38
- change default syslog facility/level to daemon/info (/etc/sysconfig/ldap)
- remove /var/log/ldap and /etc/logrotate.d/ldap from package
- #11097 move administrator's guide to openldap-doc-x.xx.x/admin-guid
- #11101 add logo files to doc package
- #11861 config-README.ALT and /etc/chroot.d/ldap.conf fixed
- fix slapd init-script:
  + altranative fix for #11879 -- add -u to slaptest;
  + add '--expect-user ldap' to start_daemon parameters

* Wed Aug 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.37-alt1
- 2.3.37
- update samba3.schema from samba-3.0.25-alt1
- bugs fixed (bugzilla.altlinux.org):
  - #11426 add NTLM support
  - #11879 chroot directory owner

* Wed Apr 18 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.35-alt0
- 2.3.35

* Sun Mar 04 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.34-alt1
- additional .schema files:
  + updated courier.schema
  + new freeradius.schema

* Thu Feb 22 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.34-alt1
- 2.3.34

* Wed Dec 27 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.31-alt1
- 2.3.31

* Sat Nov 25 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.30-alt1
- 2.3.30

* Mon Oct 30 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.28-alt1
- 2.3.28
- add samba.schema from samba-3.0.23a-alt1
- decrease default in-memory cache size for BDB from 128Mb to 64Mb

* Tue Aug 24 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.27-alt1
- 2.3.27

* Tue Apr 25 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.21-alt1
- 2.3.21
- fix chroot permissions
- misc fixes in the init-scripts and default configs
- disable build of SLAPI library
- slapd:
  + move backend database config into separate files: slapd-hdb-dbNN.conf

* Sat Mar 04 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.20-alt0.1
- rename libldap package to libldap2.3 - soname changed
- spec/scripts fixes for x86_64 build

* Fri Feb 24 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.3.20-alt0
- 2.3.20 with Berkeley DB 4.4.20
- change default backend to HDB (replacement for DBD)
- modify default DB_CONFIG
- misc fixes in chroot.d/* scripts

* Thu Nov 24 2005 Nick S. Grechukh <gns@altlinux.org> 2.3.12-alt3
- update to new version. fixed patches 8,9,20

* Sun Sep 04 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.28-alt1
- Update to new version 2.2.28

* Tue Jun 28 2005 Anton D. Kachalov <mouse@altlinux.org> 2.2.27-alt1.1
- Build with gcc3.4
- Eliminated TEXTRELs
- x86_64 support

* Sun Jun 19 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.27-alt1
- Update to new version 2.2.27
- Fix slapd.conf bug (alt bugzilla #)

* Sun May 01 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.26-alt1
- Update to new version 2.2.26
- Update openldap-ldap.lib for FIX bug #6284 (bugzilla.altlinux.ru)

* Fri Apr 29 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.25-alt1
- Update to new version 2.2.25
- Update Fix bug #6284 (bugzilla.altlinux.ru)

* Sat Mar 26 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.24-alt1
- Update to new version 2.2.24 
- Disable test by dafault
- Fix bug #6284 (bugzilla.altlinux.ru)
- Update openldap-README.ALT (NOW LDBM by DEFALUT!!!)

* Mon Feb 14 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.23-alt2
- Rebuild with libdb-4.3
- Set GCC version to 3.3 (becouse back_bdb not work)
- Update chroot scripts (Fix bug #6132 [bugzilla.altlinux.ru])
- Add dir /var/lib/ldap/usr/lib/sasl2 for sasl2 libs

* Fri Jan 28 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.23-alt1
- Update to new stable release 2.2.23
- Disable aacls (need patch coorections)

* Mon Jan 24 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.22-alt2
- Add AACLS patch from aacls.sf.net

* Mon Jan 24 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.22-alt1
- Update to new version 2.2.22 (bugfix release)
- FIX bug in initscript (slapd)
- Remove patch10 %name-2.2.18-configure.in-back-bdb-mod-compile.patch now in HEAD

* Sun Jan 02 2005 Serge A. Volkov <vserge at altlinux.ru> 2.2.20-alt1
- Update to new version 2.2.20
- Add openldap-bdb-DB_CONFIG from MDK for back_bdb (BerkeleyDB options)
- Add openldap-config-README.ALT - TODO configurations files structures
- Add openldap-slapd-access.conf - default slapd.access.conf from MDK
- Spec cleanup
- $ldap_ssl_dir move to pre_servers sections. Now create while install/update package (Need test!)
- Update openldap-slapd.init
- Update ldap.conf (made no verbose)

* Sun Dec 12 2004 Serge A. Volkov <vserge at altlinux.ru> 2.2.19-alt2
- Update Admin Guide from CVS (tag OPENLDAP_REL_ENG_2_2)

* Tue Dec 07 2004 Serge A. Volkov <vserge at altlinux.ru> 2.2.19-alt1
- Update to new version 2.2.19
- Update README.ALT
- Correct slapd.conf

* Sat Dec 04 2004 Serge A. Volkov <vserge at altlinux.ru> 2.2.18-alt6
- FIX back-bdb build dynamic (openldap-2.2.18-configure.in-back-bdb-mod-compile.patch)

* Wed Dec 01 2004 Serge A. Volkov <vserge at altlinux.ru> 2.2.18-alt5
- FIX libs soft linking to /lib from /usr/lib (path by ldv)
- Add %%def_enable ldbm
- FIX upgrade ssl dirs, move old certs to rpmsave dir
- Update README.ALT ( info about back-bdb - It's build static)

* Thu Nov 25 2004 Serge A. Volkov <vserge at altlinux.ru> 2.2.18-alt4
- Bugfixs (buzilla.altlinux.ru):
  - #5558 - copiing schemas to chroot env
  - #5566 - update openldap-slapd.init, check compilations of module bdb
  - #4820 - update chroot env: ldap.conf replace /etc/openldap/ssl by soft link to /var/lib/ssl/certs
  - #5574 - add example

* Thu Nov 11 2004 Serge A. Volkov <vserge at altlinux.ru> 2.2.18-alt3
- FIX libldap-devel: link of /usr/lib/libldap.so

* Sat Oct 30 2004 Serge A. Volkov <vserge at altlinux.ru> 2.2.18-alt2
- SPEC cleanup
- Add NPROCS=1 for correct build on SMP system

* Wed Oct 27 2004 Serge A. Volkov <vserge@altlinux.org> 2.2.18-alt1
- Update to new version 2.2.18
- Remove
  - CPPFLAGS -DNEW_LOGGING=1
  - SOURCE2 = openldap-README.upgrading
- Enable old CPPFLAGS
- FIXED bugs (Bugzilla at altlinux.ru)
  - #4968 update openldap.sysconfig file
  - #5332 update openldap-README.ALT and openldap-slapd.conf
  - #5142 update openldap-slapd.conf

* Mon Oct 11 2004 Serge A. Volkov <vserge@altlinux.org> 2.2.17-alt2
- FIX creating soft link to libs liblber and libldap 

* Sat Oct 01 2004 Serge A. Volkov <vserge@altlinux.org> 2.2.17-alt1
- Update to new version

* Thu Aug 05 2004 Serge A. Volkov <vserge@altlinux.org> 2.2.15-alt2
- Add "-DLDAP_CONNECTIONLESS=1 " in CPPFLAGS for samba integration

* Thu Aug 05 2004 Serge A. Volkov <vserge@altlinux.org> 2.2.15-alt1
- Update
  + new version 2.2.15
  + alt-servers-path.patch

* Thu Jul 6 2004 Serge A. Volkov <vserge@altlinux.org> 2.2.14-alt2
- Update
  + ldv libs scripts
  + openldap-slapd.init script
  + spec cleanup: docs installation scripts

* Sun Jul 1 2004 Serge A. Volkov <vserge@altlinux.org> 2.2.14-alt1
- Spec cleanup
- Update
  + to new version 2.2.14
  + patch9 for fix location of slapd and slurpd 
  + OLAG from CVS
  + patch19 %name-2.2.14-alt-pid.patch
  + qmail.shema from qmail-ldap.org (Thanks Konstantin Klimchev)
- Remove patches, becose it's applied to the HEAD
  - Patch22: %name-perl-PLD.patch
  - Patch15: %name-ALT-OLAG.patch
  - Patch17: %name-mark-benson-030616.patch
  - disable krb!!! 
- Add
  + -DLOG_DAEMON=1 for log to syslog as a DAEMON
  + shtoolize (Update to new version of shtool scripts)
  + configure options for slp, slapi, overlay, back_hdb, back_dnssrv, wrappers
  + try to strip TEXTREL from modules
  + RPM package options set_verify_elf_method textrel=relaxed
    and add_verify_elf_skiplist %%buildroot/%%_libdir/%%name/* for package modules 
  + Require: libopenslp for %name-servers package

* Sun May 16 2004 Igor Muratov <migor@altlinux.org> 2.1.30-alt3
- Move shared libraries to /lib again

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.30-alt2.1
- Rebuilt with openssl-0.9.7d.

* Mon Apr 26 2004 Igor Muratov <migor@altlinux.org> 2.1.30-alt2
- Fix slapd config
- Fix logrotate config
- Fix preinstall script
- Fix chroot script
- Fix file permissions
- Replace dns.schema by dnszone.schema

* Wed Apr 21 2004 Igor Muratov <migor@altlinux.org> 2.1.30-alt1
- Remove old patches and unused sources
- Remove gencert.sh Use openssl script instead
- Patch slurpd to change uid/gid and root directory
- Move slapd and slurpd to chroot
- Fix for execution privileges. Switch to ldap user

* Tue Feb 17 2004 Alexander Bokovoy <ab@altlinux.ru> 2.1.26-alt3.1
- Rebuild against libkrb5-1.3.1-alt3

* Fri Feb 13 2004  Serge A. Volkov <vserge@altlinux.ru> 2.1.26-alt3
- Add patches from CVS:
  + openldap-2.1.26-CVS-cyrus.c.patch
  + openldap-2.1.26-CVS-265-connections.c.patch not installed
  + openldap-2.1.26-CVS-266-connections.c.patch not installed

* Sat Jan 31 2004  Serge A. Volkov <vserge@altlinux.ru> 2.1.26-alt2
- Update to new version 2.1.26
- Merge pathes from PLD

* Wed Dec 10 2003  Serge A. Volkov <vserge@altlinux.ru> 2.1.25-alt1
- Update to new version 2.1.25

* Wed Dec 10 2003  Serge A. Volkov <vserge@altlinux.ru> 2.1.24-alt2
- Add configure options --disable-ltdl
- Fix permission on files *.txt in libldap-devel

* Fri Dec 05 2003 Serge A. Volkov <vserge@altlinux.ru> 2.1.24-alt1
- Update to version 2.1.24 
- Remove Patch21 it's fix in 2.1.24
- Fix some file installations

* Wed Dec 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.1.23-alt3
- libldap-devel: do not package .la files.
- openldap-servers: purge dependency_libs from .la files.

* Thu Oct 16 2003  Serge A. Volkov <vserge@altlinux.ru> 2.1.23-alt2
- Update slapd configfile patch.

* Mon Oct 13 2003  Serge A. Volkov <vserge@altlinux.ru> 2.1.23-alt1
- Update to new version 2.1.23
- Disable sasl
- Remove patch slurpd-pid - now in mainstream
- Correct server package Requires for libsasl2 and linkrb5
- Update slapd.conf patch

* Thu Oct  9 2003  Serge A. Volkov <vserge@altlinux.ru> 2.1.22-alt12
- Add perl build options to spec, but not enabled it

* Wed Oct  8 2003  Serge A. Volkov <vserge@altlinux.ru> 2.1.22-alt11
- Fixed:
  + slurpd pid file creations
- Add:
  + ALT root DSE ldif
- Remove
  + patch11 MDK for sql-backend it's fix in mainstream

* Mon Sep 29 2003 Alexander Bokovoy <ab@altlinux.ru> 2.1.22-alt10
- Fixed:
  + Missed dependency for libldap-devel on libkrb5-devel
  + Makefile target for liblber which prevented the package from build
  + Build dependencies for libtool -- libtool 1.5 is *required*
- Added:
  + SQL backend build is optional now (needed for AW/XScale project)

* Mon Sep 03 2003 Serge A. Volkov <vserge@altlinux.ru> 2.1.22-alt9
- Spec cleanup
- Enable build with Cirus-sasl libs
- Correct Requires for openldap-servers to openssl
- Correct slapd.conf patch

* Wed Sep 03 2003 Alexander Bokovoy <ab@altlinux.ru> 2.1.22-alt8
- fileutils -> coreutils dependency in openldap-servers

* Tue Sep 02 2003 Serge A. Volkov <vserge@altlinux.ru> 2.1.22-alt7
- Added by Alexander Bokovoy <ab@altlinux.ru>:
  + Samba 3.0 schema as samba3.schema
  + Configure options:
    - --with-yielding-select
    - --enable-cleartext
- Fixed by Alexander Bokovoy <ab@altlinux.ru>:
  + Build with autoconf-2.5/automake-1.6 now
  + Do not remove pid file when just doing check of configuration in slapd
- Spec updated by Alexander Bokovoy <ab@altlinux.ru>, all --with moved to enable/disable
- Spec cleanup, update openldap-README.ALT

* Mon Aug 24 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.22-alt6
- Update slapd.conf (%name-ALT-0.8-slapd.conf.patch): add replogfile
- Add dir %%_var/lib/ldap/replica for slurpd
- Update %name.sysconfig: add SLURPDURLLIST

* Mon Aug 24 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.22-alt5
- Replace all addons schemas by one tar file.
- Replace old initscripts "ldap" to new two "slapd" and "slurpd" and update it for Sisyphus
- Update BuildReq
- Update slapd.conf (openldap-ALT-0.7-slapd.conf.patch): add new options and comments

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.1.21-alt4
- Explicitly use old libtool for build.

* Mon Aug 18 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.22-alt3
- Remove %name-conffile.patch, becose with it TLS not work. Thanks Serge Vlasov.

* Sat Jul 19 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.22-alt2
- Add samba3.shema for samba3.0 support
- Rename old samba.schema to samba2.schema
- Add patches:
  - from Dmitry Lebkov for schemas
- Add script from stunnel package for generation ssl certificate
- Update openldap-ALT-slapd.conf.patch for last changes

* Wed Jul 02 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.22-alt1
- Update to version 2.1.22

* Mon Jun 2 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.21-alt1
- Change Release to alt1 for move package from Daedalus to Sisyphus

* Mon Jun 2 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.21-alt0.4
- Add patch for OpenLDAP Admin Guide

* Mon Jun 2 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.21-alt0.3
- Correct Packager:

* Mon Jun 2 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.21-alt0.2
- Correct BuildPreReq: libunixODBC-devel

* Fri May 30 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.21-alt0.1
- Update to new version 2.1.21
- Enable test for ldbm

* Fri May 30 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.20-alt0.2
- Enable back_BDB dynamic
- Add patches:
  - Masato-Taruishi-030326.patch for tests dynamic modules with corrections
  - openldap-2.1.20-ALT-test-dinamic-modules.patch addon for Masato-Taruishi patch
  - update slapd.conf.patch to new version of slapd.conf - see README.ALT
- New version of ldap init script. Update for new version of service-0.3-alt1
- Update README.ALT and rename it to openldap-README.ALT

* Thu May 22 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.20-alt0.1
- Update to version 2.1.20

* Sat May 10 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.19-alt0.2
- Add patch:
  - Masato-Taruishi-030326.patch for tests dynamic modules
  - OLAG.patch - OpenLDAP Administration Guide for correct sdf compilation.
- Docs install cleanup

* Sat May 10 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.19-alt0.1
- Update to new version 2.1.19
- We need fix OpenLDAP ITS#2354 and my new.

* Fri May 09 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.18-alt0.2
- SPEC cleanup and correct e-mail address
- ADD
  - %%If_with {krb,guide,sasl} for future builds
- Build BDB backend by default and make it buildin

* Tue May 06 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.18-alt0.1
- Update to new version 2.1.18

* Mon May 05 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.17-alt0.5
- Reorganize docs structures.

* Sun Apr 13 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.17-alt0.4
- Update initscript
  - Add function check
- Add README.ALT file for log changes which ALT Linux Team will do.
- Update slapd.conf patch
  - Update for version of OpenLDAP 2.1.17
  - Add back_monitor enable by default

* Sat Apr 12 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.17-alt0.3
- Add to CFLAGS="-DNEW_LOGGING=1" for New loggig format!!!

* Sat Apr 06 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.17-alt0.2
- Fix bdb module compile

* Sat Apr 05 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.17-alt0.1
- Update to new version 2.1.17
- Remove slapd.conf patch (we need redesign ALT-slapd.conf)

* Sun Mar 30 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.16-alt0.3
- Correct CFLAGS and LDFLAGS veraibles for build for Sisyphus. This veraibles
now EXPORTs
- Update BuildRequrs

* Mon Mar 24 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.16-alt0.2
- Add LDFLAGS and CPPFLAGS for Sysiphus correct Kerberos detection
- Add configure options:
  --with-kerberos=k5
  --enable-kpasswd

* Sat Mar 15 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.16-alt0.1
- Update to new version 2.1.16
- Rebuild against libdb4.1 and enable DBD backend

* Wed Mar 05 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.14-alt0.1
- Update to new version 2.1.14

* Wed Feb 26 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.13-alt0.1
- Update to new version 2.1.13 (Bugfix release see Changelog)
- Update RH-syslog.patch for v2.1.13
- Rename openldap-2.0.25-configure-tinfo.patch to openldap-2.0.25-ALT-configure-tinfo.patch this is ALT specific
- Remove bdb module becose in sisyphus libdb4 v4.0.14, but need v4.1
- Add Cyrus-SASL 2 support

* Mon Jan 20 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.12-alt2.2
- Add back-glue module
- Change --datadir=%%_datadir/%%name to --datadir=%%_datadir
- Add Attention message. In TODO write script to migrate from old version of OpenLDAP (2.0.27)
- Correct openldap-2.1.3-slapd.conf.patch for OpenLDAP directory bases (/var/lib/ldap/bases)

* Mon Jan 20 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.12-alt2.1
- Add --multimaster (%%configure)
- Remove alt-sasl2.patch, becouse not need with > libsasl2-2.1.10-alt1.2
- Applay recomandation from Alexander Belov <asbel@mail.ru>
  - Updated /usr/share/openldap/gencert.sh
  - Updated man pages (%%_man5dir/slapd*)
  - Include ucdata dir in package openldap-servers (%%_datadir/%%name/ucdata)
  - Add some RH patches:
    - %name-1.2.11-RH-cldap.patch
    - %name-2.1.2-RH-syslog.patch
- Rename %name-2.0.17-shell-backend-Makefile.patch to %name-2.0.17-RH-shell-backend-Makefile.patch
- Rename %name-2.0.7-schema.patch to %name-2.0.7-MDK-schema.patch and reactivate it
- Rename %name-MDK-sql.patch to %name-MDK-sql.patch

* Mon Jan 13 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.12-alt2
- Separate from one srpms support KERBEROS and SASL in diffrent packages
  If you whan to look in openldap-sasl2 and openldap-krb.
- Update BuildReq

* Fri Jan 10 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 2.1.12-alt1.1
- Updated BuildRequires

* Thu Jan 09 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.12-alt1
- Update to new release openldap-2.1.12
- Rebuild against libsasl2-2.1.10-alt1.2

* Tue Jan 07 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.11-alt2
- Enable SASL2 support
- Add patch for configure sasl2 alt-specific patch (%_includedir/sasl2/*)
- Add script by Dmitry Levin find and replace for support libsasl2
  - in source files for "#include <sasl/sasl.h>" -> "#include <sasl2/sasl.h>"
  - in source files for "#ifdef HAVE_SASL_SASL_H" -> "#ifdef HAVE_SASL2_SASL_H"

* Sat Jan 04 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.11-alt1
- Update to new version 2.1.11
- Update OpenLDAP Administration Guide for 2.1 but not ganarate HTML files
- Update BuildReq

* Fri Jan 03 2003 Serge A. Volkov <vserge at altlinux dot ru> 2.1.10-alt1
- Update to new version 2.1.10
- Add debug info to standart build
- Spec cleanup
  - Create veriables for configure script COMMONFLAGS and MODULESFLAGS
  - Add veriables krb and sasl for make same packages (see doc about %%if_with)
- Remove from build two backends, becose not compile in TODO now
  - perl
  - sql

* Sun Dec 22 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.1.9-alt2
- Create different packages for SASL and Kerberos, but SASL package in work.
- Kerberos NOT Work. Need do like in postfix package.

* Sun Dec 22 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.1.9-alt1
- Update to version 2.1.9
- Add Kerberos 5 support buildin.

* Thu Oct 31 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.1.8-alt1
- Update for version 2.1.8
- Add BuildRequires: libunixODBC-devel-static
- Add dpendensise for automake_1.4 and autoconf_2.13
- Spec cleanup
  - remove install old files (ud programm)
- Remove SQL-backend module not compile -- in TODO

* Tue Aug 2 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.1.3-alt1
- First release for version 2.1.x
- Remove files in man see CHANGELOG

* Tue Jul 09 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.0.25-alt3
- Update for use terminfo with "ud" program
  - patch for configure (libtinfo)

* Wed Jun 26 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.0.25-alt2
- Add schemas from MDK %name package
  - cron.schema
  - netscape-profile.schema
  - qmailControl.schema
  - trust.schema
  - turbo.schema
  - dns.schema
- Update schemas
  - samba.schema
  - kerberosobject.schema
- schema rfc822-MailMember.schema come back to package but by default is off
- Update guide: in root guide in html by chapter and archive with sdf files
- Update patch for slapd.conf
- Fix bugs #??? according bugs.altlinux.ru

* Thu Jun 13 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.0.25-alt1
- Update to release 2.0.25
- Add courier.schema from courier-imap
- Correct Requires for libunixODBC-devel need for back-sql

* Wed Apr 17 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.23-alt4
- Dropped useless compatibility symlinks.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.23-alt3
- Relocated lib{ldap,lber}.so.* from %_libdir/ to lib/
  (compatibility symlinks created).
- openldap: requires MTA.
- Build with libdb4, updated buildrequires.

* Thu Mar 21 2002 Dmitry V. Levin <ldv@altlinux.org> 2.0.23-alt2
- libldap: Conflicts: %name < %%version-%%release.
- openldap: PreReq: libldap = %%version-%%release.

* Tue Feb 19 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.0.23-alt1
- Update to 2.0.23 stable release
- Update openldap-guide last CVS version

* Wed Jan 16 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.0.21-alt1
- Update to 2.0.21 stable release

* Tue Jan 15 2002 Serge A. Volkov <vserge at altlinux dot ru> 2.0.20-alt1
- Update to 2.0.20

* Mon Jan 14 2002 Serga A. Volkov <vserge at altlinux dot ru> 2.0.19-alt1head
- Compile the CVS repository
- Add configure options:
  --with-phonetic; --enable-aci; --enable-dynamic; --enable-slurpd

* Fri Dec 21 2001 Serge A. Volkov <vserge at altlinux dot ru> 2.0.19-alt1
- Update to 2.0.19 release
- Cleanup spec

* Tue Dec 14 2001 Serge A. Volkov <vserge at altlinux dot ru> 2.0.18-alt2
- Removed "reload" function in initscript
- Update slapd.conf
- added script for corretion syslog.conf

* Fri Oct 26 2001 Serge	A. Volkov <vserge at altlinux dot ru> 2.0.18-alt1
- Update to 2.0.18

* Wed Oct 25 2001 Serge A. Volkov <vserge at altlinux dot ru> 2.0.17-alt3
- Clean up spec
- Correced slapd.conf patch

* Mon Oct 22 2001 Serge A. Volkov <vserge@altlinux,ru> 2.0.17-alt2
- Fixed compile problem patch by Peter Marshall

* Tue Oct 16 2001 Serge A. Volkov <vserge at altlinux dot ru> 2.0.17-alt1
- Fixed "export ac_cv_func_getaddrinfo=no" hack.
- Updated:
  - to release 2.0.17
  - OpenLDAP Guide last cvs

* Thu Sep 27 2001 Igor Muratov <migor@altlinux.ru> 2.0.15-alt2
- Set TLS to OpenSSL

* Fri Sep 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.0.15-alt2
- Specfile cleanup.
- Built with db3-3.3.11.

* Fri Sep 21 2001 Volkov A. Serge <vserge@hotbox.ru> 2.0.15-alt1
- Update to 2.0.15 release.

* Tue Sep 10 2001 Volkov A.Serge <vserge@hotbox.ru> 2.0.14-alt1
- OpenLDAP 2.0.14

* Mon Sep 10 2001 Volkov A.Serge <vserge@hotbox.ru> 2.0.13-alt1
- OpenLDAP 2.0.13

* Fri Sep 7 2001 Volkov A. Serge <vserge@hotbox.ru> 2.0.12-alt2
- Remove from this package Migration Tools package.

* Mon Sep 3 2001 Volkov A. Serge <vserge@hotbox.ru> 2.0.12-alt1
- New release 2.0.12. Add patch for not use getaddrinfo function in sources, becose it's core dumped all soft.
  Remove Red-Hat patch for 2.0.3 version, it's conflict with new sources.

* Mon Aug 6 2001 Volkov A. Serge <vserge@menatepspb.msk.ru> 2.0.11-alt1
- Clean some errors in spec. Remove the major variable it's not need in Sysiphus.

* Fri Aug 3 2001 Volkov A. Serge <vserge@menatepspb.msk.ru> 2.0.11-alt1
- Devide 4 packeges to 7 packeges. Add Guide as package. Made libldap2-static and devel.

* Wed Jul 3 2001 Volkov A. Serge <vserge@menatepspb.msk.ru> 2.0.11-alt1
- OpenLDAP 2.0.11 and Migration tool 38. It's my first redation. I look the spec file from Mandrake Linux.

* Thu May 3 2001 Rider <rider@altlinux.ru> 2.0.7-ipl4
- Migration tool 37

* Tue Apr 17 2001 Alexander Bokovoy <ab@avilink.net> 2.0.7-ipl3
- Broken ldap.init script fixed

* Thu Mar 15 2001 Dmitry V. Levin <ldv@fandra.org> 2.0.7-ipl2
- missing link to libresolv.so added

* Sun Jan 28 2001 Dmitry V. Levin <ldv@fandra.org> 2.0.7-ipl1
- RE adaptions.

* Fri Dec 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- change automount object OID from 1.3.6.1.1.1.2.9 to 1.3.6.1.1.1.2.13,
  per mail from the ldap-nis mailing list

* Tue Dec  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- force -fPIC so that shared libraries don't fall over

* Mon Dec  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- add Norbert Klasen's patch (via Del) to fix searches using ldaps URLs
  (OpenLDAP ITS #889)
- add "-h ldaps:///" to server init when TLS is enabled, in order to support
  ldaps in addition to the regular STARTTLS (suggested by Del)

* Mon Nov 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- correct mismatched-dn-cn bug in migrate_automount.pl

* Mon Nov 20 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to the correct OIDs for automount and automountInformation
- add notes on upgrading

* Tue Nov  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.0.7
- drop chdir patch (went mainstream)

* Thu Nov  2 2000 Nalin Dahyabhai <nalin@redhat.com>
- change automount object classes from auxiliary to structural

* Tue Oct 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to Migration Tools 27
- change the sense of the last simple patch

* Wed Oct 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- reorganize the patch list to separate MigrationTools and OpenLDAP patches
- switch to Luke Howard's rfc822MailMember schema instead of the aliases.schema
- configure slapd to run as the non-root user "ldap" (#19370)
- chdir() before chroot() (we don't use chroot, though) (#19369)
- disable saving of the pid file because the parent thread which saves it and
  the child thread which listens have different pids

* Wed Oct 11 2000 Nalin Dahyabhai <nalin@redhat.com>
- add missing required attributes to conversion scripts to comply with schema
- add schema for mail aliases, autofs, and kerberosSecurityObject rooted in
  our own OID tree to define attributes and classes migration scripts expect
- tweak automounter migration script

* Mon Oct  9 2000 Nalin Dahyabhai <nalin@redhat.com>
- try adding the suffix first when doing online migrations
- force ldapadd to use simple authentication in migration scripts
- add indexing of a few attributes to the default configuration
- add commented-out section on using TLS to default configuration

* Thu Oct  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.0.6
- add buildprereq on cyrus-sasl-devel, krb5-devel, openssl-devel
- take the -s flag off of slapadd invocations in migration tools
- add the cosine.schema to the default server config, needed by inetorgperson

* Wed Oct  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- add the nis.schema and inetorgperson.schema to the default server config
- make ldapadd a hard link to ldapmodify because they're identical binaries

* Fri Sep 22 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.0.4

* Fri Sep 15 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove prereq on /etc/init.d (#17531)
- update to 2.0.3
- add saucer to the included clients

* Wed Sep  6 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.0.1

* Fri Sep  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 2.0.0
- patch to build against MIT Kerberos 1.1 and later instead of 1.0.x

* Tue Aug 22 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove that pesky default password
- change "Copyright:" to "License:"

* Sun Aug 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- adjust permissions in files lists
- move libexecdir from %prefix/sbin to %_sbindir

* Fri Aug 11 2000 Nalin Dahyabhai <nalin@redhat.com>
- add migrate_automount.pl to the migration scripts set

* Tue Aug  8 2000 Nalin Dahyabhai <nalin@redhat.com>
- build a semistatic slurpd with threads, everything else without
- disable reverse lookups, per email on OpenLDAP mailing lists
- make sure the execute bits are set on the shared libraries

* Mon Jul 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- change logging facility used from local4 to daemon (#11047)

* Thu Jul 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- split off clients and servers to shrink down the package and remove the
  base package's dependency on Perl
- make certain that the binaries have sane permissions

* Mon Jul 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- move the init script back

* Thu Jul 13 2000 Nalin Dahyabhai <nalin@redhat.com>
- tweak the init script to only source /etc/sysconfig/network if it's found

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- switch to gdbm; I'm getting off the db merry-go-round
- tweak the init script some more
- add instdir to @INC in migration scripts

* Thu Jul  6 2000 Nalin Dahyabhai <nalin@redhat.com>
- tweak init script to return error codes properly
- change initscripts dependency to one on /etc/init.d

* Tue Jul  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- prereq initscripts
- make migration scripts use mktemp

* Tue Jun 27 2000 Nalin Dahyabhai <nalin@redhat.com>
- do condrestart in post and stop in preun
- move init script to /etc/init.d

* Fri Jun 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.2.11
- add condrestart logic to init script
- munge migration scripts so that you don't have to be
  /usr/share/openldap/migration to run them
- add code to create pid files in /var/run

* Mon Jun  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- FHS tweaks
- fix for compiling with libdb2

* Thu May  4 2000 Bill Nottingham <notting@redhat.com>
- minor tweak so it builds on ia64

* Wed May  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- more minimalistic fix for bug #11111 after consultation with OpenLDAP team
- backport replacement for the ldapuser patch

* Tue May  2 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix segfaults from queries with commas in them in in.xfingerd (bug #11111)

* Tue Apr 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.2.10
- add revamped version of patch from kos@bastard.net to allow execution as
  any non-root user
- remove test suite from %build because of weirdness in the build system

* Wed Apr 12 2000 Nalin Dahyabhai <nalin@redhat.com>
- move the defaults for databases and whatnot to /var/lib/ldap (bug #10714)
- fix some possible string-handling problems

* Mon Feb 14 2000 Bill Nottingham <notting@redhat.com>
- start earlier, stop later.

* Thu Feb  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- auto rebuild in new environment (release 4)

* Tue Feb  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- add -D_REENTRANT to make threaded stuff more stable, even though it looks
  like the sources define it, too
- mark *.ph files in migration tools as config files

* Fri Jan 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.2.9

* Mon Sep 13 1999 Bill Nottingham <notting@redhat.com>
- strip files

* Sat Sep 11 1999 Bill Nottingham <notting@redhat.com>
- update to 1.2.7
- fix some bugs from bugzilla (#4885, #4887, #4888, #4967)
- take include files out of base package

* Fri Aug 27 1999 Jeff Johnson <jbj@redhat.com>
- missing ;; in init script reload) (#4734).

* Tue Aug 24 1999 Cristian Gafton <gafton@redhat.com>
- move stuff from /usr/libexec to /usr/sbin
- relocate config dirs to /etc/openldap

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Wed Aug 11 1999 Cristian Gafton <gafton@redhat.com>
- add the migration tools to the package

* Fri Aug 06 1999 Cristian Gafton <gafton@redhat.com>
- upgrade to 1.2.6
- add rc.d script
- split -devel package

* Sun Feb 07 1999 Preston Brown <pbrown@redhat.com>
- upgrade to latest stable (1.1.4), it now uses configure macro.

* Fri Jan 15 1999 Bill Nottingham <notting@redhat.com>
- build on arm, glibc2.1

* Wed Oct 28 1998 Preston Brown <pbrown@redhat.com>
- initial cut.
- patches for signal handling on the alpha

