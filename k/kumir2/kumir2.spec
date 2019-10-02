%def_with devel

Name: kumir2
Version: 2.1.0
Release: alt7.gita3631abb

Summary: New version of Kumir - simple programming language and IDE for teaching programming
Summary(ru_RU.UTF-8): Новая версия системы Кумир - простого учебного языка программирования и среды разработки

License: GPL
Group: Education
URL:  https://www.niisi.ru/kumir/
#VCS: https://github.com/a-a-maly/kumir2/
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel >= 5.3
BuildRequires: qt5-svg-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-tools
BuildRequires: python3 >= 3.2
BuildRequires: git-core
BuildRequires: boost-devel

Source: %name-%version.tar
Patch1: kumir2-alt-fix-LIB_BASENAME.patch

%description
Implementation of Kumir programming language, designed by academician
Ershov. It has very simple syntax, also known as "Russian algorithmical
language". Includes compiler, runtime, IDE and  modules "Robot", "Draw",
"Turtle" and some others.

This is a second generation of well-known Kumir system. ALT Linux
package also supports a real world actor from the UMKI project:
http://vinforika.ru/umki/

%description -l ru_RU.UTF-8
Кумир - это учебный язык программирования, описанный в учебнике
А.Г.Кушниренко, и среда разработки. Он имеет простой синтаксис,
известный также как "русский алгоритмический язык". В состав среды также
входят канонические исполнители Робот, Чертежник, Черепаха и другие,
что делает Кумир очень удобным для начального обучения программированию.

Пакет kumir2 содержит новую реализацию системы Кумир. Версия пакета
ALT Linux включает также поддержку исполнителя, являющегося объектом
реального мира -- разработанного в рамках проекта УМКИ
радиоуправляемого робота.

%if_with devel
%package devel
Group: Education
Summary: Development files for Kumir
Requires: %name = %EVR

%description devel
Development files for Kumir.
%endif

%prep
%setup
%patch1 -p1
sed -i "s/^Categories=.*$/Categories=Education;Qt;ComputerScience;/" *.desktop
# Remove bundled boost
rm -rf src/3rdparty/boost*

%build
export PATH=%_qt5_bindir:$PATH
%cmake  -DUSE_QT=5 \
	-DLIB_BASENAME=%_lib
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/%name
%_datadir/%name
%_datadir/mime/packages/*.xml
%_desktopdir/*
%_iconsdir/*/*/*/*

%if_with devel
%ifarch %ix86 x86_64
%files devel
%_includedir/kumir2-libs
%_includedir/kumir2
%_libdir/cmake/Kumir2
%endif
%endif

%changelog
* Tue Oct 01 2019 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt7.gita3631abb
- New snapshot.
- Build with Qt5.
- Fix URL, maintainet and upstream source.
- Add devel package.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt6
- Remove Umki support (ALT #32162).
- Fix build on ppc64le.

* Wed Apr 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt5
- fixed packaging on aarch64

* Wed Jan 27 2016 Dmitry Derjavin <dd@altlinux.org> 2.1.0-alt4
- using system boost;
- URL fixed;
- description fixed.

* Wed Jan 27 2016 Dmitry Derjavin <dd@altlinux.org> 2.1.0-alt3
- Moved to 2.1.0 release from github.com/victor-yacovlev/kumir2.
- UMKI actor patch added from UMKI-1.8 codebase.

* Wed Nov 11 2015 Denis Kirienko <dk at altlinux.org> 2.1.0-alt2
- Increase release to alt2

* Wed Nov 11 2015 Denis Kirienko <dk at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Sun Jun 15 2014 Denis Kirienko <dk@altlinux.org> 2.1.0-alt0.beta5
- Version 2.1.0-beta5

* Thu Jan 09 2014 Denis Kirienko <dk@altlinux.org> 2.1.0-alt0.beta4
- Version 2.1.0-beta4

* Tue Nov 05 2013 Denis Kirienko <dk@altlinux.org> 2.0.99-alt1
- Version 2.1.0-beta1

* Tue Mar 20 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.99.0.alpha7-alt2
- rebuilt with optflags

* Sat Aug 20 2011 Denis Kirienko <dk@altlinux.ru> 1.99.0.alpha7-alt1
- Initial build for Sisyphus - alpha-version, only for testing.
