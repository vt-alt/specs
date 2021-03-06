%define renderer ffmpeg

Name:     imagination
Version:  3.6
Release:  alt1

Summary:  Imagination is a lightweight and simple DVD slide show maker
License:  GPLv2
Group:    Graphics
Url:      http://imagination.sourceforge.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar.bz2
Source1:  %name.watch
Source2:  ru.po

Patch1: Add-translation-support-to-some-files.patch

BuildRequires: libgtk+3-devel
BuildRequires: intltool
BuildRequires: libsox-devel
BuildRequires: xsltproc
BuildRequires: docbook-style-xsl

Requires: %renderer
Requires: libsox-fmt-alsa
Requires: libsox-fmt-flac
Requires: libsox-fmt-mp3
Requires: libsox-fmt-oss
Requires: libsox-fmt-sndfile
Requires: libsox-fmt-vorbis

%description
Imagination is a lightweight and easy to use slide show maker for Linux
and FreeBSD written in C language and built with the GTK+2 toolkit.

%prep
%setup
%patch1 -p2
cp %SOURCE2 po/ru.po

%build
%undefine _configure_gettext
%configure
%make_build CFLAGS="$CFLAGS -DPLUGINS_INSTALLED=1"

%install
%makeinstall_std
rm -f %buildroot%_libdir/%name/*.la
%find_lang %name

%files -f %name.lang
%doc AUTHORS README
%_bindir/*
%_libdir/%name/*.so
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/doc/%name

%changelog
* Mon Jun 01 2020 Andrey Cherepanov <cas@altlinux.org> 3.6-alt1
- new version 3.6

* Tue Feb 25 2020 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version 3.5.1.
- Build with GTK+3.

* Thu Jan 30 2020 Pavel Moseev <mars@altlinux.org> 3.4-alt5
- Add translation support to some files.
- Update Russian translation (thanks Olesya Gerasimenko).

* Mon Aug 12 2019 Andrey Cherepanov <cas@altlinux.org> 3.4-alt4
- Complete Russian translation (thanks Olesya Gerasimenko).
- Requires renderer (ALT #37055).
- Support sound formats by sox-fmt-* packages (ALT #37054).

* Tue Jul 16 2019 Andrey Cherepanov <cas@altlinux.org> 3.4-alt3
- Fix desktop file localization.

* Tue Jul 09 2019 Andrey Cherepanov <cas@altlinux.org> 3.4-alt2
- Update Russian translation (thanks Olesya Gerasimenko).

* Wed Jul 03 2019 Andrey Cherepanov <cas@altlinux.org> 3.4-alt1
- Initial build for Sisyphus.
