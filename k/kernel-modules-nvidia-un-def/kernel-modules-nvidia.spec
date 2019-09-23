%define nvIF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define nvIF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define nvIF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define nvIF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%define module_name		nvidia
%define modesetmodule_name	nvidia-modeset
%define uvmmodule_name		nvidia-uvm
%define drmmodule_name		nvidia-drm
%define package_version	430.50
%define module_version	%package_version
%ifarch %ix86
%define module_version	390.129
%endif
%define module_release	alt1
%define flavour		un-def
%define karch %ix86 x86_64

%setup_kernel_module %flavour
%define module_srcver	%(echo %module_version | tr -d .)
%define xorg_ver %{get_version xorg-server}
%if "%xorg_ver" == ""
%define xorg_ver %{get_version xorg-x11-server}
%endif
%nvIF_ver_lt %xorg_ver 1.6
%define legacy1 71.86.13
%else
%define legacy1 %nil
%endif
%define legacy1_src %(echo %legacy1 | tr -d .)
%nvIF_ver_lt %xorg_ver 1.13
%define legacy2 96.43.23
%else
%define legacy2 %nil
%endif
%define legacy2_src %(echo %legacy2 | tr -d .)
%nvIF_ver_lt %xorg_ver 1.16
%define legacy3 173.14.39
%else
%define legacy3 %nil
%endif
%define legacy3_src %(echo %legacy3 | tr -d .)
%nvIF_ver_lt %xorg_ver 1.20
%define legacy4 304.137
%else
%define legacy4 %nil
%endif
%define legacy4_src %(echo %legacy4 | tr -d .)
%nvIF_ver_lt %xorg_ver 1.21
%define legacy5 340.107
%else
%define legacy5 %nil
%endif
%define legacy5_src %(echo %legacy5 | tr -d .)
%nvIF_ver_lt %xorg_ver 1.21
%define legacy6 390.129
%else
%define legacy6 %nil
%endif
%define legacy6_src %(echo %legacy6 | tr -d .)
%ifarch %ix86
%define legacy6 %nil
%endif
%define mod_ver_list %module_version %legacy1 %legacy2 %legacy3 %legacy4 %legacy5 %legacy6

%define module_dir /lib/modules/%kversion-%flavour-%krelease/nVidia
%define module_local_dir /lib/modules/nvidia
%define module_version_dir /lib/modules/%kversion-%flavour-%krelease/.versions
%define nvidia_workdir %_localstatedir/nvidia
%define module_ext .ko
%nvIF_ver_lt "%kversion" "2.5.0"
%define module_ext .o
%endif

Summary:	nVidia video card drivers
Name:		kernel-modules-%module_name-%flavour
Version:	%package_version
Release:	%module_release.%kcode.%kbuildrelease
License:	Proprietary
Group:		System/Kernel and hardware
URL:		http://www.nvidia.com

Packager:       Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveArch: %karch

BuildRequires(pre): rpm-build-kernel xorg-x11-server
BuildRequires(pre): kernel-headers-modules-un-def
BuildRequires: rpm-utils
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name-%module_srcver
%if "%legacy1" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy1_src
%endif
%if "%legacy2" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy2_src
%endif
%if "%legacy3" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy3_src
%endif
%if "%legacy4" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy4_src
%endif
%if "%legacy5" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy5_src
%endif
%if "%legacy6" != "%nil"
BuildRequires: kernel-source-%module_name-%legacy6_src
%endif

Provides:  	kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: 	kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: 	kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Conflicts: modutils < 2.4.27-alt4

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Requires: kernel-modules-drm-%flavour = %kepoch%kversion-%krelease
Requires:       nvidia_glx_%module_version
%if "%legacy1" != "%nil"
Requires:       nvidia_glx_%legacy1
%endif
%if "%legacy2" != "%nil"
Requires:       nvidia_glx_%legacy2
%endif
%if "%legacy3" != "%nil"
Requires:       nvidia_glx_%legacy3
%endif
%if "%legacy4" != "%nil"
Requires:       nvidia_glx_%legacy4
%endif
%if "%legacy5" != "%nil"
Requires:       nvidia_glx_%legacy5
%endif
%if "%legacy6" != "%nil"
Requires:       nvidia_glx_%legacy6
%endif

%description
nVidia video card drivers that provide 3d and 2d graphics support for XFree86
Xserver.


%prep
%setup -cT
for ver in %mod_ver_list
do
    sffx=`echo "$ver"| sed -e "s|\.||g"`
    rm -rf kernel-source-%module_name-$sffx
    tar -jxvf %_usrsrc/kernel/sources/kernel-source-%module_name-$sffx.tar.bz2

    pushd kernel-source-%module_name-$sffx
    if [ -f Makefile.kbuild ] ; then
	rm -f makefile Makefile
	ln -s Makefile.kbuild Makefile
    fi
    popd
