%define module Source-Package

Name: perl-%module
Version: 0.179
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: %module-%version.tar
#Url: http://search.cpan.org/dist/%module
#Url: https://www.altlinux.org/Packaging_Automation/MassProcessing
Url: https://git.altlinux.org/people/viy/%module


BuildRequires: perl-devel perl(RPM/Vercmp.pm) perl(RPM/Header.pm) perl(Source/Shared/Utils/Downloader.pm)
Conflicts: perl-Source-Repository < 0.388

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
#doc README
%perl_vendor_privlib/Source*

%changelog
* Tue Oct 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.179-alt1
- new version

* Fri Jul 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.178-alt1
- new version

* Sun Feb 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.177-alt1
- new version

* Tue Jan 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.176-alt1
- new version

* Sun Dec 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.175-alt1
- new version

* Fri Dec 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.174-alt1
- new version

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.173-alt1
- new version

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.172-alt1
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.171-alt1
- new version

* Thu Mar 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.170-alt1
- suse version comparator for watch.altlinux.org

* Thu Mar 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.169-alt1
- added S::P::RPM::NoEpoch for fast web processing

* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.168-alt1
- stable release

* Sat Jan 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.167-alt1
- TeXLive support

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.166-alt1
- stable release

* Sat Oct 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.165-alt1
- development release

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.164-alt1
- bugfix release

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.163-alt1
- stable release

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.162-alt1
- development release

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.161-alt1
- development release

* Mon Oct 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- rsync url support

* Fri Sep 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- do not use old Source:Repository download call

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- development release

* Wed Jan 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- development release

* Tue Jan 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- python version class added

* Wed Dec 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- python support

* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- bugfix release

* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added rpm.org epoch comarators

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- indirect RPM br:

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- use RPM-Vercmp

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- autodownload

* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added Source::Package::Comparators::Raw

* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added Source::Package::Pair

* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added Source::Package::Comparator

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build for Sisyphus
