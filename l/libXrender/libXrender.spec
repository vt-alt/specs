Name: libXrender
Version: 0.9.10
Release: alt1
Summary: X Render Library
License: MIT/X11
Group: System/Libraries
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libX11-devel xorg-renderproto-devel xmlto xorg-util-macros xorg-sgml-doctools

%description
X Render Library

%package devel
Summary: X Render Library and Header Files
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
%_docdir/%name
%_includedir/X11/extensions
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Tue Nov 17 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.9.10-alt1
- 0.9.10
- securuty fixes: CVE-2016-7949, CVE-2016-7950

* Sat Jun 15 2013 Valery Inozemtsev <shrek@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Thu Mar 08 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Tue Feb 08 2011 Alexey Tourbin <at@altlinux.ru> 0.9.6-alt3
- rebuilt for debuginfo

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt2
- rebuild

* Wed Jun 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Sat Oct 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.4-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Sep 06 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Sat Sep 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt2
- rebuild with renderproto-0.9.3

* Tue Aug 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Sat Oct 14 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Mon Apr 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0.2-alt5
- CVS snapshot 2006-04-02:
	Fix a potential NULL chase
	Verify that a malloc succeeds

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0.2-alt4
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0.2-alt3
- fixed requires for %name-devel

* Sun Jan 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0.2-alt2
- added MDK dmx patch

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0.2-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0.1-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt0.1
- initial build

