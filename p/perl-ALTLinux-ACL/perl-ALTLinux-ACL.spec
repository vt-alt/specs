%define module ALTLinux-ACL

Name: perl-%module
Version: 0.220
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering ALTLinux ACL files
Group: Development/Perl
License: GPLv2+ or Artistic-2.0
Source: %module-%version.tar.gz
# TODO: upload
#Url: http://search.cpan.org/dist/%module
Url: http://git.altlinux.org/people/viy/packages/%name

BuildRequires: perl-devel perl(Pod/Usage.pm) perl-IPC-Run3 perl(Data/Array2ArrayMap/Hash/XSTree.pm) perl(Pod/Text.pm)

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
%perl_vendor_privlib/ALT*
%_bindir/*
%_man1dir/*

%changelog
* Mon Sep 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.220-alt1
- new version

* Tue Sep 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- new version

* Wed Sep 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3
- Remove misplaced Requires on perl-MooX-Singleton.

* Wed Sep 26 2018 Grigory Ustinov <grenka@altlinux.org> 0.20-alt2
- Add missing Requires on perl-MooX-Singleton.

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- always remove dir/ suffix from name

* Tue Sep 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- added --nvr option

* Wed Jul 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- updated documentation, fixed Url

* Sat Jun 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- support for empty acl in p8

* Thu Jan 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- updated altlinux-acl-filter-list-by-access

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- excluded changelog2ALTLinuxACLleader due to dependency on perl-RPM

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- NMU: added missing Pod dependencies

* Fri Aug 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- added altlinux-acl-get-leader

* Mon Apr 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- arguments check

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- improved altlinux-acl-filter-list-by-access

* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- bugfix in options

* Fri Jan 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added altlinux-acl-report-split-by-acl

* Wed Oct 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- new version

* Wed Oct 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- new version

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added altlinux-acl-filter-list-* scripts

* Thu May 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- support for shared options

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- altlinux-acl-filter: added filter by leadership

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added changelog2ALTLinuxACLleader script

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.M51.1
- backport

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- skip empty lines in acl filter

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new version

* Wed Oct 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- new version

* Tue Oct 12 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
