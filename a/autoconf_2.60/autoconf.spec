%define realname autoconf
%define dialect _2.60
%define suff -2.60

Name: %realname%dialect
Version: 2.69
Release: alt6
Epoch: 2

Summary: A GNU tool for automatically configuring source code
License: GPLv2+
Group: Development/Other
Url: https://www.gnu.org/software/%realname/
BuildArch: noarch

%set_compress_method xz
%define srcname %realname-%version-%release
%define __spec_autodep_custom_pre export autom4te_perllibdir=%buildroot%_datadir/%realname%suff

# git://git.altlinux.org/gears/a/autoconf_2.60.git
Source: %srcname.tar

Requires: autoconf-common
# GNU m4 version 1.4.6 or later is required; 1.4.14 or later is recommended.
Requires: m4 >= 1.4.14
# portable mktemp, later obsoleted by coreutils.
Requires: mktemp >= 1:1.3.1

BuildRequires: help2man, makeinfo
%{!?__buildreqs:%{!?_without_check:%{!?_disable_check:BuildRequires: gcc-c++ gcc-g77 libgomp-devel}}}

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to
specify various configuration options.

You should install Autoconf if you are developing software and you'd
like to use it to create shell scripts which will configure your
source code packages.  If you are installing Autoconf, you will also
need to install the GNU m4 package.

Note that the Autoconf package is not required for the end user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not
their use.

%prep
%setup -n %srcname
find -type f -print0 |
	xargs -r0 fgrep -lZ @RPM_AUTOCONF_SUFFIX@ -- |
	xargs -r0 sed -i s,@RPM_AUTOCONF_SUFFIX@,%suff, --

find -type f -print0 |
	xargs -r0 grep -FZl 'mawk gawk' -- |
	xargs -r0 sed -i 's/mawk gawk/gawk mawk/g' --

# patch texinfo file
sed -i '/@direntry/,/@end direntry/ s/^\(\*[[:space:]]\+[[:alnum:].-]\+\)\(:[[:space:]]\+\)(%realname)/\1%suff\2(%realname%suff)/' \
	doc/autoconf.texi

# Build scripts expect to find autoconf version in this file.
echo -n %version > .tarball-version

%build
export ac_cv_prog_EMACS=no
autoreconf -iv
%configure --program-suffix=%suff
%make_build

%install
%makeinstall

# We don't want to include the standards.info stuff in the package,
# since it comes from binutils.
rm -f %buildroot%_infodir/standards*

# Some more helpful scripts.
rm -f %buildroot%_datadir/%realname/INSTALL
mv %buildroot%_datadir/%realname %buildroot%_datadir/%realname%suff

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo %realname >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%name

mv %buildroot%_infodir/%realname.info %buildroot%_infodir/%realname%suff.info

for f in %buildroot%_bindir/*%suff; do
	ln -s "${f##*/}" "${f%%%suff}%dialect"
done

%define _perl_lib_path %perl_vendor_privlib:%_datadir/%realname%suff

%check
%make_build -k check VERBOSE=1

