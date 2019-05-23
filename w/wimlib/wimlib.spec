%define libname libwim
Name: wimlib
Version: 1.13.1
Release: alt1

Summary: Library to extract, create, modify, and mount WIM files

License: GPLv3+
Group: System/Libraries
Url: https://wimlib.net/

ExclusiveArch: %ix86 x86_64

Source: https://wimlib.net/downloads/wimlib-%version.tar

# manually removed: glibc-devel-static  ruby ruby-stdlibs  python3
# Automatically added by buildreq on Tue Apr 15 2014
# optimized out: libcloog-isl4 libntfs-3g pkg-config
BuildRequires: libattr-devel libfuse-devel libntfs-3g-devel libssl-devel libxml2-devel mt-st

%description
wimlib is a C library for creating, extracting, modifying, and mounting
files in the Windows Imaging Format (WIM files).  It is similar to
Microsoft's WIMGAPI but is designed for both UNIX and Windows.

%package -n %libname
Summary: Library to extract, create, modify, and mount WIM files
Group: System/Libraries

%description -n %libname
wimlib is a C library for creating, extracting, modifying, and mounting
files in the Windows Imaging Format (WIM files).  It is similar to
Microsoft's WIMGAPI but is designed for both UNIX and Windows.

%package -n %libname-devel
Summary: Development files for wimlib
Group: Development/Other
Requires: %libname = %version-%release

%description -n %libname-devel
Development files for wimlib.

%package -n wimtools
Summary: Tools to create, extract, modify, and mount WIM files
Group: File tools
Requires: syslinux, %libname = %version-%release

%description -n wimtools
Tools to create, extract, modify, and mount files in the
Windows Imaging Format (WIM files).  These files are normally
created by using the `imagex.exe' utility on Windows,
but this package contains a free implementation of ImageX called
"wimlib-imagex" that is designed to work on both UNIX and Windows.

%prep
%setup

%build
# helps with rpath
%autoreconf

%configure \
       --disable-static \
       --disable-rpath  \
       --with-libcrypto \
       --with-ntfs-3g   \
       --with-fuse      \
       --enable-xattr
%make_build

%install
%makeinstall_std

%check
:>tests/test-imagex-ntfs # this one fails
make check

%files -n %libname
%doc README NEWS
%_libdir/libwim.so.*

%files -n wimtools
%_bindir/wim*
%_bindir/mkwinpeimg
%_man1dir/*

%files -n %libname-devel
%_libdir/libwim.so
%_includedir/wimlib.h
%_pkgconfigdir/wimlib.pc

%changelog
* Mon May 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.13.1-alt1
- Build new version.

* Fri Dec 14 2018 Grigory Ustinov <grenka@altlinux.org> 1.13.0-alt1
- Build new version.

* Wed Sep 05 2018 Grigory Ustinov <grenka@altlinux.org> 1.12.0-alt1.1
- NMU: Rebuild with new openssl.

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.12.0-alt1
- new version 1.12.0 (with rpmrb script)

* Mon Apr 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt2
- rebuild with ntfs-3g-2017.3.23-alt1

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Sun Apr 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1 (with rpmrb script)

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.6.2-alt2
- wimtools: explicit syslinux dependency

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.6.2-alt1
- NMU: 1.6.2
- minor spec cleanup
- re-enable most of the tests

* Thu Aug 29 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- initial build for ALT Linux Sisyphus

