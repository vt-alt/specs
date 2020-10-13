Name: mpz
Version: 1.0.1
Release: alt1

Summary: Music player for the large local collections

License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/olegantonyan/mpz

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/olegantonyan/mpz/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: qt5-base-devel qt5-multimedia-devel qt5-x11extras-devel

%description
Music player for big local collections. Treats your folders with music as a library.
Features 3-column UI: directory tree viewer, playlists list and tracks from current playlist.
Similar to "album list" in Foobar2000.

%prep
%setup

%build
mkdir build
cd build
qmake-qt5 CONFIG+=release CONFIG+=force_debug_info ..
%make_build

%install
cd build
%make_install install INSTALL_ROOT=%buildroot

%files
%doc license.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/512x512/apps/%name.png

%changelog
* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

* Sun Aug 9 2020 Oleg Antonyan <oleg.b.antonyan@gmail.com>
- First public release
