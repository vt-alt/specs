Name: libbsd
Version: 0.9.1
Release: alt2

Summary: Library providing BSD-compatible functions for portability
License: BSD and ISC and Copyright only and Public Domain
Group: System/Libraries

Url: http://libbsd.freedesktop.org/
Source: http://libbsd.freedesktop.org/releases/%name-%version.tar
Patch: libbsd-0.9.1-alt-e2k.patch
Packager: Vitaly Lipatov <lav@altlinux.ru>

%description
libbsd provides useful functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port
projects with strong BSD origins, without needing to embed the same
code over and over again on each project.

%package devel
Summary: Development files for libbsd
Group: Development/Other
Requires: %name = %version-%release
Requires: pkg-config

%description devel
Development files for the libbsd library.

%prep
%setup
%ifarch %e2k
%patch -p1
%endif

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

# don't want static library
rm %buildroot%_libdir/%name-ctor.a

rm %buildroot%_man3dir/strlcpy*
rm %buildroot%_man3dir/strlcat*
# conflicts with setproctitle-devel
rm %buildroot/%_man3dir/setproctitle*

%files
%doc COPYING README TODO ChangeLog
%_libdir/%name.so.*

%files devel
%_man7dir/*
%_man3dir/*.3bsd.*
%_includedir/bsd/
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-ctor.pc
%_pkgconfigdir/%name-overlay.pc

%changelog
* Sat Jul 13 2019 Michael Shigorin <mike@altlinux.org> 0.9.1-alt2
- E2K: initial architecture support (patch proposed upstream)
- minor spec cleanup

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Sat Sep 13 2014 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Fri Dec 16 2011 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- initial build for ALT Linux Sisyphus

* Sat Oct 08 2011 Eric Smith <eric@brouhaha.com> - 0.3.0-1
- Update to latest upstream release.
- Removed Patch0, fixed upstream.
- Removed BuildRoot, clean, defattr.

* Fri Jan 29 2010 Eric Smith <eric@brouhaha.com> - 0.2.0-3
- changes based on review by Sebastian Dziallas

* Fri Jan 29 2010 Eric Smith <eric@brouhaha.com> - 0.2.0-2
- changes based on review comments by Jussi Lehtola and Ralf Corsepious

* Thu Jan 28 2010 Eric Smith <eric@brouhaha.com> - 0.2.0-1
- initial version
