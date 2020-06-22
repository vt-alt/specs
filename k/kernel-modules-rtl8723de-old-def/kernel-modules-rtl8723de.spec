%define IF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define IF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define IF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"

%define module_name	rtl8723de
%define module_version	5.1.1.8
%define module_release alt15

%define flavour		old-def
%define karch %ix86 x86_64 aarch64 ppc64le
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-old-def

%setup_kernel_module %flavour

%define norm_version	%kversion

%define module_dir /lib/modules/%kversion-%flavour-%krelease/net/wireless/realtek/rtlwifi/%module_name

Name: kernel-modules-%module_name-%flavour
Group: System/Kernel and hardware
Summary: Module for Realtek RTL8723DE
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
Url: https://github.com/smlinux/rtl8723de
License: GPLv2

Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

ExclusiveOS: Linux
ExclusiveArch: %ix86 x86_64

PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release

BuildRequires(pre): rpm-build-kernel
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
%define k_mod_src_suffix %nil
%IF_ver_lt %kversion 5.0
%define k_mod_src_suffix -4.15up
%endif
%IF_ver_lt %kversion 4.15
%define k_mod_src_suffix -4.11up
%endif
%IF_ver_lteq %kversion 4.10
%define k_mod_src_suffix -4.10down
%endif
BuildRequires: kernel-source-%module_name%k_mod_src_suffix = %module_version

%description
These packages contain Realtek RTL8723DE module.

%prep
rm -rf kernel-source-%module_name-%module_version
tar xvf %kernel_src/kernel-source-%module_name-%module_version.tar.bz2
%setup -D -T -n kernel-source-%module_name-%module_version

%build
. %_usrsrc/linux-%kversion-%flavour/gcc_version.inc
make \
    ARCH=%base_arch \
    CROSS_COMPILE= \
    KSRC=%_usrsrc/linux-%kversion-%flavour \
    M=${PWD} \
    modules \
    #
#    -C %_usrsrc/linux-%kversion-%flavour \

%install
KMOD_FILE=8723de.ko
[ -f rtl8723de/rtl8723de.ko ] && KMOD_FILE=rtl8723de/rtl8723de.ko
install -D -m 644 $KMOD_FILE %buildroot/%module_dir/rtl8723de.ko

%files
%module_dir

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.

* Tue Mar 10 2020 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt15
- return rtl8723de sources for new kernels

* Wed Dec 18 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt14
- using rtlwifi_new for new kernels

* Wed Jul 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt13
- add separate sources for kernnels 4.15 up to 5.0

* Thu Nov 15 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt11
- add workaround for 4.19 kernel

* Wed Sep 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt10
- fix git inheritance

* Tue Sep 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt9
- fix to build

* Tue Sep 11 2018 Sergey V Turchin <zerg at altlinux dot org> 5.1.1.8-alt8
- build only on x86

* Tue Sep 11 2018 Sergey V Turchin <zerg at altlinux dot org> 5.1.1.8-alt7
- define karch

* Tue Sep 11 2018 Sergey V Turchin <zerg at altlinux dot org> 5.1.1.8-alt6
- fix provides

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt5
- use other sources branch for old kernels

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt4
- fix build requires

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt3
- fix build requires

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt2
- fix build requires

* Tue Jan 09 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt1
- initial build
