%define _unpackaged_files_terminate_build 1
%define dist TimeDate
Name: perl-%dist
Version: 2.32
Release: alt1

Summary: Date and time manipulation routines for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/A/AT/ATOOMIC/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel

%description
This package includes a number of modules suited for manipulation of time
and date strings with Perl.  In particular, the Date::Format and Date::Parse
modules can display and read times and dates in various formats, providing
a more reliable interface to textual representations of points in time.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Date*
%perl_vendor_privlib/Time*

%changelog
* Sat Mar 14 2020 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1
- automated CPAN update

* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 2.31-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.30-alt1
- automated CPAN update

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.20-alt2
- rebuilt as plain src.rpm

* Mon Feb 15 2010 Alexey Tourbin <at@altlinux.ru> 1.20-alt1
- 1.19 -> 1.20

* Mon Oct 19 2009 Alexey Tourbin <at@altlinux.ru> 1.19-alt1
- 1.16 -> 1.19

* Wed Feb 28 2007 Alexey Tourbin <at@altlinux.ru> 1.16-alt2
- imported into git and adapted for gear
- applied documentation patch from debian
- manual pages not packaged, use perldoc

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.16-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Aug 26 2003 Alexey Tourbin <at@altlinux.ru> 1.16-alt1
- 1.16
- description updated (RH)

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 1.14-alt1
- 1.14

* Fri Nov 01 2002 Dmitry V. Levin <ldv@altlinux.org> 1.13.01-alt1
- 1.1301

* Fri Jun 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.13-alt1
- 1.13

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 1.11-alt1
- 1.11

* Mon Jun 25 2001 Stanislav Ievlev 1.10-alt1
- Rebuilt with perl-5.6.1

* Fri Mar 30 2001 Peter 'Nidd' Novodvorsky <nidd@altlinux.ru> ipl4mdk
- Added AutoReqProv: perl.

* Fri Jan 26 2001 Alexander Bokovoy <ab@avilink.net> ipl3mdk
- Rebuild from scratch using MZh's spec skeleton file
