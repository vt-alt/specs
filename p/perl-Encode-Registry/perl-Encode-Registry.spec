#
#   - Encode::Registry -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Encode::Registry
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Encode-Registry
%define m_distro Encode-Registry
%define m_name Encode::Registry
%define m_author_id unknown
%define _enable_test 1

Name: perl-Encode-Registry
Version: 0.13
Release: alt1

Summary: Encoding Registry module

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/M/MH/MHOSKEN/%m_distro-%version.tar.gz

# Automatically added by buildreq on Sat Mar 28 2009 (-bi)
BuildRequires: perl-XML-Parser perl-devel

%description
The Encode module provides a Perl interface to the cross-architecture
registry of character encoding information. This registry takes the
form of an XML file containing information about encoding files, their
types and handlers for different file types on different platforms
(or programming environments).

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/
mkdir -p %buildroot%perl_vendor_privlib/Encode/
install -m644 lib/Encode/Registry.pm %buildroot%perl_vendor_privlib/Encode/Registry.pm

%files
%perl_vendor_privlib/Encode/

%changelog
* Fri Mar 27 2009 Vitaly Lipatov <lav@altlinux.ru> 0.13-alt1
- initial build for ALT Linux Sisyphus

