#set_perl_req_method relaxed
#define _without_test 1
%define _unpackaged_files_terminate_build 1
%define module	Convert-UUlib

Name: perl-%module
Version: 1.8
Release: alt4
Epoch: 3
Summary: Perl interface to the uulib library (a.k.a. uudeview/uuenview)

License: GPL or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/%module/
Packager: Alexey Shabalin <shaba@altlinux.ru>

# BuildArch: noarch
Source0: http://www.cpan.org/authors/id/M/ML/MLEHMANN/%{module}-%{version}.tar.gz
Patch1: Convert-UUlib-1.5-alt-system-libuu.patch
Patch2: Convert-UUlib-1.71-alt_strip_stuff_not_in_libuu.patch
Patch3: Convert-UUlib-1.8-alt-system-libuu.patch
Patch4: Convert-UUlib-1.8-perl532.patch

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: libuu-devel perl-devel perl(Canary/Stability.pm) perl(common/sense.pm)

%description
The UUDeview library is a highly portable set of functions
that provide facilities for decoding uuencoded, xxencoded,
Base64 and BinHex-Encoded files as well as for encoding
binary files into all of these representations except BinHex.

%prep
%setup -q -n %{module}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README doc COPYING.Artistic COPYING.GNU
%perl_vendor_archlib/Convert
%perl_vendor_autolib/Convert

%changelog
* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 3:1.8-alt4
- properly fixed for perl 5.34
- removed req_method relaxed
- enabled tests again

* Sun May 30 2021 Igor Vlasenko <viy@altlinux.org> 3:1.8-alt3
- disabled tests and set req method to relaxed to pass perl 5.32 rebuild

* Sun May 30 2021 Igor Vlasenko <viy@altlinux.org> 3:1.8-alt2
- perl 5.32 support

* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 3:1.8-alt1
- automated CPAN update

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 2:1.71-alt1
- automated CPAN update

* Thu Feb 20 2020 Igor Vlasenko <viy@altlinux.ru> 2:1.62-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 2:1.6-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2:1.5-alt1.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2:1.5-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2:1.5-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2:1.5-alt1.1
- rebuild with new perl 5.22.0

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 2:1.5-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2:1.4-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 2:1.4-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 2:1.4-alt3
- rebuilt for perl-5.16

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 2:1.4-alt2
- rebuilt for perl-5.14

* Thu Jun 09 2011 Alexey Shabalin <shaba@altlinux.ru> 2:1.4-alt1.1
- new version 1.4

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1:1.33-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.33-alt1
- automated CPAN update

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1:1.32-alt1
- new version 1.32
- build with system libuu

* Fri Oct 17 2008 Alexey Shabalin <shaba@altlinux.ru> 1:1.12-alt1
- new version 1.12

* Wed Jun 18 2008 Alexey Shabalin <shaba@altlinux.ru> 1:1.11-alt1
- new version 1.11

* Sat Jun 02 2007 Alexey Shabalin <shaba@altlinux.ru> 1:1.09-alt1
- new version 1.09

* Thu Feb 01 2007 Alexey Shabalin <shaba@altlinux.ru> 1:1.08-alt1
- new version 1.08

* Thu Dec 08 2005 Alexey Shabalin <shaba@altlinux.ru> 1:1.06-alt1
- new version 1.06
- 1.051 -> 1.06; raised epoch to deploy new version

* Mon Apr 25 2005 Alexey Shabalin <shaba@altlinux.ru> 1.051-alt1
- update Convert-UUlib-1.051

* Thu Oct 07 2004 Alexey Shabalin <shaba@altlinux.ru> 1.03-alt1
- update Convert-UUlib-1.03

* Wed Mar 17 2004 Alexey Shabalin <shaba@altlinux.ru> 1.01-alt1
- update Convert-UUlib-1.01

* Thu Dec 04 2003 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt0.1
- First release for ALT
