Name: kernel-source-r8168
Version: 8.048.02
Release: alt1

Summary: Source for RTL8168 driver
License: GPLv2+
Group: Development/Kernel

URL: http://www.realtek.com/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: r8168-%version.tar.bz2
Source1: blacklist-r8168.conf

Patch0: kernel-5.6.patch

BuildArch: noarch

BuildPreReq: kernel-build-tools

Provides: kernel-source-rtl8168
Obsoletes: kernel-source-rtl8168

%description
RTL8168 is the Linux device driver released for RealTek RTL8168B/8111B,
RTL8168C/8111C, RTL8168CP/8111CP, RTL8168D/8111D, and RTL8168DP/8111DP
Gigabit Ethernet controllers with PCI-Express interface.

%package -n r8168-blacklist
Summary: Blacklist modules for r8168
Group: System/Kernel and hardware

%description -n r8168-blacklist
Blacklist modules for correctly working module r8168

%prep
%setup -c
%patch0 -p0
%__mv r8168-%version %name-%version

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version
%__install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/modprobe.d/blacklist-r8168.conf

%files
%dir %_usrsrc/kernel
%dir %kernel_src
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n r8168-blacklist
%dir %_sysconfdir/modprobe.d
%config %_sysconfdir/modprobe.d/blacklist-r8168.conf

%changelog
* Thu Apr 16 2020 Nazarov Denis <nenderus@altlinux.org> 8.048.02-alt1
- Version 8.048.02
- Kernel 5.6 patch

* Thu Dec 12 2019 Nazarov Denis <nenderus@altlinux.org> 8.047.05-alt2
- Add kernel 5.4 patch

* Wed Nov 27 2019 Nazarov Denis <nenderus@altlinux.org> 8.047.05-alt1
- Version 8.047.05

* Fri Jun 14 2019 Nazarov Denis <nenderus@altlinux.org> 8.047.01-alt1
- Version 8.047.01

* Sun Nov 12 2017 Nazarov Denis <nenderus@altlinux.org> 8.045.08-alt1
- Version 8.045.08

* Sun Mar 12 2017 Nazarov Denis <nenderus@altlinux.org> 8.044.02-alt1
- Version 8.044.02

* Fri Oct 14 2016 Nazarov Denis <nenderus@altlinux.org> 8.043.01-alt1
- Version 8.043.01

* Tue Jul 12 2016 Nazarov Denis <nenderus@altlinux.org> 8.042.00-alt1
- Version 8.042.00

* Sat Jan 16 2016 Nazarov Denis <nenderus@altlinux.org> 8.041.01-alt1
- Version 8.041.01

* Tue Jun 23 2015 Nazarov Denis <nenderus@altlinux.org> 8.040.00-alt1
- Version 8.040.00

* Thu Sep 25 2014 Nazarov Denis <nenderus@altlinux.org> 8.039.00-alt1
- Version 8.039.00

* Wed Mar 19 2014 Nazarov Denis <nenderus@altlinux.org> 8.038.00-alt1
- Version 8.038.00

* Tue Oct 01 2013 Nazarov Denis <nenderus@altlinux.org> 8.037.00-alt1
- Version 8.037.00

* Wed Jun 19 2013 Nazarov Denis <nenderus@altlinux.org> 8.036.00-alt2
- Update version

* Sat Jun 15 2013 Nazarov Denis <nenderus@altlinux.org> 8.036.00-alt1
- Version 8.036.00

* Wed Jan 30 2013 Nazarov Denis <nenderus@altlinux.org> 8.035.00-alt2
- Add subpackage for correctly working

* Tue Jan 29 2013 Nazarov Denis <nenderus@altlinux.org> 8.035.00-alt1
- Version 8.035.00

* Fri Dec 02 2011 Nazarov Denis <nenderus@altlinux.org> 8.027.00-alt1
- Version 8.027.00

* Sat Oct 29 2011 Nazarov Denis <nenderus@altlinux.org> 8.026.00-alt1
- Version 8.026.00

* Fri Aug 26 2011 Nazarov Denis <nenderus@altlinux.org> 8.025.00-alt1
- Version 8.025.00

* Mon May 30 2011 Nazarov Denis <nenderus@altlinux.org> 8.024.00-alt0.M60T.1
- Build for branch t6

* Sun May 29 2011 Nazarov Denis <nenderus@altlinux.org> 8.024.00-alt1
- Version 8.024.00

* Sat Apr 23 2011 Nazarov Denis <nenderus@altlinux.org> 8.023.00-alt1
- Version 8.023.00

* Sun Mar 27 2011 Nazarov Denis <nenderus@altlinux.org> 8.022.00-alt1
- Version 8.022.00

* Mon Jan 31 2011 Nazarov Denis <nenderus@altlinux.org> 8.021.00-alt1
- Version 8.021.00

* Mon Jan 03 2011 Nazarov Denis <nenderus@altlinux.org> 8.020.00-alt1
- Initial build for ALT Linux



