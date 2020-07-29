%set_verify_elf_method textrel=relaxed

%define tbname         NVIDIA-Linux-x86_64
%define dirsuffix %nil

%define nvidia_ml_sover 1
%define nvidia_ptxjitcompiler_sover 1
%define nvidia_cuda_sover 1
%define nvidia_opencl_sover 1
%define nvidia_egl_wayland_sover 1
%define nvidia_egl_wayland_libver 1.0.2
%define libnvidia_egl_wayland libnvidia-egl-wayland%nvidia_egl_wayland_sover

%ifarch %ix86
%define subd ./32
%else
%define subd ./
%endif

Name: nvidia_glx_src
Version: 450.57
Release: alt1

Source0: null
Source201: ftp://download.nvidia.com/XFree86/Linux-x86/%version/NVIDIA-Linux-x86_64-%version.run

BuildRequires: kernel-build-tools rpm-macros-alternatives
BuildRequires: libXext-devel libEGL-devel
BuildRequires: libwayland-client-devel libwayland-server-devel
#BuildRequires: libGLdispatch libGLX
ExclusiveArch: %ix86 x86_64


Group: System/Kernel and hardware
Summary: NVIDIA drivers and OpenGL libraries for XOrg X-server
Summary(ru_RU.UTF-8): Драйверы NVIDIA и библиотеки OpenGL для Х-сервера XOrg
Url: http://www.nvidia.com
License: NVIDIA
%description
Sources for nvidia_glx package

%package -n ocl-nvidia
Group: System/Libraries
#BuildArch: noarch
Summary: nvidia library
Requires: libnvidia-opencl
Requires: libnvidia-compiler
Requires: libnvidia-ptxjitcompiler
Requires: libnvidia-ml
%description -n ocl-nvidia
nvidia OpenCL library

%package -n libnvidia-ptxjitcompiler
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-ptxjitcompiler = %version-%release
%description -n libnvidia-ptxjitcompiler
nvidia library

%package -n libnvidia-ml
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-ml = %version-%release
%description -n libnvidia-ml
nvidia library

%package -n libnvidia-compiler
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-compiler = %version-%release
%description -n libnvidia-compiler
nvidia library

%package -n libcuda
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-cuda = %EVR
Obsoletes: libnvidia-cuda < %EVR
%description -n libcuda
nvidia CUDA library

%package -n libnvidia-opencl
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-opencl = %version-%release
Requires: ocl-icd
%description -n libnvidia-opencl
nvidia OpenCL library

%package -n libnvcuvid
Group: System/Libraries
Summary: nvidia library
Provides: libnvidia-nvcuvid = %version-%release
%description -n libnvcuvid
nvidia library

%package -n libnvidia-encode
Group: System/Libraries
Summary: nvidia library
%description -n libnvidia-encode
nvidia library

%prep
%setup -T -c -n %tbname-%version%dirsuffix
rm -rf %_builddir/%tbname-%version%dirsuffix
cd %_builddir
sh %SOURCE201 -x
cd %tbname-%version%dirsuffix

pushd kernel
rm -rf precompiled
popd

%build

%install
# install libraries
mkdir -p %buildroot/%_libdir/
install -m 0644 %subd/libcuda.so.%version %buildroot/%_libdir/
install -m 0644 %subd/libnvidia-opencl.so.%version %buildroot/%_libdir/
install -m 0644 %subd/libnvidia-compiler.so.%version %buildroot/%_libdir/
install -m 0644 %subd/libnvidia-ptxjitcompiler.so.%version %buildroot/%_libdir/
install -m 0644 %subd/libnvidia-ml.so.%version %buildroot/%_libdir/
install -m 0644 %subd/libnvcuvid.so.%version %buildroot/%_libdir/
install -m 0644 %subd/libnvidia-encode.so.%version %buildroot/%_libdir/
mkdir -p %buildroot/%_sysconfdir/OpenCL/vendors/
install -m 0644 nvidia.icd %buildroot/%_sysconfdir/OpenCL/vendors/

%files -n ocl-nvidia

%files -n libnvidia-compiler
%_libdir/libnvidia-compiler.so.%version

%files -n libnvidia-ptxjitcompiler
%_libdir/libnvidia-ptxjitcompiler.so.%version
%_libdir/libnvidia-ptxjitcompiler.so.%{nvidia_ptxjitcompiler_sover}

%files -n libnvidia-ml
%_libdir/libnvidia-ml.so.%version
%_libdir/libnvidia-ml.so.%{nvidia_ml_sover}

%files -n libcuda
%_libdir/libcuda.so.%{nvidia_cuda_sover}
%_libdir/libcuda.so.%version

%files -n libnvidia-opencl
%_libdir/libnvidia-opencl.so.%{nvidia_opencl_sover}
%_libdir/libnvidia-opencl.so.%version
%_sysconfdir/OpenCL/vendors/nvidia.icd

%files -n libnvcuvid
%_libdir/libnvcuvid.so.%{nvidia_opencl_sover}
%_libdir/libnvcuvid.so.%version

%files -n libnvidia-encode
%_libdir/libnvidia-encode.so.%{nvidia_opencl_sover}
%_libdir/libnvidia-encode.so.%version

%changelog
* Fri Jul 24 2020 Sergey V Turchin <zerg@altlinux.org> 450.57-alt1
- new version

* Fri Jul 17 2020 Sergey V Turchin <zerg@altlinux.org> 440.100-alt1
- new version

* Thu Apr 16 2020 Sergey V Turchin <zerg@altlinux.org> 440.82-alt1
- new version

* Mon Feb 10 2020 Sergey V Turchin <zerg@altlinux.org> 440.59-alt1
- new version

* Thu Jan 09 2020 Sergey V Turchin <zerg@altlinux.org> 440.44-alt1
- new version
- package libnvidia-encode, libnvcuvid

* Tue Nov 26 2019 Sergey V Turchin <zerg@altlinux.org> 440.36-alt1
- new version

* Wed Nov 06 2019 Sergey V Turchin <zerg@altlinux.org> 440.31-alt1
- new version

* Mon Sep 30 2019 Sergey V Turchin <zerg@altlinux.org> 430.50-alt1
- new version

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 430.34-alt1
- new version

* Thu Mar 14 2019 Sergey V Turchin <zerg@altlinux.org> 410.104-alt1
- new version

* Wed Jan 30 2019 Sergey V Turchin <zerg@altlinux.org> 410.93-alt1
- new version

* Thu Dec 13 2018 Sergey V Turchin <zerg@altlinux.org> 410.78-alt1
- new version

* Wed Dec 05 2018 Sergey V Turchin <zerg@altlinux.org> 410.73-alt1
- new version

* Thu Sep 20 2018 Sergey V Turchin <zerg@altlinux.org> 390.87-alt1
- new version

* Fri Jun 08 2018 Sergey V Turchin <zerg@altlinux.org> 390.67-alt1
- new version

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 390.59-alt1
- new version

* Thu Apr 19 2018 Sergey V Turchin <zerg@altlinux.org> 390.48-alt1
- new version

* Wed Feb 21 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt3
- require libnvidia-ml

* Mon Feb 19 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt2
- added pkgs:
libnvidia-cuda
libnvidia-compiler
libnvidia-ptxjitcompiler
libnvidia-ml

* Fri Feb 16 2018 Oleg Solovyov <mcpain@altlinux.org> 390.25-alt1
- init
