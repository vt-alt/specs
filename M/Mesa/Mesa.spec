%def_enable egl
%def_enable gles2

%define dri_drivers_add() %{expand:%%global dri_drivers %{?dri_drivers:%dri_drivers,}%{1}}
%define gallium_drivers_add() %{expand:%%global gallium_drivers %{?gallium_drivers:%gallium_drivers,}%{1}}
%define vulkan_drivers_add() %{expand:%%global vulkan_drivers %{?vulkan_drivers:%vulkan_drivers,}%{1}}

%define use_lld_arches x86_64
%define link_static_llvm_arches x86_64

%define radeon_arches %ix86 x86_64 aarch64 ppc64le mipsel
%define vulkan_radeon_arches x86_64 ppc64le mipsel
%define nouveau_arches %ix86 x86_64 aarch64 ppc64le mipsel
%define intel_arches %ix86 x86_64
%define vulkan_intel_arches x86_64
%define virgl_arches %ix86 x86_64 aarch64 ppc64le mipsel
%define armsoc_arches %arm aarch64
# OpenCL requires static clang libraries
# which may be built as ThinLTO objects (if lld
# supports target architecture).
%define opencl_arches x86_64
%define gallium_pipe_arches x86_64

#VDPAU state tracker requires at least one of the following gallium drivers: r300, r600, radeonsi, nouveau
%define vdpau_arches %radeon_arches %nouveau_arches
#XVMC state tracker requires at least one of the following gallium drivers: r600, nouveau
%define xvmc_arches %radeon_arches %nouveau_arches
# Mesa builds radeon and nouveau support as megadrivers
%define dri_megadriver_arches %radeon_arches %nouveau_arches
%define gallium_megadriver_arches %radeon_arches %nouveau_arches
# Building xa requires at least one non swrast gallium driver.
%define xa_arches %radeon_arches %nouveau_arches %virgl_arches %armsoc_arches

%gallium_drivers_add swrast
%ifarch %radeon_arches
%dri_drivers_add r100
%dri_drivers_add r200
%gallium_drivers_add r300
%gallium_drivers_add r600
%gallium_drivers_add radeonsi
%endif
%ifarch %intel_arches
%dri_drivers_add i915
%dri_drivers_add i965
%endif
%ifarch %nouveau_arches
%dri_drivers_add nouveau
%gallium_drivers_add nouveau
%endif
%ifarch %virgl_arches
%gallium_drivers_add virgl
%endif
%ifarch %armsoc_arches
%gallium_drivers_add vc4
%gallium_drivers_add etnaviv
%gallium_drivers_add freedreno
%gallium_drivers_add kmsro
%gallium_drivers_add panfrost
%gallium_drivers_add lima
%endif
%ifarch %vulkan_intel_arches
%vulkan_drivers_add intel
%endif
%ifarch %vulkan_radeon_arches
%vulkan_drivers_add amd
%endif

Name: Mesa
Version: 19.1.5
Release: alt1
Epoch: 4
License: MIT
Summary: OpenGL compatible 3D graphics library
Group: System/Libraries
Url: http://www.mesa3d.org

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version.patch

BuildPreReq: /proc
BuildRequires(pre): meson
BuildRequires: gcc-c++ indent flex libXdamage-devel libXext-devel libXft-devel libXmu-devel libXi-devel libXrender-devel libXxf86vm-devel
BuildRequires: libdrm-devel libexpat-devel python-modules libselinux-devel libxcb-devel libSM-devel libtinfo-devel libudev-devel
BuildRequires: libXdmcp-devel libffi-devel libelf-devel libva-devel libvdpau-devel libXvMC-devel xorg-proto-devel libxshmfence-devel
BuildRequires: libXrandr-devel libnettle-devel libelf-devel zlib-devel libwayland-client-devel libwayland-server-devel
BuildRequires: libwayland-egl-devel python-module-libxml2 python3-module-mako python-module-argparse wayland-protocols
BuildRequires: libclc-devel libglvnd-devel >= 0.2.0
%ifarch %radeon_arches
BuildRequires: llvm-devel clang-devel
%ifarch %link_static_llvm_arches
BuildRequires: llvm-devel-static clang-devel-static
%endif
%endif
%ifarch %use_lld_arches
BuildRequires: lld
%endif

%description
Mesa is an OpenGL compatible 3D graphics library

%package -n libGLX-mesa
Summary: OpenGL 1.3 compatible 3D graphics library for X Window server
Group: System/Libraries
Conflicts: libGL < 4:18.2.2-alt1

%description -n libGLX-mesa
Mesa is an OpenGL compatible 3D graphics library

%package -n libGL-devel
Summary: Development files for Mesa Library
Group: Development/C
Requires: libglvnd-devel >= 0.2.0 libGLX-mesa = %epoch:%version-%release

%description -n libGL-devel
libGL-devel contains the libraries and header files needed to
develop programs which make use of Mesa

%package -n libEGL-mesa
Summary: Mesa EGL library
Group: System/Libraries

%description -n libEGL-mesa
Mesa EGL library

%package -n libEGL-devel
Summary: Mesa libEGL development package
Group: Development/C
Requires: libglvnd-devel >= 0.2.0

%description -n libEGL-devel
Mesa libEGL development package

%package -n libGLES-devel
Summary: Mesa libGLES development package
Group: Development/C
Requires: libglvnd-devel >= 0.2.0

%description -n libGLES-devel
Mesa libGLES development package

%package -n libgbm
Summary: GBM buffer management library
Group: System/Libraries

%description -n libgbm
GBM buffer management library

%package -n libgbm-devel
Summary: GBM buffer management development package
Group: Development/C

%description -n libgbm-devel
GBM buffer management development package

%package -n libxatracker
Summary: Mesa XA state tracker
Group: System/Libraries

%description -n libxatracker
Xorg Gallium3D acceleration library

%package -n libxatracker-devel
Summary: Mesa XA state tracker development package
Group: Development/C

%description -n libxatracker-devel
Xorg Gallium3D acceleration development package

%package -n libMesaOpenCL
Summary: Mesa OpenCL runtime library
Group: System/Libraries
Requires: ocl-icd libclc

%description -n libMesaOpenCL
This package contains the mesa implementation of the OpenCL (Open Compute
Language) library, which is intended for use with an ICD loader. OpenCL
provides a standardized interface for computational analysis on graphical
processing units.

%package -n xorg-dri-swrast
Summary: Mesa software rendering libraries
Group: System/X11
Provides: xorg-dri-virgl
Obsoletes: xorg-dri-virgl < %epoch:%version-%release

%description -n xorg-dri-swrast
Mesa software rendering libraries

%package -n xorg-dri-intel
Summary: Intel DRI driver
Group: System/X11

%description -n xorg-dri-intel
DRI driver for Intel i8xx, i9xx

%package -n xorg-dri-radeon
Summary: ATI RADEON DRI driver
Group: System/X11
%ifarch %vdpau_arches
Requires: libvdpau
%endif

%description -n xorg-dri-radeon
DRI driver for ATI R100, R200, R300, R400, R500

%package -n xorg-dri-nouveau
Summary: nVidia DRI driver
Group: System/X11
%ifarch %vdpau_arches
Requires: libvdpau
%endif

%description -n xorg-dri-nouveau
DRI driver for nVidia

%package -n xorg-dri-armsoc
Summary: SoC DRI drivers
Group: System/X11

