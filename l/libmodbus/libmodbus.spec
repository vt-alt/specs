%def_with doc
Name: libmodbus
Version: 3.1.6
Release: alt2

Summary: A Modbus library in C, which supports RTU communication over a serial line or a TCP link

License: LGPL V3+
Url: http://www.libmodbus.org
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://libmodbus.org/releases/libmodbus-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Tue Mar 30 2010
BuildRequires: gcc-c++
%if_with doc
BuildRequires: xmlto asciidoc-a2x
%endif

%description
A Modbus library for Linux (and OSX) wrote in C and which supports
RTU communication over a serial line or a TCP link. Clean and fast!
Supports controling an RTU and being an RTU.

%package devel
Summary: Headers and development files of %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the headers and various development files needed
for compiling or development of applications that wants C++ interface
of %name library.

%prep
%setup

%build
%autoreconf
%configure \
%if_without doc
    --without-documentation \
%endif
    %nil
%make_build

%install
#mkdir -p -m755 %buildroot/
%makeinstall_std
rm -rfv %buildroot%_docdir/%name/
#mkdir -p -m755 %buildroot%_datadir/libmodbus/
#ls -lRh %buildroot/

%files
%doc AUTHORS MIGRATION NEWS COPYING* README.md
%_libdir/libmodbus.so.*

%files devel
%_libdir/libmodbus.so
%_pkgconfigdir/libmodbus.pc
%dir %_includedir/modbus/
%_includedir/modbus/modbus.h
%_includedir/modbus/modbus-rtu.h
%_includedir/modbus/modbus-tcp.h
%_includedir/modbus/modbus-version.h
%if_with doc
%_man3dir/*
%_man7dir/*
%endif

%changelog
* Sat Aug 22 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt2
- really pack 3.1.6 (ALT bug 38837)

* Mon Oct 21 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- new version 3.1.6 (with rpmrb script) (ALT bug 37365)

* Mon Nov 21 2016 Terechkov Evgenii <evg@altlinux.org> 3.1.4-alt1
- 3.1.4 (ALT#30848)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 3.0.3-alt1
- new version 3.0.3 (with rpmrb script)

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- new version 3.0.1 (with rpmrb script)

* Thu Feb 10 2011 Vitaly Lipatov <lav@altlinux.ru> 2.9.3-alt1
- new version 2.9.3 (with rpmrb script)

* Tue Mar 30 2010 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Linux Sisyphus

* Sun Mar 22 2009 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.3-1
- new upstream release

* Sun Aug 10 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.2-1
- new upstream release

* Fri Jul 2 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.1-1
- new upstream release

* Fri May 2 2008 Stéphane Raimbault <stephane.raimbault@gmail.com> - 2.0.0-1
- integrate extern_for_cpp in upstream.
- update the license to version LGPL v3.

* Tue Apr 30 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.9.0-2
- get the license corrected in the spec file.
- add a URL for where to find libmodbus.
- tweak the summary and description.

* Tue Apr 29 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.9.0-1
- upgrade to latest upstream (pre-release)
- port extern_for_cpp patch to 1.9.0

* Tue Apr 29 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.2.4-2_tad
- add a patch to allow compiling with c++ code.

* Mon Apr 28 2008 Todd Denniston <Todd.Denniston@ssa.crane.navy.mil> - 1.2.4-1_tad
- build spec file.
- include patch for controling error-treat.
