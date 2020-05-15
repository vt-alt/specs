
Name: qtscrob
Version: 0.11
Release: alt2

Group: Sound
Summary: Submit .scrobbler.log from portable players to Last.fm and Libre.fm
Url: http://qtscrob.sourceforge.net/
License: GPL-2.0-only

Requires: %name-gui %name-cli

Source: qtscrob-%version.tar
# Debian
Patch1: 0001-Add-dependencies-between-install-and-compress-man.patch
Patch2: dont-update-language-files.patch
Patch3: install-higher-res-icons.patch
Patch4: qt5-port.patch

# Automatically added by buildreq on Thu May 22 2014 (-bi)
# optimized out: elfutils fontconfig libX11-devel libXext-devel libcloog-isl4 libqt4-core libqt4-gui libqt4-network libqt4-sql libqt4-xml libstdc++-devel libusb-devel phonon-devel pkg-config python-base
#BuildRequires: desktop-file-utils dos2unix gcc-c++ glibc-devel-static libicu50 libmtp-devel libqt4-devel ruby ruby-stdlibs
BuildRequires: desktop-file-utils gcc-c++ glibc-devel libmtp-devel libXext-devel qt5-base-devel qt5-tools

%description
Update your last.fm profile using information from portable player!
QTScrobbler is tool for submitting from portable players to
Last.fm & Libre.fm. It is written in C++ using the QT4 library.

Features:
 * Parsing iPod's Play Counts file to get recently played tracks;
 * Parsing .scrobbler.log (and .scrobbler-timeless.log);
 * MTP (aka PlaysForSure) support;
 * Ability to recalculate the listen times of any loaded tracks;
 * Proxy support;
 * Protocol 1.2 support;
 * Automatically detect timezone and summertime details;

%package gui
Group: Sound
Summary: %name GUI tool
%description gui
qtscrob is a GUI tool which reads playback information from iPods,
MTP (aka Plays for Sure) or Rockbox (open source audio player
firmware) devices and submits them to an audioscrobbler service, such
as "last.fm" or "libre.fm"

%package cli
Group: Sound
Summary: %name CLI tool
%description cli
scrobbler is a CLI tool which reads playback information from iPods,
MTP (aka Plays for Sure) or Rockbox (open source audio player
firmware) devices and submits them to an audioscrobbler service, such
as "last.fm" or "libre.fm".


%prep
%setup
find ./ -type f | \
while read f
do
    chmod 0644 $f
done

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

cd src
%qmake_qt5 PREFIX=%_prefix


%build
cd src
%make_build


%install
cd src
%installqt5
ln -s scrobbler %buildroot/%_bindir/qtscrob-cli
ln -s qtscrob %buildroot/%_bindir/qtscrob-gui

desktop-file-install \
    --vendor="" \
    --add-category="AudioVideo" \
    --add-category="Music" \
    --remove-category="Network" \
    --dir %buildroot/%_desktopdir %buildroot/%_desktopdir/%name.desktop

%files

%files cli
%doc AUTHORS CHANGELOG README
%_bindir/scrobbler
%_bindir/qtscrob-cli
%_man1dir/scrobbler.*

%files gui
%doc AUTHORS CHANGELOG README
%_bindir/qtscrob
%_bindir/qtscrob-gui
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/qtscrob.*

%changelog
* Wed May 13 2020 Sergey V Turchin <zerg@altlinux.org> 0.11-alt2
- port to Qt5

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 0.11-alt0.M70P.1
- built for M70P

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 0.11-alt1
- initial build
