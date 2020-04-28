Name: gettext
Version: 0.20.2
Release: alt1

%define libintl libintl3

Summary: GNU libraries and utilities for producing multi-lingual messages
License: GPLv3+ and LGPLv2.1+ and GFDL-1.2+
Group: System/Base
Url: https://www.gnu.org/software/gettext/

# https://ftp.gnu.org/gnu/gettext/gettext-%version.tar.xz
Source: gettext-%version.tar
Source1: msghack.py
Source2: msghack.1
Source3: gettext-po-mode-start.el

Patch10: gettext-alt-autogen.patch
Patch11: gettext-alt-gettextize-quiet.patch
Patch12: gettext-alt-autopoint-archive.patch
Patch13: gettext-alt-tmp-autopoint.patch
Patch14: gettext-alt-gcc.patch
Patch15: gettext-alt-urlview.patch
Patch16: gettext-alt-libtextstyle.patch

Provides: %name-base = %version-%release
Obsoletes: %name-base

%def_disable static
%def_without included_gettext
%def_without java
%def_with emacs

%{?_with_included_gettext:Requires: %libintl = %version-%release}
BuildPreReq: gcc-c++ makeinfo xz %{?_with_java:jdkgcj /proc} %{?_with_emacs:emacs-nox}
# Needed for the --color option of the various programs.
# Otherwise, embedded versions are used, which is forbidden by policy.
BuildRequires: glib2-devel libcroco-devel libncurses-devel libunistring-devel libxml2-devel
# Needed for the test suite.
%{?!_without_check:%{?!_disable_check:BuildRequires: python-modules}}

%package -n %libintl
Summary: The dynamic %libintl library for the gettext package
License: LGPLv2+
Group: System/Libraries
Provides: libintl = %version-%release
Obsoletes: libintl

%package -n %libintl-devel
Summary: Development library for %libintl
License: LGPLv2+
Group: Development/C
Requires: %libintl = %version-%release
Provides: libintl-devel = %version-%release
Obsoletes: libintl-devel

%package -n %libintl-devel-static
Summary: Development static library for %libintl
License: LGPLv2+
Group: Development/C
Requires: %libintl-devel = %version-%release
Provides: libintl-devel-static = %version-%release
Obsoletes: libintl-devel-static

%package tools
Summary: Tools and documentation for developers and translators
License: GPLv3+
Group: Development/Other
Provides: %name-devel = %version-%release
Obsoletes: %name-devel
Requires: %name = %version-%release
Requires: mktemp >= 1:1.3.1
%define lib_suffix %{?_is_libsuff:()(%{_libsuff}bit)}
%{!?_with_included_gettext:Provides: preloadable_libintl.so%lib_suffix}

%package tools-java
Summary: Tools for java developers and translators
License: GPLv3+
Group: Development/Other
Requires: %name-tools = %version-%release

%package tools-python
Summary: Python tools for developers and translators
License: GPLv2+
Group: Development/Other
BuildArch: noarch
Requires: %name-tools = %version-%release

%package doc
Summary: The GNU gettext manual
License: GPLv2+ or GFDL-1.2+
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%package -n libasprintf
Summary: Formatted output to strings in C++
License: LGPLv2+
Group: Development/C++

%package -n libasprintf-devel
Summary: Development related files for libasprintf
License: LGPLv2+
Group: Development/C++
Requires: libasprintf = %version-%release

%package -n libtextstyle
Summary: A text styling library
License: GPLv3+
Group: Development/C++

%package -n libtextstyle-devel
Summary: Development related files for libtextstyle
License: GPLv3+
Group: Development/C++
Requires: libtextstyle = %version-%release

%description
The GNU gettext provides a set of tools and documentation for producing
multi-lingual messages in programs.  Tools include a set of conventions about
how programs should be written to support message catalogs, a directory and
file naming organization for the message catalogs, a runtime library which
supports the retrieval of translated messages, and stand-alone programs for
handling the translatable and the already translated strings.  Gettext provides
an easy to use library and tools for creating, using, and modifying natural
language catalogs and is a powerful and simple method for internationalizing
programs.

