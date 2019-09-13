Name: distrodb-utils
Version: 0.246
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: utils for managing Distrodb databases
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://www.altlinux.org/Packaging_Automation/DistroMap

Requires: python-module-DistroDbMaker

BuildRequires: rpm-build-perl perl(DistroMap.pm)
# for DistroDBTools
BuildRequires: perl(Source/Shared/FindLocalMirror/ALTLinux.pm)
# for ProjectDB
BuildRequires: perl(RPM/Header.pm) perl(Source/Repository/RPM.pm) perl(Clone.pm)

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -m 755 projectdb-* \
	distrodb-helper-* \
	distrodb-list-duplicates.pl \
	distrodb-verify-newpkglist.pl \
	distrodb-check-health-*.pl \
	mkdistromap-*.pl \
	%buildroot%_bindir/
mkdir -p %buildroot%perl_vendor_privlib/DistroDB/CLI/
install -m 644 *.pm %buildroot%perl_vendor_privlib/
install -m 644 DistroDB/*.pm %buildroot%perl_vendor_privlib/DistroDB/
install -m 644 DistroDB/CLI/*.pm %buildroot%perl_vendor_privlib/DistroDB/CLI/

%files
%doc README
%_bindir/*
%perl_vendor_privlib/*.pm
%perl_vendor_privlib/DistroDB

%changelog
* Thu Sep 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.246-alt1
- new version

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.245-alt1
- new version

* Sat Apr 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.244-alt1
- new version

* Wed Apr 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.243-alt1
- new version

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.242-alt1
- new version

* Sat Dec 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.241-alt1
- new version

* Sat Jun 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.240-alt1
- new version

* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.239-alt1
- new version

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.238-alt1
- new version

* Tue Apr 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.237-alt1
- new version

* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.236-alt1
- new version

* Tue Mar 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.235-alt1
- new version

* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.234-alt1
- new version

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.233-alt1
- new version

* Sat Mar 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.232-alt1
- new version

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.231-alt1
- new version

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- new version

* Sat Feb 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- new version

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- new version

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- new version

* Thu Dec 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- new version

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- new version

* Tue Dec 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- new version

* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- new version
- projectdb support

* Fri Dec 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- new version

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- new distrodb format

* Fri Sep 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- new version

* Sat May 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- support for rpm 4.0.4

* Thu Mar 30 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.11-alt1
- Adapted to the new RPM (>= 4.13) Python API (ALT#32900),
  introduced in commit 5211039a20762b4a50c006ccf79666bff34967c2
  Author: jbj Date: Mon Aug 5 21:46:50 2002 +0000

* Thu Oct 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- new version

* Wed Jul 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- new version

* Thu Jul 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- new version

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- new version

* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- generic source translation

* Thu Jun 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- pyegg db

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added management utils for manual maps

* Fri May 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added common lib

* Thu May 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first release
