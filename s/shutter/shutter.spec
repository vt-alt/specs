Name: shutter
Version: 0.95
Release: alt1

Summary: Shutter is a feature-rich screenshot program
License: GPLv3+
Group: Graphics

Url: http://shutter-project.org/
Source: shutter-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-perl
BuildRequires:	perl-Gtk2-Unique
Requires: ImageMagick-tools libgtkimageview
Requires: perl-Sort-Naturally
Requires: perl-Glib perl-File-Which perl-File-Copy-Recursive perl-File-BaseDir perl-IO-stringy
Requires: perl-Gnome2 perl-File-DesktopEntry perl-File-MimeInfo perl-Proc-ProcessTable
Requires: perl-Gnome2-Canvas perl-Proc-Simple perl-Locale-gettext perl-JSON
Requires: perl-Number-Bytes-Human perl-Glib-Object-Introspection
Requires: perl-Gnome2-GConf
Requires: perl-Gnome2-VFS
Requires: perl-Gnome2-Wnck
Requires: perl-Goo-Canvas
Requires: perl-Gtk2
Requires: perl-Gtk2-ImageView
Requires: perl-Gtk2-Unique
Requires: perl-HTML-Form
Requires: perl-Net-DBus
Requires: perl-Net-OAuth
Requires: perl-Magick
Requires: perl-WWW-Mechanize
Requires: perl-X11-Protocol
Requires: perl-XML-Simple
Requires: perl-libwww-perl
Requires: perl-podlators
Requires: procps

# not autodetected:
Requires: xdg-utils

%description
Shutter is a feature-rich screenshot program. You can take a screenshot of a
specific area, window, your whole screen, or even a Web site, apply different
effects to it, draw on it to highlight points, and then upload to an image
hosting site, all within one window.

%prep
%setup

subst 's/Application;/Graphics;2DGraphics;RasterGraphics;/' share/applications/shutter.desktop

%build
./po2mo.sh

%install
install -pDm 755 bin/shutter %buildroot%_bindir/shutter
cp -a share %buildroot/usr

#Clean
%__rm %buildroot/usr/share/doc/shutter/COPYING
%__rm %buildroot/usr/share/doc/shutter/README

%find_lang shutter
%find_lang --append --output=shutter.lang shutter-plugins shutter-upload-plugins

%set_perl_req_method relaxed

%files -f shutter.lang
%doc COPYING README
%_bindir/*
%_datadir/shutter
%_datadir/appdata/shutter.appdata.xml
%_man1dir/*
%_desktopdir/*
%_pixmapsdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/128x128/*
%_iconsdir/hicolor/192x192/*
%_iconsdir/hicolor/22x22/*
%_iconsdir/hicolor/24x24/*
%_iconsdir/hicolor/256x256/*
%_iconsdir/hicolor/36x36/*
%_iconsdir/hicolor/64x64/*
%_iconsdir/hicolor/72x72/*
%_iconsdir/hicolor/96x96/*
%_iconsdir/hicolor/scalable/*/*
%_iconsdir/HighContrast/scalable/apps/shutter*

%changelog
* Mon Feb 08 2021 Grigory Ustinov <grenka@altlinux.org> 0.95-alt1
- Build new version (Closes: #39323).

* Tue Oct 06 2020 Grigory Ustinov <grenka@altlinux.org> 0.94.3-alt1
- Build new version (Closes: #39038).

* Thu Dec 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.94.2-alt3
- Translation fixed

* Tue Oct 02 2018 Grigory Ustinov <grenka@altlinux.org> 0.94.2-alt2
- Remove dependency on ImageMagick.

* Thu Sep 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.94.2-alt1
- Build new version.

* Fri Aug 03 2018 Grigory Ustinov <grenka@altlinux.org> 0.94-alt2
- Fix desktop names (Closes: #35149).

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 0.94-alt1
- Build new version.

* Sat Jul 09 2016 Andrey Cherepanov <cas@altlinux.org> 0.93.1-alt1
- 0.93.1 (ALT #32228)
- Add requires of perl-podlators (ALT #31413)

* Tue Feb 28 2012 Radik Usupov <radik@altlinux.org> 0.88.2-alt1
- 0.88.2
- Added requires (Closes: 26996)

* Fri Feb 10 2012 Radik Usupov <radik@altlinux.org> 0.88.1-alt1
- 0.88.1

* Thu Sep 01 2011 Radik Usupov <radik@altlinux.org> 0.87.3-alt1
- 0.87.3
- New packager

* Mon Sep 13 2010 Victor Forsiuk <force@altlinux.org> 0.86.4-alt1
- 0.86.4

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 0.86.3-alt1
- 0.86.3

* Wed Jun 09 2010 Victor Forsiuk <force@altlinux.org> 0.86.2-alt1
- 0.86.2
- Set relaxed perl.req mode instead of skipping files it fails to process.

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.86.1-alt1
- 0.86.1

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 0.86-alt1
- 0.86

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 0.85.1-alt1
- 0.85.1

* Mon Nov 23 2009 Victor Forsyuk <force@altlinux.org> 0.85-alt1
- 0.85

* Thu Aug 13 2009 Victor Forsyuk <force@altlinux.org> 0.80.1-alt1
- Initial build.
