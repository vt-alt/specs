Name:     qlcplus
Version:  5.0.0
Release:  alt0.alpha3

Summary:  Q Light Controller Plus

License:  ASL 2.0
Group:    Other
Url:      https://github.com/mcallegari/qlcplus

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++ qt5-base-devel libudev-devel qt5-multimedia-devel
BuildRequires: qt5-script-devel libalsa-devel libftdi1-devel libusb-compat-devel

%description
QLC+ is a fork of the great QLC project written by Heikki Junnila. This project
aims to continue the development of QLC and to introduce new features.
The primary goal is to bring QLC+ at the level of other lighting control
commercial softwares.

%prep
%setup
sed -i '95s/lib/%_lib/' variables.pri

%build
qmake-qt5
make %{?_smp_mflags}

%install
INSTALL_ROOT=%buildroot make install

%files
%_bindir/qlcplus
%_bindir/qlcplus-fixtureeditor
%_libdir/libqlcplusengine*
%_libdir/libqlcplusui*
%_libdir/libqlcpluswebaccess*
%_datadir/qlcplus/
%_libdir/qt5/plugins/qlcplus/
%_datadir/applications/qlcplus.desktop
%_datadir/appdata/qlcplus*.xml
%_man1dir/*
%_datadir/pixmaps/qlcplus.png
%_datadir/applications/qlcplus-fixtureeditor.desktop
%_datadir/pixmaps/qlcplus-fixtureeditor.png
%_datadir/mime/packages/qlcplus.xml
%_sysconfdir/udev/rules.d/*

%changelog
* Mon May 27 2019 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt0.alpha3
- Initial build for Sisyphus (Closes: #36799).
