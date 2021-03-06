#
#   - CSS::Squish -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       CSS::Squish
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module CSS-Squish
%define m_distro CSS-Squish
%define m_name CSS::Squish
%define m_author_id RUZ
%define _enable_test 1

Name: perl-CSS-Squish
Version: 0.10
Release: alt1

Summary: Compact many CSS files into one big file

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
#Source: http://search.cpan.org//CPAN/authors/id/R/RU/RUZ/%m_distro-%version.tar.bz2
Source: http://www.cpan.org/authors/id/T/TS/TSIBLEY/CSS-Squish-0.10.tar.gz

# Automatically added by buildreq on Thu Jan 03 2008
BuildRequires: perl-PerlIO perl-Test-LongString perl-Test-Pod perl-Test-Pod-Coverage perl-URI

%description
This module takes a list of CSS files and concatenates them, making sure
to honor any valid @import statements included in the files.

Following the CSS 2.1 spec, @import statements must be the first rules in
a CSS file.  Media-specific @import statements will be honored by enclosing
the included file in an @media rule.  This has the side effect of actually
*improving* compatibility in Internet Explorer, which ignores
media-specific @import rules but understands @media rules.

It is possible that future versions will include methods to compact
whitespace and other parts of the CSS itself, but this functionality
is not supported at the current time.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/CSS/

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt2
- fix directory ownership violation

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- initial build for ALT Linux Sisyphus

