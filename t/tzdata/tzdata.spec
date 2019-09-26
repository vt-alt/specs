Name: tzdata
Version: 2019c
Release: alt1

Summary: Timezone data
# tzdata itself is Public Domain, but tzupdate is GPLv2+,
# so it is OK to release the whole as GPLv2+.
License: GPLv2+
Group: System/Base
Url: http://www.iana.org/time-zones
BuildArch: noarch

%define srcname %name-%version-%release
%define srcdir %_usrsrc/%name

# git://git.altlinux.org/gears/t/tzdata.git
Source: %srcname.tar

Provides: zoneinfo /usr/sbin/tzupdate
Obsoletes: zoneinfo
Conflicts: glibc-timezones <= 6:2.5.1-alt7

BuildRequires: hardlink /usr/sbin/zic

%description
This package contains data files with rules for various timezones around
the world.

%package source
Summary: Timezone data source
Group: Development/Other
Requires: %name = %version-%release

%description source
This package contains timezone data source for use by tz compilers.

%prep
%setup -n %srcname
xz -9k NEWS

%build
make CFLAGS='%optflags' VERSION=%version

%install
%make_install install_default DESTDIR=%buildroot TZDATA_TEXT= VERSION=%version
mv %buildroot%_datadir/zoneinfo{-leaps,/right}
rm %buildroot%_datadir/zoneinfo-posix
mkdir %buildroot%_datadir/zoneinfo/posix
cp -al %buildroot%_datadir/zoneinfo/[A-Z]* %buildroot%_datadir/zoneinfo/posix/

install -pDm755 tzupdate %buildroot%_sbindir/tzupdate

rearguard=tzdata%version-rearguard.tar.gz
make $rearguard VERSION=%version
mkdir -p %buildroot%srcdir
tar -xf $rearguard -C %buildroot%srcdir
echo '%name%version' > %buildroot%srcdir/VERSION

# Hardlink identical files together.
%define __spec_install_custom_post hardlink -vc %buildroot

%check
make -k check_tables

%post -p %_sbindir/tzupdate

%files
%_sbindir/tzupdate
%_datadir/zoneinfo
%doc NEWS.xz README *.html

%files source
%srcdir/

