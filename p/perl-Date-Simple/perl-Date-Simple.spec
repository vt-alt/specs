#
#   - Date::Simple -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       -f mlist
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Date-Simple
%define m_distro Date-Simple
%define m_name Date::Simple
%define m_author_id unknown
%define _enable_test 1

Name: perl-Date-Simple
Version: 3.03
Release: alt3.2

Summary: a simple date object

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Kirill Maslinsky <kirill@altlinux.org>

Source: http://search.cpan.org//CPAN/authors/id/I/IZ/IZUT/%m_distro-%version.tar.gz

# Automatically added by buildreq on Wed Nov 02 2011
BuildRequires: perl-devel

%description
Dates are complex enough without times and timezones.  This module may
be used to create simple date objects.  It handles:

=over 4

=item Validation.

Reject 1999-02-29 but accept 2000-02-29.

=item Interval arithmetic.

How many days were between two given dates?  What date comes N days
after today?

=item Day-of-week calculation.

What day of the week is a given date?

=item Transparent date formatting.

How should a date object be formatted.

=back

It does not deal with hours, minutes, seconds, and time zones.

A date is uniquely identified by year, month, and day integers within
valid ranges.  This module will not allow the creation of objects for
invalid dates.  Attempting to create an invalid date will return
undef.  Month numbering starts at 1 for January, unlike in C and Java.
Years are 4-digit.

Gregorian dates up to year 9999 are handled correctly, but we rely on
Perl's builtin `localtime' function when the current date is
requested.  On some platforms, `localtime' may be vulnerable to
rollovers such as the Unix `time_t' wraparound of 18 January 2038.

Overloading is used so you can compare or subtract two dates using
standard numeric operators such as `==', and the sum of a date object
and an integer is another date object.

Date::Simple objects are immutable.  After assigning `$date1' to
`$date2', no change to `$date1' can affect `$date2'.  This means,
for example, that there is nothing like a `set_year' operation, and
`$date++' assigns a new object to `$date'.

This module contains various undocumented functions.  They may not be
available on all platforms and are likely to change or disappear in
future releases.  Please let the author know if you think any of them
should be public.

%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Date/*
%perl_vendor_autolib/Date/*

%changelog
* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 3.03-alt3.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.03-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.03-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.03-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.03-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 3.03-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 3.03-alt2
- rebuilt for perl-5.16

* Wed Nov 02 2011 Kirill Maslinsky <kirill@altlinux.org> 3.03-alt1
- initial build for ALT Linux Sisyphus

