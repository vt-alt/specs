Name:		ripes
Version:	1.0.3
Release:	alt2
Source:		v.%version.tar.gz
Summary:	A graphical 5-stage RISC-V pipeline simulator
Group:		Emulators
License:	MIT
URL:		https://github.com/mortbopet/Ripes

# Automatically added by buildreq on Thu Aug 01 2019
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libqt5-core libqt5-gui libqt5-svg libqt5-widgets libstdc++-devel python-base python-modules qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel sh4
BuildRequires: qt5-3d-devel qt5-charts-devel qt5-connectivity-devel qt5-datavis3d-devel qt5-gamepad-devel qt5-multimedia-devel qt5-networkauth-devel qt5-phonon-devel qt5-quickcontrols2-devel qt5-script-devel qt5-scxml-devel qt5-sensors-devel qt5-serialbus-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-virtualkeyboard-devel qt5-wayland-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-webview-devel qt5-x11extras-devel qt5-xmlpatterns-devel

%description
Ripes is a graphical 5-stage processor pipeline simulator and assembly
code editor built for the RISC-V instruction set architecture, suitable
for teaching how assembly level code is executed on a classic pipelined
architecture. Ripes is especially suitable for illustrating how concepts
such as forwarding and stalling works, giving a visual representation of
both cases.

%prep
%setup -n Ripes-v.%version

%build
%qmake_qt5
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot STRIP=/bin/true
install -D appdir/usr/share/applications/Ripes.desktop %buildroot%_desktopdir/Ripes.desktop

%files
%doc *.md
%_bindir/*
%_desktopdir/*

%changelog
* Thu Aug 01 2019 Fr. Br. George <george@altlinux.ru> 1.0.3-alt2
- Update to git 2019-05-21

* Thu Aug 01 2019 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Initial build for ALT

