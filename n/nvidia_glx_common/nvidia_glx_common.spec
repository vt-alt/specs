%define Nif_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define Nif_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define Nif_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define Nif_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%define tbname         NVIDIA-Linux-x86
%ifarch x86_64
%define tbname         NVIDIA-Linux-x86_64
%endif
%define virtual_pkg_name NVIDIA_GLX
%define bin_pkg_name     nvidia_glx
%define module_name    nvidia
%define dirsuffix -common

# version-release

%define nv_version 430
%define nv_release 40
%define nv_minor %nil
%define pkg_rel alt216
%define set_gl_nvidia_ver 1.1.1

%define tbver %{nv_version}.%{nv_release}.%{nv_minor}
%if "%nv_minor" == "%nil"
%define tbver %{nv_version}.%{nv_release}
%endif
%define module_version	%nv_version%nv_release%nv_minor
%define module_release	%pkg_rel

%define myGroup System/Kernel and hardware
%define mySummary This is common package for usability NVIDIA drivers.
%define mySummaryRu Пакет для совместимости драйверов NVIDIA.

%define module_local_dir /lib/modules/nvidia
%define mods /modules
%define exts /modules/extensions
%define drvs /modules/drivers
%define x_etclib_sym_dir %_sysconfdir/X11/%_lib
%define nv_etclib_sym_dir %{x_etclib_sym_dir}_nvidia
%define nv_lib32_sym_dir %_sysconfdir/X11/lib_nvidia
%define xdrv_d /usr/libexec/X11/drv.d
%define xdrv_d_old /usr/X11R6/lib/drv.d
%define xdrv_pre_d /usr/libexec/X11/drvpre.d
%define xdrv_pre_d_old /usr/X11R6/lib/drvpre.d

%define xinf_dir %_datadir/hwdatabase/videoaliases/
%define nv_workdirdir %_localstatedir/nvidia
%define tls_lib_dir %_libdir
%define x11_lib_dir %_libdir
%define x11_lib_old /usr/X11R6/lib
%define x11_mod_dir /usr/%_lib/X11%mods
%define x11_mod_old /usr/X11R6/%_lib%mods
%define x11_drv_dir /usr/%_lib/X11%drvs
%define x11_drv_old /usr/%_lib/X11%drvs
%define x11_ext_dir /usr/%_lib/X11%exts
%define x11_ext_old /usr/X11R6/%_lib%exts
%define x11driver_dir %_libdir/X11
%define glvnddriver_dir %_libdir/glvnd
%define nv_lib_dir_prefix %_libdir/nvidia_
%define nv_lib_dir_prefix_old /usr/X11R6/%_lib/nvidia_
%define nv_lib_dir %nv_lib_dir_prefix%tbver

%add_findprov_lib_path %nv_lib_dir/*
%add_findreq_skiplist %_libdir/*
%add_findreq_skiplist %x11_lib_dir/*
%add_findreq_skiplist %x11_lib_old/*
%add_findreq_skiplist %_bindir/nvidia-bug-report*.sh

Name: nvidia_glx_common
%if "%nv_minor" == "%nil"
Version: %nv_version.%nv_release
%else
Version: %nv_version.%nv_release.%nv_minor
%endif
Release: %pkg_rel

Source: set_gl_nvidia-%set_gl_nvidia_ver.tar
Source1: alternate-install-present
Source2: nvidia-install-driver
Source3: nvidia-clean-driver

BuildRequires(pre): rpm-build-ubt
BuildRequires: libsysfs-devel
ExclusiveArch: %ix86 x86_64


Group: %myGroup
Summary: %mySummary
Summary(ru_RU.UTF-8): %mySummaryRu
Url: http://altlinux.ru/
License: GPLv2
#
Provides: %virtual_pkg_name = %version-%release
Obsoletes: %virtual_pkg_name < %version-%release
#
Conflicts: xorg-x11-mesagl <= 6.8.2-alt7
PreReq: libGL
Requires: apt-scripts-nvidia
Requires: /usr/bin/xsetup-monitor
Requires(post): x11presetdrv
# old
Conflicts: nvidia_glx_100.14.19-100.14.19 <= alt40
Conflicts: nvidia_glx_169.07-169.07 <= alt40
Conflicts: nvidia_glx_169.09-169.09 <= alt41
Conflicts: nvidia_glx_71.86.01-71.86.01 <= alt36
Conflicts: nvidia_glx_96.43.01-96.43.01 <= alt36
#
Conflicts: nvidia_glx_71.86.04-71.86.04 <= alt37
Conflicts: nvidia_glx_71.86.06-71.86.06 <= alt38
Conflicts: nvidia_glx_96.43.05-96.43.05 <= alt37
Conflicts: nvidia_glx_96.43.07-96.43.07 <= alt38
Conflicts: nvidia_glx_169.12-169.12 <= alt44
Conflicts: nvidia_glx_173.14.12-173.14.12 <= alt47
%description
This is common package for NVIDIA drivers.
%description -l ru_RU.UTF-8
Этот пакет нужен для совместимости при отсутствии
одной из компонент драйверов для NVIDIA.


%prep
%setup -T -c -n %tbname-%tbver%dirsuffix
cd %_builddir
cd %tbname-%tbver%dirsuffix
tar xvf %SOURCE0
pushd set_gl_nvidia*
cp settings.h.in settings.h

%define glvnd_scheme 0
%Nif_ver_gteq %ubt_id M90
%define glvnd_scheme 0
%else
%define glvnd_scheme -1
%endif
#Nif_ver_gteq %ubt_id M100
#define glvnd_scheme 1
#endif
sed -i "s|@GLVND_SCHEME@|%glvnd_scheme|" settings.h

sed -i "s|@DEFAULT_VERSION@|%version|" settings.h
sed -i "s|@X_ETCLIB_SYML_DIR@|%x_etclib_sym_dir|" settings.h
sed -i "s|@NV_ETCLIB_SYML_DIR@|%nv_etclib_sym_dir|" settings.h
sed -i "s|@TLS_LIB_DIR@|%tls_lib_dir|" settings.h

sed -i "s|@XLIB_DIR@|%x11_lib_dir|" settings.h
sed -i "s|@XLIB_DIR_OLD@|%x11_lib_old|" settings.h

sed -i "s|@XMOD_DIR@|%x11_mod_dir|" settings.h
sed -i "s|@XMOD_DIR_OLD@|%x11_mod_old|" settings.h

sed -i "s|@XDRV_DIR@|%x11_drv_dir|" settings.h
sed -i "s|@XDRV_DIR_OLD@|%x11_drv_old|" settings.h

sed -i "s|@XEXT_DIR@|%x11_ext_dir|" settings.h
sed -i "s|@XEXT_DIR_OLD@|%x11_ext_old|" settings.h

sed -i "s|@X_DRV_DIR@|%x11driver_dir|" settings.h
sed -i "s|@NV_DRV_DIR_PREFIX@|%nv_lib_dir_prefix|" settings.h
sed -i "s|@NV_DRV_DIR_PREFIX_OLD@|%nv_lib_dir_prefix_old|" settings.h

sed -i "s|@XINF_DIR@|%xinf_dir|" settings.h
popd


%build
%add_optflags -pedantic
#make OPTFLAGS="%optflags -Wl,--hash-style=sysv" -C set_gl_nvidia*
make OPTFLAGS="%optflags" LDFLAGS="-L%_libdir" -C set_gl_nvidia*
echo "void ___some_unused_function_to_fill_sources___() {}" >nvidianull.c
gcc %optflags -c nvidianull.c -o nvidianull.o
#ld --hash-style=sysv --shared nvidianull.o -o libnvidianull.so
ld --shared nvidianull.o -o libnvidianull.so


%install
%__mkdir_p %buildroot/%module_local_dir
%__mkdir_p %buildroot/%_sbindir
%__mkdir_p %buildroot/%tls_lib_dir
%__mkdir_p %buildroot/%nv_lib_dir
%__mkdir_p %buildroot/%x11_mod_dir
#%__mkdir_p %buildroot/%x11_mod_old
%__mkdir_p %buildroot/%x11_drv_dir
#%__mkdir_p %buildroot/%x11_drv_old
%__mkdir_p %buildroot/%x11_ext_dir
#%__mkdir_p %buildroot/%x11_ext_old
%__mkdir_p %buildroot/%x_etclib_sym_dir
%__mkdir_p %buildroot/%nv_etclib_sym_dir
%__mkdir_p %buildroot/%nv_lib32_sym_dir
%__mkdir_p %buildroot/%xdrv_d
#%__mkdir_p %buildroot/%xdrv_d_old
%__mkdir_p %buildroot/%xdrv_pre_d
%__mkdir_p %buildroot/%xinf_dir
%__mkdir_p %buildroot/%nv_workdirdir
%__mkdir_p %buildroot/%_datadir/nvidia
%__mkdir_p %buildroot/%x11_lib_dir/vdpau

# prompt user to don't use nvidia-installer
mkdir -p %buildroot/usr/lib/nvidia/
install -m 0644 %SOURCE1 %buildroot/usr/lib/nvidia/
mkdir -p %buildroot/%_bindir/
install -m 0755 %SOURCE2 %buildroot/%_bindir/
install -m 0755 %SOURCE3 %buildroot/%_bindir/

%__install -m 0755 set_gl_nvidia*/nvidia %buildroot/%xdrv_d/nvidia
#%__ln_s ../../../..%xdrv_d/nvidia %buildroot/%xdrv_d_old/nvidia
%__install -m 0755 set_gl_nvidia*/nvidia_preset %buildroot/%xdrv_pre_d/nvidia
%__install -m 0644 libnvidianull.so %buildroot/%x11_lib_dir/

%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_etclib_sym_dir/libvdpau_nvidia.so
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_etclib_sym_dir/libnvidia-cfg.so.1
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_etclib_sym_dir/libEGL_nvidia.so.0
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_etclib_sym_dir/libGLESv2_nvidia.so.2
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_etclib_sym_dir/libGLESv1_CM_nvidia.so.1
%__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_etclib_sym_dir/libGLX_nvidia.so.0
%__ln_s `relative %x11driver_dir %_sysconfdir/libnvidiacurrent` %buildroot/%_sysconfdir/libnvidiacurrent
%__ln_s `relative %_sysconfdir/libnvidiacurrent %nv_etclib_sym_dir/current` %buildroot/%nv_etclib_sym_dir/current
%if "%_lib" == "lib64"
%__ln_s `relative %x11driver_dir %_sysconfdir/libnvidia32current` %buildroot/%_sysconfdir/libnvidia32current
%__ln_s `relative %_sysconfdir/libnvidia32current %nv_lib32_sym_dir/current` %buildroot/%nv_lib32_sym_dir/current
%endif

