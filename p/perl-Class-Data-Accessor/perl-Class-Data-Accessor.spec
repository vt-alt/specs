#
#   - Class::Data::Accessor -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module Class-Data-Accessor
%define m_distro Class-Data-Accessor
%define m_name Class::Data::Accessor
%define m_author_id CLACO
%def_enable test

Name: perl-Class-Data-Accessor
Version: 0.04004
Release: alt1.1

Summary: %m_name - Inheritable, overridable class and instance data accessor creation

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Class-Data-Accessor/

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Tue Sep 23 2008 (-bi)
BuildRequires: perl-Module-Install

%description
Class::Data::Accessor is the marriage of Class::Accessor and
Class::Data::Inheritable into a single module. It is used for
creating accessors to class data that overridable in subclasses
as well as in class instances.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class*
%doc Changes README 

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.04004-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Sep 23 2008 Michael Bochkaryov <misha@altlinux.ru> 0.04004-alt1
- 0.04004 version
- fix directory ownership violation

* Sat May 24 2008 Michael Bochkaryov <misha@altlinux.ru> 0.04002-alt1
- 0.04002 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.03-alt1
- first build for ALT Linux Sisyphus

