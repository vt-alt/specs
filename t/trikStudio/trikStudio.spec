%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist  %_libdir/trikStudio/*.so* %_libdir/trikStudio/plugins/tools/kitPlugins/*.so %_libdir/trikStudio/plugins/tools/*.so %_libdir/trikStudio/plugins/editors/*.so
%def_without separate_trikruntime
%define trikrunime_version 3.2.0-aa444d318d338cce56a7bd308ed3b7d728aa6d4e
Name: trikStudio
Version: 3.2.0
Release: alt3
Summary: Intuitive programming environment robots
Summary(ru_RU.UTF-8): Интуитивно-понятная среда программирования роботов
License: Apache License 2.0
Group: Education
Url: https://github.com/qreal/qreal/

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar.gz

BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel qt5-script-devel qt5-multimedia-devel libusb-devel libudev-devel libgmock-devel

Requires: %name-data = %version-%release
Conflicts: lib%name

%description
Intuitive programming environment allows you to program robots using a sequence
of pictures. With TRIK Studio programming is easy and fun.

TRIK Studio perfectly as universal for teaching programming, provided the
transition from the chart to the textual programming language that is planned to
implement the language of block diagrams. The environment is also implemented
programming robots Lego Mindsorms NXT 2.0 and EV3, but the possibility of such
robots are very limited in comparison with the TRIC .

%description -l ru_RU.UTF-8
Интуитивно-понятная среда программирования позволяет программировать роботов с
помощью последовательности картинок. С TRIK Studio программирование становится
простым и увлекательным.

TRIK Studio прекрасно подходит как универсальное ПО преподавания основ
программирования, предусмотрен переход от диаграмм к текстовым языкам
программирования, планируется реализация языка блок-схем. В среде также
реализовано программирование роботов Lego Mindsorms NXT 2.0 и EV3, но
возможности таких роботов сильно ограничены в сравнении с ТРИК.

%package data
Summary: Data files for %name
Group: Education
BuildArch: noarch

%description data
Data files for %name

%package -n trikRuntime
Summary: Trik runtime libraries for %name
Group: Education
BuildArch: noarch

%description -n trikRuntime
Trik runtime libraries for %name

%package -n trikRuntime-devel
Summary: Trik runtime development files for %name
Group: Education
BuildArch: noarch

%description -n trikRuntime-devel
Trik runtime development files for %name

%prep
%setup
sed -e '2 a export LD_LIBRARY_PATH=%_libdir\/trikStudio\/' -i installer/platform/trikStudio.sh
cd plugins/robots/thirdparty/trikRuntime
tar -xf trikRunTime-%trikrunime_version.tar.bz2

%build
%qmake_qt5 -r CONFIG-=debug CONFIG+=release CONFIG+=no_rpath PREFIX=%_prefix LIBDIR=%_libdir qrealRobots.pro
#%%qmake_qt5 -r 'QMAKE_CXXFLAGS=-pipe -Wall -g -O2 -fPIC -DPIC -std=c++0x' CONFIG-=debug CONFIG+=no_rpath CONFIG+=release PREFIX=/usr qrealRobots.pro
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
mv %buildroot%_libdir/*.so* %buildroot%_libdir/%name
%if_with separate_trikruntime
mv %buildroot%_prefix/lib/libqslog*.so* %buildroot%_libdir
mv %buildroot%_prefix/lib/libtrik*.so* %buildroot%_libdir
%else
rm -rf %buildroot%_sysconfdir/trik
rm -f %buildroot%_prefix/lib/libqslog*.so*
rm -f %buildroot%_prefix/lib/libtrik*.so*
rm -rf %buildroot%_datadir/trikRuntime
rm -rf %buildroot%_prefix/local/share/qslog/
rm -rf %buildroot%_includedir/trik*
rm -rf %buildroot%_includedir/qslog*
rm -rf %buildroot%_includedir/QsLog*
%endif

%files
%_bindir/*
%_libdir/%name
%_sysconfdir/%name.config

%files data
%_datadir/%name
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
%_desktopdir/*
%doc LICENSE NOTICE README.md

%if_with separate_trikruntime
%files -n trikRuntime
%_sysconfdir/trik
%_libdir/libqslog*.so.*
%_libdir/libtrik*.so.*
%_datadir/trikRuntime

%files -n trikRuntime-devel
%_libdir/libqslog*.so
%_libdir/libtrik*.so
%_includedir/trik*
%_includedir/qslog*
%_includedir/QsLog*
%endif

%changelog
* Thu Jun 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.2.0-alt3
- Fix program name in desktop file (Closes: 36823)

* Fri Feb 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.2.0-alt2
- Fix installation on different 64-bit platforms via LIBDIR as qmake option

* Wed Feb 13 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.2.0-alt1
- New version 3.2.0 with trikRuntime from trikset git submodule:
  https://github.com/trikset/trikRuntime

* Fri Jul 15 2016 Anton Midyukov <antohami@altlinux.org> 3.1.4-alt1
- New version 3.1.4
- Remove install.patch

* Tue Jun 21 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt5.91af0cec.1
- New snapshot
- Replaced library
- Packages libtrikStudio, libtrikStudio-devel united into a package trikStudio.

* Sat Mar 26 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt4.30210b3a.1
- Move config file from package trikStudio-data in package trikStudio
- Added conflict with libqscintilla2-qt4-devel.

* Wed Mar 23 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt3.30210b3a.1
- fix install.patch

* Wed Mar 23 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt2.30210b3a.1
- new package libtrikStudio
- rename package trikStudio-devel to libtrikStudio-devel

* Mon Mar 21 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1.30210b3a.1
- Fix altlinux-policy-shared-lib-contains-devel-so
- Exclude libqextserialport (it has in the repository)
- Diveded into 3 package

* Fri Mar 18 2016 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt0.1.30210b3a
- Initial build for ALT Linux Sisyphus (Closes: 31733).
