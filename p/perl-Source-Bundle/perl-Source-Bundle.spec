# BEGIN SourceDeps(oneline):
BuildRequires: perl(Module/Build/Tiny.pm) perl-devel
# END SourceDeps(oneline)
%define module Source-Bundle

Name: perl-%module
Version: 0.010.001
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: %module-%version.tar
Url: http://search.cpan.org/dist/%module

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc README
%perl_vendor_privlib/Source*

%changelog
* Sun Jun 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.010.001-alt1
- added datatypes

* Thu Jan 31 2019 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- added gem support

* Sun Jan 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build for Sisyphus
