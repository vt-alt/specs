%def_enable snapshot
%define _libexecdir %_prefix/libexec

%def_enable trust_module
%def_enable doc
# the hash implementation -- freebl or internal
%define hash_impl internal
%define trust_paths %_sysconfdir/pki/ca-trust/source:%_datadir/pki/ca-trust-source
%def_disable systemd

Name: p11-kit
Version: 0.23.15
Release: alt2

Summary: Utilities for PKCS#11 modules
Group: Security/Networking
License: BSD
Url: http://p11-glue.freedesktop.org/p11-kit.html

%if_enabled snapshot
# VCS: https://github.com/p11-glue/p11-kit.git
Source: %name-%version.tar
%else
#Source: http://p11-glue.freedesktop.org/releases/%name-%version.tar.gz
Source: https://github.com/p11-glue/%name/releases/download/%version/%name-%version.tar.gz
%endif

Source1: p11-kit-extract-trust
Patch: %name-%version-%release.patch
Patch1: lib%name-0.23.8-alt-lfs.patch

Requires: %_datadir/pki/ca-trust-source/ca-bundle.trust.p11-kit
Requires: %name-trust = %version-%release

BuildRequires(pre): rpm-macros-alternatives
BuildRequires: libtasn1-devel libffi-devel
%if %hash_impl == freebl
BuildRequires: libnss-devel
%endif
%{?_enable_systemd:BuildRequires: systemd-devel}
%{?_enable_doc:BuildRequires: gtk-doc}

%description
%name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

This package contains the p11-kit tool for listing PKCS#11 modules.

%package -n lib%name
Summary: Library for loading and sharing PKCS#11 modules
Group: System/Libraries

%description -n lib%name
%name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

%package trust
Summary: System trust module from %name package
Group: Security/Networking
Requires: lib%name = %version-%release
Provides: pkcs11-trust-module = %version-%release
Provides: lib%name-trust = %version-%release
Obsoletes: lib%name-trust < %version-%release
Requires: ca-trust

%description trust
The %name-trust package contains a system trust PKCS#11 module which
contains certificate anchors and black lists.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
%name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they're discoverable.

The %name-devel package provides libraries and headers for developing
applications that use %name library.

%package  -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: lib%name < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
%name provides a way to load and enumerate PKCS#11 modules, as well
as a standard configuration setup for installing PKCS#11 modules in
such a way that they\'re discoverable.

This package contains development documentation for %name library.

%package server
Summary: Server and client commands for %name
Group: Security/Networking
Requires: lib%name = %version-%release

%description server
The %name-server package contains command line tools that enable to
export PKCS#11 modules through a Unix domain socket.  Note that this
feature is still experimental.

%package checkinstall
Summary: Check p11-kit-trust.so and libnssckbi.so compatibility
Group: Other
Requires: %name-trust
Requires: nss-utils

%description checkinstall
Check during install that p11-kit-trust.so and libnssckbi.so are
compatible with each other.
This package is intended to be used in the install check step in the build
system only and should not be installed in the real systems.

%prep
%setup -n %name-%version
%patch -p1
%{?_enable_snapshot:NOCONFIGURE=1 ./autogen.sh}
%patch1

%build
%autoreconf
%configure --disable-static \
	--enable-debug=no \
	%{subst_enable trust_module} \
%if_enabled trust_module
	--with-libtasn1 \
	--with-trust-paths=%trust_paths \
%endif
	--with-hash-impl=%hash_impl \
	%{subst_enable doc}
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/pkcs11/modules
install -p -m755 %SOURCE1 %buildroot/%_libexecdir/%name/

# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/libnssckbi-%name <<EOF
%_libdir/libnssckbi.so	%_libdir/pkcs11/p11-kit-trust.so	30
EOF

%check
make check

%post checkinstall
TEST_DIR="$(mktemp -dt %name-installcheckXXXXXXXX)"
cd "$TEST_DIR"
mkdir nssdb
certutil -N --empty-password -d nssdb
ln -rs %_libdir/pkcs11/p11-kit-trust.so nssdb/libnssckbi.so
certutil -L -d nssdb -h 'Builtin Object Token' | sed -r -n \
	's|^Default Trust:(.+[^[:blank:]])[[:blank:]]+[^[:blank:]]+[[:blank:]]*$|\1|p' \
	| sort >certutil.list
trust list --filter=certificates \
	| sed -n -r 's|^[[:blank:]]+label:[[:blank:]]+(.+)[[:blank:]]*$|\1|p' \
	| sort >trust.list
if [ ! -s certutil.list ]; then
	echo "certutil.list is empty" 1>&2
	exit 1
fi
if [ ! -s trust.list ]; then
	echo "trust.list is empty" 1>&2
	exit 1
fi

diff trust.list certutil.list || exit 1
cd - >/dev/null
rm -r -- "$TEST_DIR"

%files
%_bindir/%name
%_libexecdir/%name/p11-kit-remote
%{?_enable_doc:%_man8dir/p11-kit.*}

%if_enabled systemd
%_prefix/lib/systemd/user/%name-remote.socket
%_prefix/lib/systemd/user/%name-remote@.service
%_prefix/lib/systemd/user/sockets.target.wants/%name-remote.socket
%endif

