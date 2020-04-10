Name: pcre
Version: 8.44
Release: alt1

Summary: Perl-compatible regular expression library
License: BSD-style
Group: System/Libraries
Url: http://www.pcre.org/

# ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-%version.tar.bz2
Source: pcre-%version.tar
Source1: pcre-config.1

Patch: pcre-%version-%release.patch

Summary(ru_RU.UTF-8): Библиотека для работы с Perl-совместимыми регулярными выражениями

%define libname libpcre3
%def_enable cpp
%def_disable jit

BuildRequires: gcc-c++ libreadline-devel

%package -n %libname
Summary: Perl-compatible regular expression shared library
Summary(ru_RU.UTF-8): Разделяемая библиотека для работы с регулярными выражениями Perl-стиля
Group: System/Libraries
Provides: pcre-config(utf8)
Provides: pcre-config(unicode-properties)
Provides: %name = %version
Obsoletes: %name < %version

%package -n libpcre16
Summary: Perl-compatible regular expression shared library with UTF-16 support
Summary(ru_RU.UTF-8): Разделяемая библиотека для работы с регулярными выражениями Perl-стиля с поддержкой UTF-16
Group: System/Libraries
Provides: pcre-config(utf16)

%package -n lib%name-devel
Summary: Perl-compatible regular expressions development environment
Summary(ru_RU.UTF-8): Заголовочные файлы и документация для разработки с использованием библиотеки PCRE
Group: Development/C
Provides: %name-devel = %version
Obsoletes: %name-devel < %version
Requires: %libname = %version-%release
Requires: libpcre16 = %version-%release
Requires: pcretest = %version-%release

%package -n lib%name-devel-static
Summary: Perl-compatible regular expressions static library
Summary(ru_RU.UTF-8): Вариант библиотеки PCRE для статической компоновки
Group: Development/C
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static < %version
Requires: lib%name-devel = %version-%release

%package -n lib%{name}cpp3
Summary: Perl-compatible regular expressions C++ wrapper shared library
Summary(ru_RU.UTF-8): Разделяемая библиотека для работы с регулярными выражениями Perl-стиля на C++
Group: System/Libraries
Provides: lib%{name}cpp = %version
Requires: %libname = %version-%release

%package -n lib%{name}cpp-devel
Summary: Perl-compatible regular expressions C++ wrapper development library and header files
Summary(ru_RU.UTF-8): Заголовочные файлы и библиотека для разработки на C++ с использованием PCRE
Group: Development/C
Requires: lib%{name}cpp3 = %version-%release, lib%name-devel = %version-%release

%package -n pcretest
Summary: A program for testing Perl-compatible regular expressions
Group: Development/Other
Requires: %libname = %version-%release
Requires: libpcre16 = %version-%release

%description
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

%description -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет
набор функций для работы с регулярными выражениями, синтаксис и смысл
которых полностью совпадают со встроенными регулярными выражениями
языка Perl версии 5.8.

%description -n %libname
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains PCRE runtime shared libraries.

%description -n %libname -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет
набор функций для работы с регулярными выражениями, синтаксис и смысл
которых полностью совпадают со встроенными регулярными выражениями
языка Perl версии 5.8.

Данный пакет содержит динамическую разделяемую библиотеку PCRE.

%description -n libpcre16
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains libpcre16 runtime dhared library.

%description -n libpcre16 -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет
набор функций для работы с регулярными выражениями, синтаксис и смысл
которых полностью совпадают со встроенными регулярными выражениями
языка Perl версии 5.8.

Данный пакет содержит динамическую разделяемую библиотеку libpcre16.

%description -n lib%{name}cpp3
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains PCRE C++ wrapper shared library.

%description -n lib%{name}cpp3 -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит динамическую разделяемую библиотеку PCRE для C++.

%description -n lib%name-devel
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains development libraries, include files and development
documentation required for developing applications which use perl-style
regular expressions.

%description -n lib%name-devel -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит средства разработки: заголовочные файлы и
документацию, необходимые для написания и сборки программ, использующих
библиотеку PCRE.

%description -n lib%{name}cpp-devel
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains development libraries, include files and development
documentation required for developing C++ applications which use
perl-style regular expressions.

%description -n lib%{name}cpp-devel -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит средства разработки: заголовочные файлы и
документацию, необходимые для написания и сборки программ на C++,
использующих библиотеку PCRE.

