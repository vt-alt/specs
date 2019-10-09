
%define sover 1
%define libnvidia_egl_wayland libnvidia-egl-wayland%sover

Name: egl-wayland
Version: 1.1.4
Release: alt1
Epoch: 1

Group: System/Libraries
Summary: Wayland EGL External Platform library
Url: https://github.com/NVIDIA/%name
License: MIT

Source0: %name-%version.tar
Source1: 10_nvidia_wayland.json

# Automatically added by buildreq on Fri Jul 12 2019 (-bi)
# optimized out: elfutils glibc-devel-static glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libstdc++-devel libwayland-client libwayland-client-devel libwayland-server perl pkg-config python-base python-modules python3 python3-base python3-dev rpm-build-python3 sh4 wayland-devel xorg-proto-devel
#BuildRequires: eglexternalplatform-devel gcc-c++ libEGL-devel libstdc++-devel-static libwayland-egl-devel libwayland-server-devel python3-module-mpl_toolkits
BuildRequires: autoconf-archive
BuildRequires: eglexternalplatform-devel libEGL-devel
BuildRequires: libwayland-egl-devel libwayland-server-devel libwayland-client-devel wayland-devel

%description
%summary

%package -n %libnvidia_egl_wayland
Summary: %summary
Group: System/Libraries
Provides: libnvidia-egl-wayland = %version-%release
Provides: nvidia-egl-wayland = %version-%release
%description -n %libnvidia_egl_wayland
%summary

%package devel
Group: Development/Other
Summary: Wayland EGL External Platform library development package
%description devel
Wayland EGL External Platform library development package

%prep
%setup -q
%autoreconf

%build
%configure
%make_build

%install
%makeinstall_std
install -m 0755 -d %buildroot/%_datadir/egl/egl_external_platform.d/
install -pm 0644 %SOURCE1 %buildroot/%_datadir/egl/egl_external_platform.d/

%files -n %libnvidia_egl_wayland
%doc README.md COPYING
%_libdir/libnvidia-egl-wayland.so.%sover
%_libdir/libnvidia-egl-wayland.so.*
%_datadir/egl/egl_external_platform.d/10_nvidia_wayland.json

%files devel
%_libdir/lib*.so
%_datadir/pkgconfig/wayland-eglstream*.pc
%_datadir/wayland-eglstream/

%changelog
* Wed Oct 09 2019 Sergey V Turchin <zerg@altlinux.org> 1:1.1.4-alt1
- new version

* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 1:1.1.3-alt1
- initial build

