#define git_hash .git173782d7331e
%define git_hash %nil

%define dbus_version 1.2.12-alt2
%define libdbus_glib_version 0.76

%def_without libnm_glib

%if_with libnm_glib
%define nm_glib_sover 4
%define libnm_glib libnm-glib%nm_glib_sover
%define nm_glib_vpn_sover 1
%define libnm_glib_vpn libnm-glib-vpn%nm_glib_vpn_sover
%define nm_util_sover 2
%define libnm_util libnm-util%nm_util_sover
%endif

%define ppp_version %((%{__awk} '/^#define VERSION/ { print $NF }' /usr/include/pppd/patchlevel.h 2>/dev/null||echo none)|/usr/bin/tr -d '"')
%define wpa_supplicant_version 0.7.3-alt3
%define dhcpcd_version 4.0.0
%define openresolv_version 3.5.4-alt3

%def_enable systemd
%def_enable introspection
%def_enable teamdctl
%def_enable nmtui
%def_enable bluez5dun
%def_enable vala
%ifnarch %e2k %mips
%def_enable ovs
%else
%def_disable ovs
%endif
%def_without iwd

%if %{expand:%%{!?_without_check:%%{!?_disable_check:1}}0}
%define tests yes
%else
%define tests no
%endif

# There is no sources in debuginfo with LTO
%def_disable lto

# NOTE: ONLY use sanitizers for debug purposes
%def_disable sanitizers

%ifarch %e2k
%define more_warnings no
%else
%define more_warnings error
%endif

%if_with iwd
%define iwd_support yes
%else
%define iwd_support no
%endif

%define _name %name-daemon
%define dispatcherdir %_sysconfdir/NetworkManager/dispatcher.d
%define nmlibdir %_prefix/lib/NetworkManager
%define nmplugindir %_libdir/%name/%version-%release

%define _unpackaged_files_terminate_build 1

Name: NetworkManager
Version: 1.18.6
Release: alt1%git_hash
License: GPLv2+ and LGPLv2+
Group: System/Configuration/Networking
Summary: Install NetworkManager daemon and plugins
Url: http://www.gnome.org/projects/NetworkManager/
Vcs: git://git.freedesktop.org/git/NetworkManager/NetworkManager.git
Source: %name-%version.tar
Source1: %name.conf
Source2: 50-ntp
Source5: 20-hostname
Source6: NetworkManager.sysconfig
Source7: 30-efw
Source8: 80-etcnet-iface-scripts
Source9: NetworkManager-prestart
Source10: nm-dispatcher-sh-functions
Source11: NetworkManager.init
Patch: %name-%version-%release.patch

# For tests
%{?!_without_check:%{?!_disable_check:BuildPreReq: dbus dhcpcd dhcp-client}}
%{?!_without_check:%{?!_disable_check:BuildRequires: python3-module-pygobject3 python-module-dbus}}

BuildPreReq: intltool libgcrypt-devel libtool
BuildRequires: iproute2 ppp-devel
BuildRequires: libdbus-glib-devel >= %libdbus_glib_version
BuildRequires: libpolkit1-devel libnss-devel libgio-devel libuuid-devel gtk-doc
BuildRequires: libudev-devel
BuildRequires: iptables
BuildRequires: libmm-glib-devel
BuildRequires: libndp-devel
BuildRequires: libreadline-devel
BuildRequires: libaudit-devel
BuildRequires: libcurl-devel libpsl-devel
BuildRequires: python-module-pygobject3
%{?_enable_teamdctl:BuildRequires: libteamdctl-devel libjansson-devel}
%{?_enable_nmtui:BuildRequires: libnewt-devel}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgudev-gir-devel}
%{?_enable_systemd:BuildRequires: systemd-devel libsystemd-login-devel}
%{?_enable_bluez5dun:BuildRequires: libbluez-devel}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala}
%{?_enable_vala:BuildRequires: vala-tools}
# For create-exports-NetworkManager.sh
BuildRequires: /proc

Requires: dnsmasq

Requires: %name-adsl = %version-%release
Requires: %name-bluetooth = %version-%release
%{?_enable_teamdctl:Requires: %name-team}
Requires: %name-wifi = %version-%release
Requires: %name-wwan = %version-%release
Requires: %name-ppp = %version-%release

%description
NetworkManager is a system service that manages network interfaces and
connections based on user or automatic configuration. It supports
Ethernet, Bridge, Bond, VLAN, Team, InfiniBand, Wi-Fi, mobile broadband
(WWAN), PPPoE and other devices, and supports a variety of different VPN
services.

This is virtual package for install NetworkManager daemon
and all its plugins (excluding VPN plugins).

%package daemon
License: GPLv2+
Group: System/Configuration/Networking
Summary: Network Link Manager and User Applications
Requires: dbus >= %dbus_version
Requires: iproute2 openssl
Requires: nss >= 3.11.7
Requires: openresolv >= %openresolv_version
Requires: openresolv-dnsmasq >= %openresolv_version
Requires: libshell

Conflicts: NetworkManager-vpnc < 1.1.90
Conflicts: NetworkManager-openvpn < 1.1.90
Conflicts: NetworkManager-pptp < 1.1.90
Conflicts: NetworkManager-openconnect < 1.1.90
Conflicts: NetworkManager-l2tp < 1.1.0
Conflicts: NetworkManager-ssh < 1.1.0
Conflicts: NetworkManager-gnome < 1.1.90

Conflicts: dhcpcd < %dhcpcd_version

Obsoletes: nmcli

Provides: network-config-subsystem

%description daemon
NetworkManager is a system service that manages network interfaces and
connections based on user or automatic configuration. It supports
Ethernet, Bridge, Bond, VLAN, Team, InfiniBand, Wi-Fi, mobile broadband
(WWAN), PPPoE and other devices, and supports a variety of different VPN
services.

This package contents NetworkManager daemon itself and other
utilities.

%package adsl
License: GPLv2+
Summary: ADSL device plugin for NetworkManager
Group: System/Configuration/Networking
Requires: ppp-pppoe
Requires: %_name = %version-%release
Requires: %name-ppp = %version-%release

%description adsl
This package contains NetworkManager support for ADSL devices.

%package bluetooth
License: GPLv2+
Summary: Bluetooth device plugin for NetworkManager
Group: System/Configuration/Networking
Requires: %_name = %version-%release
Requires: %name-wwan = %version-%release

%description bluetooth
This package contains NetworkManager support for Bluetooth devices.

%package ovs
License: GPLv2+
Summary: OpenVSwitch device plugin for NetworkManager
Group: System/Configuration/Networking
Requires: %_name = %version-%release
Requires: openvswitch

%description ovs
This package contains NetworkManager support for OpenVSwitch bridges.

%package team
License: GPLv2+
Summary: Team device plugin for NetworkManager
Group: System/Configuration/Networking
Requires: teamd
Requires: %_name = %version-%release

%description team
This package contains NetworkManager support for team devices.

%package wifi
License: GPLv2+
Summary: Wifi plugin for NetworkManager
Group: System/Configuration/Networking
Requires: wpa_supplicant >= %wpa_supplicant_version
Requires: %_name = %version-%release

%description wifi
This package contains NetworkManager support for Wifi and OLPC devices.

%package wwan
License: GPLv2+
Summary: Mobile broadband device plugin for NetworkManager
Group: System/Configuration/Networking
Requires: ModemManager >= 0.7
Requires: %_name = %version-%release

%description wwan
This package contains NetworkManager support for mobile broadband (WWAN) devices.

%package ppp
License: GPLv2+
Summary: PPP plugin for NetworkManager
Group: System/Configuration/Networking
Requires: %_name = %version-%release
Requires: ppp = %ppp_version

%description ppp
This package contains NetworkManager support for PPP.

%package tui
License: GPLv2+
Summary: Curses-based Text User Interface for NetworkManager
Group: System/Configuration/Networking
Requires: %_name = %version-%release

%description tui
%summary

%if_with libnm_glib
%package devel
License: LGPLv2+
Summary: Libraries and headers for adding NetworkManager support to applications
Group: Development/Other
Requires: libdbus-glib >= %libdbus_glib_version
Requires: libdbus-devel >= %dbus_version
Requires: pkgconfig

