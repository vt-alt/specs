Name: kernel-source-ipt_netflow
Version: 2.5
Release: alt2

Summary: Netflow iptables module for Linux kernel
License: GPL
Group: Development/Kernel
URL: http://sourceforge.net/projects/ipt-netflow/
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source0: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-kernel

%description
Ipt-netflow is very fast and effective Netflow exporting module for
Linux kernel. Designed for Linux router with heavy network load.
This is netfilter/iptables module adding support for NETFLOW target.

%prep
%setup -q -c

%install
mkdir -p %kernel_srcdir
mv %name-%version ipt_netflow-%version
tar -cjf %kernel_srcdir/ipt_netflow-%version.tar.bz2 ipt_netflow-%version

%files
%attr(0644,root,root) %kernel_src/ipt_netflow-%version.tar.bz2

%changelog
* Wed Jun 03 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.5-alt2
- kernel 5.7 compatibility from upstream

* Tue Apr 28 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.5-alt1
- v2.5
- kernel 5.6 compatibility

* Fri Jun 14 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.3-alt5
- updated from git: kernel 5.2 compatibility

* Wed Mar 27 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.3-alt4
- updated from git: kernel 5.0 compatibility

* Thu Apr 05 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.3-alt3
- updated to 2.3

* Tue Sep 12 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.2-alt3
- updated from git: kernel 4.13 compatibility

* Mon Mar 13 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.2-alt2
- updated from git: kernel 4.10 compatibility

* Tue Jun 21 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.2-alt1
- 2.2
- updated from git: kernel 4.6 compatibility

* Tue Sep 29 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.1-alt2
- updated from git: kernel 4.2 compatibility

* Tue Feb 10 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.1-alt1
- 2.1

* Wed Oct 22 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed Jul 17 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8-alt2
- support for kernel 3.10 added

* Tue May 07 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8-alt1
- build as separate module 

