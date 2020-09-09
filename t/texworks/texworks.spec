Name: texworks
Version: 0.6.5
Release: alt2

Summary: A simple IDE for authoring TeX documents
Summary(ru_RU.UTF-8): Простой редактор для документов TeX

License: GPL-2.0
Group: Publishing
Url: http://tug.org/texworks/

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires: gcc-c++ qt5-base-devel qt5-script-devel qt5-tools-devel-static zlib-devel
BuildRequires: libhunspell-devel libdbus-devel libpoppler-qt5-devel unzip cmake

Source0: %name-%version.tar
Source1: texworks-alt-icons.tar
Source2: TeXworks-manual-r1029.pdf

Patch1: %name-0.6.3-desktop.patch
Patch2: 0001-QtPDF-Fix-compilation-with-Qt-5.15.patch

%description
TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc)
documents, with a Unicode-based, TeX-aware editor, integrated PDF
viewer, and a clean, simple interface accessible to casual
and non-technical users.

You may install the texlive-* packages to make this program useful.

%description -l ru_RU.UTF-8
TeXworks - это простой редактор для работы с TeX документами (LaTeX,
ConTeXt и другие) с возможностью просмотра скомпилированных
PDF-документов и простым интерфейсом, понятным даже для
начинающих осваивать TeX.

Для того, чтобы использовать TeXworks вам также понадобится установить
пакеты texlive-*.

%package doc
Summary: Documentation for TeXworks
Summary(ru_RU.UTF-8): Документация для редактора TeXworks
Group: Publishing
Requires: %name = %version-%release
BuildArch: noarch

%description doc
User manual for TeXworks editor.

%description doc -l ru_RU.UTF-8
Документация к редактору TeXworks.

%prep
%setup -a1
%patch1 -p2
%patch2 -p1

%build
%cmake_insource -DDESIRED_QT_VERSION=5
%make

%install
%makeinstall_std
install -m 644 -D texworks-alt-icons/TeXworks-16x16.png %buildroot%_miconsdir/TeXworks.png
install -m 644 -D texworks-alt-icons/TeXworks-32x32.png %buildroot%_niconsdir/TeXworks.png
install -m 644 -D texworks-alt-icons/TeXworks-48x48.png %buildroot%_liconsdir/TeXworks.png
install -m 644 -D %SOURCE2 %buildroot/%_docdir/%name

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/64x64
%_iconsdir/hicolor/128x128
%_iconsdir/hicolor/512x512
%_datadir/metainfo
%_man1dir/*
%_docdir/%name
%exclude %_docdir/%name/TeXworks-manual-*.pdf

%files doc
%_docdir/%name/TeXworks-manual-*.pdf

%changelog
* Thu Aug 27 2020 Grigory Ustinov <grenka@altlinux.org> 0.6.5-alt2
- Fix license.

* Thu Mar 26 2020 Grigory Ustinov <grenka@altlinux.org> 0.6.5-alt1
- Build new version.

* Mon Mar 16 2020 Grigory Ustinov <grenka@altlinux.org> 0.6.4-alt1
- Build new version.

* Wed Apr 17 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt1
- Build new version.

* Fri Aug 03 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.2.0.115.git67caf97-alt1
- Build from last commit.
- Transfer package to qt5.

* Thu Jan 18 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.2-alt1
- Build new version.

* Sun Jun 07 2015 Denis Kirienko <dk@altlinux.org> 0.4.6-alt1
- Version 0.4.6

* Fri Jun 21 2013 Denis Kirienko <dk@altlinux.org> 0.4.5-alt1
- Version 0.4.5 (SVN 1281)

* Sun Apr 07 2013 Denis Kirienko <dk@altlinux.org> 0.4.4-alt2
- Rebuild with new libpoppler

* Sat Jun 02 2012 Denis Kirienko <dk@altlinux.org> 0.4.4-alt1
- Version 0.4.4 (SVN 1004)

* Fri Aug 05 2011 Denis Kirienko <dk@altlinux.ru> 0.4.3-alt1
- Version 0.4.3 (SVN 858)

* Fri Apr 22 2011 Denis Kirienko <dk@altlinux.ru> 0.4.0-alt1
- Version 0.4.0 (SVN 759)

* Fri Feb 18 2011 Denis Kirienko <dk@altlinux.ru> 0.3-alt2
- SVN 731

* Wed May 05 2010 Denis Kirienko <dk@altlinux.ru> 0.3-alt1
- SVN 641
- Added user manual
- Fixed spellchecking support

* Sat May 01 2010 Denis Kirienko <dk@altlinux.ru> 0.2.3-alt1
- First build for Sisyphus, based on Fedora specfile