%description -n lib%name-devel-static
The PCRE library is a set of functions that implement regular expression
pattern matching using the same syntax and semantics as Perl, with
just a few differences.  The current implementation of PCRE corresponds
approximately with Perl 5.8.

This package contains static development libraries required for developing
statically linked applications which use perl-style regular expressions.

%description -n lib%name-devel-static -l ru_RU.UTF-8
Библиотека PCRE (Perl-compatible regular expressions) предоставляет набор
функций для работы с регулярными выражениями, синтаксис и смысл которых
полностью совпадают со встроенными регулярными выражениями языка Perl
версии 5.8.

Данный пакет содержит библиотеку для статической компоновки программ,
использующих функции PCRE.

%description -n pcretest
pcretest is a program for testing Perl-compatible regular expressions.
It was written as a test program for the PCRE regular expression library
itself, but it can also be  used for experimenting with Perl-compatible
regular expressions.

%prep
%setup
%patch -p1

rm aclocal.m4 m4/{libtool,lt*}.m4

%build
%autoreconf
%define docdir %_docdir/%name-%version
%configure --includedir=%_includedir/%name \
	--docdir=%docdir \
	--enable-pcre8 \
	--enable-pcre16 \
	--enable-utf \
	--enable-unicode-properties \
	--enable-pcretest-libreadline \
	%{subst_enable cpp} \
	%{subst_enable jit} \
	#
%make_build

%install
%makeinstall_std

# Relocate shared libraries from %_libdir/ to /%_lib/.
mkdir %buildroot/%_lib
for f in %buildroot%_libdir/libpcre{,posix}.so; do
	if t=$(readlink "$f"); then
		ln -sf ../../%_lib/"$t" "$f"
	fi
done
mv %buildroot%_libdir/libpcre{,posix}.so.* %buildroot/%_lib/

install -pm644 %_sourcedir/pcre-config.1 %buildroot%_man1dir/

bzip2 -9 %buildroot%docdir/ChangeLog
install -pm644 HACKING pcredemo.c %buildroot%docdir/

