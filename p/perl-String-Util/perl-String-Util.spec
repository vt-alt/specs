%define _unpackaged_files_terminate_build 1
%define module_name String-Util
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(Exporter.pm) perl(FileHandle.pm) perl(Module/Build.pm) perl(Number/Misc.pm) perl(Test/Toolbox.pm) perl(base.pm) perl(overload.pm) perl(Module/Build/Tiny.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.31
Release: alt1
Summary: String::Util -- String processing utilities
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/B/BA/BAKERSCOT/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
String::Util provides a collection of small, handy utilities for processing
strings.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes docs
%perl_vendor_privlib/S*

%changelog
* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.26-alt2
- to Sisyphus as perl-Finance-Quote dep

* Sun Sep 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- regenerated from template by package builder

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- regenerated from template by package builder

* Tue May 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- initial import by package builder

