
%def_without bootstrap
%def_with doc
%def_with ldap
%def_with selinux
%def_with verto
%def_enable check

Name: krb5
Version: 1.17.1
Release: alt1

%if_without bootstrap
%if_with doc
%define _unpackaged_files_terminate_build 1
%endif
%endif

%define _docdir %_defaultdocdir/%name-%version

Summary: The Kerberos network authentication system
License: MIT
Group: System/Libraries
Url: http://web.mit.edu/kerberos/www/

Source0: %name-%version.tar
Source2: %name-alt.tar

# Tex style for new sphinx pdf builder
Source11: ltxcmds.sty

# Carry this locally until it's available in a packaged form.
Source100: noport.c

# fedora patches:
Patch6: krb5-1.12-fedora-ksu-path.patch
Patch12: krb5-1.12-fedora-ktany.patch
Patch23: krb5-1.3.1-fedora-dns.patch
Patch39: krb5-1.12-fedora-api.patch
Patch60: krb5-1.12.1-fedora-pam.patch
Patch63: krb5-1.17-beta1-fedora-selinux-label.patch
Patch71: krb5-1.13-fedora-dirsrv-accountlock.patch
Patch86: krb5-1.9-fedora-debuginfo.patch
Patch129: krb5-1.11-fedora-run_user_0.patch
Patch134: krb5-1.11-fedora-kpasswdtest.patch

# alt patches:
Patch200: krb5-1.16-alt-default_keytab_group.patch

BuildRequires: /dev/pts /proc
BuildRequires: flex libcom_err-devel libkeyutils-devel
BuildRequires: libncurses-devel libss-devel libssl-devel libtinfo-devel
BuildRequires: libpam-devel

%{?_with_ldap:BuildRequires: libldap-devel libsasl2-devel}
%{?_with_verto:BuildRequires: libverto-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}

%if_with doc
BuildRequires: python-module-sphinx
BuildRequires: texlive-latex-base texlive-base-bin texlive-latex-recommended latexmk
%endif

%ifarch %{ix86} x86_64
%{?!_with_bootstrap:BuildRequires: yasm}
%endif

%if_enabled check
# for tests
BuildRequires: libverto-libev python-modules gcc-c++
BuildRequires: nss_wrapper socket_wrapper
# dejagnu tests disabled
# BuildRequires: dejagnu tcl-devel
%endif

%description
Kerberos V5 is a trusted-third-party network authentication system,
which can improve your network's security by eliminating the insecure
practice of cleartext passwords.

# {{{ subpackages

%package -n lib%name
Summary: The shared libraries used by Kerberos 5
Group: System/Libraries
Requires: gawk

%package -n lib%name-ldap
Summary: The shared Kerberos 5 libraries, LDAP support
Group: System/Libraries
Requires: lib%name = %version-%release

%package -n lib%name-devel
Summary: Development files needed to compile Kerberos 5 programs
Group: System/Libraries
Requires: lib%name = %version-%release
%{?_with_ldap:Requires: lib%name-ldap = %version-%release}
Requires: libcom_err-devel
Provides: %name-services = %version-%release
Provides: %name-clients = %version-%release
Obsoletes: %name-services < %version-%release
Obsoletes: %name-clients < %version-%release

%if_without verto
%package -n libverto
Version: 0.0.%version
Summary: verto shared libraries (bootstrap build)
Group: System/Legacy libraries

%description -n libverto
This is a temporary libverto package built within krb5;
only used for bootstrap.
%endif

%package kdc
Group: System/Servers
Summary: The Kerberos 5 Key Distribution Center
Requires: %name-kadmin = %version-%release
Requires: lib%name = %version-%release
Requires: lib%name-ldap = %version-%release
Requires: libverto-libev
Provides: %name-server = %version-%release
Obsoletes: %name-server < %version-%release

%package kadmin
Group: System/Servers
Summary: The KDC admin programs for Kerberos 5
Requires: %name-kinit = %version-%release
Requires: lib%name = %version-%release

%package kinit
Summary: Kerberos 5 programs for use on workstations
Group: System/Base
Requires: lib%name = %version-%release
Provides: %name-workstation = %version-%release
Obsoletes: %name-workstation < %version-%release

%package ksu
Summary: Kerberized super-user
Group: System/Base
PreReq: control
Requires: lib%name = %version-%release
Conflicts: %name-kinit < %version-%release

%package doc
Group: Books/Computer books
Summary: Kerberos 5 documentation
BuildArch: noarch

%description -n lib%name
Kerberos is a network authentication system.  This package contains
the shared libraries needed by Kerberos 5.  If you are using Kerberos,
you need to install this package.

%description -n lib%name-ldap
Kerberos is a network authentication system.  This package contains
the shared Kerberos 5 libraries needed for LDAP backend support.

%description -n lib%name-devel
Kerberos is a network authentication system.  This package contains the
header files and libraries needed for compiling Kerberos 5 programs.
If you want to develop Kerberos-aware programs, you need to install
this package.

%description kdc
Kerberos is a network authentication system.
This package contains the programs that must be installed
on a Kerberos 5 Key Distribution Center.

%description kadmin
Kerberos is a network authentication system.
This package contains set of programs helping to manage
a Kerberos 5 Key Distribution Center.

%description kinit
Kerberos is a network authentication system.
This package contains the basic Kerberos programs.
If your network uses Kerberos, this package should be installed
on every workstation.

%description ksu
Kerberos is a network authentication system.
This package contains ksu program, which is a Kerberized version
of the su program that has two missions: to securely change the
real and effective user ID to that of the target user, and to
create a new security context.

%description doc
Kerberos is a network authentication system.
This packages contains documentation bundled with
MIT Kerberos.

# }}}

%prep
%setup