rm %buildroot%_bindir/pcregrep
rm %buildroot%_man1dir/pcregrep.*
rm %buildroot%_libdir/*.la

%check
%make_build check

%files -n %libname
/%_lib/libpcre.so.*
/%_lib/libpcreposix.so.*
%dir %docdir
%docdir/[ACLN]*

%files -n libpcre16
%_libdir/libpcre16.so.*

%files -n lib%name-devel
%_libdir/libpcre.so
%_libdir/libpcre16.so
%_libdir/libpcreposix.so
%_includedir/pcre
%_bindir/*
%_pkgconfigdir/libpcre.pc
%_pkgconfigdir/libpcre16.pc
%_pkgconfigdir/libpcreposix.pc
%_man1dir/*
%_man3dir/*
%exclude %_bindir/pcretest
%exclude %_man1dir/pcretest.*
%if_enabled cpp
%exclude %_includedir/pcre/pcrecpp*.h
%exclude %_includedir/pcre/pcre_*.h
%exclude %_man3dir/pcrecpp.*
%endif #cpp
%dir %docdir
%docdir/H*
%docdir/*.c
%docdir/*.txt
%docdir/html
%exclude %docdir/README

%if_enabled cpp
%files -n lib%{name}cpp3
%_libdir/libpcrecpp.so.*

%files -n lib%{name}cpp-devel
%_libdir/libpcrecpp.so
%dir %_includedir/pcre
%_includedir/pcre/pcrecpp*.h
%_includedir/pcre/pcre_*.h
%_pkgconfigdir/libpcrecpp.pc
%_man3dir/pcrecpp.*
%endif #cpp

%files -n lib%name-devel-static
%_libdir/*.a

%files -n pcretest
%_bindir/pcretest
%_man1dir/pcretest.*

%changelog
* Wed Feb 12 2020 Dmitry V. Levin <ldv@altlinux.org> 8.44-alt1
- 8.43 -> 8.44.

* Sat Feb 23 2019 Dmitry V. Levin <ldv@altlinux.org> 8.43-alt1
- 8.42 -> 8.43.

* Thu Jul 12 2018 Dmitry V. Levin <ldv@altlinux.org> 8.42-alt1
- 8.41 -> 8.42.

* Wed Jul 05 2017 Dmitry V. Levin <ldv@altlinux.org> 8.41-alt1
- 8.40 -> 8.41.

* Wed Jan 11 2017 Dmitry V. Levin <ldv@altlinux.org> 8.40-alt1
- 8.39 -> 8.40.

* Tue Jun 14 2016 Dmitry V. Levin <ldv@altlinux.org> 8.39-alt1
- Updated to 8.39.

* Tue Nov 24 2015 Dmitry V. Levin <ldv@altlinux.org> 8.38-alt1
- Updated to 8.38.

* Wed Oct 07 2015 Dmitry V. Levin <ldv@altlinux.org> 8.37-alt3
- Imported some upstream fixes from Fedora pcre-8.37-4 package.

* Tue May 26 2015 Dmitry V. Levin <ldv@altlinux.org> 8.37-alt2
- Bumped libpcrecpp soname due to libstdc++ ABI change.

* Tue May 26 2015 Dmitry V. Levin <ldv@altlinux.org> 8.37-alt1
- Updated to 8.37 (closes: #24958).

* Thu May 30 2013 Dmitry V. Levin <ldv@altlinux.org> 8.33-alt2
- Disabled JIT compiling support because it pulls in pthread library.

* Wed May 29 2013 Dmitry V. Levin <ldv@altlinux.org> 8.33-alt1
- Updated to 8.33.
- Enabled JIT compiling support.

* Sun Dec 16 2012 Dmitry V. Levin <ldv@altlinux.org> 8.32-alt1
- Updated to 8.32.

* Mon Sep 24 2012 Dmitry V. Levin <ldv@altlinux.org> 8.31-alt2
- libpcre3: reintroduced obsolete pcre_info() API for compatiblity.

* Mon Sep 24 2012 Dmitry V. Levin <ldv@altlinux.org> 8.31-alt1
- Updated to 8.31.
- Enabled and packaged libpcre16.

* Wed Dec 14 2011 Dmitry V. Levin <ldv@altlinux.org> 8.21-alt1
- Updated to 8.21.

* Thu Oct 06 2011 Dmitry V. Levin <ldv@altlinux.org> 8.20-alt0.1
- Updated to 8.20-rc2 (closes: #26422).

* Wed Sep 14 2011 Dmitry V. Levin <ldv@altlinux.org> 8.13-alt1
- Updated to 8.13.

* Sat Feb 05 2011 Dmitry V. Levin <ldv@altlinux.org> 8.12-alt2
- Packaged pcretest separately from -devel (closes: #24980).

* Sun Jan 23 2011 Dmitry V. Levin <ldv@altlinux.org> 8.12-alt1
- Updated to 8.12 (closes: #24958).

* Fri Oct 08 2010 Dmitry V. Levin <ldv@altlinux.org> 8.10-alt1
- Updated to 8.10.

* Mon Jun 21 2010 Dmitry V. Levin <ldv@altlinux.org> 8.02-alt1
- Updated to 8.02.
- Synced with Debian 8.02-1.
- Packaged html docs.

* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 7.9-alt3
- Moved "make check" to %%check section.

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 7.9-alt2
- Moved pcrecpp manpage to lib%{name}cpp-devel subpackage.

* Wed May 27 2009 Dmitry V. Levin <ldv@altlinux.org> 7.9-alt1
- Updated to 7.9.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 7.8-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Fri Sep 26 2008 Dmitry V. Levin <ldv@altlinux.org> 7.8-alt1
- Updated to 7.8.

* Thu Sep 11 2008 Alexey Tourbin <at@altlinux.ru> 7.7-alt3
- enable unicode properties (required for glib2)
- provide pcre-config(utf8) and pcre-config(unicode-properties)

* Tue Jul 01 2008 Dmitry V. Levin <ldv@altlinux.org> 7.7-alt2
- pcre_compile: Fix potential heap buffer overflow
  (by Tavis Ormandy, closes: CVE-2008-2371).

* Sat May 31 2008 Dmitry V. Levin <ldv@altlinux.org> 7.7-alt1
- Updated to 7.7.

* Tue Feb 12 2008 Dmitry V. Levin <ldv@altlinux.org> 7.6-alt1
- Updated to 7.6 (CVE-2008-0674).

* Tue Jan 15 2008 Dmitry V. Levin <ldv@altlinux.org> 7.5-alt1
- Updated to 7.5.

* Fri Sep 21 2007 Dmitry V. Levin <ldv@altlinux.org> 7.4-alt1
- Updated to 7.4.

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 7.3-alt1
- Updated to 7.3.

* Sun Jan 14 2007 Dmitry V. Levin <ldv@altlinux.org> 7.0-alt2
- Bump libpcrecpp soname version number to reflect API change.
- Package %_pkgconfigdir/libpcrecpp.pc in libpcrecpp-devel.

* Sat Jan 13 2007 Dmitry V. Levin <ldv@altlinux.org> 7.0-alt1
- Updated to 7.0.

* Sun Sep 24 2006 Dmitry V. Levin <ldv@altlinux.org> 6.7-alt1
- Updated to 6.7.

* Sat Dec 03 2005 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt2
- Relocated shared libraries from %_libdir/ to /%_lib/.
- Merged grep subpackage into devel subpackage.
- Moved pcregrep to grep package.

* Tue Oct 04 2005 Dmitry V. Levin <ldv@altlinux.org> 6.4-alt1
- Updated to 6.4.

* Tue Sep 13 2005 Dmitry V. Levin <ldv@altlinux.org> 6.3-alt1
- Updated to 6.3.
- Updated Debian patches.
- Dropped unused bootstage logic.
- Packaged pcredemo.c (#7720).
- Packaged zpcregrep.
- Packaged C++ bindings in separate subpackages.

* Sun Apr  3 2005 Ilya Evseev <evseev@altlinux.org> 5.0-alt2
- enabled UTF-8 support by default, see bugreport #2030
- added optional bootstage support package, see bugreport #3851

* Tue Mar  8 2005 Ilya Evseev <evseev@altlinux.org> 5.0-alt1
- 5.0
- specfile: added russian summaries/descriptions

* Thu Dec 11 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5-alt1
- Updated to 4.5.
- Removed alt-makefile patch (merged upstream).

* Mon Nov 03 2003 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt1
- Updated to 4.4.
- Changed API, soname and renamed library subpackage to libpcre3.
- Implemented backwards compatibility build mode.
- Reverted back library relocation introduced in 3.4-ipl3mdk.
- Added pcre-config(1) manpage (deb).
- Do not package .la files.
- Updated package descriptions.
- Fixed SMP build.

* Tue Sep 10 2002 Dmitry V. Levin <ldv@altlinux.org> 3.9-alt3
- Fixed lib%name.la

* Sun Sep 01 2002 Dmitry V. Levin <ldv@altlinux.org> 3.9-alt2
- Updated %post/%postun scripts.
- Fixed library symlinks generation.
- Relocated documentation.
- Updated devel-static requirements.

* Mon Jan 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.9-alt1
- 3.9

* Mon Nov 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.7-alt1
- 3.7
- Created subdirectory for include files.

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.5-alt1
- 3.5
- Moved static libraries to devel-static subpackage.
- Corrected requires.
- Corrected license info.
- Added pcretest utility to grep subpackage.

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl4mdk
- Fixed group tag in %name-grep subpackage.
- Libification.

* Wed Dec 13 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl3mdk
- Moved shared libraries from %_libdir to /lib.

* Wed Oct 11 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl2mdk
- Automatically added BuildRequires.

* Thu Aug 24 2000 Dmitry V. Levin <ldv@fandra.org> 3.4-ipl1mdk
- 3.4

* Thu Aug  3 2000 Dmitry V. Levin <ldv@fandra.org> 3.3-ipl1mdk
- 3.3
- Renamed subpackage pgrep --> pcre-grep.

* Wed Jun 28 2000 Dmitry V. Levin <ldv@fandra.org> 3.2-ipl1mdk
- Use FHS-compatible macros.

* Wed May 17 2000 Dmitry V. Levin <ldv@fandra.org>
- 3.2

* Thu Feb 10 2000 Dmitry V. Levin <ldv@fandra.org>
- 3.1

* Sun Dec 12 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Fri Nov 05 1999 Arne Coucheron <arneco@online.no>
  [2.08-1]
- using name and version macros
- changed Group to comply with RH 6.x
- using make install
- using install -d instead of mkdir -p
- removing RPM_BUILD_ROOT before installing
- some changes in the files section

* Fri May 28 1999 Damien Miller <dmiller@ilogic.com.au>
- Built RPMs
