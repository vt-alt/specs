%define _unpackaged_files_terminate_build 1
%define dist Email-Outlook-Message
Name: perl-%dist
Version: 0.919
Release: alt1

Summary: Easy MIME message parsing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: https://cpan.metacpan.org/authors/id/M/MV/MVZ/%{dist}-%{version}.tar.gz

BuildArch: noarch

Provides: perl-Email-Outlook-Message-AddressInfo perl-Email-Outlook-Message-Attachment perl-Email-Outlook-Message-Base

BuildRequires: perl-Carp-Always perl-Encode perl-Getopt-Long-Descriptive perl-IO-All perl-IO-String perl-Module-Build perl-Pod-Usage perl-Test-Pod-Coverage perl-Email-MIME perl-Email-MIME-ContentType perl-Email-Sender perl-Email-Simple perl-OLE-Storage_Lite

%description
Parses .msg message files as produced by Microsoft Outlook.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGELOG README
%perl_vendor_privlib/Email*
%_bindir/msgconvert
%_mandir/man1/msgconvert.1.xz

%changelog
* Mon Sep 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.919-alt1
- backport to p9 (closes: #38978)

