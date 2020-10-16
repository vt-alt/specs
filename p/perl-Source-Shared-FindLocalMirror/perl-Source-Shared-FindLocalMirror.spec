%define module Source-Shared-FindLocalMirror

Name: perl-%module
Version: 0.008
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Local Mirror locator for Source-Shared framework
Group: Development/Perl
License: GPLv2+ or Artistic-2.0
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
#Url: http://search.cpan.org/dist/%module
Url: http://git.altlinux.org/people/viy/packages/perl-%module

BuildRequires: perl-devel perl(Module/Build/Tiny.pm) perl(Source/Shared/CLI.pm)

%description
a small Local Mirror locator library
for Source-Shared framework

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%_bindir/*
%perl_vendor_privlib/S*

%changelog
* Wed Oct 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- altlinux-find-local-mirror: both -b sisyphus and -b Sisyphus

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- added p9 & p10 support

* Wed Oct 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- added /var/ftp/pub/distribution

* Fri Oct 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- new version

* Tue Apr 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- new version

* Sun Apr 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- new version

* Sat Apr 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- added script/altlinux-find-local-mirror

* Sat Apr 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
