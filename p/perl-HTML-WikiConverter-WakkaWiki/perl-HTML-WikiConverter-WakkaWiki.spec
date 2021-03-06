#
#   - HTML::WikiConverter::WakkaWiki -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       HTML::WikiConverter::WakkaWiki
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module HTML-WikiConverter-WakkaWiki
%define m_distro HTML-WikiConverter-WakkaWiki
%define m_name HTML::WikiConverter::WakkaWiki
%define m_author_id unknown
%define _enable_test 1

Name: perl-HTML-WikiConverter-WakkaWiki
Version: 0.50
Release: alt2.1

Summary: Convert HTML to WakkaWiki markup

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Thu Jan 03 2008
BuildRequires: perl-HTML-WikiConverter perl-Test-Pod perl-Test-Pod-Coverage

%description
This module contains rules for converting HTML into WakkaWiki
markup. See HTML::WikiConverter for additional usage details.

%prep
%setup -q -n %m_distro-%version
%__subst "s|.*strip_comments.*||g" t/runtests.pl

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTML/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.50-alt2
- fix directory ownership violation

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.50-alt1
- first build for ALT Linux Sisyphus

