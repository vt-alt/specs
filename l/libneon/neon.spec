Name: libneon
Version: 0.31.2
Release: alt1
Summary: neon is an HTTP and WebDAV client library
License: LGPLv2+
Group: System/Libraries
Url: https://notroj.github.io/neon/

Obsoletes: %{name}0.25 %{name}0.26

Source: neon-%version.tar.gz
Patch1: neon-0.27.0-multilib.patch

BuildRequires: libexpat-devel libkrb5-devel libssl-devel openssl zlib-devel libgssapi-devel xmlto

%description
neon is an HTTP and WebDAV client library, with a C language API.
Provides lower-level interfaces to directly implement new HTTP
methods, and higher-level interfaces so that you don't have to
worry about the lower-level stuff.

%package devel
Summary: Header files for neon HTTP and WebDAV client library
Group: System/Libraries
Requires: %name = %version-%release
Provides: %{name}0.25-devel %{name}0.26-devel
Obsoletes: %{name}0.25-devel %{name}0.26-devel

%description devel
neon is an HTTP and WebDAV client library, with a C language API.
Provides lower-level interfaces to directly implement new HTTP
methods, and higher-level interfaces so that you don't have to
worry about the lower-level stuff.

%prep
%setup -n neon-%version
%patch1 -p1

%build
%configure \
	--with-ssl \
	--enable-shared \
	--disable-static

%make_build

%check
%make -k check ||:

