Name: unzip
Version: 6.0
Release: alt4

Packager: Victor Forsyuk <force@altlinux.org>

Summary: An utility for unpacking zip archives
License: Info-ZIP
Group: Archiving/Compression

Url: http://www.info-zip.org/
%define src_ver	%(echo %version|sed "s/\\.//"g)
Source: http://downloads.sourceforge.net/infozip/unzip%src_ver.tar.gz
Patch0: unzip-6.0-alt-natspec.patch

# Not sent to upstream.
Patch1: unzip-6.0-bzip2-configure.patch
# Upstream plans to do this in zip (hopefully also in unzip).
Patch2: unzip-6.0-exec-shield.patch
# Upstream plans to do similar thing.
Patch3: unzip-6.0-close.patch
# Details in rhbz#532380.
# Reported to upstream: http://www.info-zip.org/board/board.pl?m-1259575993/
Patch4: unzip-6.0-attribs-overflow.patch
# Not sent to upstream, as it's Fedora/RHEL specific.
# Modify the configure script to accept var LFLAGS2 so linking can be configurable
# from the spec file. In addition '-s' is still removed as before
Patch5: unzip-6.0-configure.patch
Patch6: unzip-6.0-manpage-fix.patch
# Update match.c with recmatch() from zip 3.0's util.c
# This also resolves the license issue in that old function.
# Original came from here: https://projects.parabolagnulinux.org/abslibre.git/plain/libre/unzip-libre/match.patch
Patch7: unzip-6.0-fix-recmatch.patch
# Update process.c
Patch8: unzip-6.0-symlink.patch
# change using of macro "case_map" by "to_up"
Patch9: unzip-6.0-caseinsensitive.patch
# downstream fix for "-Werror=format-security"
# upstream doesn't want hear about this option again
Patch10: unzip-6.0-format-secure.patch

Patch11: unzip-6.0-valgrind.patch
Patch12: unzip-6.0-x-option.patch
Patch13: unzip-6.0-overflow.patch
Patch14: unzip-6.0-cve-2014-8139.patch
Patch15: unzip-6.0-cve-2014-8140.patch
Patch16: unzip-6.0-cve-2014-8141.patch
Patch17: unzip-6.0-overflow-long-fsize.patch

# Fix heap overflow and infinite loop when invalid input is given (#1260947)
Patch18: unzip-6.0-heap-overflow-infloop.patch

# support non-{latin,unicode} encoding
#Patch19: unzip-6.0-alt-iconv-utf8.patch
#Patch20: unzip-6.0-alt-iconv-utf8-print.patch
Patch21: 0001-Fix-CVE-2016-9844-rhbz-1404283.patch

# restore unix timestamp accurately
Patch22: unzip-6.0-timestamp.patch

# fix possible heap based stack overflow in passwd protected files
Patch23: unzip-6.0-cve-2018-1000035-heap-based-overflow.patch

Patch24: unzip-6.0-cve-2018-18384.patch

# covscan issues
Patch25: unzip-6.0-COVSCAN-fix-unterminated-string.patch

Patch26: unzip-zipbomb-part1.patch
Patch27: unzip-zipbomb-part2.patch
Patch28: unzip-zipbomb-part3.patch
Patch29: unzip-zipbomb-manpage.patch

Patch30: CVE-2015-7697-part_from_opensuse.patch

# Automatically added by buildreq on Mon Aug 10 2009
BuildRequires: libnatspec-devel
BuildRequires: bzip2-devel

%description
The unzip utility is used to list, test, or extract files from a zip archive.
Zip archives are commonly found on MS-DOS systems. The zip utility, included in
the zip package, creates zip archives. Zip and unzip are both compatible with
archives created by PKWARE(R)'s PKZIP for MS-DOS, but the programs' options and
default behaviors do differ in some respects.

%prep
%setup -n unzip%src_ver
%patch0 -p1

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#conflicts with natspec
#patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
#conflicts with natspec
#patch19 -p1
#patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
#conflicts with natspec
#patch25 -p1

#CVE-2019-13232 possible zipbomb in unzip
#not works on 32-bit platforms
#patch26 -p1
#patch27 -p1
#patch28 -p1
#patch29 -p1

%patch30 -p1

ln -s unix/Makefile .

%__subst 's/1L/1/g' man/*.1

# Let configure emit link flag required for our build instead of useless strip option:
%__subst 's/"-s"/"-lnatspec"/' unix/configure
# Tweak to build with our optimizations and defines:
# IZ_HAVE_UXUIDGID is needed for right functionality of unzip -X
# NOMEMCPY solve problem with memory overlapping - decomression is slowly,
# but successfull.
%define _optlevel 3
%__subst 's/CFLAGS_OPT=.-O3./CFLAGS_OPT="%optflags -DUNIX -DNO_WORKING_ISPRINT -DNOMEMCPY -DIZ_HAVE_UXUIDGID -DDATE_FORMAT=DF_YMD"/g' unix/configure
# -DNO_WORKING_ISPRINT fixes ALT bug #21137.

%build
# We will use `generic' make target instead of ready made `linux' or `linux_noasm`
# This target allows us to use flags and defines produced by unzip's configure
# script at build time instead of hardcoded for linux target.
%make flags
%make_build -e generic
%make test

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -p -m755 %name f%name %{name}sfx unix/zipgrep %buildroot%_bindir
install -p -m644 man/*.1 %buildroot%_man1dir/
ln -s unzip %buildroot%_bindir/zipinfo

%files
%_bindir/*
%_man1dir/*
%doc BUGS LICENSE

%changelog
* Fri Nov 13 2020 Evgeny Sinelnikov <sin@altlinux.org> 6.0-alt4
- Build with bzip2 compression method support
- Massive apply security patches from Fedora and openSUSE
- Fixes:
  + CVE-2014-8139 CRC32 verification heap-based buffer overread
  + CVE-2014-8140 out-of-bounds write issue in test_compr_eb()
  + CVE-2014-8141 getZip64Data() out-of-bounds read issues
  + CVE-2014-9913 buffer overflow in zipinfo
  + CVE-2014-9636 out-of-bounds read or write and crash
  + CVE-2015-7696 fix for heap overflow
  + CVE-2015-7697 fix infinite loop when extracting empty bzip2 data
  + CVE-2016-9844 buffer overflow in zipinfo in similar way like fix for CVE-2014-9913
  + CVE-2018-1000035 heap based buffer overflow when opening password protected files
  + CVE-2018-18384 buffer overflow, when a ZIP archive specially crafted

* Wed Jan 15 2020 Nikita Ermakov <arei@altlinux.org> 6.0-alt3
- Update license to meet the SPDX.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 6.0-alt2.qa1
- NMU: rebuilt for debuginfo.

* Mon Sep 21 2009 Victor Forsyuk <force@altlinux.org> 6.0-alt2
- Fix ALT #21137.

* Mon Aug 10 2009 Victor Forsyuk <force@altlinux.org> 6.0-alt1
- 6.0
- Man pages in section 1, not 1L. Fixed.
- Correct branding: "by ALT Linux Team.  Original by Info-ZIP.".
- Built using DATE_FORMAT=DF_YMD so that unzip -l show dates in ISO format.

* Tue Mar 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 5.52-alt5
- fix CVE-2008-0888

* Wed Aug 01 2007 Eugene Ostapets <eostapets@altlinux.ru> 5.52-alt4
- workaround for stupid incoming, nothing else.

* Mon Jul 30 2007 Eugene Ostapets <eostapets@altlinux.ru> 5.52-alt3
- use libnatspec instead iconv + some guesses (fix bug #12313) tnx lav@
- small cleanup spec: use SMP build, use man1dir only

* Tue Apr 10 2007 Eugene Ostapets <eostapets@altlinux.ru> 5.52-alt2
- fix CAN-2005-2475
- fix CVE-2005-4667

* Tue May 17 2005 Alexey Voinov <voins@altlinux.ru> 5.52-alt1
- new version (5.52)
- iconv patch updated
- ddottrav patch disabled

* Tue Dec 14 2004 Alexey Voinov <voins@altlinux.ru> 5.50-alt4
- added iconv patch (by Dmitry Vukolov <dav@altlinux.org>)
  [fixes #4871]

* Wed Jul 02 2003 Alexey Voinov <voins@altlinux.ru> 5.50-alt3
- Fixed '../' directory traversal for filenames which include
  quote and/or control characters.
- Spec cleanup.

* Mon Sep 30 2002 Dmitry V. Levin <ldv@altlinux.org> 5.50-alt2
- Fixed summaries, description and url.
- Fixed build to:
  + honor $RPM_OPT_FLAGS properly, define _GNU_SOURCE;
  + avoid implicit strip during buiuld.
- Enabled "unshrinking" algorithm (i.e. LZW decompression).
- Build without assembly, it doesn't seem to increase performance.

* Fri Mar 22 2002 Rider <rider@altlinux.ru> 5.50-alt1
- 5.50

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 5.42-alt1
- 5.42

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 5.41-ipl3mdk
- RE adaptions.
- FHSification.

* Thu Apr 20 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.

* Sun Nov 28 1999 Pixel <pixel@linux-mandrake.com>
- non-intel adaptation (thanks to Stefan van der Eijk)
- cleanup (was it really mandrake adapted?!)

* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- build release.

* Mon Aug 23 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 5.40
- ix86 optimizations and various spec cleanings

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- builds on non i386 platforms

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated the version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
