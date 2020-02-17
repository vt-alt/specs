
%def_disable mp4

%define rname kid3
Name: kde5-%rname
Version: 3.8.2
Release: alt1
%K5init altplace

Group: Sound
Summary: ID3 tagger
License: GPL-2.0-or-later
Url: http://kid3.sourceforge.net/

Source: kid3-%{version}.tar
Source1: ru.po
Patch1: kid3-3.0.2-alt-desktop_ru.patch

# Automatically added by buildreq on Fri Nov 13 2015 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gtk-update-icon-cache id3lib kf5-kdoctools-devel libEGL-devel libGL-devel libavcodec-devel libavutil-devel libflac-devel libgpg-error libjson-c libogg-devel libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-printsupport libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl-parent pkg-config python-base python3 python3-base qt5-base-devel qt5-tools ruby ruby-stdlibs xml-common xml-utils zlib-devel
#BuildRequires: extra-cmake-modules gcc-c++ id3lib-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libavdevice-devel libavformat-devel libavresample-devel libchromaprint-devel libflac++-devel libreadline-devel libswscale-devel libtag-devel libvorbis-devel python-module-google qt5-multimedia-devel qt5-tools-devel rpm-build-python3 rpm-build-ruby xsltproc
BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake extra-cmake-modules
BuildRequires: gettext-tools
BuildRequires: gcc-c++ glib2-devel libreadline-devel /usr/bin/xsltproc
BuildRequires: libavdevice-devel libavformat-devel libavresample-devel libswscale-devel
BuildRequires: libchromaprint-devel
BuildRequires: id3lib-devel libtag-devel
BuildRequires: libflac++-devel libvorbis-devel
%if_enabled mp4
BuildRequires: libmpeg4ip-devel
%endif
BuildRequires: qt5-base-devel qt5-multimedia-devel qt5-tools-devel qt5-phonon-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kdoctools kf5-kdoctools-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-solid-devel kf5-kxmlgui-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static
BuildRequires: kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel


%description
Kid3 - Efficient Audio Tagger

With Kid3 you can:

- Edit ID3v1.1 tags
- Edit all ID3v2.3 and ID3v2.4 frames
- Convert between ID3v1.1, ID3v2.3 and ID3v2.4 tags
- Edit tags in MP3, Ogg/Vorbis, FLAC, MPC, APE, MP4/AAC, MP2, Speex,
  TrueAudio, WavPack, WMA, WAV, AIFF files and tracker modules.
- Edit tags of multiple files, e.g. the artist, album, year and genre
  of all files of an album typically have the same values and can be
  set together.
- Generate tags from filenames
- Generate tags from the contents of tag fields
- Generate filenames from tags
- Rename directories from tags
- Generate playlist files
- Automatic case conversion and string translation
- Import and export album data
- Import from gnudb.org, TrackType.org, MusicBrainz, Discogs, Amazon

Authors: Urs Fleisch

%package common
Summary: Common empty package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf5-filesystem
%description common
Common empty package for %name

%package core
Summary: Core files needed for %name
Group: System/Libraries
Requires: %name-common = %EVR
%description core
Core files needed for %name

%package -n %rname-ui-kde5
Summary: ID3 tagger KDE5 UI
Group: Sound
Requires: %name-core = %EVR
Provides: %rname = %version-%release
Provides: kde5-kid3 = %EVR
Obsoletes: kde5-kid3 < %EVR
%description -n %rname-ui-kde5
Package contains KDE5 UI.
%{description}

%package -n %rname-ui-qt5
Summary: ID3 tagger Qt5 UI
Group: Sound
Requires: %name-core = %EVR
Conflicts: kid3-ui-qt4
%description -n %rname-ui-qt5
Package contains Qt5 UI.
%{description}

%package -n %rname-ui-cli5
Summary: ID3 tagger CLI UI
Group: Sound
Requires: %name-core = %EVR
%description -n %rname-ui-cli5
Package contains command line UI.
%{description}


%package -n libkid3-core5
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libkid3-core5
%name library.

%package -n libkid3-gui5
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libkid3-gui5
%name library.


%prep
%setup -q -n %rname-%version
%patch1 -p1

