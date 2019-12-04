%define _unpackaged_files_terminate_build 1
%define dist JSON-XS

Name: perl-%dist
Version: 3.04
Release: alt2
Epoch: 20191119

Summary: JSON serialising/deserialising, done correctly and fast
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/ML/MLEHMANN/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Encode perl-common-sense perl-devel perl(Types/Serialiser.pm) perl(Canary/Stability.pm)

%description
This module converts Perl data structures to JSON and vice versa. Its
primary goal is to be *correct* and its secondary goal is to be
*fast*. To reach the latter goal it was written in C.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/json_xs
%perl_vendor_archlib/JSON
%perl_vendor_autolib/JSON

%changelog
* Tue Nov 19 2019 Valery Inozemtsev <shrek@altlinux.ru> 20191119:3.04-alt2
- reverted to 3.04

* Wed Mar 06 2019 Igor Vlasenko <viy@altlinux.ru> 3:4.02-alt1
- automated CPAN update

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 3:4.01-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 3:3.04-alt1.1
- rebuild with new perl 5.28.1

* Wed Jan 16 2019 Igor Vlasenko <viy@altlinux.ru> 3:3.04-alt1
- reverted to 3.04

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 2:4.0-alt1
- automated CPAN update

* Fri Nov 30 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:3.04-alt1
- 4.0 -> 3.04 (4.0 pre-release, do not use other than for testing)

* Tue Nov 20 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.0-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.04-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.04-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.03-alt1.1
- rebuild with new perl 5.24.1

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.03-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.02-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.01-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.01-alt1.1
- rebuild with new perl 5.20.1

* Fri Nov 01 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.01-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1:2.34-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1:2.34-alt1
- automated CPAN update

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1:2.33-alt1
- 2.32 -> 2.33
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1:2.32-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1:2.32-alt1
- automated CPAN update

* Fri Nov 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1:2.3-alt2
- new release

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1:2.3-alt1
- 2.24 -> 2.3
- build for perl-5.12

* Sun Jul 12 2009 Michael Bochkaryov <misha@altlinux.ru> 2.2400-alt1
- 2.24 version build

* Sat Sep 06 2008 Michael Bochkaryov <misha@altlinux.ru> 2.2222-alt1
- 2.2222 version build
- fix directory ownership violation

* Thu Jul 17 2008 Michael Bochkaryov <misha@altlinux.ru> 2.22-alt1
- 2.22 version build

* Sun Apr 13 2008 Michael Bochkaryov <misha@altlinux.ru> 2.1-alt1
- first build for ALT Linux Sisyphus
