%define dist Net-RawIP
Name: perl-%dist
Version: 0.25
Release: alt3.2

Summary: Perl extension to manipulate raw IP packets
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# a test tries to open /proc/net/route
BuildPreReq: /proc

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libpcap-devel perl-devel

%description
This is Net::RawIP, a perl module can to manipulate raw IP packets,
with an optional feature for manipulating Ethernet headers.

%prep
%setup -n %dist-%version

%ifdef __BTE
# disable network-dependent tests
mv t/iflist.t t/iflist.t.orig
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.25-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Fri May 29 2009 Michael Shigorin <mike@altlinux.org> 0.2.5-alt1
- initial build for ALT Linux Sisyphus
  (roguedetect dependency)
- buildreq