%changelog
* Tue Sep 24 2019 Dmitry V. Levin <ldv@altlinux.org> 2019c-alt1
- 2019b -> 2019c (closes: #37260).

* Mon Jul 01 2019 Dmitry V. Levin <ldv@altlinux.org> 2019b-alt1
- 2018i -> 2019b.

* Mon Dec 31 2018 Dmitry V. Levin <ldv@altlinux.org> 2018i-alt1
- 2018g -> 2018i.

* Mon Oct 29 2018 Dmitry V. Levin <ldv@altlinux.org> 2018g-alt2
- tzdata-source: changed format to rearguard.

* Sat Oct 27 2018 Dmitry V. Levin <ldv@altlinux.org> 2018g-alt1
- 2018f -> 2018g.

* Thu Oct 18 2018 Dmitry V. Levin <ldv@altlinux.org> 2018f-alt1
- 2018e -> 2018f.

* Wed May 02 2018 Dmitry V. Levin <ldv@altlinux.org> 2018e-alt1
- 2018d -> 2018e.

* Thu Apr 06 2018 Maxim Voronov <mvoronov@altlinux.org> 2018d-alt2
- tzupdate: create /etc/localtime as a symlink if it does not exist.

* Thu Mar 22 2018 Dmitry V. Levin <ldv@altlinux.org> 2018d-alt1
- 2018c -> 2018d.

* Tue Feb 20 2018 Dmitry V. Levin <ldv@altlinux.org> 2018c-alt2
- Dropped java subpackage.
- Packaged tzdata source.

* Tue Jan 23 2018 Dmitry V. Levin <ldv@altlinux.org> 2018c-alt1
- 2017c -> 2018c.

* Tue Oct 24 2017 Dmitry V. Levin <ldv@altlinux.org> 2017c-alt2
- Unpackaged text data files tzdata.zi and leapseconds.

* Tue Oct 24 2017 Dmitry V. Levin <ldv@altlinux.org> 2017c-alt1
- 2017b -> 2017c.

* Fri Mar 17 2017 Dmitry V. Levin <ldv@altlinux.org> 2017b-alt1
- 2017a -> 2017b.

* Tue Feb 28 2017 Dmitry V. Levin <ldv@altlinux.org> 2017a-alt1
- 2016j -> 2017a.

* Thu Nov 24 2016 Dmitry V. Levin <ldv@altlinux.org> 2016j-alt1
- 2016g -> 2016j.

* Wed Sep 21 2016 Dmitry V. Levin <ldv@altlinux.org> 2016g-alt1
- 2016f -> 2016g.

* Tue Jul 05 2016 Dmitry V. Levin <ldv@altlinux.org> 2016f-alt1
- 2016e -> 2016f.

* Tue Jun 14 2016 Dmitry V. Levin <ldv@altlinux.org> 2016e-alt1
- Updated to 2016e.

* Mon Apr 18 2016 Dmitry V. Levin <ldv@altlinux.org> 2016d-alt1
- Updated to 2016d.

* Wed Mar 23 2016 Dmitry V. Levin <ldv@altlinux.org> 2016c-alt1
- Updated to 2016c.

* Fri Feb 05 2016 Dmitry V. Levin <ldv@altlinux.org> 2016a-alt1
- Updated to 2016a.

* Mon Dec 28 2015 Dmitry V. Levin <ldv@altlinux.org> 2015g-alt1
- Updated to 2015g (closes: #31663).

* Sat Apr 11 2015 Dmitry V. Levin <ldv@altlinux.org> 2015c-alt1
- Updated to 2015c.

* Tue Nov 11 2014 Dmitry V. Levin <ldv@altlinux.org> 2014j-alt1
- Updated to 2014j.

* Wed Oct 22 2014 Dmitry V. Levin <ldv@altlinux.org> 2014i-alt1
- Updated to 2014i.

* Fri Sep 26 2014 Dmitry V. Levin <ldv@altlinux.org> 2014h-alt1
- Updated to 2014h.

* Wed Aug 06 2014 Dmitry V. Levin <ldv@altlinux.org> 2014f-alt1
- Updated to 2014f.

* Sun Mar 09 2014 Dmitry V. Levin <ldv@altlinux.org> 2014a-alt1
- Updated to 2014a.

* Thu Dec 19 2013 Dmitry V. Levin <ldv@altlinux.org> 2013i-alt1
- Updated to 2013i.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 2013h-alt1
- Updated to 2013h.

* Sat Oct 19 2013 Dmitry V. Levin <ldv@altlinux.org> 2013g-alt1
- Updated to 2013g.

* Sat Sep 21 2013 Dmitry V. Levin <ldv@altlinux.org> 2013e-alt1
- Updated to 2013e.

* Mon Jul 08 2013 Dmitry V. Levin <ldv@altlinux.org> 2013d-alt1
- Updated to 2013d.

* Mon Apr 22 2013 Dmitry V. Levin <ldv@altlinux.org> 2013c-alt1
- Updated to 2013c.

* Mon Mar 25 2013 Dmitry V. Levin <ldv@altlinux.org> 2013b-alt1
- Updated to 2013b.

* Mon Mar 04 2013 Dmitry V. Levin <ldv@altlinux.org> 2013a-alt1
- Updated to 2013a.

* Tue Nov 13 2012 Dmitry V. Levin <ldv@altlinux.org> 2012j-alt1
- Updated to 2012j.

* Sun Nov 04 2012 Dmitry V. Levin <ldv@altlinux.org> 2012i-alt1
- Updated to 2012i.

* Sat Oct 27 2012 Dmitry V. Levin <ldv@altlinux.org> 2012h-alt1
- Updated to 2012h.

* Fri Jul 27 2012 Dmitry V. Levin <ldv@altlinux.org> 2012d-alt2
- Packaged and made use of %_sbindir/tzupdate (closes: #27568).

* Wed Jul 25 2012 Dmitry V. Levin <ldv@altlinux.org> 2012d-alt1
- Updated tzdata to 2012d.

* Mon Apr 09 2012 Dmitry V. Levin <ldv@altlinux.org> 2012c-alt1
- Updated tzdata to 2012c.

* Mon Oct 31 2011 Dmitry V. Levin <ldv@altlinux.org> 2011n-alt1
- Updated tzdata to 2011n.

* Mon Oct 24 2011 Dmitry V. Levin <ldv@altlinux.org> 2011m-alt1
- Updated tzdata to 2011m (closes: #26481).

* Wed Sep 28 2011 Dmitry V. Levin <ldv@altlinux.org> 2011k-alt1
- Updated tzdata to 2011k (closes: #26341).

* Wed Sep 14 2011 Cronbuild Service <cronbuild@altlinux.org> 2011j-alt1
- repocop cronbuild 20110914. At your service.

* Tue Aug 30 2011 Cronbuild Service <cronbuild@altlinux.org> 2011i-alt1
- repocop cronbuild 20110830. At your service.

* Fri Jul 01 2011 Cronbuild Service <cronbuild@altlinux.org> 2011h-alt1
- repocop cronbuild 20110701. At your service.

* Wed Apr 27 2011 Cronbuild Service <cronbuild@altlinux.org> 2011g-alt1
- repocop cronbuild 20110427. At your service.

* Sun Apr 17 2011 Cronbuild Service <cronbuild@altlinux.org> 2011f-alt1
- repocop cronbuild 20110417. At your service.

* Tue Apr 05 2011 Dmitry V. Levin <ldv@altlinux.org> 2011e-alt2
- Added gear-cronbuild support (by Igor Vlasenko).

* Sun Apr 03 2011 Dmitry V. Levin <ldv@altlinux.org> 2011e-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2011e.

* Wed Nov 24 2010 Dmitry V. Levin <ldv@altlinux.org> 2010o-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2010o.

* Wed Sep 15 2010 Dmitry V. Levin <ldv@altlinux.org> 2010l-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2010l.

* Thu Aug 05 2010 Dmitry V. Levin <ldv@altlinux.org> 2010k-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2010k.

* Fri Jul 16 2010 Dmitry V. Levin <ldv@altlinux.org> 2010j-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2010j.

* Thu Mar 25 2010 Dmitry V. Levin <ldv@altlinux.org> 2010f-alt2
- Updated tzdata/europe for Russia 28.03.2010 timezone changes
  (closes: #23227).

* Thu Mar 25 2010 Dmitry V. Levin <ldv@altlinux.org> 2010f-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2010f.
- Moved "make check" to %%check section.
- Hardlinked identical files together.

* Thu Jan 14 2010 Dmitry V. Levin <ldv@altlinux.org> 2009u-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2009u.

* Fri Jun 19 2009 Dmitry V. Levin <ldv@altlinux.org> 2009j-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2009j.

* Sun May 03 2009 Dmitry V. Levin <ldv@altlinux.org> 2009g-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2009g.

* Mon Mar 02 2009 Dmitry V. Levin <ldv@altlinux.org> 2009b-alt1
- Updated to ftp://elsie.nci.nih.gov/pub/tzdata2009b.
- Added /etc/localtime update %%post script (closes: #18786).

* Thu Oct 30 2008 Dmitry V. Levin <ldv@altlinux.org> 2008i-alt1
- Updated to 2008i.
- Use gcc-java to build tzdata-java.

* Thu Oct 23 2008 Dmitry V. Levin <ldv@altlinux.org> 2008h-alt1
- Updated to 2008h.
- Use jdkgcj to build tzdata-java.

* Wed Oct 08 2008 Dmitry V. Levin <ldv@altlinux.org> 2008g-alt1
- Ported to ALT Linux.

* Tue Oct  7 2008 Petr Machata <pmachata@redhat.com> - 2008g-1
- Upstream 2008g
  - Fixed future DST transitions for Brazil

* Tue Sep 16 2008 Petr Machata <pmachata@redhat.com> - 2008f-1
- Upstream 2008f
  - Changes for Mauritius (extends DST to years to come)
  - Palestine changes clocks for the duration of Ramadan
  - Argentina will start DST on Sunday October 19, 2008
  - Brazil will start DST on 2008-10-19
- Drop Pakistan and Morocco patches

* Thu Aug 28 2008 Petr Machata <pmachata@redhat.com> - 2008e-2
- Pakistan DST is scheduled until Oct/31
- Morocco DST is scheduled until Aug/31

* Tue Aug 12 2008 Petr Machata <pmachata@redhat.com> - 2008e-1
- Upstream 2008e
  - Changes for Mauritius
  - Leap second coverage for 31/Dec 2008
  - Corrections of historical dates

* Tue Jul  8 2008 Petr Machata <pmachata@redhat.com> - 2008d-1
- Upstream 2008d
  - Changes for Brazil and Mauritius

* Wed May 30 2008 Petr Machata <pmachata@redhat.com> - 2008c-1
- Upstream 2008c
  - Mongolia changes zone
  - Pakistan DST is scheduled until Sep/1, instead of Aug/31
- Drop Morocco and Pakistan patches that are superseded by upstream
- Fix a typo in Java subpackage name

* Tue May 27 2008 Petr Machata <pmachata@redhat.com> - 2008b-3
- Morocco introduces DST

* Fri May 23 2008 Petr Machata <pmachata@redhat.com> - 2008b-2
- Pakistan introduces DST

* Wed Mar 26 2008 Petr Machata <pmachata@redhat.com> - 2008b-1
- Upstream 2008b
  - DST changes for Syria, Cuba; Iraq abandons DST
  - Saigon zone renamed Ho_Chi_Minh; backward link provided
  - Add America/Argentina/San_Luis information

* Tue Mar  4 2008 Petr Machata <pmachata@redhat.com> - 2007k-2
- Chile moves DST to 29/Mar
- Related: #435959

* Thu Jan  3 2008 Petr Machata <pmachata@redhat.com> - 2007k-1
- Upstream 2007k
  - Argentina readopted the daylight saving time

* Tue Dec  4 2007 Petr Machata <pmachata@redhat.com> - 2007j-1
- Upstream 2007j
  - New links America/St_Barthelemy and America/Marigot
  - Venezuela is changing their clocks on December 9 at 03:00

* Mon Nov  5 2007 Petr Machata <pmachata@redhat.com> - 2007i-1
- Upstream 2007i
  - Syria DST will take place at Midnight between Thursday and Friday.
  - Cuba will end DST on the last Sunday of October.
- Update tst-timezone.c from glibc CVS

* Mon Oct  1 2007 Petr Machata <pmachata@redhat.com> - 2007h-1
- Upstream 2007h
  - Brazil will observe DST from 2007-10-14 to 2008-02-17
  - Egypt and Gaza switched earlier than we expected
  - Iran will resume DST next year
  - Venezuela is scheduled to change TZ to -4:30 on January 1

* Thu Sep 25 2007 Keith Seitz <keiths@redhat.com> - 2007g-2
- Add support for building java's zoneinfo files in new
  tzdata-java RPM.

* Wed Aug 22 2007 Petr Machata <pmachata@redhat.com> - 2007g-1
- Fix licensing tag.
- Upstream 2007g
  - Egypt switches the September 7, not September 28
  - Daviess, Dubous, Knox, Martin, and Pike Counties, Indiana, switch
    from central to eastern time in November
  - South Australia, Tasmania, Victoria, New South Wales and Lord Howe
    Island are changing their DST rules effective next year
  - Sync several Antarctic station's rules with the New Zealand
  - leapseconds contain changes from the most recent IERS bulletin

* Wed May  9 2007 Petr Machata <pmachata@redhat.com> - 2007f-1
- Upstream 2007f
  - New Zealand is extending DST, starting later this year.
  - Haiti no longer observes DST.
  - The Turks and Caicos switch at 02:00, not at 00:00, and have
    adopted US DST rules.

* Tue Apr  3 2007 Petr Machata <pmachata@redhat.com> - 2007e-1
- Upstream 2007e
  - Syria switched to summer time at Mar/29.
  - Honduras will not enter DST this year.

* Wed Mar 21 2007 Petr Machata <pmachata@redhat.com> - 2007d-1
- Upstream 2007d
  - Mongolia has abolished DST.
  - Turkey will use EU rules this year, changing at 01:00 UTC rather
    than 01:00 standard time.
  - Cuba observed DST starting Sunday.
  - Resolute, Nunavut switched from Central to Eastern time last
    November.

* Mon Feb 26 2007 Petr Machata <pmachata@redhat.com> - 2007c-1
- Upstream 2007c
  - Pulaski County, Indiana, switched back to eastern time.
  - Turkey switches at 01:00 standard time, not at 01:00 UTC.
- Upstream 2007b
  - Changes to the commentary in "leapseconds".

* Wed Feb  7 2007 Petr Machata <pmachata@redhat.com> - 2007a-2
- tidy up the specfile per rpmlint comments

* Thu Jan 18 2007 Petr Machata <pmachata@redhat.com> - 2007a-1
- Upstream 2007a
  - Updates to Bahamas, they will be in sync with 2007 US DST change
  - New zone Australia/Eucla
  - Africa/Asmera renamed to Africa/Asmara, link created
  - Atlantic/Faeroe renamed to Atlantic/Faroe, link created
- Packaging
  - Adding BuildRequires: glibc-common >= 2.5.90-7 to build tzdata
    with extended 64-bit format necessary for dates beyond 2037

* Wed Nov 29 2006 Petr Machata <pmachata@redhat.com> - 2006p-1
- Upstream 2006p
  - Official version of Western Australia DST trial changes
  - Latitude/longitude changes for Europe/Jersey and Europe/Podgorica

* Wed Nov 22 2006 Petr Machata <pmachata@redhat.com> - 2006o-2
- Patch for Western Australia DST trial

* Thu Nov  9 2006 Petr Machata <pmachata@redhat.com> - 2006o-1
- Cuba has ended its three years of permanent DST.
- Updates in historical timestamps for Chile.

* Tue Oct 10 2006 Petr Machata <pmachata@redhat.com> - 2006m-2
- Proposed upstream patch (#210058)
  - Jordan will switch to winter time on October 27, not September 29
  - Brazil's DST this year is the first Sunday in November to the last
    Sunday in February.  (Thanks to Frederico A. C. Neves.)
  - ISO 3166 codes for Serbia and Montenegro, zone Europe/Podgorica
  - Commentary and past timestamps changes

* Tue Oct  3 2006 Petr Machata <pmachata@redhat.com> - 2006m-1
- Upstream 2006m:
  - Adjustments for Egypt, Palestine, Uruguay
  - Better description of `until' field in zic (8) manpage

* Thu Sep 21 2006 Petr Machata <pmachata@redhat.com> - 2006l-1
- Upstream 2006k, 2006l:
  - Adjustments for Egypt, Palestine, Cuba, Honduras
  - Documentation changes

* Tue Aug 22 2006 Petr Machata <pmachata@redhat.com> - 2006j-1
- Upstream 2006j
  - Honduras stopped observing DST on Monday at 00:00
  - America/Bermuda will follow the US's lead next year
  - America/Moncton will use US-style rules next year
  - New Zone America/Blanc-Sablon, for Canadians who observe AST all
    year
  - New zone: America/Atikokan instead of America/Coral_Harbour
  - New zones: Europe/Jersey, Europe/Guernsey, Europe/Isle_of_Man
  - Historical changes
  - Commentary updates
- Upstream 2006i
  - localtime.c fixes
- Upstream 2006h
  - zic leapsecond fix

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2006g-1.1
- rebuild

* Thu May 11 2006 Petr Machata <pmachata@redhat.com> - 2006g-1
- Honduras chose to follow Guatemala and will observe DST May/6 to Sep/2
- Nicaragua updates

* Tue May  2 2006 Petr Machata <pmachata@redhat.com> - 2006f-1
- Upstream 2006f
  - America/Guatemala observes DST between Apr/30 and Oct/1
  - Historical changes for Nicaragua
  - Update of America/Indiana/Vincennes in zone table

* Thu Apr 20 2006 Petr Machata <pmachata@redhat.com> - 2006d-1
- Upstream 2006d
  - Haiti observes DST
  - Sri Lanka change actually took effect Apr/15
  - All Canada is now scheduled for 2007 US DST rules
  - Some historical fixes

* Thu Apr  6 2006 Petr Machata <pmachata@redhat.com> - 2006c-1
- Upstream 2006c
  - Time-related changes:
    - dozens of historical and commentary changes
    - Iran stopped observing DST
    - Sri Lanka switches from UTC+6 to UTC+5:30
    - America/Thule and America/Edmonton will adopt new US rules,
      starting 2007
    - Tunisia is adopting regular DST
  - Code:
    - asctime.c: Chages in format strings to silent gcc warnings
    - removing K&R notation from function signatures
    - few fixes across the code

* Thu Mar 16 2006 Petr Machata <pmachata@redhat.com> - 2006b-2
- Patch for Sri Lanka time zone change (#184514)

* Thu Feb 22 2006 Petr Machata <pmachata@redhat.com> 2006b-1
- Upstream 2006b:
  - using tz64code version, as 32 is legacy according to tzdata ML
  - new manual pages for ctime, strftime, tzset
  - some source code reorganizations
  - no timezone/dst rule updates

* Thu Feb 02 2006 Petr Machata <pmachata@redhat.com> 2006a-2
- Small changes in tst-timezone.c

* Thu Feb 02 2006 Petr Machata <pmachata@redhat.com> 2006a-1
- Upstream 2006a:
  - private.h(scheck): changing char* to char const*
  - Rule changes for Palestine, zone changes for Indiana/US, both
    changes for Canada.
  - Many related doc changes.
- Naming scheme in spec file doesn't use %%{name}, but tzdata.

* Thu Jan 12 2006 Petr Machata <pmachata@redhat.com> 2005r-3
- 2005r-3
  - Meta changes.  Renaming tzdata.tar.bz2 file to tzdata$ver-base,
    so that it won't clash across updates.

* Thu Jan  5 2006 Petr Machata <pmachata@redhat.com> 2005r-2
- 2005r
  - Zones EST, MST, HST, EST5EDT, CST6CDT, MST7MDT, PST8PDT moved to
    northamerica to guard against old files with obsolete information
    being left in the time zone binary directory.
  - Changes for countries that are supposed to join 2007 US DST
    change.  This includes most of Canada, however entries already in
    the database (Alberta, British Columbia, Newfoundland, Northwest
    Territories, and Yukon) were left alone for the time being.
  - Fixes in zdump.c (abbrok): conditions are chained, and the string
    is checked for emptiness.

* Sat Dec 17 2005 Jakub Jelinek <jakub@redhat.com> 2005q-2
- 2005q
  - changes for Georgia, Azerbaijan, Jordan, Palestine, Cuba, Nicaragua
  - SystemV timezone changes

* Wed Nov  2 2005 Jakub Jelinek <jakub@redhat.com> 2005n-2
- 2005n
  - changes for Kyrgyzstan and Uruguay
- fix a typo in the Makefile (used TZDATA env var instead of TZDIR during
  make check), update tst-timezone.c from glibc CVS (#172102)

* Tue Sep  6 2005 Jakub Jelinek <jakub@redhat.com> 2005m-2
- 2005m
  - changes for USA (extending DST by 4 weeks since 2007), Tunisia,
    Australia, Kazakhstan
  - historical timezone data changes for Japan, Poland, Northern Ireland and
    Mali
  - timezone name change for East Timor

* Fri Jul 15 2005 Jakub Jelinek <jakub@redhat.com> 2005k-2
- 2005k
  - leap seconds update

* Sat Apr 30 2005 Jakub Jelinek <jakub@redhat.com> 2005i-2
- 2005i
  - updates for Iran, Haiti and Nicaragua

* Mon Apr  4 2005 Jakub Jelinek <jakub@redhat.com> 2005h-2
- 2005h
  - fixes for Kazakhstan

* Thu Mar 17 2005 Jakub Jelinek <jakub@redhat.com> 2005g-2
- 2005g
  - fixes for Uruguay
- include README and Theory from tzcode tarball in %%{_docdir};
  Theory includes a good summary of how the timezone data files
  are supposed to be named

* Tue Mar  1 2005 Jakub Jelinek <jakub@redhat.com> 2005f-2
- 2005f
  - more updates for Israel, updates for Azerbaijan

* Wed Jan 26 2005 Jakub Jelinek <jakub@redhat.com> 2005c-3
- 2005c
  - updates for Israel and Paraguay

* Mon Nov 29 2004 Jakub Jelinek <jakub@redhat.com> 2004g-1
- 2004g (#141107)
  - updates for Cuba

* Mon Oct 11 2004 Jakub Jelinek <jakub@redhat.com> 2004e-2
- 2004e (#135194)
  - updates for Brazil, Uruguay and Argentina

* Wed Aug  4 2004 Jakub Jelinek <jakub@redhat.com> 2004b-2
- 2004b

* Mon Oct  6 2003 Jakub Jelinek <jakub@redhat.com> 2003d-1
- 2003d

* Thu Sep 25 2003 Jakub Jelinek <jakub@redhat.com> 2003c-1
- 2003c
- updates for Brazil (#104840)

* Mon Jul 28 2003 Jakub Jelinek <jakub@redhat.com> 2003a-2
- rebuilt

* Mon Jul 28 2003 Jakub Jelinek <jakub@redhat.com> 2003a-1
- initial package
