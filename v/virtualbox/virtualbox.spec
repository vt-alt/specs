%define oldmodname kernel-source-virtualbox
%define oldmodnamenetflt kernel-source-virtualbox-netfilter
%define oldmodnamenetadp kernel-source-virtualbox-netadaptor
%define oldmodnameadd kernel-source-virtualbox-addition
%define oldmodnameguest kernel-source-virtualbox-guest
%define oldmodnamevfs kernel-source-virtualbox-vfs
%define oldmodnamevideo kernel-source-virtualbox-video

%define modname kernel-source-vboxdrv
%define modnamepci kernel-source-vboxpci
%define modnamenetflt kernel-source-vboxnetflt
%define modnamenetadp kernel-source-vboxnetadp
%define modnameguest kernel-source-vboxguest
%define modnamevfs kernel-source-vboxsf
%define modnamevideo kernel-source-vboxvideo

%define distname VirtualBox
%define distarchive %distname-%{version}_OSE

%def_disable debug

%def_with manual
%def_without manualbuild
%def_without manualchm
%def_without manualsdk
%def_with additions
%def_with webservice
%def_without java
%def_with vnc
%def_with vde
%def_with libvpx
%def_with python
%def_without vboxpci

%ifarch %ix86
%define vbox_platform linux.x86
%endif
%ifarch x86_64
%define vbox_platform linux.amd64
%endif

%if_enabled debug
%define vboxdir %_builddir/%distarchive/out/%vbox_platform/release/bin
%define vboxdbg vbox-debug.sh
%define vboxdbg_file %_builddir/%distarchive/%vboxdbg
%else
%define vboxdir %_libdir/virtualbox
%endif

%if_with webservice
%define vboxwebdir %_localstatedir/vboxwebsrv
%endif

%define vboxdatadir %_datadir/virtualbox
%define ld_so_confdir %_sysconfdir/ld.so.conf.d
%define ld_so_conf %ld_so_confdir/%name-%_arch.conf

%filter_from_provides '/^lib[E]\\?GL\\.so\\./d'

%set_verify_elf_method textrel=relaxed
%add_findprov_lib_path %vboxdir

Name: virtualbox
Version: 6.1.8
Release: alt1

Summary: VM VirtualBox OSE - Virtual Machine for x86 hardware
License: GPLv2
Group: Emulators
Url: http://www.virtualbox.org/

ExclusiveArch: %ix86 x86_64

BuildRequires(pre): rpm-build-ubt

Source: %distarchive.tar

Source1:	%name.control.in
Source2:	%name.init
Source3:	%name-addition.rules
Source4:	%name.rules
Source5:	60-vboxadd.perms
Source6:	vboxadd-service.sysconfig
Source8:	vboxadd-service.init
Source9:	vboxweb-service.sysconfig
Source10:	vboxweb-service.init
Source15:	os_altlinux.png
Source16:	os_altlinux_64.png
Source22:	%name.service
Source23:	virtualbox.conf
Source25:	virtualbox-vboxvideo.modprobe.conf
Source26:	virtualbox-vboxguest.modprobe.conf
Source27:	virtualbox-vmsvga.service
Source28:	virtualbox-addition.conf

%if_with manual
%if_without manualbuild
Source100:	UserManual-%version.pdf
%endif
%endif

%if_enabled debug
Source99:	%vboxdbg.in
%endif

Patch:		%name-%version-alt.patch

BuildPreReq: dev86 iasl gcc-c++ libstdc++-devel-static
BuildPreReq: libIDL-devel libSDL-devel libpng-devel
BuildPreReq: libXcursor-devel libXext-devel
BuildPreReq: xsltproc
BuildPreReq: rpm-build-kernel
BuildPreReq: rpm-macros-qt5
BuildRequires: genisoimage
BuildRequires: docbook-dtds
BuildPreReq: libpulseaudio-devel
BuildRequires: libdevmapper-devel
BuildRequires: makeself
BuildRequires: qt5-tools
BuildRequires: qt5-connectivity-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-location-devel 
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-phonon-devel
BuildRequires: qt5-quick1-devel 
BuildRequires: qt5-quickcontrols2-devel 
BuildRequires: qt5-script-devel
BuildRequires: qt5-sensors-devel
BuildRequires: qt5-serialbus-devel
BuildRequires: qt5-x11extras-devel

BuildRequires: libopus-devel
BuildRequires: libssl-devel
BuildRequires: libxml2-devel libxslt-devel
BuildRequires: qt5-base-devel libalsa-devel
BuildRequires: libcap-devel libcurl-devel
BuildRequires: libXmu-devel libGLU-devel
BuildRequires: libXinerama-devel libXrandr-devel
BuildRequires: libXdamage-devel libXcomposite-devel libXcomposite
BuildRequires: xorg-xf86driproto-devel xorg-glproto-devel
BuildRequires: xorg-resourceproto-devel xorg-scrnsaverproto-devel
BuildRequires(pre): xorg-sdk
BuildPreReq: yasm kBuild >= 0.1.9998.r3178
%if_with webservice
BuildRequires: libgsoap-devel libgsoap-devel-static > 2.8.0
%endif
%if_with python
BuildRequires: python-dev
%endif
BuildRequires: libpam-devel
%if_with manualbuild
BuildRequires: texlive-latex-recommended
BuildRequires: docbook-style-xsl
BuildRequires: /usr/bin/chmcmd
%endif
%if_with manualchm
BuildRequires: i586-wine-vanilla
%endif
%if_with vnc
BuildRequires: libvncserver-devel
%endif
%if_with libvpx
BuildRequires: libvpx-devel
%endif
BuildRequires: rpm-build-xdg rpm-macros-pam
BuildRequires: /proc

PreReq: %name-common = %version-%release

%description
VirtualBox is a powerful PC virtualization solution allowing
you to run a wide range of PC operating systems on your Linux
system. This includes Windows, Linux, FreeBSD, DOS, OpenBSD
and others. VirtualBox comes with a broad feature set and
excellent performance, making it the premier virtualization
software solution on the market.

%package guest-additions
Summary: Full package of additions for VirtualBox OSE guest systems
Group: Emulators
Requires: xorg-drv-vboxvideo x11presetdrv
Requires: %name-guest-utils
Provides: %name-guest-additions-gl = %version-%release
Obsoletes: %name-guest-additions-gl < %version-%release

%description guest-additions
This packages contains full package of additions for VirtualBox OSE
guest systems. It consists basic utils, which allows to share files and
sync time with host system, and intergrates with xorg-server for mouse
and video driver with OpenGL support, copy/paste between guest and host.