%__ln_s ../../..%nv_etclib_sym_dir/libvdpau_nvidia.so %buildroot/%x11_lib_dir/vdpau/libvdpau_nvidia.so
%__ln_s libvdpau_nvidia.so %buildroot/%x11_lib_dir/vdpau/libvdpau_nvidia.so.1
%__ln_s ../..%nv_etclib_sym_dir/libnvidia-cfg.so.1 %buildroot/%x11_lib_dir/libnvidia-cfg.so.1
%__ln_s ../..%nv_etclib_sym_dir/libEGL_nvidia.so.0 %buildroot/%x11_lib_dir/libEGL_nvidia.so.0
%__ln_s ../..%nv_etclib_sym_dir/libGLESv2_nvidia.so.2 %buildroot/%x11_lib_dir/libGLESv2_nvidia.so.2
%__ln_s ../..%nv_etclib_sym_dir/libGLESv1_CM_nvidia.so.1 %buildroot/%x11_lib_dir/libGLESv1_CM_nvidia.so.1
%__ln_s ../..%nv_etclib_sym_dir/libGLX_nvidia.so.0 %buildroot/%x11_lib_dir/libGLX_nvidia.so.0


# nvidia_drv.o
if false ; then
    %__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_etclib_sym_dir/nvidia_drv.o
    %__ln_s ../../../../..%nv_etclib_sym_dir/nvidia_drv.o %buildroot/%x11_drv_dir/nvidia_drv.o
    #%__ln_s ../../../../..%nv_etclib_sym_dir/nvidia_drv.o %buildroot/%x11_drv_old/nvidia_drv.o
fi
# nvidia_drv.so
if true ; then
    %__ln_s ../../..%x11_lib_dir/libnvidianull.so %buildroot/%nv_etclib_sym_dir/nvidia_drv.so
    %__ln_s ../../../../..%nv_etclib_sym_dir/nvidia_drv.so %buildroot/%x11_drv_dir/nvidia_drv.so
    #%__ln_s ../../../../..%nv_etclib_sym_dir/nvidia_drv.so %buildroot/%x11_drv_old/nvidia_drv.so
fi


mkdir -p %buildroot/%_bindir
ln -s /bin/true %buildroot/%_bindir/nvidia-bug-report.sh

# install configs
mkdir -p %buildroot/%_sysconfdir/X11/xorg.conf.d/
echo >%buildroot/%_sysconfdir/X11/xorg.conf.d/09-nvidia.conf
mkdir -p %buildroot/%_sysconfdir/ld.so.conf.d/
echo >%buildroot/%_sysconfdir/ld.so.conf.d/nvidia.conf

%post -n %{bin_pkg_name}_common
if [ -z "$DURING_INSTALL" ]; then
    X11PRESETDRV=`which x11presetdrv 2>/dev/null`
    if [ -n "$X11PRESETDRV" ]; then
	$X11PRESETDRV ||:
    else
	echo "Warning! x11presetdrv program not found!" >&2
    fi
fi


%files
%dir %module_local_dir
%dir %_datadir/nvidia/
%ghost %_bindir/nvidia-bug-report.sh
%ghost %_sysconfdir/X11/xorg.conf.d/09-nvidia.conf
%ghost %_sysconfdir/ld.so.conf.d/nvidia.conf
%xdrv_pre_d/nvidia
%xdrv_d/nvidia
#%xdrv_d_old/nvidia
%x11_lib_dir/libnvidianull.so
%dir %nv_etclib_sym_dir/
#
%nv_etclib_sym_dir/nvidia_drv.*
%x11_drv_dir/nvidia_drv.*
#%ghost %x11_drv_old/nvidia_drv.*
#
%nv_workdirdir
%nv_etclib_sym_dir/libvdpau_nvidia.so
%nv_etclib_sym_dir/libnvidia-cfg.so.?
%nv_etclib_sym_dir/libEGL_nvidia.so.?
%nv_etclib_sym_dir/libGLESv2_nvidia.so.?
%nv_etclib_sym_dir/libGLESv1_CM_nvidia.so.?
%nv_etclib_sym_dir/libGLX_nvidia.so.?
#%nv_etclib_sym_dir/nvidia.xinf
%nv_etclib_sym_dir/current
%_sysconfdir/libnvidiacurrent
%if "%_lib" == "lib64"
%dir %nv_lib32_sym_dir/
%nv_lib32_sym_dir/current
%_sysconfdir/libnvidia32current
%endif
#
%x11_lib_dir/vdpau/libvdpau_nvidia.so
%x11_lib_dir/vdpau/libvdpau_nvidia.so.?
%x11_lib_dir/libnvidia-cfg.so.?
%x11_lib_dir/libEGL_nvidia.so.?
%x11_lib_dir/libGLESv2_nvidia.so.?
%x11_lib_dir/libGLESv1_CM_nvidia.so.?
%x11_lib_dir/libGLX_nvidia.so.?
#
%_bindir/nvidia-clean-driver
%_bindir/nvidia-install-driver
/usr/lib/nvidia/alternate-install-present

%changelog
* Thu Aug 15 2019 Sergey V Turchin <zerg@altlinux.org> 430.40-alt216
- new version

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 430.34-alt215
- new version

* Tue Jun 11 2019 Sergey V Turchin <zerg@altlinux.org> 430.26-alt214
- new version

* Thu Mar 14 2019 Sergey V Turchin <zerg@altlinux.org> 410.104-alt213
- new version