%files
%config %_sysconfdir/buildreqs/packages/substitute.d/%name
%_bindir/*
%_datadir/%realname%suff
%_man1dir/*
%_infodir/*.info*
%doc AUTHORS NEWS README TODO

%changelog
* Wed Oct 02 2019 Dmitry V. Levin <ldv@altlinux.org> 2:2.69-alt6
- Backported two more upstream fixes.
- AC_PATH_XTRA: removed RPATH injection code.

* Thu Apr 11 2019 Dmitry V. Levin <ldv@altlinux.org> 2:2.69-alt5
- %%check: fixed build with libtool 2.4.6.

* Sat Aug 04 2018 Dmitry V. Levin <ldv@altlinux.org> 2:2.69-alt4
- Dropped alternatives in favour of autoconf-defaults setup.

* Mon Dec 07 2015 Dmitry V. Levin <ldv@altlinux.org> 2:2.69-alt3
- Backported yet more upstream fixes.
- Changed compress method from gzip to xz.

* Thu Oct 31 2013 Dmitry V. Levin <ldv@altlinux.org> 2:2.69-alt2
- Backported more upstream fixes.

* Sun Oct 27 2013 Dmitry V. Levin <ldv@altlinux.org> 2:2.69-alt1
- Updated to v2.69.
- Backported upstream documentation fixes.

* Sat Nov 26 2011 Dmitry V. Levin <ldv@altlinux.org> 2:2.68-alt3
- Backported upstream fix for regression in AC_REPLACE_FUNCS.

* Thu Nov 24 2011 Dmitry V. Levin <ldv@altlinux.org> 2:2.68-alt2
- Backported upstream fix for regression in AS_LITERAL_IF.

* Thu Sep 23 2010 Dmitry V. Levin <ldv@altlinux.org> 2:2.68-alt1
- Updated to v2.68.

* Mon Jan 25 2010 Dmitry V. Levin <ldv@altlinux.org> 2:2.65-alt3
- Updated to v2.65-35-ga2889ee.
- Enhanced AC_LANG_WERROR and "gcc -Werror" support in AC_CHECK_FUNC,
  added tests to ensure that AC_CHECK_FUNC remains compatible with
  AC_LANG_WERROR and "gcc -Werror".

* Tue Jan 19 2010 Dmitry V. Levin <ldv@altlinux.org> 2:2.65-alt2
- Updated to v2.65-32-g57b9bc3.
- Fixed recently introduced typos in builtin functions check support.
- Added %%check.
- Reenabled parallel build.

* Tue Jan 05 2010 Dmitry V. Levin <ldv@altlinux.org> 2:2.65-alt1
- Updated to v2.65-19-g6c11abd (closes: #21744).
- autoreconf: Added gtkdocize support.

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 2:2.63-alt4
- Removed obsolete %%install_info/%%uninstall_info calls.

* Mon Apr 27 2009 Dmitry V. Levin <ldv@altlinux.org> 2:2.63-alt3
- autoreconf: Pass --install to libtoolize.

* Fri Nov 21 2008 Dmitry V. Levin <ldv@altlinux.org> 2:2.63-alt2
- autoreconf: Pass -I to aclocal (upstream; closes: #11438).
- Switched to alternatives-0.4.

* Wed Sep 10 2008 Dmitry V. Levin <ldv@altlinux.org> 2:2.63-alt1
- Updated to v2.63.

* Sun Aug 03 2008 Dmitry V. Levin <ldv@altlinux.org> 2:2.62-alt1
- Updated to v2.62-1-gc4a32a0.

* Sun Jan 13 2008 Alex V. Myltsev <avm@altlinux.ru> 2:2.61-alt4
- Unbroke the datadir patch. (This is getting tiresome.)

* Thu Jan 10 2008 Alex V. Myltsev <avm@altlinux.ru> 2:2.61-alt3
- Fixed "set_autoconf_version 2.60".
- Restored the AC_PATH_XTRA patch.
- Pulled from upstream the fix for _AC_PATH_SEPARATOR_PREPARE.

* Tue Dec 25 2007 Dmitry V. Levin <ldv@altlinux.org> 2:2.61-alt2
- Fixed texinfo direntry.

* Wed Nov 28 2007 Alex V. Myltsev <avm@altlinux.ru> 2:2.61-alt1
- 2.61 (straightforward version bump).

* Fri Nov 02 2007 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt7
- Patched AC_LANG_FUNC_LINK_TRY to ask GNU C headers to include stubs.
  This is required for better glibc-devel >= 2.5-alt5 support.

* Thu Oct 18 2007 Alexey Rusakov <ktirf@altlinux.org> 2:2.59-alt6
- Added intltool support to autoreconf.

* Tue Jun 20 2006 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt5
- Merged all warning fixes to single patch.
- Applied Owl patch to use mktemp in a fail-close way.
- Applied RH patch to _AC_PATH_X_DIRECT macro:
  + check for Xlib.h instead of Intrinsic.h to find X11 headers location;
  + try to link with libX11 instead of libXt to find X11 libraries location.

* Thu Feb 24 2005 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt4
- Converted alternatives config file to new format (0.2.0).

* Fri May 14 2004 Alexey Voinov <voins@altlinux.ru> 2:2.59-alt3
- Some more fixes for "-Wall -Werror"

* Tue Jan 06 2004 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt2
- Changed AC_PROG_CXXCPP so it won't fail when no c++
  preprocessor available.

* Thu Nov 27 2003 Dmitry V. Levin <ldv@altlinux.org> 2:2.59-alt1
- Updated to 2.59.

* Sun Nov 16 2003 Dmitry V. Levin <ldv@altlinux.org> 2:2.58-alt1
- Updated to 2.58.
- Removed alt-dnet patch (no longer needed).

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 2:2.57-alt2
- Updated package dependencies.
- Corrected ac_extension order.
- Partially fixed "-Wall -Werror" support (voins, #2913).

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 2:2.57-alt1.1
- move to new alternatives scheme

* Sat Dec 14 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.57-alt1
- Updated to 2.57

* Sun Nov 17 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.56-alt1
- 2.56

* Mon Oct 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.54-alt2
- Removed libdnet checks.
- Explicitly disabled build of autoconf mode for emacs.
- Changed suffix, compatibility symlinks added (#0001192).
- Added autoconf-common support.
- Raised alternatives priority.

* Tue Sep 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.54-alt1
- 2.54

* Sat May 18 2002 Dmitry V. Levin <ldv@altlinux.org> 2.53-alt4
- Fixed typo in provides.

* Wed May 15 2002 Alexey Voinov <voins@altlinux.ru> 2.53-alt3
- Use configure --program-suffix to add suffixes to (almost) all files.
- .alt-datadir patch fixes Makefile.ins to use /usr/share/autoconf_2.5
- Simplified %install section.

* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.53-alt2
- Set compress method to "gzip".
- Set dircategory to "Development/Other".
- Added more files to alternatives support.

* Sat Apr 06 2002 Alexey Voinov <voins@voins.program.ru> 2.53-alt1
- fork from 2:2.13-alt4
- new version (2.53)
- URL corrected
- support for *.info and man pages (update-)alternatives.

* Tue Mar 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 2:2.13-alt4
- Renamed to autoconf_2.13
- Added update-alternatives support (voins).

* Wed Feb 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 2:2.13-alt3
- Fixed acspecific to avoid -lelf usage for getloadavg.

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.13-alt2
- Rebuilt.

* Thu Aug 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.13-alt1
- Revert back to stable version.
- Reworked tmp files handling.
- Merged RH patches:
  + acgeneral.m4: fixed exit status;
  + autoscan.pl: patched to get a better choice of init file (#42071),
    to test for CPP after CC (#42072) and to detect C++ source and g++ (#42073).
  + acspecific.m4: include various standard C headers as needed
    by various autoconf tests (#19114);
  + acgeneral.m4, acspecific.m4: back-ported _AC_PROG_CXX_EXIT_DECLARATION
    from version 2.50 to make detection of C++ exit() declaration prototype
    platform independent. The check is done in AC_PROG_CXX with the result
    stored in "confdefs.h". The exit() prototype in AC_TRY_RUN_NATIVE is no
    longer needed.

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.52b-alt1
- 2.52b

* Fri Aug 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.52-alt1
- 2.52
- Added manpages from debian.

* Sun Dec 24 2000 Dmitry V. Levin <ldv@fandra.org> 2.13-ipl5mdk
- Fixed exit function prototype for gcc >= 2.96.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 2.13-ipl4mdk
- RE adaptions.

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-4mdk
- macros for install-info

* Mon Jul 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-3mdk
- cleanup and macros

* Fri Mar 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.13-2mdk
- new groups

* Mon Mar  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.13-1mdk
- Back to last 2.13 and stable version, add a serial.

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge change of Jeff package.

* Thu May 13 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- 2.14.1

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add patch to help autoconf clean after itself and not leave /tmp clobbered
  with acin.* and acout.* files (can you say annoying?)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)
- use gawk, not mawk

* Thu Mar 18 1999 Preston Brown <pbrown@redhat.com>
- moved /usr/lib/autoconf to /usr/share/autoconf (with automake)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.13.

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- requires perl

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- patch for fixing /tmp race conditions

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- made a noarch package
- uses autoconf
- uses install-info

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built with glibc

