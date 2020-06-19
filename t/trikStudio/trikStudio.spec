%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist  %_libdir/trikStudio/*.so* %_libdir/trikStudio/plugins/tools/kitPlugins/*.so %_libdir/trikStudio/plugins/tools/*.so %_libdir/trikStudio/plugins/editors/*.so
%def_without separate_trikruntime
%def_without sanitize
%def_without debug
%define appname trik-studio

Name: trikStudio
Version: 2020.3
Release: alt1
Summary: Intuitive programming environment robots
Summary(ru_RU.UTF-8): Интуитивно-понятная среда программирования роботов
License: Apache-2.0
Group: Education
Url: https://github.com/qreal/qreal/

Packager: Evgeny Sinelnikov <sin@altlinux.org>
Source: %name-%version.tar
Patch: %name-%version-alt.patch
Patch1: gamepad.patch

BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel qt5-script-devel qt5-multimedia-devel libusb-devel libudev-devel libgmock-devel
BuildRequires: libqscintilla2-qt5-devel zlib-devel libquazip-qt5-devel python3-dev libhidapi-devel libusb-devel
# Workaround due project build with -fsanitize=undefined natively
# https://bugzilla.altlinux.org/show_bug.cgi?id=38106
#if_with sanitize
BuildRequires: libubsan-devel-static
#endif
BuildRequires: rsync qt5-tools

Requires: libquazip-qt5 libhidapi
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
%patch -p1
sed -e '2 a export LD_LIBRARY_PATH=%_libdir\/%name\/' -i installer/platform/trikStudio.sh
sed -e 's|^trik-studio|%_libdir/%name/trik-studio|' -i installer/platform/trikStudio.sh

pushd plugins/robots/thirdparty/Box2D
tar -xf Box2D.tar.bz2
popd
pushd plugins/robots/thirdparty/trikRuntime
tar -xf trikRuntime.tar.bz2
popd
pushd thirdparty/gamepad
rm -rf qscintilla quazip
tar -xf gamepad.tar.bz2
%patch1
popd
pushd qrgui/thirdparty
tar -xf qt-solutions.tar.bz2
popd

%build
%qmake_qt5 -r \
%if_with debug
    CONFIG+=debug CONFIG-=release \
%else
    CONFIG-=debug CONFIG+=release \
%endif
%if_with sanitize
    CONFIG+=!nosanitizers \
%endif
    CONFIG+=no_rpath \
    PREFIX=%_prefix LIBDIR=%_libdir studio.pro
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
mv %buildroot%_libdir/*.so* %buildroot%_libdir/%name
mv %buildroot%_bindir/trik-studio %buildroot%_libdir/%name/
ln -fs %name %buildroot%_bindir/trik-studio
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
rm -f %buildroot/lib/*PythonQt_QtAll* %buildroot/include/PythonQt_QtAll.h
rm -f %buildroot%_libdir/%name/plugins/tools/kitPlugins/librobots-null-interpreter.so

pushd bin/release
for d in examples help translations images; do
    cp -fr $d %buildroot%_datadir/%name/
done
#cp -fr trikSharp %buildroot%_libdir/%name/
cp -f gamepad %buildroot%_bindir/
mkdir -p %buildroot%_datadir/%name/languages
cp -f ../../thirdparty/gamepad/gamepad/languages/*.qm %buildroot%_datadir/%name/languages/
popd

%files
%_bindir/*
%_libdir/%name
%_sysconfdir/%appname.config

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
* Tue Jun 09 2020 Valery Sinelnikov <greh@altlinux.org> 2020.3-alt1
- Update to 2020.3

* Thu Apr 30 2020 Valery Sinelnikov <greh@altlinux.org> 2020.1-alt3
- Changing the path of the language catalog with translation for the gamepad

* Thu Apr 23 2020 Valery Sinelnikov <greh@altlinux.org> 2020.1-alt2
- Build with latest gamepad sources
- Copy language directory with translation for gamepad (Closes: 38375)

* Fri Apr 17 2020 Valery Sinelnikov <greh@altlinux.org> 2020.1-alt1
- Update to 2020.1

* Thu Apr 09 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt8
- Fix gamepad segfault during close application

* Fri Mar 20 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt7
- Fix to load default platform config

* Wed Mar 18 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt6
- Replace /etc/trikStudio.config settings to global settingsDefaultValues

* Wed Mar 18 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt5
- Add requirement to libhidapi for ev3 robots plugin
- Fix null model removing

* Fri Mar 13 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt4
- Disable sanitize_undefined due it produces false positives with derived
  objects causing the runtime error member with call on address which does
  not point to an object of type.

* Tue Feb 18 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt3
- Build with workaround force requirement to libubsan-devel-static
- Add missed requirement to libquazip-qt5

* Sun Feb 16 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt2
- Build with explicitly enable gcc sanitize options needs
  libubsan-devel-static as build requirement

* Fri Feb 14 2020 Valery Sinelnikov <greh@altlinux.org> 2019.8-alt1
- Update to 2019.8
- Change license to Apache-2.0

* Thu Nov 21 2019 Valery Sinelnikov <greh@altlinux.org> 2019.6-alt1
- New version 2019.6

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
