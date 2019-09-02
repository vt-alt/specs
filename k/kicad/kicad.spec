# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define majver 5.0

Name: kicad
Summary: An open source software for the creation of electronic schematic diagrams
Summary(ru_RU.UTF-8): Программа с открытым исходным кодом для проектирования электронных схем
Version: 5.1.4
Release: alt1
Epoch: 1
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch: fix_python_sitepackages_path.patch
Patch1: %name-5.1.0-nostrip.patch
License: GPLv2+
Group: Engineering
Url: https://code.launchpad.net/kicad
#Url: https://github.com/KiCad/kicad-source-mirror.git

BuildRequires(pre): cmake rpm-macros-cmake
#BuildRequires(pre): rpm-build-python3
#BuildRequires: python-module-wx4.0-devel
BuildRequires: boost-devel boost-asio-devel boost-asio-devel boost-context-devel boost-filesystem-devel boost-geometry-devel boost-interprocess-devel boost-locale-devel boost-program_options-devel
BuildRequires: ccmake gcc-c++
BuildRequires: libwxGTK3.1-devel
BuildRequires: libGLEW-devel libcairo-devel libssl-devel swig pkgconfig(gobject-2.0) libpcre-devel libpixman-devel pkgconfig(harfbuzz) pkgconfig(expat) pkgconfig(libdrm) pkgconfig(xdmcp) pkgconfig(xdamage) pkgconfig(xxf86vm) libcurl-devel
BuildRequires: doxygen
BuildRequires: dos2unix
BuildRequires: python-devel
BuildRequires: libglm-devel
BuildRequires: libuuid-devel
BuildRequires: ngspice-devel
BuildRequires: OCE-devel
BuildRequires: openmpi-devel
BuildRequires: ImageMagick-tools
BuildRequires: desktop-file-utils
Requires: %name-data = %EVR
#Requires: kicad-packages3D >= %majver
Requires: kicad-symbols >= %majver
Requires: kicad-footprints >= %majver
Requires: kicad-templates >= %majver
Requires: %name-doc >= %epoch:%majver
Requires: %name-i18n >= %majver

%description
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad is a set of four softwares and a project manager:

Kicad: Project manager.
Eeschema: Schematic entry.
Pcbnew: Board editor.
Cvpcb: Footprint selector for components used in the circuit design.
Gerbview: GERBER viewer (photoplotter documents).

%description -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Включает в себя редактор схем, средство трассировки печатных плат,
средства трёхмерного просмотра печатных плат в конечном виде.

Kicad состоит из 5 основных компонентов:

 * kicad — менеджер проектов
 * eeschema — редактор схем
 * pcbnew — редактор печатных плат
 * gerbview — просмотр GERBER
 * cvpcb — выбор мест для компонентов

На заметку:
Для использования рамки ГОСТ необходимо выбрать шаблон
gost_landscape.kicad_wks или gost_portrait.kicad_wks в диалоговом окне
"Настройки страницы" в поле "Файл описания разметки листа".
Стандартные файлы рамки (*.kicad_wks) находятся в %_datadir/kicad/template/.

%package data
Summary: An open source software for the creation of electronic schematic diagrams
Summary(ru_RU.UTF-8): Программа с открытым исходным кодом для проектирования электронных схем
Group: Sciences/Computer science
BuildArch: noarch
Requires: icon-theme-hicolor
%add_python_req_skip pcbnew

%description data
Kicad is an open source (GPL) software for the creation of electronic
schematic diagrams and printed circuit board artwork.

Kicad is a set of four softwares and a project manager:

Kicad: Project manager.
Eeschema: Schematic entry.
Pcbnew: Board editor.
Cvpcb: Footprint selector for components used in the circuit design.
Gerbview: GERBER viewer (photoplotter documents).

Package contains data files.

%description data -l ru_RU.UTF-8
Kicad - это программное обеспечение с открытым исходным кодом для
проектирования электронных схем и получения на их основе печатных плат.

Для использования рамки ГОСТ необходимо выбрать шаблон
gost_landscape.kicad_wks или gost_portrait.kicad_wks в диалоговом окне
"Настройки страницы" в поле "Файл описания разметки листа".
Стандартные файлы рамки (*.kicad_wks) находятся в %_datadir/kicad/template/.

Пакет содержит архитектурно-независимые файлы.

%prep
%setup -n %name-%version
#patch -p1
%patch1 -p1

%build    
%cmake \
    -DKICAD_SCRIPTING=OFF \
    -DKICAD_SCRIPTING_MODULES=OFF \
    -DKICAD_SCRIPTING_WXPYTHON=OFF \
    -DKICAD_SCRIPTING_WXPYTHON_PHOENIX=OFF \
    -DKICAD_SCRIPTING_PYTHON3=OFF \
    -DKICAD_SCRIPTING_ACTION_MENU=OFF \
    -DKICAD_SPICE=ON \
    -DKICAD_VERSION_EXTRA=%release \
    -DCMAKE_BUILD_TYPE=Release \