done


%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
for ver in %mod_ver_list
do
    sffx=`echo "$ver"| sed -e "s|\.||g"`
    pushd kernel-source-%module_name-$sffx
    INTO_KERNEL_SRCDIR=
    [ -d nvidia-modeset ] || \
	INTO_KERNEL_SRCDIR="-C %_usrsrc/linux-%kversion-%flavour"
    %make_build modules \
	$INTO_KERNEL_SRCDIR \
	M=$PWD \
	TEMP_DIR=$PWD/ \
	ARCH=%base_arch \
	SYSSRC=%_usrsrc/linux-%kversion-%flavour
	if [ -d uvm ] ; then
	    pushd uvm
	    cp -a ../Module.symvers .
	    %make_build modules \
		$INTO_KERNEL_SRCDIR \
		M=$PWD \
		TEMP_DIR=$PWD/ \
		ARCH=%base_arch \
		SYSSRC=%_usrsrc/linux-%kversion-%flavour
	    popd
	fi
    popd
done

%install
mkdir -p %buildroot/%module_dir
mkdir -p %buildroot/%module_local_dir
mkdir -p %buildroot/%module_version_dir
mkdir -p %buildroot/%nvidia_workdir

for ver in %mod_ver_list
do
    sffx=`echo "$ver"| sed -e "s|\.||g"`
    pushd kernel-source-%module_name-$sffx
    install -p -m644 %module_name%module_ext %buildroot/%module_local_dir/%kversion-%flavour-%krelease-$ver
    [ -e %modesetmodule_name%module_ext ] &&
	install -p -m644 %modesetmodule_name%module_ext %buildroot/%module_local_dir/modeset-%kversion-%flavour-%krelease-$ver
    [ -e %drmmodule_name%module_ext ] &&
	install -p -m644 %drmmodule_name%module_ext %buildroot/%module_local_dir/drm-%kversion-%flavour-%krelease-$ver
    [ -e uvm/%uvmmodule_name%module_ext ] &&
	install -p -m644 uvm/%uvmmodule_name%module_ext %buildroot/%module_local_dir/uvm-%kversion-%flavour-%krelease-$ver
    [ -e %uvmmodule_name%module_ext ] &&
	install -p -m644 %uvmmodule_name%module_ext    %buildroot/%module_local_dir/uvm-%kversion-%flavour-%krelease-$ver
    popd
done
# workaround agains absent uvm module
if ! [ -e %buildroot/%module_local_dir/uvm-%kversion-%flavour-%krelease-%module_version ] ; then
    LAST_UVM_MOD_PATH=`ls -1d %buildroot/%module_local_dir/uvm-* 2>/dev/null | sort -r | head -n1`
    if [ -n "$LAST_UVM_MOD_PATH" ] ; then
	LAST_UVM_MOD_FILE=`basename $LAST_UVM_MOD_PATH`
	ln -s `relative %module_local_dir/$LAST_UVM_MOD_FILE %module_local_dir/uvm-%kversion-%flavour-%krelease-%module_version` %buildroot/%module_local_dir/uvm-%kversion-%flavour-%krelease-%module_version
    else
	ln -s `relative %module_local_dir/%kversion-%flavour-%krelease-%module_version %module_local_dir/uvm-%kversion-%flavour-%krelease-%module_version` %buildroot/%module_local_dir/uvm-%kversion-%flavour-%krelease-%module_version
    fi
fi

echo -n "%module_version" >%buildroot/%nvidia_workdir/%kversion-%flavour-%krelease
ln -s `relative %nvidia_workdir/%kversion-%flavour-%krelease %module_version_dir/%module_name` %buildroot/%module_version_dir/%module_name
ln -s nvidia %buildroot/%module_version_dir/%modesetmodule_name
ln -s nvidia %buildroot/%module_version_dir/%drmmodule_name
ln -s nvidia %buildroot/%module_version_dir/%uvmmodule_name
ln -s `relative %module_local_dir/%kversion-%flavour-%krelease-%module_version         %module_dir/%module_name%module_ext`    %buildroot/%module_dir/%module_name%module_ext
ln -s `relative %module_local_dir/modeset-%kversion-%flavour-%krelease-%module_version %module_dir/%modesetmodule_name%module_ext` %buildroot/%module_dir/%modesetmodule_name%module_ext
ln -s `relative %module_local_dir/drm-%kversion-%flavour-%krelease-%module_version %module_dir/%drmmodule_name%module_ext` %buildroot/%module_dir/%drmmodule_name%module_ext
ln -s `relative %module_local_dir/uvm-%kversion-%flavour-%krelease-%module_version     %module_dir/%uvmmodule_name%module_ext` %buildroot/%module_dir/%uvmmodule_name%module_ext


