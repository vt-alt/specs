Name: kumir2
Version: 2.1.0
Release: alt6

Summary: New version of Kumir - simple programming language and IDE for teaching programming
Summary(ru_RU.UTF-8): Новая версия системы Кумир - простого учебного языка программирования и среды разработки

License: GPL
Group: Education
Url: https://github.com/victor-yacovlev/kumir2
Packager: Denis Kirienko <dk@altlinux.ru>

BuildRequires(pre): cmake
BuildPreReq: libqt4-devel gcc-c++ python-modules python-modules-json boost-devel
Requires: libqt4-core

Source: %name-%version.tar
Patch1: kumir2-2.1.0-actor_umki.patch
Patch2: kumir2-alt-fix-LIB_BASENAME.patch

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

%prep
%setup
sed -i "s/^Categories=.*$/Categories=Education;Qt;ComputerScience;/" *.desktop
#patch1 -p1
%patch2 -p2

%build
rm -rf src/3rdparty/boost-1.54.0
%cmake \
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

%changelog
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