%description devel
This package contains various headers accessing some NetworkManager
functionality from applications.
%endif

%package -n libnm
License: LGPLv2+
Summary: Library for adding NetworkManager support to applications
Group: System/Libraries

%description -n libnm
This package contains the libraries that make it easier to use some
NetworkManager functionality from applications.

%if_with libnm_glib
%package -n %libnm_glib
License: LGPLv2+
Summary: Library for adding NetworkManager support to applications that use glib
Group: System/Libraries
Requires: dbus >= %dbus_version
Obsoletes: NetworkManager-glib < 0.9.10.0

%description -n %libnm_glib
This package contains the library that applications can use to query
connection status via NetworkManager.

%package -n %libnm_glib_vpn
License: LGPLv2+
Summary: Library for creating VPN connections via NetworkManager
Group: System/Libraries
Requires: dbus >= %dbus_version
Obsoletes: NetworkManager-glib < 0.9.10.0

%description -n %libnm_glib_vpn
This package contains the library that applications can use for creating
VPN connections via NetworkManager.

%package -n %libnm_util
License: LGPLv2+
Summary: A convenience library to ease the access to NetworkManager.
Group: System/Libraries
Requires: dbus >= %dbus_version
Obsoletes: NetworkManager-glib < 0.9.10.0

%description -n %libnm_util
This package contains a convenience library to ease the access to
NetworkManager.

%package glib-devel
License: LGPLv2+
Summary: Header files for adding NetworkManager support to applications that use glib.
Group: Development/GNOME and GTK+
Requires: libnm-glib-devel libnm-glib-vpn-devel libnm-util-devel
BuildArch: noarch

%description glib-devel
Virtual package for backward compatibility.
Deprecated and will be removed soon.
%endif

%package -n libnm-devel
License: LGPLv2+
Summary: Header files for adding NetworkManager support to applications.
Group: Development/C
Requires: glib2-devel
Requires: pkgconfig
Requires: libdbus-glib-devel >= %libdbus_glib_version
Requires: libnm = %version-%release

%description -n libnm-devel
This package contains the header and pkg-config files for development
applications using NetworkManager functionality.

%if_with libnm_glib
%package -n libnm-glib-devel
License: LGPLv2+
Summary: Header files for adding NetworkManager support to applications that use glib.
Group: Development/C
Requires: %name-devel = %version-%release
Requires: libnm-util-devel = %version-%release
Requires: glib2-devel
Requires: pkgconfig
Requires: libdbus-glib-devel >= %libdbus_glib_version
Requires: %libnm_glib = %version-%release

%description -n libnm-glib-devel
This package contains the header and pkg-config files for development
applications that can to query connection status via NetworkManager.

%package -n libnm-glib-vpn-devel
License: LGPLv2+
Summary: Header files for %libnm_glib_vpn
Group: Development/C
Requires: %name-devel = %version-%release
Requires: libnm-glib-devel = %version-%release
Requires: glib2-devel
Requires: pkgconfig
Requires: libdbus-glib-devel >= %libdbus_glib_version
Requires: %libnm_glib_vpn = %version-%release

%description -n libnm-glib-vpn-devel
This package contains the header and pkg-config files for development
applications that can to create VPN connections via NetworkManager.

%package -n libnm-util-devel
License: LGPLv2+
Summary: Header files for %libnm_util
Group: Development/C
Requires: %name-devel = %version-%release
Requires: %libnm_util = %version-%release
Requires: glib2-devel
Requires: pkgconfig
Requires: libdbus-glib-devel >= %libdbus_glib_version

%description -n libnm-util-devel
This package contains the header and pkg-config files
for %libnm_util.
%endif

%package -n libnm-devel-doc
License: GFDL-1.1+
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n libnm-devel-doc
This package contains development documentation for %name.

%if_with libnm_glib
%package devel-doc
License: GFDL-1.1+
Summary: Development documentation for %name
Group: Development/Documentation
Obsoletes: NetworkManager-glib-devel-doc < 0.9.10.0
Provides: NetworkManager-glib-devel-doc = %version-%release
BuildArch: noarch
Requires: libnm-devel-doc = %version-%release

# No comments
Obsoletes: %name-%name-devel-doc < %version-%release

%description devel-doc
This package contains development documentation for %name.
Includes libnm-util and libnm-glib development documentation.
%endif

%package -n libnm-gir
License: LGPLv2+
Summary: GObject introspection data for the NetworkManager (libnm)
Group: System/Libraries
Requires: libnm = %version-%release

%description -n libnm-gir
GObject introspection data for the NetworkManager (libnm).

%package -n libnm-gir-devel
License: LGPLv2+
Summary: GObject introspection devel data for the NetworkManager (libnm)
Group: System/Libraries
BuildArch: noarch
Requires: libnm-gir = %version-%release

%description -n libnm-gir-devel
GObject introspection devel data for the NetworkManager (libnm).

%if_with libnm_glib
%package glib-gir
License: LGPLv2+
Summary: GObject introspection data for the NetworkManager
Group: System/Libraries
Requires: %libnm_glib %libnm_glib_vpn %libnm_util

%description glib-gir
GObject introspection data for the NetworkManager.

%package glib-gir-devel
License: LGPLv2+
Summary: GObject introspection devel data for the NetworkManager
Group: System/Libraries
BuildArch: noarch
Requires: %name-glib-gir = %version-%release
Requires: libnm-glib-devel = %version-%release
Requires: libnm-glib-vpn-devel = %version-%release
Requires: libnm-util-devel = %version-%release

%description glib-gir-devel
GObject introspection devel data for the NetworkManager.
%endif

%prep
%setup
%patch -p1

%build
%add_optflags -fpie
export LDFLAGS=-pie
%autoreconf
%configure \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
	--docdir=%_defaultdocdir/%name-%version \
	--disable-static \
	--with-crypto=nss \
	--with-dhclient=/sbin/dhclient \
	--with-dhcpcd=yes \
	--with-config-dhcp-default=internal \
	--with-dnsmasq=/usr/sbin/dnsmasq \
	--enable-gtk-doc=yes \
	--with-config-dns-rc-manager-default=resolvconf \
	--with-resolvconf=/sbin/resolvconf \
	--enable-concheck \
	--with-pppd-plugin-dir=%_libdir/pppd/%ppp_version \
	--enable-ppp=yes \
	--with-system-ca-path=/var/lib/ssl/certs \
	--enable-tests=%tests \
	%{?_enable_systemd:--with-systemdsystemunitdir=/lib/systemd/system} \
%if_enabled systemd
	--with-session-tracking=systemd \
	--with-suspend-resume=systemd \
	--with-config-logging-backend-default=journal \
%else
	--with-session-tracking=ck \
	--with-suspend-resume=upower \
	--with-config-logging-backend-default=syslog \
%endif
	--with-udev-dir=/lib/udev \
	--enable-polkit=yes \
	--enable-polkit-agent \
	--enable-modify-system=no \
	--enable-etcnet-alt \
	--disable-ifcfg-rh \
	--disable-ifupdown \
	--enable-config-plugin-ibft \
	--with-config-plugins-default='etcnet-alt' \
	--with-modem-manager-1 \
	%{subst_enable teamdctl} \
	%{subst_enable ovs} \
%if_enabled nmtui
	--with-nmtui=yes \
%else
	--with-nmtui=no \
%endif
%if_enabled bluez5dun
	--enable-bluez5-dun \
%else
	--disable-bluez5-dun \
%endif
	--enable-introspection=auto \
	%{subst_enable lto} \
	%{subst_enable vala} \
	--with-libaudit=yes-disabled-by-default \
	--with-ofono=no \
%if_enabled teamdctl
	--enable-json-validation \
%else
	--disable-json-validation \
%endif
	--with-libpsl=yes \
%if_enabled sanitizers
	--with-address-sanitizer=yes \
	--enable-undefined-sanitizer \
%else
	--without-address-sanitizer \
	--disable-undefined-sanitizer \
%endif
%if_with libnm_glib
	--with-libnm-glib \
%else
	--without-libnm-glib \