%post
# switch nvidia driver and libraries
if [ -z "$DURING_INSTALL" ]; then
    if [ "`uname -r`" == "%kversion-%flavour-%krelease" ] ; then
	X11PRESETDRV=`which x11presetdrv 2>/dev/null`
	if [ -n "$X11PRESETDRV" ]; then
	    $X11PRESETDRV ||:
	else
	    echo "Warning! x11presetdrv program not found!" >&2
	fi
    fi
fi

%postun
if [ -z "$DURING_INSTALL" ]; then
    if [ "`uname -r`" == "%kversion-%flavour-%krelease" ] ; then
	X11PRESETDRV=`which x11presetdrv 2>/dev/null`
	if [ -n "$X11PRESETDRV" ]; then
	    $X11PRESETDRV ||:
	else
	    echo "Warning! x11presetdrv program not found!" >&2
	fi
    fi
fi

%files
%defattr(644,root,root,755)
%module_dir
%module_version_dir/%module_name
%module_version_dir/%modesetmodule_name
%module_version_dir/%drmmodule_name
%module_version_dir/%uvmmodule_name
%module_local_dir/%kversion-%flavour-%krelease-*
%module_local_dir/modeset-%kversion-%flavour-%krelease-*
%module_local_dir/drm-%kversion-%flavour-%krelease-*
%module_local_dir/uvm-%kversion-%flavour-%krelease-*
%config(noreplace) %nvidia_workdir/%kversion-%flavour-%krelease

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Fri Sep 20 2019 Sergey V Turchin <zerg at altlinux dot org> 430.50-alt1
- new release (430.50)

* Thu Aug 15 2019 Sergey V Turchin <zerg at altlinux dot org> 430.40-alt1
- new releases (430.40, 390.129)

* Fri Jul 12 2019 Sergey V Turchin <zerg at altlinux dot org> 430.34-alt1
- new release (430.34)

* Tue Jun 11 2019 Sergey V Turchin <zerg at altlinux dot org> 430.26-alt1
- new release (430.26)

* Thu Mar 14 2019 Sergey V Turchin <zerg at altlinux dot org> 410.104-alt1
- new releases (410.104, 390.116)

* Thu Jan 10 2019 Sergey V Turchin <zerg at altlinux dot org> 410.93-alt1
- new release (410.93 for x86_64)

* Fri Nov 09 2018 Sergey V Turchin <zerg at altlinux dot org> 410.78-alt2
- new release (410.78 for x86_64)

* Fri Nov 09 2018 Sergey V Turchin <zerg at altlinux dot org> 410.73-alt2
- new release (410.73 for x86_64)

* Mon Sep 10 2018 Sergey V Turchin <zerg at altlinux dot org> 390.87-alt1
- new release (390.87)

* Mon Aug 20 2018 Sergey V Turchin <zerg at altlinux dot org> 390.77-alt2
- add karch specsubst

* Fri Aug 17 2018 Sergey V Turchin <zerg at altlinux dot org> 390.77-alt1
- new release (390.77)

* Thu Jun 07 2018 Sergey V Turchin <zerg at altlinux dot org> 390.67-alt1
- new releases (390.67, 340.107)

* Tue May 22 2018 Sergey V Turchin <zerg at altlinux dot org> 390.59-alt1
- new release (390.59)


* Mon Apr 16 2018 Sergey V Turchin <zerg at altlinux dot org> 390.48-alt2
- fix for 4.16 kernel

* Mon Apr 02 2018 Sergey V Turchin <zerg at altlinux dot org> 390.48-alt1
- new release (390.48)

* Mon Feb 12 2018 Sergey V Turchin <zerg at altlinux dot org> 390.25-alt1
- new release (390.25)

* Mon Jan 29 2018 Sergey V Turchin <zerg at altlinux dot org> 384.111-alt2
- new legacy release (340.106)

* Thu Dec 14 2017 Sergey V Turchin <zerg at altlinux dot org> 384.111-alt1
- new release (384.111)

* Thu Dec 14 2017 Sergey V Turchin <zerg at altlinux dot org> 384.98-alt2
- add fixes for lagacy drivers

* Mon Dec 04 2017 Sergey V Turchin <zerg at altlinux dot org> 384.98-alt1
- new release (384.98)

* Tue Aug 08 2017 Sergey V Turchin <zerg at altlinux dot org> 384.90-alt1
- new releases (384.90, 340.104, 304.137)

* Tue Aug 08 2017 Sergey V Turchin <zerg at altlinux dot org> 375.82-alt1
- new release (375.82)

* Wed May 10 2017 Sergey V Turchin <zerg at altlinux dot org> 375.66-alt1
- new release (375.66)

* Wed Mar 15 2017 Sergey V Turchin <zerg at altlinux dot org> 375.39-alt2
- new releases (340.102, 304.135)

