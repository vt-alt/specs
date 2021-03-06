Name: tcl-tdom
Version: 0.9.1
Release: alt2

Summary: A XML/DOM/XPath/XSLT implementation for Tcl
License: MPL-1.1
Group: Development/Tcl
Url: http://www.tdom.org

# repacked http://tdom.org/downloads/tdom-%version-src.tgz
Source: tdom-%version.tar
Patch2: 0002-ALT-install-test-targets-fixed.patch
Patch3: 0003-ALT-TEA.patch

BuildRequires: tcl-devel libexpat-devel libgumbo-devel

%description
This package contains a freely distributable extension to Tcl
implementing memory channels, i.e. channels storing the data
placed into them in memory, not on disk.

%prep
%setup -n tdom-%version
%patch2 -p2
%patch3 -p2
# remove needless stuff
rm -r macosx/ win/

%build
%autoreconf
%configure \
	--disable-rpath \
	--enable-html5 \
	--enable-threads \
	--with-expat=%_prefix \
	#
%make_build all

%install
%makeinstall_std

%check
make test

%files
%_tcllibdir/libtdom%version.so
%_tcllibdir/tdom%version
%_tcldatadir/tdom%version
%_mandir/mann/*

%changelog
* Tue Sep 24 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1-alt2
- Fixed build with external expat.
- Built with HTLM5 parser support.
- Explicitly enabled threads.
- Fixed license field according SPDX.

* Mon Sep 23 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.9.1-alt1
- 0.9.1.
- Moved pkgIndex.tcl to arch-depended location cause tdom is arch-depended
  extension.
- Dropped devel subpackage.

* Tue Jul 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.8.3-alt0.2
- Fixed FTBFS
- Fixed:
  + XPath element-available function
  + pkgIndex.tcl missing whitespace
  + generic/domxslt.c: wrong size on memcpy on 64 bit
- Built devel subpackage

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8.3-alt0.1.qa1
- NMU: rebuilt for debuginfo.

* Sat Feb 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.3-alt0.1
- first build for %distribution
