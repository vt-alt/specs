%define _unpackaged_files_terminate_build 1
Name: perl-Role-Tiny
Version: 2.002004
Release: alt1

Summary: Role::Tiny - minimalist role composition tool
Group: Development/Perl
License: Perl

# Cloned from git://git.shadowcat.co.uk/gitmo/Role-Tiny.git
Url: %CPAN Role-Tiny
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: perl-devel perl-Class-Method-Modifiers perl-Test-Fatal
BuildArch: noarch

%description
%summary

%prep
%setup -q
%patch -p1
sed -i /MRO::Compat/d Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README* Changes
%perl_vendor_privlib/Role/Tiny*

%changelog
* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 2.002004-alt1
- new version

* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 2.002003-alt1
- new version

* Sat Nov 07 2020 Igor Vlasenko <viy@altlinux.ru> 2.001004-alt2
- build w/o MRO::Compat

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 2.001004-alt1
- new version

* Sun Oct 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.001003-alt1
- new version

* Mon Oct 07 2019 Igor Vlasenko <viy@altlinux.ru> 2.001001-alt1
- new version

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.000008-alt1
- new version

* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 2.000006-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.000005-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.000003-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.000001-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.003004-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 1.003003-alt1
- automated CPAN update

* Tue Sep 17 2013 Vladimir Lettiev <crux@altlinux.ru> 1.003002-alt1
- 1.002005 -> 1.003002

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.002005-alt1
- 1.001005 -> 1.002005

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.001005-alt1
- 1.000000 -> 1.001005

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.000000-alt1
- initial build