* Tue Feb 26 2019 Sergey V Turchin <zerg@altlinux.org> 410.93-alt212
- fix detect intel videocards

* Wed Jan 09 2019 Sergey V Turchin <zerg@altlinux.org> 410.93-alt211
- new version

* Wed Jan 09 2019 Sergey V Turchin <zerg@altlinux.org> 410.78-alt210
- require xsetup

* Sat Dec 29 2018 Sergey V Turchin <zerg@altlinux.org> 410.78-alt209
- don't use nvidia-xconfig to prevent creation of /etc/X11/xorg.conf

* Wed Dec 12 2018 Sergey V Turchin <zerg@altlinux.org> 410.78-alt208
- new version

* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt207
- fix create kernel module symlinks

* Wed Dec 05 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt206
- always rewrite xorg.conf.d/09-nvidia.conf
- don't save broken kernel module symlinks

* Mon Nov 26 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt205
- don't mix kernel modules (ALT#35650)

* Fri Nov 16 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt204
- using X11 libglx.so with new nvidia driver on old systems

* Fri Nov 16 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt203
- use AllowEmptyInitialConfiguration only on new systems

* Thu Nov 15 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt202
- always using MatchDriver xorg feature if possible
- create xorg.conf if not glvnd packaging scheme

* Wed Nov 07 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt201
- new version

* Fri Nov 02 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt200
- using MatchDriver xorg feature only with glvnd packaging scheme

* Thu Nov 01 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt199
- don't detect new glvnd packaging scheme on old branches

* Wed Oct 31 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt198
- package symlinks

* Tue Oct 30 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt197
- using new kernel/xorg facility to load nvidia driver when possible

* Fri Oct 19 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt196
- add 32bit libs to ld.so.conf for old drivers
- clean nvidia configs if non-nvidia

* Thu Oct 18 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt195
- add support of new glvnd packaging scheme

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt194%ubt
- new version

* Wed Aug 15 2018 Sergey V Turchin <zerg@altlinux.org> 390.77-alt193%ubt
- new version

* Thu Jun 07 2018 Sergey V Turchin <zerg@altlinux.org> 390.67-alt192%ubt
- new version

* Tue May 22 2018 Sergey V Turchin <zerg@altlinux.org> 390.59-alt191%ubt
- new version

* Mon Apr 02 2018 Sergey V Turchin <zerg@altlinux.org> 390.48-alt190%ubt
- new version

* Mon Feb 12 2018 Sergey V Turchin <zerg@altlinux.org> 390.25-alt189%ubt
- new version

* Fri Jan 12 2018 Sergey V Turchin <zerg@altlinux.org> 384.111-alt188%ubt
- new version

