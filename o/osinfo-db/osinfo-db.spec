
Summary: osinfo database files
Name: osinfo-db
Version: 20190805
Release: alt1
License: LGPLv2+
Group: System/Libraries
Url: https://libosinfo.org
Source: https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: intltool >= 0.40.0
BuildRequires: osinfo-db-tools
Conflicts: libosinfo < 1.0.0

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%install
osinfo-db-import --root %buildroot --system %SOURCE0

%files
%dir %_datadir/osinfo
%_datadir/osinfo/*

%changelog
* Fri Aug 23 2019 Alexey Shabalin <shaba@altlinux.org> 20190805-alt1
- 20190805

* Wed May 15 2019 Alexey Shabalin <shaba@altlinux.org> 20190504-alt1
- 20190504

* Sat Mar 16 2019 Alexey Shabalin <shaba@altlinux.org> 20190304-alt1
- 20190304

* Sat Mar 02 2019 Alexey Shabalin <shaba@altlinux.org> 20190301-alt1
- 20190301

* Sat Feb 02 2019 Alexey Shabalin <shaba@altlinux.org> 20190120-alt1
- 20190120

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 20181116-alt1
- 20181116

* Fri Oct 19 2018 Alexey Shabalin <shaba@altlinux.org> 20181019-alt1
- 20181019

* Thu Oct 18 2018 Alexey Shabalin <shaba@altlinux.org> 20181018-alt1
- 20181018
- update ALT support

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 20180903-alt1
- 20180903

* Fri Apr 06 2018 Alexey Shabalin <shaba@altlinux.ru> 20180325-alt1
- 20180325

* Wed Oct 11 2017 Alexey Shabalin <shaba@altlinux.ru> 20170813-alt1
- 20170813

* Fri Dec 30 2016 Alexey Shabalin <shaba@altlinux.ru> 20161026-alt1
- 20161026

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 20160728-alt1
- 20160728