# fedora patches:
%patch60 -p1 -b .pam
%patch63 -p1 -b .selinux-label
%patch6  -p1 -b .ksu-path
%patch12 -p1 -b .ktany
%patch23 -p1 -b .dns
%patch39 -p1 -b .api
%patch71 -p1 -b .dirsrv-accountlock
%patch86 -p1 -b .debuginfo
# Apply when the hard-wired or configured default location is
# DIR:/run/user/%%{uid}/krb5cc.
%patch129 -p1 -b .run_user_0
%patch134 -p1 -b .kpasswdtest

%patch200 -p2 -b .default_keytab_group

# Generate an FDS-compatible LDIF file.
inldif=src/plugins/kdb/ldap/libkdb_ldap/kerberos.ldif
cat > '60kerberos.ldif' << EOF
# This is a variation on kerberos.ldif which 389 Directory Server will like.
dn: cn=schema
EOF
egrep -iv '(^$|^dn:|^changetype:|^add:)' $inldif | \
sed -r 's,^		,                ,g' | \
sed -r 's,^	,        ,g' >> 60kerberos.ldif
touch -r $inldif 60kerberos.ldif

%ifarch %e2k
sed -r -i 's, error=(pointer-arith|uninitialized),,g' \
   src/aclocal.m4 src/configure*
%endif

%build
# Go ahead and supply tcl info, because configure doesn't know how to find it.
# . %_libdir/tclConfig.sh

DEFINES="-D_FILE_OFFSET_BITS=64" ; export DEFINES
%add_optflags -I/usr/include/et
%add_optflags -DKRB5_DNS_LOOKUP

# Set this so that configure will have a value even if the current version of
# autoconf doesn't set one.
runstatedir=%_runtimedir; export runstatedir

pushd src
autoreconf --verbose --force
%configure \
	--enable-shared --disable-static \
	--localstatedir=%_localstatedir/kerberos \
	--with-system-et \
	--with-system-ss \
	%{?_with_verto:--with-system-verto} \
	%{subst_with ldap} \
	%{subst_with selinux} \
	--enable-dns-for-realm \
	--with-dirsrv-account-locking \
	--enable-pkinit \
%if_without bootstrap
	--with-pkinit-crypto-impl=openssl \
	--with-tls-impl=openssl \
%endif
	--with-pam \
	--with-netlib=-lresolv \
	--disable-rpath \
	#

# dejagnu tests disabled
# 	--with-tcl=%_libdir \
%make_build
popd

# Sanity check the KDC_RUN_DIR.
configured_kdcrundir=`grep KDC_RUN_DIR src/include/osconf.h | awk '{print $NF}'`
configured_kdcrundir=`eval echo $configured_kdcrundir`
if test "$configured_kdcrundir" != %_runtimedir/krb5kdc ; then
    exit 1
fi

%if_with doc
# Build the docs.
make -C src/doc paths.py version.py
cp src/doc/paths.py doc/
mkdir -p build-man build-html build-pdf
sphinx-build -a -b man   -t pathsubs doc build-man
sphinx-build -a -b html  -t pathsubs doc build-html
rm -fr build-html/_sources
sphinx-build -a -b latex -t pathsubs doc build-pdf
# Fix build PDFs with newest sphinx and latexmk
# https://bugzilla.altlinux.org/show_bug.cgi?id=34119
mkdir -p build-pdf/texmf/tex/latex
cp -f %SOURCE11 build-pdf/texmf/tex/latex/
export TEXMFHOME=texmf/
# Build the PDFs if we didn't have pre-built ones.
for pdf in admin appdev basic build plugindev user ; do
    test -s build-pdf/$pdf.pdf || make -C build-pdf
done
%endif

# We need to cut off any access to locally-running nameservers, too.
%__cc -fPIC -shared -o noport.so -Wall -Wextra %SOURCE100

%check
mkdir nss_wrapper

# Set things up to use the test wrappers.
export NSS_WRAPPER_HOSTNAME=test.example.com
export NSS_WRAPPER_HOSTS="$PWD/nss_wrapper/fakehosts"
echo "127.0.0.1 $NSS_WRAPPER_HOSTNAME localhost" > $NSS_WRAPPER_HOSTS
export NOPORT='53,111'
export SOCKET_WRAPPER_DIR="$PWD/sockets" ; mkdir -p $SOCKET_WRAPPER_DIR
export LD_PRELOAD="$PWD/noport.so:libnss_wrapper.so:libsocket_wrapper.so"

# NOTE(iv@): this test hangs for too long, look at this later
echo > src/tests/t_iprop.py

# skip this test, because getaddrinfo with flag AI_ADDRCONFIG return error in hasher
echo > src/tests/t_kprop.py

make -C src runenv.py
make -C src check TMPDIR=%_tmppath OFFLINE=yes PYTESTFLAGS="-v"

%install

make -C src install \
    DESTDIR=%buildroot \
    INSTALL_SETUID='install -m0755' \
    EXAMPLEDIR=%_docdir/examples

# Server init scripts, sample client config file and sample KDC config files.
tar xf %SOURCE2 -C %buildroot

mkdir -p %buildroot%_sysconfdir/krb5.conf.d

# Fix preporcessor loop
# sed -i 's,<krb5/krb5.h>,<krb5/krb5/krb5.h>,' %buildroot%_includedir/krb5/krb5.h

# Relocate *some* shared libraries
mkdir -p %buildroot/%_lib
for lib in libgssapi_krb5 libk5crypto libkrb5 libkrb5support; do
  mv %buildroot%_libdir/${lib}.so.* %buildroot/%_lib
  ln -snf ../../%_lib/`readlink %buildroot%_libdir/${lib}.so` %buildroot%_libdir/${lib}.so
done

