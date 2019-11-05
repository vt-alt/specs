Name: grep
Version: 3.3.0.16.268ca
Release: alt1

Summary: The GNU versions of grep pattern matching utilities
License: GPLv3+
Group: File tools
Url: https://www.gnu.org/software/grep/

%define srcname %name-%version-%release
# git://git.altlinux.org/people/ldv/packages/grep refs/heads/grep-current
Source0: %srcname.tar
# git://git.altlinux.org/people/ldv/packages/grep refs/heads/po-current
Source1: po-%version-%release.tar

Source3: GREP_COLORS
Source4: color_grep.sh
Source5: color_grep.csh

# due to libpcre relocation.
Requires: libpcre3 >= 0:6.4-alt2
Provides: pcre-grep, pgrep
Obsoletes: pcre-grep, pgrep

BuildRequires: makeinfo, gnulib >= 0.1.2305.95c96
# due to build from git
BuildRequires: gperf
# due to --perl-regexp
BuildRequires: libpcre-devel

%description
The GNU versions of commonly used grep utilities.  grep searches through
textual input for lines which contain a match to a specified pattern
and then prints the matching lines.  GNU's grep utilities include grep,
egrep, fgrep, and pcregrep.

%prep
%setup -n %srcname -a1

# Build scripts expect to find the grep version in this file.
echo -n %version > .tarball-version

# Generate LINGUAS file.
ls po/*.po | sed 's|.*/||; s|\.po$||' > po/LINGUAS

# git and rsync aren't needed for build.
sed -i '/^\(git\|rsync\)[[:space:]]/d' bootstrap.conf

%build
./bootstrap --skip-po --gnulib-srcdir=%_datadir/gnulib

# Unset the variable gl_printf_safe to indicate that we do not need
# a safe handling of non-IEEE-754 'long double' values.
sed -i 's/gl_printf_safe=yes/gl_printf_safe=/' m4/gnulib-comp.m4 configure

%configure \
	--bindir=/bin \
	--disable-silent-rules \
	--enable-gcc-warnings \
	#
%make_build

%install
%makeinstall_std bindir=/bin

# Use symlinks for pcregrep
ln -s grep %buildroot/bin/pcregrep
ln -s grep.1 %buildroot%_man1dir/pcregrep.1

mkdir -p %buildroot%_sysconfdir/profile.d
install -pm755 %_sourcedir/color_grep.{sh,csh} \
	%buildroot%_sysconfdir/profile.d/
install -pm644 %_sourcedir/GREP_COLORS \
	%buildroot%_sysconfdir/

%find_lang %name

%check
# pcre-jitstack needs more stack space
ulimit -s 32768
%make_build -k check