%endif
	--with-iwd=%iwd_support \
	--with-dist-version=%version-%release \
	--disable-silent-rules \
	--enable-more-warnings=%more_warnings

%make_build

# Set charset utf8 for utf8 man page
sed -i '1i .\\" -*- mode: troff; coding: utf8 -*-' man/nmcli-examples.7

%install
%makeinstall_std
%find_lang %name
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_sysconfdir/NetworkManager/VPN
mkdir -p %buildroot%_sysconfdir/NetworkManager/system-connections
mkdir -p %buildroot%_sysconfdir/NetworkManager/conf.d
mkdir -p %buildroot%nmlibdir/conf.d
mkdir -p %buildroot/%_var/log/
touch %buildroot/%_var/log/NetworkManager
mkdir -p %buildroot/%_var/lib/NetworkManager
touch %buildroot/%_var/lib/NetworkManager/timestamps
touch %buildroot/%_var/lib/NetworkManager/NetworkManager.state
mkdir -p %buildroot%nmlibdir/VPN/
install -m 0644 %SOURCE1 %buildroot%_sysconfdir/NetworkManager/
install -m 0755 %SOURCE2 %buildroot%dispatcherdir/
install -m 0755 %SOURCE5 %buildroot%dispatcherdir/
install -m 0755 %SOURCE7 %buildroot%dispatcherdir/
install -m 0755 %SOURCE8 %buildroot%dispatcherdir/
install -Dm0644 %SOURCE6 %buildroot%_sysconfdir/sysconfig/%name

# Create pre-down.d/pre-up.d directories and
# symlink scripts if needed
mkdir -p %buildroot%dispatcherdir/pre-{up,down}.d
ln -s ../80-etcnet-iface-scripts %buildroot%dispatcherdir/pre-up.d/80-etcnet-iface-scripts
ln -s ../80-etcnet-iface-scripts %buildroot%dispatcherdir/pre-down.d/80-etcnet-iface-scripts

# Install initscript
install -Dm0755 %SOURCE11 %buildroot%_initrddir/NetworkManager

# Install NetworkManager pre start script
install -Dm0755 %SOURCE9 %buildroot%_sbindir/NetworkManager-prestart

# Install functions file for nm-dispather scripts
install -Dm0644 %SOURCE10 %buildroot%_libexecdir/NetworkManager/nm-dispatcher-sh-functions

