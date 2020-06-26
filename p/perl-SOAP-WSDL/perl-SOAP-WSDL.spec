%define _unpackaged_files_terminate_build 1
%define module SOAP-WSDL

Name: perl-%module
Version: 3.004
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: SOAP-WSDL provides a SOAP client with WSDL support
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/S/SW/SWALTERS/%{module}-%{version}.tar.gz

# Patches from debian
Patch5: SOAP-WSDL-2.00.10-debian-use_test_xml.patch


BuildArch: noarch

# Automatically added by buildreq on Fri Aug 01 2008 (-bi)
BuildRequires: apache2-mod_perl libnss-mdns perl-Class-Std-Fast perl-IO-stringy perl-Log-Agent perl-Module-Build perl-SOAP-Lite perl-Template perl-Term-ReadKey perl-Test-Pod perl-TimeDate perl-Class-Load perl(TAP/Formatter/HTML.pm) perl(File/Find/Rule.pm)

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
SOAP-WSDL provides a SOAP client with WSDL support.

%prep
%setup -q -n %{module}-%{version}
%patch5 -p1

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes LICENSE TODO example
%exclude %_bindir/wsdl2perl.pl*
%exclude %_man1dir/wsdl2perl.pl*
%perl_vendor_privlib/SOAP/*

%changelog
* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 3.004-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 3.002-alt1
- automated CPAN update

* Tue Feb 11 2014 Vladimir Lettiev <crux@altlinux.ru> 2.00.10-alt3
- fixed build with perl-5.18 (patches from Debian)

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 2.00.10-alt2
- fixed build with perl-5.16

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 2.00.10-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 2.00.10-alt1
- 2.00.10

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 2.00.06-alt1
- 2.00.06

* Tue Aug 05 2008 Victor Forsyuk <force@altlinux.org> 2.00.05-alt1
- Initial build.
