Name: repocop-report-prometheus
Version: 0.35
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop report script that dumps test results to prometeus1 format
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Requires: repocop > 0.80
#Requires: perl-JSON-XS
Obsoletes: repocop-prometeus < 0.22
Obsoletes: repocop-report-prometeus < 0.31

BuildRequires: perl-devel perldoc
#perl-JSON
BuildRequires: repocop

Source: %name-%version.tar

%description
Repocop is a repository unit tests platform.
%summary

%package -n repocop-report-prometheus2
Summary: repocop report script that dumps test results to prometheus2 format
Group: Development/Other
License: GPL or Artistic
Requires: repocop > 0.80
Obsoletes: repocop-report-heroku < 0.4
Obsoletes: repocop-report-prometeus2 < 0.31

%description -n repocop-report-prometheus2
Repocop is a repository unit tests platform.
%summary

%prep
%setup
rm -f *.spec

%build

%install
mkdir -p %buildroot/%_bindir
install -m 755 repocop-report-prometheus* %buildroot/%_bindir/

%files
#doc README ChangeLog
%_bindir/repocop-report-prometheus-*
#%_man1dir/repocop-report-prometheus-*

%files -n repocop-report-prometheus2
%_bindir/repocop-report-prometheus2*

%changelog
* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- ported for repocop 0.81+

* Tue Jul 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- bugfix release 

* Tue Jul 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- adapted for repocop 0.77

* Sun Oct 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- support for TestDB

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2
- added Obsoletes

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- renamed to prometheus (closes: 28131)

* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2
- code cleanup; but still has old txt support for prometeus2.

* Fri Jul 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- added sqlite report

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- bugfix release (closes: 26741)

* Thu Dec 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- bugfix release

* Tue Dec 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- added branch to sql

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- added branch option

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2
- added repository option

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- new version

* Sun Nov 08 2009 Igor Vlasenko <viy@altlinux.ru> 0.24-alt2
- fix in repocop-report-prometeus2-patches

* Fri Nov 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- added repocop-report-prometeus2-patches

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- bugfixed format4 (prometeus2)

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- format4

* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- renamed; now contains prometeus and prometeus2 reports

* Thu Sep 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- format3

* Wed Sep 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- format2

* Wed Sep 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- First build for Sisyphus.
