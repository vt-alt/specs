%def_enable tests
%def_enable dummy

# fwupdate is only available on these arches
%ifarch x86_64 aarch64
%def_enable uefi
%endif

# libsmbios is only available on x86, and fwupdate is available on just x86_64
%ifarch x86_64
%def_enable dell
%endif

Summary: Firmware update daemon
Name: fwupd
Version: 1.3.6
Release: alt1
License: GPLv2+
Group: System/Configuration/Hardware
Url: https://github.com/hughsie/fwupd
Source0: %name-%version.tar
Source2: fwupd.watch
Patch0: %name-%version-alt.patch
ExclusiveArch: %ix86 x86_64 aarch64 ppc64le

BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: glib2-devel
BuildRequires: libappstream-glib-devel
BuildRequires: libjson-glib-devel
BuildRequires: libgudev-devel
BuildRequires: libudev-devel
BuildRequires: libgusb-devel
BuildRequires: libsoup-devel
BuildRequires: libsoup-gir-devel
BuildRequires: libcolord-devel
BuildRequires: libpolkit-devel
BuildRequires: libsqlite3-devel
BuildRequires: libsystemd-devel
BuildRequires: libgpgme-devel
BuildRequires: systemd 
BuildRequires: libumockdev-devel
BuildRequires: gcab
BuildRequires: libarchive-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgcab-devel
BuildRequires: valgrind-devel
BuildRequires: libelf-devel
BuildRequires: gtk-doc
BuildRequires: libuuid-devel
BuildRequires: libgnutls-devel
BuildRequires: gnutls-utils
BuildRequires: meson
BuildRequires: vala-tools
BuildRequires: help2man
BuildRequires: libxmlb-devel
BuildRequires: bash-completion
BuildRequires: libtpm2-tss-devel
BuildRequires: cmake
BuildRequires: libgusb-gir-devel
BuildRequires: python3 python3-module-pycairo python3-module-pygobject3 python3-module-Pillow rpm-build-python3

%if_enabled dell
BuildRequires: libsmbios-devel
%endif

%if_enabled tests
BuildRequires: /proc
%endif

%if_enabled uefi
BuildRequires: libpango-devel
BuildRequires: libcairo-devel libcairo-gobject-devel
BuildRequires: libfreetype-devel
BuildRequires: fontconfig
BuildRequires: fonts-ttf-dejavu
BuildRequires: gnu-efi libefivar-devel
Requires: gcab
Provides: fwupdate
Obsoletes: fwupdate
%endif

Requires: fwupd-labels = %EVR
Requires: bubblewrap

%description
fwupd is a daemon to allow session software to update device firmware.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Files for development with %name.

%package labels
Group: System/Configuration/Hardware
Summary: Rendered labels for display during system firmware updates
# RedHat: BuildArch: noarch is disabled as we can get "different" .BMP files even when
# running the build on the same architecture due to the randomness introduced
# by the TTF files.

%description labels
Rendered labels for display during system firmware updates.

%package tests
Group: System/Configuration/Hardware
Summary: Data files for installed tests
BuildArch: noarch

%description tests
Data files for installed tests.

%prep
%setup
%patch0 -p1

%build
%meson \
    -Dgtkdoc=true \
    -Dfirmware-packager=true \
    -Dman=false \
    -Dlvfs=true \
    -Dplugin_flashrom=false \
%if_enabled tests
    -Dtests=true \
%else
    -Dtests=false \
%endif
%if_enabled dummy
    -Dplugin_dummy=true \
%else
    -Dplugin_dummy=false \
%endif
    -Dplugin_thunderbolt=true \
%if_enabled uefi
    -Dplugin_uefi=true \
    -Dplugin_redfish=true \
    -Dplugin_nvme=true \
%else
    -Dplugin_uefi=false \
    -Dplugin_redfish=false \
    -Dplugin_nvme=false \
%endif
%if_enabled dell
    -Dplugin_dell=true \
    -Dplugin_synaptics=true \
%else
    -Dplugin_dell=false \
    -Dplugin_synaptics=false \
%endif

%meson_build

%if_enabled tests
%check
export LD_LIBRARY_PATH=%buildroot%_libdir 
%meson_test
%endif

%install
%meson_install

mkdir -p --mode=0700 %buildroot%_localstatedir/fwupd/gnupg

