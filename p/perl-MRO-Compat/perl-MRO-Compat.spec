%define _unpackaged_files_terminate_build 1
%define module	MRO-Compat
%define name	perl-%{module}

Name:		%{name}
Version:	0.13
Release:	alt2
Summary:	mro::* interface compatibility for Perls < 5.9.5
URL:		http://search.cpan.org/dist/%{module}
Source0:		http://www.cpan.org/authors/id/H/HA/HAARG/%{module}-%{version}.tar.gz
License:	GPL
Group:		Development/Perl
# Automatically added by buildreq on Fri Nov 13 2009 (-bi)
BuildRequires: perl-Class-C3 perl-Test-Pod perl-Test-Pod-Coverage

BuildRequires:	perl-devel
BuildRequires:	perl-Class-C3
BuildRequires:	perl-Class-C3-XS
BuildArch:	noarch


%description
The "mro" namespace provides several utilities for dealing with method
resolution order and method caching in general in Perl 5.9.5 and higher.

This module provides those interfaces for earlier versions of Perl (back to
5.6.0 anyways).

It is a harmless no-op to use this module on 5.9.5+. If you're writing a piece
of software that would like to use the parts of 5.9.5+'s mro:: interfaces that
are supported here, and you want compatibility with older Perls, this is the
module for you.

Some parts of this interface will work better with Class::C3::XS installed, but
it's not a requirement.

This module never exports any functions. All calls must be fully qualified with
the mro:: prefix.

The interface documentation here serves only as a quick reference of what the
function basically does, and what differences between MRO::Compat and 5.9.5+
one should look out for. The main docs in 5.9.5's mro are the real interface
docs, and contain a lot of other

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib


%changelog
* Sat Nov 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- build w/o mro.pm provides

* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1.1
- dropped deprecated BR: perl-Module-Install

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.11-alt1
- 0.11 version

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 0.05-alt3
- sisyphus check fixes

* Thu May 15 2008 Mikhail Pokidko <pma@altlinux.org> 0.05-alt2
- Fixing perl(mro.pm)

* Thu May 15 2008 Mikhail Pokidko <pma@altlinux.org> 0.05-alt1
- Initial build

