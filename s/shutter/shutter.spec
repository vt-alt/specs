%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%_datadir/shutter/resources/modules'
# run "buildreq-src --update --spec shutter.spec ." to update BuildRequires below
# note: remove perl(Furl/HTTP.pm) as it is optional dependency from autoimports
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Digest/MD5.pm) perl(Encode.pm) perl(Encode/Locale.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(File/Copy/Recursive.pm) perl(File/Which.pm) perl(File/stat.pm) perl(FindBin.pm) perl(Glib.pm) perl(Glib/Object/Introspection.pm) perl(Gnome2/Canvas.pm) perl(Gnome2/Wnck.pm) perl(Goo/Canvas.pm) perl(Gtk2.pm) perl(Gtk2/ImageView.pm) perl(Gtk2/Pango.pm) perl(Gtk2/TrayIcon.pm) perl(HTTP/Request.pm) perl(HTTP/Request/Common.pm) perl(HTTP/Status.pm) perl(IO/File.pm) perl(IO/Socket/SSL.pm) perl(Image/Magick.pm) perl(JSON/MaybeXS.pm) perl(LWP/UserAgent.pm) perl(List/Util.pm) perl(Locale/gettext.pm) perl(MIME/Base64.pm) perl(Net/DBus.pm) perl(Net/FTP.pm) perl(Net/OAuth.pm) perl(Number/Bytes/Human.pm) perl(Path/Class.pm) perl(Pod/Usage.pm) perl(Proc/Killfam.pm) perl(Proc/Simple.pm) perl(Sort/Naturally.pm)
BuildRequires: perl(Time/HiRes.pm) perl(URI.pm) perl(URI/Escape.pm) perl(URI/Split.pm) perl(WWW/Mechanize.pm) perl(WebService/Gyazo/B.pm) perl(X11/Protocol.pm) perl(XML/Simple.pm) perl(lib.pm)
# END SourceDeps(oneline)
Name: shutter
Version: 0.95
Release: alt2

Summary: Shutter is a feature-rich screenshot program
License: GPLv3+
Group: Graphics

Url: http://shutter-project.org/
Source: shutter-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-perl
BuildRequires:	perl-Gtk2-Unique
BuildRequires: perl(X11/Protocol/Ext/XFIXES.pm)
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
Requires: perl(X11/Protocol/Ext/XFIXES.pm)

%description
Shutter is a feature-rich screenshot program. You can take a screenshot of a
specific area, window, your whole screen, or even a Web site, apply different
effects to it, draw on it to highlight points, and then upload to an image
hosting site, all within one window.

%prep
%setup

subst 's/Application;/Graphics;2DGraphics;RasterGraphics;/' share/applications/shutter.desktop

# in external library
rm share/shutter/resources/modules/X11/Protocol/Ext/XFIXES.pm
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
* Tue Feb 09 2021 Igor Vlasenko <viy@altlinux.ru> 0.95-alt2
- added perl magic

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
