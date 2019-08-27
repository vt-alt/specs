Name:    cuneiform-qt
Version: 0.1.4
Release: alt2
Summary: GUI frontend for Cuneiform OCR

License: GPLv3+
Group:   Graphics
URL:     http://www.altlinux.org/Cuneiform-Qt

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: qt5-base-devel
BuildRequires: ImageMagick

Requires: cuneiform
Requires: qt5-translations

%description
This application is GUI frontend for Cuneiform (OCR system originally
developed and open sourced by Cognitive technologies). It allow
to open scanned image, view this one in preview pane, recornize text via
Cuneiform and save result in HTML file.

%prep
%setup -q

%build
%qmake_qt5
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 icons/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 icons/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 icons/%name.png %buildroot%_miconsdir/%name.png

%files
%doc AUTHORS README.md TODO.md
%_bindir/%name
%_datadir/apps/%name/*.qm
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_pixmapsdir/%name.png

%changelog
* Mon Aug 26 2019 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt2
- Do not strip debugging information.

* Tue Feb 05 2019 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1
- Fix saving of file, fix status bar message during saving.

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1
- New version based on patches from Magea.
- Build with Qt5.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Apr 10 2009 Andrey Cherepanov <cas@altlinux.org> 0.1.2-alt1
- Fix build with Qt 4.3

* Fri Apr 10 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1.1-alt1.2
- created Ukrainian translation
- add Ukrainian to desktop-file

* Wed Apr 08 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1.1-alt1.1
- fix optflags
- change icons from pixmapsdir to iconsdir
- cleanup spec

* Tue Apr 07 2009 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- Add Russian translation
- Save from text widget instead copy temporary file
- Remove temporary file
- Check for errors during saving
- Differ saved format and filter in saved file selection dialog
- Show application icon in about dialog
- Remove native option because it is binary format and it will not display correctly
- Fix readOnly flag for result text
- Move installation instruction from spec to QMake project file

* Mon Apr 06 2009 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial release
