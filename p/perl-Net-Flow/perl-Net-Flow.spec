#
#   - Net::Flow -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       Net::Flow
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Net-Flow
%define m_distro Net-Flow
%define m_name Net::Flow
%define m_author_id unknown
%define _enable_test 1

Name: perl-Net-Flow
Version: 1.003
Release: alt1

Summary: decode and encode NetFlow/IPFIX datagrams

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Eugene Prokopiev <enp@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/A/AC/ACFEREN/Net-Flow-%{version}.tar.gz

# Automatically added by buildreq on Wed Mar 21 2012
BuildRequires: perl-devel

%description
The Flow module provides the decoding function for NetFlow version 5,9 and IPFIX, and the encoding function for NetFlow version 9 and IPFIX. It supports NetFlow version 9 (RFC3945) and NetFlow version 5 (http://www.cisco.com/) and IPFIX(RFC5101). You can easily make the Flow Proxy, Protocol Converter and Flow Concentrator by using the combination of both function, just like Flow Mediator(draft-kobayashi-ipfix-mediator-model-02.txt). The Mediator would have multiple functions by utilizing intermediate process. And also, you can make the flexible Collector which can receive any Templates by using the Storable perl module.

%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/*

%changelog
* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1
- automated CPAN update

* Wed Mar 21 2012 Eugene Prokopiev <enp@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus

