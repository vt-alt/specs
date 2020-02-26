
%def_enable vgauth
%def_enable xmlsec1
%def_disable xmlsecurity

%def_disable deploypkg
%def_enable multimon
%def_without dnet
%def_enable resolutionkms

%def_without gtk2
%def_without gtkmm
%def_with gtk3
%def_with gtkmm3

%global majorversion    11.0
%global minorversion    5
%global toolsbuild      15389592
%global toolsversion    %majorversion.%minorversion
%global toolsdaemon     vmtoolsd
%global vgauthdaemon    vgauthd

Name: open-vm-tools
Version: %toolsversion
Release: alt1
Summary: Open Virtual Machine Tools for virtual machines hosted on VMware
Group: System/Kernel and hardware
License: GPLv2
Url: http://%name.sourceforge.net/
Source0: %name-%version.tar
Source1: %toolsdaemon.service
Source11: %vgauthdaemon.service
Source2: %toolsdaemon.init
Source12: %vgauthdaemon.init
Source3: %name.rules
Source4: %name-desktop.tmpfile
Source5: %toolsdaemon.pam
Source6: %name-%vgauthdaemon.tmpfile
Source99: 99-vmware-scsi-udev.rules

Patch100: add-altlinux-open-vm-tools.patch
Patch101: gcc9-drop-obsolete-G_INLINE_FUNC.patch

ExclusiveArch: %ix86 x86_64

# Need for vgauth
%{?_enable_xmlsec1:Requires: libxmlsec1-openssl >= 1.2.24-alt2}

BuildRequires: gcc-c++
BuildRequires: doxygen
# Fuse is optional and enables vmblock-fuse
BuildRequires: libfuse-devel
BuildRequires: glib2-devel >= 2.34.0
BuildRequires: gtk2-devel >= 2.4.0
BuildRequires: libgtkmm2-devel libsigc++2-devel
BuildRequires: libgtk+3-devel >= 2.4.0
BuildRequires: libgtkmm3-devel libsigc++2-devel
BuildRequires: libpam-devel
BuildRequires: libtirpc-devel
%{?_with_dnet:BuildRequires: libdnet-devel}
%{?_enable_multimon:BuildRequires: libX11-devel libXext-devel libXinerama-devel libXi-devel libXrender-devel libXrandr-devel libXtst-devel libICE-devel libSM-devel libXcomposite-devel}
%{?_enable_deploypkg:BuildRequires: libmspack-devel}
%{?_enable_vgauth:BuildRequires: libssl-devel}
%{?_enable_xmlsec1:BuildRequires: libxmlsec1-devel libxml2-devel}
%{?_enable_xmlsecurity:BuildRequires: libxml-security-c-devel libxerces-c-devel}
%{?_enable_resolutionkms:BuildRequires: libdrm-devel libudev-devel}

#BuildRequires:          kernel-headers-modules-std-def

%description
The %name project is an open source implementation of VMware Tools. It
is a suite of open source virtualization utilities and drivers to improve the
functionality, user experience and administration of VMware virtual machines.
This package contains only the core user-space programs and libraries of
%name.

%package desktop
Summary: User experience components for Open Virtual Machine Tools
Group: System/Libraries
Requires: %name = %version-%release

%description desktop
This package contains only the user-space programs and libraries of
%name that are essential for improved user experience of VMware virtual
machines.

%package devel
Summary: Development libraries for Open Virtual Machine Tools
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains only the user-space programs and libraries of
%name that are essential for developing customized applications for
VMware virtual machines.

%prep
%setup
#%%patch100 -p1
%patch101 -p2

rm -rf autom4te.cache
rm -f configure

%build
export CXXFLAGS="$RPM_OPT_FLAGS -std=gnu++11"
%autoreconf

%undefine _configure_gettext
%configure \
    --without-kernel-modules \
    --without-root-privileges \
    %{subst_enable vgauth} \
    %{subst_enable xmlsec1} \
    %{subst_enable xmlsecurity} \
    %{subst_enable deploypkg} \
    %{subst_enable multimon} \
    %{subst_with dnet} \
    %{subst_with gtk2} \
    %{subst_with gtkmm} \
    %{subst_with gtk3} \
    %{subst_with gtkmm3} \
    %{subst_enable resolutionkms} \
    --disable-static
# sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
# export DONT_STRIP=1
%makeinstall_std

mv %buildroot%_sysconfdir/vmware-tools/tools.conf.example %buildroot%_sysconfdir/vmware-tools/tools.conf
chmod a-x %buildroot%_sysconfdir/vmware-tools/*.conf
# Remove exec bit from config files
chmod a-x %buildroot%_sysconfdir/pam.d/*
%if_enabled vgauth
chmod a-x %buildroot%_sysconfdir/vmware-tools/vgauth/schemas/*
%endif

# Remove exec bit on udev rules
chmod a-x %buildroot%_udevrulesdir/99-vmware-scsi-udev.rules

# Remove the DOS line endings
sed -i "s|\r||g" README

# Remove "Encoding" key from the "Desktop Entry"
sed -i "s|^Encoding.*$||g" %buildroot%_sysconfdir/xdg/autostart/vmware-user.desktop

# Remove unnecessary files from packaging
find %buildroot%_libdir -name '*.la' -delete
rm -fr %buildroot%_defaultdocdir
rm -f docs/api/build/html/FreeSans.ttf

# Remove mount.vmhgfs & symlink
rm -fr %buildroot%_sbindir %buildroot/sbin/mount.vmhgfs

# Move vm-support to /usr/bin
mv %buildroot%_sysconfdir/vmware-tools/vm-support %buildroot%_bindir

# Systemd unit files
install -p -m 644 -D %SOURCE1 %buildroot%_unitdir/%toolsdaemon.service
install -p -m 644 -D %SOURCE11 %buildroot%_unitdir/%vgauthdaemon.service
# SysV init script
install -p -m 755 -D %SOURCE2 %buildroot%_initdir/%toolsdaemon
install -p -m 755 -D %SOURCE12 %buildroot%_initdir/%vgauthdaemon
# udev rules
install -p -m 644 -D %SOURCE3 %buildroot%_udevrulesdir/98-%name.rules
# install fixed udev rules
install -p -m 644 -D %SOURCE99 %buildroot%_udevrulesdir/99-vmware-scsi-udev.rules
# tmpfiles
install -p -m 644 -D %SOURCE4 %buildroot%_tmpfilesdir/%name-desktop.conf
install -p -m 644 -D %SOURCE6 %buildroot%_tmpfilesdir/%name-%vgauthdaemon.conf
# pam
install -p -m 644 -D %SOURCE5 %buildroot%_sysconfdir/pam.d/%toolsdaemon

mkdir -p %buildroot%_runtimedir/vmware
# 'make check' in open-vm-tools rebuilds docs and ends up regenerating
# the font file. We can add %%check secion once 'make check' is fixed
# upstream

%post
# Setup mount point for Shared Folders
if [ -f %_bindir/vmware-checkvm -a                     \
     -f %_bindir/vmhgfs-fuse ] &&                      \
   %_bindir/vmware-checkvm &> /dev/null &&             \
   %_bindir/vmware-checkvm -p | grep -q Workstation && \
   %_bindir/vmhgfs-fuse -e &> /dev/null; then
   mkdir -p /mnt/hgfs
fi

%post_service %vgauthdaemon
%post_service %toolsdaemon

%preun
%preun_service %toolsdaemon
%preun_service %vgauthdaemon
# Tell VMware that open-vm-tools is being uninstalled
if [ "$1" = "0" -a                      \
     -e %_bindir/vmware-checkvm -a    \
     -e %_bindir/vmware-rpctool ] &&  \
     %_bindir/vmware-checkvm &> /dev/null; then
		%_bindir/vmware-rpctool 'tools.set.version 0' &> /dev/null || /bin/true
		
		if [ -d /mnt/hgfs ] &&   \
		    %{_bindir}/vmware-checkvm -p | grep -q Workstation; then
		    umount /mnt/hgfs &> /dev/null || /bin/true
		    rmdir /mnt/hgfs &> /dev/null || /bin/true
		fi
fi

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %_sysconfdir/pam.d/*
%dir %_sysconfdir/vmware-tools
%if_enabled vgauth
%dir %_sysconfdir/vmware-tools/vgauth
%dir %_sysconfdir/vmware-tools/vgauth/schemas
%config(noreplace) %_sysconfdir/vmware-tools/*.conf
%config %_sysconfdir/vmware-tools/vgauth/schemas/*
%_initdir/%vgauthdaemon
%_unitdir/%vgauthdaemon.service
%_runtimedir/vmware
%_tmpfilesdir/%name-%vgauthdaemon.conf
%_bindir/vmware-vgauth-cmd
%_bindir/VGAuthService
%_libdir/libvgauth.so.*
%endif
%_sysconfdir/vmware-tools/*-vm-default
%_sysconfdir/vmware-tools/scripts
%_sysconfdir/vmware-tools/statechange.subr
%_bindir/vm-support
%_bindir/vmhgfs-fuse
%_bindir/vmtoolsd
%_bindir/vmware-checkvm
%_bindir/vmware-hgfsclient
%_bindir/vmware-namespace-cmd
%_bindir/vmware-rpctool
%_bindir/vmware-toolbox-cmd
%_bindir/vmware-xferlogs
%_libdir/libguestlib.so.*
%_libdir/libhgfs.so.*
%_libdir/libvmtools.so.*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/common
%_libdir/%name/plugins/common/*.so
%dir %_libdir/%name/plugins/vmsvc
%_libdir/%name/plugins/vmsvc/*.so
%_datadir/%name/
%_unitdir/%toolsdaemon.service
%_initdir/%toolsdaemon
%_udevrulesdir/*.rules

%files desktop
%_sysconfdir/xdg/autostart/*.desktop
%_bindir/vmware-user
%_bindir/vmware-user-suid-wrapper
%_bindir/vmware-vmblock-fuse
%_libdir/%name/plugins/vmusr/
%_tmpfilesdir/%name-desktop.conf

%files devel
%doc docs/api/build/*
%_includedir/vmGuestLib/
%_libdir/pkgconfig/*.pc
%_libdir/libguestlib.so
%_libdir/libhgfs.so
%_libdir/libvmtools.so
%if_enabled vgauth
%_libdir/libvgauth.so
%endif

%changelog
* Fri Feb 21 2020 Alexey Shabalin <shaba@altlinux.org> 11.0.5-alt1
- 11.0.5

* Sat Sep 28 2019 Alexey Shabalin <shaba@altlinux.org> 11.0.0-alt1
- 11.0.0

* Sun Mar 24 2019 Alexey Shabalin <shaba@altlinux.org> 10.3.10-alt1
- 10.3.10

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 10.3.5-alt1
- 10.3.5

* Mon Sep 10 2018 Alexey Shabalin <shaba@altlinux.org> 10.3.0-alt1
- 10.3.0

* Thu Sep 06 2018 Grigory Ustinov <grenka@altlinux.org> 10.1.10-alt1.S1.1
- NMU: rebuild with new openssl.

* Sun Aug 06 2017 Alexey Shabalin <shaba@altlinux.ru> 10.1.10-alt1
- 10.1.10
- build with gtk3 to sisyphus, and with gtk2 to p8
- build with vgauth

* Thu Jul 21 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt4
- add basealt detection

* Wed Mar 23 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt3
- fix to use git repo for source instead of tarball

* Thu Feb 25 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt1.M70P.1
- build for M70P

* Wed Feb 24 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt2
- fix search for alt linux
- clean package release from toolsbuild

* Wed Feb 24 2016 Sergey V Turchin <zerg@altlinux.org> 10.0.7-alt1.3227872
- new version

* Fri Dec 25 2015 Alexey Shabalin <shaba@altlinux.ru> 10.0.5-alt1.3227872
- 10.0.5

* Mon Sep 14 2015 Alexey Shabalin <shaba@altlinux.ru> 10.0.0-alt1.3000743
- open-vm-tools-10.0.0-3000743

* Thu Aug 13 2015 Alexey Shabalin <shaba@altlinux.ru> 9.10.2-alt1
- 9.10.2

* Sat Jun 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 9.10.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Apr 13 2015 Alexey Shabalin <shaba@altlinux.ru> 9.10.0-alt1
- 9.10.0

* Sat Apr 11 2015 Andrey Cherepanov <cas@altlinux.org> 9.4.6-alt1
- Initial build in Sisyphus (from Fedora)