%files -f %name.lang
%config(noreplace) %_sysconfdir/GREP_COLORS
%config(noreplace) %_sysconfdir/profile.d/*
/bin/*
%_mandir/man?/*
%_infodir/*.info*
%doc AUTHORS NEWS README TODO

%changelog
* Sun Oct 13 2019 Dmitry V. Levin <ldv@altlinux.org> 3.3.0.16.268ca-alt1
- grep: v3.3 -> v3.3-16-g268cae4.

* Sun Dec 23 2018 Dmitry V. Levin <ldv@altlinux.org> 3.3-alt1
- grep: v3.0-12-ge2b7253 -> v3.3.
- gnulib: v0.1-1213-g683b60789 -> v0.1-2305-g95c96b6dd.

* Sun Mar 26 2017 Dmitry V. Levin <ldv@altlinux.org> 3.0.0.12.e2b7-alt1
- grep: v3.0-11-gdff64f9 -> v3.0-12-ge2b7253.
- gnulib: v0.1-1209-g24b3216 -> v0.1-1213-g683b607.

* Tue Mar 21 2017 Dmitry V. Levin <ldv@altlinux.org> 3.0.0.11.dff6-alt1
- grep: v2.22 -> v3.0-11-gdff64f9.
- gnulib: v0.1-585-g2fda85e -> v0.1-1209-g24b3216.

* Mon Dec 14 2015 Dmitry V. Levin <ldv@altlinux.org> 2.22-alt1
- Updated to v2.22.
- Updated translations from translationproject.org.

* Sun Sep 20 2015 Dmitry V. Levin <ldv@altlinux.org> 2.21.0.65.4f89-alt1
- Updated to v2.21-65-g4f89.
- Updated translations from translationproject.org.
- Built with gnulib v0.1-585-g2fda85e.

* Fri Feb 21 2014 Dmitry V. Levin <ldv@altlinux.org> 2.18-alt1
- Updated to v2.18.

* Wed Feb 19 2014 Dmitry V. Levin <ldv@altlinux.org> 2.17-alt1
- Updated to v2.17.
- Updated translations from translationproject.org.
- Built with gnulib v0.1-114-gcaf1b31.

* Thu Jan 02 2014 Dmitry V. Levin <ldv@altlinux.org> 2.16-alt1
- Updated to v2.16.
- Updated translations from translationproject.org.
- Built with gnulib v0.1-58-g0f3a662.

* Sun Nov 17 2013 Dmitry V. Levin <ldv@altlinux.org> 2.15-alt2
- Updated to v2.15-6-g9a9b4c5.
- Updated translations from translationproject.org.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 2.15-alt1
- Updated to v2.15-3-g2581aa3.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-8061-g5191b35.

* Mon Apr 08 2013 Dmitry V. Levin <ldv@altlinux.org> 2.14-alt3
- Updated to v2.14-23-gce9c968.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7901-g076ac82.

* Tue Oct 30 2012 Dmitry V. Levin <ldv@altlinux.org> 2.14-alt2
- Updated to grep v2.14-11-g753d122.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7677-g4027785.

* Mon Aug 20 2012 Dmitry V. Levin <ldv@altlinux.org> 2.14-alt1
- Updated to grep v2.14.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7591-g898f143.

* Fri Aug 03 2012 Dmitry V. Levin <ldv@altlinux.org> 2.13-alt1
- Updated to grep v2.13-11-g8c74af8.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7557-gee60576.

* Fri Apr 20 2012 Dmitry V. Levin <ldv@altlinux.org> 2.11-alt1
- Updated to grep v2.11-18-g42f01d2.
- Updated translations from translationproject.org.
- Built with gnulib v0.0-7312-g7995834.

* Sun Nov 20 2011 Dmitry V. Levin <ldv@altlinux.org> 2.10-alt1
- Updated grep to v2.10.
- Updated gnulib to v0.0-6628-g4f6a7ef.
- Updated translations from translationproject.org.
- Fixed %%find_lang misplacement (closes: #26570).

* Thu Jun 23 2011 Dmitry V. Levin <ldv@altlinux.org> 2.9-alt1
- Updated grep to v2.9.
- Updated gnulib to v0.0-5844-g2dbdfc4.
- Updated translations from translationproject.org.

* Thu May 19 2011 Dmitry V. Levin <ldv@altlinux.org> 2.8-alt1
- Updated grep to v2.8.
- Updated gnulib to v0.0-5275-gc6dc8f1.
- Updated translations from translationproject.org.

* Wed May 11 2011 Dmitry V. Levin <ldv@altlinux.org> 2.7-alt4
- Updated grep to v2.7-43-ged23dd2.
- Updated gnulib to v0.0-5245-gc1a8825.
- Updated translations from translationproject.org.

* Mon Jan 31 2011 Dmitry V. Levin <ldv@altlinux.org> 2.7-alt3
- Updated grep to v2.7-24-ga14a699.
- Updated gnulib to v0.0-4672-ga2e8447.
- Updated translations from translationproject.org.
- Added /etc/profile.d/color_grep.*sh and /etc/GREP_COLORS files
  (closes: #24729).

* Mon Oct 04 2010 Dmitry V. Levin <ldv@altlinux.org> 2.7-alt2
- Fixed build on ARM.

* Mon Sep 20 2010 Dmitry V. Levin <ldv@altlinux.org> 2.7-alt1
- Updated to 2.7.

* Fri Apr 02 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.3-alt1
- Updated to 2.6.3.

* Mon Mar 29 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.2-alt1
- Updated to 2.6.2.

* Thu Mar 25 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.1-alt0.1
- Updated to 2.6.1 prerelease snapshot v2.6-17-g74ab780 (closes: #23228).

* Tue Mar 23 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt1
- Updated to 2.6 (closes: #19291).
- Removed obsolete patches.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.1a-alt5
- Moved "make check" to %%check section.

* Mon Jul 13 2009 Dmitry V. Levin <ldv@altlinux.org> 2.5.1a-alt4
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 2.5.1a-alt3
- Imported "fgrep -w" fix by Pavel Kankovsky.
- Adopted Debian fix for big file handling.

* Sat Sep 02 2006 Dmitry V. Levin <ldv@altlinux.org> 2.5.1a-alt2
- Fixed various segfaults due to incorrect bound checks (#9941).
- Applied upstream patch to fix '-D skip' (RH#189580).
- Add requirement on libpcre3 >= 0:6.4-alt2 (#9666).

* Sat Dec 03 2005 Dmitry V. Levin <ldv@altlinux.org> 2.5.1a-alt1
- Updated to 2.5.1a.
- Merged patches from Owl, Debian and Red Hat.
- Cleaned up specfile.
- Enabled PCRE support.

* Tue Oct 28 2003 Stanislav Ievlev <inger@altlinux.ru> 2.5.1-alt0.4.cvs
- fix requires

* Thu Oct 16 2003 Stanislav Ievlev <inger@altlinux.ru> 2.5.1-alt0.3.cvs
- fix manpage

* Tue Oct 29 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.1-alt0.2.cvs
- rebuild with gcc3
- added patch from RH ( casesensitive lookup with -o -i options )

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 2.5.1-alt0.1.cvs
- 2.5.1

* Thu Dec 27 2001 Stanislav Ievlev <inger@altlinux.ru> 2.4.2-ipl6mdk
- added Belarusian translation

* Wed Nov 15 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.2-ipl5mdk
- RE adaptions.
- Fixed texinfo documentation.

* Mon Sep 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.2-4mdk
- Add i18n character ranges patch from Ulrich Drepper.

* Sat Sep  2 2000 Pixel <pixel@mandrakesoft.com> 2.4.2-3mdk
- use find_lang

* Wed Jul 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.2-2mdk
- BM.
- Macros.
- CLean-up.

* Thu Mar 30 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.2-1mdk
- Clean up specs.
- Adjust groups.
- 2.4.2.

* Tue Mar  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.4.1-1mdk
- 2.4.1.

* Fri Dec  3 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- adjust URL.
- 2.4.

* Tue Nov 02 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Prereq install-info.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.
- Fix buid as user.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to grep 2.3, added install-info %post/%preun for info

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.0 to 2.1
- spec file cleanups
- added BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