%cmake_build

%install
%cmakeinstall_std

#fix line ending
dos2unix %buildroot%_desktopdir/*.desktop

#validate desktop files
desktop-file-validate %buildroot%_desktopdir/*.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Engineering \
	%buildroot%_desktopdir/kicad.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Engineering \
	%buildroot%_desktopdir/eeschema.desktop

%files
%_bindir/*
%_desktopdir/*.desktop
%_libdir/*.so*
%_libdir/%name/
#python_sitelibdir/*

%files data
%doc %_docdir/%name
%_datadir/appdata/%name.appdata.xml
%_iconsdir/hicolor/*/mimetypes/application-x-*.*
%_iconsdir/hicolor/*/apps/*.*
%_datadir/%name/
%_datadir/mime/packages/*

%changelog
* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.4-alt1
- new version 5.1.4

* Mon May 20 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.2-alt2
- Not requires to kicad-packages3D (large package)

* Thu Apr 25 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.2-alt1
- new version 5.1.2

* Fri Mar 15 2019 Anton Midyukov <antohami@altlinux.org> 1:5.1.0-alt1
- new version 5.1.0
- disable srcipting support
- build with wxGTK3.1

* Thu Jan 03 2019 Anton Midyukov <antohami@altlinux.org> 1:5.0.2-alt1
- new version 5.0.2

* Fri Nov 23 2018 Anton Midyukov <antohami@altlinux.org> 1:5.0.1-alt1
- new version 5.0.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.0.0-alt1.1.qa1
- NMU: applied repocop patch

* Wed Sep 12 2018 Anton Midyukov <antohami@altlinux.org> 1:5.0.0-alt1.1
- Rebuilt with libssl-1.1

* Thu Jul 19 2018 Anton Midyukov <antohami@altlinux.org> 1:5.0.0-alt1
- New version 5.0.0
- Change group Engineering

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.0.7-alt2.1
- NMU: rebuilt with boost-1.67.0

* Thu Oct 26 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.7-alt2
- Skip requires pcbnew.

* Wed Aug 30 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.7-alt1
- New version 4.0.7
- exclude cvpcb.desktop

* Wed Feb 22 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.6-alt1
- New version 4.0.6

* Mon Jan 30 2017 Anton Midyukov <antohami@altlinux.org> 1:4.0.5-alt2
- Fix build with gcc6 and boost-1.61

* Sat Dec 10 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.5-alt1
- New version 4.0.5

* Wed Aug 31 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.4-alt1
- New version 4.0.4

* Thu Jul 21 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.2-alt2
- Enable build github plugin
- New packages kicad-data (fix arch-dep-package-has-big-usr-share)
- Fix line ending in desktop files
- Fix missing buildrequires.

* Sat Jun 04 2016 Anton Midyukov <antohami@altlinux.org> 1:4.0.2-alt1
- New version.

* Sat Feb 27 2016 barssc <barssc at altlinux.ru> r4029-alt2
- fix build for Sisyphus

* Sat Nov 29 2014 barssc <barssc at altlinux.ru> r4029-alt1
- new version

* Tue Nov 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20110522-alt2.1
- Fixed build with gcc 4.7

* Tue Jun 07 2011 Denis Klimov <zver at altlinux.org> 20110522-alt2
- fix inherit

* Mon Jun 06 2011 Denis Klimov <zver at altlinux.org> 20110522-alt1
- new version

* Tue May 24 2011 Repocop Q. A. Robot <repocop at altlinux.org> 20110421-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for kicad

* Fri Apr 22 2011 Denis Klimov <zver at altlinux.org> 20110421-alt1
- new version

* Tue Apr 12 2011 Denis Klimov <zver at altlinux.org> 20110409-alt2
- fix install netlist_form_pads-pcb.xsl for x86_64

* Mon Apr 11 2011 Denis Klimov <zver at altlinux.org> 20110409-alt1
- new version

* Fri Apr 08 2011 Denis Klimov <zver at altlinux.org> 20110401-alt1
- new version

* Mon Mar 28 2011 Denis Klimov <zver at altlinux.org> 20110325-alt1
- new version
- remove patches
- cleanup spec

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop at altlinux.org> 20080825-alt0.2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for kicad
  * postclean-05-filetriggers for spec file

* Fri Feb 13 2009 Alexey Shentzev <ashen at altlinux.ru> 20080825-alt0.2
- fix desktop files

* Fri Feb 13 2009 Alexey Shentzev <ashen at altlinux.ru> 20080825-alt0.1
- first build for ALT Linux
