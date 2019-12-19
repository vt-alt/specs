%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=761847
%def_disable mp3gain
%def_disable permhelper
%_K5if_ver_gteq %ubt_id M90
%def_enable obsolete_kde4
%else
%def_disable obsolete_kde4
%endif

%define mp3gain_ver %{get_version mp3gain}
%define is_ffmpeg %([ -n "`rpmquery --qf '%%{SOURCERPM}' libavformat-devel 2>/dev/null | grep -e '^libav'`" ] && echo 0 || echo 1)

%define sover 1
%define libsoundkonvertercore libsoundkonvertercore%sover

%define rname soundKonverter
%define tname soundkonverter
Name: kde5-soundkonverter
Version: 3.0.1
Release: alt4
%K5init %{?_enable_obsolete_kde4:no_altplace}

Summary: A frontend to various audio converters
License: GPLv2
Group: Sound

Provides: soundkonverter = %version-%release
Conflicts: soundkonverter <= 0.3.9-alt8.1

Url: https://github.com/dfaust/soundkonverter
Source: %tname-%version.tar
Patch1: alt-mp3gain1.4.patch
Patch2: alt-lib-sover.patch
Patch3: alt-mp2-range.patch
Patch4: alt-load-translations.patch

%if_enabled obsolete_kde4
Provides: kde4-soundkonverter = %version-%release
Obsoletes: kde4-soundkonverter < %version-%release
%endif
%if %is_ffmpeg
Requires: /usr/bin/ffmpeg
%else
Requires: /usr/bin/avconv
%endif
Requires: vorbis-tools vorbisgain flac lame cdparanoia speex wavpack faad mppenc sox opus-tools
%if_enabled mp3gain
Requires: mp3gain
%endif
#Requires: faac

# Automatically added by buildreq on Tue Sep 19 2017 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdelibs4support kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libEGL-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libssl-devel libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: extra-cmake-modules gtk-update-icon-cache kde5-libkcddb-devel kf5-kdelibs4support-devel kf5-kio-devel libcdparanoia-devel libtag-devel python-module-google python3-dev python3-module-zope qt5-phonon-devel rpm-build-ruby
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt libavformat-devel
%if_enabled mp3gain
BuildRequires(pre): mp3gain
%endif
BuildRequires: libcdparanoia-devel libtag-devel
BuildRequires: qt5-phonon-devel
BuildRequires: extra-cmake-modules
BuildRequires: kde5-libkcddb-devel
BuildRequires: kf5-kdelibs4support-devel kf5-kio-devel

%description
%rname project is a frontend to various audio converters.
The key features are:
- Audio conversion
- Replay Gain calculation
- CD ripping

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package -n %libsoundkonvertercore
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n %libsoundkonvertercore
%name library

%prep
%setup -qn %tname-%version
%_K5if_ver_lt %mp3gain_ver 1.5
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm -f cmake/modules/FindTaglib.cmake


%build
pushd src
%K5build
popd


%install
pushd src
%K5install
%K5install_move data %tname solid locale
popd
%find_lang --with-kde %tname

%files common
%doc src/README src/CHANGELOG

%files -f %tname.lang
%_K5bin/%tname
%_K5plug/soundkonverter_*.so
%_K5xdgapp/*.desktop
%_K5icon/hicolor/*/*/*.*
%_K5data/%tname
%_K5data/solid/actions/soundkonverter-*.desktop
%_K5srv/%{tname}_*.desktop
%_K5srvtyp/%{tname}_*.desktop
%_K5xmlgui/%tname/

%files -n %libsoundkonvertercore
%_K5lib/libsoundkonvertercore.so.%sover
%_K5lib/libsoundkonvertercore.so.*

%changelog
* Wed Dec 18 2019 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt4
- don't require mp3gain

* Thu Mar 14 2019 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt3
- obsolete kde4-sounkonverter

* Fri Oct 27 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt2%ubt
- fix mp2 bitrate range (ALT#34073)
- fix load translations

* Thu Oct 26 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.1-alt1%ubt
- new version

* Mon Sep 18 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt1%ubt
- initial build