%files -n lib%name
%doc %name/pkcs11.conf.example
%doc AUTHORS COPYING NEWS README
%_libdir/lib%name.so.*
%_libdir/%name-proxy.so
%dir %_libdir/pkcs11/
%dir %_libexecdir/%name
%dir %_datadir/%name
%dir %_datadir/%name/modules
%dir %_sysconfdir/pkcs11
%dir %_sysconfdir/pkcs11/modules
%{?_enable_doc:%_man5dir/pkcs11.conf.*}

%exclude %_sysconfdir/pkcs11/pkcs11.conf.example
%exclude %_libdir/pkcs11/*.la

%files -n lib%name-devel
%_includedir/%name-1
%_libdir/lib%name.so
%_pkgconfigdir/%name-1.pc

%if_enabled doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name
%endif

%if_enabled trust_module
%files trust
%_bindir/trust
%_libdir/pkcs11/%name-trust.so
%_datadir/%name/modules/%name-trust.module
%_libexecdir/%name/%name-extract-trust
%_libexecdir/%name/trust-extract-compat
%{?_enable_doc:%_man1dir/trust.*}
%_altdir/libnssckbi-%name
%endif

%files server
%_libdir/pkcs11/%name-client.so
%_libexecdir/%name/%name-server

%files checkinstall
%changelog
* Thu Jun 04 2020 Andrew Savchenko <bircoph@altlinux.org> 0.23.15-alt2
- Add rpm-macros-alternatives build dependency for %%_altdir.

* Tue Apr 02 2019 Mikhail Efremov <sem@altlinux.org> 0.23.15-alt1
- Changes from upstream:
  + modules: Fix index used in call to p11_dict_remove().
  + Fix Win32 p11_dl_error crash.
  + modules: check gl.modules before iterates on it when freeing.
  + trust: Ignore unreadable content in anchors.
  + extract-jks: Prefer _p11_extract_jks_timestamp to SOURCE_DATE_EPOCH.
- Drop proxy-refresh-slots.patch.
- 0.23.15.

* Tue May 08 2018 Mikhail Efremov <sem@altlinux.org> 0.23.9-alt5
- Fix alternatives file.

* Wed Apr 04 2018 Michael Shigorin <mike@altlinux.org> 0.23.9-alt4
- Fix doc knob.

* Tue Jan 09 2018 Mikhail Efremov <sem@altlinux.org> 0.23.9-alt3
- Simplify checkinstall.
- Fix checkinstall group and description.
- Require p11-kit bundle instead of ca-certificates.

* Fri Dec 29 2017 Mikhail Efremov <sem@altlinux.org> 0.23.9-alt2
- Rename and package alternative file for libnssckbi.so.
- Add checkinstall subpackage.
- Use ca-certificates with p11-kit support.
- p11-kit-extract-trust: Run update-ca-trust.
- Don't use libfreebl3 for hashes.
- Re-split and rename package.

* Mon Oct 16 2017 Paul Wolneykien <manowar@altlinux.org> 0.23.9-alt1
- Exclude the alteranatives file for libnssckbi.so.
- Patch the sources just after unpacking them.
- Release 0.23.9 (thx Daiki Ueno).

* Wed Sep 06 2017 Paul Wolneykien <manowar@altlinux.org> 0.23.8-alt2
- Refresh the slot list each time C_GetSlotList() is called (patch).

* Thu Aug 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23.8-alt1
- 0.23.8 (0.23.7-24-g26312a8)

* Sun Jun 18 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23.7-alt1
- 0.23.7

* Mon Mar 06 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23.5-alt1
- 0.23.5

* Sat Feb 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.23.4-alt1
- 0.23.4

* Fri Dec 23 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.3-alt1
- 0.23.3

* Sun Jan 17 2016 Yuri N. Sedunov <aris@altlinux.org> 0.23.2-alt1
- 0.23.2

* Wed Dec 02 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.1-alt1
- 0.23.1 (ALT #31583)

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 0.22.1-alt1
- 0.22.1

* Tue Oct 07 2014 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Wed Sep 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.21.2-alt1
- 0.21.3

* Mon Jul 07 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.3-alt1
- 0.20.3

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.2-alt1
- 0.20.2

* Wed Oct 09 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.1-alt1
- 0.20.1

* Wed Sep 11 2013 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Wed Aug 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.5-alt1
- 0.18.5

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.3-alt1
- 0.18.3

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.2-alt1
- 0.18.2

* Fri Apr 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.18.1-alt1
- 0.18.1

* Wed Apr 10 2013 Dmitry V. Levin <ldv@altlinux.org> 0.18.0-alt1
- Updated to 0.18.0 (stable).

* Sat Mar 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.17.5-alt1
- 0.17.5

* Sat Mar 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.17.4-alt1
- 0.17.4 (unstable)

* Wed Mar 13 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.4-alt1
- 0.16.4
- used %_datadir/pki/ca-trust-source and %_sysconfdir/pki/ca-trust/source
  as system CA anchors paths
- new -trust subpackage with system trust PKCS#11 module that provides
  an alternative to libnss module

* Sun Mar 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.3-alt1
- 0.16.3

* Tue Mar 05 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Tue Feb 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.15.2-alt1
- 0.15.2

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.14-alt1
- 0.14

* Sun Mar 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12-alt1
- 0.12
- %%check section

* Thu Nov 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- 0.9

* Sun Sep 18 2011 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Wed Aug 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- first build for Sisyphus

