%define _unpackaged_files_terminate_build 1
%define dist LWP-MediaTypes
Name: perl-%dist
Version: 6.04
Release: alt1

Summary: Guess media type for a file or a URL
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/O/OA/OALDERS/%{dist}-%{version}.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-devel perl(Test/Fatal.pm)

%description
This module provides functions for handling media (also known as MIME)
types and encodings.  The mapping from file extensions to media types
is defined by the media.types file.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/LWP

%changelog
* Thu Mar 21 2019 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1
- automated CPAN update

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- rebuitl as plain src.rpm

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 6.01-alt2
- rebuilt as plain src.rpm

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.01-alt1
- initial revision
