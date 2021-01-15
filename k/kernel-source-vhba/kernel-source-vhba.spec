Name: kernel-source-vhba
Version: 20200106
Release: alt1

Summary: Source for VHBA module
License: GPLv2
Group: Development/Kernel

URL: http://cdemu.sourceforge.net/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: http://downloads.sourceforge.net/cdemu/vhba-module-%version.tar.bz2
Source1: 60-vhba.rules

BuildArch: noarch

BuildPreReq: kernel-build-tools
BuildRequires(pre): rpm-build-kernel

%package -n vhba-udev-rules
Summary: Source for VHBA module
Group: System/Kernel and hardware

%description
VHBA kernel module, a virtual SCSI host bus adapter used by CDEmu daemon from
userspace-cdemu suite.

%description -n vhba-udev-rules
Udev rules for VHBA kernel module

%prep
%setup -c
mv vhba-module-%version %name-%version

%install
%__mkdir_p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version
install -Dp -m0644 %SOURCE1 %buildroot%_udevrulesdir/60-vhba.rules

%files
%dir %_usrsrc/kernel
%dir %kernel_src
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n vhba-udev-rules
%config %_udevrulesdir/60-vhba.rules

%changelog
* Mon Nov 02 2020 Nazarov Denis <nenderus@altlinux.org> 20200106-alt1
- Version 20200106

* Mon Jun 17 2019 Nazarov Denis <nenderus@altlinux.org> 20190410-alt1
- Version 20190410

* Sat Jan 26 2019 Nazarov Denis <nenderus@altlinux.org> 20170610-alt2
- Remove %ubt macro

* Mon Jul 31 2017 Nazarov Denis <nenderus@altlinux.org> 20170610-alt1%ubt
- Version 20170610

* Thu Oct 13 2016 Nazarov Denis <nenderus@altlinux.org> 20161009-alt1
- Version 20161009

* Fri Oct 10 2014 Nazarov Denis <nenderus@altlinux.org> 20140928-alt0.M70T.1
- Build for branch t7

* Tue Oct 07 2014 Nazarov Denis <nenderus@altlinux.org> 20140928-alt1
- Version 20140928

* Sun Jul 20 2014 Nazarov Denis <nenderus@altlinux.org> 20140629-alt0.M70P.1
- Build for branch p7

* Fri Jul 04 2014 Nazarov Denis <nenderus@altlinux.org> 20140629-alt0.M70T.1
- Build for branch t7

* Wed Jul 02 2014 Nazarov Denis <nenderus@altlinux.org> 20140629-alt1
- Version 20140629

* Sun Jun 09 2013 Nazarov Denis <nenderus@altlinux.org> 20130607-alt1.1
- Fix udev rules path

* Sun Jun 09 2013 Nazarov Denis <nenderus@altlinux.org> 20130607-alt1
- Version 20130607

* Tue Apr 24 2012 Nazarov Denis <nenderus@altlinux.org> 20120422-alt1
- Version 20120422

* Tue Oct 11 2011 Anton Protopopov <aspsk@altlinux.org> 20110915-alt2
- vhba-udev-rules: new package with udev rules to module

* Sun Sep 18 2011 Nazarov Denis <nenderus@altlinux.org> 20110915-alt1
- Version 20110915

* Thu Jun 09 2011 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20110416-alt0.M60T.1
- Build for branch t6

* Thu Jun 09 2011 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20110416-alt1
- Version 1.2.1.20110416

* Tue Apr 12 2011 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20100822-alt2
- Add 2 patches

* Thu Nov 18 2010 Nazarov Denis <nenderus@altlinux.org> 1.2.1.20100822-alt1
- Fix version number

* Wed Nov 10 2010 Nazarov Denis <nenderus@altlinux.org> 0.20100822-alt1
- Initial build for ALT Linux