%install
%makeinstall_std
%define docdir %_docdir/neon-%version
install -pm644 AUTHORS BUGS NEWS README* THANKS TODO doc/*.txt \
	%buildroot/%docdir/
%find_lang neon

%files -f neon.lang
%_libdir/lib*.so.*

%files devel
%doc 
%_bindir/*
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*
%_man1dir/*
%_man3dir/*
%docdir

%changelog
* Sat Feb 13 2021 Fr. Br. George <george@altlinux.ru> 0.31.2-alt1
- Autobuild version bump to 0.31.2

* Wed Sep 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 0.30.2-alt1
- 0.30.2

* Wed Oct 22 2014 Valery Inozemtsev <shrek@altlinux.ru> 0.30.1-alt1
- 0.30.1

* Mon Oct 21 2013 Valery Inozemtsev <shrek@altlinux.ru> 0.30.0-alt1
- 0.30.0

* Wed Apr 17 2013 Dmitry V. Levin <ldv@altlinux.org> 0.29.6-alt2
- Rebuilt with current libssl due to compile time OPENSSL_VERSION_NUMBER
  binding in ne_sock_connect_ssl (closes: #28862).

* Thu May 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.29.6-alt1
- 0.29.6

* Fri Apr 22 2011 Dmitry V. Levin <ldv@altlinux.org> 0.29.5-alt2
- Rebuilt for debuginfo.

* Thu Oct 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.29.5-alt1
- 0.29.5

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.29.4-alt1
- 0.29.4

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 0.29.3-alt2
- Minor packaging improvements.
- Rebuilt with libcrypto.so.10.

* Tue Jan 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.29.3-alt1
- 0.29.3

* Thu Dec 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.29.2-alt1
- 0.29.2

* Thu Dec 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.29.1-alt1
- 0.29.1

* Mon Sep 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.29.0-alt1
- 0.29.0

* Wed Aug 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.28.6-alt1
- 0.28.6:
  + fixed CVE-2009-2473, CVE-2009-2474

* Sun Jul 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.28.5-alt1
- 0.28.5

* Sun Jun 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.28.4-alt3
- apply patch from previous change

* Sat Jun 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.28.4-alt2
- fixed forward compat with new-glibc/old kernel cases (closes: #20471)

* Fri May 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.28.4-alt1
- 0.28.4

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.28.3-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Aug 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.28.3-alt1
- fixed CVE-2008-3746

* Mon Aug 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.28.2-alt3
- added provides libneon0.25-devel, libneon0.26-devel

* Sun Aug 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.28.2-alt2
- Obsoletes libneon0.25, libneon0.26

* Mon Jun 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.28.2-alt1
- 0.28.2

* Tue Jul 24 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.26.4-alt1
- Updated to 0.26.4
- Removed patcges (applied in upstream):
  + neon-0.26.3-ne_auth-kerberos.patch
  + neon-0.26.3-ne_auth-negotiate.patch

* Wed Feb 07 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.26.3-alt2
- Added patches to fix kerberos authentication:
  + neon-0.26.3-ne_auth-kerberos.patch
  + neon-0.26.3-ne_auth-negotiate.patch

* Wed Jan 24 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.26.3-alt1
- Updated to 0.26.3
- Removed uri_lookup patch (applied in upstream)

* Wed Jan 10 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.26.2-alt2
- Applied uri_lookup fix (CVE-2007-0157)

* Sun Dec 17 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.26.2-alt1
- Updated to 0.26.2
- Rediffed alt-linkage patch

* Sun Dec 17 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.26.1-alt1
- Updated to 0.26.1

* Sat Dec 16 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.26.0-alt1
- Updated to 0.26.0
- Packaged translation files

* Thu Feb 16 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.25.5-alt1
- Updated to 0.25.5
- Added Conflicts: libneon-devel (#9085)

* Thu Dec 01 2005 Sviatoslav Sviridov <svd@altlinux.ru> 0.25.4-alt1
- Updated to 0.25.4 (started new branch for the package: both
  libneon and libneon0.25 will be available in Sisyphus)
- Updated alt-linkage patch
- Added build dependency to libgssapi-devel

* Sun Jan 23 2005 Sviatoslav Sviridov <svd@altlinux.ru> 0.24.7-alt3
- added post/postun scripts running ldconfig (#5927)
- building static libraries by default (#5927)

* Wed Aug 18 2004 Dmitry V. Levin <ldv@altlinux.org> 0.24.7-alt2
- Fixed "neon-config --libs" and "pkg-config neon --libs" output.
- Relocated documentation.

* Wed Jul 28 2004 Sviatoslav Sviridov <svd@altlinux.ru> 0.24.7-alt1
- 0.24.7

* Fri May 14 2004 Dmitry V. Levin <ldv@altlinux.org> 0.24.5-alt2
- Fixed libneon sscanf overflow (CAN-2004-0398).
- Do not build static library by default.
- Fixed interpackage dependencies.
- Fixed build dependencies.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.24.5-alt1.1
- Rebuilt with openssl-0.9.7d.

* Wed Apr 14 2004 Sviatoslav Sviridov <svd@altlinux.ru> 0.24.5-alt1
- 0.24.5
- do not apply any patches (already applied in upstream)

* Fri Apr 02 2004 Sviatoslav Sviridov <svd@altlinux.ru> 0.24.4-alt3
- applied patch CAN-2004-0179: neon format string bugs
- compiled with Kerberos support

* Wed Mar 24 2004 Sviatoslav Sviridov <svd@altlinux.ru> 0.24.4-alt2
- packaged file %%_libdir/pkgconfig/neon.pc
- documentation moved to devel subpackage

* Sun Nov 30 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.24.4-alt1
- 0.24.4
- removed *.la

* Mon Oct 13 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.24.3-alt1
- 0.24.3

* Tue Apr 29 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.23.9-alt1
- 0.23.9
- html docs placed in 'html' subdir
- manpages included in libneon-devel

* Mon Mar 03 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.23.8-alt1
- 0.23.8:
  + SECURITY: Prevent control characters from being included in the
    reason_phrase field filled in by ne_parse_statusline(), and in
    the session error string.
  + Disable getaddrinfo() support on HP-UX; fix resolver for HP-UX 11.11.
  + Fix digest auth response verification for >9 responses in session
    (bug manifests as "Server was not authenticated correctly" error).
  + On Linux, skip slow lookup for IPv6 addresses when IPv6 support is
    not loaded in kernel (thanks to Daniel Stenberg for this technique).
  + Update to autoconf 2.57 and libtool 1.4.3.

* Wed Jan 29 2003 Sviatoslav Sviridov <svd@altlinux.ru> 0.23.7-alt1
- new version
- updated BuildRequires

* Fri Nov 22 2002 Rider <rider@altlinux.ru> 0.23.5-alt1
- new version

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 0.23.4-alt1
- new version
- specfile cleanup

* Thu Jun 14 2001 AEN <aen@logic.ru> 0.15.1-alt1
- first build for Sisyphus
