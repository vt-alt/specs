%define module_version 1.2
%define module_name Number-Misc
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.2
Release: alt2
Summary: Number::Misc - handy utilities for numbers
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MI/MIKO/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
Number::Misc provides some miscellaneous handy utilities for handling numbers.
These utilities handle processing numbers as strings, determining basic properties
of numbers, or selecting a random number from a range.


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_privlib/N*

%changelog
* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2
- to Sisyphus as perl-Finance-Quote dep

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- regenerated from template by package builder

* Tue May 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- initial import by package builder

