%define _unpackaged_files_terminate_build 1

Name: cuneiform
Version: 1.1.0
Release: alt5

Summary: Cuneiform is an OCR system originally developed and open sourced by Cognitive technologies.
Summary(ru_RU.KOI8-R): Программа распознавания символов (OCR) Cuneiform, Linux-версия

License: BSD-style
Group: Graphics
Url: https://launchpad.net/cuneiform-linux

# http://launchpad.net/%name-linux/%version/%version/+download/%name-linux-%version.tar.bz2
Source: %name-%version.tar

# Man page from Gentoo
Source1: cuneiform.1

# Patches from Debian
Patch1: graphicsmagick.diff
Patch2: libm.diff
Patch3: c-assert.diff
Patch4: fix_buffer_overflow.diff
Patch5: fix_buffer_overflow_2.diff
Patch6: gcc-6.patch
Patch7: typos.patch
Patch8: strings.patch

# Patches from Gentoo
Patch50: cuneiform-1.1.0-gcc7.patch

Requires: %name-data

BuildRequires: gcc-c++ cmake
BuildRequires: libGraphicsMagick-devel libGraphicsMagick-c++-devel

%description
Cuneiform is an OCR system originally developed and open sourced by
Cognitive technologies. This project aims to create a fully portable
version of Cuneiform.

%description -l ru_RU.KOI8-R
Программа распознавания символов (OCR) Cuneiform, некогда очень
популярная в нашей стране, была выложена компанией Cognitive
Technologies в свободный доступ в 2008 году. Проект cuneiform-linux
ставит своей целью полное портирование и дальнейшее развитие Cuneiform
под Linux и другие операционные системы.

%package data
Summary: Language support and other data files required for Cuneiform OCR
Summary(ru_RU.KOI8-R): Поддержка различных языков и другие файлы с данными для OCR Cuneiform
Group: Graphics
BuildArch: noarch

%description data
Language support and other data files required for Cuneiform OCR

%description -l ru_RU.KOI8-R data
Поддержка различных языков и другие файлы с данными для OCR Cuneiform

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch50 -p1

%build
%add_optflags -fcommon
%cmake
%cmake_build

%install
%cmakeinstall_std

install -D -p -m644 %SOURCE1 %buildroot%_man1dir/cuneiform.1

%files
%_bindir/%name
%_libdir/*.so*
%_includedir/%name.h
%_man1dir/*.1*

%files data
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Mon Mar 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt5
- Applied patches from Debian and Gentoo and fixed build with gcc-10.

* Tue Oct 02 2018 Fr. Br. George <george@altlinux.ru> 1.1.0-alt4
- Version up

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 1.0-alt4
- Rebuilt for ImageMagick

* Thu Jan 19 2017 Fr. Br. George <george@altlinux.ru> 1.0-alt3.qa2
- Rebuilt for gcc6

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.0-alt3.qa1
- Rebuilt for gcc5 C++11 ABI.

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 1.0-alt3
- Rebuild with new libImageMagick

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 1.0-alt2.1
- Rebuild with new libImageMagick

* Mon Feb 28 2011 Sergey Alembekov <rt@altlinux.ru> 1.0-alt2
- Closes bug: #21335
- fix debuginfo.req errors
- remove circular dependencies on cuneiform-data 

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.0-alt1.1
- Rebuild with new libImageMagick

* Fri Jul 16 2010 Sergey Alembekov <rt@altlinux.ru> 1.0-alt1
- upstream version 1.0
- remove broken libidl patch

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1.1
- Rebuilt with libMagick++.so.2.

* Tue Mar 03 2009 Sergey Alembekov <rt@altlinux.ru> 0.6-alt1
- new upstream version

* Tue Dec 16 2008 Sergey Alembekov <rt@altlinux.ru> 0.5.0-alt1.1
- add forgotten libidl patch
- add cuneiform-data to requires

* Mon Dec 15 2008 Sergey Alembekov <rt@altlinux.ru> 0.5.0-alt1
- New 0.5 version build

* Sat Aug 16 2008 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build from scratch
- Thanks thresh@ for libdl hint

