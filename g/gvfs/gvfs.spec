%def_enable snapshot

%define ver_major 1.40

%def_disable gdu
%def_disable gtk_doc
# obexftp support removed since 3.15.91
%def_disable obexftp
%def_enable afc
%def_enable afp
%def_enable archive
%def_enable avahi
%def_enable bluray
%def_enable cdda
%def_enable fuse
%def_enable gcr
%def_enable goa
%def_enable gphoto2
%def_enable http
%def_enable installed_tests
%def_enable keyring
%def_enable libmtp
%def_enable nfs
%def_enable samba
%def_enable systemd_login
%def_enable udisks2
%def_enable google
%def_enable admin
%def_enable libusb
%def_enable dnssd
%def_enable man
%def_disable check

Name: gvfs
Version: %ver_major.2
Release: alt1

Summary: The GNOME virtual filesystem libraries
License: %lgpl2plus
Group: System/Libraries
Url: https://wiki.gnome.org/Projects/gvfs

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
# https://bugzilla.altlinux.org/show_bug.cgi?id=29047
# https://bugzilla.altlinux.org/show_bug.cgi?id=29171
# https://mail.gnome.org/archives/gvfs-list/2013-May/msg00014.html
Patch1: gvfs-1.19.90-alt-1-logind-state.patch

%{?_enable_gdu:Obsoletes: gnome-mount <= 0.8}
%{?_enable_gdu:Obsoletes: gnome-mount-nautilus-properties <= 0.8}

# obsolete by %_bindir/gio from libgio
Obsoletes: %name-utils < 1.31
Obsoletes: bash-completion-gvfs < 1.31

%define glib_ver 2.57.2
%define libsoup_ver 2.42
%define avahi_ver 0.6
%define libcdio_paranoia_ver 10.2
%define bluez_ver 4.0
%define gdu_ver 3.3.91
%define udisks_ver 1.99
%define mtp_ver 1.1.5
%define goa_ver 3.17.1
%define libarchive_ver 3.0.22
%define imobiledevice_ver 1.1.5
%define nfs_ver 1.9.7
%define gdata_ver 0.17.3
%define libusb_ver 1.0.21

Requires: dconf
%{?_enable_fuse:Requires: fuse-gvfs}
%{?_enable_gdu:Requires: gnome-disk-utility >= %gdu_ver}
%{?_enable_udisks2:Requires: udisks2}

BuildRequires(pre): meson rpm-build-gnome rpm-build-licenses

BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libdbus-devel gtk-doc
BuildRequires: openssh-clients
# hotplug backend
BuildRequires: libgudev-devel
# required if autoreconf used
BuildRequires: libgcrypt-devel
%{?_enable_afc:BuildPreReq: libimobiledevice-devel >= %imobiledevice_ver}
%{?_enable_afp:BuildPreReq: libgcrypt-devel}
%{?_enable_archive:BuildPreReq: libarchive-devel >= %libarchive_ver}
%{?_enable_dnssd:BuildPreReq: libavahi-glib-devel >= %avahi_ver libavahi-devel >= %avahi_ver}
%{?_enable_bluray:BuildRequires: libbluray-devel}
%{?_enable_cdda:BuildPreReq: libcdio-paranoia-devel >= %libcdio_paranoia_ver}
%{?_enable_fuse:BuildPreReq: libfuse-devel}
%{?_enable_gcr:BuildRequires: gcr-libs-devel}
%{?_enable_gdu:BuildPreReq: libgdu-devel >= %gdu_ver libgudev-devel}
%{?_enable_goa:BuildPreReq: libgnome-online-accounts-devel >= %goa_ver}
%{?_enable_gphoto2:BuildPreReq: libgphoto2-devel}
%{?_enable_http:BuildPreReq: libsoup-devel >= %libsoup_ver libxml2-devel}
%{?_enable_keyring:BuildPreReq: libsecret-devel}
%{?_enable_libmtp:BuildPreReq: libmtp-devel >= %mtp_ver}
%{?_enable_nfs:BuildPreReq: libnfs-devel >= %nfs_ver}
%{?_enable_obexftp:BuildPreReq: libbluez-devel >= %bluez_ver libdbus-glib-devel libexpat-devel}
%{?_enable_samba:BuildPreReq: libsmbclient-devel}
%{?_enable_systemd_login:BuildPreReq: libsystemd-devel}
%{?_enable_udisks2:BuildPreReq: libudisks2-devel >= %udisks_ver}
%{?_enable_google:BuildPreReq: libgdata-devel >= %gdata_ver}
%{?_enable_admin:BuildRequires: libpolkit-devel libcap-devel}
%{?_enable_libusb:BuildRequires: libusb-devel >= %libusb_ver}