# Fix binaries clashes
mv -f %buildroot%_bindir/uuclient %buildroot%_bindir/%name-uuclient
mv -f %buildroot%_sbindir/uuserver %buildroot%_sbindir/%name-uuserver

# Where per-user keytabs live by default.
mkdir -p %buildroot%_localstatedir/kerberos/krb5/user

# Parent of configuration file for list of loadable GSS mechs ("mechs").  This
# location is not relative to sysconfdir, but is hard-coded in g_initialize.c.
mkdir -m 755 -p %buildroot%_sysconfdir/gss
# Parent of groups of configuration files for a list of loadable GSS mechs
# ("mechs").  This location is not relative to sysconfdir, and is also
# hard-coded in g_initialize.c.
mkdir -m 755 -p %buildroot%_sysconfdir/gss/mech.d

%if_with doc
# Install docs
mkdir -p %buildroot%_docdir/pdf
cp build-pdf/*.pdf %buildroot%_docdir/pdf/
cp -R build-html/ %buildroot/%_docdir/
cp -p src/plugins/kdb/ldap/libkdb_ldap/kerberos.{ldif,schema} %buildroot%_docdir/
%endif

# cleanups
rm -rf %buildroot%_libdir/krb5/plugins/preauth/test.so
rm -rf %buildroot%_datadir/gnats
rm -rf %buildroot%_mandir/cat*
touch %buildroot%_sysconfdir/krb5.keytab

%find_lang mit-krb5

%if_without bootstrap
%post kdc
%post_service krb5kdc
%post_service kadmin
%post_service kprop

%preun kdc
%preun_service krb5kdc
%preun_service kadmin
%preun_service kprop
%endif

%pre -n lib%name
/usr/sbin/groupadd -r -f _keytab

%pre ksu
%pre_control ksu

%post ksu
%post_control -s wheelonly ksu


%triggerpostun -n lib%name -- lib%name < 1.14.4-alt2
if [ -f %_sysconfdir/krb5.keytab ]; then
    chown :_keytab %_sysconfdir/krb5.keytab
    chmod g+r %_sysconfdir/krb5.keytab
fi

%files -n lib%name -f mit-krb5.lang
%config(noreplace) %_sysconfdir/krb5.conf
%ghost %config(noreplace) %attr(640,root,_keytab) %_sysconfdir/krb5.keytab
%dir %_sysconfdir/gss
%dir %_sysconfdir/gss/mech.d
%dir %_sysconfdir/krb5.conf.d
%dir %_localstatedir/kerberos
%dir %_localstatedir/kerberos/krb5
%dir %_localstatedir/kerberos/krb5/user

/%_lib/lib*.so.*

%_libdir/libgssrpc.so.*
%_libdir/libkadm5clnt_mit.so.*
%_libdir/libkadm5srv_mit.so.*
%_libdir/libkdb5.so.*
%_libdir/libkrad.so.*

%dir %_libdir/%name
%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/kdb
%dir %_libdir/%name/plugins/preauth
%dir %_libdir/%name/plugins/tls
%_libdir/%name/plugins/kdb/db2.so
%_libdir/%name/plugins/preauth/otp.so
%_libdir/%name/plugins/preauth/pkinit.so
%_libdir/%name/plugins/preauth/spake.so
%_libdir/%name/plugins/tls/k5tls.so

%_man5dir/krb5.conf.5*
%_man7dir/kerberos.7*

%if_with ldap
%files -n lib%name-ldap
%_libdir/libkdb_ldap.so.*
%_libdir/%name/plugins/kdb/kldap.so
%endif

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_bindir/gss-client
%_bindir/sclient
%_bindir/krb5-config
%_bindir/sim_client
%_bindir/%name-uuclient
%_sbindir/%name-uuserver
%_sbindir/gss-server
%exclude %_sbindir/krb5-send-pr
%_sbindir/sim_server
%_sbindir/sserver
%_man1dir/sclient.1*
%_man1dir/krb5-config.1*
%_man8dir/sserver.8*
%_pkgconfigdir/*

%if_without verto
%files -n libverto
%_prefix/lib*/libverto.so.*
%endif

%if_without bootstrap
%files kdc
%dir %_localstatedir/kerberos/krb5kdc
%config(noreplace) %_localstatedir/kerberos/krb5kdc/kdc.conf
%config(noreplace) %_localstatedir/kerberos/krb5kdc/kadm5.acl

%config(noreplace) %_sysconfdir/sysconfig/kadmin
%config(noreplace) %_sysconfdir/sysconfig/krb5kdc

%_initdir/kadmin
%_initdir/krb5kdc
%_initdir/kprop

%systemd_unitdir/kadmin.service
%systemd_unitdir/kprop.service
%systemd_unitdir/krb5kdc.service

%_sbindir/kadmin.local
%_sbindir/kadmind
%_sbindir/kdb5_util
%{?_with_ldap:%_sbindir/kdb5_ldap_util}
%_sbindir/kprop
%_sbindir/kproplog
%_sbindir/kpropd
%_sbindir/krb5kdc

%_man5dir/kadm5.acl.5*
%_man5dir/kdc.conf.5*
%_man8dir/kadmin.local.8*
%_man8dir/kadmind.8*
%_man8dir/kdb5_util.8*
%{?_with_ldap:%_man8dir/kdb5_ldap_util.8*}
%_man8dir/kprop.8*
%_man8dir/kproplog.8*
%_man8dir/kpropd.8*
%_man8dir/krb5kdc.8*
%endif

%files kadmin
%_bindir/kadmin
%_bindir/ktutil
%_man1dir/kadmin.1*
%_man1dir/ktutil.1*

%_bindir/k5srvutil
%_man1dir/k5srvutil.1*

