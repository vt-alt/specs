Name: libqtkeychain-qt5
Version: 0.9.1
Release: alt3

%define sover 1
%define libqt5keychain libqt5keychain%sover

Group: Development/KDE and QT
Summary: QtKeychain is a Qt API to store passwords and other secret data securely
License: 2-clause BSD
Url: https://github.com/frankosterfeld/qtkeychain

Source0: %name-%version.tar
BuildRequires: cmake qt5-tools-devel pkgconfig(Qt5DBus) libsecret-devel

%description
QtKeychain is a Qt API to store passwords and other secret data securely.
If running, GNOME Keyring is used, otherwise  qtkeychain tries to use
KWallet (via D-Bus), if available.

%package -n qt5keychain-common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
Conflicts: libqtkeychain-qt5 < 0.7
%description -n qt5keychain-common
%name common package

%package -n %libqt5keychain
Group: Development/KDE and QT
Summary: A password store library
Provides: qtkeychain-qt5 = %version
Requires: qt5keychain-common
%description -n %libqt5keychain
The qt5keychain library allows you to store passwords easy and secure.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name-qt5
Provides: qtkeychain-qt5-devel = %version
Requires: libsecret-devel
%description devel
This package contains development files for qt5keychain.

%prep
%setup

%build
QTDIR="%_qt5_prefix" \
%cmake .. \
    -DBUILD_WITH_QT4:BOOL=OFF \
    -DQTKEYCHAIN_STATIC=OFF \
    -DECM_MKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
PATH=$PATH:%_qt5_bindir \
make install DESTDIR=%buildroot -C BUILD

%find_lang --with-qt qtkeychain

%files -n qt5keychain-common -f qtkeychain.lang
%doc ReadMe.txt
%doc COPYING

%files -n %libqt5keychain
%_libdir/libqt5keychain.so.%sover
%_libdir/libqt5keychain.so.*

%files devel
%_includedir/qt5keychain/
%_libdir/cmake/Qt5Keychain/
%_libdir/libqt5keychain.so
%_qt5_archdatadir/mkspecs/qt_Qt5Keychain.pri

%changelog
* Wed Aug 28 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt3
- separate with qt4 version

