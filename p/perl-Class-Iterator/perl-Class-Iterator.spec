#
#   - Class::Iterator -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Class::Iterator
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Class-Iterator
%define m_distro Class-Iterator
%define m_name Class::Iterator
%define m_author_id TEXMEC
%define _enable_test 1

Name: perl-Class-Iterator
Version: 0.3
Release: alt2.1

Summary: Class::Iterator - generic iterator object class

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Class-Iterator/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/T/TE/TEXMEC/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Jul 14 2008
BuildRequires: perl-devel

%description
Class::Iterator is a generic iterator object class.
It use a closure an wrap into an object interface.

	use Class::Iterator;

	my $it = Class::Iterator->new(\&closure_generator);
	while (my $v = $it->next) { print "value : $v\n" }

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class*
%doc README

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Sep 23 2008 Michael Bochkaryov <misha@altlinux.ru> 0.3-alt2
- fix directory ownership violation

* Mon Jul 14 2008 Michael Bochkaryov <misha@altlinux.ru> 0.3-alt1
- first build for ALT Linux Sisyphus

