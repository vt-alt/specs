%define _unpackaged_files_terminate_build 1
Name: perl-AnyEvent-HTTP
Version: 2.25
Release: alt3
Summary: AnyEvent::HTTP - simple but non-blocking HTTP/HTTPS client

Group: Development/Perl
License: Perl
Url: %CPAN AnyEvent-HTTP

BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: AnyEvent-HTTP-2.25-perl7.patch
BuildRequires: perl-AnyEvent perl-common-sense perl-devel

%description
%summary

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/AnyEvent/HTTP*
%doc Changes README

%changelog
* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 2.25-alt3
- enabled tests disabled for IO-AIO

* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 2.25-alt2
- support for perl v7 - no feature qw(indirect);

* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1
- new version

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1
- automated CPAN update

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1
- new version 2.15

* Thu May 31 2012 Vladimir Lettiev <crux@altlinux.ru> 2.14-alt1
- 2.13 -> 2.14

* Mon Aug 08 2011 Vladimir Lettiev <crux@altlinux.ru> 2.13-alt1
- initial build