# Install example configs
mkdir -p %buildroot%_defaultdocdir/%name-%version/examples/conf.d/
cp -a examples/nm-conf.d/* %buildroot%_defaultdocdir/%name-%version/examples/conf.d/

# Use 31-mac-addr-change.conf
# See https://bugzilla.altlinux.org/32467
# https://bugzilla.gnome.org/show_bug.cgi?id=777523
mv %buildroot%_defaultdocdir/%name-%version/examples/conf.d/31-mac-addr-change.conf %buildroot%nmlibdir/conf.d/

%check
make check

%pre daemon
# Workaround for upgrade
[ -d %_var/lib/NetworkManager/timestamps ] &&
rm -rf %_var/lib/NetworkManager/timestamps/ ||:

%post daemon
#post_service %name
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
	"$SYSTEMCTL" daemon-reload ||:
	if [ "$1" -eq 1 ]; then
		"$SYSTEMCTL" -q preset %name.service %name-wait-online.service %name-dispatcher.service ||:
	fi
else
	if [ "$1" -eq 1 ]; then
		/sbin/chkconfig --add NetworkManager ||:
	else
		/sbin/chkconfig NetworkManager resetpriorities ||:
	fi
fi

%preun daemon
#preun_service %name
if [ "$1" -eq 0 ]; then
	SYSTEMCTL=systemctl
	if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
		"$SYSTEMCTL" --no-reload -q disable %name.service %name-wait-online.service %name-dispatcher.service ||:
	else
		chkconfig --del NetworkManager ||:
	fi

    killall -TERM nm-system-settings >/dev/null 2>&1 ||:
fi

%triggerpostun daemon -- %name <= 0.9.8.2-alt3
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" -q is-enabled %name.service; then
	"$SYSTEMCTL" enable -q %name-dispatcher.service
fi

%files

%files -f %name.lang daemon
%doc COPYING NEWS AUTHORS README CONTRIBUTING TODO
%_bindir/nm-online
%_bindir/nmcli
%_datadir/dbus-1/system-services/*.service
%doc %_man1dir/*.*
%doc %_man5dir/*.*
%doc %_man7dir/*.*
%doc %_man8dir/*.*
%doc %_defaultdocdir/%name-%version/
%dir %_libdir/NetworkManager/
%dir %nmlibdir/
%dir %nmlibdir/VPN/
%dir %nmplugindir/
%nmplugindir/libnm-settings-plugin-*.so
%_libexecdir/NetworkManager/nm-*
%_sbindir/*
%_sysconfdir/dbus-1/system.d/*.conf
%config(noreplace) %_sysconfdir/NetworkManager/%name.conf
%_initrddir/NetworkManager
%dir %_sysconfdir/NetworkManager
%dir %_sysconfdir/NetworkManager/VPN
%dir %_sysconfdir/NetworkManager/system-connections
%dir %_sysconfdir/NetworkManager/conf.d
%dir %nmlibdir/conf.d/
%config %nmlibdir/conf.d/31-mac-addr-change.conf
%dir %_var/lib/NetworkManager
%dispatcherdir/
%ghost %config(noreplace) %_var/log/NetworkManager
%ghost %config(noreplace) %_var/lib/NetworkManager/NetworkManager.state
%ghost %config(noreplace) %_var/lib/NetworkManager/timestamps
/lib/udev/rules.d/*
%_datadir/polkit-1/actions/*.policy
%_datadir/bash-completion/completions/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%{?_enable_systemd:/lib/systemd/system/%name.service}
%{?_enable_systemd:/lib/systemd/system/%name-wait-online.service}
%{?_enable_systemd:/lib/systemd/system/%name-dispatcher.service}
%if_enabled ovs
%{?_enable_systemd:%dir %_unitdir/NetworkManager.service.d/}
%endif

%exclude %_man1dir/nmtui*
%if_enabled ovs
%exclude %_man7dir/nm-openvswitch.*
%endif

%files adsl
%nmplugindir/libnm-device-plugin-adsl.so

%files bluetooth
%nmplugindir/libnm-device-plugin-bluetooth.so

%if_enabled ovs
%files ovs
%_unitdir/NetworkManager.service.d/NetworkManager-ovs.conf
%nmplugindir/libnm-device-plugin-ovs.so
%_man7dir/nm-openvswitch.*
%endif

%if_enabled teamdctl
%files team
%nmplugindir/libnm-device-plugin-team.so
%endif

%files wifi
%nmplugindir/libnm-device-plugin-wifi.so

%files wwan
%nmplugindir/libnm-device-plugin-wwan.so
%nmplugindir/libnm-wwan.so

%if_enabled nmtui
%files tui
%_bindir/nmtui*
%_man1dir/nmtui*
%endif

%files ppp
%_libdir/pppd/%ppp_version/nm-pppd-plugin.so
%nmplugindir/libnm-ppp-plugin.so

%if_with libnm_glib
%files devel
%dir %_includedir/%name
%_includedir/%name/%name.h
%_includedir/%name/NetworkManagerVPN.h
%_includedir/%name/nm-version-macros.h
%_includedir/%name/nm-version.h
%_pkgconfigdir/%name.pc
%endif

%files -n libnm
%_libdir/libnm.so.*

%if_with libnm_glib
%files -n %libnm_glib
%_libdir/libnm-glib.so.%nm_glib_sover
%_libdir/libnm-glib.so.%nm_glib_sover.*

%files -n %libnm_glib_vpn
%_libdir/libnm-glib-vpn.so.%nm_glib_vpn_sover
%_libdir/libnm-glib-vpn.so.%nm_glib_vpn_sover.*

%files -n %libnm_util
%_libdir/libnm-util.so.%nm_util_sover
%_libdir/libnm-util.so.%nm_util_sover.*

%files glib-devel
%endif

%files -n libnm-devel
%_includedir/libnm
%_pkgconfigdir/libnm.pc
%_libdir/libnm.so
%{?_enable_vala:%_vapidir/libnm.*}
%_datadir/dbus-1/interfaces/*.xml

%if_with libnm_glib
%files -n libnm-glib-devel
%_includedir/libnm-glib
%exclude %_includedir/libnm-glib/nm-vpn-*.h
%_pkgconfigdir/libnm-glib.pc
%_libdir/libnm-glib.so
%{?_enable_vala:%_vapidir/libnm-glib.*}

%files -n libnm-glib-vpn-devel
%_includedir/libnm-glib/nm-vpn-*.h
%_pkgconfigdir/libnm-glib-vpn.pc
%_libdir/libnm-glib-vpn.so

%files -n libnm-util-devel
%_includedir/%name/nm-setting*.h
%_includedir/%name/nm-connection.h
%_includedir/%name/nm-utils*.h
%_pkgconfigdir/libnm-util.pc
%_libdir/libnm-util.so
%{?_enable_vala:%_vapidir/libnm-util.*}
%endif

%files -n libnm-devel-doc
%doc %_datadir/gtk-doc/html/libnm
%doc %_datadir/gtk-doc/html/%name

%if_with libnm_glib
%files devel-doc
%doc %_datadir/gtk-doc/html/libnm-glib
%doc %_datadir/gtk-doc/html/libnm-util
%endif

%if_enabled introspection
%files -n libnm-gir
%_libdir/girepository-1.0/NM-1.0.typelib

%files -n libnm-gir-devel
%_datadir/gir-1.0/NM-1.0.gir

%if_with libnm_glib
%files glib-gir
%_libdir/girepository-1.0/NMClient-1.0.typelib
%_libdir/girepository-1.0/NetworkManager-1.0.typelib

%files glib-gir-devel
%_datadir/gir-1.0/NMClient-1.0.gir
%_datadir/gir-1.0/NetworkManager-1.0.gir
%endif
%endif

%exclude %nmplugindir/*.la
%exclude %_libdir/pppd/%ppp_version/*.la

%changelog
* Fri May 15 2020 Mikhail Efremov <sem@altlinux.org> 1.18.6-alt1
- Added Vcs tag.
- Fixed license.
- Updated to 1.18.6.

* Mon Mar 09 2020 Alexey Shabalin <shaba@altlinux.org> 1.18.4-alt2
- Rebuild with ppp-2.4.8.

* Thu Oct 10 2019 Mikhail Efremov <sem@altlinux.org> 1.18.4-alt1
- Updated to 1.18.4.

* Sat Sep 28 2019 Mikhail Efremov <sem@altlinux.org> 1.18.3-alt2.git173782d7331e
- Fix build with glib-2.62.0.
- Upstream git snapshot (nm-1-18 branch).

* Wed Sep 18 2019 Mikhail Efremov <sem@altlinux.org> 1.18.3-alt1.gitade986436672
- sysconfig: Wait for network online on SysVinit by default.
- Backported from NM-1.20:
  + build: use regexp in gtkdoc --ignore-decorators option.
  + build: fix errors when building with gtk-doc 1.32.
  + data: fix the ID_NET_DRIVER udev rule.
- libnm-core: Set windows-1251 as prefered encoding for Cyrillic
  langs.
- Upstream git snapshot (nm-1-18 branch).

* Tue Apr 30 2019 Mikhail Efremov <sem@altlinux.org> 1.18.0-alt2
- etcnet-alt: Fix memory leak.
- etcnet-alt: Fix connections removal (closes: #35185).

* Mon Apr 22 2019 Mikhail Efremov <sem@altlinux.org> 1.18.0-alt1
- etcnet-alt: Update nm-udev-utils.h location.
- Build with -pie.
- etcnet-alt: Don't print 'current profile' message.
- etcnet-alt: Use nm_log_dbg in PLUGIN_DEBUG macro.
- Use internal DHCP client by default.
- Updated to 1.18.0.

* Mon Mar 18 2019 Mikhail Efremov <sem@altlinux.org> 1.16.0-alt1
- Updated to 1.16.0.

* Mon Mar 11 2019 Mikhail Efremov <sem@altlinux.org> 1.15.91-alt1
- Added iwd support knob.
- Updated to 1.15.91 (1.16-rc2).

* Mon Feb 25 2019 Mikhail Efremov <sem@altlinux.org> 1.15.90-alt1
- Drop non-existent plugins from configure options.
- Fix configure options for support sanitizer build.
- Fix configure option to disable ibft plugin.
- Treat warnings as errors again.
- Add rpm-build-vala to BR(pre).
- dispatcher hooks: Rename 50-ntpd -> 50-ntp.
- dispatcher hooks: Rewrite 50-ntpd.
- etcnet-alt: Update copyright year.
- etcnet-alt: Drop get_ether_addr_array() declaration.
- etcnet-alt: Fix read_supplicant_network() if no memory.
- etcnet-alt: Fix headers scope in the includes.
- Drop perl-YAML from BR.
- Drop libwireless-devel from BR.
- etcnet-alt: Drop unneeded includes.
- Drop libnl from BR.
- Updated to 1.15.90 (1.16-rc1).

* Fri Jan 25 2019 Mikhail Efremov <sem@altlinux.org> 1.14.5-alt3.git542e340f01b2
- Fix build: don't treat warnings as errors.
- Upstream git snapshot (nm-1-14 branch).

* Fri Dec 14 2018 Mikhail Efremov <sem@altlinux.org> 1.14.5-alt2.git1445b5b2966d
- Disable libnm-glib build.
- Start NM _after_ network.service.
- Update 'not set to disconndcted' patch.
- Fix 'not set to disconndcted' patch (closes: #35341).
- Revert "Require /proc for tests".
- etcnet-alt: Use g_[s]list_free_full() (closes: #35698).
- etcnet-alt: Fix indentation in nms-etcnet-alt-shvar.c.
- Upstream git snapshot (nm-1-14 branch).

* Thu Nov 01 2018 Mikhail Efremov <sem@altlinux.org> 1.14.5-alt1.gitba83251bba87
- Upstream git snapshot (nm-1-14 branch) (fixes: CVE-2018-15688).

* Fri Oct 26 2018 Mikhail Efremov <sem@altlinux.org> 1.14.5-alt1.git2c6fafad7abe
- Explicitly disable ibft plugin.
- Upstream git snapshot (nm-1-14 branch).

* Mon Oct 08 2018 Mikhail Efremov <sem@altlinux.org> 1.14.1-alt2.gitcd3aacefdd0b
- etcnet-alt: Fix setting of autoconnect property (closes: #35489).

* Fri Oct 05 2018 Mikhail Efremov <sem@altlinux.org> 1.14.1-alt1.gitcd3aacefdd0b
- Upstream git snapshot (nm-1-14 branch).

* Mon Sep 10 2018 Mikhail Efremov <sem@altlinux.org> 1.13.90-alt1
- Require /proc for tests.
- etcnet-alt tests: Fix interface name for test.
- etcnet-alt: Don't try to unref NULL.
- etcnet-alt: Use interface name instead of MAC to restrict connection.
- etcnet-alt: Use nm_connection_get_setting_connection().
- etcnet-alt: Fix nm_etcnet_connection_get_id().
- etcnet-alt: Update for upstream changes.
- Move network-config-subsystem provide to daemon subpackage.
- Updated to 1.13.90 (1.14-rc1).

* Fri Aug 03 2018 Mikhail Efremov <sem@altlinux.org> 1.12.2-alt3
- Disable ovs plugin for mips.

* Wed Aug 01 2018 Mikhail Efremov <sem@altlinux.org> 1.12.2-alt2
- Fix from upstream:
  + fix compile error due to NM_AVAILABLE_IN_1_12_2 macro.

* Thu Jul 26 2018 Mikhail Efremov <sem@altlinux.org> 1.12.2-alt1
- Updated to 1.12.2.

* Mon Jul 16 2018 Mikhail Efremov <sem@altlinux.org> 1.12.0-alt1
- Updated to 1.12.0.

* Mon Jun 18 2018 Mikhail Efremov <sem@altlinux.org> 1.11.90-alt1
- Fix requires.
- Make build with libnm-glib-* optional.
- Disable scan-rand-mac-address for rtl8192ce (closes: #35058).
- Cleanup BR.
- Don't package directory twice.
- Update path to plugins.
- etcnet-alt: Drop properties.
- etcnet-alt: Fix build with current NM.
- Updated 'not set to disconndcted' patch.
- Updated "Don't use dns plugins" patch.
- Updated to 1.11.90 (1.12-rc1).

* Fri May 11 2018 Mikhail Efremov <sem@altlinux.org> 1.10.8-alt1
- Disable ovs plugin on e2k.
- Use %%e2k macro.
- macro.h: Fix build on e2k.
- Make build with tests conditional.
- Update 'not set to disconndcted' patch.
- Updated to 1.10.8.

* Mon Mar 12 2018 Mikhail Efremov <sem@altlinux.org> 1.10.6-alt1
- Updated to 1.10.6.

* Wed Feb 21 2018 Mikhail Efremov <sem@altlinux.org> 1.10.4-alt2
- Don't fail if dhcp client for DHCPv6 didn't start.

* Fri Feb 09 2018 Mikhail Efremov <sem@altlinux.org> 1.10.4-alt1
- Drop obsoleted patch..
- Updated to 1.10.4.

* Mon Dec 25 2017 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt2
- Workaround 'deprecated structs' issue.
- Patches from upstream: bug fixes found via coverity.

* Thu Dec 14 2017 Mikhail Efremov <sem@altlinux.org> 1.10.2-alt1
- etcnet-alt: Use nm_settings_connection_update();
- Updated to 1.10.2.

* Tue Nov 14 2017 Mikhail Efremov <sem@altlinux.org> 1.10.0-alt1
- etcnet-alt: Fix nm_settings_connection_delete() call.
- Enable teamd support.
- Fix build on e2k.
- Updated to 1.10.0.

* Wed Sep 20 2017 Mikhail Efremov <sem@altlinux.org> 1.8.4-alt1
- Updated to 1.8.4.

* Tue Jul 11 2017 Mikhail Efremov <sem@altlinux.org> 1.8.2-alt1
- Use --with-dist-version configure option.
- Fixes from upstream:
  + add test parsing dhclient config.
  + improve "interface" statement parsing.
- Updated to 1.8.2.

* Wed Jul 05 2017 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1.git20170629
- sysconfig: Set NM_DOWN_CONTROLLED and NM_STOP_ONEXIT to 'no'.
- NetworkManager.conf: Drop note about MAC randomization.
- Disable changing MAC for broken drivers by default (closes: #32467).
- Explicitly set logging backend to journal if built with systemd.
- Enable json-validation if built with teamd.
- Package example config files.
- Use %%nmlibdir macro to package VPN directory.
- Package /usr/lib/NetworkManager/conf.d/ directory.
- Upstream git snapshot (nm-1-8 branch).

* Mon Apr 24 2017 Mikhail Efremov <sem@altlinux.org> 1.7.92-alt1
- Updated to 1.7.92 (1.8-rc3).

* Tue Apr 11 2017 Mikhail Efremov <sem@altlinux.org> 1.7.91-alt1
- NetworkManager.conf: Add note about Wi-Fi MAC rondomization.
- etcnet-alt: Don't print error if ipv4address doesn't exist.
- Drop wimax support.
- Fix wrong configure option.
- etcnet-alt: Don't return a value from read_device_config().
- etcnet-alt: Use libudev instead of libgudev.
- Update 'not set to disconndcted' patch.
- Drop 'build LTO' patch.
- Updated to 1.7.91 (1.8-rc2).

* Fri Feb 17 2017 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1
- etcnet-alt: Fix tests build.
- Build fixes from upstream.
- Updated to 1.6.2.

* Mon Feb 06 2017 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt1.git20170206
- Split PPP support into a separate subpackage.
- Upstream git snapshot (nm-1-6 branch).

* Wed Jan 25 2017 Mikhail Efremov <sem@altlinux.org> 1.5.3-alt1
- Package libnm vala bindings and DBus API.
- Add /proc to BR.
- Disable silent rules.
- Makefile: Fix etcnet-alt build.
- dispatcher scripts: Don't use obsoleted variables.
- etcnet-alt: Use glib test framework.
- etcnet-alt: merge etcnet-alt/tests/Makefile.am" into toplevel
  Makefile.
- etcnet-alt: rename files to "nms-etcnet-alt-*".
- dns-manager: Enable systemd-resolved plugin support.
- Updated to 1.5.3 (1.6-rc1).

* Fri Dec 16 2016 Mikhail Efremov <sem@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Mon Oct 03 2016 Mikhail Efremov <sem@altlinux.org> 1.4.2-alt1
- etcnet-alt: Fix get_property().
- Updated to 1.4.2.

* Fri Sep 16 2016 Mikhail Efremov <sem@altlinux.org> 1.4.1-alt1.git20160914
- keyfile/tests: Fix test without JSON library.
- Fix dhcpcd pidfile name.
- Upstream git snapshot (nm-1-4 branch).

* Mon Sep 05 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt2
- Patches from upstream (closes: #32467):
  + dbus: fix emitting D-Bus NetworkManager's old-style PropertiesChange
    signal
  + exported-object: fix source interface for PropertiesChanged D-Bus
    signal
  + device: don't let external changes cause a release of the slave
  + platform: fix return value for error case in
    do_change_link_request().
  + platform: fix build.
  + device: add hack to wait after changing MAC address.
  + device: fix spelling in logging.
  + platform: workaround kernel wrongly returning ENFILE when changing
    MAC address.
  + platform: split processing result from do_change_link().

* Thu Aug 25 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Tue Aug 23 2016 Mikhail Efremov <sem@altlinux.org> 1.3.91-alt1
- Updated to 1.3.91 (1.4-rc1).

* Thu Aug 04 2016 Mikhail Efremov <sem@altlinux.org> 1.2.4-alt1
- Build with libaudit support.
- Fix nmcli-examples(7) charset.
- Updated to 1.2.4.

* Wed May 11 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Thu Apr 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt2
- NetworkManager-prestart: Make errors non-fatal.
- Own %%_libexecdir/NetworkManager/VPN/.
- etcnet-alt: Add test no-type.
- etcnet-alt: Don't ignore interface if TYPE is not specified.

* Fri Apr 22 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Tue Apr 12 2016 Mikhail Efremov <sem@altlinux.org> 1.1.94-alt1
- Updated to 1.1.94 (1.2-rc2).

* Wed Apr 06 2016 Mikhail Efremov <sem@altlinux.org> 1.1.93-alt1
- Make NetworkManager-glib-devel subpackage noarch.
- Updated to 1.1.93 (1.2-rc1).

* Tue Mar 29 2016 Mikhail Efremov <sem@altlinux.org> 1.1.92-alt1
- Disable systemd tests.
- Fix documentation build.
- Use resolvconf with immutable resolv.conf too.
- Updated to 1.1.92 (1.2-beta3).

* Tue Mar 01 2016 Mikhail Efremov <sem@altlinux.org> 1.1.91-alt1
- etcnet-alt: convert tests to g_assert().
- etcnet-alt: Replace config.h with nm-default.h.
- Updated to 1.1.91 (1.2-beta2).

* Tue Jan 19 2016 Mikhail Efremov <sem@altlinux.org> 1.1.90-alt1
- etcnet-alt: Fix tests build.
- etcnet-alt: Fix build.
- etcnet-alt: Drop unneeded include.
- etcnet-alt: Remove hostname handling.
- etcnet-alt: Use NMSettingsPluginInterface.
- etcnet-alt: Add some includes to common.h.
- etcnet-alt: Rename NMSystemConfigInterface to NMSettingsPlugin.
- Updated "_nmconnect group" patch.
- Updated to 1.1.90.

* Wed Jan 13 2016 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt2
- Patches from upstream:
   + infiniband: take interface down to set transport mode.
   + device: update @ip_iface only if IP interface exists.
   + ppp-manager: clear @ppp_watch_id upon pppd termination.
   + core: fix failure to configure routes due to wrong device-route
     for IPv4 peer-addresses.

* Thu Dec 24 2015 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt1
- Patch from upstream:
  + man: fix typos.
- Updated to 1.0.10.

* Mon Nov 30 2015 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1
- Updated to 1.0.8.

* Mon Nov 02 2015 Mikhail Efremov <sem@altlinux.org> 1.0.7-alt1.git20151102
- nm-dispatcher-sh-functions: Drop debug output.
- Enable vala bindings (closes: #31422).
- Upstream git snapshot (nm-1-0 branch).

* Mon Aug 31 2015 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1
- Fix pkg-check of gio-unix-2.0 and gmodule.
- Add ability to skip any dispatcher script.
- Let the configure script find dhcpcd path.
- Own %_defaultdocdir/%name-%version/.
- Updated to 1.0.6.

* Tue Jul 14 2015 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Fix build with LTO (but disable it by default).
- etcnet-alt: Update nm_platform_*() functions call.
- etcnet-alt: Update tests.
- etcnet-alt: Explicitly set DHCPv6 as config method if needed.
- etcnet-alt: Allow 1/0 values in config files as TRUE/FALSE.
- etcnet-alt: Fix NM_CONTROLLED reading.
- etcnet-alt: Add 'no-nm-controlled' test.
- etcnet-alt: Setup more errors.
- etcnet-alt: Change options_true_value() signature.
- etcnet-alt: Explicitly disable IP configuration if needed.
- etcnet-alt: Print plugin name in messages.
- Updated to 1.0.4.

* Fri May 08 2015 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1
- Use symlinks for nmtui* manpages.
- Package /etc/NetworkManager/conf.d/ directory.
- Move nmtui manpages to tui subpackage.
- Don't package nm-settings-ifcfg-rh manpage.
- man: Add etcnet-alt decription and drop non-existent plugins.
- Drop DNS plugins description from man page.
- Use /var/lib/ssl/certs as system CA path.
- etcnet-alt: Fix nm_settings_connection_replace_settings() call.
- Update 'Don't use dns plugins' patch.
- Provide network-config-subsystem (closes: #30262).
- etcnet-alt: Get rid of duplicate code in the IP config.
- Updated to 1.0.2.

* Mon Feb 02 2015 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- Move dnsmasq and nm-dhcp-client requires to NetworkManager subpackage.
- Drop libgsystem.
- etcnet-alt: Update and port to libnm.
- Updated ALT-specific patches.
- Updated to 1.0.0.

* Mon Jan 19 2015 Mikhail Efremov <sem@altlinux.org> 0.9.10.1-alt3.git20141029
- Build with bluez5.

* Fri Jan 16 2015 Mikhail Efremov <sem@altlinux.org> 0.9.10.1-alt2.git20141029
- Rebuild with ppp-2.4.7.
- Fix 'Obsoletes' tags again (closes: #30542).

* Wed Oct 29 2014 Mikhail Efremov <sem@altlinux.org> 0.9.10.1-alt1.git20141029
- Upstream git snapshot (nm-0-9-10 branch).

* Fri Jul 25 2014 Mikhail Efremov <sem@altlinux.org> 0.9.10.0-alt1
- Package pre-down.d/pre-up.d directories.
- Replace 80-etcnet-post with 80-etcnet-iface-scripts.
- Drop 10-netfs hook.
- Updated to 0.9.10.0.

* Mon Jun 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.9.9.98-alt2
- define DISTRO_NETWORK_SERVICE=network.service for ALTLinux
- don't order NetworkManager-wait-online.service before network.target

* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.9.98-alt1
- Add libreadline-devel to BR.
- preun: Don't use preun_service.
- post: Handle all *.service in case of systemd.
- init script: Use --wait-for-startup option for nm-online.
- init script: Add comment about nm-dispatcher.action kill.
- Package examples/server.conf.
- Package plugins as separate packages.
- etcnet-alt: Updated for current NM.
- nm-dispatcher: Drop --persist option.
- Updated to 0.9.9.98 (0.9.10-rc1).

* Tue Apr 22 2014 Mikhail Efremov <sem@altlinux.org> 0.9.9.1-alt1.git20140422
- etcnet-alt: Use nm-platform.h instead of wifi-utils.h.
- etcnet-alt: Ignore more suffixes in the config files names.
- etcnet-alt: Update copyrights.
- etcnet-alt: Use macros for type cast.
- etcnet-alt: Fix profiled connections reading.
- etcnet-alt: Use default 'options' file for device type.
- etcnet-alt: Print message in case of unmanaged devices.
- dhcp-manager: downgrade warning about unhandled STOP DHCP
  event too.
- etcnet-alt: Refactor device config reading code.
- init script: Drop NM_STOP_MODEMMANAGER support.
- etcnet-alt: switch from $(INCLUDES) to $(AM_CPPFLAGS).
- etcnet-alt: Add reload_connections() function.
- etcnet-alt: Support monitor-connection-files config option.
- etcnet-alt: Fix plugin type name and cleanup.
- Upstream git snapshot (master branch).

* Thu Mar 27 2014 Mikhail Efremov <sem@altlinux.org> 0.9.9.1-alt1.git20140327
- init script: Updated for new nmcli syntax.
- Fix devel-doc subpackage name.
- Don't generate connections for unmanaged devices.
- etcnet-alt: Add more tests.
- etcnet-alt: Add initial bridges support.
- etcnet-alt: Use wifi_utils_is_wifi().
- Upstream git snapshot (master branch).

* Fri Feb 07 2014 Mikhail Efremov <sem@altlinux.org> 0.9.9.0-alt1.git20140205
- Add 'tui' subpackage.
- Drop --enable-bluez4 configure option.
- Upstream git snapshot (master branch).

* Wed Dec 11 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.8-alt4
- Fix 'Obsoletes' tags (closes: #29535).
- Support build with bluez5.
- Patches from upstream git:
  + agents: fix crash in nm_secret_agent_cancel_secrets() (rh #922855).
  + agents: fix removing requests from hash table while iterating it.

* Wed Nov 20 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.8-alt3
- Fix path to the dhcpcd pid file.
- Patches from upstream git:
  + dispatcher: fix crash while logging from signal handler.
  + core: fix segfault in NMAgentManager (rh #1031196).
  + dhcp: print a warning when we can't get DHCP lease.

* Wed Oct 30 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.8-alt2
- Move all development documentation to the devel-doc subpackage.
- Split NetworkManager-glib-devel too.
- Split NetworkManager-glib subpackage (by zerg@) (closes: #29535).

* Mon Oct 14 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.8-alt1
- Updated to 0.9.8.8.

* Tue Sep 24 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt2
- Patches from upstream git:
  + updated Japanese (ja) translation.
  + do not call functions with connection==NULL.
- Don't remove addresses already assigned to the interface.
- Don't package 70-vendor-encap hook.
- Don't reload DBUS configuration during install.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.4-alt1
- etcnet-alt: Add AP mode support for wpa_supplicant.
- Updated to 0.9.8.4.

* Mon Jul 15 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.2-alt4.git20130711
- Add trigger for NetworkManager-dispatcher.service.
- Enable/disable NetworkManager-dispatcher.service too.
- Upstream git snapshot (nm-0-9-8 branch).

* Thu Jul 04 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.2-alt3
- Change group name 'nmconnect' to '_nmconnect'.

* Wed Jul 03 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.2-alt2
- Allow to use connections of 'nmconnect' group's members.

* Tue Jun 11 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.2-alt1
- dbus: allow talking to the NetworkManager-sstp VPN plugin.
- Updated to 0.9.8.2.

* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt5.git20130327
- Allow talking to the NetworkManager-l2tp VPN plugin.
- Use systemctl preset.
- Upstream git snapshot (nm-0-9-8 branch).

* Thu Mar 07 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt4
- Require openresolv-dnsmasq.
- dnsmasq-manager: Updated resolvconf-related code.

* Wed Mar 06 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt3
- Added NetworkManager-prestart script.
- initscript: Fix ModemManager stopping.
- Patches from upstream:
  + fix a crash in 'nmcli d l'.
  + plug some memory leaks.

* Mon Feb 25 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt2
- Enable build with ModemManager-0.7.x.
- etcnet-alt: Fix connections uuid.

* Thu Feb 21 2013 Mikhail Efremov <sem@altlinux.org> 0.9.8.0-alt1
- Updated to 0.9.8.0.

* Wed Feb 13 2013 Mikhail Efremov <sem@altlinux.org> 0.9.7.997-alt1
- Updated ALT support.
- etcnet-alt: Remove trailing whitespace from NM_CONTROLLED value.
- Remove ALT backend.
- Drop support of reading WPA_DRIVER from etcnet.
- Updated to 0.9.7.997 (0.9.8-beta2).

* Wed Nov 28 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.0-alt2
- Require nm-dhcp-client.
- Build with both dhcpcd and dhclient support.
- etcnet-alt: Add test for IPv6 configuration.
- etcnet-alt: Implement IPv6 support.

* Wed Aug 08 2012 Mikhail Efremov <sem@altlinux.org> 0.9.6.0-alt1
- Updated to 0.9.6.0.

* Tue Jul 03 2012 Mikhail Efremov <sem@altlinux.org> 0.9.5.95-alt1
- Treat warrnings as errors again.
- Updated from upstream git (18b0ba499c).
- Updated to 0.9.5.95 (0.9.6-rc1).

* Mon May 21 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt3
- Use libsystemd-login if systemd support is enabled (closes: #27339).
- atcnet-alt: Fix test's DSO linking.
- sysconfig: Fix comment.
- Drop systemd handling from spec.

* Thu Apr 12 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt2
- Disable wimax support.
- Updated from upstream git (21bc3ab517):
  + wifi: check the driver reports any encryption caps with nl80211
    (bgo #673717).
  + Fix a few misc issues noticed by Coverity.

* Thu Apr 05 2012 Mikhail Efremov <sem@altlinux.org> 0.9.4.0-alt1
- Updated from upstream git (6a1208b526).
- 0.9.4.0.

* Wed Mar 28 2012 Mikhail Efremov <sem@altlinux.org> 0.9.3.995-alt1.git20120315
- Temporary don't treat warrnings as errors.
- initscript: Pass --nocheck to the nmcli.
- etcnet-alt: Updated according with upstream changes.
- alt backend: Updated and cleanup according with upstream changes.
- upstream git snapshot (master branch).

* Thu Mar 01 2012 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt3
- Don't try to unmount network filesystems (closes: #27013).

* Thu Feb 16 2012 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt2
- netfs hook: Fix typo in service name (closes: #26947).
- systemd support: Enable service during install (closes: #26586).

* Fri Nov 11 2011 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1
- Rename src.rpm package again.
- 0.9.2 release.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.95-alt1.git20111101
- 0.9.1.95 (0.9.2-rc1).

* Tue Sep 20 2011 Mikhail Efremov <sem@altlinux.org> 0.9.1.90-alt1.git20110920
- upstream git snapshot (master branch).

* Wed Aug 24 2011 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1
- 0.9.0 release.

* Tue Jun 07 2011 Mikhail Efremov <sem@altlinux.org> 0.8.9997-alt1.git20110607
- etcnet-alt: Fix adding/removal devices handling.
- Drop fix for env path in python scripts (fixed in upstream).
- upstream git snapshot (master branch) (closes: #21834).

* Fri May 27 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt3.git20110510
- Rename src.rpm package.

* Wed May 11 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt2.git20110510
- Package NetworkManager-wait-online.service file.
- From upstream git:
    + systemd: tweak NM-wait-online.service.
- Try to reconnect when cable is plugged.

* Tue May 10 2011 Mikhail Efremov <sem@altlinux.org> 0.8.999-alt1.git20110510
- etcnet-alt:
    + Added more tests.
    + Handle MAC from iplink file.
    + Handle route metric.
    + Honor current etcnet network profile (closes: #18435).
    + Various fixes.
    + Allow tab as tokens delimiter.
    + add tests for wired configuration.
    + Allow several IPv4 addresses and routes.
    + Don't send signals if it is unnecessary.
- Add 80-etcnet-post dispatcher script.
- Add 30-efw dispatcher script (closes: #21834).
- Suppress annoying messages.
- init script: Use the new Sleep() method.
- init script: Disconnect all ifaces on stop.
- ntpd hook: Don't create garbage in /tmp.
- Set cp1251 as prefered encoding for Cyrillic langs (closes: #25404).
- Handle write result in signals handler.
- Move nm-version.h to devel subpackage.
- Fix work with dnsmasq-2.57.
- Enable gobject-introspection (by aris@).
- upstream git snapshot (master branch).

* Wed Mar 23 2011 Mikhail Efremov <sem@altlinux.org> 0.8.997-alt1.git20110323
- Workaround for upgrade: remove old timestamps directory.
- etcnet-alt: Drop obsoleted timestamps handling.
- Don't use dns plugins with resolvconf support.
- etcnet-alt: cosmetic cleanup.
- etcnet-alt: Don't send signals if it is unnecessary.
- etcnet-alt: Update connections for device on dir creation.
- Disable remote settings client test.
- Fix env path in tests/examples.
- etcnet-alt: Updated for NM-0.9.
- upstream git snapshot (master branch).

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt3.git20101126
- Enable systemd support (closes: #25118).
- Minor spec cleanup.

* Fri Nov 26 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101126
- etcnet-alt: minor fixes.
- etcnet-alt: Use timestamps for connections.
- etcnet-alt: Fix ONBOOT option handling.
- sysconfig: Set NM_DOWN_CONTROLLED to 'yes' by default again.
- init script: Not start NM if networking is disabled..
- Rewrite and rename 10-mount -> 10-netfs.
- Drop Packager from spec.
- upstream git snapshot (master branch).

* Thu Nov 11 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt2.git20101106
- Ensure that dhcp client is exited before start an another one.
- Fix source tarball and general patch packaging.
- Add /etc/sysconfig/NetworkManager config.
- Enable tests.
- test-keyfile: drop dbus stuff.

* Sat Nov 06 2010 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20101106
- drop alt-set-iwconfig-essid.patch.
- upstream git snapshot
    (almost corresponds with 0.8.2 release, but builded from master branch).

* Tue Sep 21 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt3.git20100914
- add 20-hostname dispatcher script
    (Call update_chrooted when hostname is changed).
- Don't lost hostnames mapped to 127.0.0.1 and ::1.

* Tue Sep 14 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100914
- add versioned dependency on NetworkManager-glib.
- upstream git snapshot (master branch).

* Thu Jul 22 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100722
- spec cleanup
- upstream git snapshot
    (almost corresponds with 0.8.1 release, but builded from master branch).

* Wed Jun 30 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2.git20100628
- Allow sending sleep/wake signals for clients in active sessions (tnx shrek@)

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1.git20100628
- NetworkManager.conf: Explicitly specify dhcpcd as DHCP client.
- upstream git snapshot (master branch).

* Fri May 28 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt2.git20100525
- etcnet-alt: fix connectons export.

* Tue May 25 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0.997-alt1.git20100525
- Not ignore modems with 'bluetooth' driver
- upstream git snapshot
- Move checking for the X server presence to _set_hostname().

* Thu Apr 29 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt3.git20100427
- fix self-inheritance of NMDHCPDhcpcd.
- rename nm-system-settings.conf -> NetworkManager.conf.
- add etcnet-alt description to man page.
- upstream git snapshot

* Fri Mar 12 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt2
- fix X server finding while changing hostname.

* Sat Feb 27 2010 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1
- 0.8.0 release

* Thu Feb 04 2010 Mikhail Efremov <sem@altlinux.org> 0.7.999-alt1.git20100204
- package docs/spec.html.
- Don't package ChangeLog.
- upstream git snapshot

* Wed Jan 13 2010 Mikhail Efremov <sem@altlinux.org> 0.7.998-alt2
- build with pppd 2.4.5.

* Sat Jan 09 2010 Mikhail Efremov <sem@altlinux.org> 0.7.998-alt1
- 0.7.998 (0.8-rc2)

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 0.7.997-alt1.git20091209
- upstream git snapshot

* Tue Dec 01 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt3.git20091124
- etcnet-alt: allow connections without default gateway.
- init script: change pidfile path.
- fix localstatedir path.

* Tue Nov 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt2.git20091124
- init script: killall nm-system-settings again.
- upstream git snapshot

* Mon Nov 09 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt2.git20091026
- fix cooperation between dnsmasq and resolvconf.
- etcnet-alt: bind mac address to connections.

* Wed Oct 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.996-alt1.git20091026
- Don't create default wired connection.
- init script: remove haldaemon reqiures.
- init script: remove killall system-setting.
- etcnet-alt plugin updated.
- 0.7.996 (upstream git snapshot)

* Wed Oct 21 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1.997-alt1
- 0.7.1.997 (0.7.2-rc3)

* Mon Oct 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt9.git20091005
- Build libnm-util docs again.
- kill usage of sha1 according with upstream changes.
- upstream git snapshot (NETWORKMANAGER_0_7 branch)

* Sun Aug 23 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt9.git20090716
- init script: taking down devices before NM start.
- libnm-util: fix setting wireless security.
- etcnet-alt: fixed proto WPA2 from wpa_supplicant.conf.

* Thu Aug 20 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt8.git20090716
- Don't write resolv.conf if resolvconf failed.

* Thu Jul 16 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt7.git20090716
- upstream git snapshot (NETWORKMANAGER_0_7 branch)
- added 10-mount dispatcher script

* Mon Jul 06 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt6
- build with libudev.
- etcnet-alt: fixed build without libgio.
- fixed exit status of 70-vendor-encap.

* Tue Jun 30 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt5
- cherry-picked from upstream git:
	+ wifi: don't bring device up if it's rfkilled.
	+ serial: use termios for better compatibility (rh #464760).
- added 70-vendor-encap dispatcher script.

* Wed May 13 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt4
- from upstream git:
  dns: fix handling of searches and domains in resolv.conf

* Tue Apr 28 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt3
- ignore interface if 'options' file present and NM_CONTROLLED
  not set.

* Tue Apr 21 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt2
- Remove 'invalid' tag from connections when cable was unplugged
  and plugged again.

* Wed Apr 15 2009 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Release 0.7.1

* Mon Apr 13 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt5
- etcnet-alt: fixed handling multiple networks from
  wpa_supplicant.conf.
- added 'sleep' and 'wake' init script commands.

* Fri Apr 10 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt4
- etcnet-alt: don't return secrets in the GetSettings handler
- build development documentation

* Thu Apr 09 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt3
- Set hostname if no X server present.
- etcnet-alt plugin: implement 'get hostname' property.
- use 'action' for sysctl in init script.
- use '--persist' nm-dispatcher option.
- avoid nm-dispatcher error message.

* Tue Apr 07 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt2
- use own dispatcher script for ntpd

* Mon Apr 06 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.100-alt1
- 0.7.0.100 (0.7.1-rc4)

* Fri Apr 03 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt7
- call dhcpcd hook for ntpd

* Tue Mar 24 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt6
- use /etc/net/ifaces/default for creating connections 
	even if /etc/net/ifaces/<iface> not exists.

* Mon Mar 23 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt5
- Fix possible crash when resynchronizing devices if HAL restarts
	(from upstream git)

* Tue Mar 17 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt4
- update-chrooted dispatcher script is removed

* Tue Mar 17 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt3
- enable resolvconf support
- don't backup resolv.conf anymore

* Fri Mar 13 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt2
- init script start/stop priority changed from '40 90' to '12 90'
	(close ALT bug #19002)

* Thu Mar 05 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.99-alt1
- 0.7.0.99 (0.7.1-rc3)

* Thu Feb 26 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.98-alt1
- 0.7.0.98 (0.7.1-rc2)
- pack source as tar instead tar.gz.

* Thu Feb 19 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0.97-alt1
- 0.7.0.97 (0.7.1-rc1)
- spec cleanup
- fix keyfile plugin test build.

* Fri Feb 13 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt19
- also monitoring /etc/net/ifaces/ directory.
- fix segfault when file is deleted from /etc/net/ifaces/*/.

* Mon Jan 26 2009 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt18
- use dhcpcd 4 

* Tue Dec 30 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt17
- enable debug message again
- not check frequency matching

* Fri Dec 26 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt16
- alt-set-iwconfig-essid.patch update.
- nm-device-wifi.c: disable debug message.

* Tue Dec 23 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt15
- alt-set-iwconfig-essid.patch updated.
- init script start/stop priority changed from '98 02' to '40 90'.

* Fri Dec 19 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt14
- save/restore resolv.conf
- some fixes in etcnet-alt plugin (close ALT bug #16736, etc)

* Mon Dec 15 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt13
- create /etc/NetworkManager/system-connections directory.
- kill nm-system-settings when service stop.

* Fri Dec 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt12
- enable keyfile plugin
- fix segmentation fault in keyfile plugin
- fix reading routes

* Mon Dec 08 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt11
- remove NetworkManager-devel -> NetworkManager requires(close #18129)
- alt-dhcp-client-pid.patch is added (close #18021).
- remove device from hash table before sending signal.
- src/nm-netlink-monitor.c: fix function call.

* Wed Dec 03 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt10
- Release NetworkManager 0.7

* Wed Nov 26 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt9.svn.r4326
- don't create default connection in nm-system-settings daemon 
	(nm-applet do it)

* Tue Nov 25 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt8.svn.r4326
- dnsmasq requires is added

* Mon Nov 24 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt7.svn.r4326
- new svn snapshot
- etcnet-alt plugin updated according to upstream code changes
- fix WEP keys reading

* Fri Nov 21 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt7.svn.r4229
- ldconfig removed (obsolete)
- don't restart service when upgrade (close #17275)
- etcnet-alt plugin can read wireless settings 
	from wpa_supplicant.conf (WPA and WEP)

* Wed Nov 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt6.svn.r4229
- fix zombies bug

* Wed Nov 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt5.svn.r4229
- new svn snapshot
- NetworkManager-0.7.0-alt-no-strict-aliasing.patch,
  NetworkManager-0.7.0-alt-no_check_dhclient.patch and
  NetworkManager-0.7.0-alt-supplicant_interface.patch
	removed (obsolete)
- alt-set-iwconfig-essid.patch	
	(dirty patch for set essid when connecting to wireless networks)
- alt-no-update-hostname.patch
- update-chrooted dispatcher script is added
- fix preun
- ppp-pppoe requires is added

* Mon Oct 27 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt5.svn.r4209
- new svn revision 

* Thu Oct 02 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7.0-alt5.svn.r3930
- expiremental patch for not exposyng system connections to user
- expiremental dirty patch to not set DISCONNECTED state when there are routes 

* Tue Aug 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt4.svn.r3930
- new svn snapshot
- %post updated (D-Bus config reload; add %post_service)

* Wed Aug 06 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt4.svn20080722
- spec cleanup
- split NetworkManager-glib on NetworkManager-glib and NetworkManager-glib-devel
- NetworkManager-0.7.0-alt-kill_supplicant.patch is added
	(not kill all wpa_supplicant, only for managed interfaces)
- NetworkManager-0.7.0-alt-supplicant_interface.patch
	(release the interface when NM exit)

* Mon Jul 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.2.svn20080722
- update  NetworkManager-0.7.0-alt-dhcpcd_opt.patch ("-K" option is added)

* Wed Jul 23 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.1.svn20080722
- version for dhcpcd 4

* Tue Jul 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn20080722
- new svn snapshot (3842)
- .la files are not packaged (close #15840)

* Wed May 28 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn20080527
- new svn snapshot (3694)
- nm-system-settings plugin is completely rewritten

* Tue May 13 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt3.svn20080428
- reading "WPA_DRIVER" from "/etc/net/ifaces/<interface>/options" is added

* Mon May 12 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.svn20080428
- killall wpa_supplicant on start
- nm-system-settings plugin update

* Tue Apr 29 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080428
- new svn snapshot (3614)
- dhcpcd-1.3.x -> dhcpcd-3.0.x
- spec cleanup

* Tue Apr 22 2008 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.svn20080419
- initial build

