%define module_name             accel-ppp
%define module_version          1.12.0
%define module_release          alt1

%define flavour		std-def
%define karch	%ix86 x86_64

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/ipoe

Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease

Summary: Linux Kernel drivers support IPoE for accel-ppp
License: GPLv2
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/accel-ppp/

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
BuildRequires(pre): rpm-build-kernel cmake libpcre-devel libssl-devel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name

Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

Requires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %karch

%description
%module_name kernel driver support IPoE for accel-ppp

%prep
rm -rf %module_name-%module_version
tar -jxvf %kernel_src/%module_name-%module_version.tar.bz2
%setup -D -T -n %module_name-%module_version

%build
%cmake \
      -DKDIR=%_usrsrc/linux-%kversion-%flavour \
      -DBUILD_IPOE_DRIVER=TRUE \
      -DBUILD_VLAN_MON_DRIVER=TRUE \
      ..

make -C BUILD/drivers/ipoe
make -C BUILD/drivers/vlan_mon

%install
install -d %buildroot/%module_dir
install -m644 -D BUILD/drivers/ipoe/driver/ipoe.ko %buildroot/%module_dir/ipoe.ko
install -m644 -D BUILD/drivers/vlan_mon/driver/vlan_mon.ko %buildroot/%module_dir/vlan_mon.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Aug 06 2019 Alexei Takaseev <taf@altlinux.org> 1.12.0-alt1
- 1.12.0

* Mon Jun 17 2019 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt3
- Add karch define, PreReq -> Requires(pre)

* Fri Aug 11 2017 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt2
- Fix build with kernels >= 4.10

* Thu Aug 10 2017 Alexei Takaseev <taf@altlinux.org> 1.11.2-alt1
- 1.11.2

* Thu Mar 23 2017 Alexei Takaseev <taf@altlinux.org> 1.11.1-alt4
- Add vlan_mon.ko

* Thu Feb 16 2017 Alexei Takaseev <taf@altlinux.org> 1.11.1-alt3
- update upstream to git:444385f2be198318d6092c049bbebf5cc981eeca

* Tue Nov 29 2016 Alexei Takaseev <taf@altlinux.org> 1.11.1-alt1
- 1.11.1

* Wed Jul 13 2016 Alexei Takaseev <taf@altlinux.org> 1.11.0-alt1
- 1.11.0

* Thu May 12 2016 Alexei Takaseev <taf@altlinux.org> 1.10.2-alt1
- 1.10.2

* Tue Dec 22 2015 Alexei Takaseev <taf@altlinux.org> 1.10.0-alt1
- 1.10.0

* Thu Sep 03 2015 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt4
- update upstream to git:30cff41b56be0d4c3e407e8aa4de5b289eef2ab0

* Wed Dec 10 2014 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt1
- 1.9.0 release

* Mon Oct 13 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt4
- update upstream to git:8d3351d4cdfcaf45aa2c918b0f8920798be4dc04

* Mon Sep 01 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt3
- update upstream to git:ec9968885ed2f273c4d2c18297986c463fb9cf9b

* Tue Aug 05 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt2
- update upstream to git:2cdd67782c6d11af141992dba2943e03134593b5

* Fri May 09 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt1
- 1.8.0 release

* Mon Apr 14 2014 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt0.beta.1
- Initial build for Sisuphus
