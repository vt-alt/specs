Name: drbd9
Version: 9.0.23
Release: alt0.rc3.1
%define githash 2d2e11074a6e1a4d2f3c0cbb6ca6db32f0c42a5d

Summary: The Linux kernel code for DRBD9.
License: GPLv2
Group: System/Kernel and hardware
BuildArch: noarch

Url: https://github.com/LINBIT/drbd.git
Source0: %name-%version.tar
Source1: %name-headers-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-kernel kernel-headers-modules-std-def
BuildRequires: coccinelle >= 1.0.8
BuildRequires: libelf-devel

%description
DRBD, developed by LINBIT, is a software that allows RAID 1 functionality over
TCP/IP and RDMA for GNU/Linux. DRBD is a block device which is designed
to build high availability clusters and software defined storage by providing
a virtual shared device which keeps disks in nodes synchronised using TCP/IP
or RDMA. This simulates RAID 1 but avoids the use of uncommon hardware
(shared SCSI buses or Fibre Channel).

%package -n kernel-source-%name
Summary: The Linux kernel code for DRBD9.
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-%name
The Linux kernel code for DRBD9.

%prep
%setup -q
tar -xf %SOURCE1 -C drbd/drbd-headers
echo "GIT-hash: %githash" >drbd/.drbd_git_revision
%patch -p1

%build

%install
mkdir -p %kernel_srcdir
cd ..
tar -cf %kernel_srcdir/kernel-source-%name-%version.tar %name-%version

%check
# sed -i s/SUBDIRS=/M=/g Makefile
# make -C drbd KDIR=/lib/modules/*/build

%files -n kernel-source-%name
%attr(0644,root,root) %kernel_src/kernel-source-%name-%version.tar

%files
%doc README.md COPYING

%changelog
* Thu Jun 04 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.23-alt0.rc3.1
- 9.0.23rc3

* Thu May 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.23-alt0.rc1.1
- 9.0.23rc1

* Tue Apr 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.22-alt1
- 9.0.22

* Fri Mar 06 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.21-alt3
- Fix pr_warning().

* Thu Mar 05 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.21-alt2
- Fix build for un-def.

* Mon Feb 10 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.0.21-alt1
- Initial import for ALT.