%package guest-utils
Summary: Additions tools for VirtualBox OSE guest systems
Group: Emulators
Requires: %name-guest-common = %version-%release

%description guest-utils
This packages contains basic utils for VirtualBox OSE guest systems.
It allows to share files and sync time with host system.

%package guest-common
Summary: Additions common files for VirtualBox OSE guest systems
Group: Emulators

%description guest-common
This packages contains common files for VirtualBox OSE guest systems.
It consists modprobe rules to load kernel modules guest on guest system.

%package guest-common-vboxvideo
Summary: Additions common files for VirtualBox OSE vboxvideo driver
Group: Emulators

%description guest-common-vboxvideo
This packages contains common files for VirtualBox OSE vboxvideo driver.
It consists modprobe rules to load kernel module vboxvideo on guest system.

%package guest-common-vboxguest
Summary: Additions common files for VirtualBox OSE vboxguest driver
Group: Emulators

%description guest-common-vboxguest
This packages contains common files for VirtualBox OSE vboxguest driver.
It consists modprobe rules to load kernel module vboxguest on guest system.

%package webservice
Summary: VirtualBox Web Service
Group: Emulators
Requires: %name = %version-%release

%description webservice
This packages contains VirtualBox web service API daemon.
It allows to control virtual machines via web interface.

%package -n python-module-vboxapi
Summary: VirtualBox python API
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-vboxapi
This packages contains VirtualBox python module 'vboxapi'.
It allows to control virtual machines via python scripts.

%package -n %modname
Summary: Sources for VirtualBox module
Group: Development/Kernel
Provides: %oldmodname = %version-%release

%description -n %modname
Sources for VirtualBox kernel module.

%package -n %modnamepci
Summary: Sources for VirtualBox module for OSE pci
Group: Development/Kernel

%description -n %modnamepci
Sources for VirtualBox kernel module for OSE pci.

%package -n %modnamenetflt
Summary: Sources for VirtualBox module for OSE netfilter
Group: Development/Kernel
Provides: %oldmodnamenetflt = %version-%release

%description -n %modnamenetflt
Sources for VirtualBox kernel module for OSE netfilter.

%package -n %modnamenetadp
Summary: Sources for VirtualBox module for OSE netadaptor
Group: Development/Kernel
Provides: %oldmodnamenetadp = %version-%release

%description -n %modnamenetadp
Sources for VirtualBox kernel module for OSE netadaptor.

%package -n %modnameguest
Summary: Sources for VirtualBox module for OSE guest additions
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodnameadd = %version-%release
Provides: %oldmodnameguest = %version-%release

%description -n %modnameguest
Sources for VirtualBox kernel module for OSE guest additions.

%package -n %modnamevfs
Summary: Sources for VirtualBox module for OSE VFS
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodnamevfs = %version-%release

%description -n %modnamevfs
Sources for VirtualBox kernel module for OSE VFS.

%package -n %modnamevideo
Summary: Sources for VirtualBox module for OSE Video DRM
Group: Development/Kernel
BuildArch: noarch
Provides: %oldmodnamevideo = %version-%release

%description -n %modnamevideo
Sources for VirtualBox kernel module for OSE Video DRM.

%package common
Summary: VirtualBox module support files
Group: System/Configuration/Other
# due to new_summary function and is_builtin_mode bugfix
PreReq: control >= 0.7.2-alt1
PreReq: shadow-utils
# due to /bin/mountpoint
PreReq: sysvinit-utils

%description common
This package contains scripts and other support files which are
required to use the vboxdrv kernel module in the ALT Linux system.
The kernel module itself is not included - you need to install the
appropriate kernel-modules-virtualbox-* package for your kernel.

%package doc
Summary: VirtualBox documentation
Group: Documentation
Requires: %name = %version-%release

%description doc
This package contains VirtualBox User Manual.

%package sdk
Summary: VirtualBox SDK
Group: Development/Other
Requires: python-module-vboxapi = %version-%release

%description sdk
This package contains VirtualBox SDK.

%package sdk-xpcom
Summary: VirtualBox SDK XPCOM
Group: Development/Other
Requires: %name-sdk = %EVR

%description sdk-xpcom
This package contains VirtualBox SDK for XPCOM.

%prep
%setup -q -n %distarchive
%patch -p1

cp %SOURCE15 %SOURCE16 src/VBox/Frontends/VirtualBox/images

# fix python shebang for scripts
grep -R '^#!/usr/bin/\(env[[:space:]]\+\)\?python' src | cut -d: -f1 |
    while read f; do
        sed -E -i '1 s@^(#![[:space:]]*)%_bindir/(env[[:space:]]+)?python$@\1%__python@' "$f"
    done

%build
./configure --ose \
    --with-makeself="/usr/bin/makeself.sh" \
    --disable-kmods \
%if_with webservice
    --enable-webservice \
%endif
%if_without python
    --disable-python \
%endif
%if_without java
    --disable-java \
%endif
%if_with vnc
    --enable-vnc \
%endif
%if_with vde
    --enable-vde \
%endif
%if_without libvpx
    --disable-libvpx \
%endif
%if_without manualbuild
    --disable-docs \
%endif
%if_with manualchm
    --setup-wine \
%endif
%ifarch x86_64
    --disable-vmmraw \
%endif
    --enable-qt5 \

kbuild=%_bindir

%if_without additions
echo "VBOX_WITH_X11_ADDITIONS    := " >> LocalConfig.kmk
%endif
# don't build testcases to save time, they are not needed for the package
echo "VBOX_WITH_TESTCASES        :=" >> LocalConfig.kmk
echo "VBOX_WITH_TESTSUITE        :=" >> LocalConfig.kmk
# required for VBOX_PATH_APP_PRIVATE_*
echo "VBOX_DOCBOOK_WITH_LATEX    := 1" >> LocalConfig.kmk
echo "KBUILD_MSG_STYLE           := brief" >> LocalConfig.kmk
echo "VBOX_PATH_APP_PRIVATE_ARCH := %vboxdir" >> LocalConfig.kmk
echo "VBOX_PATH_SHARED_LIBS      := \$(VBOX_PATH_APP_PRIVATE_ARCH)" >> LocalConfig.kmk
echo "VBOX_WITH_RUNPATH          := \$(VBOX_PATH_APP_PRIVATE_ARCH)" >> LocalConfig.kmk
echo "VBOX_PATH_APP_PRIVATE      := %vboxdatadir" >> LocalConfig.kmk
echo "VBOX_PATH_APP_DOCS         := %_defaultdocdir/%name-doc-%version" >> LocalConfig.kmk
echo "VBOX_PATH_PACKAGE_DOCS     := \$(VBOX_PATH_APP_DOCS)" >> LocalConfig.kmk
echo "VBOX_VENDOR                := ALT Linux Team" >> LocalConfig.kmk
echo "VBOX_VENDOR_SHORT          := ALT" >> LocalConfig.kmk
echo "VBOX_PRODUCT               := VM VirtualBox OSE" >> LocalConfig.kmk