%description -n xorg-dri-armsoc
DRI drivers for various SoCs

%set_verify_elf_method unresolved=relaxed

%prep
%setup -q
%patch -p1

mkdir -p $(pwd)/bin
%ifarch %use_lld_arches
ln -s %_bindir/ld.lld $(pwd)/bin/ld
%endif

%build
%ifarch %use_lld_arches
export PATH=$(pwd)/bin:$PATH
# without this options every lld instance will try to consume all cpus
%add_optflags -Wl,--no-threads -Wl,--thinlto-jobs=1
%endif
%meson \
	-Dplatforms=x11,wayland,drm \
	-Ddri-drivers='%{?dri_drivers}' \
	-Dgallium-drivers='%{?gallium_drivers}' \
	-Dvulkan-drivers='%{?vulkan_drivers}' \
%ifarch %vdpau_arches
	-Dgallium-vdpau=true \
%endif
%ifarch %xvmc_arches
	-Dgallium-xvmc=true \
%endif
	-Ddri3=true \
%ifarch %opencl_arches
	-Dgallium-opencl=icd \
%endif
%ifarch %radeon_arches
	-Dllvm=true \
%ifarch %link_static_llvm_arches
	-Dshared-llvm=false \
%else
	-Dshared-llvm=true \
%endif
%endif
	-Dshared-glapi=true \
%if_enabled egl
	-Degl=true \
%else
	-Degl=false \
%endif
%if_enabled gles2
	-Dgles2=true \
%else
	-Dgles2=false \
%endif
%ifarch %xa_arches
	-Dgallium-xa=true \
%else
	-Dgallium-xa=false \
%endif
	-Dgles1=false \
	-Dopengl=true \
	-Dselinux=true \
	-Dglvnd=true \
	-Ddri-drivers-path=%_libdir/X11/modules/dri \
#

%meson_build -v

%install
export PATH=$(pwd)/bin:$PATH
%meson_install

rm -f %buildroot%_libdir/gallium-pipe/*.la

shopt -s nullglob
m="%buildroot%_libdir/X11/modules/dri %buildroot%_libdir/dri"
for d in $m; do
	for f in $d/*.so; do
		[ ! -L "$f" ] || continue
		n="${f##*/}"
		s="$(objdump -p "$f" | awk '/SONAME/ {print $2}')"
		[ -n "$s" ]
		[ "$n" != "$s" ] || continue
		t="$d/$s"
		[ -f "$t" ] || mv "$f" "$t"
		ln -v -snf "${t##*/}" "$f"
	done
done
d=%buildroot%_libdir/vdpau
	for f in $d/*.so.1.0.0; do
                [ ! -L "$f" ] || continue
                n="${f##*/}"
                s="$(objdump -p "$f" | awk '/SONAME/ {print $2}')"
                [ -n "$s" ]
                [ "$n" != "$s" ] || continue
                t="$d/$s"
                [ -f "$t" ] || mv "$f" "$t"
                ln -v -snf "${t##*/}" "$f"
        done
d=%buildroot%_libdir
	for f in $d/libXvMC*.so; do
                [ ! -L "$f" ] || continue
                n="${f##*/}"
                s="$(objdump -p "$f" | awk '/SONAME/ {print $2}')"
                [ -n "$s" ]
                [ "$n" != "$s" ] || continue
                t="$d/$s"
                [ -f "$t" ] || mv "$f" "$t"
                ln -v -snf "${t##*/}" "$f"
        done

%ifarch %armsoc_arches
find %buildroot%_libdir/X11/modules/dri/ -type l | sed -ne "s|^%buildroot||p" > xorg-dri-armsoc.list
sed -i '/.*swrast.*/d' xorg-dri-armsoc.list
sed -i '/.*virtio.*/d' xorg-dri-armsoc.list
sed -i '/.*nouveau.*/d' xorg-dri-armsoc.list
sed -i '/.*dri\/r[a236].*/d' xorg-dri-armsoc.list
%endif

cat << __EOF__ > %buildroot%_pkgconfigdir/glesv2.pc
prefix=/usr
libdir=\${prefix}/lib64
includedir=\${prefix}/include

Name: glesv2
Description: Mesa OpenGL ES 2.0 library
Version: %version
Libs: -L\${libdir} -lGLESv2
Libs.private: -lpthread -pthread -lm -ldl
Cflags: -I\${includedir}
__EOF__

# remove unpackaged files
cd %buildroot
 rm -f .%_includedir/GL/glcorearb.h
%ifarch %vulkan_intel_arches
 rm -f .%_includedir/vulkan/vulkan_intel.h
%endif
%ifarch %opencl_arches
 rm -f .%_libdir/libMesaOpenCL.so
%endif
cd -

%define _unpackaged_files_terminate_build 1

%files -n libGLX-mesa
%doc docs/relnotes/%version.html
%_libdir/libGLX_mesa.so.*
%_libdir/libglapi.so.*

%files -n libGL-devel
%dir %_includedir/GL
%_includedir/GL/internal
%_includedir/GL/gl.h
%_includedir/GL/gl_mangle.h
%_includedir/GL/glext.h
%_includedir/GL/glx.h
%_includedir/GL/glx_mangle.h
%_includedir/GL/glxext.h
%_libdir/libGLX_mesa.so
%_libdir/libglapi.so
%_pkgconfigdir/gl.pc
%_pkgconfigdir/dri.pc

%if_enabled egl
%files -n libEGL-mesa
%_libdir/libEGL_mesa.so.*
%_datadir/glvnd/egl_vendor.d/50_mesa.json

%files -n libEGL-devel
%_includedir/EGL
%_includedir/KHR
%_libdir/libEGL_mesa.so
%_pkgconfigdir/egl.pc
%endif

%if_enabled gles2
%files -n libGLES-devel
%_includedir/GLES2
%_includedir/GLES3
%_pkgconfigdir/glesv2.pc
%endif

%files -n libgbm
%_libdir/libgbm.so.*

%files -n libgbm-devel
%_includedir/gbm.h
%_libdir/libgbm.so
%_pkgconfigdir/gbm.pc

%ifarch %xa_arches
%files -n libxatracker
%_libdir/libxatracker.so.*

%files -n libxatracker-devel
%_includedir/xa_*.h
%_libdir/libxatracker.so
%_pkgconfigdir/xatracker.pc
%endif

%ifarch %opencl_arches
%files -n libMesaOpenCL
%dir %_sysconfdir/OpenCL
%dir %_sysconfdir/OpenCL/vendors
%_sysconfdir/OpenCL/vendors/mesa.icd
%_libdir/libMesaOpenCL.so.*
%endif

