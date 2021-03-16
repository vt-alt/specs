# SPDX-License-Identifier: GPL-2.0-only

Name: kernel-source-hifc
Version: 3.5.0.11
Release: alt1
Summary: Huawei Hifc PCI Express Linux driver
License: GPL-2.0-only
Group: Development/Kernel
Url: https://openeuler.org/en/
Vcs: https://github.com/openeuler-mirror/kernel.git
# Vcs: https://gitee.com/openeuler/kernel.git

Source0: %name-%version.tar
BuildArch: noarch
ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-un-def
BuildRequires: kernel-headers-modules-std-def

%description
%summary

%prep
%setup

%install
install -pDm0644 %_sourcedir/%name-%version.tar %kernel_srcdir/%name-%version.tar

%check
make -C /lib/modules/*-un-def-*/build  M=$PWD/drivers/scsi/huawei/hifc modules CONFIG_SCSI_FC_HIFC=m -j
make -C /lib/modules/*-std-def-*/build M=$PWD/drivers/scsi/huawei/hifc modules CONFIG_SCSI_FC_HIFC=m -j

%files
%kernel_src/%name-%version.tar

%changelog
* Thu Mar 04 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.5.0.11-alt1
- First import of 3.5.0.11 from openEuler kernel-4.19.

