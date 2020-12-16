Name:           pdfmod
Version:        0.9.1
Release:        alt10

Summary:        PDF Modifier
License:        GPL-2.0+
Group:          File tools

Url:            https://wiki.gnome.org/Apps/PdfMod
Source0:        %name-%version.tar.gz
Patch0:         pdfmod-0.9.1-alt-fix-configure.patch
Packager:       Korneechev Evgeniy <ekorneechev@altlinux.org>

BuildRequires:  /proc
BuildRequires:  gnome-doc-utils
BuildRequires:  hyena-devel
BuildRequires:  intltool
BuildRequires:  libgnome-sharp-devel
BuildRequires:  mono-data
BuildRequires:  mono-devel
BuildRequires:  python3-base

Requires:       gawk
Requires:       libgnome-sharp
Requires:       libgtk-sharp2
Requires:       libpoppler8-glib
Requires:       mono-core >= 5.0

%description
PDF Mod is a simple tool for modifying your PDFs: moving, removing,
extracting, and rotating pages.

%prep
%setup
%patch0 -p1

%build
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot
%find_lang %name %{?no_lang_C}

%post
awk '{gsub ("</configuration>", "", $0); print > FILENAME}' %_sysconfdir/mono/config
echo '  <dllmap dll="glib-2.0.dll" target="libglib-2.0.so.0" os="!windows"/>' >> %_sysconfdir/mono/config
echo "</configuration>" >> %_sysconfdir/mono/config

%files -f %name.lang
%doc AUTHORS NEWS README COPYING
%_datadir/gnome/help/%name/
%_bindir/%name
%_libdir/%name/
%_datadir/icons/hicolor/*/apps/*
%_datadir/applications/%name.desktop

%changelog
* Mon Dec 07 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt10
- Fixed build: mono-devel to deps

* Thu Sep 21 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt9
- Reverted previous change

* Thu Sep 21 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt8
- Fixed unowned files

* Tue Sep 12 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt7
- Rebuild with mono5

* Mon Oct 17 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt6
- Update categories in .desktop and group in .spec

* Tue Sep 13 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt5
- Fix OnHelp - fix path to glib.dll for mono

* Fri Sep 09 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt4
- fix buildreq and macros

* Fri Sep 09 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt3
- libpoppler-glib.so 4 >> 8
- fix requires

* Fri Sep 09 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt2
- Fix compilation under Mono 2.10
Force use of the overloaded implicit operator of Hyena.Gui.DragDropList
to solve mono 2.10 compilation problems.
Fix from Alexander Kojevnikov <alexander@kojevnikov.com>

* Thu Sep 08 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.1-alt1
- Initial build
