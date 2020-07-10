%set_verify_elf_method unresolved=relaxed
%add_findreq_skiplist  %_libdir/trikStudio/*.so* %_libdir/trikStudio/plugins/tools/kitPlugins/*.so %_libdir/trikStudio/plugins/tools/*.so %_libdir/trikStudio/plugins/editors/*.so
%def_without separate_trikruntime
%def_without sanitize
%def_without debug
%define appname trik-studio-junior

Name: trikStudioJunior
Version: 2020.2
Release: alt1
Summary: Intuitive graphical programming environment
Summary(ru_RU.UTF-8): Интуитивно-понятная графическая среда программирования
License: Apache-2.0
Group: Education
Url: https://github.com/trikset/trik-studio

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel qt5-script-devel qt5-multimedia-devel libusb-devel libudev-devel libgmock-devel
BuildRequires: libqscintilla2-qt5-devel zlib-devel libquazip-qt5-devel python3-dev
# Workaround due project build with -fsanitize=undefined natively
# https://bugzilla.altlinux.org/show_bug.cgi?id=38106
#if_with sanitize
BuildRequires: libubsan-devel-static
#endif
BuildRequires: rsync qt5-tools

Requires: libquazip-qt5
Requires: %name-data = %version-%release
Conflicts: lib%name

%description

An intuitive programming environment allows you to program with
using a sequence of pictures. TRIK Studio Junior is an opportunity
build a continuous learning process, do programming
simple and fun.

The environment has a common interface with the TRIK Studio robot programming environment,
allows you to program a simulation model and a real robot
Python and JavaScript are both visual and text devices.

%description -l ru_RU.UTF-8
Интуитивно-понятная среда программирования позволяет программировать с
помощью последовательности картинок. TRIK Studio Junior — это возможность
построить непрерывный процесс образования, сделать обучение программированию
простым и увлекательным.

Среда имеет общий интерфейс со средой программирования роботов TRIK Studio,
позволяющей программировать имитационную модель и реальные робототехнические
устройства на визуальном языке и текстовых языках Python и JavaScript.


%package data
Summary: Data files for %name
Group: Education
BuildArch: noarch

%description data
Data files for %name

%prep
%setup
%patch -p1
sed -e '2 a export LD_LIBRARY_PATH=%_libdir\/%name\/' -i installer/platform/trikStudio.sh
sed -e 's|^trik-studio|%_libdir/%name/trik-studio|' -i installer/platform/trikStudio.sh

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
mv %buildroot%_bindir/%appname %buildroot%_libdir/%name/
ln -fs %name %buildroot%_bindir/%appname

rm -rf %buildroot%_sysconfdir/trik
rm -f %buildroot%_prefix/lib/libqslog*.so*
rm -f %buildroot%_prefix/lib/libtrik*.so*
rm -rf %buildroot%_datadir/trikRuntime
rm -rf %buildroot%_prefix/local/share/qslog/
rm -rf %buildroot%_includedir/trik*
rm -rf %buildroot%_includedir/qslog*
rm -rf %buildroot%_includedir/QsLog*

rm -f %buildroot/lib/*PythonQt_QtAll* %buildroot/include/PythonQt_QtAll.h
rm -f %buildroot%_libdir/%name/plugins/tools/kitPlugins/librobots-null-interpreter.so

pushd bin/release
for d in examples help translations images; do
    cp -fr $d %buildroot%_datadir/%name/
done
#cp -fr trikSharp %buildroot%_libdir/%name/

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

%changelog
* Tue Jun 23 2020 Valery Sinelnikov <greh@altlinux.org> 2020.2-alt1
- Initial build for Sisyphus

