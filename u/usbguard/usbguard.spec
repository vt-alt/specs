
%define _localstatedir /var
%define _libexecdir /usr/libexec

%def_enable dbus
%def_disable applet

%define sover 0
%define libusbguard libusbguard%sover

Name: usbguard
Version: 0.7.8
Release: alt1

Group: System/Servers
Summary: A tool for implementing USB device usage policy
License: GPLv2+
Url: https://usbguard.github.io/

#Requires: systemd
#Requires(post): systemd
#Requires(preun): systemd
#Requires(postun): systemd
Requires: %name-common = %EVR

Source0: %name-%version.tar
Source1: usbguard-daemon.conf

# Automatically added by buildreq on Fri Aug 04 2017 (-bi)
# optimized out: elfutils gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libcap-ng libdbus-devel libdbus-glib libgpg-error libgpg-error-devel libqt4-devel libqt5-core libqt5-gui libqt5-svg libqt5-widgets libqt5-xml libstdc++-devel perl pkg-config python-base python-modules python3 python3-base qt5-base-common qt5-base-devel rpm-build-python3 ruby ruby-stdlibs xml-utils xz
#BuildRequires: aspell catch-devel glibc-devel-static libcap-ng-devel libdbus-glib-devel libgcrypt-devel libgio-devel libprotobuf-devel libqb-devel libseccomp-devel pegtl-devel protobuf-compiler python-module-google python3-dev python3-module-zope qt5-svg-devel qt5-tools rpm-build-ruby xsltproc
BuildRequires: glibc-devel libcap-ng-devel libgcrypt-devel libseccomp-devel
#BuildRequires: catch pegtl-devel
BuildRequires: xsltproc asciidoctor
BuildRequires: libsystemd-devel libaudit-devel
BuildRequires: qt5-svg-devel qt5-tools
BuildRequires: libprotobuf-devel protobuf-compiler libqb-devel
BuildRequires: libumockdev-devel
%if_enabled dbus
BuildRequires: libdbus-glib-devel libgio-devel libpolkit-devel
%endif

%description
The USBGuard software framework helps to protect your computer against rogue USB
devices by implementing basic whitelisting/blacklisting capabilities based on
USB device attributes.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
%description common
%name common package

%package -n %libusbguard
Group: System/Libraries
Summary: %name library
Requires: %name-common = %EVR
%description -n %libusbguard
%name library

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name-common = %EVR
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package utils
Summary: USBGuard Utils
Group: System/Configuration/Hardware
Requires: %name-common = %EVR
Provides: usbguard-tools = %EVR
%description utils
The %name-utils package contains optional utils from the USBGuard
software framework.

%package applet
Summary: USBGuard Applet
Group: System/Configuration/Hardware
Requires: %name
Requires: libqt5-svg
Provides: usbguard-applet-qt = %EVR
%description applet
The %name-applet package contains an optional desktop applet
for interacting with the USBGuard daemon component.

%if_enabled dbus
%package dbus
Summary: USBGuard D-Bus Service
Group: System/Configuration/Hardware
Requires: %name
Requires: dbus polkit
%description dbus
The %name-dbus package contains an optional component that provides
a D-Bus interface to the USBGuard daemon component.
%endif

%prep
%setup
mv .gear/ThirdParty/* src/ThirdParty/
%autoreconf

%if_enabled applet
# systray want to show icon
for f in src/GUI.Qt/*.cpp; do
    sed -i '/systray->setIcon(/s/QIcon(/QPixmap(/' $f
    sed -i '/QSystemTrayIcon(/s/QIcon(/QPixmap(/' $f
done
%endif

%build
%configure \
    --disable-static \
    --enable-shared \
    --disable-silent-rules \
    --with-bundled-catch \
    --with-bundled-pegtl \
    --enable-systemd \
%if_enabled applet
    --with-gui-qt=qt5 \
%endif
%if_enabled dbus
    --with-dbus \
    --with-polkit \
%else
    --without-dbus \
    --without-polkit \
%endif
    --with-crypto-library=gcrypt \
    #
%make_build
asciidoctor -v -b html README.adoc -o README.html

%install
%make INSTALL='install -p' DESTDIR=%buildroot install-am

# Overwrite configuration with distribution defaults
mkdir -p %buildroot%_sysconfdir/usbguard
install -p -m 644 %SOURCE1 %buildroot%_sysconfdir/usbguard/usbguard-daemon.conf

%files common

%files
%doc README.html CHANGELOG.*
%_sbindir/usbguard-daemon
%_bindir/usbguard
%dir %_localstatedir/log/usbguard
%dir %_sysconfdir/usbguard
%dir %_sysconfdir/usbguard/IPCAccessControl.d
%config(noreplace) %attr(0600,root,root) %_sysconfdir/usbguard/usbguard-daemon.conf
%config(noreplace) %attr(0600,root,root) %_sysconfdir/usbguard/rules.conf
%_unitdir/usbguard.service
#%_datadir/bash-completion/completions/usbguard

%files -n %libusbguard
%_libdir/libusbguard.so.%sover
%_libdir/libusbguard.so.%sover.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files utils
%_bindir/usbguard-rule-parser

%if_enabled applet
%files applet
%_bindir/usbguard-applet-qt
%_datadir/applications/usbguard-applet-qt.desktop
%_iconsdir/*/*/apps/usbguard-icon.*
%endif

%if_enabled dbus
%files dbus
%_sbindir/usbguard-dbus
%_datadir/dbus-1/system-services/org.usbguard1.service
%_datadir/dbus-1/system.d/org.usbguard1.conf
%_datadir/polkit-1/actions/org.usbguard1.policy
%_unitdir/usbguard-dbus.service
%endif

%changelog
* Tue Jul 07 2020 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt1
- new version

* Thu Feb 06 2020 Sergey V Turchin <zerg@altlinux.org> 0.7.6-alt1
- new version

* Tue Mar 26 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.4-alt2
- rebuild with new protobuf
- do not use %%ubt macro

* Wed Aug 08 2018 Sergey V Turchin <zerg@altlinux.org> 0.7.4-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt3
- merge upstream fix for audit backend

* Wed Apr 04 2018 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt2
- update default usbguard-daemon.conf

* Tue Apr 03 2018 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- new version
- fix systemtray icon (ALT#34752)

* Tue Dec 26 2017 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- new version

* Mon Aug 07 2017 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt2
- fix configs permissions

* Fri Aug 04 2017 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- initial build