# disable build with bundled xorg/mesa headers
echo "VBOX_USE_SYSTEM_XORG_HEADERS := 1" >> LocalConfig.kmk
echo "VBOX_USE_SYSTEM_GL_HEADERS := 1" >> LocalConfig.kmk
# do not build legacy xorg driver
echo "VBOX_NO_LEGACY_XORG_X11 := 1" >> LocalConfig.kmk

echo "VBOX_WITH_REGISTRATION_REQUEST :=" >> LocalConfig.kmk
echo "VBOX_WITH_UPDATE_REQUEST :=" >> LocalConfig.kmk
echo "KBUILD_VERBOSE := 2" >> LocalConfig.kmk
echo "VBOX_WITH_EXTPACK_VBOXDTRACE :=" >> LocalConfig.kmk
%if_with vboxpci
echo "VBOX_WITH_PCI_PASSTHROUGH := 1" >> LocalConfig.kmk
%endif

# respect RPM optflags
echo "TOOL_GCC3_CFLAGS := %optflags" >> LocalConfig.kmk
echo "TOOL_GCC3_CXXFLAGS := %optflags" >> LocalConfig.kmk
echo "VBOX_GCC_OPT := %optflags" >> LocalConfig.kmk

%if_with manualsdk
echo "VBOX_WITH_DOCS_SDKREF      := 1" >> LocalConfig.kmk
%endif
%if_without manualsdk
echo "VBOX_WITH_DOCS_SDKREF      :=" >> LocalConfig.kmk
%endif
%if_with manualchm
echo "VBOX_WITH_DOCS_CHM         := 1" >> LocalConfig.kmk
echo "VBOX_CHMCMD                := 1" >> LocalConfig.kmk
%endif
%if_without manualchm
echo "VBOX_WITH_DOCS_CHM         :=" >> LocalConfig.kmk
echo "VBOX_CHMCMD                :=" >> LocalConfig.kmk
%endif
%if_with manualbuild
echo "VBOX_PATH_DOCBOOK          := /usr/share/xml/docbook/xsl-stylesheets" >> LocalConfig.kmk
echo "VBOX_PATH_DOCBOOK_DTD      := /usr/share/xml/docbook/dtd/4.5" >> LocalConfig.kmk
%endif

#source env.sh
[ -n "$NPROCS" ] || NPROCS=%__nprocs
# Set NPROCS=1 due build server constraints:
# https://lists.altlinux.org/pipermail/devel/2018-July/204964.html
NPROCS=1; kmk -j$NPROCS  VBOXDIR=%vboxdir

%if_enabled debug
sed 's|@VBOX_BUILD_DIR@|%vboxdir|g' %SOURCE99 >%vboxdbg_file
chmod u+x %vboxdbg_file
%endif

%install
%if_enabled debug
echo -e "\nVirtualBox not installable due debug build enabled\nRun: %vboxdbg_file\n  or %vboxdbg_file ./VirtualBox\n"
false
%endif

mkdir -p %buildroot{%_bindir,%_sbindir,%vboxdir/ExtensionPacks,%vboxdatadir,%kernel_src,%_initrddir,%_udevrulesdir}

%ifarch x86_64
# install common
install -Dp %SOURCE1 %buildroot%_controldir/%name
sed -i -e 's|@udevrulesdir@|%_udevrulesdir|g' %buildroot%_controldir/%name
install -Dp %SOURCE2 %buildroot%_initdir/%name
%if_without vboxpci
sed -i -n '/action .* modprobe --syslog $MODULENAMEPCI/!p' %buildroot%_initdir/%name
%endif
install -Dp -m644 %SOURCE4 \
	%buildroot%_udevrulesdir/90-%name.rules
%endif

%if_with additions
# install additions from src
install -Dp %SOURCE8 %buildroot%_initdir/vboxadd-service
install -Dp -m644 %SOURCE3 %buildroot%_udevrulesdir/60-vboxadd.rules

#install -d %buildroot%_sysconfdir/hal/fdi/policy
#install -m644 src/VBox/Additions/linux/installer/90-vboxguest.fdi %buildroot%_sysconfdir/hal/fdi/policy/90-vboxguest.fdi

install -d %buildroot%_sysconfdir/X11/xinit.d
install -m755 src/VBox/Additions/x11/Installer/98vboxadd-xclient %buildroot%_sysconfdir/X11/xinit.d
%endif

# install application
cd out/%vbox_platform/release/bin

%ifarch x86_64
cp -a \
    VBoxAutostart \
    VBoxBalloonCtrl \
    VBoxExtPackHelperApp \
    VBoxHeadless \
    VBoxManage \
    VBoxNetNAT \
    VBoxNetAdpCtl \
    VBoxNetDHCP \
    VBoxSDL \
    VBoxSVC \
    VBoxTestOGL \
    VBoxTunctl \
    VBoxVolInfo \
    VBoxXPCOMIPCD \
    VirtualBox \
    VirtualBoxVM \
    iPxeBaseBin \
    xpidl \
    *.r0 \
%ifarch %ix86
    *.rc \
%endif
    *.so \
    *.fd \
    *.py \
    components/ \
%if_with webservice
    vboxwebsrv \
%endif
    %buildroot%vboxdir

find sdk -maxdepth 1 -mindepth 1 -not -name docs -print0 | xargs -0 cp -R --target-directory=%buildroot%vboxdir --parents

cd ../../../../include/
mkdir -p %buildroot%_includedir
for d in iprt VBox/com; do
	cp -R --target-directory=%buildroot%_includedir --parents $d
done
cd -

%if_with python
cd sdk/installer >/dev/null
  VBOX_INSTALL_PATH=%vboxdir VBOX_VERSION=%version %__python vboxapisetup.py install --install-lib=%python_sitelibdir --root=%buildroot
cd -
%endif

cp -a \
    VBoxCreateUSBNode.sh \
    nls/ \
    %buildroot%vboxdatadir

# create links
for n in VBoxAutostart \
         VBoxBalloonCtrl \
	 VBoxHeadless \
         VBoxManage \
         VBoxSDL \
         VBoxTunctl \
         VBoxVolInfo \
         VirtualBoxVM \
         VirtualBox; do
    ln -s $n %buildroot%vboxdir/$(echo $n | tr A-Z a-z)