BuildPreReq: desktop-file-utils
BuildRequires: gcc-c++ perl-XML-Parser

# for check
#BuildRequires: /proc dbus-tools-gui python3 python3-module-pygobject3 python-module-twisted-core
#BuildRequires:  openssh-server apache2 samba genisoimage
# and more

%package devel
Summary: Libraries and include files for developing gvfs applications
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name = %version-%release

%package -n fuse-%name
Summary: gvfs fuse gateway
Group: System/Kernel and hardware
Requires: %name = %version-%release
Requires: %{get_dep fuse}

%package backend-smb
Summary: Samba backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release
Requires: samba-client

%package backend-obexftp
Summary: Obexftp backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-dnssd
Summary: Dnssd(avahi) backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-cdda
Summary: Music CD-ROM backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-afc
Summary: i{Phone,Pod} backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-afp
Summary: Apple Filing Protocol backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-recent-files
Summary: Recent files backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-goa
Summary: gnome-online-accounts backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release
Requires: gnome-online-accounts

%package backend-mtp
Summary: MTP support for gvfs
Group: System/Libraries
Requires: %name = %version-%release

%package backend-nfs
Summary: NFS backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release
Requires: nfs-clients
Requires(post): libcap-utils

%package backend-google
Summary: Google drive backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release
Requires: gnome-online-accounts

%package backend-admin
Summary: Admin backend for gvfs
Group: System/Libraries
Requires: %name = %version-%release
Requires: polkit

%package backends
Summary: All backends for gvfs
Group: System/Libraries
BuildArch: noarch
Requires: gvfs gvfs-backend-smb gvfs-backend-dnssd
Requires: gvfs-backend-recent-files
%{?_enable_cdda:Requires: gvfs-backend-cdda}
%{?_enable_obexftp:Requires: gvfs-backend-obexftp}
%{?_enable_afc:Requires: gvfs-backend-afc}
%{?_enable_afp:Requires: gvfs-backend-afp}
%{?_enable_goa:Requires: gvfs-backend-goa}
%{?_enable_libmtp:Requires: gvfs-backend-mtp}
%{?_enable_nfs:Requires: gvfs-backend-nfs}
%{?_enable_google:Requires: gvfs-backend-google}
%{?_enable_admin:Requires: gvfs-backend-admin}

%description
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via dbus. It also contains a gio module that
seamlessly adds gvfs support to all applications using the gio API. It also
supports exposing the gvfs mounts to non-gio applications using fuse.

This package contains the gvfs server, libgvfscommon library, gio
modules and backends for gvfs: archive, burn, computer, dav, ftp,
gphoto2, http, localtest, network, sftp and trash.

%description devel
gvfs is a userspace virtual filesystem where mount runs as a separate
processes which you talk to via dbus. It also contains a gio module that
seamlessly adds gvfs support to all applications using the gio API. It also
supports exposing the gvfs mounts to non-gio applications using fuse.

This package contains the libgvfscommon development files.

%description -n fuse-%name
fuse-gvfs is a bridge between the gvfs filesystem design and fuse, a
program to mount user-space filesystems.

%description backend-smb
This package contains the smb and smb-browse backends for gvfs.

%description backend-obexftp
This package contains the obexftp backend for gvfs.

%description backend-dnssd
This package contains the dnssd backend for gvfs.

%description backend-cdda
This package contains the cdda backend for gvfs.

%description backend-afc
This package contains a backend for gvfs, providing access to Apple's
iPhone, and iPod Touch devices.

%description backend-afp
This package contains a backend for gvfs, providing access to Apple
Mac OS X filesystem by AFP (Apple Filing Protocol) network protocol.

%description backend-recent-files
This package contains recent files backend for gvfs.

%description backend-goa
This package contains gnome-online-accounts backend for gvfs.

%description backend-mtp
This package provides support for reading and writing files on MTP based
devices (Media Transfer Protocol) to applications using gvfs.

%description backend-nfs
This package provides support for mounting NFS shares using gvfs.

%description backend-google
This package provides support for mounting google drive using gvfs.