%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS COPYING
%config(noreplace)%_sysconfdir/fwupd/daemon.conf
%config(noreplace)%_sysconfdir/fwupd/thunderbolt.conf
%dir %_libexecdir/fwupd
%dir %_iconsdir/hicolor/scalable/apps
%_libexecdir/fwupd/fwupd
%_libexecdir/fwupd/fwupdtool
%_libexecdir/fwupd/fwupdagent
%_libexecdir/fwupd/fwupdoffline
%_libexecdir/fwupd/fwupdtpmevlog
%_datadir/bash-completion/completions/*
%_iconsdir/hicolor/scalable/apps/org.freedesktop.fwupd.svg
%if_enabled uefi
%_libexecdir/fwupd/fwupdate
%_libdir/efi/fwupd*.efi
%endif
%_bindir/dfu-tool
%_bindir/fwupdmgr
%dir %_sysconfdir/fwupd
%dir %_sysconfdir/fwupd/remotes.d
%config(noreplace)%_sysconfdir/fwupd/remotes.d/*.conf
%_sysconfdir/pki/fwupd
%_sysconfdir/pki/fwupd-metadata
%_datadir/dbus-1/system.d/org.freedesktop.fwupd.conf
%ifarch x86_64
%_datadir/fwupd/remotes.d/dell-esrt/metadata.xml
%endif
%_datadir/fwupd/remotes.d/vendor/firmware
%_datadir/dbus-1/interfaces/org.freedesktop.fwupd.xml
%_datadir/polkit-1/actions/org.freedesktop.fwupd.policy
%_datadir/polkit-1/rules.d/org.freedesktop.fwupd.rules
%_datadir/dbus-1/system-services/org.freedesktop.fwupd.service
%_datadir/metainfo/org.freedesktop.fwupd.metainfo.xml
%_datadir/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs-testing.metainfo.xml
%_datadir/fwupd/metainfo/org.freedesktop.fwupd.remotes.lvfs.metainfo.xml
%_datadir/fwupd/firmware_packager.py
%_datadir/fwupd/add_capsule_header.py
%_datadir/fwupd/install_dell_bios_exe.py
%_datadir/fwupd/simple_client.py
%_presetdir/fwupd-refresh.preset
%_unitdir/fwupd-offline-update.service
%_unitdir/fwupd.service
%_unitdir/fwupd-refresh.timer
%_unitdir/fwupd-refresh.service
%_unitdir/system-update.target.wants/
/lib/systemd/system-shutdown/fwupd.shutdown
%dir %_localstatedir/fwupd
%dir %_datadir/fwupd/quirks.d
%dir %_localstatedir/fwupd/builder
%_localstatedir/fwupd/builder/README.md
%_datadir/fwupd/quirks.d/*.quirk
%_libdir/libfwupd*.so.*
%_libdir/girepository-1.0/Fwupd-2.0.typelib
%_libdir/girepository-1.0/FwupdPlugin-1.0.typelib
/lib/udev/rules.d/*.rules
%dir %_libdir/fwupd-plugins-3
%_libdir/fwupd-plugins-3/libfu_plugin_altos.so
%_libdir/fwupd-plugins-3/libfu_plugin_ata.so
%_libdir/fwupd-plugins-3/libfu_plugin_csr.so
%_libdir/fwupd-plugins-3/libfu_plugin_amt.so
%_libdir/fwupd-plugins-3/libfu_plugin_emmc.so
%_libdir/fwupd-plugins-3/libfu_plugin_colorhug.so
%_libdir/fwupd-plugins-3/libfu_plugin_coreboot.so
%if_enabled dell
%_libdir/fwupd-plugins-3/libfu_plugin_dell.so
%_libdir/fwupd-plugins-3/libfu_plugin_dell_esrt.so
%endif
%_libdir/fwupd-plugins-3/libfu_plugin_dell_dock.so
%_libdir/fwupd-plugins-3/libfu_plugin_dfu.so
%_libdir/fwupd-plugins-3/libfu_plugin_ebitdo.so
%_libdir/fwupd-plugins-3/libfu_plugin_tpm.so
%_libdir/fwupd-plugins-3/libfu_plugin_tpm_eventlog.so
%_libdir/fwupd-plugins-3/libfu_plugin_fastboot.so
%_libdir/fwupd-plugins-3/libfu_plugin_nitrokey.so
%_libdir/fwupd-plugins-3/libfu_plugin_rts54hid.so
%_libdir/fwupd-plugins-3/libfu_plugin_rts54hub.so
%_libdir/fwupd-plugins-3/libfu_plugin_superio.so
%_libdir/fwupd-plugins-3/libfu_plugin_solokey.so
%_libdir/fwupd-plugins-3/libfu_plugin_steelseries.so
%_libdir/fwupd-plugins-3/libfu_plugin_jabra.so
%_libdir/fwupd-plugins-3/libfu_plugin_optionrom.so
%_libdir/fwupd-plugins-3/libfu_plugin_synaptics_rmi.so
%_libdir/fwupd-plugins-3/libfu_plugin_vli_usbhub.so
%_libdir/fwupd-plugins-3/libfu_plugin_synaptics_cxaudio.so
%_libdir/fwupd-plugins-3/libfu_plugin_logitech_hidpp.so
%_libdir/fwupd-plugins-3/libfu_plugin_synaptics_prometheus.so
%if_enabled dell
%_libdir/fwupd-plugins-3/libfu_plugin_synaptics_mst.so
%endif
%if_enabled dummy
%_libdir/fwupd-plugins-3/libfu_plugin_invalid.so
%_libdir/fwupd-plugins-3/libfu_plugin_test.so
%endif
%_libdir/fwupd-plugins-3/libfu_plugin_thelio_io.so
%_libdir/fwupd-plugins-3/libfu_plugin_thunderbolt.so
%_libdir/fwupd-plugins-3/libfu_plugin_thunderbolt_power.so
%if_enabled uefi
%_libdir/fwupd-plugins-3/libfu_plugin_nvme.so
%_libdir/fwupd-plugins-3/libfu_plugin_uefi.so
%_libdir/fwupd-plugins-3/libfu_plugin_uefi_recovery.so
%_libdir/fwupd-plugins-3/libfu_plugin_redfish.so
%config(noreplace)%_sysconfdir/fwupd/uefi.conf
%config(noreplace)%_sysconfdir/fwupd/redfish.conf
%endif
%_libdir/fwupd-plugins-3/libfu_plugin_upower.so
%_libdir/fwupd-plugins-3/libfu_plugin_wacom_usb.so
%_libdir/fwupd-plugins-3/libfu_plugin_wacom_raw.so

%ghost %_localstatedir/fwupd/gnupg

%files devel
%_datadir/gir-1.0/Fwupd-2.0.gir
%_datadir/gir-1.0/FwupdPlugin-1.0.gir
%_datadir/gtk-doc/html/fwupd
%_includedir/fwupd-1
%_libdir/libfwupd*.so
%_libdir/pkgconfig/fwupd.pc
%_libdir/pkgconfig/fwupdplugin.pc
%_datadir/vala/vapi/fwupd.*
%_datadir/vala/vapi/fwupdplugin.*

%files labels
%if_enabled uefi
%_datadir/locale/*/LC_IMAGES/fwupd*
%endif

