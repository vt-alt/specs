# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/Exception.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.09
%define module_name ExtUtils-MY_Metafile
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt3
Summary: META.yml customize with ExtUtil::MakeMaker
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/H/HI/HIO/%module_name-%module_version.tar.gz
Patch: ExtUtils-MY_Metafile-0.09.-perl532.patch

BuildArch: noarch

%description
put ExtUtils/MY_Metafile.pm into inc/ExtUtils/MY_Metafile.pm:
and write in your Makefile.PL:

  use ExtUtils::MakeMaker;
  use inc::ExtUtils::MY_Metafile;
  
  my_metafile {
    no_index => {
      directory => [ qw(inc example t), ],
    },
    license  => 'perl',
  };
  
  WriteMakefile(
    DISTNAME => 'Your::Module',
    ...
  );

%prep
%setup -n %module_name-%module_version
%patch -p0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README example
%perl_vendor_privlib/E*

%changelog
* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0.09-alt3
- fixed build with perl 5.32

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- initial import by package builder