%description backend-admin
This package provides admin backend for gvfs based on polkit.

%description backends
This virtual package contains the all backends for gvfs.

%package tests
Summary: GVFS test programms
Group: Development/GNOME and GTK+
BuildArch: noarch
Requires: %name-backends = %version-%release fuse-%name

%description tests
The %name-tests package provides programms for testing GVFS.

%define _libexecdir %_prefix/libexec/%name

%prep
%setup
#%%patch1 -p2 -b .logind-state

%build
%meson \
        %{?_enable_http:-Dhttp=true} \
        %{?_enable_dnssd:-Ddnssd=true} \
        %{?_enable_cdda:-Dcdda=true} \
        %{?_enable_fuse:-Dfuse=true} \
        %{?_enable_gphoto2:-Dgphoto2=true} \
        %{?_enable_keyring:-Dkeyring=true} \
        %{?_enable_samba:-Dsmb=true} \
        %{?_enable_archive:-Darchive=true} \
        %{?_enable_afc:-Dafc=true} \
        %{?_enable_afp:-Dafp=true} \
        %{?_enable_gdu:-Dgdu=true} \
        %{?_enable_udisks2:-Dudisks2=true} \
        %{?_enable_libmtp:-Dmtp=true} \
        %{?_enable_bluray:-Dbluray=true} \
        %{?_enable_nfs:-Dnfs=true} \
        %{?_enable_google:-Dgoogle=true} \
        %{?_enable_libusb:-Dlibusb=true} \
        %{?_enable_systemd_login:-Dlogind=true} \
        %{?_enable_gtk_doc:-Dgtk_doc=true} \
        %{?_enable_man:-Dman=true} \
        %{?_enable_installed_tests:-Dinstalled_tests=true}
%meson_build

%install
%meson_install
%find_lang %name

%check
export PATH=/usr/sbin:$PATH
%meson_test

%post
killall -USR1 gvfsd >&/dev/null || :

%post backend-nfs
# for privileged ports
setcap -q cap_net_bind_service=ep %_libexecdir/gvfsd-nfs ||:


