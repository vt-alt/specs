Name: telepathy-morse
Version: 0.1.0
Release: alt3

Summary: Morse is a Qt-based Telegram connection manager for the Telepathy framework.
License: GPLv2
Group: System/Libraries

URL: https://telepathy.freedesktop.org/components/telepathy-morse/
Source: telepathy-morse-%version.tar

# Automatically added by buildreq on Fri Apr 20 2018
# optimized out: cmake-modules gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libqt5-core libqt5-dbus libqt5-network libqt5-xml libstdc++-devel libtelegram-qt5 libtelepathy-qt5-farstream0 libtelepathy-qt5-service0 libtelepathy-qt50 python-base python-modules
BuildRequires: cmake libssl-devel qt5-base-devel telepathy-qt5-devel zlib-devel
BuildRequires: libtelegram-qt5-devel

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_prefix/libexec/telepathy-morse
%_datadir/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.morse.service
%_datadir/telepathy/

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt2
- NMU: remove %ubt from release

* Fri Apr 20 2018 Oleg Solovyov <mcpain@altlinux.org> 0.1.0-alt1%ubt
- initial build for ALT

