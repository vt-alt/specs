BuildRequires: perl(Module/Build.pm)
#
#   - Number::Compare -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only Number::Compare
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Number-Compare
%define m_distro Number-Compare
%define m_name Number::Compare
%define m_author_id unknown
%define _enable_test 1

Name: perl-Number-Compare
Version: 0.03
Release: alt1

Summary: Number-Compare - numeric comparisons

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/R/RC/RCLAMP/Number-Compare-%{version}.tar.gz

# Automatically added by buildreq on Tue Jul 12 2005
BuildRequires: perl-devel

%description
Number::Compare compiles a simple comparison to an anonymous
subroutine, which you can call with a value to be tested again.

Now this would be very pointless, if Number::Compare didn't understand
magnitudes.

The target value may use magnitudes of kilobytes ("k", "ki"),
megabytes ("m", "mi"), or gigabytes ("g", "gi").  Those suffixed
with an "i" use the appropriate 2**n version in accordance with the
IEC standard: http://physics.nist.gov/cuu/Units/binary.html

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Number/

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.01-alt2
- fix directory ownership violation

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.01-alt1
- first build for ALT Linux Sisyphus
