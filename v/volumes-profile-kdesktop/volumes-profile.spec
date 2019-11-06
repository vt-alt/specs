Name: volumes-profile-kdesktop
Version: 0.9.0
Release: alt2

Summary: Volumes description for Desktop KDE distribution
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar


%description
Volumes description for Desktop KDE distribution

%prep
%setup

%install
%define hook1dir %_datadir/install2/initinstall.d
%define hook2dir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hook1dir
install -pm755 10-*.sh %buildroot%hook1dir/
#mkdir -p %buildroot%hook2dir
#install -pm755 01-*.sh %buildroot%hook2dir/

%files
%hook1dir/*
#%hook2dir/*

%changelog
* Tue Nov 05 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt2
- fix space requirement

* Fri Nov 01 2019 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- update profile

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Thu Dec 06 2018 Sergey V Turchin <zerg@altlinux.org> 0.8.0-alt1
- use LVM by default

* Fri Oct 27 2017 Sergey V Turchin <zerg@altlinux.org> 0.7.4-alt1
- fix to decrease default swap size

* Wed Oct 25 2017 Sergey V Turchin <zerg@altlinux.org> 0.7.3-alt1
- fix to decrease default swap size

* Wed Aug 16 2017 Sergey V Turchin <zerg@altlinux.org> 0.7.2-alt1
- decrease default swap size

* Mon Jun 26 2017 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- decrease space requires to fit 32GB-drive

* Fri Apr 15 2016 Sergey V Turchin <zerg@altlinux.org> 0.7.0-alt1
- don't separate home

* Wed May 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.6.1-alt1
- increase mimimum root size

* Wed Aug 10 2011 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- remove 01-move-fs-ofs.sh

* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- remove server partitioning entry

* Wed Mar 09 2011 Sergey V Turchin <zerg@altlinux.org> 0.5-alt1
- adopted for KDesktop

* Tue Feb 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt2
- spaces fixed

* Mon Feb 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- don't create raids when virtualized

* Thu Jan 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- not more them 16Gb of swap

* Fri Oct 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- / size for server increased

* Tue Oct 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initital build