%files kinit
%_bindir/kdestroy
%_bindir/kinit
%_bindir/klist
%_bindir/kpasswd
%_bindir/kvno
%_bindir/kswitch

%_man1dir/kdestroy.1*
# %%_man1dir/kerberos.1*
%_man1dir/kinit.1*
%_man1dir/klist.1*
%_man1dir/kpasswd.1*
%_man1dir/kvno.1*
%_man1dir/kswitch.1*
%_man5dir/.k5login.5*
%_man5dir/k5login.5*
%_man5dir/.k5identity.5*
%_man5dir/k5identity.5*

%files ksu
%config(noreplace) %_sysconfdir/pam.d/ksu
%_controldir/ksu
%_bindir/ksu
%_man1dir/ksu.1*


%if_with doc
%files doc
%doc %_docdir
%endif

# {{{ changelog

%changelog
* Thu Dec 12 2019 Ivan A. Melnikov <iv@altlinux.org> 1.17.1-alt1
- 1.17.1

* Wed Jan 09 2019 Ivan A. Melnikov <iv@altlinux.org> 1.17-alt1
- 1.17
- drop patch 1, as we don't need that export any more
- update patch 63 from fedora

* Tue Jan 08 2019 Ivan A. Melnikov <iv@altlinux.org> 1.16.3-alt1
- 1.16.3 (CVE-2018-20217)
- apply bootstrap and e2k tweaks (mike@) (closes: #32982)
  + introduce doc, ldap, selinux, verto knobs (on by default)
  + conditionally package bundled libverto
  + e2k: disable -Werror={pointer-arith,uninitialized} (lcc)

* Thu Nov 29 2018 Stanislav Levin <slev@altlinux.org> 1.16.2-alt2
- Fixed yield of cache from MEMORY ccache (closes #35597, #35667).

* Fri Nov 02 2018 Ivan A. Melnikov <iv@altlinux.org> 1.16.2-alt1
- 1.16.2

* Wed Oct 17 2018 Ivan A. Melnikov <iv@altlinux.org> 1.16.1-alt3
- move ksu to a separate subpackage
- add control facility to manage ksu binary permissions (closes #33479)
- get rid of UBT

* Wed Aug 29 2018 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt2.S1
- rebuild with openssl-1.1

* Mon Aug 27 2018 Ivan A. Melnikov <iv@altlinux.org> 1.16.1-alt1.S1
- 1.16.1 (CVE-2018-5729, CVE-2018-5730)

* Mon Jan 22 2018 Evgeny Sinelnikov <sin@altlinux.org> 1.16-alt1.S1
- Update to latest stable release 1.16

* Fri Nov 03 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.15.2-alt2.S1
- Fix build-pdf on Sisyphus
- Add noport, nss_wrapper and socket_wrapper for tests running

* Wed Nov 01 2017 Evgeny Sinelnikov <sin@altlinux.org> 1.15.2-alt1.S1
- Update to latest stable release 1.15.2 with kdcpreauth from 1.16.x

* Sun Aug 20 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.15.1-alt1.S1
- Update to latest stable release 1.15.1 with kdcpreauth from 1.16.x

* Fri Mar 24 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.5-alt1.S1
- Update to first spring release 1.14.5

* Tue Feb 28 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.4-alt2.S1
- Add _keytab group for default keytab /etc/krb5.keytab

* Wed Feb 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.14.4-alt1.S1
- 1.14.4
- fixed CVE-2016-3120

* Thu Jun 09 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.14.2-alt2
- krb5kdc.service: start after slapd

* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.2-alt1
- 1.14.2
- fixed CVE-2015-2695,CVE-2015-2696,CVE-2015-2697,CVE-2015-2698,CVE-2015-8629,CVE-2015-8630,CVE-2015-8631,CVE-2016-3119
- allow verification of attributes on krb5.conf

* Mon Nov 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.13.2-alt2
- Comment out includedir directive in /etc/krb5.conf because samba
  cannot get Kerberos context while domain provision

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.13.2-alt1
- 1.13.2
- fixed CVE-2014-5355, CVE-2015-2694
- add patches from fedora

* Sun Feb 22 2015 Ivan A. Melnikov <iv@altlinux.org> 1.13.1-alt1
- 1.13.1;
- drop patches already applied by upstream.

* Sun Feb 08 2015 Ivan A. Melnikov <iv@altlinux.org> 1.13-alt3
- fix for MITKRB5-SA-2015-001 (CVE-2014-5352, CVE-2014-9421,
  CVE-2014-9422, CVE-2014-9423)

* Tue Dec 23 2014 Alexey Shabalin <shaba@altlinux.ru> 1.13-alt2
- fixed CVE-2014-5353, CVE-2014-5354

* Fri Oct 31 2014 Alexey Shabalin <shaba@altlinux.ru> 1.13-alt1
- 1.13
- fixed CVE-2014-5351
- move header from /usr/include/krb5 to /usr/include
- drop kdcrotate service
- update krb5.conf:
  + add [logging] example
  + add [realms] example
  + add [domain_realm] example
  + define default_ccache_name as KEYRING:persistent:%%{uid}

* Thu Mar 27 2014 Timur Aitov <timonbl4@altlinux.org> 1.12-alt2
- applied upstream fix for libdb2
- disabled t_kprop.py test

* Sun Jan 12 2014 Ivan A. Melnikov <iv@altlinux.org> 1.12-alt1
- 1.12;
- update fedora patches;
- import memory leak fixes from upstream master (RT#7803, RT#7805).

* Sat Jun 08 2013 Ivan A. Melnikov <iv@altlinux.org> 1.11.3-alt1
- 1.11.3
- drop obsolete patch 23.

* Fri May 31 2013 Andrey Cherepanov <cas@altlinux.org> 1.11.2-alt3
- Increase run order from 40 to 41 to prevent error reading from LDAP:
  'preauth pkinit failed to initialize: No realms configured correctly
  for pkinit support'

* Tue May 14 2013 Ivan A. Melnikov <iv@altlinux.org> 1.11.2-alt2
- add patch 23 from upstream git to fix kpasswd udp ping-pong
  (CVE-2002-2443).

* Sat Apr 13 2013 Ivan A. Melnikov <iv@altlinux.org> 1.11.2-alt1
- 1.11.2;
- drop obsolete patch 22.

* Sat Mar 30 2013 Ivan A. Melnikov <iv@altlinux.org> 1.11.1-alt1
- 1.11.1
  + fix a null pointer dereference in the KDC PKINIT code
    (CVE-2013-1415);
- drop obsolete patch 21;
- add patch 22 from upstream git to fix a memory leak in
  krb5_get_init_creds_keytab (upstream ticket 7586).

* Fri Jan 04 2013 Ivan A. Melnikov <iv@altlinux.org> 1.11-alt2
- added %%check section.

* Fri Jan 04 2013 Ivan A. Melnikov <iv@altlinux.org> 1.11-alt1
- 1.11;
- dropped obsolete patches;
- updated fedora patches;
- add patch 21 from fedora;
- update gear rules to better match upstream distribution;
- change way we deal with preprocessor loop in krb5/krb5.h (instead
  of patch that caused build problems we do it with sed in %%install);
- dropped internal headers packaging;
- minor packaging improvements.

* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt2.1
- Fixed build

* Tue Aug 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.2-alt2
- CVE-2012-1015

* Thu Jul 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.2-alt1.1
- Added necessary headers into lib%name-devel (ALT #27467)

* Wed Jul 04 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.2-alt1
- 1.10.2
- CVE-2012-1013

* Fri May 04 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt3
- Add systemd unit files

* Sat Apr 28 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt2
- resurrect krb5-1.10-alt-avoid-preprocessor-loop.patch

* Mon Apr 23 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt1
- 1.10.1
- get rid of almost empty services, clients subpackages
- replace server, workstation packages by Provides/Obsoletes

* Wed Jul 06 2011 Ivan A. Melnikov <iv@altlinux.org> 1.6.3-alt13
- check if ftp daemon fails to set effective group id
  (MITKRB5-SA-2011-005, CVE-2011-1526).

* Tue Mar 15 2011 Alexey Tourbin <at@altlinux.ru> 1.6.3-alt12
- krb5-config: disabled dependency on libkeyutils-devel

* Thu Feb 10 2011 Ivan A. Melnikov <iv@altlinux.org> 1.6.3-alt11
- fixed:
  + MITKRB5-SA-2010-003
  + MITKRB5-SA-2010-005
  + MITKRB5-SA-2010-007
  + MITKRB5-SA-2011-002
- added strict requiremets on libkrb5-ldap;
- rebuild with debuinfo.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.6.3-alt10
- Backported pkinit_crypto_openssl.c fixes from trunk.
- Packaged -doc, -server and -workstation subpackages as noarch.
- Built with libcrypto.so.10.

* Wed Jan 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt9
- fixed:
  + MITKRB-SA-2009-004

* Sat Sep 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt8
- rebuilt with openldap2.4

* Fri Apr  3 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt7
- kdc initscript modified to run after slapd
- kadmin & kprop services off by default
- fixed:
  + MITKRB5-SA-2009-001
  + MITKRB5-SA-2009-002

* Fri Mar 20 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt6
- change defaults to rely on DNS SRV/TXT records
- redundant req on libe2fs-devel in devel subpackage dropped (#16637)

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt5
- obsolete by filetriggers macros removed

* Sun Aug 10 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt4
- redundant build req to e2fs-devel removed (#16137)
- krb5.h modifed to avoid preprocessor loop
- rebuilt againts recent openssl

* Mon Mar 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt3
- fixed:
  + MITKRB5-SA-2008-001
  + MITKRB5-SA-2008-002

* Fri Jan 11 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt2
- added req on libkeyutils-devel to krb5-devel subpackage (#13977)

* Sat Jan  5 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 released

* Fri Sep  7 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt7
- MITKRB5-SA-2007-006 fix revised

* Tue Sep  4 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt6
- fixed:
  + MITKRB5-SA-2007-006

* Tue Jun 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt5
- fixed:
  + MITKRB5-SA-2007-004
  + MITKRB5-SA-2007-005

* Wed Apr  4 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt4
- fixed:
  + MITKRB5-SA-2007-001
  + MITKRB5-SA-2007-002
  + MITKRB5-SA-2007-003

* Sat Jan 13 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt3
- kadmind: MITKRB5-SA-2006-002, MITKRB5-SA-2006-003
- bug fixed: #10494

* Sat Oct 28 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt2
- packaged missing db2 plugin

* Sat Oct  7 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.1-alt1
- 1.5.1 released
- patches rediffed & applied:
  + krb5-1.3-alt-rh-manpage-paths.patch
  + krb5-1.3-rh-netkit-rsh.patch
  + krb5-1.4-alt-rh-rlogind-environ.patch
  + krb5-1.3-rh-ksu-access.patch
  + krb5-1.3-rh-ksu-path.patch
  + krb5-1.1.1-rh-brokenrev.patch
  + krb5-1.2.1-rh-passive.patch
  + krb5-1.4-rh-ktany.patch
  + krb5-1.3-rh-large-file.patch
  + krb5-1.3-rh-ftp-glob.patch
  + krb5-1.3-rh-check.patch
  + krb5-1.2.7-rh-reject-bad-transited.patch
  + krb5-1.3.1-rh-dns.patch
  + krb5-1.4-rh-null.patch
  + krb5-1.3.3-rh-rcp-sendlarge.patch
  + krb5-1.3.5-rh-kprop-mktemp.patch
  + krb5-1.3.6-alt-send-pr.patch
  + krb5-1.4.1-rh-api.patch
  + krb5-1.4.1-rh-telnet-environ.patch
  + krb5-1.4.3-rh-enospc.patch
  + krb5-1.5-rh-fclose.patch
  + krb5-1.5-rh-gssinit.patch
  + krb5-1.5-rh-io.patch
  + krb5-1.5.1-alt-tinfo.patch
  + krb5-1.5.1-alt-norpath.patch
  + krb5-1.5.1-alt-krb5config.patch
  + krb5-1.5.1-alt-krb5-rlogin-prog.patch
  + krb5-1.5.1-alt-kadmind-pidfile.patch

* Sat Apr 15 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.3-alt2
- fixed #9408

* Sat Apr  8 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.3-alt1
- 1.4.3
- linked against system libss

* Sun Jun 19 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1
- subpackages rearranged:
  + made new -kdc, -kadmin and -kinit subpackages
  + old -server and -workstation now contains no data
  + extra docs packaged separately to -doc subpackage
- some libraries returned back to %%_libdir
- bugs fixed: #6109, #6678, #6727

* Fri Jan 21 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Mon Aug 30 2004 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt5
- NMU, fixes:
  + MITKRB5-SA-2004-001,
  + MITKRB5-SA-2004-002,
  + MITKRB5-SA-2004-003.

* Mon Jun 28 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.1-alt4.1
- Removed unneeded %%set_*_version calls.

* Tue Feb 24 2004 Alexander Bokovoy <ab@altlinux.ru> 1.3.1-alt4
- Force -I%_includedir/et in krb5-config

* Fri Feb 13 2004 Alexander Bokovoy <ab@altlinux.ru> 1.3.1-alt3
- Fixed:
    + #3494, #3655, #3136, and #2770
- Changed:
    + Libraries moved from %_libdir/krb5 to /lib
- Added:
    + Compile krb5 against system libcom_err from libe2fs
- Removed:
    + Static libraries

* Mon Sep 29 2003 Alexander Bokovoy <ab@altlinux.ru> 1.3.1-alt2
- Added:
    + all init scripts moved to start-stop-daemon approach
- Fixed:
    + #2875, in kpropd and kadmind initscripts
- Removed:
    + Kerberos IV support

* Mon Sep 29 2003 Alexander Bokovoy <ab@altlinux.ru> 1.3.1-alt1
- 1.3.1 release (with support for RC4-HMAC encryption type)

* Mon Mar 24 2003 Alexander Bokovoy <ab@altlinux.ru> 1.2.7-alt2
- Fixed:
    + MITKRB5-SA-2003-03
    + CAN-2003-0072
    + CAN-2003-0082

* Sat Feb 15 2003 Alexander Bokovoy <ab@altlinux.ru> 1.2.7-alt1
- 1.2.7
- Fixed:
    + krb5-config to reflect our layout
    + localstatedir to %_localstatedir/kerberos
    + description of lib%name-devel
- Splitted:
    + statically compiled libraries to lib%name-devel-static

* Mon Jan 27 2003 Alexander Bokovoy <ab@altlinux.ru> 1.2.5.1-alt2
- Merge AW changes with Sisyphus

* Mon Jan 20 2003 Grigory Milev <week@altlinux.ru> 1.2.5.1-5aw
- spec cleanup

* Thu Jan  9 2003 Grigory Milev <week@altlinux.ru> 1.2.5.1-4aw
- AW adaptations

* Mon Dec 30 2002 Alexander Bokovoy <ab@altlinux.ru> 1.2.5.1-alt1
- Integrate krb5-current into Sisyphus
- Patch list revised
- Move various samples to libkrb5-devel

* Wed Sep 04 2002 Alexander Bokovoy <ab@optifacio.com> 1.2.5.1-1aw
- Integrate krb5-current to get access to enc.type 23
- remove libtinfo/samba support as it is not required yet.

* Mon Aug 05 2002 Alexander Bokovoy <ab@altlinux.ru> 1.2.5-alt1
- New release
- Fixed:
    + MITKRB5-SA-2002-001: Remote root vulnerability in MIT krb5 admin system
- Added but not compiled in yet:
    + A patch from Andrew Tridgell to better support Samba 3.0 ADS mode

* Thu Jul 18 2002 Alexander Bokovoy <ab@altlinux.ru> 1.2.2-alt7
- Build against libtinfo, get rid of termcap/ncurses

* Sat Mar 02 2002 Alexander Bokovoy <ab@altlinux.ru> 1.2.2-alt6
- Fixed:
    + %_includedir/krb5 ownership

* Thu Jan 03 2002 Alexander Bokovoy <ab@altlinux.ru> 1.2.2-alt5
- Fixed:
    + documentation clashes with overriden utilites

* Tue Dec 18 2001 Alexander Bokovoy <ab@altlinux.ru> 1.2.2-alt4
- Fixed:
    + paths in xinet.d services
    + /var/kerberos moved to %_localstatedir/kerberos (FHS)

* Mon Dec 17 2001 Alexander Bokovoy <ab@altlinux.ru> 1.2.2-alt3
- Fixed:
    + postin/un scripts for lib%name

* Sat Dec 15 2001 Alexander Bokovoy <ab@altlinux.ru> 1.2.2-alt2
- Fixed:
    + Info pages for server/workstation

* Tue Dec 11 2001 Alexander Bokovoy <ab@altlinux.ru> 1.2.2-alt1
- Initial build for ALT Linux based on Applianceware version
- Fixed:
    + all libs moved to %_libdir/krb5/, includes to %_includedir/krb5
    + postinstall/postuninstall scripts for libs
    + dependencies for several sub-packages to eliminate file deps.
    + krb5-send-pr to not expose direct Requires: to nis/yp utils
- Packages renamed:
    + %name-libs -> lib%name
    + %name-devel -> lib%name-devel

* Fri Aug  3 2001 Nalin Dahyabhai <nalin@redhat.com>
- bump release number and rebuild

* Wed Aug  1 2001 Nalin Dahyabhai <nalin@redhat.com>
- add patch to fix telnetd vulnerability

* Fri Jul 20 2001 Nalin Dahyabhai <nalin@redhat.com>
- tweak statglue.c to fix stat/stat64 aliasing problems
- be cleaner in use of gcc to build shlibs

* Wed Jul 11 2001 Nalin Dahyabhai <nalin@redhat.com>
- use gcc to build shared libraries

* Wed Jun 27 2001 Nalin Dahyabhai <nalin@redhat.com>
- add patch to support "ANY" keytab type (i.e.,
  "default_keytab_name = ANY:FILE:/etc/krb5.keytab,SRVTAB:/etc/srvtab"
  patch from Gerald Britton, #42551)
- build with -D_FILE_OFFSET_BITS=64 to get large file I/O in ftpd (#30697)
- patch ftpd to use long long and %%lld format specifiers to support the SIZE
  command on large files (also #30697)
- don't use LOG_AUTH as an option value when calling openlog() in ksu (#45965)
- implement reload in krb5kdc and kadmind init scripts (#41911)
- lose the krb5server init script (not using it any more)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Tue May 29 2001 Nalin Dahyabhai <nalin@redhat.com>
- pass some structures by address instead of on the stack in krb5kdc

* Tue May 22 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Thu Apr 26 2001 Nalin Dahyabhai <nalin@redhat.com>
- add patch from Tom Yu to fix ftpd overflows (#37731)

* Wed Apr 18 2001 Than Ngo <than@redhat.com>
- disable optimizations on the alpha again

* Fri Mar 30 2001 Nalin Dahyabhai <nalin@redhat.com>
- add in glue code to make sure that libkrb5 continues to provide a
  weak copy of stat()

* Thu Mar 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- build alpha with -O0 for now

* Thu Mar  8 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix the kpropd init script

* Mon Mar  5 2001 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.2.2, which fixes some bugs relating to empty ETYPE-INFO
- re-enable optimization on Alpha

* Thu Feb  8 2001 Nalin Dahyabhai <nalin@redhat.com>
- build alpha with -O0 for now
- own %_var/kerberos

* Tue Feb  6 2001 Nalin Dahyabhai <nalin@redhat.com>
- own the directories which are created for each package (#26342)

* Tue Jan 23 2001 Nalin Dahyabhai <nalin@redhat.com>
- gettextize init scripts

* Fri Jan 19 2001 Nalin Dahyabhai <nalin@redhat.com>
- add some comments to the ksu patches for the curious
- re-enable optimization on alphas

* Mon Jan 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix krb5-send-pr (#18932) and move it from -server to -workstation
- buildprereq libtermcap-devel
- temporariliy disable optimization on alphas
- gettextize init scripts

* Tue Dec  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- force -fPIC

* Fri Dec  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Oct 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- add bison as a BuildPrereq (#20091)

* Mon Oct 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- change /usr/dict/words to /usr/share/dict/words in default kdc.conf (#20000)

* Thu Oct  5 2000 Nalin Dahyabhai <nalin@redhat.com>
- apply kpasswd bug fixes from David Wragg

* Wed Oct  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- make krb5-libs obsolete the old krb5-configs package (#18351)
- don't quit from the kpropd init script if there's no principal database so
  that you can propagate the first time without running kpropd manually
- don't complain if /etc/ld.so.conf doesn't exist in the -libs %post

* Tue Sep 12 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix credential forwarding problem in klogind (goof in KRB5CCNAME handling)
  (#11588)
- fix heap corruption bug in FTP client (#14301)

* Wed Aug 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix summaries and descriptions
- switched the default transfer protocol from PORT to PASV as proposed on
  bugzilla (#16134), and to match the regular ftp package's behavior

* Wed Jul 19 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Fri Jul 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- disable servers by default to keep linuxconf from thinking they need to be
  started when they don't

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- change cleanup code in post to not tickle chkconfig
- add grep as a Prereq: for -libs

* Thu Jul  6 2000 Nalin Dahyabhai <nalin@redhat.com>
- move condrestarts to postun
- make xinetd configs noreplace
- add descriptions to xinetd configs
- add /etc/init.d as a prereq for the -server package
- patch to properly truncate $TERM in krlogind

* Fri Jun 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to 1.2.1
- back out Tom Yu's patch, which is a big chunk of the 1.2 -> 1.2.1 update
- start using the official source tarball instead of its contents

* Thu Jun 29 2000 Nalin Dahyabhai <nalin@redhat.com>
- Tom Yu's patch to fix compatibility between 1.2 kadmin and 1.1.1 kadmind
- pull out 6.2 options in the spec file (sonames changing in 1.2 means it's not
  compatible with other stuff in 6.2, so no need)

* Wed Jun 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- tweak graceful start/stop logic in post and preun

* Mon Jun 26 2000 Nalin Dahyabhai <nalin@redhat.com>
- update to the 1.2 release
- ditch a lot of our patches which went upstream
- enable use of DNS to look up things at build-time
- disable use of DNS to look up things at run-time in default krb5.conf
- change ownership of the convert-config-files script to root.root
- compress PS docs
- fix some typos in the kinit man page
- run condrestart in server post, and shut down in preun

* Mon Jun 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- only remove old krb5server init script links if the init script is there

* Sat Jun 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- disable kshell and eklogin by default

* Thu Jun 15 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch mkdir/rmdir problem in ftpcmd.y
- add condrestart option to init script
- split the server init script into three pieces and add one for kpropd

* Wed Jun 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- make sure workstation servers are all disabled by default
- clean up krb5server init script

* Fri Jun  9 2000 Nalin Dahyabhai <nalin@redhat.com>
- apply second set of buffer overflow fixes from Tom Yu
- fix from Dirk Husung for a bug in buffer cleanups in the test suite
- work around possibly broken rev binary in running test suite
- move default realm configs from /var/kerberos to %_var/kerberos

* Tue Jun  6 2000 Nalin Dahyabhai <nalin@redhat.com>
- make ksu and v4rcp owned by root

* Sat Jun  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- use %%{_infodir} to better comply with FHS
- move .so files to -devel subpackage
- tweak xinetd config files (bugs #11833, #11835, #11836, #11840)
- fix package descriptions again

* Wed May 24 2000 Nalin Dahyabhai <nalin@redhat.com>
- change a LINE_MAX to 1024, fix from Ken Raeburn
- add fix for login vulnerability in case anyone rebuilds without krb4 compat
- add tweaks for byte-swapping macros in krb.h, also from Ken
- add xinetd config files
- make rsh and rlogin quieter
- build with debug to fix credential forwarding
- add rsh as a build-time req because the configure scripts look for it to
  determine paths

* Wed May 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix config_subpackage logic

* Tue May 16 2000 Nalin Dahyabhai <nalin@redhat.com>
- remove setuid bit on v4rcp and ksu in case the checks previously added
  don't close all of the problems in ksu
- apply patches from Jeffrey Schiller to fix overruns Chris Evans found
- reintroduce configs subpackage for use in the errata
- add PreReq: sh-utils

* Mon May 15 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix double-free in the kdc (patch merged into MIT tree)
- include convert-config-files script as a documentation file

* Wed May 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- patch ksu man page because the -C option never works
- add access() checks and disable debug mode in ksu
- modify default ksu build arguments to specify more directories in CMD_PATH
  and to use getusershell()

* Wed May 03 2000 Bill Nottingham <notting@redhat.com>
- fix configure stuff for ia64

* Mon Apr 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- add LDCOMBINE=-lc to configure invocation to use libc versioning (bug #10653)
- change Requires: for/in subpackages to include %version

* Wed Apr 05 2000 Nalin Dahyabhai <nalin@redhat.com>
- add man pages for kerberos(1), kvno(1), .k5login(5)
- add kvno to -workstation

* Mon Apr 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- Merge krb5-configs back into krb5-libs.  The krb5.conf file is marked as
  a %%config file anyway.
- Make krb5.conf a noreplace config file.

* Thu Mar 30 2000 Nalin Dahyabhai <nalin@redhat.com>
- Make klogind pass a clean environment to children, like NetKit's rlogind does.

* Wed Mar 08 2000 Nalin Dahyabhai <nalin@redhat.com>
- Don't enable the server by default.
- Compress info pages.
- Add defaults for the PAM module to krb5.conf

* Mon Mar 06 2000 Nalin Dahyabhai <nalin@redhat.com>
- Correct copyright: it's exportable now, provided the proper paperwork is
  filed with the government.

* Fri Mar 03 2000 Nalin Dahyabhai <nalin@redhat.com>
- apply Mike Friedman's patch to fix format string problems
- don't strip off argv[0] when invoking regular rsh/rlogin

* Thu Mar 02 2000 Nalin Dahyabhai <nalin@redhat.com>
- run kadmin.local correctly at startup

* Mon Feb 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- pass absolute path to kadm5.keytab if/when extracting keys at startup

* Sat Feb 19 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix info page insertions

* Wed Feb  9 2000 Nalin Dahyabhai <nalin@redhat.com>
- tweak server init script to automatically extract kadm5 keys if
  /var/kerberos/krb5kdc/kadm5.keytab doesn't exist yet
- adjust package descriptions

* Thu Feb  3 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix for potentially gzipped man pages

* Fri Jan 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix comments in krb5-configs

* Fri Jan  7 2000 Nalin Dahyabhai <nalin@redhat.com>
- move /usr/kerberos/bin to end of PATH

* Tue Dec 28 1999 Nalin Dahyabhai <nalin@redhat.com>
- install kadmin header files

* Tue Dec 21 1999 Nalin Dahyabhai <nalin@redhat.com>
- patch around TIOCGTLC defined on alpha and remove warnings from libpty.h
- add installation of info docs
- remove krb4 compat patch because it doesn't fix workstation-side servers

* Mon Dec 20 1999 Nalin Dahyabhai <nalin@redhat.com>
- remove hesiod dependency at build-time

* Sun Dec 19 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- rebuild on 1.1.1

* Thu Oct  7 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- clean up init script for server, verify that it works [jlkatz]
- clean up rotation script so that rc likes it better
- add clean stanza

* Mon Oct  4 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- backed out ncurses and makeshlib patches
- update for krb5-1.1
- add KDC rotation to rc.boot, based on ideas from Michael's C version

* Mon Sep 26 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- added -lncurses to telnet and telnetd makefiles

* Mon Jul  5 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- added krb5.csh and krb5.sh to /etc/profile.d

* Mon Jun 22 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- broke out configuration files

* Mon Jun 14 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- fixed server package so that it works now

* Sat May 15 1999 Nalin Dahyabhai <nsdahya1@eos.ncsu.edu>
- started changelog
- updated existing 1.0.5 RPM from Eos Linux to krb5 1.0.6
- added --force to makeinfo commands to skip errors during build

# }}}