done
for n in VBoxAutostart \
         vboxautostart \
         VBoxBalloonCtrl \
         vboxballoonctrl \
         VBoxManage \
         vboxmanage \
         VBoxSDL \
         vboxsdl \
         VBoxTunctl \
         vboxtunctl \
         VBoxVolInfo \
         vboxvolinfo \
         VirtualBox \
         VirtualBoxVM \
         virtualbox \
%if_with webservice
         vboxwebsrv \
%endif
         xpidl; do
    ln -s $(relative %vboxdir/$n %_bindir/$n) %buildroot%_bindir
done

# remove breaked symlink to deleted module
rm -f %buildroot%vboxdir/components/VBoxREM.so

# install kernel sources
cp -a src/vboxdrv %buildroot%kernel_src/%modname-%version
%if_with vboxpci
cp -a src/vboxpci %buildroot%kernel_src/%modnamepci-%version
%endif
cp -a src/vboxnetflt %buildroot%kernel_src/%modnamenetflt-%version
cp -a src/vboxnetadp %buildroot%kernel_src/%modnamenetadp-%version
tar -C %buildroot%kernel_src -c %modname-%version | bzip2 -c > \
    %buildroot%kernel_src/%modname-%version.tar.bz2
rm -rf %buildroot%kernel_src/%modname-%version
%if_with vboxpci
tar -C %buildroot%kernel_src -c %modnamepci-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamepci-%version.tar.bz2
rm -rf %buildroot%kernel_src/%modnamepci-%version
%endif
tar -C %buildroot%kernel_src -c %modnamenetflt-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamenetflt-%version.tar.bz2
rm -rf %buildroot%kernel_src/%modnamenetflt-%version
tar -C %buildroot%kernel_src -c %modnamenetadp-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamenetadp-%version.tar.bz2
rm -rf %buildroot%kernel_src/%modnamenetadp-%version
%endif

cd additions >/dev/null
# install additions kernel sources
  cp -a src/vboxguest %buildroot%kernel_src/%modnameguest-%version
  tar -C %buildroot%kernel_src -c %modnameguest-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnameguest-%version.tar.bz2
  rm -rf %buildroot%kernel_src/%modnameguest-%version

# install VFS kernel sources
  cp -a src/vboxsf %buildroot%kernel_src/%modnamevfs-%version
  tar -C %buildroot%kernel_src -c %modnamevfs-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamevfs-%version.tar.bz2
  rm -rf %buildroot%kernel_src/%modnamevfs-%version

# install VFS kernel sources
  cp -a src/vboxvideo %buildroot%kernel_src/%modnamevideo-%version
  tar -C %buildroot%kernel_src -c %modnamevideo-%version | bzip2 -c > \
    %buildroot%kernel_src/%modnamevideo-%version.tar.bz2
  rm -rf %buildroot%kernel_src/%modnamevideo-%version

%if_with additions
# install additions
  install -d %buildroot/%_bindir
  install -m755 VBoxClient VBoxControl VBoxService %buildroot/%_bindir/

# install kernel modules configuration
  install -pDm644 %SOURCE25 %buildroot%_sysconfdir/modprobe.d/virtualbox-vboxvideo.conf
  install -pDm644 %SOURCE26 %buildroot%_sysconfdir/modprobe.d/virtualbox-vboxguest.conf
  install -pDm644 %SOURCE28 %buildroot%_sysconfdir/modules-load.d/virtualbox-addition.conf

# create links
  ln -s $(relative %_bindir/VBoxService %_sbindir/) %buildroot%_sbindir/vboxadd-service

# install sysconfig for vboxadd-service
  mkdir -p %buildroot%_sysconfdir/sysconfig
  cp %SOURCE6 %buildroot%_sysconfdir/sysconfig/vboxadd-service

# install mount vbox share folder
  install -d %buildroot/sbin
  install -m755 mount.vboxsf %buildroot/sbin/mount.vboxsf

  install -d %buildroot%_sysconfdir/security/console.perms.d/
  install -m644 %SOURCE5 %buildroot%_sysconfdir/security/console.perms.d/

  install -d %buildroot%_unitdir/
  install -m755 %SOURCE27 %buildroot%_unitdir/

  mkdir -p %buildroot%_pam_modules_dir/
  install -m644 pam_vbox.so %buildroot%_pam_modules_dir/
%endif
cd - >/dev/null

