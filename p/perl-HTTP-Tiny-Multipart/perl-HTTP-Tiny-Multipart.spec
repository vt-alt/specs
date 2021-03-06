%define module_name HTTP-Tiny-Multipart
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(HTTP/Tiny.pm) perl(MIME/Base64.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: Add post_multipart to HTTP::Tiny
Group: Development/Perl
License: artistic_2
URL: http://github.com/reneeb/HTTP-Tiny-Multipart

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/R/RE/RENEEB/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes CONTRIBUTORS
%perl_vendor_privlib/H*

%changelog
* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- to Sisyphus as devscripts dep

* Fri May 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Thu Aug 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

