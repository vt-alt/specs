Name: units
Version: 2.19
Release: alt1

Summary: A utility for converting amounts from one unit to another
License: GPLv3+
Group: Office
Url: https://www.gnu.org/software/units/units.html
# https://ftp.gnu.org/pub/gnu/%name/%name-%version.tar.gz
Source: %name-%version.tar
BuildRequires: libreadline-devel makeinfo

%description
Units converts an amount from one unit to another, or tells you what
mathematical operation you need to perform to convert from one unit to
another.  The units program can handle multiplicative scale changes as
well as conversions such as Fahrenheit to Celsius.

%prep
%setup
# remove generated files
rm parse.tab.c *.info*
# do not try to update currency.units from network during build
sed -i '/^install-support:/ s/ currency-units-update//' Makefile.in

%build
%configure
%make_build

%install
%makeinstall_std
ln -s units.1 %buildroot%_man1dir/units_cur.1

s=/usr/share/units/currency.units
t="$(readlink "%buildroot$s")"
case "$t" in
	/*) ln -fnrs "%buildroot$t" "%buildroot$s" ;;
esac

%check
%make_build -k check

%define _unpackaged_files_terminate_build 1

%files
%_bindir/*
%_datadir/%name/
/var/lib/%name/
%_infodir/*.info*
%_man1dir/*
%doc NEWS README

%changelog
* Fri May 31 2019 Dmitry V. Levin <ldv@altlinux.org> 2.19-alt1
- 2.18 -> 2.19.

* Sun Dec 02 2018 Dmitry V. Levin <ldv@altlinux.org> 2.18-alt1
- 2.12 -> 2.18.

* Thu Oct 15 2015 Dmitry V. Levin <ldv@altlinux.org> 2.12-alt1
- 2.11 -> 2.12.

* Wed Nov 19 2014 Dmitry V. Levin <ldv@altlinux.org> 2.11-alt1
- 2.02 -> 2.11.

* Sat Sep 21 2013 Dmitry V. Levin <ldv@altlinux.org> 2.02-alt1
- Updated to 2.02.

* Tue Apr 16 2013 Dmitry V. Levin <ldv@altlinux.org> 2.01-alt1
- Updated to 2.01.
- Enabled test suite.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.88-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Mar 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.88-alt1
- Updated to 1.88.
- Cleaned up specfile.

* Tue Oct 02 2007 Stanislav Ievlev <inger@altlinux.org> 1.87-alt1
- 1.87

* Fri Apr 13 2007 Stanislav Ievlev <inger@altlinux.org> 1.86-alt1
- 1.86
- fix License tag value

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.80-alt2.1
- Rebuilt with libreadline.so.5.

* Mon Jan 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.80-alt2
- fix building with gcc 3.3

* Wed Sep 25 2002 Stanislav Ievlev <inger@altlinux.ru> 1.80-alt1
- 1.80

* Fri Jul 06 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.74-alt1
- new version

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.55-ipl9mdk
- RE adaptions.
- Fixed texinfo documentation.

* Mon Dec 25 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.55-9mdk
- fix BuildRequires

* Thu Dec 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.55-8mdk
- Recompile with full optimisations.

* Tue Nov 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.55-7mdk
- Compile as -O2.
- Change BuildRequires: to the new lib policy.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.55-6mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.55-5mdk
- macros, BM

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.55-4mdk
- Clean up specs.
- Use makeinstall macros.

* Sat Mar 25 2000 Daouda Lo	<daouda@mandrakesoft.com> 1.55-3mdk
- fix group

* Sat Nov 06 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Tue Aug 17 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 1.55
- update source URL
- bzip2 man page
- FHS compliance
- install info page to info dir

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 12)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- units.lib corrections (problem #685)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