* Mon Feb 20 2017 Sergey V Turchin <zerg at altlinux dot org> 375.39-alt1
- new release (375.39)

* Tue Jan 17 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 375.26-alt2
- use kernel gcc

* Fri Dec 16 2016 Sergey V Turchin <zerg at altlinux dot org> 375.26-alt1..
- new releases (375.26, 340.101, 304.134)

* Tue Nov 29 2016 Sergey V Turchin <zerg at altlinux dot org> 375.20-alt1..
- new release (375.20)

* Mon Nov 21 2016 Sergey V Turchin <zerg at altlinux dot org> 367.57-alt2..
- downgrade 304.132 to 304.131 (ALT#32772)

* Thu Oct 13 2016 Sergey V Turchin <zerg at altlinux dot org> 367.57-alt1..
- new release (367.57)

* Wed Sep 28 2016 Sergey V Turchin <zerg at altlinux dot org> 367.44-alt2..
- new releases (304.132,340.98)

* Tue Aug 30 2016 Sergey V Turchin <zerg at altlinux dot org> 367.44-alt1..
- new release (367.44)

* Mon Jul 18 2016 Sergey V Turchin <zerg at altlinux dot org> 367.35-alt1..
- new release (367.35)

* Fri Jul 01 2016 Sergey V Turchin <zerg at altlinux dot org> 367.27-alt1..
- new release (367.27)

* Mon May 30 2016 Sergey V Turchin <zerg at altlinux dot org> 361.45.11-alt2..
- rebuild with fixed 304.131 module (ALT#32154)

* Fri May 27 2016 Sergey V Turchin <zerg at altlinux dot org> 361.45.11-alt1..
- new release (361.45.11)

* Fri Apr 22 2016 Sergey V Turchin <zerg at altlinux dot org> 361.42-alt3..
- workaround agains absent uvm module

* Fri Apr 22 2016 Sergey V Turchin <zerg at altlinux dot org> 361.42-alt2..
- make default symlinks relative

* Fri Apr 22 2016 Sergey V Turchin <zerg at altlinux dot org> 361.42-alt1..
- new release (361.42)
- build uvm module

* Fri Mar 04 2016 Sergey V Turchin <zerg at altlinux dot org> 361.28-alt1..
- new release (361.28)

* Thu Jan 28 2016 Sergey V Turchin <zerg at altlinux dot org> 352.79-alt1..
- new release (352.79)

* Tue Nov 24 2015 Sergey V Turchin <zerg at altlinux dot org> 352.63-alt1..
- new release (352.63)

* Mon Nov 23 2015 Sergey V Turchin <zerg at altlinux dot org> 352.55-alt2..
- new releases (304.131,304.96)

* Mon Oct 19 2015 Sergey V Turchin <zerg at altlinux dot org> 352.55-alt1..
- new release (352.55)

* Wed Sep 30 2015 Sergey V Turchin <zerg at altlinux dot org> 352.41-alt3..
- ignore CONFIG_X86_DMA_REMAP

* Thu Sep 03 2015 Sergey V Turchin <zerg at altlinux dot org> 352.41-alt2..
- new release (340.93)

* Wed Sep 02 2015 Sergey V Turchin <zerg at altlinux dot org> 352.41-alt1..
- new releases (352.41, 304.128)

* Wed Jul 29 2015 Sergey V Turchin <zerg at altlinux dot org> 346.87-alt1..
- new release (346.87)

* Mon Jun 29 2015 Sergey V Turchin <zerg at altlinux dot org> 346.82-alt1..
- new release (346.82)

* Fri May 15 2015 Sergey V Turchin <zerg at altlinux dot org> 346.72-alt1..
- new release (346.72)

* Wed Apr 08 2015 Sergey V Turchin <zerg at altlinux dot org> 346.59-alt1..
- new release (346.59)

* Tue Mar 10 2015 Sergey V Turchin <zerg at altlinux dot org> 346.47-alt1..
- new release (346.47)

* Mon Feb 09 2015 Sergey V Turchin <zerg at altlinux dot org> 346.35-alt2..
- new release (340.76)

* Thu Jan 22 2015 Sergey V Turchin <zerg at altlinux dot org> 346.35-alt1..
- new release (346.35)

* Tue Dec 09 2014 Sergey V Turchin <zerg at altlinux dot org> 340.65-alt3..
- new release (340.65)

* Tue Dec 09 2014 Sergey V Turchin <zerg at altlinux dot org> 340.58-alt2..
- new release (304.125)

* Mon Nov 10 2014 Sergey V Turchin <zerg at altlinux dot org> 340.58-alt1..
- new release (340.58)

* Mon Oct 06 2014 Sergey V Turchin <zerg at altlinux dot org> 340.46-alt1..
- new release (340.46)

* Tue Aug 19 2014 Sergey V Turchin <zerg at altlinux dot org> 340.32-alt1..
- new release (340.32)

* Fri Jul 18 2014 Sergey V Turchin <zerg at altlinux dot org> 340.24-alt1..
- new releases (340.24, 304.123)

* Mon Jul 07 2014 Sergey V Turchin <zerg at altlinux dot org> 331.89-alt1..
- new release (331.89)

* Fri May 23 2014 Sergey V Turchin <zerg at altlinux dot org> 331.79-alt1..
- new release (331.79)

* Wed Apr 30 2014 Sergey V Turchin <zerg at altlinux dot org> 331.67-alt1..
- new release (331.67)

* Tue Mar 18 2014 Sergey V Turchin <zerg at altlinux dot org> 331.49-alt2..
- new release (304.121)

* Wed Feb 19 2014 Sergey V Turchin <zerg at altlinux dot org> 331.49-alt1..
- new release (331.49)

* Wed Jan 29 2014 Sergey V Turchin <zerg at altlinux dot org> 331.38-alt2..
- new release (304.119)

* Tue Jan 14 2014 Sergey V Turchin <zerg at altlinux dot org> 331.38-alt1..
- new release (331.38)

* Fri Jan 10 2014 Sergey V Turchin <zerg at altlinux dot org> 331.20-alt2..
- new releases (173.14.39, 304.117) with XOrg 1.15 support

* Tue Nov 19 2013 Sergey V Turchin <zerg at altlinux dot org> 331.20-alt1..
- new release (331.20)

* Thu Nov 07 2013 Sergey V Turchin <zerg at altlinux dot org> 319.72-alt1..
- new releases (319.72, 304.116, 173.14.38)

* Fri Oct 04 2013 Sergey V Turchin <zerg at altlinux dot org> 319.60-alt1..
- new release (319.60)

* Mon Sep 02 2013 Sergey V Turchin <zerg at altlinux dot org> 319.49-alt1..
- new releases (319.49 and 304.108)

* Wed Jun 26 2013 Sergey V Turchin <zerg at altlinux dot org> 319.32-alt1..
- new release (319.32)

* Fri May 24 2013 Sergey V Turchin <zerg at altlinux dot org> 319.23-alt1..
- new release (319.23)

* Thu May 23 2013 Sergey V Turchin <zerg at altlinux dot org> 319.17-alt2..
- require kernel-modules-drm

* Tue May 14 2013 Sergey V Turchin <zerg at altlinux dot org> 319.17-alt1..
- new release (319.17)

* Wed Apr 03 2013 Sergey V Turchin <zerg at altlinux dot org> 310.44-alt1..
- new releases (310.44 and 304.88)
- security fixes:
  CVE-2013-0131

* Mon Mar 11 2013 Sergey V Turchin <zerg at altlinux dot org> 310.40-alt1
- new release (310.40 and 173.14.37 with xorg-server-1.14 support)

* Thu Mar 07 2013 Sergey V Turchin <zerg at altlinux dot org> 310.32-alt2
- new release (304.84 with xorg-server-1.14 support)

* Wed Jan 23 2013 Sergey V Turchin <zerg at altlinux dot org> 310.32-alt1
- new release (310.32)

* Fri Dec 07 2012 Sergey V Turchin <zerg at altlinux dot org> 310.19-alt2
- remove *_kernel_modules macroses using
- remove x11setupdrv using

* Mon Nov 19 2012 Sergey V Turchin <zerg at altlinux dot org> 310.19-alt1
- new release (310.19)
- add new legacy branch (304.64)
- fix 173.X xorg dependency

* Thu Nov 08 2012 Sergey V Turchin <zerg at altlinux dot org> 304.64-alt1
- new release (304.64)

* Mon Oct 29 2012 Sergey V Turchin <zerg at altlinux dot org> 304.60-alt1
- new release (304.60)

* Tue Oct 02 2012 Sergey V Turchin <zerg at altlinux dot org> 304.51-alt2
- new releases 173.14.35 and 96.43.23 with xorg-server-1.12 support)

* Tue Oct 02 2012 Sergey V Turchin <zerg at altlinux dot org> 304.51-alt1
- new release (304.51)

* Wed Aug 29 2012 Sergey V Turchin <zerg at altlinux dot org> 304.43-alt1
- new release (304.43)

* Tue Aug 14 2012 Sergey V Turchin <zerg at altlinux dot org> 304.37-alt1
- new release (304.37)

* Thu Jul 12 2012 Sergey V Turchin <zerg at altlinux dot org> 302.17-alt1
- new release (302.17)

* Thu Jun 14 2012 Sergey V Turchin <zerg at altlinux dot org> 295.59-alt1
- new release (295.59)

* Fri Jun 08 2012 Sergey V Turchin <zerg at altlinux dot org> 295.53-alt3
- fix requires

* Thu Jun 07 2012 Sergey V Turchin <zerg at altlinux dot org> 295.53-alt2
- new release (173.14.35 with xorg-server-1.12 support)

* Thu May 17 2012 Sergey V Turchin <zerg at altlinux dot org> 295.53-alt1
- new release (295.53)

* Thu May 03 2012 Sergey V Turchin <zerg at altlinux dot org> 295.49-alt1
- new release (295.49)

* Wed Apr 11 2012 Sergey V Turchin <zerg at altlinux dot org> 295.40-alt1
- new release (295.40)
- fixed CVE-2012-0946

* Mon Mar 26 2012 Sergey V Turchin <zerg at altlinux dot org> 295.33-alt1
- new release (295.33)

* Wed Feb 15 2012 Sergey V Turchin <zerg at altlinux dot org> 295.20-alt1
- new release (295.20)

* Wed Nov 23 2011 Sergey V Turchin <zerg at altlinux dot org> 290.10-alt1
- new release (290.10)

* Tue Oct 04 2011 Sergey V Turchin <zerg at altlinux dot org> 285.05.09-alt1
- new pre-release (285.05.09)

* Wed Aug 03 2011 Sergey V Turchin <zerg at altlinux dot org> 280.13-alt1
- new release (280.13)
- add ExclusiveArch workaround for std-pae

* Tue Aug 02 2011 Sergey V Turchin <zerg at altlinux dot org> 275.21-alt1
- new releases (275.21, 173.14.31, 96.43.20)

* Fri Jul 01 2011 Anton Protopopov <aspsk@altlinux.org> 275.09.07-alt2
- Use @ kernelarch @ macro in ExclusiveArch

* Wed Jun 15 2011 Sergey V Turchin <zerg at altlinux dot org> 275.09.07-alt1
- new release (275.09.07)

* Mon May 23 2011 Sergey V Turchin <zerg at altlinux dot org> 270.41.19-alt1
- new release (270.41.19)

* Mon Apr 25 2011 Sergey V Turchin <zerg at altlinux dot org> 270.41.06-alt1
- new releases (270.41.06, 173.14.30)

* Wed Apr 13 2011 Sergey V Turchin <zerg at altlinux dot org> 270.41.03-alt1
- new release (270.41.03)

* Mon Mar 14 2011 Sergey V Turchin <zerg at altlinux dot org> 260.19.44-alt1
- new release (260.19.44)

* Tue Jan 25 2011 Sergey V Turchin <zerg at altlinux dot org> 260.19.36-alt1
- new release (260.19.36)

* Fri Dec 24 2010 Sergey V Turchin <zerg at altlinux dot org> 260.19.29-alt1
- new release (260.19.29)

* Wed Nov 10 2010 Sergey V Turchin <zerg at altlinux dot org> 260.19.21-alt1
- new release (260.19.21)

* Wed Nov 03 2010 Sergey V Turchin <zerg at altlinux dot org> 260.19.12-alt2
- new release (96.43.19) with xorg-1.9 support

* Mon Oct 25 2010 Sergey V Turchin <zerg at altlinux dot org> 260.19.12-alt1
- new release (260.19.12)

* Fri Oct 01 2010 Sergey V Turchin <zerg at altlinux dot org> 256.53-alt4
- fix to build

* Fri Oct 01 2010 Sergey V Turchin <zerg at altlinux dot org> 256.53-alt3
- new release (173.14.28)

* Fri Oct 01 2010 Sergey V Turchin <zerg at altlinux dot org> 256.53-alt2
- don't build xorg incompatible modules

* Wed Sep 01 2010 Sergey V Turchin <zerg at altlinux dot org> 256.53-alt1
- new release (256.53)

* Tue Aug 31 2010 Sergey V Turchin <zerg at altlinux dot org> 256.52-alt1
- new release (256.52)

* Thu Aug 12 2010 Sergey V Turchin <zerg at altlinux dot org> 256.44-alt1
- new release (256.44)

* Mon Jul 19 2010 Sergey V Turchin <zerg at altlinux dot org> 256.35-alt2
- new releases (173.14.27, 96.43.18)

* Wed Jul 14 2010 Sergey V Turchin <zerg at altlinux dot org> 256.35-alt1
- new release (256.35)

* Tue Jun 14 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.31-alt1
- new release (195.36.31)

* Mon Apr 26 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.24-alt1
- new releases (195.36.24, 96.43.17)

* Thu Mar 18 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.15-alt1
- new release (195.36.15)

* Tue Mar 02 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.08-alt1
- new release (195.36.08)

* Thu Feb 18 2010 Sergey V Turchin <zerg at altlinux dot org> 195.36.03-alt1
- new beta release (195.36.03)
- new releases (173.14.25, 96.43.16)

* Thu Dec 17 2009 Sergey V Turchin <zerg at altlinux dot org> 190.53-alt1
- new releases (190.53, 173.14.22, 96.43.14)

* Thu Dec 17 2009 Sergey V Turchin <zerg at altlinux dot org> 190.42-alt2
- remove ldconfig from %%post

* Wed Oct 28 2009 Sergey V Turchin <zerg at altlinux dot org> 190.42-alt1
- new release (190.42)

* Tue Sep 08 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.36-alt2
- don't package legacy 71.86.11 because incompatible with current XOrg

* Mon Aug 24 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.36-alt1
- new release (185.18.36)

* Tue Aug 04 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.31-alt1
- new release (185.18.31)

* Thu Jul 02 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.14-alt3
- new legacy pre-releases (71.86.11, 96.43.13, 173.14.20)

* Tue Jun 23 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.14-alt2
- new legacy release candidates (71.86.10, 96.43.12, 173.14.19)

* Mon Jun 08 2009 Sergey V Turchin <zerg at altlinux dot org> 185.18.14-alt1
- new release (185.18.14)

* Mon Jun 08 2009 Sergey V Turchin <zerg at altlinux dot org> 180.60-alt1
- new release (180.60)

* Fri Apr 24 2009 Sergey V Turchin <zerg at altlinux dot org> 180.51-alt1
- new release (180.51)

* Thu Apr 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.44-alt1
- new release (180.44)

* Fri Mar 13 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt2
- new legacy release (173.14.18)

* Thu Mar 12 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt1
- revert to stable 180.29

* Wed Mar 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.37-alt1
- new beta (180.37)

* Tue Mar 10 2009 Sergey V Turchin <zerg at altlinux dot org> 180.35-alt2
- new legacy release (71.86.09)

* Tue Mar 03 2009 Sergey V Turchin <zerg at altlinux dot org> 180.35-alt1
- new beta (180.35)

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt1
- new release (180.29)
- new legacy betas (173.14.17, 96.43.11, 71.86.08)
- don't warn if x11setupdrv not found
- don't use deprecated macroses
- always execute %%post_kernel_modules macros

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt1
- new release (180.22)

* Mon Nov 17 2008 Sergey V Turchin <zerg at altlinux dot org> 177.82-alt1
- new release (177.82)
- new legacy betas (173.14.15, 96.43.09, 71.86.07)

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 177.80-alt1
- new release (177.80)
- 3 legacy (173.14.12, 96.43.07, 71.86.06)

* Tue Aug 05 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.12-alt1
- new release (173.14.12)

* Tue Jul 29 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.09-alt1
- new release (173.14.09)
- new legacy releases(96.43.07, 71.86.06)

* Fri May 30 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.05-alt1
- new release (173.14.05)

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 169.12-alt1
- new release (169.12)

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 169.09-alt2
- new legacy releases(96.43.05, 71.86.04)

* Fri Jan 25 2008 Sergey V Turchin <zerg at altlinux dot org> 169.09-alt1
- new release (169.09)

* Wed Dec 26 2007 Sergey Vlasov <vsu@altlinux.ru> 169.07-alt2
- Restructure the spec file to avoid %%if around the "Version:" line (required
  to work properly with gear, which does not support RPM conditionals).

* Fri Dec 21 2007 Sergey V Turchin <zerg at altlinux dot org> 169.07-alt1
- new release (169.07)

* Mon Oct 01 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt3
- new legacy releases(96.43.01, 71.86.01)

* Tue Sep 25 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt2
- bump release to rebuild

* Fri Sep 21 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt1
- new release (100.14.19)

* Fri Sep 21 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt3
- fix kernel modile filename

* Tue Sep 18 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt2
- use new nvidia drivers packaging scheme
- include legacy kernel modules

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt1
- new release (100.14.11)

* Sat Jun 09 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.09-alt1
- new release (100.14.09)

* Thu Mar 15 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9755-alt1
- new release (9755)

* Wed Feb 21 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9746-alt1
- new release (9746)

* Mon Jan 29 2007 Sergey Vlasov <vsu@altlinux.ru> 1.0.9631-alt2
- Updated dependencies: replaced "Prereq: modutils >= 2.4.27-alt4" with
  "Conflicts: modutils < 2.4.27-alt4" (the dependency on modutils or
  module-init-tools already comes indirectly through kernel-image-%%flavour).

* Thu Dec 07 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9631-alt1
- new release (9631)

* Thu Nov 09 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9629-alt1
- new release (9629)

* Fri Nov 03 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9626-alt1
- new release (9626)

* Wed Oct 25 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8776-alt1
- new release (8776)

* Wed Sep 06 2006 L.A. Kostis <lakostis@altlinux.org> 1.0.8774-alt2
- make build independed from host-arch.

* Fri Sep 01 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8774-alt1
- new release (8774)

* Wed May 24 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8762-alt1
- new release (8762)

* Wed Apr 12 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8756-alt1
- new release (8756)
- remove NVIDIA_kernel-1.0-8178-U012206.diff (merged by upstream)

* Sat Mar 18 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.8178-alt2
- Added NVIDIA_kernel-1.0-8178-U012206.diff update patch from the nvnews.net
  forum (fixes several problems with newer kernels, including compilation
  failure with 2.6.16).

* Mon Dec 26 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.8178-alt1
- new release (8178)

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7676-alt1
- new release (7676)

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7667-alt1
- new release (7667)

* Tue Jun 21 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.7174-alt3
- Require modutils >= 2.4.27-alt4 because of .versions/nvidia (#7151).

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt2
- add file with module version

* Thu Apr 07 2005 Anton Farygin <rider@altlinux.ru> 1.0.7174-alt1
- new release (7174)

* Mon Mar 14 2005 Sergey Vlasov <vsu@altlinux.ru> 1.0.7167-alt1
- New release (7167).
- Removed obsolete compatibility patches.

* Wed Dec 29 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6629-alt2
- Added patches for compatibility with kernel 2.6.10 (Patch2, Patch3).

* Sun Dec 26 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6629-alt1
- New release (6629).

* Wed Oct 20 2004 Anton Farygin <rider@altlinux.ru> 1.0.6111-alt4
- fixed unreslved symbols with kernel 2.6.9

* Sun Oct 17 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6111-alt3
- Rebuild for kernel 2.4.27.

* Mon Sep 06 2004 Anton Farygin <rider@altlinux.ru> 1.0.6111-alt2
- License fixed

* Tue Aug 17 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6111-alt1
- New release (6111).

* Tue Aug 03 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6106-alt2
- Use %%post_kernel_modules and %%postun_kernel_modules macros in scripts.

* Fri Jul 02 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.6106-alt1
- New release (6106).

* Thu May 13 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.5336-alt2
- Rebuild for kernel 2.4.26.

* Mon Mar 22 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.5336-alt1
- New release (5336).
- Removed AGP fix patch (not needed for 5336).
- Modified build for new makefiles.

* Fri Feb 27 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.5328-alt5
- Updated for the new compiler version selection scheme (GCC_VERSION).

* Wed Feb 18 2004 Anton Farygin <rider@altlinux.ru> 1.0.5328-alt4
- rebuild for 2.6.3 (increment release without changes)

* Mon Feb 16 2004 Anton Farygin <rider@altlinux.ru> 1.0.5328-alt3
- added build scripts for kernel 2.6 

* Thu Jan 15 2004 Sergey Vlasov <vsu@altlinux.ru> 1.0.5328-alt2
- Added patch to work around problems with AGP support (part of the Linux-2.6
  adaptation patch from www.minion.de).

* Mon Dec 22 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.5328-alt1
- New release (5328).

* Tue Dec 16 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.4496-alt12
- Fixed compiler selection.

* Fri Nov 28 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.4496-alt11
- Added Provides/Conflicts to make sure that only one version of the package
  can be installed for each kernel version.

* Tue Nov 18 2003 Sergey Vlasov <vsu@altlinux.ru> 1.0.4496-alt10
- Fixed spec file name.
- Avoid %%postun failure when this package is removed after
  kernel-image-%%flavour (currently rpm cannot prevent this).

* Sat Sep 06 2003 Anton Farygin <rider@altlinux.ru> 1.0.4496-alt9
- /usr/include replaces to macros _includedir
- build requires fix

* Tue Aug 26 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt8
- rebuilt with 2.4.21rel-alt14

* Fri Aug 15 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt7
- rebuilt with 2.4.21rel-alt13

* Wed Aug 13 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt6
- rebuilt with 2.4.21rel-alt12

* Tue Aug 12 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt5
- rebuilt with 2.4.21rel-alt11

* Mon Aug 11 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt4
- rebuilt with 2.4.21rel-alt10

* Thu Aug 07 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt3
- rebuilt with 2.4.21rel-alt9

* Wed Aug 06 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt2
- rebuilt with 2.4.21rel-alt8

* Wed Jul 30 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4496-alt1
- new release (4496)
- rebuilt with 2.4.21rel-alt7

* Thu Jul 17 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt5
- rebuilt with 2.4.21rel-alt6

* Wed Jul 16 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt4
- rebuilt with 2.4.21rel-alt5

* Mon Jul 07 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt3
- rebuilt with 2.4.21rel alt3 kernel

* Wed Jul 02 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt2
- add provides NVIDIA_kernel = %version

* Sat Jun 21 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4363-alt1
- rebuilt with 2.4.21rel kernel

* Thu Apr 10 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4349-alt2
- Provides NVIDIA_kernel for now.

* Sun Mar 23 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4349-alt1
- Initial release


