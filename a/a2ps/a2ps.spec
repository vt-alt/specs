%define _unpackaged_files_terminate_build 1

Name: a2ps
Version: 4.14
Release: alt3

# Brain damaged lib/program_name system...
%set_verify_elf_method unresolved=relaxed

Summary: Any to PostScript filter
License: GPL
Group: Publishing
Url: http://www.gnu.org/s/a2ps

Source0: %name-%version.tar
Source1: %name-reconfigure
Patch1: %name-2.13-pld-info.patch
Patch2: %name-2.13-pld-security.patch
Patch3: %name-2.13-pld-etc.patch
Patch4: %name-2.13-pld-flex.patch
Patch5: %name-2.13-pld-glibcpaper.patch
Patch6: %name-2.13-pld-autoenc.patch
Patch7: %name-2.13-pld-i18n.patch
Patch8: %name-2.13-pld-ogonkify-xfig-fix.patch
Patch9: %name-4.13-select_c-filename-shell-command-vulnerability.patch
#Patch10: %name-4.13-alt-gcc3.4.patch
Patch10: %name-4.13-includes.patch
Patch11: %name-4.13-varargs.patch
Patch12: %name-4.13-64bit-fixes.patch
Patch13: %name-4.13-alt-liba2ps_with_lm.patch
Patch14: %name-alt-koi8.edf.patch
Patch15: %name-4.14-gentoo-CVE-2014-0466.patch
Patch16: %name-4.14-debian-fix-bad-free.patch
Patch17: %name-4.14-debian-fix-format-security.patch

PreReq: lib%name = %EVR

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

Requires: fonts-type1-urw

# Automatically added by buildreq on Fri Jan 20 2012
# optimized out: ghostscript-common texlive-base-bin texlive-latex-base
BuildRequires: ImageMagick-tools chrpath flex ghostscript-utils gperf groff-base gv imake libX11-devel libpaper-devel xorg-cf-files

%description
GNU a2ps is an Any to PostScript filter.  Of course it processes plain
text files, but also pretty prints quite a few popular languages.

Its slogan is precisely `` Do The Right Thing '', which means that
though it is highly configurable, everything was made so that a novice
user can do complicated PostScript manipulations.  For instance, it
has the ability to delegate the processing of some files to other
filters (such as groff, texi2dvi, dvips, gzip etc.), what allows a
uniform treatment (n-up, page selection, duplex etc.) of heterogeneous
files.

%description -l ru_RU.KOI8-R
GNU a2ps -- это фильтр, преобразующий документы из различных форматов в
PostScript. Он достаточно прост в использовании, но при этом позволяет
выполнять сложные операции над файлами PostScript. В своей работе он
может взаимодействовать с другими фильтрами, такими как groff, texi2dvi,
dvips, gzip и т.д.

%package -n lib%name
Summary: %name shared library
Group: System/Libraries
License: GPL

%description -n lib%name
The lib%name package contains a shared library of functions of %name' filters.

%description -n lib%name -l ru_RU.KOI8-R
В этом пакете находится динамическая библиотека, используемая фильтрами %name.

%package -n lib%name-devel
Summary: %name development files
Group: Development/C
License: GPL
PreReq: lib%name = %EVR

%description -n lib%name-devel
The lib%name package contains development files for using
lib%name in development.

%description -n lib%name-devel -l ru_RU.KOI8-R
В этом пакете находятся файлы, необхоимые для использования
библиотеки lib%name в разработке приложений.

%package -n lib%name-devel-static
Summary: Staitc library for %name
Group: Development/C
License: GPL
PreReq: lib%name-devel = %EVR

%description -n lib%name-devel-static
This package contains library for building statically linked software.

%description -n lib%name-devel-static -l ru_RU.KOI8-R
В этом пакете находятся файлы, необхоимые для использования
библиотеки lib%name в разработке статических приложений.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p0
# Applied in 4.14
#patch9 -p0
%patch10 -p1
# Rewritten in 4.14
#patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p0
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
lispdir=%_sysconfdir/emacs/site-start.d
%configure --disable-rpath --enable-shared --sysconfdir=%_sysconfdir/%name %{subst_enable static}
%make
chrpath -d ./src/.libs/a2ps

%install
%make DESTDIR=%buildroot install
install -d %buildroot%_sbindir
install -m 755 %SOURCE1 %buildroot%_sbindir

%find_lang %name

%post
# Adapt /usr/share/a2ps/afm/fonts.map to the current system environment
%_sbindir/%name-reconfigure > /dev/null 2>&1

%files -f %name.lang
%config(noreplace) %_sysconfdir/%name/*.cfg
%_bindir/*
%_sbindir/*
%_datadir/%name
%_datadir/ogonkify
%_infodir/*
%_man1dir/*
%doc ANNOUNCE AUTHORS FAQ NEWS README ChangeLog TODO THANKS

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Dec 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.14-alt3
- Applied security patches from Debian and Gentoo (Fixes: CVE-2014-0466, CVE-2015-8107).

* Thu Jan 19 2012 Fr. Br. George <george@altlinux.ru> 4.14-alt2
- Fix build

* Wed Sep 14 2011 Fr. Br. George <george@altlinux.ru> 4.14-alt1
- New old upstream
- Version up

* Mon Oct 09 2006 Fr. Br. George <george@altlinux.ru> 4.13-alt3
- Resurrect from orphaned.
- MDV patches are included.
- VERIFY_ELF_UNRESOLVED set to "relaxed" for ill-designed "program_name".
- Use fonts-type1-urw for koi8 encoding.

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt2
- Fixed compilation with gcc3.4.

* Sat Dec 25 2004 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt1
- Security fix: CAN-2004-1170 

* Thu Dec 11 2003 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt0.4
- Fixed permissions on some sources.

* Sun Dec 07 2003 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt0.3
- *.la files removed.

* Wed Sep 03 2003 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt0.1
- First version of RPM package for Sisyphus.