%files tests
%dir %_datadir/installed-tests/fwupd
%_datadir/installed-tests/fwupd/fwupd-tests.xml
%_datadir/installed-tests/fwupd/*.test
%_datadir/installed-tests/fwupd/*.cab
%_datadir/installed-tests/fwupd/*.sh
%_datadir/installed-tests/fwupd/*.py*

%changelog
* Fri Jan 10 2020 Anton Farygin <rider@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Fri Dec 27 2019 Anton Farygin <rider@altlinux.ru> 1.3.5-alt2
- added gcab to requires list (used in firmware_packager.py)

* Mon Dec 02 2019 Anton Farygin <rider@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Mon Nov 25 2019 Anton Farygin <rider@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Tue Nov 19 2019 Anton Farygin <rider@altlinux.ru> 1.3.3-alt2
- fixed work with EFI secure boot (closes: #37486)

* Thu Nov 07 2019 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- 1.3.3
- enabled tests

* Mon Sep 30 2019 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Mon Sep 16 2019 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.2.10-alt1
- 1.2.10

* Mon Jul 15 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.9-alt2
- Added ppc64le to ExclusiveArch tag.

* Fri May 24 2019 Anton Farygin <rider@altlinux.ru> 1.2.9-alt1
- 1.2.9

* Thu Apr 25 2019 Anton Farygin <rider@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Tue Apr 16 2019 Anton Farygin <rider@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Mon Apr 01 2019 Anton Farygin <rider@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Wed Mar 06 2019 Anton Farygin <rider@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Mon Feb 11 2019 Anton Farygin <rider@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Mon Jan 07 2019 Anton Farygin <rider@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Mon Dec 03 2018 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Mon Nov 12 2018 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Wed Oct 17 2018 Anton Farygin <rider@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Mon Sep 03 2018 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Tue Jul 31 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri May 04 2018 Anton Farygin <rider@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Thu Mar 22 2018 Anton Farygin <rider@altlinux.ru> 1.0.6-alt1
- new version
- temporarily disabled check section due to impossible testing of the thunderbolt interface in the hasher environment

* Wed Mar 07 2018 Anton Farygin <rider@altlinux.ru> 1.0.5-alt1
- first build for ALT, based on RH spec

