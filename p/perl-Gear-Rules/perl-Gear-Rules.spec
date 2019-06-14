# option for bootstrap (possible circular dependency)
%def_with RPMSourceEditor
%define module Gear-Rules

Name: perl-%module
Version: 0.198
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering Gear rules files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
Url: http://git.altlinux.org/people/viy/packages/perl-%module

BuildRequires: perl-devel perl(Pod/Usage.pm) perl(Pod/Text.pm)
Requires: gear perl(Pod/Text.pm)
%if_with RPMSourceEditor
BuildRequires: perl-RPM-Source-Editor
%endif

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/G*
%_bindir/*
%_man1dir/*
%if_without RPMSourceEditor
%exclude %_bindir/gear-rules-verify
%endif

%changelog
* Thu Jun 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.198-alt1
- new version

* Tue Feb 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.197-alt1
- added has_external_commits and external_commits to API

* Thu Oct 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.196-alt1
- subtree merge support

* Sun Sep 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.195-alt1
- new version

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.194-alt1
- new version

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.193-alt1
- new version

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.192-alt1
- new version

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.191-alt1
- new version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.190-alt1
- new version

* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2
- added lnkvisitor@lnkvisitor.localdomain

* Mon Jan 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- new version

* Mon Mar 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- new version (closes: #31882)

* Sun Dec 06 2015 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- new version

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- etersoft in git commits is friendly

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- support for .gear/uupdate_ignore_commits

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- bugfix release

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- new version

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- new version

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- bugfix release

* Tue Jun 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2
- explicit requires on perl(Pod/Text.pm)

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added ab@samba

* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added gear-rules-print-specfile

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- bugfix release

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- support for pure gear tags

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt5
- NMU: added missing Pod dependencies

* Sat Nov 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt4
- added --force to gear-rules-restore-branches

* Wed Nov 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt3
- added gear dependency.

* Wed Nov 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- added gear-rules-restore-branches

* Tue Nov 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- new version

* Sun Oct 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- new version

* Thu Oct 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Tue Oct 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- new version

* Sun Oct 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new version

* Fri Oct 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new version

* Thu Oct 13 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- new version

* Sun Sep 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
