
%define sover 5
%define libwcs libwcs%sover

Name: wcslib
Version: 5.19.1
Release: alt2

Group: System/Libraries
Summary: An implementation of the FITS World Coordinate System standard
Url: http://www.atnf.csiro.au/people/mcalabre/WCS/
License: LGPLv3+ / GPLv3+

Source: %name-%version.tar

# Automatically added by buildreq on Mon Nov 11 2013 (-bi)
# optimized out: elfutils gnu-config pkg-config python-base python3 python3-base ruby ruby-stdlibs
#BuildRequires: flex libcfitsio-devel rpm-build-python3 rpm-build-ruby
BuildRequires(pre): rpm-build-ubt
BuildRequires: flex libcfitsio-devel zlib-devel

%description
WCSLIB is a library that implements the "World Coordinate System" (WCS)
convention in FITS (Flexible Image Transport System)

%package -n %libwcs
Group: System/Libraries
Summary: An implementation of the FITS World Coordinate System standard
License: LGPLv3+
%description -n %libwcs
WCSLIB is a library that implements the "World Coordinate System" (WCS)
convention in FITS (Flexible Image Transport System)

%package devel
Group: Development/C
Summary: Libraries, includes, etc. used to develop an application with %name
License: LGPLv3+
%description devel
These are the files needed to develop an application using %name.

%package utils
Summary: Utility programs provided by %name
Group: Development/Other
License: GPLv3+
%description utils
Utils provided with %name

%prep
%setup

%build
%add_optflags %optflags_shared
%configure \
    --disable-fortran \
    --disable-static \
    #
%make -C C
%make_build

%install
%make install DESTDIR=%buildroot
# cleanup
rm -rf %buildroot/%_libdir/*.a
rm -rf %buildroot/%_docdir/wcslib-*

%files -n %libwcs
%doc README
%_libdir/libwcs.so.%sover
%_libdir/libwcs.so.%sover.*

%files devel
%doc html wcslib.pdf README
%_libdir/*.so
%_libdir/pkgconfig/wcslib.pc
%_includedir/wcslib
%_includedir/wcslib-%version

%files utils
%_bindir/*
%_man1dir/*

%changelog
* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 5.19.1-alt2
- NMU: remove %ubt from release

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 5.19.1-alt1%ubt
- new version

* Fri Jul 27 2018 Sergey V Turchin <zerg@altlinux.org> 5.18-alt1%ubt
- new version

* Tue Mar 22 2016 Sergey V Turchin <zerg@altlinux.org> 5.14-alt1
- new version

* Mon Mar 21 2016 Sergey V Turchin <zerg@altlinux.org> 4.25.1-alt1
- new version

* Thu Jun 19 2014 Sergey V Turchin <zerg@altlinux.org> 4.23-alt0.M70P.1
- built for M70P

* Thu Jun 05 2014 Sergey V Turchin <zerg@altlinux.org> 4.23-alt1
- new version

* Tue Mar 25 2014 Sergey V Turchin <zerg@altlinux.org> 4.21-alt1
- new version

* Fri Nov 15 2013 Sergey V Turchin <zerg@altlinux.org> 4.19-alt2
- bump release to prevent spam from autoimports robot

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.19-alt0.M70P.1
- built for M70P

* Mon Nov 11 2013 Sergey V Turchin <zerg@altlinux.org> 4.19-alt1
- initial build
