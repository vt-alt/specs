Name: libogg
Version: 1.3.4
Release: alt1

Summary: Ogg Bitstream Library
Summary(ru_RU.UTF-8): Библиотека потокового формата Ogg
License: BSD-3-Clause
Group: System/Libraries
Url: https://www.xiph.org/ogg/
# https://downloads.xiph.org/releases/ogg/%name-%version.tar.xz
Source: %name-%version.tar

%def_disable static

%description
Libogg is a library for manipulating ogg bitstreams. It handles
both making ogg bitstreams and getting packets from ogg bitstreams.

%description -l ru_RU.UTF-8
Libogg - это библиотека для работы с потоками формата ogg.
С ее помощью создаются потоки и производится их разбор на пакеты.

%package devel
Summary: Development files for libogg
Group: Development/C
PreReq: %name = %version-%release

%description devel
This package contains the header files and documentation needed
to develop applications with libogg.

%description devel -l ru_RU.UTF-8
В этом пакете находятся файлы, необходимые для использования libogg
в разработке приложений.

%package devel-static
Summary: Static libraries for libogg
Group: Development/C
PreReq: %name-devel = %version-%release

%description devel-static
This package contains development libraries required for packaging
statically linked libogg-based software.

%description devel-static -l ru_RU.UTF-8
В этом пакете находятся статические библиотеки, необходимые
для использования libogg в разработке статических приложений.

%prep
%setup
sed -i 's,-O20,,g' configure*

%build
%autoreconf
%configure %{subst_enable static}
%make_build OGG_CFLAGS="%optflags"

%install
%makeinstall_std
%define docdir %_docdir/%name
install -pm644 AUTHORS CHANGES COPYING %buildroot%docdir/

%files
%_libdir/*.so.*
%dir %docdir/
%docdir/[AC]*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_aclocaldir/*
%docdir/
%exclude %docdir/[AC]*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Aug 31 2019 Dmitry V. Levin <ldv@altlinux.org> 1.3.4-alt1
- 1.3.3 -> 1.3.4.

* Mon Dec 17 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt1
- 1.3.2 -> 1.3.3.

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 1.3.2-alt2
- piggyback our CFLAGS instead as these don't get respected by libogg
  (thx ldv@ yet again)

* Fri Jan 27 2017 Michael Shigorin <mike@altlinux.org> 1.3.2-alt1.1
- E2K: "-O20" is a bit too much!
  + see also https://github.com/kripken/emscripten/issues/264
- autoreconf

* Sat Nov 15 2014 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2.

* Mon Jul 23 2012 L.A. Kostis <lakostis@altlinux.ru> 1.3.0-alt1
- Updated to 1.3.0.

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Tue Aug 18 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- Updated to 1.1.4.

* Thu Nov 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.1.3-alt1
- new version 1.1.3

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.2-alt1.1
- Rebuilt for new pkg-config dependencies.

* Sat Sep 25 2004 Andrey Astafiev <andrei@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Mon Sep 13 2004 Andrey Astafiev <andrei@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Sat Nov 22 2003 Andrey Astafiev <andrei@altlinux.ru> 1.1-alt1
- 1.1

* Thu Oct 31 2002 Rider <rider@altlinux.ru> 1.0release-alt2
- rebuild with gcc 3.2

* Tue Jul 30 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0release-alt1
- 1.0
- some temprorary changes to avoid using Serial.

* Thu Jan 03 2002 Andrey Astafiev <andrei@altlinux.ru> 1.0rc3-alt1
- 1.0rc3

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0-alt2
- Fixed license tag.
- Relocated documentation, a bit more specfile cleanup.

* Thu Sep 27 2001 Andrey Astafiev <andrei@altlinux.ru> 1.0rc2-alt1
- spec cleanup.

* Sat Sep 22 2001 Michael Shigorin <mike@lic145.kiev.ua>
- built for ALTLinux.

* Sat Sep 02 2000 Jack Moffitt <jack@icecast.org>
- initial spec file created.
