#
#   - Template::Provider::DBIC -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --version 0.02 Template::Provider::DBIC
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Template-Provider-DBIC
%define m_distro Template-Provider-DBIC
%define m_name Template::Provider::DBIC
%define m_author_id DCARDWELL
%define _enable_test 1

Name: perl-Template-Provider-DBIC
Version: 0.02
Release: alt1.1.1

Summary: %m_name - Load templates using DBIx::Class

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Template-Provider-DBIC/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCARDWELL/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Jun 30 2008
BuildRequires: perl-DBD-SQLite perl-DBIx-Class perl-Log-Agent perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-TimeDate perl-version

%description
Template::Provider::DBIC allows a Template object to fetch its data
using DBIx::Class instead of, or in addition to, the default
filesystem-based Template::Provider.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%doc examples/* README Changes
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 0.02-alt1
- first build for ALT Linux Sisyphus

