%filter_from_requires /^repocop-unittest-build-logs/d

Name: autorepo-altnode-repocop
Version: 0.26
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: scripts for an automated repocop node
Group: Other
License: GPLv2+
Url: http://repocop.altlinux.org
Source: %name-%version.tar

BuildRequires: perl(Pod/Text.pm) repocop-resource-html repocop > 0.79
Requires: repocop > 0.79
Requires: pigz pzstd
Conflicts: repocop-unittest-unmet-dependency < 0.10

%description
scripts for an automated repocop node
in `autorepo' Automated Package Maintainance Cluster.

%package tasktest
Summary: scripts for an automated "repocop for tasks" node
Group: Other
# tasktest
Requires: perl-File-Lock-ParentLock >= 0.08
Requires: repocop-resource-html
BuildRequires: perl(HTML/Template/Pro.pm)

%description tasktest
scripts for an automated "repocop for tasks" node
in `autorepo' Automated Package Maintainance Cluster.

%prep
%setup

%build

%install

mkdir -p $RPM_BUILD_ROOT%_bindir
install -m 755 repocop-* $RPM_BUILD_ROOT%_bindir

%files
%doc daily.conf.*
%doc crontab.repocop
%_bindir/*
%exclude %_bindir/repocop-tasktest-*

%files tasktest
%doc crontab.tasktest*
%_bindir/repocop-tasktest-*

%changelog
* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- added metadata fix support

* Fri Jul 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- repocop for tasks added (tasktest scripts)

* Mon Jul 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- support for repocop-unittest-unmet-dependency >= 0.10

* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- extended mail reports

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- repocop 0.77 api

* Wed Jun 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- mail reports on emergency

* Wed Jun 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- new version

* Tue Feb 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- better distrodb archives

* Sat Oct 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- support for autoimports distrodb extra

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- support for new distrodb extra

* Fri Mar 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- stable release

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- NMU: added missing Pod dependencies

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- repocop TestDB interface support

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- dropped obsolete symlinks

* Tue Jul 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- more daily.conf

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- html support

* Fri Jul 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- release

* Thu Jul 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt6
- bugfix release

* Wed Jul 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt5
- fixed dependencies

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt4
- more altnode tags

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3
- support for html report

* Mon Jul 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- added altnode support

* Mon Jul 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added extra statistics reports

* Fri May 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- support for archive task on autorepo nodes

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- new distrodb format

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- distrodb-extra support

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- enabled build logs again

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- dropped optional dependency on repocop-unittest-build-logs

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- prometheus2 support

* Fri Jul 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- export of watch files

* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- repocop 0.59 distrotest support

* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- repocop 0.58 support

* Fri Jul 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- support for repocop-report-prometeus2-sqlite

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
