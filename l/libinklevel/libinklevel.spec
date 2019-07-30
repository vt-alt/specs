Name: libinklevel
Version: 0.8.0
Release: alt2

Summary: Library for retrieving the ink level of a printer.
License: GPL
Group: System/Libraries

Url: http://libinklevel.sourceforge.net
Source0: %url/%name-%version.tar.gz
Source1: %name-index.html
Source2: %name.watch
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildPreReq: libieee1284-devel

%package devel
Summary: Headers for libinklevel
Group: Development/C
Requires: %name = %version-%release

%description
Libinklevel is a linux library for retrieving the ink level of a printer
attached via the parallel port or USB.

%description devel
Headers for building software that uses libinklevel

%prep
%setup
cp -a %SOURCE1 index.html
cp -at . -- /usr/share/gnu-config/config.sub /usr/share/gnu-config/config.guess

%build
%configure
%make_build OPTFLAGS="%optflags"

%install
%makeinstall_std
ln -sf /usr/share/license/GPL-2 COPYING

%files
%_libdir/*.so.*
%doc index.html
%doc --no-dereference COPYING

%files devel
%_libdir/*.so
%_includedir/*.h

%changelog
* Thu May 23 2019 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- E2K: fix build by updating config.*
- spec fixup/cleanup

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1.qa2
- NMU: fixed bugs in watch file

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Sep 30 2010 Ilya Mashkin <oddity@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libinklevel
  * postun_ldconfig for libinklevel

* Sun Jan 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.7.2-alt1
- new version
- return from orphaned
- add watch file

* Sun Oct 10 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.3-alt2
- set OPTFLAGS when building
- update index.html

* Fri Sep 17 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.3-alt1
- new version
- update Url (moved to SF)
- remove supported_printers.txt, add index.html from project page

* Sat Jan 10 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.2-alt1
- new version

* Sat Dec 06 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.1-alt1
- new version

* Thu Dec 04 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.6-alt1
- new version
- supported printers list added (from project homepage)

* Fri Oct 10 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.5-alt1
- postin fix
- built for Sisyphus
