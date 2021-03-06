#
#   - Encode-compat -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Encode::compat
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Encode-compat
%define m_distro Encode-compat
%define m_name Encode-compat
%define m_author_id unknown
%define _disable_test 1

Name: perl-Encode-compat
Version: 0.07
Release: alt2.1

Summary: Encode-compat - Encode.pm compatibility layer

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/A/AU/AUTRIJUS/%m_distro-%version.tar.gz

# Automatically added by buildreq on Tue Jun 07 2005
BuildRequires: perl-devel

%description
WARNING: THIS IS A PROOF-OF-CONCEPT.  Most functions are incomplete.
All implementation details are subject to change!

This module provide a compatibility layer for Encode.pm users on perl
versions earlier than v5.7.1.  It translates whatever call it receives
into Text::Iconv, or (in the future) Unicode::MapUTF8 to perform
the actual work.

The "is_utf8()", "_utf8_on()" and "_utf8_off()" calls are performed
by the method native to the perl version -- 5.6.1 would use
"pack"/"unpack", 5.6.0 uses "tr//CU", etc.

Theoretically, it could be backported to 5.005 and earlier, with none of
the unicode-related semantics available, and serves only as a
abstraction layer above "Text::Iconv", "Unicode::MapUTF8" and possibly
other transcoding modules.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Encode/

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt2
- fix directory ownership violation

* Tue Jun 07 2005 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- first build for ALT Linux Sisyphus
