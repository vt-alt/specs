Name: libXvMC
Version: 1.0.12
Release: alt1

Summary: The XvMC Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel libXv-devel xorg-util-macros xorg-sgml-doctools xmlto

%description
The XvMC Library

%package devel
Summary: The XvMC Library and Header Files
Group: Development/C

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/X11
touch %buildroot%_sysconfdir/X11/XvMCConfig

%files
%ghost %_sysconfdir/X11/XvMCConfig
%_libdir/*.so.*

%files devel
%_includedir/X11/extensions
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Mar 12 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Mon Mar 18 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Tue May 29 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Sat Jun 15 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt2
- devel: fixed pkg-config requires

* Sun Aug 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Wed Oct 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt3
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Jun 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt2
- added %_sysconfdir/X11/XvMCConfig

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Thu Sep 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

