Name: kvdo
Version: 6.2.5.41
Release: alt1

Summary: Kernel Modules for Virtual Data Optimizer
License: GPL-2.0-only
Url: https://github.com/dm-vdo/kvdo
# merged with from https://github.com/rhawalsh/kvdo.git
Group: System/Kernel and hardware
Source0: %name-%version.tar
BuildRequires(pre): rpm-build-kernel

%description
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

%package -n kernel-source-%name
Summary: Kernel Modules for Virtual Data Optimizer (source)
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
Source code for the Virtual Data Optimizer (VDO) which is a device mapper
target that delivers block-level deduplication, compression, and thin
provisioning.

%prep

%build

%install
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/kernel-source-%name-%version.tar

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%changelog
* Mon Jul 05 2021 Alexey Shabalin <shaba@altlinux.org> 6.2.5.41-alt1
- 6.2.5.41

* Tue Mar 02 2021 Alexey Shabalin <shaba@altlinux.org> 6.2.4.26-alt2
- Sync with rhawalsh patches:
  + Removed currentTime() from exported symbols list for uds.
  + Temporarily disabled frame size checks.

* Wed Dec 16 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.4.26-alt1
- Update to 6.2.4.26 with rhawalsh patches.

* Mon Sep 07 2020 Alexey Shabalin <shaba@altlinux.org> 6.2.3.114-alt1
- Update to 6.2.3.114 with rhawalsh patches.

* Tue Apr 07 2020 Vitaly Chikunov <vt@altlinux.org> 6.2.2.117-alt1
- Update to 6.2.2.117 with rhawalsh patches.

* Tue Oct 22 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.2.18-alt1
- Update to 6.2.2.18

* Fri Aug 09 2019 Vitaly Chikunov <vt@altlinux.org> 6.2.1.138-alt1
- Update to 6.2.1.138.

* Fri Feb 22 2019 Vitaly Chikunov <vt@altlinux.org> 6.2.0.293-alt1
- Update to 6.2.0.293.

* Wed Dec 05 2018 Vitaly Chikunov <vt@altlinux.org> 6.2.0.273-alt1
- First import.

