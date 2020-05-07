Summary:	Audio/Video converter
Name:		mystiq
Version:	20.03.23
Release:	alt1
License:	GPLv3
Group:		Video
Url:		https://mystiqapp.com/
Source0:	MystiQ-%version.tar.gz

Requires:	/usr/bin/ffmpeg /usr/bin/ffprobe /usr/bin/sox

BuildPreReq:	extra-cmake-modules

# Automatically added by buildreq on Fri May 01 2020 (-bi)
# optimized out: elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libGL-devel libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-opengl libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-widgets libqt5-xml libstdc++-devel pkg-config python-base python-modules qt5-base-devel qt5-tools sh4 xz
BuildRequires: qt5-charts-devel qt5-declarative-devel qt5-multimedia-devel qt5-svg-devel qt5-tools-devel

%description
MystiQ is a GUI for FFmpeg, a powerful media converter.
FFmpeg can read audio and video files in various
formats and convert them into other formats.
MystiQ features an intuitive graphical
interface and a rich set of presets to help you
convert media files within a few clicks.
Advanced users can also adjust conversion parameters in detail.

%prep
%setup -n MystiQ-%version
chmod -x mystiq.desktop icons/mystiq.svg

%build
lrelease-qt5 *.pro
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" PREFIX=%prefix DEFINES+=NO_NEW_VERSION_CHECK
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/%name
%_datadir/metainfo/*
%_iconsdir/hicolor/scalable/apps/%name.svg
%_desktopdir/*.desktop
%_man1dir/*

%changelog
* Fri May 01 2020 Motsyo Gennadi <drool@altlinux.ru> 20.03.23-alt1
- initial build