%ifarch x86_64
# install icons
mkdir -p %buildroot%_niconsdir
install -m644 icons/32x32/*.png %buildroot%_niconsdir/
mkdir -p %buildroot%_miconsdir
install -m644 icons/16x16/*.png %buildroot%_miconsdir/
mkdir -p %buildroot%_liconsdir
install -m644 icons/48x48/*.png %buildroot%_liconsdir/
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
install -m644 icons/64x64/*.png %buildroot%_iconsdir/hicolor/64x64/apps/
mkdir -p %buildroot%_iconsdir/hicolor/128x128/apps
install -m644 icons/128x128/*.png %buildroot%_iconsdir/hicolor/128x128/apps/

# install mime types
mkdir -p %buildroot%_xdgmimedir/packages
install -m644 virtualbox.xml %buildroot%_xdgmimedir/packages/virtualbox.xml

# install menu entries
mkdir -p %buildroot%_desktopdir
install -m644 %name.desktop %buildroot%_desktopdir/
sed -i 's|^DocPath=|#DocPath=|' %buildroot%_desktopdir/%name.desktop

# install docs
mkdir -p %buildroot%_defaultdocdir/%name-doc-%version
%if_with manual
%if_with manualbuild
install -m644 UserManual.pdf %buildroot%_defaultdocdir/%name-doc-%version/
cp -r ../obj/manual/en_US/HTMLHelp %buildroot%_defaultdocdir/%name-doc-%version/HTML
%endif
%if_with manualchm
install -m644 VirtualBox.chm %buildroot%_defaultdocdir/%name-doc-%version/
%endif
%if_with manualsdk
find sdk/docs -maxdepth 1 -mindepth 1 -print0 | xargs -0 -i install -m644 {} %buildroot%_defaultdocdir/%name-doc-%version/
%endif
%if_without manualbuild
install -m644 %SOURCE100 %buildroot%_defaultdocdir/%name-doc-%version/UserManual.pdf
%endif
%endif

# install unit file
install -pDm644 %SOURCE22 %buildroot%_unitdir/%name.service
install -pDm644 %SOURCE23 %buildroot%_sysconfdir/modules-load.d/%name.conf
%if_without vboxpci
sed -i -n '/vboxcpi/!p' %buildroot%_unitdir/%name.service
sed -i -n '/vboxcpi/!p' %buildroot%_sysconfdir/modules-load.d/%name.conf
%endif



%if_with vnc
 cp -a ExtensionPacks/VNC %buildroot%vboxdir/ExtensionPacks/
%endif

%if_with webservice
  mkdir -p %buildroot%vboxwebdir

# install vboxweb-service initscript
  install -Dp %SOURCE10 %buildroot%_initdir/vboxweb-service

# install sysconfig for vboxweb-service
  mkdir -p %buildroot%_sysconfdir/sysconfig
  cp %SOURCE9 %buildroot%_sysconfdir/sysconfig/vboxweb-service
%endif
%endif

%pre
%pre_control %name

%post
%post_control -s vboxusers %name
%post_service virtualbox

%preun
%preun_service virtualbox

%post doc
sed -i 's|^#DocPath=|DocPath=|' %_desktopdir/%name.desktop
XDG_DATA_DIRS="%_datadir" update-desktop-database -q ||:

%preun doc
sed -i 's|^DocPath=|#DocPath=|' %_desktopdir/%name.desktop
XDG_DATA_DIRS="%_datadir" update-desktop-database -q ||:

%pre common
%pre_control %name
/usr/sbin/groupadd -r -f vboxusers

%post common
%post_service %name
%post_control -s vboxusers %name

%preun common
%preun_service %name

%triggerin common -- dev
# If using static /dev, select the same status again to fix permissions
mountpoint -q /dev || {
	status="`/usr/sbin/control %name status`" || status=
	[ -n "$status" ] && /usr/sbin/control %name "$status" ||:
}

%pre guest-additions
/usr/sbin/groupadd -r -f vboxadd

%if_with webservice
%pre webservice
/usr/sbin/useradd -r -g vboxusers -d %vboxwebdir -c 'VirtualBox Web Service' -n vboxwebsrv -s /bin/sh >/dev/null 2>&1 ||:
%endif

%ifarch x86_64
%files
%_bindir/*
%vboxdir/*
%exclude %_bindir/xpidl
%if_with additions
%exclude %_bindir/VBoxClient
%exclude %_bindir/VBoxControl
%exclude %_bindir/VBoxService
%endif
%if_with webservice
%exclude %_bindir/vboxwebsrv
%exclude %vboxdir/vboxwebsrv
%endif
%dir %vboxdir
%dir %vboxdir/ExtensionPacks
%attr(4710,root,vboxusers) %vboxdir/VBoxExtPackHelperApp
%attr(4710,root,vboxusers) %vboxdir/VBoxHeadless
%attr(4710,root,vboxusers) %vboxdir/VBoxNetDHCP
%attr(4710,root,vboxusers) %vboxdir/VBoxNetNAT
%attr(4710,root,vboxusers) %vboxdir/VBoxNetAdpCtl
%attr(4710,root,vboxusers) %vboxdir/VBoxSDL
%attr(4710,root,vboxusers) %vboxdir/VBoxVolInfo
%attr(4710,root,vboxusers) %vboxdir/VirtualBoxVM
%vboxdir/VirtualBox
%exclude %vboxdir/sdk
%exclude %vboxdir/xpidl
%exclude %vboxdir/VBoxPython*.so
%vboxdatadir/nls
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png
%_iconsdir/hicolor/64x64/apps/*.png
%_iconsdir/hicolor/128x128/apps/*.png
%_xdgmimedir/packages/*.xml
%_desktopdir/*.desktop

%files -n %modname
%kernel_src/%modname-%version.tar.bz2

%if_with vboxpci
%files -n %modnamepci
%kernel_src/%modnamepci-%version.tar.bz2
%endif

%files -n %modnamenetflt
%kernel_src/%modnamenetflt-%version.tar.bz2

%files -n %modnamenetadp
%kernel_src/%modnamenetadp-%version.tar.bz2
%endif

%files -n %modnameguest
%kernel_src/%modnameguest-%version.tar.bz2

%files -n %modnamevfs
%kernel_src/%modnamevfs-%version.tar.bz2

%files -n %modnamevideo
%kernel_src/%modnamevideo-%version.tar.bz2

%if_with additions
%files guest-common
%config %_sysconfdir/modules-load.d/virtualbox-addition.conf

%files guest-common-vboxvideo
%config %_sysconfdir/modprobe.d/virtualbox-vboxvideo.conf

%files guest-common-vboxguest
%config %_sysconfdir/modprobe.d/virtualbox-vboxguest.conf

%files guest-utils
/sbin/mount.vboxsf
%_initrddir/vboxadd-service
%config(noreplace) %_sysconfdir/sysconfig/vboxadd-service
%config %_udevrulesdir/60-vboxadd.rules
%_sbindir/vboxadd-service
%_bindir/VBoxControl
%_bindir/VBoxService
%_pam_modules_dir/*.so
%_sysconfdir/security/console.perms.d/60-vboxadd.perms

%files guest-additions
%_unitdir/virtualbox-vmsvga.service
%_sysconfdir/X11/xinit.d/98vboxadd-xclient
%_bindir/VBoxClient
%endif

%ifarch x86_64
%if_with webservice
%files webservice
%_initrddir/vboxweb-service
%config(noreplace) %_sysconfdir/sysconfig/vboxweb-service
%dir %attr(0750,vboxwebsrv,vboxusers) %vboxwebdir
%vboxdir/vboxwebsrv
%_bindir/vboxwebsrv
%endif

%if_with python
%files -n python-module-vboxapi
%vboxdir/VBoxPython*.so
%python_sitelibdir/*
%vboxdir/sdk/bindings/xpcom/python/xpcom
%endif

%files common
%_initdir/%name
%_unitdir/%name.service
%_controldir/%name
%config %_udevrulesdir/90-%name.rules
%dir %vboxdatadir
%vboxdatadir/VBoxCreateUSBNode.sh
%config %_sysconfdir/modules-load.d/%name.conf

%if_with manual
%files doc
%_defaultdocdir/%name-doc-%version
%endif

%files sdk
%_bindir/xpidl
%vboxdir/xpidl
%vboxdir/sdk
%if_with python
%exclude %vboxdir/sdk/bindings/xpcom/python/xpcom
%endif

%files sdk-xpcom
%_includedir/iprt
%_includedir/VBox/com
%endif

%changelog
* Thu May 21 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.8-alt1
- Update to newest version 6.1.8

* Wed Apr 15 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.6-alt1
- Update to newest version 6.1.6

* Fri Apr 03 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt5
- Build with installable documentation (Closes: 38316)

* Thu Mar 19 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt4
- Fix shared clipboard regression:
  https://www.virtualbox.org/ticket/19336 (Closes: 38239)

* Fri Mar 13 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt3
- Removed loading the vboxpci kernel module (Closes: 38157)

* Wed Mar 04 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt2
- Add separated modprobe rules for vboxguest and vboxvideo

* Thu Feb 20 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.4-alt1
- Update to newest version 6.1.4

* Mon Jan 20 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.2-alt1
- Update to latest maintenance of 6.1 release
- Build without droped PCI passthrough host driver, due current code is too
  incomplete (cannot handle PCIe devices at all), i.e. not useful enough

* Mon Jan 20 2020 Valery Sinelnikov <greh@altlinux.org> 6.1.0-alt3
- Fix window resize with VMSVGA

* Mon Dec 23 2019 Valery Sinelnikov <greh@altlinux.org> 6.1.0-alt2
- Replace shabang in python scripts
- Build guest additions only for i586
- Revert vboxpci module

* Wed Dec 18 2019 Valery Sinelnikov <greh@altlinux.org> 6.1.0-alt1
- Update to newest version of 6.1 release
- Remove obsolete kernel source subpackage for vboxpci module

* Wed Dec 18 2019 Valery Sinelnikov <greh@altlinux.org> 6.0.14-alt1
- Update to newest version of 6.0 release

* Wed Dec 04 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.34-alt3
- Add virtualbox-guest-common subpackages with modules load and modprobe rules
- Fix build with newest libglvnd later than 1.2.0 on Sisyphus
- Adjust license to GPLv2 (closes: 37575)

* Tue Dec 03 2019 Valery Sinelnikov <greh@altlinux.org> 5.2.34-alt2
- Add modprobe install rules for renamed vboxguest and vboxvideo

* Sun Oct 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.34-alt1
- Update to latest of 5.2 release with support kernel-5.3.x (Closes: 37351)

* Mon Oct 14 2019 Valery Sinelnikov <greh@altlinux.org> 5.2.32-alt1
- Update to latest of 5.2 release

* Tue Jul 09 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.30-alt1
- Update to latest of 5.2 release with Linux 5.0 and 5.1 support

* Tue Mar 26 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.26-alt3
- Rebuild without obsolete qt5-gstreamer1 (Closes: 36428)

* Wed Mar 06 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.26-alt2
- Fix drv preload in check if 3D acceleration is supported (Closes: 36235)

* Fri Feb 08 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.26-alt1
- Update to latest of 5.2 release

* Fri Feb 08 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.24-alt5
- Replace drvpre script from spec to separate file

* Thu Feb 07 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 5.2.24-alt4
- Propperly check if 3D acceleration is supported before preloading
  VirtualBox's libGL.so.1 and libEGL.so.1 and update ldconfig cache
  after changes to /etc/ld.so.conf.d/*.conf (Closes: 36035)

* Fri Jan 25 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.24-alt3
- Fix rEFInd 0.11.4 icons missing due to inaccessible files on ISO9660 partition (Closes: 34435)

* Thu Jan 24 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.24-alt2
- Avoid volatile in asm inline within function context due new gcc8 release (Closes: 35929)

* Wed Jan 16 2019 Evgeny Sinelnikov <sin@altlinux.org> 5.2.24-alt1
- Build first winter security release (Fixes: CVE-2019-2500, CVE-2019-2524, CVE-2019-2552)

* Wed Dec 12 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.22-alt4
- Add lost VMMRC.rc due manual install on ix86

* Tue Dec 04 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.22-alt3
- Merge with branch c8.1 for common build

* Tue Dec 04 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.22-alt2
- Merge with branch c8 for common build with branch p8

* Fri Nov 30 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.22-alt1
- Build second autumn release

* Fri Oct 19 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.20-alt1
- Build first autumn release

* Mon Oct 15 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.18-alt1
- Build latest release of 5.2 release
- Add vboxfs patch from Debian fixed failure with new kernel 4.18
- Disable ubt macros due binary package identity changes
- Obsoletes virtualbox-guest-additions-gl subpackage (closes #35059)
- Add x11presetdrv script for dynamic create ld.so.conf settings for GL libraries

* Thu Sep 06 2018 Grigory Ustinov <grenka@altlinux.org> 5.2.16-alt2%ubt.1
- NMU: rebuild with new openssl.

* Tue Jul 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.16-alt2%ubt
- Replace VirtualBox OpenGL libraries and settings to separate package due
  it conflicts with drivers on host systems, where virtualbox-guest-additions
  already installed (closes: #35170)

* Wed Jul 18 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.16-alt1%ubt
- Build second summer release
- guest-addition: fix OGL/EGL provides (thanks to lakostis@)

* Tue Jul 10 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.14-alt1%ubt
- Build latest summer release

* Thu May 24 2018 Evgeny Sinelnikov <sin@altlinux.org> 5.2.12-alt1%ubt
- Build latest version with ubt macros (aka universal build tag)

* Sat May 19 2018 L.A. Kostis <lakostis@altlinux.ru> 5.2.12-alt0.3
- fix OGL/EGL guest libs.
- respect RPM optflags.

* Fri May 18 2018 L.A. Kostis <lakostis@altlinux.ru> 5.2.12-alt0.2
- .spec: sync with debian:
    + VBOX_WITH_REGISTRATION_REQUEST=
    + VBOX_WITH_UPDATE_REQUEST=
    + KBUILD_VERBOSE=2
    + VBOX_WITH_EXTPACK_VBOXDTRACE=
    + use system xorg libs again.
    + remove obsoleted xorg vbox drv.
    + rework OGL/EGL support.

* Thu May 17 2018 L.A. Kostis <lakostis@altlinux.ru> 5.2.12-alt0.1
- try build of 5.2.12.

* Thu Jan 11 2018 Denis Medvedev <nbr@altlinux.org> 5.1.30-alt3
- add missed altlinux type handling routines

* Mon Dec 25 2017 Denis Medvedev <nbr@altlinux.org> 5.1.30-alt2
- patch for kernel 4.14

* Mon Nov 13 2017 Denis Medvedev <nbr@altlinux.org> 5.1.30-alt1
- new version 5.1.30
No more %ubt - too much changes between branches.
(Fixes: CVE-2017-10392,
CVE-2017-10407,
CVE-2017-10408,
CVE-2017-3733,
CVE-2017-10428)

* Thu Jul 20 2017 Denis Medvedev <nbr@altlinux.org> 5.1.24-alt1%ubt
- new version 5.1.24
(Fixes: CVE-2017-10129, CVE-2017-10187, CVE-2017-10204, CVE-2017-10209, CVE-2017-10210, CVE-2017-10233, CVE-2017-10235, CVE-2017-10236, CVE-2017-10237, CVE-2017-10238, CVE-2017-10239, CVE-2017-10240, CVE-2017-10241, CVE-2017-10242)

* Thu Mar 16 2017 Denis Medvedev <nbr@altlinux.org> 5.1.18-alt1%ubt
- new version 5.1.18

* Wed Mar 15 2017 Denis Medvedev <nbr@altlinux.org> 5.1.16-alt1%ubt
- new version 5.1.16, git sources changed to have branch
 upstream, 5.1.16-patched for alt patches and
 sisyphus - for spec and local files.

* Thu Feb 02 2017 Evgeny Sinelnikov <sin@altlinux.ru> 5.1.14-alt2%ubt
- Rebuild with gsoap-2.8.x and universal build tag

* Fri Jan 20 2017 Denis Medvedev <nbr@altlinux.org> 5.1.14-alt1
- new version 5.1.14

* Thu Dec 22 2016 Denis Medvedev <nbr@altlinux.org> 5.1.12-alt1
- new version 5.1.12

* Tue Nov 22 2016 Denis Medvedev <nbr@altlinux.org> 5.1.10-alt1
- new version 5.1.10

* Thu Sep 15 2016 Denis Medvedev <nbr@altlinux.org> 5.1.6-alt1
- new version 5.1.6, ALT Linux types marked as "do not use", fixed
overflow bug.

* Wed Jul 27 2016 Denis Medvedev <nbr@altlinux.org> 5.1.2-alt1
- new version 5.1.2 (clean)

* Fri Jun 24 2016 Denis Medvedev <nbr@altlinux.org> 5.0.20-alt2
- fixed translation of message that happens when virtualbox
service is not started

* Wed May 11 2016 Denis Medvedev <nbr@altlinux.org> 5.0.20-alt1
- 5.0.20

* Tue Apr 05 2016 Denis Medvedev <nbr@altlinux.org> 5.0.16-alt2
- with docs

* Tue Apr 05 2016 Denis Medvedev <nbr@altlinux.org> 5.0.16-alt1
- new version imported

* Thu Mar 10 2016 Denis Medvedev <nbr@altlinux.org> 5.0.14-alt2
- added support for virtual machines with ALTLinux.

* Wed Feb 17 2016 Denis Medvedev <nbr@altlinux.org> 5.0.14-alt1
- new version imported.

* Fri Nov 27 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.3.30-alt3
- removed requires XORG_ABI_VIDEODRV

* Tue Sep 01 2015 Aleksey Avdeev <solo@altlinux.org> 4.3.30-alt2
- Add subpackage virtualbox-sdk-xpcom (Closes: 31178)
- Add synonyms lowercase (Closes: 31245)

* Mon Aug 31 2015 Aleksey Avdeev <solo@altlinux.org> 4.3.30-alt1
- Update to last stable release
- All documentation is build

* Sun Jul 05 2015 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.28-alt1
- Update to last stable release

* Fri May 22 2015 Michael Shigorin <mike@altlinux.org> 4.3.26-alt2
- Fixed thinko in 4.3.22-alt2 (closes: #31023)

* Sat Apr 11 2015 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.26-alt1
- Update to new release with Linux 4.0 fixes

* Tue Apr 07 2015 Michael Shigorin <mike@altlinux.org> 4.3.22-alt2
- Don't raise desktop notification about absent kernel modules
  if modules are present but not loaded on e.g. real hardware

* Sat Feb 14 2015 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.22-alt1
- Update to last stable release

* Mon Jan 19 2015 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.20-alt1
- Update to new release

* Thu Oct 16 2014 Michael Shigorin <mike@altlinux.org> 4.3.14-alt2
- Added systemd unit file (see also #30260)
- Rebuild with xorg-1.16.1

* Tue Sep 02 2014 Michael Shigorin <mike@altlinux.org> 4.3.14-alt1
- Update to new release

* Tue Feb 04 2014 Fr. Br. George <george@altlinux.ru> 4.3.6-alt3
- Rebuild with xorg-1.15

* Tue Jan 07 2014 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.6-alt2
- Control VBoxExtPackHelperApp with setuid restrictions

* Tue Jan 07 2014 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.6-alt1
- Update to new release

* Wed Dec 04 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.4-alt1
- Update to new release

* Thu Nov 21 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.3.2-alt1
- Update to new release of stable branch 4.3

* Wed Nov 20 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.18-alt1
- Update to last release of stable branch 4.2

* Tue Oct 08 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.2.16-alt4
- Fix build with libvncserver >= 0.9.9.

* Mon Sep 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.2.16-alt3
- fix virtualbox-addition for build with kernel 3.11

* Mon Sep 09 2013 Fr. Br. George <george@altlinux.ru> 4.2.16-alt2
- Switch back to GCC 4.5 (Closes: #29344)

* Wed Aug 14 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.16-alt1
- Update to new release of stable branch 4.2
- Build for Sisyphus with gcc-4.7

* Sun Jun 30 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.14-alt1
- Update to last release of stable branch 4.2
- Add python-module-vboxapi separate VirtualBox SDK subpackage

* Tue Apr 30 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.12-alt2
- Fix rpath for VBoxOGL.so and VBoxOGL*spu.so (Closes: 27340)

* Thu Apr 18 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.12-alt1
- Update to last release of stable branch 4.2
- Enable build with webservice
- Fix installation of VNC ExtensionPack

* Sun Mar 17 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.10-alt1
- Update to last stable release with multiple fixes for Sisyphus

* Wed Jan 30 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.6-alt1
- Update to last release of stable branch 4.2

* Sun Jan 20 2013 Michael Shigorin <mike@altlinux.org> 4.2.4-alt1.1
- NMU: rebuilt against xorg-1.13

* Thu Nov 22 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.2.4-alt1
- Update to last stable release 4.2
- Remove vboxmouse_drv due it not needed at all for X.Org Server 1.7 and later

* Thu Oct 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.20-alt1.1
- Rebuilt with libpng15

* Wed Aug 22 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.20-alt1
- Update to new stable release
- Revert exclude for vboxadddir to main virtualbox package
- Fix VBoxCreateUSBNode.sh empty class with --create option

* Sat Jul 28 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.18-alt1
- Update to new release for Sisyphus
- Enable Virtual Distributed Ethernet (VDE) support
- Create /dev/vboxusb at startup (Closes: 26953)
- Fix virtualbox control facility restore during upgrade (Closes: 25150)
- Fix OpenGL installation for guest additions (Closes: 27340)

* Wed Apr 04 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.12-alt2
- Enable the built in VNC server
- Avoid conflict with renamed xorg-drv modules

* Wed Apr 04 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.12-alt1
- Update to new release for Sisyphus
- Fix build vboxvideo with new xorg-server-1.12

* Sun Apr 01 2012 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.10-alt1
- Update to new release
- Add subpackage virtualbox-guest-utils with basic guest addition tools
  without dependency to xorg server

* Fri Dec 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.6-alt1
- Update to new release with minor bugfixes:
 + VRDP: fixed screen corruption
 + NAT: the interface stopped working after a lot of failed ICMP requests
 + ATA: fixed a possible crash during ATAPI passthrough with certain guests
 + ATA: improved compatibility with ancient Linux kernels
 + Main: fixed incorrect framebuffer information after leaving the
   fullscreen mode with X11 guests

* Fri Nov 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.4-alt1.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.4-alt1
- Update to new release
- Added kernel source subpackage for vboxpci module

* Sat Jul 23 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.12-alt1
- Update to new release
- Fix problems with guest addition init scripts.

* Tue May 03 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt4
- Adopt and apply Ubuntu patch for build the X.Org driver only
  for the selected system X Server version with native includes

* Mon May 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt3
- Rebuild with xorg-server-1.10
- Apply patches from Ubuntu build:
 + Fix build failure with kernel 2.6.39-rc1
 + Fix FTBFS with ld --as-needed
 + Make Xsession.d script ignore errors

* Tue Mar 01 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt2
- Add missed VBoxExtPackHelperApp

* Tue Feb 22 2011 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.4-alt1
- Update to new release
+ Fix ALT Linux OS type support
+ Set Default OS type to Linux
+ Replace nls files to vboxdatadir
+ Add udev rules for USB (works only for vboxusers group now)
+ Add HTML documentation
+ Register mime types for next extensions:
 *.vbox - VirtualBox Machine Definition
 *.vbox-extpack - VirtualBox Extension Pack
 *.ovf - Open Virtualization Format
 *.ova - Open Virtualization Format Archive

* Wed Jan 06 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.12-alt1
- Update to new release
- Adjust addittional xorg drivers for xorg-server-1.9.x
- Set fixed rpath to VBOXDIR
- Add SDK Reference to documentation

* Thu Dec 16 2010 Michail Yakushin <silicium@altlinux.ru> 3.2.4-alt4
- Fix build

* Fri Jun 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt3
- Fix RuntimeGuestR3Mini linkage with rtThreadGet() for xorg addition drivers
- Fix vboxmouse default installation (Closes: 23479)

* Thu Jun 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt2
- Add build require for libpam-devel

* Mon Jun 09 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.4-alt1
- Update to new release

* Mon May 10 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.8-alt1
- Update to new release
- Rename kernel-source subpackages (Closes: 22458)
- Copy additional video drivers for xorg-server-1.8

* Sat Mar 27 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.6-alt1
- Update to new release

* Wed Mar 03 2010 Evgeny Sinelnikov <sin@altlinux.ru> 3.1.4-alt1
- Update to lastest release (Closes: 22556)

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 3.0.10-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for virtualbox
  * postclean-05-filetriggers for spec file

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.10-alt1.1
- Rebuilt with python 2.6

* Tue Nov 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.10-alt1
- Update to new release

* Wed Oct 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.8-alt1
- Update to new release
- Add various files for guest-addition (#21727)

* Sun Sep 20 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.6-alt1
- Update to new release

* Tue Aug 11 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.4-alt1
- Update to new release

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.2-alt1
- Fix vboxadd-service sysconfig file installation
- Update to new release

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt3
- Fix guest addition initscripts

* Sun Jul 12 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt2
- Add new VBoxNetAdpCtl utility and VBoxNetDHCP feature
- Add support for new kernel modules
- Added kernel source subpackage for netadaptor module
- Added kernel source subpackage for video module

* Wed Jul 08 2009 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.0-alt1
- Update to new release

* Tue Jun 02 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.4-alt1
- Update to new release
- Build with gcc-4.3

* Sun May 10 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.2.2-alt1
- Update to new release

* Mon Mar 09 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt5
- Build with last xorg drivers

* Sat Mar 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt4
- Added ALT Linux OS type

* Sat Mar 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt3
- Avoided addition installation to main packages
- Applied vbox-evdev.patch

* Sat Mar 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt2
- Fixed for building witn glibc-kernheaders >= 2.6.28

* Wed Feb 25 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.4-alt1
- Update to new release
- Requires added to base package from common subpackage (#18434)

* Thu Feb 05 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.2-alt1
- Update to new release

* Wed Feb 04 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt4
- Fixed SDK package instalation due silly python requires for _xpcom

* Wed Feb 04 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt3
- Fixed problem with different set of noarch packages for i586
  with x86_64 build

* Wed Feb 04 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt2
- Build for x86_64
- Remove vbox-guest-additions from modprobe.d and add initscirpt
  instead (#18282)
- Build fixes (thanks for vsu@)
 + Put uncompressed tarball into src.rpm
 + Honor NPROCS and %__nprocs when invoking kmk
 + Add workarounds for missing biarch support and enable x86_64 build

* Fri Dec 19 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.1.0-alt1
- Update to new release
- Fixed bug with control adjust for setuid binary (#18170)
- Fixed rpath and initscripts patches for new version
- Added kernel source subpackage for vboxnetflt module
- Fixed virtualbox initscript for vboxnetflt module using
- Added sdk subpackage

* Sun Nov 02 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.4-alt1
- Update to new release

* Thu Sep 04 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.6-alt1
- Updated to new release
- Removed not needed and bad patches:
 + vbox-vboxfs-2.6.25.diff - not used
 + virtualbox-missing-Makefiles.diff - fixed in new version
 + use-o3-to-workaround-gcc-ice.diff - bad on gcc-4.1
- Prepared to build for x86_64 (not ready yet)

* Fri Aug 29 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.4-alt1
- Updated to new version
- Added documentation subpackage with UserManual.pdf (#16700)
- Added links for VBoxTunctl, VBoxAddIF and VBoxDeleteIF (#16700)
- Fixed desktop file (#16700)

* Sat Jun 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.2-alt1
- Updated to 1.6.2
- Fixed building patches

* Sat Jun 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.0-alt0
- Updated to 1.6.0
- Fixed requires

* Fri Apr 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt2
- Removed SysVinit version at requires

* Sat Apr 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt1
- Add nls for i18n support

* Thu Mar 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 1.5.6-alt0.1
- Build new version

* Mon Apr 23 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.99-alt0.r2155
- SVN r2155
- symlink binaries into %%_bindir
- add udev rules file for /dev/vboxdrv

* Sun Apr 01 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.99-alt0.r1788
- SVN r1788

* Sat Feb 17 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.99-alt0.r934
- initial build
