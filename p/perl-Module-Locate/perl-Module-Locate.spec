%define _unpackaged_files_terminate_build 1
#
#   - Module::Locate -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Module::Locate
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Module-Locate
%define m_distro Module-Locate
%define m_name Module::Locate
%define m_author_id BROQ
%define _enable_test 1

Name: perl-Module-Locate
Version: 1.80
Release: alt1

Summary: locate modules in the same fashion as "require" and "use"

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Module-Locate/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/N/NE/NEILB/Module-Locate-%{version}.tar.gz

# Automatically added by buildreq on Wed Apr 09 2008
BuildRequires: perl-devel

%description
Using "locate()", return the path that "require" would find for a given
module or filename (it can also return a filehandle if a reference in @INC
has been used). This means you can test for the existence, or find the path
for, modules without having to evaluate the code they contain.

This module also comes with accompanying utility functions that are used within
the module itself (except for "get_source") and are available for import.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%doc Changes README
%exclude %perl_vendor_archlib

%changelog
* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.80-alt1
- automated CPAN update

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.79-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.76-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.74-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Apr 09 2008 Michael Bochkaryov <misha@altlinux.ru> 1.7-alt1
- first build for ALT Linux Sisyphus

