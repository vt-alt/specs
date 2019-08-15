Name: kvdo
Version: 6.2.1.138
Release: alt1

Summary: Kernel Modules for Virtual Data Optimizer
License: GPLv2+
Url: http://github.com/dm-vdo/kvdo
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
* Fri Aug 09 2019 Vitaly Chikunov <vt@altlinux.org> 6.2.1.138-alt1
- Update to 6.2.1.138.

* Fri Feb 22 2019 Vitaly Chikunov <vt@altlinux.org> 6.2.0.293-alt1
- Update to 6.2.0.293.

* Wed Dec 05 2018 Vitaly Chikunov <vt@altlinux.org> 6.2.0.273-alt1
- First import.