%files -n xorg-dri-swrast
%_datadir/drirc.d
%_libdir/X11/modules/dri/*swrast*_dri.so
%_libdir/X11/modules/dri/libgallium_dri.so
%ifarch %dri_megadriver_arches
%_libdir/X11/modules/dri/libmesa_dri_drivers.so
%endif
%ifarch %virgl_arches
%_libdir/X11/modules/dri/virtio_gpu_dri.so
%endif
%ifarch %gallium_pipe_arches
%dir %_libdir/gallium-pipe
%_libdir/gallium-pipe/pipe_swrast.so
%endif
%ifarch %gallium_megadriver_arches
%_libdir/libXvMCgallium.so
%_libdir/dri/libgallium_drv_video.so
%endif
%ifarch %vdpau_arches
%_libdir/vdpau/libvdpau_gallium.so.1.0.0
%endif

%ifarch %intel_arches
%files -n xorg-dri-intel
%_libdir/X11/modules/dri/i9?5_dri.so
%ifarch %vulkan_intel_arches
%_libdir/libvulkan_intel.so
%dir %_datadir/vulkan
%dir %_datadir/vulkan/icd.d
%_datadir/vulkan/icd.d/intel_icd*
%endif
%endif

%ifarch %nouveau_arches
%files -n xorg-dri-nouveau
%_libdir/X11/modules/dri/nouveau_*dri.so
%_libdir/dri/nouveau_drv_video.so
%_libdir/vdpau/libvdpau_nouveau.so*
%_libdir/libXvMCnouveau.so
%ifarch %gallium_pipe_arches
%_libdir/gallium-pipe/pipe_nouveau.so
%endif
%endif

%ifarch %radeon_arches
%files -n xorg-dri-radeon
%_libdir/X11/modules/dri/radeon*_dri.so
%_libdir/X11/modules/dri/r?00_dri.so
%_libdir/vdpau/libvdpau_r*.so*
%_libdir/dri/r*_drv_video.so
%_libdir/libXvMCr*.so
%ifarch %gallium_pipe_arches
%_libdir/gallium-pipe/pipe_r*.so
%endif
%ifarch %vulkan_radeon_arches
%_libdir/libvulkan_radeon.so
%dir %_datadir/vulkan
%dir %_datadir/vulkan/icd.d
%_datadir/vulkan/icd.d/radeon_icd*
%endif
%endif

%ifarch %armsoc_arches
%files -n xorg-dri-armsoc -f xorg-dri-armsoc.list
%endif

%changelog
* Mon Aug 26 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.1.5-alt1
- 19.1.5

* Wed Jul 24 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.1.3-alt1
- 19.1.3

* Tue Jul 09 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.1.2-alt1
- 19.1.2

* Wed Jun 26 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.1.1-alt1
- 19.1.1

* Wed Jun 19 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.1.0-alt1
- 19.1.0

* Thu Jun 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.0.6-alt1
- 19.0.6

* Wed May 22 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.0.5-alt1
- 19.0.5

* Tue May 21 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4:19.0.4-alt2
- spec:
  - Switched to meson build ifrastructure;
  - Added support of ppc64le and mipsel architectures;
  - Fixed build on architectures without any specific support (build only
    swrast driver).
- mips*: patched gallium to set set mips{32,64}r2 as llvm target processor.
- amsoc: enabled kmsro driver.

* Mon May 13 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.0.4-alt1
- 19.0.4

* Thu Apr 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.0.3-alt1
- 19.0.3

* Wed Apr 17 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.0.2-alt1
- 19.0.2 (closes: #36592)

* Thu Mar 28 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.0.1-alt1
- 19.0.1

* Thu Mar 14 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:19.0.0-alt1
- 19.0.0

* Tue Feb 19 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:18.3.4-alt1
- 18.3.4

* Mon Feb 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:18.3.3-alt1
- 18.3.3

* Fri Jan 18 2019 Valery Inozemtsev <shrek@altlinux.ru> 4:18.3.2-alt1
- 18.3.2

* Wed Dec 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.3.1-alt1
- 18.3.1

* Mon Dec 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.3.0-alt1
- 18.3.0

* Mon Dec 03 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.2.6-alt1
- 18.2.6

* Fri Nov 16 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.2.5-alt1
- 18.2.5

* Thu Nov 01 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.2.4-alt1
- 18.2.4

* Mon Oct 22 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.2.3-alt1
- 18.2.3

* Thu Oct 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.2.2-alt1
- updated build dependencies

* Mon Oct 08 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.2.2-alt0.dummy
- 18.2.2
- enable libglvnd

* Mon Jul 02 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.1.3-alt1.S1
- 18.1.3

* Thu Jun 14 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.1.1-alt1.S1
- 18.1.1

* Thu May 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:18.1.0-alt1.S1
- 18.1.0

* Wed May 16 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:17.3.9-alt1.S1
- 17.3.9

* Thu Apr 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:17.3.8-alt1
- 17.3.8

* Mon Mar 26 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:17.3.7-alt1
- 17.3.7

* Tue Feb 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:17.3.6-alt1
- 17.3.6
- packed GLES3 includes (closes: #34580)

* Sun Jan 21 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:17.3.3-alt1
- 17.3.3

* Tue Jan 16 2018 Valery Inozemtsev <shrek@altlinux.ru> 4:17.3.2-alt1
- 17.3.2

* Thu Dec 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.7-alt1
- 17.2.7

* Mon Nov 27 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.6-alt1
- 17.2.6

* Sat Nov 11 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.5-alt1
- 17.2.5

* Wed Nov 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.4-alt1
- 17.2.4

* Thu Oct 19 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.3-alt1
- 17.2.3

* Tue Oct 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.2-alt1
- 17.2.2

* Mon Sep 18 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.1-alt1
- 17.2.1

* Wed Sep 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.0-alt2
- build with static llvm libs

* Tue Sep 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.2.0-alt1
- 17.2.0

* Tue Aug 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.1.6-alt1
- 17.1.6

* Mon Jul 24 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.1.5-alt1
- 17.1.5

* Mon Jul 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.1.4-alt1
- 17.1.4

* Thu Jun 22 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.1.3-alt1
- 17.1.3

* Thu Jun 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.1.1-alt2
- new subpackage xorg-dri-virgl

* Mon May 29 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.1.1-alt1
- 17.1.1

* Fri May 05 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.0.5-alt1
- 17.0.5

* Thu Apr 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.0.4-alt1
- 17.0.4

* Mon Apr 03 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.0.3-alt1
- 17.0.3

* Thu Mar 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.0.2-alt1
- 17.0.2

* Thu Mar 16 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.0.1-alt1
- 17.0.1

* Tue Feb 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:17.0.0-alt1
- 17.0.0

* Wed Feb 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:13.0.4-alt1
- 13.0.4

* Thu Jan 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 4:13.0.3-alt1
- 13.0.3

* Tue Nov 29 2016 Valery Inozemtsev <shrek@altlinux.ru> 4:13.0.2-alt1
- 13.0.2

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4:12.0.3-alt1
- 12.0.3

* Tue Sep 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4:12.0.2-alt1
- 12.0.2

* Mon Jul 11 2016 Valery Inozemtsev <shrek@altlinux.ru> 4:12.0.1-alt1
- 12.0.1

* Mon Apr 18 2016 Valery Inozemtsev <shrek@altlinux.ru> 4:11.1.3-alt1
- 11.1.3

* Thu Feb 25 2016 Valery Inozemtsev <shrek@altlinux.ru> 4:11.1.2-alt1
- 11.1.2

* Thu Jan 14 2016 Valery Inozemtsev <shrek@altlinux.ru> 4:11.1.1-alt1
- 11.1.1

* Wed Dec 16 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:11.1.0-alt1
- 11.1.0

* Mon Nov 23 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:11.0.6-alt1
- 11.0.6

* Sun Oct 25 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:11.0.4-alt1
- 11.0.4

* Mon Oct 05 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:11.0.2-alt1
- 11.0.2

* Sun Sep 13 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:11.0.0-alt1
- 11.0.0

* Sun Aug 23 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.6.5-alt1
- 10.6.5

* Wed Aug 12 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.6.4-alt1
- 10.6.4

* Sun Jul 12 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.6.2-alt1
- 10.6.2

* Mon Jun 29 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.6.1-alt1
- 10.6.1

* Sun Jun 07 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.7-alt1
- 10.5.7

* Wed May 27 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.6-alt1
- 10.5.6

* Wed May 13 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.5-alt1
- 10.5.5

* Tue Apr 14 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.3-alt1
- 10.5.3

* Mon Mar 30 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.2-alt1
- 10.5.2

* Sun Mar 15 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.1-alt1
- 10.5.1

* Sat Mar 07 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.0-alt1
- 10.5.0

* Mon Mar 02 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.0-alt0.rc3
- 10.5.0 RC3

* Fri Feb 27 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.5.0-alt0.rc2
- 10.5.0 RC2

* Sun Feb 22 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.4.5-alt1
- 10.4.5

* Tue Feb 10 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.4.4-alt1
- 10.4.4

* Mon Jan 26 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.4.3-alt1
- 10.4.3

* Tue Jan 13 2015 Valery Inozemtsev <shrek@altlinux.ru> 4:10.4.2-alt1
- 10.4.2

* Tue Dec 30 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.4.1-alt1
- 10.4.1

* Mon Dec 15 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.4.0-alt1
- 10.4.0

* Sun Dec 07 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.3.5-alt1
- 10.3.5

* Sat Nov 22 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.3.4-alt1
- 10.3.4

* Sun Nov 09 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.3.3-alt1
- 10.3.3

* Sat Oct 25 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.3.2-alt1
- 10.3.2

* Tue Oct 21 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.3.1-alt2
- enabled XA state tracker

* Mon Oct 13 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.3.1-alt1
- 10.3.1

* Sat Sep 20 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.3-alt1
- 10.3

* Sat Sep 20 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.8-alt1
- 10.2.8

* Sat Sep 06 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.7-alt1
- 10.2.7

* Tue Aug 26 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.6-alt1.1
- rebuild with libxcb-1.11

* Fri Aug 22 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.6-alt1
- 10.2.6

* Sun Aug 03 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.5-alt1
- 10.2.5

* Mon Jul 21 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.4-alt1
- 10.2.4

* Tue Jul 08 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.3-alt1
- 10.2.3

* Wed Jun 25 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.2-alt1
- 10.2.2

* Mon Jun 09 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.2.1-alt1
- 10.2.1

* Mon May 26 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1.4-alt1
- 10.1.4

* Sun May 11 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1.3-alt1
- 10.1.3

* Tue May 06 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1.2-alt1
- 10.1.2

* Sat Apr 19 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1.1-alt1
- 10.1.1

* Thu Apr 17 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1-alt2
- updated to 10.1 git.c755ebf

* Thu Mar 06 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1-alt1
- 10.1 release

* Sun Mar 02 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1-alt0.rc3
- 10.1 RC3

* Sat Feb 22 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1-alt0.rc2
- 10.1 RC2

* Mon Feb 10 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.1-alt0.rc1
- 10.1 RC1

* Tue Feb 04 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.0.3-alt1
- 10.0.3

* Fri Jan 10 2014 Valery Inozemtsev <shrek@altlinux.ru> 4:10.0.2-alt1
- 10.0.2

* Fri Dec 13 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:10.0.1-alt1
- 10.0.1

* Sun Dec 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:10.0-alt1
- 10.0 release

* Thu Nov 28 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:10.0-alt0.rc2
- 10.0 RC2

* Thu Nov 28 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.2.4-alt1
- 9.2.4

* Thu Nov 14 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.2.3-alt1
- 9.2.3

* Sat Oct 19 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.2.2-alt1
- 9.2.2

* Sun Oct 13 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.2.1-alt2
- enabled vdpau (closes: #29338)
- enabled XvMC

* Sun Oct 06 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.2.1-alt1
- 9.2.1 release

* Sat Sep 28 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.2-alt1.1
- updated to 9.2 git.4babf9b

* Thu Aug 29 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.2-alt1
- 9.2 release

* Thu Aug 29 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.6-alt2
- rebuild with llvm 3.3

* Sun Aug 04 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.6-alt1
- 9.1.6

* Wed Jul 24 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.5-alt1
- 9.1.5

* Tue Jul 02 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.4-alt1
- 9.1.4

* Fri Jun 28 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.3-alt3
- updated to 9.1 git.bf8053a2

* Tue Jun 04 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.3-alt2
- updated to 9.1 git.6de60dd

* Wed May 22 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.3-alt1
- 9.1.3

* Mon May 13 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.2-alt2
- updated to 9.1 git.1e043eb

* Wed May 01 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.2-alt1
- 9.1.2

* Sun Apr 07 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.1-alt2
- update to 9.1 git.c7720a2

* Thu Mar 21 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1.1-alt1
- 9.1.1

* Sat Mar 09 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1-alt3
- update to 9.1 git.ed29a98

* Wed Mar 06 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1-alt2
- updated to 9.1 git.09199c

* Sun Feb 24 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.1-alt1
- 9.1

* Sat Feb 23 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0.3-alt1
- 9.0.3

* Thu Feb 14 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0.2-alt2
- updated to 9.0 git.dddc5df

* Wed Jan 23 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0.2-alt1
- 9.0.2

* Fri Jan 18 2013 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0.1-alt2
- switch libEGL & libGLES (closes: #27875)

* Sat Nov 17 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0.1-alt1
- 9.0.1

* Sat Nov 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0-alt3
- intel-2012q4.1

* Tue Oct 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0-alt2
- enabled radeonsi gallium driver
- rebuild with wayland 1.0.0

* Tue Oct 09 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0-alt1
- 9.0 release

* Fri Sep 14 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0-alt0.2
- updated to 9.0 git.a5a8665

* Mon Sep 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:9.0-alt0.1
- 9.0-devel

* Wed Jul 11 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:8.0.4-alt1
- 8.0.4

* Mon May 21 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:8.0.3-alt1
- 8.0.3

* Thu Mar 22 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:8.0.2-alt1
- 8.0.2

* Fri Feb 17 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:8.0.1-alt1
- 8.0.1

* Fri Feb 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:8.0-alt1
- 8.0 release

* Sun Feb 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:8.0-alt0.2
- 8.0 RC2

* Mon Jan 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11.2-alt2
- updated to 7.11 git.9ae2499

* Mon Nov 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11.2-alt1
- 7.11.2

* Fri Nov 18 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11.1-alt1
- 7.11.1

* Sat Nov 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11-alt5
- updated to 7.11 git.5459781

* Sat Oct 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11-alt4
- updated to 7.11 git.4464ee1

* Mon Oct 17 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11-alt3
- updated to 7.11 git.b9cc916

* Mon Oct 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11-alt2
- updated to 7.11 git.7d2ff4a

* Mon Aug 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11-alt1
- 7.11 release

* Fri Jul 29 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11-alt0.4
- 7.11 RC4

* Wed Jul 20 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11-alt0.2
- 7.11 RC2

* Sat Jul 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.11-alt0.1
- 7.11 RC1

* Tue Jun 14 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.3-alt2
- 7.10.3 release

* Sun Jun 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.3-alt1
- 7.10.3

* Wed Jun 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.2-alt4
- updated to 7.10 git.4d08ca2

* Sun May 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.2-alt3
- updated to 7.10 git.c66ffcf

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.2-alt2
- updated to 7.10 git.73f4273

* Thu Apr 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.2-alt1
- 7.10.2

* Mon Apr 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.1-alt3
- updated to 7.10 git.ed5c9ae

* Fri Apr 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.1-alt2
- updated to 7.10 git.a947d9b

* Thu Mar 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10.1-alt1
- 7.10.1

* Tue Mar 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10-alt4
- updated to 7.10 git.f9f01e4

* Mon Feb 28 2011 Alexey Tourbin <at@altlinux.ru> 4:7.10-alt3
- rebuilt for pkgconfig
- enabled strict dependencies between subpackages

* Tue Feb 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10-alt2
- updated to 7.10 git.546aade

* Sat Jan 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.10-alt1
- 7.10

* Sat Jan 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9.1-alt1
- 7.9.1

* Wed Dec 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt9
- updated to 7.9 git.2fb170c

* Thu Dec 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt8
- updated to 7.9 git.4b19941

* Wed Dec 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt7
- updated to 7.9 git.5b28db2

* Mon Nov 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt6
- updated to 7.9 git.b6ae3d7

* Sun Nov 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt5
- enabled GLES library

* Wed Nov 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt4
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt3
- updated to 7.9 git.7f2d128

* Mon Oct 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt2
- intel: vblank always sync

* Tue Oct 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt1
- 7.9 release

* Wed Sep 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt0.rc2
- 7.9 RC2

* Mon Sep 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.9-alt0.rc1
- 7.9 RC1

* Sat Aug 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8.3-alt1
- enabled SELinux support

* Wed Aug 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8.3-alt0.pre1
- 7.8 branch 2010-08-24 (b7cea230b32da0cc072b1989bf070347656fce7c)

* Thu Jun 17 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8.2-alt1
- 7.8.2

* Wed Jun 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8.1-alt4
- 7.8 branch 2010-05-27 (fadc3c5c06bb3dc6de77cbcfa559392806a92819)

* Sat Apr 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8.1-alt3
- r600: added new r7xx pci ids (edff2e058571cfd8e1cb94e668c35f3d3cac4d80)

* Fri Apr 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8.1-alt2
- 7.8 branch 2010-04-09 (b22a00bff4aadd390dd8af6b5b05bd2833ec7f85):
  + mesa: fix instruction indexing bugs (fd.o bug 27566)

* Mon Apr 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8.1-alt1
- 7.8.1

* Fri Apr 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8-alt2
- GLX/DRI2: pass GLX drawable ID to dri2InvalidateBuffers

* Mon Mar 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8-alt1
- 7.8 release

* Tue Mar 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.8-alt0.rc2
- 7.8 RC2

* Sat Feb 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7.1-alt0.d5
- mesa_7_7_branch 2010-02-26 (7123f3d77ad7a62d9604d3febc42881e881452ea):
  + glx: fixed incorrect array stack memory allocation (fd.o bug 26768)

* Thu Feb 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7.1-alt0.d4
- mesa_7_7_branch 2010-02-25 (c0e8d443fe29bc81318144ab33a4e3a5afa88ed4)
  + closes: #22525

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7.1-alt0.d3
- mesa_7_7_branch 2010-02-18 (d437d905e6924ebc05ec9efe87e1e2c48d75bc13)

* Sat Feb 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7.1-alt0.d2
- mesa_7_7_branch 2010-02-06 (a1cac0732b53df8b08aa0ef1b440ea4398a467cc)

* Sat Jan 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7.1-alt0.d1
- 7.7.1-devel (f5145a6ec3e9086988ab8ec004276f845fecc3d9)

* Tue Dec 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7-alt1
- 7.7 release

* Wed Dec 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7-alt0.rc3
- 7.7 RC3

* Tue Dec 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7-alt0.rc2
- 7.7 RC2

* Tue Dec 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.7-alt0.rc1
- 7.7 RC1

* Tue Dec 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6.1-alt0.rc2
- 7.6.1 RC2

* Thu Nov 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6.1-alt0.rc1
- 7.6.1 RC1

* Mon Nov 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt9
- build for arm fixed

* Sun Nov 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt8
- mesa_7_6_branch 2009-10-28 (635ea8737488cc2fdcf0fcacb4ca39c8bc3b028a)

* Fri Oct 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt7
- mesa_7_6_branch 2009-10-14 (3f30b0709b5a71915df336194f9f805e4c306cef)

* Mon Oct 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt6
- i965:
  + Fixed the last valid address setting for the index buffer
  + Fixed the bounds emitted in the vertex buffer packets

* Sat Oct 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt5
- radeon: fixed scissor regression

* Sat Oct 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt4
- fixed default texture binding bug when a bound texture was deleted
- r300: Work around an issue with very large fragment programs on R500

* Fri Oct 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt3
- fixed memory leak when generating mipmaps for compressed textures

* Tue Sep 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt2
- 7.6 release

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.6-alt1.rc1
- 7.6 RC1

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5.2-alt1.rc1
- 7.5.2 RC1

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5.1-alt6
- mesa_7_5_branch 2009-09-24 (126d62edd18f22ff9e744efea81e0383cd0a19c5):
  + i915: Fix GetBufferSubData in the case of a system-memory BO

* Thu Sep 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5.1-alt5
- mesa_7_5_branch 2009-09-23 (2acd5de22651a3461c0576107c8e8fab1f01469a)

* Mon Sep 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5.1-alt4
- mesa_7_5_branch 2009-09-21 (5a0b29050f22b4475426a6f05a0338a7cdf546a0):
  + fixed crash in intel_flush()

* Wed Sep 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5.1-alt3
- mesa_7_5_branch 2009-09-16 (2921a2555d0a76fa649b23c31e3264bbc78b2ff5)
- libOSMesa-devel: packaged .so

* Wed Sep 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5.1-alt2
- new subpackage libOSMesa-devel (closes: #21499)

* Fri Sep 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5.1-alt1
- 7.5.1 release

* Mon Aug 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5-alt10
- fixed glXCreateGLXPixmap() for direct rendering

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5-alt9
- mesa_7_5_branch 2009-00-04 (3a221a9018f5166f249671ba41e8d44fe6b3301f):
  + Fixed swapbuffers jerkiness in Doom3/etc in Intel drivers.
  + Fixed front buffer rendering bug in Intel drivers.
  + Fixed minor GLX memory leaks.
  + Fixed some texture env / fragment program state bugs.

* Tue Jul 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5-alt8
- mesa_7_5_branch 2009-07-27 (3dbaf68bdc1f7427a60bdcc8da635ae7a27aa3cd)

* Sat Jul 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5-alt7
- 7.5 release

* Mon Jul 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5-alt6.rc4
- intel_2009q2_rc3

* Sat Jul 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5-alt5.rc4
- enabled glut

* Wed Jul 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 4:7.5-alt4.rc4
- removed r600 driver

* Mon Jul 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.5-alt3.rc4
- mesa_7_5_branch 2009-07-04 (fc6e02ce6210d6615af0058f1b57e7ee37a6527f)

* Sat Jun 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.5-alt2.rc4
- 7.5 RC4

* Wed Jun 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.5-alt2.rc3
- mesa_7_5_branch 2009-06-17 (ebe0796ba2d314202c30a1c9291a7e725c64b16a)
- merged r200/r300/r600 from r6xx-rewrite branch

* Sat Jun 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.5-alt1.rc3
- 7.5 RC3

* Fri May 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.5-alt1.rc2
- 7.5 RC2

* Fri May 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4.2-alt1
- 7.4.2 release

* Mon May 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4.1-alt4
- mesa_7_4_branch 2009-05-11 (2ff47b80f50deecc468c6baa34506a4718c38637)
  + fixed texture object mem leak during context destruction
  + fixed some i965 GLSL bugs
  + fixed an R300 driver texture object bad memory reference

* Sat May 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4.1-alt3
- mesa_7_4_branch 2009-05-01 (63375254979be322736fd3ea1c692c6ab08e817b)
  + fixed segfault when rendering to front buffer with DRI 1
  + fixed swrast texture rectangle bug when wrap mode = GL_CLAMP_TO_BORDER and filter mode = GL_LINEAR
  + fixed buffer overflow when parsing generic vertex attributes
  + fixed state validation bug for glCopyTex[Sub]Image()

* Fri Apr 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4.1-alt2
- merged mesa-7.2 branch

* Sat Apr 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4.1-alt1
- 7.4.1 release

* Thu Apr 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt7
- mesa_7_4_branch 2009-04-16 (a975da7aca34883bc2a723306fbf95a3365a65d8)
  + fixed point rendering in software rasterizer
  + fixed potential deadlock in object hash functions
  + fix a couple bugs surrounding front-buffer rendering with DRI2, but this is not quite complete.
  + fixed glPopAttrib() bug when restoring user clip planes
- intel_2009q1_rc3

* Mon Apr 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt6
- mesa_7_4_branch 2009-04-11 (49e0c74ddd91900fc4effb6d305d56e0563b456d):
  + fixed a two-sided lighting bug in fixed-function-to-GPU code generation
  + indexing the GLSL gl_EyePlane[] or gl_ObjectPlane[] arrays with a variable was broken
  + fixed incorrect texture unit bias in TXB instruction
  + glTexParameter settings weren't always propogated to drivers
  + assorted vertex/fragment program bug fixes

* Sat Mar 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt5
- 7.4 release

* Fri Mar 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt4.rc2
- intel_2009q1_rc2

* Thu Mar 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt3.rc2
- 7.4 RC2

* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt3.rc1
- 7.4 RC1
- libGLw: build with motif

* Tue Mar 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt3
- intel_2009q1_rc1

* Fri Mar 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt2
- mesa_7_4_branch 2009-03-06 (6801240205cd607eaa41b54d714fd1deeb4d8e3b)

* Fri Feb 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.4-alt1
- mesa_7_4_branch 2009-02-25 (4480e631cdb1d749cc0d921897a5df237ccdf997)
- build libOSMesa.so/libGLw.so

* Thu Jan 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.3-alt2
- 7.3 release

* Tue Jan 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.3-alt1.rc3
- 7.3 RC3

* Thu Jan 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.3-alt1.rc2
- 7.3 RC2

* Sat Jan 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.3-alt1.rc1
- 7.3 RC1

* Sat Jan 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt20
- openchrome: workaround to avoid the assert main/renderbuffer.c (close #18390)

* Sun Dec 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt19
- i965: Finish OPCODE_NOISEn instructions

* Fri Dec 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt18
- intel: check for null texture

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt17
- mesa: add missing break statements

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt16
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Nov 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt15
- intel: reset cliprect_mode to IGNORE_CLIPRECTS
- mesa: fix logic error in GLSL linker when looking for main() shaders

* Sat Nov 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt14
- added ppc support (Sergey Bolshakov)

* Thu Nov 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt13
- i965: implement missing OPCODE_NOISE3 instruction in fragment shaders

* Sun Nov 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt12
- i965: implement the missing OPCODE_NOISE1 and OPCODE_NOISE2 instructions

* Tue Oct 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt11
- i965: Allocate temporaries contiguously with other regs in fragment shaders

* Thu Oct 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt10
- drop %%_libdir/libGL.so.1.2

* Wed Oct 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt9
- fixed potential glTexImage(GL_DEPTH_COMPONENT) + convolution bugs

* Tue Oct 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt8
- i915: fix carsh in i830_emit_state

* Thu Oct 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt7
- glGetObjectParameter() sometimes generated wrong error codes

* Thu Oct 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt6
- fixed rare vertex color bug in software renderer

* Wed Oct 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt5
- fixed out of bounds memory writes to depth textures

* Mon Oct 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt4
- bufmgr_fake: Copy data from card memory back to backing store when mapping (close #17434)

* Sun Sep 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt3
- disable TTM API

* Sat Sep 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt2
- 7.2 release

* Sun Sep 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.2-alt1.rc1
- 7.2 RC1

* Sat Sep 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.1-alt7
- enabled TTM API
- added "--with-driver=dri" for configure (close #17093)

* Fri Sep 12 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.1-alt6
- i965: added support for G41 chipset which is another 4 series chipset

* Sat Sep 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.1-alt5
- intel: replsed VBLANK_ALWAYS_SYNC to VBLANK_DEF_INTERVAL_0

* Fri Sep 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.1-alt4
- separate libmesa

* Wed Sep 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.1-alt3
- obsoletes libGLU < %%version-%%release

* Fri Aug 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.1-alt2
- update libGL.so.1 links for both architectures (close #16227)

* Wed Aug 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 3:7.1-alt1
- 7.1 release

* Thu Aug 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.4-alt8
- fixed float blend bug

* Mon Aug 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.4-alt7
- rearrange some code in _mesa_BindTexture() to fix error detection

* Sat Aug 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.4-alt6
- 7.0.4 release

* Fri Aug 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.4-alt5
- mesa_7_0_branch 2008-08-08:
  + fix out-of-bounds memory reads in swizzle_copy()
  + fix some FBO/texture queries

* Fri Aug 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.4-alt4
- mesa_7_0_branch 2008-07-29
* Mon Jul 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.4-alt3
- mesa_7_0_branch 2008-07-14:
  + Fixed broken all(bvec2) GLSL function, added misc missing bvec constructors
  + ARB program "state.clip[n].plane" didn't parse correctly
  + Fixed broken glGetUniformiv()

* Wed Jun 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.4-alt2
- add support for Intel 4 series chipsets

* Tue Jun 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.4-alt1
- 7.0.4

* Mon Jun 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt12
- mesa_7_0_branch 2008-06-13

* Mon Jun 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt11
- renamed xorg-x11-dri-* to xorg-dri-*
- add support for GL shading language in I965 driver

* Mon Jun 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt9
- mesa_7_0_branch 2008-05-30:
  + Fix segfault in _save_OBE_DrawElements() when using VBO and display list
  + i965 some fixes

* Tue May 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt8
- mesa_7_0_branch 2008-05-27:
  + Fixed a per-vertex glMaterial bug which could cause bad lighting
  + Fixed potential crash in AA/smoothed triangle rendering when using a fragment shader

* Thu May 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt7
- fixed headers install (close #15570)

* Wed May 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt6
- add E7221 variant to i915

* Fri May 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt5
- mesa_7_0_branch 2008-04-30
- new subpackage Mesa-sources

* Sun Apr 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt4
- install dri_interface.h

* Sat Apr 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt3
- 7.0.3 release

* Wed Apr 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt2.rc3
- 7.0.3 RC3
* Sun Mar 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt2.rc2
- separate xorg-x11-dri-ati for xorg-x11-drv-ati-6.8.0

* Fri Feb 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.3-alt1.rc2
- 7.0.3RC2

* Sun Feb 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.2-alt8
- fixed ddx version in nouveau driver

* Sat Jan 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.2-alt7
- disable build libglut, libGLw

* Sat Jan 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.2-alt6
- arm build support

* Sat Dec 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.2-alt5
- fix GL_LINE_LOOP with drivers using own render pipeline stage
- fixed typo in glw.pc

* Fri Nov 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.2-alt4
- added GLw includes
- added pkgconfig files
- spec cleanup

* Sun Nov 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.2-alt3
- make sure a valid value is returned for GLX_BIND_TO_MIPMAP_TEXTURE_EXT

* Fri Nov 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.2-alt2
- rebuild with libdrm-2.4.0

* Sun Nov 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.2-alt1
- 7.0.2 is a stable release with bug fixes since version 7.0
- drop upstream patches

* Mon Nov 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.1-alt6
- Mesa-7.0.1-git-memleak-in-SSE.patch:
  + Fix mem leak in SSE code generation path and don't crash
    if _mesa_exec_malloc() returns NULL.

* Thu Oct 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.1-alt5
- added Mesa-7.0.1-r200-settexoffset.patch,
	Mesa-7.0.1-r300-fix-writemask.patch

* Sun Oct 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.1-alt4
- build with xcb

* Fri Sep 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.1-alt3
- added "Requires(post): coreutils" for libmesa (close #12959)
- update nouveau dri driver from GIT

* Wed Sep 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.1-alt2
- returned Mesa-7.0.1-I945_GME-G33-Q33-Q35.patch
- update nouveau dri driver from GIT

* Sat Aug 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.1-alt1
- 7.0.1 bug-fix release

* Wed Aug 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt9
- added Mesa-7.0-git-MAT_ATTRIB_MAX-bug11811.patch,
	Mesa-7.0-git-stencil-value-masking-bug11805.patch,
	Mesa-7.0-git-vbo_split_copy-bug9962.patch,
	Mesa-7.0-git-potential-NULL-dereference-bug11880.patch,
	Mesa-7.0-git-swizzle-error-test-bug11881.patch
- update nouveau dri driver from GIT (requires libdrm-2.3.1-alt5)
- fixed requires for xorg-x11-dri-*

* Wed Aug 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt8
- added Mesa-7.0-git-memleak-bug11791.patch,
	Mesa-7.0-git-memleak-bug11793.patch

* Wed Aug 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt7
- added Mesa-7.0-git-failure-caused-by-undeclared-variable-bug11783.patch,
	Mesa-7.0-git-glGetAttribLocation-bug11774.patch

* Mon Jul 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt6
- added Mesa-7.0-git-glPointParameteriv-bug11754.patch

* Fri Jul 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt5
- added Mesa-7.0-git-fragment-program-bug11733.patch,
	Mesa-7.0-git-function-call-bug11731.patch

* Mon Jul 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt4
- added Mesa-7.0-git-GLX_STEREO-handling-bug11705.patch
- update nouveau dri driver

* Mon Jul 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt3
- added Mesa-7.0-git-depth-mix-up-bug11577.patch,
	Mesa-7.0-git-swizzle-related-bug11534.patch,
	Mesa-7.0-git-shader-info-bug11588.patch

* Tue Jul 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt2
- added Mesa-7.0-git-image-bug11448.patch,
	Mesa-7.0-git-GL_DOT3_RGBA-bug11030.patch

* Sat Jun 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0-alt1
- 7.0 is released. This is a stable release featuring OpenGL 2.1 support.

* Wed Jun 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.3-alt8
- add support for the G33, Q33, and Q35 chipsets

* Thu May 31 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.3-alt7
- Mesa-6.5.3-git-point-attentuation-bug11042.patch: fix point attentuation problem
- Mesa-6.5.3-git-GL_TEXTURE_LOD_BIAS-bug11049.patch: restore GL_TEXTURE_LOD_BIAS in _mesa_PopAttrib()
- add support for the i945GME, i965GME and i965GLE chipsets

* Tue May 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.3-alt6
- build without xcb

* Sat May 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.3-alt5
- added Mesa-6.5.3-git-STATE_HALF_VECTOR-bug10987.patch,
	Mesa-6.5.3-git-i915-s3tc-mipmaps-bug10968.patch

* Tue May 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.3-alt4
- added Mesa-6.5.3-git-glXGetArrayType-return-type-bug10938.patch

* Wed May 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.3-alt3
- build with xcb

* Sun Apr 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.3-alt2
- added Mesa-6.5.3-git-r300-page-flipping.patch: Page flipping fixes

* Fri Apr 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.3-alt1
- 6.5.3 release

* Mon Apr 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt21
- added menu file and icons for glxgears (close #11355)

* Tue Mar 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt20
- use movdqu instead of movdqa for unaligned load avoiding a segfault (upstream bug 10265) 

* Tue Mar 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt19
- added Mesa-6.5.2-git-n_dot_h-bug9977.patch,
	Mesa-6.5.2-git-fix-textrel.patch
- spec cleanup

* Wed Feb 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt18
- added Mesa-6.5.2-git-tnl-bug9856.patch,
	Mesa-6.5.2-git-unichrome-CN700.patch,
	Mesa-6.5.2-git-fd-bug9684.patch

* Mon Feb 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt17
- added Mesa-6.5.2-git-main-mem-leak.patch,
	Mesa-6.5.2-git-glxext-mem-leak.patch

* Mon Feb 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt16
- added Mesa-6.5.2-git-i965-glxswapcontrol.patch,
	Mesa-6.5.2-git-CheckArrayBounds-bug9285.patch,
	Mesa-6.5.2-git-GetVertexAttribPointerv-bug9628.patch,
	Mesa-6.5.2-git-i965-static-buffer-bug9604.patch,
	Mesa-6.5.2-git-radeon-radeonClear.patch,
	Mesa-6.5.2-git-i915-vertexfog-bug9686.patch

* Tue Jan 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt15
- added Mesa-6.5.2-git-i915tex-randr-resizing.patch,
	Mesa-6.5.2-git-i915tex-relocation.patch

* Fri Jan 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt14
- added Mesa-6.5.2-git-i965-bug9625.patch

* Sun Jan 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt13
- added Mesa-6.5.2-git-r300-vertex-position.patch
- fixed Mesa-6.5.2-git-r300-fragprog-correct.patch

* Tue Jan 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt12
- added Mesa-6.5.2-git-PolygonMode-bug9578.patch,
	Mesa-6.5.2-git-VBO-state-bug9445.patch,
	Mesa-6.5.2-git-32bit-Z-buffer.patch,
	Mesa-6.5.2-git-i965-inteldebug.patch,
	Mesa-6.5.2-git-i965-flowmode.patch,
	Mesa-6.5.2-git-i965-ARB_occlusion_query.patch,
	Mesa-6.5.2-git-i965-maxprim.patch,
	Mesa-6.5.2-git-i965-bug9201.patch

* Thu Jan 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt11
- added Mesa-6.5.2-git-r300-fragprog-correct.patch

* Mon Jan 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt10
- added Mesa-6.5.2-git-r300-fragprog.patch,
	Mesa-6.5.2-git-i915tex-advertising.patch,
	Mesa-6.5.2-git-i965-sarea.patch

* Mon Dec 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt9
- fixed requires for libmesa
- added Mesa-6.5.2-git-swrast-bug9345.patch

* Thu Dec 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt8
- added Mesa-6.5.2-git-i965-fix-crash-wine.patch,
	Mesa-6.5.2-git-mach64-bug7260.patch,
	Mesa-6.5.2-git-mach64-bug7790.patch,
	Mesa-6.5.2-git-mach64-bug7861.patch,
	Mesa-6.5.2-git-r200-WoW-bug8250.patch
- added -fno-strict-aliasing to CFLAGS (fixed #10418)

* Sun Dec 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt7
- added Mesa-6.5.2-git-i965-bug9045.patch,
	Mesa-6.5.2-git-i965-bug9237.patch

* Thu Dec 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt6
- added Mesa-6.5.2-git-i915tex-intelWindowMoved.patch

* Sun Dec 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt5
- 6.5.2 release

* Sat Dec 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt4
- CVS snapshot 2006-12-01:
  + Fixed glDrawPixels(GL_COLOR_INDEX, GL_BITMAP) segfault
  + Fixed some gluBuild2DMipmaps() bugs
  + Fixed broken "mgl" name mangling
  + Fixed indirect rending was broken for glMap* functions
  + Added support for ARB_occlusion_query to the tdfx driver

* Thu Nov 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt3
- CVS snapshot 2006-11-15:
  + Fixed glGetVertexAttribfvARB bug 8883
  + Implemented glGetUniform[fi]vARB() functions

* Tue Nov 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt2
- CVS snapshot 2006-11-14:
  + fragment.fogcoord register didn't always contain the correct value
  + RGBA logicops didn't work reliably in some DRI drivers
  + Fixed broken RGBA LogicOps in Intel DRI drivers
  + Fixed some fragment program bugs in Intel i915 DRI driver
  + New DRI memory manager system. Currently used by the i915tex driver.
- enabled TLS support for x86_64

* Wed Oct 18 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.2-alt1
- CVS snapshot 2006-10-18:
  + fixed invalid memory read while rendering textured points
  + fixed problems with freebsd-dri configuration
  + Mesa's fake glxGetCurrentContext() wasn't thread-aware
  + OPTION NV_position_invariant didn't work in NV vertex programs
  + glDrawPixels into a user-created framebuffer object could crash Xlib driver
  + Line clipping was broken in some circumstances

* Wed Oct 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.1-alt8
- build to GLX_USE_TLS to enable TLS support.

* Wed Oct 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.1-alt7
- rebuild with glibc-2.5

* Sat Sep 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.1-alt6
- 6.5.1 release

* Thu Sep 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.1-alt5
- added %%_optlevel 3

* Mon Sep 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.1-alt4
- added -pipe -O2 to optflags
- added -fPIC to optflags for %ix86
- added mesa-6.4.1-radeon-use-right-texture-format.patch

* Thu Aug 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.1-alt3
- build mga, savage, sis, tdfx for x86_64

* Wed Aug 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.1-alt2
- 6.5.1
- build i810, mga, savage, sis, tdfx for i586 only

* Sat Jun 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.5.1-alt0.cvs20060612
- enabled arch optimization for x86

* Sat Apr 08 2006 Valery Inozemtsev <shrek@altlinux.ru> 2:6.4.2-alt1
- rollback 6.4.2

* Sun Apr 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.5-alt2
- enabled arch optimization

* Sat Apr 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.5-alt1
- 6.5

* Tue Mar 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.2-alt3
- added obsoletes Mesa to libmesa

* Sun Mar 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.2-alt2
- removed not used i830_dri.so

* Thu Feb 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.2-alt1
- 6.4.2

* Mon Feb 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.1-alt6
- fixed provides

* Wed Jan 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.1-alt5
- fixed LIBGL_DRIVERS_DIR for x86_64 

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.1-alt4
- added Provides libGLU-devel to libmesa-devel (#8892)

* Fri Jan 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.1-alt3
- set LIBGL_DRIVERS_DIR to %_libdir/X11/modules/dri

* Thu Jan 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.1-alt2
- fixed requires

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 1:6.4.1-alt1
- 6.4.1

* Tue Nov 22 2005 Valery Inozemtsev <shrek@altlinux.ru> 6.4-alt0.1
- 6.4

* Fri Dec 17 2004 Valery Inozemtsev <shrek@altlinux.ru> 6.2.1-alt1
- 6.2.1

* Wed Sep 22 2004 Valery Inozemtsev <shrek@altlinux.ru> 6.1-alt1
- 6.1
- build demos, glut only

* Wed Apr 28 2004 Anton Farygin <rider@altlinux.ru> 5.0.2-alt2
- removed all compat libMesaGL symlinks (it's need for ldconfig from glibc 2.3)

* Fri Apr 23 2004 Anton Farygin <rider@altlinux.ru> 5.0.2-alt1
- updated to Mesa 5.0.2
- specfile cleanup
- updated glx to glx-xf4-20031008

* Thu Oct 02 2003 Rider <rider@altlinux.ru> 5.0.1-alt7
- enable build libOSMesa (fixed bug #3090)

* Wed Oct 01 2003 Rider <rider@altlinux.ru> 5.0.1-alt6
- fix requires and provides

* Fri Sep 26 2003 Anton Farygin <rider@altlinux.ru> 5.0.1-alt5
- added check in to libGLwrapper for ATI math based video cards

* Tue Jul 29 2003 Peter Novodvorsky <nidd@altlinux.com> 5.0.1-alt4
- updated ALT_MESA and MESA versions.

* Wed Jul 16 2003 Peter Novodvorsky <nidd@altlinux.com> 5.0.1-alt3
- updated Mesa to 5.0.1
- added fglrx support in GLwrapper

* Thu Oct 03 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.0.3-alt3
- Rebuild with gcc 3.2

* Wed Sep 18 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.0.3-alt2
- Fixed linking libraries
- Removed .la files from devel package

* Fri Sep 06 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.0.3-alt1
- 4.0.3
- Now we building libGLU packages
- build with gcc 2.96
- Fixed rpath

* Tue Apr 16 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Mon Mar 18 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.0.1-alt1
- 4.0.1
- Some spec cleanup

* Fri Nov 16 2001 Konstantin Volckov <goldhead@altlinux.ru> 4.0-alt1
- 4.0

* Tue Jul 10 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.5-alt2
- Fixed bug with files in Mesa-demos
- Compile c++ files with optimization
- Added SSE optimization
- Return back libGLU and added libGLU & libGLU-devel packages, define it
  for build it
- Disabled osmesa build
- Fixed SGIX features in libglut - they're not present in Mesa 3.4.2

* Sat Jun 30 2001 Mikhail Zabaluev <mhz@altlinux.ru> 3.5-alt1.1
- added -fno-exceptions -fno-rtti to optflags

* Wed Jun 27 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.5-alt1
- New version
- Some spec cleanup
- Added MesaOS to Mesa package

* Thu Jun 7 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.4.2-alt1
- New Mesa version
- Remove changelog messages before Jan 2001
- Remove libGLU library. It's now in XFree86-libs package.
- Added new packages - libglut, libglut-devel, glx, libGLwrapper
- Patched libGLwrapper for nVidia commercial driver compatibility
- Some spec cleanup

* Sun Feb 25 2001 AEN <aen@logic.ru>	3.4.1-ipl2mdk
- build 3.4.1 in RE environment
- cleanup spec