%files -f %name.lang
%doc NEWS README* monitor/udisks2/what-is-shown.txt
%dir %_libdir/%name
%_libdir/%name/libgvfs*.so
%dir %_libexecdir
# daemon
%_libexecdir/gvfsd
%config %_datadir/glib-2.0/schemas/org.gnome.system.gvfs.enums.xml
%_prefix/lib/systemd/user/gvfs-daemon.service
%_prefix/lib/systemd/user/gvfs-metadata.service
# monitors
%_libexecdir/gvfs-gphoto2-volume-monitor
%_prefix/lib/systemd/user/gvfs-gphoto2-volume-monitor.service
%{?_enable_gdu:%_libexecdir/gvfs-gdu-volume-monitor}
%{?_enable_udisks2:%_libexecdir/gvfs-udisks2-volume-monitor}
%{?_enable_udisks2:%_prefix/lib/systemd/user/gvfs-udisks2-volume-monitor.service}
%_datadir/dbus-1/services/*
# gio modules
%_libdir/gio/modules/*.so
# default backends
%_libexecdir/gvfsd-*

%exclude %_libexecdir/gvfsd-fuse

%dir %_datadir/%name
%dir %_datadir/%name/remote-volume-monitors
%_datadir/%name/remote-volume-monitors/gphoto2.monitor
%{?_enable_gdu:%_datadir/%name/remote-volume-monitors/gdu.monitor}
%{?_enable_udisks2:%_datadir/%name/remote-volume-monitors/udisks2.monitor}

%_datadir/%name/mounts

%if_enabled man
%_man1dir/gvfsd-fuse.1.*
%_man1dir/gvfsd-metadata.1.*
%_man1dir/gvfsd.1.*
%_man7dir/gvfs.7.*
%endif

# in another packages
%exclude %_libexecdir/gvfsd-recent
%exclude %_datadir/%name/mounts/recent.mount

%if_enabled samba
    %exclude %_libexecdir/gvfsd-smb
    %exclude %_libexecdir/gvfsd-smb-browse
    %exclude %_datadir/%name/mounts/smb.mount
    %exclude %_datadir/%name/mounts/smb-browse.mount
%endif

%{?_enable_cdda:%exclude %_libexecdir/gvfsd-cdda}

%if_enabled obexftp
    %exclude %_libexecdir/gvfsd-obexftp
    %exclude %_datadir/%name/mounts/obexftp.mount
%endif

%if_enabled afc
    %exclude %_libexecdir/gvfsd-afc
    %exclude %_datadir/%name/mounts/afc.mount
%endif

%if_enabled afp
    %exclude %_libexecdir/gvfsd-afp
    %exclude %_libexecdir/gvfsd-afp-browse
    %exclude %_datadir/%name/mounts/afp.mount
    %exclude %_datadir/%name/mounts/afp-browse.mount
%endif

%{?_enable_cdda:%exclude %_datadir/%name/mounts/cdda.mount}
%{?_enable_dnssd:%exclude %_libexecdir/gvfsd-dnssd}
%{?_enable_dnssd:%exclude %_datadir/%name/mounts/dns-sd.mount}

%if_enabled libmtp
    %exclude %_libexecdir/gvfsd-mtp
    %exclude %_datadir/%name/mounts/mtp.mount
    %exclude %_datadir/dbus-1/services/org.gtk.vfs.MTPVolumeMonitor.service
%endif

%if_enabled nfs
    %exclude %_libexecdir/gvfsd-nfs
    %exclude %_datadir/%name/mounts/nfs.mount
%endif

%if_enabled google
    %exclude %_libexecdir/gvfsd-google
    %exclude %_datadir/%name/mounts/google.mount
%endif

%if_enabled admin
    %exclude %_libexecdir/gvfsd-admin
    %exclude %_datadir/%name/mounts/admin.mount
%endif

%files devel
%_includedir/*

%files -n fuse-%name
%_libexecdir/gvfsd-fuse
/lib/tmpfiles.d/gvfsd-fuse-tmpfiles.conf

%files backend-smb
%_libexecdir/gvfsd-smb
%_libexecdir/gvfsd-smb-browse
%_datadir/%name/mounts/smb.mount
%_datadir/%name/mounts/smb-browse.mount
%config %_datadir/glib-2.0/schemas/org.gnome.system.smb.gschema.xml
%_datadir/GConf/gsettings/gvfs-smb.convert

%if_enabled obexftp
%files backend-obexftp
%_libexecdir/gvfsd-obexftp
%_datadir/%name/mounts/obexftp.mount
%endif

%if_enabled dnssd
%files backend-dnssd
%_libexecdir/gvfsd-dnssd
%_datadir/%name/mounts/dns-sd.mount
%config %_datadir/glib-2.0/schemas/org.gnome.system.dns_sd.gschema.xml
%_datadir/GConf/gsettings/gvfs-dns-sd.convert
%endif

%if_enabled cdda
%files backend-cdda
%_libexecdir/gvfsd-cdda
%_datadir/%name/mounts/cdda.mount
%endif

%if_enabled afc
%files backend-afc
%_libexecdir/gvfsd-afc
%_libexecdir/gvfs-afc-volume-monitor
%_datadir/%name/mounts/afc.mount
%_datadir/%name/remote-volume-monitors/afc.monitor
%_prefix/lib/systemd/user/gvfs-afc-volume-monitor.service
%endif

%if_enabled afp
%files backend-afp
%_libexecdir/gvfsd-afp
%_libexecdir/gvfsd-afp-browse
%_datadir/%name/mounts/afp.mount
%_datadir/%name/mounts/afp-browse.mount
%endif

%files backend-recent-files
%_libexecdir/gvfsd-recent
%_datadir/%name/mounts/recent.mount

%if_enabled goa
%files backend-goa
%_libexecdir/%name-goa-volume-monitor
%_datadir/%name/remote-volume-monitors/goa.monitor
%_prefix/lib/systemd/user/gvfs-goa-volume-monitor.service
%endif

%if_enabled libmtp
%files backend-mtp
%_libexecdir/gvfsd-mtp
%_libexecdir/gvfs-mtp-volume-monitor
%_datadir/%name/mounts/mtp.mount
%_datadir/%name/remote-volume-monitors/mtp.monitor
%_datadir/dbus-1/services/org.gtk.vfs.MTPVolumeMonitor.service
%_prefix/lib/systemd/user/gvfs-mtp-volume-monitor.service
%endif

%if_enabled nfs
%files backend-nfs
%_libexecdir/gvfsd-nfs
%_datadir/%name/mounts/nfs.mount
%endif

%if_enabled google
%files backend-google
%_libexecdir/gvfsd-google
%_datadir/%name/mounts/google.mount
%endif

%if_enabled admin
%files backend-admin
%_libexecdir/gvfsd-admin
%_datadir/%name/mounts/admin.mount
%_datadir/polkit-1/actions/org.gtk.vfs.file-operations.policy
%_datadir/polkit-1/rules.d/org.gtk.vfs.file-operations.rules
%endif

%files backends

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/
%_datadir/installed-tests/%name/
%endif


%changelog
* Sun Aug 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.40.2-alt1
- updated to 1.40.2-2-g4fd68eb2 (fixed CVE-2019-12447,
  CVE-2019-12448, CVE-2019-12449, CVE-2019-12795)

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.40.1-alt1.1
- fix man knob (unbuilt manpages can't be packaged)

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.40.1-alt1
- 1.40.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 1.40.0-alt1
- 1.40.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 1.38.2-alt1
- 1.38.2 (fixed CVE-2019-3827)

* Wed Feb 13 2019 Yuri N. Sedunov <aris@altlinux.org> 1.38.1-alt4
- rebuilt against libnfs.so.13

* Wed Jan 16 2019 Yuri N. Sedunov <aris@altlinux.org> 1.38.1-alt3
- updated to 1.38.1-8-ge4eec2bc (fixed GLI ##348, 355)
- disabled obsolete logind-state.patch

* Fri Nov 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.38.1-alt2
- updated to 1.38.1-5-gc5fd1efd

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 1.38.1-alt1
- 1.38.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.38.0-alt1
- 1.38.0

* Sun Jul 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1.36.2-alt3
- rebuilt against libnfs.so.12

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.36.2-alt2
- rebuilt against libbluray.so.2

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1.36.2-alt1
- 1.36.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.36.1-alt1
- 1.36.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 1.36.0-alt1
- 1.36.0

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.34.2.1-alt1
- 1.34.2.1

* Tue Feb 06 2018 Yuri N. Sedunov <aris@altlinux.org> 1.34.2-alt1
- 1.34.2

* Fri Jan 12 2018 Yuri N. Sedunov <aris@altlinux.org> 1.34.1-alt2
- rebuilt against libcdio.so.18

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.34.1-alt1
- 1.34.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 1.34.0-alt1
- 1.34.0

* Sun Jun 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.32.1-alt2
- rebuilt against libnfs.so.11

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.32.1-alt1
- 1.32.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.32.0-alt1
- 1.32.0

* Fri Dec 16 2016 Yuri N. Sedunov <aris@altlinux.org> 1.30.3-alt1
- 1.30.3

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.30.2-alt1
- 1.30.2

* Mon Oct 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.30.1.1-alt1
- 1.30.1.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0
- new admin backend

* Thu Aug 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.28.3-alt1
- 1.28.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.28.2-alt1
- 1.28.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.28.1-alt1
- 1.28.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.28.0-alt1
- 1.28.0

* Thu Feb 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.26.3-alt1
- 1.26.3

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.26.2-alt1
- 1.26.2

* Thu Oct 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.26.1.1-alt1
- 1.26.1.1

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 1.26.1-alt1
- 1.26.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1
- 1.26.0
- new google backend

* Thu Aug 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.24.2-alt1
- 1.24.2

* Mon Jul 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.24.1-alt2
- rebuilt against libcdio_{cdda,paranoia}.so.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 1.24.1-alt1
- 1.24.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1
- 1.24.0

* Mon Mar 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.4-alt1
- 1.22.4

* Mon Feb 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.3-alt3
- rebuilt against libimobiledevice.so.6

* Wed Jan 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.3-alt2
- rebuilt against libgphoto2_port.so.12

* Thu Jan 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.3-alt1
- 1.22.3

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.22.2-alt1
- 1.22.2
- new -tests subpackage

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt2
- rebuilt against libimobiledevice.so.5

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt1
- 1.22.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Mon Aug 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt1
- 1.20.3

* Fri Jun 20 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt2
- rebuilt against libplist.so.2

* Fri May 09 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt1
- 1.20.2

* Fri Apr 11 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Fri Mar 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Mon Jan 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt0.1
- 1.18.4 snapshot (fixed BGO ##720482, 598092, 720743, 670534..)

* Fri Nov 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Thu Oct 03 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2

* Thu Sep 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0
- disabled broken libgvfsdaemon+headers_install.patch

* Mon Jul 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt5
- sem@: new version of the alt-logind-state.patch (ALT #29185)

* Wed Jul 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt4
- sem@: updated alt-logind-state.patch

* Fri Jul 05 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt3
- new backend-mtp subpackage

* Tue Jul 02 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt2
- fixed afc backend for libimobiledevice new api from upstream
- added dependencies:
  backend-smb -> samba-client (ALT #29107)
- backend-goa -> gnome-online-accounts

* Fri Jun 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt1
- 1.16.3

* Tue Jun 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt2
- boyarsh@, aen@: gvfs-1.16.1-alt-logind-state.patch (ALT #29047)

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Tue Apr 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt2
- rebuilt against libimobiledevice.so.4

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0
- new gnome-online-accounts backend

* Mon Mar 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt3
- rebuilt against libarchive.so.13

* Tue Nov 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt2
- mtp devices support via libmtp (ALT #27989)

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2
- rediffed headers_install.patch

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1 release

* Wed Oct 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt0.1
- 1.14.1 snapshot (407e0eb1b)

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0
- new gvfs-backend-recent-files subpackage
- optional libsystemd-login support

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3 release

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt0.1
- 1.12.3 snapshot (01161473e)

* Wed May 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt2
- rebuild against libimobiledevice-1.1.3
- fixed build of afp backend

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Tue Sep 06 2011 Yuri N. Sedunov <aris@altlinux.org> 1.9.5-alt1
- 1.9.5
- new -backend-afp subpackage

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt1
- 1.6.7
- remove upstreamed patches

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt3
- fixed build against newer libgio
- fixed GNOME bug #633330

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt2
- libbluez4-devel/libbluez-devel

* Sat Nov 13 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- 1.6.6

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.5-alt1
- 1.5.5

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Mon Jan 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2
- AFC backend temporarily disabled (not ready for libiphone-0.9.6)

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Thu Dec 03 2009 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1
- new afc backend

* Mon Nov 30 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2
- removed upstreamed patches

* Wed Nov 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt3
- obsoletes gnome-mount{,-nautilus-properties} if enabled gdu
- some upstream patches

* Thu Nov 05 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt2
- rebuild against new libcdio

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2
- g-d-u support disabled for Sisyphus

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- 1.3.5

* Thu Aug 20 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt2
- g-d-u support enabled

* Mon Aug 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.3.4-alt1
- 1.3.4
- updated buildreqs

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Apr 21 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt2
- removed strange dependency on glib2-devel

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Apr 02 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Mar 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- 1.1.8

* Wed Feb 04 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5
- removed upstreamed patch
- enabled obexftp plugin

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4
- updated buildreqs
- temporarily disabled obexftp plugin, requires bluez >= 4.0

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3
- remove obsolete %%post{,un} scripts

* Mon Oct 20 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Oct 14 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt3
- remove support synce
- install common, daemon headers. build libgvfsdaemon.so (patch3)

* Mon Oct 13 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt2
- add synce-gvfs-0.1 backend as patch2 from http://sourceforge.net/projects/synce/

* Sat Sep 27 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- new version
- removed gvfs-ftp-read-directory-2.patch and
  gvfs-0.2.4-trash-automount.patch (fixed in upstream)
- updated archive-integration.patch
- updated buildreqs
- updated %%files
- don't rebuild documentation

* Thu Jun 26 2008 Alexey Shabalin <shaba@altlinux.ru> 0.99.1-alt1
- 0.99.1
- enable archive integration (patch1)
- fix GNOME bugs #522933, #525779 (patch2, patch3)
- add update_desktopdb in post-scripts

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Wed Apr 09 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1
- 0.2.3
- changed libexec dir to %_prefix/libexec/%name

* Wed Apr 02 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- 0.2.2

* Fri Mar 28 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt2
- fix exclude files (change libdir to libexecdir)

* Thu Mar 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- 0.2.1
- split the package into backends, utils
- move gvfs-bash-completion.sh from /etc/profile.d to /etc/bash_completion.d/,
  and individual package. (#15068)

* Thu Mar 20 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt2
- add require gnome-mount

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt1.1
- remove require gnome-mount

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt1
- redesigned spec

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 0.2.0.1-alt0.2
- update BuildRequires

* Thu Mar 13 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.2.0.1-alt0.1
- 0.2.0.1
- requires improvement

* Wed Mar 12 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 0.2.0-alt0.1
- 0.2.0
