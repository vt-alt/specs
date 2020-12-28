# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(File/Basename.pm) perl(FileHandle.pm) perl(Module/Build.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.4
%define module_name Test-Toolbox
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.4
Release: alt2
Summary: Test::Toolbox - tools for testing
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/M/MI/MIKO/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
# load module
 use Test::Toolbox;
 
 # plan tests
 rtplan 43;
 
 # or, plan tests, but die on the first failure
 rtplan 43, autodie=>1;
 
 # basic test
 rtok 'my test name', $success;

 # test for failure if you prefer
 rtok 'test name', $success, should=>0;

 # two values should equal each other
 rtcomp 'test name', $val, $other_val;
 
 # two values should not equal each other
 rtcomp 'test name', $val, $other_val, should=>0;
 
 # run some code which should succeed
 # note that the second param is undef
 rteval 'test name', undef, sub { mysub() };
 
 # run some code which should cause a specific error code
 rteval 'test name', 'file-open-failed', sub { mysub() };
 
 # check that $@ has a specific error code
 rtid 'test name', $@, 'missing-keys';
 
 # much more
%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_privlib/T*

%changelog
* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2
- to Sisyphus as perl-Finance-Quote dep

* Tue Sep 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1
- initial import by package builder

