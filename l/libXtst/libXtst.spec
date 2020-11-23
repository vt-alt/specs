Name: libXtst
Version: 1.2.3
Release: alt1
Summary: The Xtst Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel libXext-devel libXi-devel xmlto xorg-recordproto-devel xmlto xorg-sgml-doctools xorg-util-macros

%description
The Xtst Library

%package devel
Summary: The Xtst Library and Header Files
Group: Development/C
Requires: %name = %version-%release

%description devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

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

%files
%_libdir/*.so.*

%files devel
%dir %_docdir/%name
%_docdir/%name/*.html
%_includedir/X11
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*.3*

%changelog
* Tue Nov 17 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.2.3-alt1
- 1.2.3
- securuty fixes: CVE-2016-7951, CVE-2016-7952

* Fri May 31 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Mar 03 2011 Alexey Tourbin <at@altlinux.ru> 1.2.0-alt3
- rebuilt for debuginfo

* Tue Nov 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2
- devel: fixed pkg-config requires

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Apr 11 2010 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt2
- Fixed package dependencies (closes: #23318).

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Sat Aug 18 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Jun 07 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.3-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt0.1
- initial build