This package contains gettext and ngettext utilities.

If you would like to internationalize or incorporate multi-lingual messages
into programs that you're developing, you should install %name-tools.

%description -n %libintl
This package contains the dynamic %libintl library.

%description -n %libintl-devel
This package contains development %libintl library.

%description -n %libintl-devel-static
This package contains static %libintl library.

%description tools
The GNU gettext provides a set of tools and documentation for producing
multi-lingual messages in programs.  Tools include a set of conventions about
how programs should be written to support message catalogs, a directory and
file naming organization for the message catalogs, a runtime library which
supports the retrieval of translated messages, and stand-alone programs for
handling the translatable and the already translated strings.  Gettext provides
an easy to use library and tools for creating, using, and modifying natural
language catalogs and is a powerful and simple method for internationalizing
programs.

If you would like to internationalize or incorporate multi-lingual messages
into programs that you're developing, you should install this package.

%description tools-java
This package adds java support to %name-tools.

%description tools-python
This package contains msghack utility.

%description doc
GNU gettext offers to programmers, translators and even users, a well
integrated set of tools and documentation that provides a framework within
which other free packages may produce multi-lingual messages.

This manual documents GNU gettext.

%description -n libasprintf
This package makes the C formatted output routines (fprintf et al.)
usable in C++ programs, for use with the <string> strings and the
<iostream> streams.

%description -n libasprintf-devel
This packages contains development files for libasprintf,
a formatted output library for C++.

%description -n libtextstyle
The GNU libtextstyle is a text styling library that provides an easy way
to add styling to programs that produce output to a console or terminal
emulator window.

%description -n libtextstyle-devel
This packages contains all development related files for the GNU libtextstyle,
a text styling library.

%prep
%setup
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

# Comment out sys_lib_search_path_spec and sys_lib_dlsearch_path_spec.
mkdir archive
cd archive
archive=../gettext-tools/misc/archive.dir.tar
tar -xf $archive
find -type f -print0 |
	xargs -r0 grep -lZ '\<sys_lib_\(dl\)\?search_path_spec=' -- |
	xargs -r0 sed -i 's/\<sys_lib_\(dl\)\?search_path_spec=/#&/' --
tar --owner=root --group=root -cf $archive *
cd -
rm -rf archive

# Regenerate texinfo documentation.
find -type f -name '*.info*' -delete

# Guard against libtextstyle attempt to bundle libcroco and libxml2.
# The comments indicate this is done because the libtextstyle authors do
# not want applications using their code to suffer startup delays due to
# the relocations in these libraries.  This is not an acceptable reason.
rm -r libtextstyle/gnulib-local/lib/lib* libtextstyle/lib/lib{croco,xml}

%build
%if_with java
if [ ! -f /proc/self/maps ]; then
	echo 'java support is enabled, but /proc/self/maps is not available'
	exit 1
fi
%endif
./autogen.sh --skip-gnulib
%add_optflags -fno-strict-aliasing
%configure --enable-shared \
	--without-included-regex \
	--without-included-glib \
	--without-included-libcroco \
	--without-included-libxml \
	--disable-csharp \
	--without-cvs --without-git \
	%{subst_with emacs} \
	%{subst_enable static} \
	%{?_with_included_gettext:--with-included-gettext} \
	#
# We have to edit libtool files by hand until autoreconf can be used here.
find -type f -name libtool -print0 |
	xargs -r0 grep -lZ '^sys_lib_dlsearch_path_spec="' -- |
	xargs -r0 sed -i 's|^\(sys_lib_dlsearch_path_spec="\).*|\1/%_lib %_libdir"|' --
%make_build

%install
%makeinstall_std \
	lispdir=%_datadir/emacs/site-lisp \
	aclocaldir=%_datadir/aclocal \
	#

install -pD -m755 %_sourcedir/msghack.py \
	%buildroot%_bindir/msghack
