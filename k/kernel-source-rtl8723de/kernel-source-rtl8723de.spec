%define module_name rtl8723de
%define module_version 5.1.1.8

%define module_source %module_name.tar

Name: kernel-source-%module_name
Version: %module_version
Release: alt14

Group: Development/Kernel
Summary: Linux %module_name modules sources
License: GPL
URL: https://github.com/smlinux/rtl8723de
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar
Patch1: alt-build-time.diff
Patch2: alt-ampdu-buf-define.diff
Patch3: switch.diff
Patch4: alt-kernel-5.6-proc_ops.diff

BuildRequires: kernel-build-tools

%description
%module_name modules sources for RTL8723DE Linux kernel driver

%prep
%setup -c -q
pushd %name-%version
%patch1 -p1
#%patch2 -p1
%patch3 -p1
%patch4 -p1
popd

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/kernel-source-%module_name-%version.tar.bz2 %name-%version

%files
%_usrsrc/*

%changelog
* Thu Aug 27 2020 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt14
- update for kernel 5.8

* Thu May 07 2020 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt13
- fix against kernel 5.6

* Tue Apr 21 2020 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt12
- update from smlinux/current branch

* Fri Mar 06 2020 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt11
- return rtl8723de sources

* Tue Dec 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt10
- using rtlwifi_new sources

* Wed Dec 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt9
- fix to compile

* Mon Dec 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt8
- add fix against 5.3 kernel

* Wed Jul 17 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt7
- update from 5.0-up branch

* Wed Mar 13 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt6
- update from 4.15-up branch to apply fix for 5.0 kernel
- remove compile warnings

* Mon Feb 11 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt5
- update from 4.15-up branch

* Tue Sep 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt4
- update from 4.15-up branch

* Fri Apr 06 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt3
- add fix against 4.16 kernel

* Mon Jan 29 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt2
- remove build time

* Mon Jan 29 2018 Sergey V Turchin <zerg@altlinux.org> 5.1.1.8-alt1
- initial build
