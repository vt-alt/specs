%define arm_release 26
%define baikal_sdk_version 4.2
# It's a binary blob we've got from a vendor, so don't bother to
# produce debuginfo packages
%global __find_debuginfo_files %nil

Name: mali-drv-baikalm
Version: %arm_release.%baikal_sdk_version
Release: alt2

Summary: Proprietary GPU drivers for BE-M1000 SoC, userspace part
License: Proprietary
Group: System/Kernel and hardware

ExclusiveArch: aarch64
ExclusiveOS: Linux

Source: %name-%version.tar

BuildRequires: gcc
BuildRequires: libdrm-devel
BuildRequires: libgbm-devel
BuildRequires: chrpath
BuildRequires: libwayland-client.so.0()(64bit)

Requires: libdrm.so.2()(64bit)
Requires: libwayland-client.so.0()(64bit)
Requires: libwayland-server.so.0()(64bit)

%description
Proprietary Mali-T628 GPU drivers for BE-M1000 (Baikal-M) SoC.
This package provides GL ES implementation. The kernel mode Mali
driver mali_kbase is required but is NOT shipped with this package.

%prep
%setup

%build
%make_build

%install
make install DESTDIR=%buildroot
chrpath -d %buildroot/usr/lib64/mali/liboffline_compiler_api_gles.so

%files
/etc/ld.so.conf.d/mali.conf
/usr/lib64/mali/libEGL.so.1
/usr/lib64/mali/libgbm.so.1
/usr/lib64/mali/libgbm.so.1.0.0
/usr/lib64/mali/libGLESv2.so.2
/usr/lib64/mali/libmali.so
/usr/lib64/mali/liboffline_compiler_api_gles.so
/usr/lib64/mali/libwayland-egl.so.1

%post
ldconfig

%changelog
* Mon May 25 2020 Alexey Sheplyakov <asheplyakov@altlinux.org> 26.4.2-alt2
- Disabled debuginfo

* Sun May 24 2020 Alexey Sheplyakov <asheplyakov@altlinux.org> 26.4.2-alt1
- Initial build