tmp_file=`mktemp`
msgcat --use-first translations/po/ru/kid3_qt.po %SOURCE1 >"$tmp_file"
cat "$tmp_file" >translations/po/ru/kid3_qt.po
rm -f "$tmp_file"

find -type f -name CMakeLists.txt | \
while read f ; do
    for l in kid3-gui kid3-core ; do
	sed -i "s|${l}|${l}5|" $f
    done
done

%build
%K5cmake \
    -DWITH_APPS="cli;qt;kde" \
    -DWITH_BINDIR=%_K5bin \
    -DWITH_LIBDIR=%_lib \
    -DWITH_DATAROOTDIR=%_datadir \
    -DWITH_PLUGINSDIR=%_libdir/kid3-kf5/plugins \
    -DWITH_QMLDIR=%_datadir/kid3-kf5/qml \
    -DWITH_TRANSLATIONSDIR=share/kid3-kf5/translations \
    -DWITH_DOCDIR=%_docdir/%name \
    -DWITH_QT4:BOOL=OFF \
    -DWITH_QT5:BOOL=ON \
    -DWITH_TAGLIB:BOOL=ON \
    -DWITH_ID3LIB:BOOL=ON \
    -DWITH_VORBIS:BOOL=ON \
%if_enabled mp4
    -DWITH_MP4V2:BOOL=ON \
%endif
    -DWITH_FLAC:BOOL=ON \
    -DWITH_CHROMAPRINT=ON \
    -DWITH_DBUS=ON \
    -DWITH_QML=OFF \
    #
%K5make


%install
%K5install
%find_lang --with-kde --with-qt %rname

%files common -f %rname.lang
%dir %_datadir/kid3-kf5/
%dir %_datadir/kid3-kf5/translations

%files core
%_libdir/kid3-kf5/plugins/lib*.so

%files -n %rname-ui-kde5
%doc AUTHORS NEWS README ChangeLog
%_K5bin/%rname
%_K5xmlgui/kid3/
%_K5xdgapp/net.sourceforge.kid3.desktop
%_K5icon/hicolor/*/apps/%rname.*

%files -n %rname-ui-qt5
%doc AUTHORS NEWS README ChangeLog
#_bindir/%rname-qt
%_K5bin/%rname-qt
%doc %_docdir/kde5-kid3/
%_iconsdir/*/*/apps/kid3-qt.*
%_desktopdir/net.sourceforge.kid3-qt.desktop

%files -n %rname-ui-cli5
%doc AUTHORS NEWS README ChangeLog
#_bindir/%rname-cli
%_K5bin/%rname-cli

%files -n libkid3-core5
%_libdir/libkid3-core5.so.*

%files -n libkid3-gui5
%_libdir/libkid3-gui5.so.*

#%files devel
#%_K5dbus_iface/*id3*

%changelog
* Wed Feb 12 2020 Sergey V Turchin <zerg@altlinux.org> 3.8.2-alt1
- new version

* Wed Dec 18 2019 Sergey V Turchin <zerg@altlinux.org> 3.8.0-alt1
- new version

* Tue Oct 09 2018 Sergey V Turchin <zerg@altlinux.org> 3.6.2-alt2
- update russian translation

* Thu Sep 13 2018 Sergey V Turchin <zerg@altlinux.org> 3.6.2-alt1
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 3.6.1-alt1
- new version

* Wed Mar 28 2018 Sergey V Turchin <zerg@altlinux.org> 3.6.0-alt1
- new version

* Thu Dec 14 2017 Sergey V Turchin <zerg@altlinux.org> 3.5.1-alt1
- new version

* Thu Aug 10 2017 Sergey V Turchin <zerg@altlinux.org> 3.4.5-alt2
- rebuild with new chromaprint

* Tue Jun 06 2017 Sergey V Turchin <zerg@altlinux.org> 3.4.5-alt1
- new version

* Mon Jan 09 2017 Sergey V Turchin <zerg@altlinux.org> 3.4.4-alt1
- new version

* Fri Jul 15 2016 Sergey V Turchin <zerg@altlinux.org> 3.4.1-alt2
- fix load translations

* Thu Jul 14 2016 Sergey V Turchin <zerg@altlinux.org> 3.4.1-alt1
- new version

* Mon Nov 09 2015 Sergey V Turchin <zerg@altlinux.org> 3.3.0-alt1
- initial build