install -pm644 %_sourcedir/msghack.1 %buildroot%_man1dir/
install -pD -m644 %_sourcedir/gettext-po-mode-start.el \
	%buildroot%_sysconfdir/emacs/site-start.d/gettext.el

%if_with included_gettext
mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d
echo libintl >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%libintl
#if_enabled static
echo libintl-devel >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%libintl-devel
echo libintl-devel-static >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/%libintl-devel-static
#endif #enabled static
chmod 644 %buildroot%_sysconfdir/buildreqs/packages/substitute.d/*
%endif #with included_gettext
mkdir -p %buildroot%_docdir
%define docdir %_docdir/gettext

%find_lang %name-runtime
%find_lang %name-tools

%check
%make_build -k check VERBOSE=1

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%if_with included_gettext
%files -n %libintl
%config %_sysconfdir/buildreqs/packages/substitute.d/%libintl
%_libdir/libintl*.so.*

#if_enabled static
%files -n %libintl-devel
%config %_sysconfdir/buildreqs/packages/substitute.d/%libintl-devel
%_libdir/libintl*.so

%files -n %libintl-devel-static
%config %_sysconfdir/buildreqs/packages/substitute.d/%libintl-devel-static
%_libdir/libintl*.a
#endif #enabled static
%endif #with included_gettext

%files -f %name-runtime.lang
%_bindir/gettext
%_bindir/ngettext
%_bindir/envsubst
%_bindir/gettext.sh
%_man1dir/gettext.*
%_man1dir/ngettext.*
%_man1dir/envsubst.*

%files tools -f %name-tools.lang
%_libdir/gettext
%{?_with_java:%exclude %_libdir/gettext/gnu.gettext.*}
%_libdir/lib%{name}*.so*
%{!?_with_included_gettext:%_libdir/preloadable_libintl.so}
%_bindir/*
%exclude %_bindir/gettext
%exclude %_bindir/ngettext
%exclude %_bindir/envsubst
%exclude %_bindir/gettext.sh
%exclude %_bindir/msghack
%_includedir/%{name}*
%_mandir/man?/*
%exclude %_man1dir/gettext.*
%exclude %_man1dir/ngettext.*
%exclude %_man1dir/envsubst.*
%exclude %_man1dir/msghack.*
%_infodir/gettext.info*
%_datadir/gettext/
%_datadir/gettext-*/
%{?_with_java:%exclude %_datadir/gettext/libintl.jar}
%_datadir/aclocal/*
%if_with emacs
%_datadir/emacs/site-lisp/*.el*
%config(noreplace) %_sysconfdir/emacs/site-start.d/*.el
%endif
%dir %docdir
%docdir/FAQ.html
%docdir/tutorial.html

%files doc
%docdir
%exclude %docdir/FAQ.html
%exclude %docdir/tutorial.html

%if_with java
%files tools-java
%dir %_libdir/gettext
%_libdir/gettext/gnu.gettext.*
%dir %_datadir/gettext
%_datadir/gettext/libintl.jar
%endif

%files tools-python
%_bindir/msghack
%_man1dir/msghack.*

%files -n libasprintf
%_libdir/libasprintf.so.*

%files -n libasprintf-devel
%_includedir/autosprintf.h
%_libdir/libasprintf.so
%_infodir/autosprintf.info*
%_defaultdocdir/libasprintf

%files -n libtextstyle
%_libdir/libtextstyle.so.*

%files -n libtextstyle-devel
%_includedir/textstyle*
%_libdir/libtextstyle.so
%_infodir/libtextstyle.info*
%_defaultdocdir/libtextstyle/

%changelog
* Tue Apr 14 2020 Dmitry V. Levin <ldv@altlinux.org> 0.20.2-alt1
- 0.20.1 -> 0.20.2.

* Fri Jan 03 2020 Dmitry V. Levin <ldv@altlinux.org> 0.20.1-alt1
- 0.19.8.1 -> 0.20.1 (closes: #37078).

* Tue Oct 30 2018 Dmitry V. Levin <ldv@altlinux.org> 0.19.8.1-alt6
- Updated %%check build dependencies.

* Thu May 03 2018 Dmitry V. Levin <ldv@altlinux.org> 0.19.8.1-alt5
- spec: added emacs knob (enabled by default; by mike@).

* Tue Apr 03 2018 Dmitry V. Levin <ldv@altlinux.org> 0.19.8.1-alt4
- Fixed build with new perl.

* Thu Nov 23 2017 Dmitry V. Levin <ldv@altlinux.org> 0.19.8.1-alt3
- Disabled build of java tools because of gcj retirement, see
  https://lists.altlinux.org/pipermail/devel/2017-November/203532.html.

* Wed Nov 22 2017 Dmitry V. Levin <ldv@altlinux.org> 0.19.8.1-alt2
- autopoint: removed unused code that caused shell.req to generate
  a few bogus dependencies.
- Fixed build with glibc >= 2.25.

* Tue Sep 27 2016 Dmitry V. Levin <ldv@altlinux.org> 0.19.8.1-alt1
- 0.19.6 -> 0.19.8.1 (closes: #31007).

* Tue Dec 08 2015 Dmitry V. Levin <ldv@altlinux.org> 0.19.6-alt1
- Updated to 0.19.6.

* Tue May 26 2015 Dmitry V. Levin <ldv@altlinux.org> 0.19.4-alt1
- Updated to 0.19.4 (closes: #31007).

* Tue Jan 07 2014 Dmitry V. Levin <ldv@altlinux.org> 0.18.3.2-alt1
- Updated to 0.18.3.2.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 0.18.3.1-alt2
- Backported some upstream fixes.

* Mon Oct 28 2013 Dmitry V. Levin <ldv@altlinux.org> 0.18.3.1-alt1
- Updated to 0.18.3.1.

* Sun Apr 07 2013 Dmitry V. Levin <ldv@altlinux.org> 0.18.2.1-alt1
- Updated to 0.18.2.1.

* Tue Aug 28 2012 Dmitry V. Levin <ldv@altlinux.org> 0.18.1.1-alt3
- Synced with Debian gettext-0.18.1.1-9:
  + modified msgfmt to always create little endian .mo files;
  + changed project-id to use quotes around pwd;
  + applied upstream patch that teaches xgettext about new scheme syntax;
  + applied upstream patch that fixes xgettext crash when extracting
    a message with plural that is excluded.
- Fixed build with glibc-2.16.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.18.1.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.18.1.1-alt2
- Fixed build on linux kernel >= 2.6.39.

* Fri Nov 05 2010 Dmitry V. Levin <ldv@altlinux.org> 0.18.1.1-alt1
- Updated to 0.18.1.1 (no changes, just rebuilt for soname set-versions).

* Fri Jun 04 2010 Dmitry V. Levin <ldv@altlinux.org> 0.18.1-alt1
- Updated to 0.18.1.

* Thu Jun 03 2010 Dmitry V. Levin <ldv@altlinux.org> 0.18-alt2
- Packaged tools-python subpackage as noarch.

* Thu Jun 03 2010 Dmitry V. Levin <ldv@altlinux.org> 0.18-alt1
- Updated to 0.18.
- autopoint: built without cvs dependency.
- Dropped clumsy urlview helper, changed all scripts to work without it.

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt10.1
- Rebuilt with python 2.6

* Sun Nov 22 2009 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt10
- autopoint: Disabled sys_lib_dlsearch_path_spec settings in
  installed files to avoid breaking libtool.
- Fixed build of utilities to avoid unwanted RPATH on x86-64.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt9
- Moved "make check" to %%check section.

* Sun Jun 07 2009 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt8
- Built --without-included-regex.

* Sun Jun 07 2009 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt7
- Removed obsolete %%install_info/%%uninstall_info calls.
- Backported several upstream fixes.
- Added README.ALT.
- Built --color support with system libraries instead of embedded.
- Enabled testsuite during build by default.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt6
- Packaged -doc subpackage as noarch.

* Sun Nov 02 2008 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt5
- Rebuilt with gcc4.3.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt4
- Fixed "gettext -n" description (closes: #16770).
- Applied some upstream fixes.

* Fri Feb 15 2008 Dmitry V. Levin <ldv@altlinux.org> 0.17-alt3
- Added --with/without java build option (Kirill A. Shutemov).
- If java support is requested, then ensure that /proc is mounted
  during build (#14483).

* Tue Dec 18 2007 Alex V. Myltsev <avm@altlinux.ru> 0.17-alt2
- Fixed %files: everything java-related in tools-java again.

* Fri Nov 23 2007 Alex V. Myltsev <avm@altlinux.ru> 0.17-alt1
- Updated to 0.17.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 0.14.6-alt2
- Disabled optimization based on strict aliasing rules.

* Sat Sep 23 2006 Dmitry V. Levin <ldv@altlinux.org> 0.14.6-alt1
- Updated to 0.14.6.

* Thu Mar 30 2006 Dmitry V. Levin <ldv@altlinux.org> 0.14.5-alt2
- Fixed a few typos in gettext documentation (#8526).
- Corrected preloadable_libintl.so provides.

* Wed Aug 17 2005 Dmitry V. Levin <ldv@altlinux.org> 0.14.5-alt1
- Updated to 0.14.5.

* Wed Apr 13 2005 Dmitry V. Levin <ldv@altlinux.org> 0.14.4-alt1
- Updated to 0.14.4.

* Tue Mar 15 2005 Dmitry V. Levin <ldv@altlinux.org> 0.14.3-alt1
- Updated to 0.14.3.

* Wed Mar 02 2005 Dmitry V. Levin <ldv@altlinux.org> 0.14.2-alt2
- Do not build with included gettext by default.

* Tue Mar 01 2005 Dmitry V. Levin <ldv@altlinux.org> 0.14.2-alt1
- Updated to 0.14.2.
- Updated patches.

* Mon Jan 17 2005 Dmitry V. Levin <ldv@altlinux.org> 0.14.1-alt5
- Explicitly use automake_1.8 for build.

* Tue Jan 04 2005 Dmitry V. Levin <ldv@altlinux.org> 0.14.1-alt4
- Moved gettext manual to separate subpackage.
- Fixed autopoint temporary file handling.
- Applied few patches from Debian:
  + fixed xgettext misparsing of perl source;
  + improved ABOUT-NLS wording;

* Mon Sep 13 2004 Dmitry V. Levin <ldv@altlinux.org> 0.14.1-alt3
- autopoint, gettextize: Rewritten func_find_curr_installdir
  using readlink(1).
- signed.m4: Fixed "gcc -Wall -Werror" support (#5147).

* Wed Mar 10 2004 Dmitry V. Levin <ldv@altlinux.org> 0.14.1-alt2
- Updated build dependencies.

* Thu Feb 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.14.1-alt1
- Updated to 0.14.1
- Updated patches.
- Removed obsolete or merged upstream patches:
  rh-jbj
  alt-m4-compat
  alt-aclocaldir
  alt-libobjs
  alt-amproglex
  rh-gettextize
- Enabled packaging of emacs site-start.d files again.
- Do not build static libintl library by default.

* Tue Dec 09 2003 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt13
- Do not package .la files.
- Disabled packaging of emacs site-start.d files for a while.

* Fri Dec 13 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt12
- gettextize: fixed AM_GNU_GETTEXT_VERSION corruption (rh).
- msghack: moved to -tools-python subpackage.

* Sun Dec 08 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt11
- gettext.m4: relaxed error reporting (introduced in -alt10).
- Specfile cleanup (removed old unneeded hacks).

* Thu Nov 21 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt10
- gettext.m4: removed broken "compatibility" patch
  (thanks to Sergey Pinaev).
- autopoint: fixed cvs support.
- %name-po-mode-start.el: fixed autoload (#0001614).

* Tue Oct 29 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt9
- Relocated archive.tar.gz from %_datadir/%name/intl/ to
  %_datadir/%name/ in order to repair autopoint.

* Sat Oct 26 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt8
- gettext.m4: fix some compatibility issues.

* Fri Oct 25 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt7
- Fixed gettext-tools subpackage:
  + moved java support to separate subpackage;
  + removed cvs dependence.

* Thu Oct 24 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt6
- Fixed texinfo installation scripts (reported by Alexander Bokovoy).

* Wed Oct 23 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt5
- Added "quiet" option to gettextize.
- Resplit packages:
  gettext-base + gettext + gettext-devel -> gettext + gettext-tools.

* Tue Oct 15 2002 Dmitry V. Levin <ldv@altlinux.org> 0.11.5-alt4
- Updated %post/%postun scripts.
- Fixed library symlinks generation.
- Added %_libdir/gettext to gettext subpackage.
- Relocated all libraries from /lib/ back to %_libdir/.
- Relocated all binaries from /bin/ back to %_bindir/.
- Additional convention enforcement on patch file names.

* Sun Oct 13 2002 Alexey Voinov <voins@voins.program.ru> 0.11.5-alt3.1
- autopoint added to filelist of gettext-devel

* Sun Oct 13 2002 Alexey Voinov <voins@voins.program.ru> 0.11.5-alt3
- new version(0.11.5)
- INSTOBJEXT patch updated to 0.11.5
- libobjs patch added (fixes use of LIBOBJS substitution in configure.in)
- amproglex patch added (hack to please automake-1.6)
- libintl version increased
- html docs included in gettext-devel

* Tue Mar 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.10.40-alt3
- Added buildreq substitution rules.

* Fri Mar 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.10.40-alt2
- Updated emacs po-mode (0000554).
- Preparing to libintl2:
  + renamed libintl subpackage to libintl1;
  + moved libraries from gettext-devel to libintl-* subpackages.

* Wed Sep 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.10.40-alt1
- 0.10.40

* Mon Aug 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.10.39-alt3
- Rebuilt.

* Tue Aug 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.10.39-alt2
- Added msghack utility (rh).

* Tue Jul 31 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.10.39-alt1
- 0.10.39

* Fri May 25 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.10.38-alt1
- 0.10.38

* Sun May 06 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.10.37-alt2
- Resurrected INSTOBJEXT from %name-0.10.35.

* Thu Apr 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.10.37-alt1
- 0.10.37

* Sat Nov 04 2000 Dmitry V. Levin <ldv@fandra.org> 0.10.35-ipl16mdk
- Merged RH patches.
- RE adaptions.

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.10.35-16mdk
- automatically added packager tag

* Tue Aug 22 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.10.35-15mdk
- bugfixed gettextize when headers are not there
  thanks to <rchaillat@mandrakesoft.com>

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.10.35-14mdk
- macros

* Fri May  5 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.10.35-13mdk
- quick patch to have it work!

* Sat Apr 08 2000 John Buswell <johnb@mandrakesoft.com> 0.10.35-12mdk
- added devel package

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 0.10.35-11mdk
- fixed groups
- Removed version number from spec filename
- spec-helper

* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- rebuild for new environment

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- s/arch-RedHat/arch-Mandrake/
- msghack updates.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 8)

* Mon Mar 08 1999 Cristian Gafton <gafton@redhat.com>
- added patch for misc hacks to facilitate rpm translations

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch to allow to build on ARM

* Wed Sep 30 1998 Jeff Johnson <jbj@redhat.com>
- add Emacs po-mode.el files.

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- include the aclocal support files

* Thu Sep  3 1998 Bill Nottingham <notting@redhat.com>
- remove devel package (functionality is in glibc)

* Tue Sep  1 1998 Jeff Johnson <jbj@redhat.com>
- update to 0.10.35.

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- add gettextize.
- create devel package for libintl.a and libgettext.h.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Nov 02 1997 Cristian Gafton <gafton@redhat.com>
- added info handling
- added misc-patch (skip emacs-lisp modofications)

* Sat Nov 01 1997 Erik Troan <ewt@redhat.com>
- removed locale.aliases as we get it from glibc now
- uses a buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Built against glibc