* Tue Dec 19 2017 Sergey V Turchin <zerg@altlinux.org> 384.98-alt187%ubt
- fix driver switching (ALT#34357)

* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 384.98-alt186%ubt
- small code optimization

* Wed Nov 29 2017 Sergey V Turchin <zerg@altlinux.org> 384.98-alt185%ubt
- recognize VGA 3D controllers

* Mon Nov 27 2017 Sergey V Turchin <zerg@altlinux.org> 384.98-alt184%ubt
- new version

* Mon Oct 30 2017 Sergey V Turchin <zerg@altlinux.org> 384.90-alt183%ubt
- fix create symlinks to current nvidia libraries directory

* Mon Oct 30 2017 Sergey V Turchin <zerg@altlinux.org> 384.90-alt182%ubt
- fix symlinks (ALT#34080)

* Thu Oct 26 2017 Sergey V Turchin <zerg@altlinux.org> 384.90-alt181%ubt
- use new driver directory if available for current libraries directory symlink

* Fri Oct 20 2017 Sergey V Turchin <zerg@altlinux.org> 384.90-alt180%ubt
- create /etc/X11/lib{64,}_nvidia/current symlink to all nvidia libraries directory

* Tue Sep 26 2017 Sergey V Turchin <zerg@altlinux.org> 384.90-alt179%ubt
- new version

* Tue Aug 08 2017 Sergey V Turchin <zerg@altlinux.org> 375.82-alt178%ubt
- new version

* Wed May 10 2017 Sergey V Turchin <zerg@altlinux.org> 375.66-alt177
- new version

* Fri Feb 17 2017 Sergey V Turchin <zerg@altlinux.org> 375.39-alt176
- new version

* Fri Dec 16 2016 Sergey V Turchin <zerg@altlinux.org> 375.26-alt175
- new version

* Tue Nov 29 2016 Sergey V Turchin <zerg@altlinux.org> 375.20-alt174
- new version

* Tue Oct 11 2016 Sergey V Turchin <zerg@altlinux.org> 367.57-alt173
- fix symlinks only for nvidia

* Thu Sep 29 2016 Sergey V Turchin <zerg@altlinux.org> 367.44-alt172
- force nvidia libraries only for nvidia

* Wed Sep 28 2016 Sergey V Turchin <zerg@altlinux.org> 367.44-alt171
- fix check for xorg.conf

* Wed Sep 28 2016 Sergey V Turchin <zerg@altlinux.org> 367.44-alt170
- fix check for xorg.conf

* Mon Aug 29 2016 Sergey V Turchin <zerg@altlinux.org> 367.44-alt169
- new version

* Mon Jul 25 2016 Sergey V Turchin <zerg@altlinux.org> 367.35-alt168
- switch libGLESv1_CM

* Thu Jul 21 2016 Sergey V Turchin <zerg@altlinux.org> 367.35-alt167
- switch libGLX

* Mon Jul 18 2016 Sergey V Turchin <zerg@altlinux.org> 367.35-alt166
- bump version

* Fri Jul 01 2016 Sergey V Turchin <zerg@altlinux.org> 367.27-alt165
- add nvidia-drm module support

* Fri May 27 2016 Sergey V Turchin <zerg@altlinux.org> 361.45.11-alt164
- bump version

* Fri May 27 2016 Sergey V Turchin <zerg@altlinux.org> 361.42-alt163
- switch libGLdispatch

* Fri Apr 22 2016 Sergey V Turchin <zerg@altlinux.org> 361.42-alt162
- add nvidia-uvm module support

* Mon Apr 11 2016 Sergey V Turchin <zerg@altlinux.org> 361.42-alt161
- bump version

* Fri Mar 04 2016 Sergey V Turchin <zerg@altlinux.org> 361.28-alt160
- fix nvidia-modeset symlink

* Fri Mar 04 2016 Sergey V Turchin <zerg@altlinux.org> 361.28-alt159
- fix 32-bit symlinks on x86_64

* Fri Feb 19 2016 Sergey V Turchin <zerg@altlinux.org> 361.28-alt158
- add libglvnd support
- add nvidia-modeset.ko support

* Wed Jan 27 2016 Sergey V Turchin <zerg@altlinux.org> 352.79-alt157
- bump version

* Tue Nov 24 2015 Sergey V Turchin <zerg@altlinux.org> 352.63-alt156
- bump version

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 352.55-alt155
- new version
- add nvidia-clean-driver

* Tue Sep 01 2015 Sergey V Turchin <zerg@altlinux.org> 352.41-alt154
- bump version

* Mon Jul 27 2015 Sergey V Turchin <zerg@altlinux.org> 346.87-alt153
- bump version

* Thu Jun 25 2015 Sergey V Turchin <zerg@altlinux.org> 346.82-alt152
- bump version

* Fri May 15 2015 Sergey V Turchin <zerg@altlinux.org> 346.72-alt151
- bump version

* Wed Apr 08 2015 Sergey V Turchin <zerg@altlinux.org> 346.59-alt150
- bump version

* Tue Mar 10 2015 Sergey V Turchin <zerg@altlinux.org> 346.47-alt149
- provide NVIDIA_GLX for compatibility

* Tue Mar 10 2015 Sergey V Turchin <zerg@altlinux.org> 346.47-alt148
- bump version

* Thu Feb 05 2015 Sergey V Turchin <zerg@altlinux.org> 346.35-alt147
- apt-get update when nvidia-install-driver

* Wed Feb 04 2015 Sergey V Turchin <zerg@altlinux.org> 346.35-alt146
- small optimization

* Wed Feb 04 2015 Sergey V Turchin <zerg@altlinux.org> 346.35-alt145
- fix card autoselection

* Wed Feb 04 2015 Sergey V Turchin <zerg@altlinux.org> 346.35-alt144
- execute x11presetdrv on finish nvidia-install-driver

* Thu Jan 22 2015 Sergey V Turchin <zerg@altlinux.org> 346.35-alt143
- bump version

* Tue Dec 09 2014 Sergey V Turchin <zerg@altlinux.org> 340.65-alt142
- bump version

* Mon Nov 10 2014 Sergey V Turchin <zerg@altlinux.org> 340.58-alt141
- bump version

* Mon Oct 06 2014 Sergey V Turchin <zerg@altlinux.org> 340.46-alt140
- bump version

* Wed Oct 01 2014 Sergey V Turchin <zerg@altlinux.org> 340.32-alt139
- update message when restoring symlinks

* Mon Aug 18 2014 Sergey V Turchin <zerg@altlinux.org> 340.32-alt138
- bump version

* Thu Jul 17 2014 Sergey V Turchin <zerg@altlinux.org> 340.24-alt137
- bump version

* Mon Jul 07 2014 Sergey V Turchin <zerg@altlinux.org> 331.89-alt136
- bump version

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 331.79-alt135
- bump version

* Tue Apr 29 2014 Sergey V Turchin <zerg@altlinux.org> 331.67-alt134
- bump version

* Wed Feb 19 2014 Sergey V Turchin <zerg@altlinux.org> 331.49-alt133
- bump version

* Thu Feb 13 2014 Sergey V Turchin <zerg@altlinux.org> 331.38-alt132
- using apt-scripts-nvidia for nvidia-install-driver

* Tue Jan 21 2014 Sergey V Turchin <zerg@altlinux.org> 331.38-alt131
- add libvdpau_nvidia.so.1

* Thu Jan 16 2014 Sergey V Turchin <zerg@altlinux.org> 331.38-alt130
- move vdpau module to libdir/vdpau/

* Thu Jan 16 2014 Sergey V Turchin <zerg@altlinux.org> 331.38-alt129
- fix process non-NVIDIA devices (ALT#29729)

* Tue Jan 14 2014 Sergey V Turchin <zerg@altlinux.org> 331.38-alt128
- bump version

* Tue Nov 19 2013 Sergey V Turchin <zerg@altlinux.org> 331.20-alt127
- switch new nvidia own libGLESv2 and libEGL
- imply always have /etc/X11/lib64 on x86_64

* Thu Nov 07 2013 Sergey V Turchin <zerg@altlinux.org> 319.72-alt126
- bump version

* Thu Oct 03 2013 Sergey V Turchin <zerg@altlinux.org> 319.60-alt125
- bump version

* Mon Sep 02 2013 Sergey V Turchin <zerg@altlinux.org> 319.49-alt124
- bump version

* Sun Jul 21 2013 Sergey V Turchin <zerg@altlinux.org> 319.32-alt123
- fix nvidia-install-driver premissions

* Sat Jul 20 2013 Sergey V Turchin <zerg@altlinux.org> 319.32-alt122
- simplify driver install command

* Tue Jul 02 2013 Sergey V Turchin <zerg@altlinux.org> 319.32-alt121
- prompt user to don't use nvidia-installer

* Wed Jun 26 2013 Sergey V Turchin <zerg@altlinux.org> 319.32-alt120
- bump version

* Fri May 24 2013 Sergey V Turchin <zerg@altlinux.org> 319.23-alt119
- bump version

* Mon May 13 2013 Sergey V Turchin <zerg@altlinux.org> 319.17-alt118
- bump version

* Wed Apr 03 2013 Sergey V Turchin <zerg@altlinux.org> 310.44-alt117
- bump version

* Mon Mar 11 2013 Sergey V Turchin <zerg@altlinux.org> 310.40-alt116
- bump version

* Wed Jan 23 2013 Sergey V Turchin <zerg@altlinux.org> 310.32-alt115
- bump version

* Fri Nov 23 2012 Sergey V Turchin <zerg@altlinux.org> 310.19-alt114
- switch libGLESv2.so.2 and libEGL.so.1

* Wed Nov 21 2012 Sergey V Turchin <zerg@altlinux.org> 310.19-alt113
- remove XvMC plugin support

* Mon Nov 19 2012 Sergey V Turchin <zerg@altlinux.org> 310.19-alt112
- bump version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 304.64-alt111
- bump version

* Fri Oct 19 2012 Sergey V Turchin <zerg@altlinux.org> 304.60-alt110
- bump version

* Tue Oct 02 2012 Sergey V Turchin <zerg@altlinux.org> 304.51-alt109
- bump version

* Wed Aug 29 2012 Sergey V Turchin <zerg@altlinux.org> 304.43-alt108
- bump version

* Tue Aug 14 2012 Sergey V Turchin <zerg@altlinux.org> 304.37-alt107
- bump version

* Thu Jul 12 2012 Sergey V Turchin <zerg@altlinux.org> 302.17-alt106
- new version

* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 295.59-alt105
- bump version

* Thu May 17 2012 Sergey V Turchin <zerg@altlinux.org> 295.53-alt104
- bump version

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 295.49-alt103
- bump version

* Wed Apr 11 2012 Sergey V Turchin <zerg@altlinux.org> 295.40-alt102
- bump version

* Mon Mar 26 2012 Sergey V Turchin <zerg@altlinux.org> 295.33-alt101
- bump version

* Tue Feb 14 2012 Sergey V Turchin <zerg@altlinux.org> 295.20-alt100
- bump version

* Tue Nov 22 2011 Sergey V Turchin <zerg@altlinux.org> 290.10-alt99
- bump version

* Tue Oct 04 2011 Sergey V Turchin <zerg@altlinux.org> 285.05.09-alt98
- cleanup specfile

* Wed Aug 24 2011 Sergey V Turchin <zerg@altlinux.org> 280.13-alt97
- use xsetup-monitor before nvidia-xconfig when setup xorg.conf (see bug 25134)

* Wed Aug 03 2011 Sergey V Turchin <zerg@altlinux.org> 280.13-alt96
- bump version

* Tue Aug 02 2011 Sergey V Turchin <zerg@altlinux.org> 275.21-alt95
- bump version

* Wed Jun 15 2011 Sergey V Turchin <zerg@altlinux.org> 275.09.07-alt94
- bump version

* Mon May 23 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.19-alt93
- bump version

* Tue May 03 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.06-alt92
- fix libGL.so.1 symlink, when points to /usr/lib*/nvidia_*

* Fri Apr 22 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.06-alt91
- bump version

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.03-alt90
- create xorg.conf when needed

* Tue Apr 12 2011 Sergey V Turchin <zerg@altlinux.org> 270.41.03-alt89
- bump version

* Tue Mar 15 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.44-alt87.M51.1
- built for M51

* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.44-alt88
- bump version

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 260.19.36-alt87
- bump version

* Fri Dec 24 2010 Sergey V Turchin <zerg@altlinux.org> 260.19.29-alt86
- bump version

* Wed Nov 10 2010 Sergey V Turchin <zerg@altlinux.org> 260.19.21-alt85
- bump version

* Fri Oct 22 2010 Sergey V Turchin <zerg@altlinux.org> 260.19.12-alt84
- bump version

* Tue Aug 31 2010 Sergey V Turchin <zerg@altlinux.org> 256.53-alt83
- split from full package

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 256.52-alt82
- new release 256.52

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 256.44-alt81
- new release 256.44

* Wed Jul 14 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt79.M51.1
- built for M51

* Tue Jul 13 2010 Sergey V Turchin <zerg@altlinux.org> 256.35-alt80
- new release 256.35
- make nvidia-bug-report.sh as alternative

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.31-alt79
- new release 195.36.31

* Mon Apr 26 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.24-alt78
- new release 195.36.24

* Tue Mar 16 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.15-alt77
- new release 195.36.15

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.08-alt76
- new release 195.36.08

* Mon Feb 15 2010 Sergey V Turchin <zerg@altlinux.org> 195.36.03-alt75
- new release 195.36.03

* Thu Dec 17 2009 Sergey V Turchin <zerg@altlinux.org> 190.53-alt73.M40.1
- built for M40

* Thu Dec 17 2009 Sergey V Turchin <zerg@altlinux.org> 190.53-alt73.M41.1
- built for M41

* Thu Dec 17 2009 Sergey V Turchin <zerg@altlinux.org> 190.53-alt74
- remove ldconfig from %%post

* Thu Dec 17 2009 Sergey V Turchin <zerg@altlinux.org> 190.53-alt73
- new version

* Thu Dec 10 2009 Sergey V Turchin <zerg@altlinux.org> 190.42-alt71.M41.1
- built for M41

* Thu Dec 10 2009 Sergey V Turchin <zerg@altlinux.org> 190.42-alt71.M40.1
- built for M40

* Wed Oct 28 2009 Sergey V Turchin <zerg@altlinux.org> 190.42-alt72
- new version

* Thu Oct 15 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.36-alt71
- don't package libvdpau
- fix file perissions

* Fri Sep 25 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.36-alt70
- add 0x087D to .xinf (ALT#21688)

* Wed Sep 09 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.36-alt69
- don't restore %_libdir/X11/modules/libwfb.so

* Mon Aug 24 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.36-alt68
- new version

* Tue Aug 04 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.31-alt67
- new version

* Fri Jul 10 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt66
- add libdri.so switching

* Wed Jul 01 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt65
- check kernel module symlink when x11presetdrv

* Mon Jun 08 2009 Sergey V Turchin <zerg@altlinux.org> 185.18.14-alt64
- new version

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 180.60-alt63
- new version

* Thu Apr 23 2009 Sergey V Turchin <zerg@altlinux.org> 180.51-alt62
- new version

* Thu Apr 02 2009 Sergey V Turchin <zerg@altlinux.org> 180.44-alt61
- new version

* Wed Mar 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.37-alt60
- new beta

* Tue Mar 03 2009 Sergey V Turchin <zerg at altlinux dot org> 180.35-alt59
- new version

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt59
- update xinf-file

* Mon Mar 02 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt58
- remove x11setupdrv requires
- don't use deprecated macroses in post-scripts

* Mon Feb 16 2009 Sergey V Turchin <zerg at altlinux dot org> 180.29-alt57
- new version

* Fri Jan 30 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt56
- move vdpau includes upper

* Tue Jan 13 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt55
- reduce debug messages when update symlinks during x11setupdrv

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt54
- libvdpau and vdpau nvidia module

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 180.22-alt53
- new version

* Fri Dec 26 2008 Sergey V Turchin <zerg at altlinux dot org> 177.82-alt52
- don't touch proper symlinks during x11setupdrv
- remove *_ldconfig macroses frpm post* scripts

* Mon Nov 17 2008 Sergey V Turchin <zerg at altlinux dot org> 177.82-alt51
- new release

* Wed Oct 08 2008 Sergey V Turchin <zerg at altlinux dot org> 177.80-alt50
- new version

* Fri Oct 03 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.12-alt49
- remove 10DE:0242(GF 6100) from .xinf

* Fri Aug 29 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.12-alt48
- add support for /etc/X11/lib64
- add support for 32-bit libs switching on x86_64
  (requies to install proper i586-nvidia_glx_XXXX package
  or copy /usr/lib/nvidia_XXXX from proper i586 package)

* Tue Aug 05 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.12-alt47
- new version

* Tue Jul 29 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.09-alt46
- new version

* Fri May 30 2008 Sergey V Turchin <zerg at altlinux dot org> 173.14.05-alt45
- new version

* Mon Mar 17 2008 Sergey V Turchin <zerg at altlinux dot org> 169.12-alt44
- use libsysfs instead of libpci in drvpre.d/nvidia

* Fri Mar 07 2008 Sergey V Turchin <zerg at altlinux dot org> 169.12-alt43
- update xinf-file

* Wed Feb 27 2008 Sergey V Turchin <zerg at altlinux dot org> 169.12-alt42
- new version

* Wed Jan 23 2008 Sergey V Turchin <zerg at altlinux dot org> 169.09-alt41
- new version

* Fri Dec 21 2007 Sergey V Turchin <zerg at altlinux dot org> 169.07-alt40
- new version

* Fri Dec 14 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt40
- clean xinf-file

* Thu Sep 27 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt39
- fix selecting best driver in drvpre.d/nvidia

* Wed Sep 26 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt38
- add more versbosity to drvpre.d/nvidia

* Tue Sep 25 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt37
- reduce executed code in drvpre.d if no nvidia cards found

* Mon Sep 24 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt36
- more check the loaded kernel version

* Fri Sep 21 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.19-alt35
- new version

* Fri Sep 21 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt34
- fix crush of drvpre.d/nvidia

* Thu Sep 20 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt33
- check loaded kernel module version before try to unload

* Wed Sep 19 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt32
- add autoswitching of kernel module

* Fri Jun 22 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.11-alt31
- new version

* Sat Jun 09 2007 Sergey V Turchin <zerg at altlinux dot org> 100.14.09-alt30
- new version

* Thu Mar 15 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9755-alt29
- new version
- megre x86_64 and ix86 into one src.rpm
- update package description

* Mon Feb 05 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9746-alt28
- fix modules path in %%post

* Wed Jan 24 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9746-alt27
- add info file for alterator-x11

* Wed Jan 10 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.9746-alt26
- new version

* Tue Dec 05 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9631-alt25
- new version

* Thu Nov 09 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.9629-alt24
- new version

* Tue Nov 07 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8776-alt23
- add nvidia-bug-report.sh

* Tue Oct 24 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8776-alt22
- new version

* Mon Oct 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8774-alt21
- remove requires to rtld(GNU_HASH)

* Thu Oct 05 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8774-alt20
- turn on tls checking in x11setupdrv module
- turn off verbosity for /usr/X11R6 support by default

* Tue Aug 29 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8774-alt19
- new version
- add libnvidia-cfg.so to package

* Tue May 23 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8762-alt18
- new version

* Mon Apr 10 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8756-alt17
- new version

* Tue Jan 17 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.8178-alt16
- fix to work with old and new xorg

* Mon Dec 26 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.8178-alt15
- new version

* Thu Aug 25 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7676-alt14
- dont restore libglx.so for Compact-3.0

* Thu Aug 18 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7676-alt13
- symlink /etc/X11/lib_nvidia/nvidia_drv.* to existing file again

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7676-alt12
- new version

* Mon Aug 08 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7667-alt11
- new version

* Mon Aug 08 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt10
- add libglx.so
- turn off verbosity of /usr/X11R6/lib/drv.d/nvidia by default
  (added command line options)

* Wed Jul 06 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt9
- fix path to .versions/nvidia in %%post

* Thu Jun 30 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt8
- change setgl to x11setupdrv in %%post
- symlink /etc/X11/lib_nvidia/nvidia_drv.* to unexisting file by default

* Tue Jun 14 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt7
- add symlink libnvidia-tls.so.1 to /usr/lib
- do not check for tls in /usr/X11R6/lib/nvidia
- restore symlinks for libglx.a and libGL.so.1 in /usr/X11R6/lib if absent

* Fri Jun 10 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt6
- move writable symlinks to nv_etclib_sym_dir
- add check for tls to link libnvidia-tls.so correctly

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt5
- new x11 driver switch system; %xdrv_d/nvidia adjust the driver

* Fri Apr 29 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt4
- fix provides for X configurator

* Thu Apr 07 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt3
- add kernel-source-nvidia subpackage

* Wed Apr 06 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt2
- fix nvidia_set_glx

* Mon Apr 04 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7174-alt1
- new version

* Tue Mar 15 2005 Sergey V Turchin <zerg at altlinux dot org> 1.0.7167-alt1
- new version
- service start after network by default

* Mon Nov 22 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6629-alt1
- new version

* Fri Oct 08 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6111-alt2
- try to fix link to libGL.so.1 when service nvidia_glx starts

* Fri Aug 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6111-alt1
- new version

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6106-alt4
- ignore non-NVIDIA videocards via pciscan in initscript

* Tue Jul 13 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6106-alt3
- add %%ghost files to -common package

* Fri Jul 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6106-alt2
- fix libnvidia-tls.so.1 link placement

* Fri Jul 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6106-alt1
- new version

* Tue Feb 03 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.5336-alt1
- new version

* Mon Jan 19 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.5328-alt2
- initscript compatible with 2.6.x kernels
- add start on 3,4 runlevels

* Tue Dec 23 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.5328-alt1
- new version

* Tue Dec 23 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt7
- fix initscript status message

* Thu Oct 30 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt6
- fix initscript fail message

* Fri Sep 26 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt5
- fix %%post

* Fri Sep 26 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt4
- force install service nvidia_lgx when variable DURING_INSTALL=1

* Mon Sep 15 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt3
- fix initscript

* Mon Sep 15 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4363-alt2
- make possible to install different versions together

* Wed Jul 30 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4496-alt1
- new version

* Tue Jul 01 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.4363-alt1
- new version

* Tue May 06 2003 Sergey V Turchin <zerg at altlinux dot ru> 1.0.4349-alt2
- remove requires to XFree86-server libGLwrapper
- remove very old versions from %%versions

* Wed Apr 02 2003 Peter Novodvorsky <nidd@altlinux.com> 1.0.4349-alt1
- New upstream version

* Sun Feb 16 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.0.4191-alt3
- Fixed file permissions on %%doc
- Added Summary and %%description in Russian

* Fri Dec 20 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.4191-alt2
- fix link to libglx.so

* Thu Dec 19 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.4191-alt1
- new version

* Fri Sep 13 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.3123-alt1
- new version

* Thu Jun 06 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.2960-alt1
- new version

* Fri Mar 15 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.2802-alt1
- new version

* Fri Feb 22 2002 Sergey V Turchin <zerg@altlinux.ru> 1.0.2313-alt1
- prepare for Sisyphus

* Thu Jan 31 2002 Sergey V Turchin <zerg@altlinux.ru> ALL-alt2
- fix requires
- cleanup spec

* Tue Jan 29 2002 Sergey V Turchin <zerg@altlinux.ru> ALL-alt1
- add interactive build

* Sat Dec 29 2001 Ivan Zakharyaschev <imz@altlinux.ru> 1.0.2313-alt3
- fix requires version (add 1.0 prefix)

* Tue Dec 18 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.2313-alt2
- Fixed requires as kernel_version of this driver is 2314

* Wed Dec 05 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.2313-alt1
- new version

* Thu Jun 14 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.1251-alt5
- changed pakage name to nvidiaGL

* Fri Jun 08 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0.1251-alt4
- fix requires

* Wed May 23 2001 Sergey V Turchin <zerg@altlinux.ru>
- first build
