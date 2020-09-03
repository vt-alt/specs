%def_with doxygen
%def_without check
%def_disable static

%define major 1.13

Name: sofia-sip
Version: 1.13.1
Release: alt0.d10a3d268c

Summary: Sofia SIP User-Agent library 
License: LGPLv2.1
Group: System/Libraries
Url: http://sofia-sip.sourceforge.net/

Source: %name-%version-%release.tar

BuildRequires: glib2-devel libssl-devel %{?_with_doxygen: doxygen graphviz fonts-ttf-liberation} %{?_with_check: libcheck-devel}

%description
Sofia SIP is a RFC-3261-compliant library for SIP user agents and other
network elements.

%package -n libsofia-sip
Summary: Sofia SIP User-Agent library
Group: System/Libraries
Provides: sofia-sip
Obsoletes: sofia-sip

%package -n libsofia-sip-devel
Summary: Sofia-SIP Development Package
Group: Development/C
Requires: libsofia-sip = %version-%release

%package -n libsofia-sip-glib
Summary: GLIB bindings for Sofia-SIP 
Group: System/Libraries
Requires: libsofia-sip = %version-%release
Provides: sofia-sip-glib
Obsoletes: sofia-sip-glib

%package -n libsofia-sip-glib-devel
Summary: GLIB bindings for Sofia SIP development files
Group: Development/C
Requires: libsofia-sip-glib = %version-%release
Requires: libsofia-sip-devel = %version-%release

%package docs
Summary: Sofia-SIP Development Manual Package
Group: Documentation
BuildArch: noarch

%package utils
Summary: Sofia-SIP Command Line Utilities
Group: Networking/Other
Requires: libsofia-sip = %version-%release

%description -n libsofia-sip
Sofia SIP is a RFC-3261-compliant library for SIP user agents and other
network elements.

%description -n libsofia-sip-devel
Development package for Sofia SIP UA library. This package includes 
static libraries and include files.

%description -n libsofia-sip-glib
GLib interface to Sofia SIP User Agent library.

%description -n libsofia-sip-glib-devel
Development package for Sofia SIP UA Glib library. This package includes
static libraries and include files for developing glib programs using Sofia
SIP.

%description docs
HTML reference documentation for Sofia SIP UA library.

%description utils
Command line utilities for Sofia SIP UA library.

%prep
%setup

%build
%autoreconf
%configure --disable-sctp %{subst_enable static}
make all %{?_with_doxygen: doxygen} %{?_with_check: check}
%if_with doxygen
pushd utils
doxygen
popd
%endif

%install
%make_install DESTDIR=%buildroot install

%if_with doxygen
cp -pr libsofia-sip-ua/docs/html manual
mkdir -p %buildroot/%_man1dir
install -pm0644 man/man1/* %buildroot/%_man1dir/
%endif

%files -n libsofia-sip
%doc AUTHORS COPYRIGHTS README* RELEASE TODO
%_libdir/libsofia-sip-ua.so.*

%files -n libsofia-sip-glib
%_libdir/libsofia-sip-ua-glib.so.*

%files -n libsofia-sip-devel
%_libdir/libsofia-sip-ua.so

%_includedir/sofia-sip-%major
%exclude %_includedir/sofia-sip-%major/sofia-sip/su_glib.h
%exclude %_includedir/sofia-sip-%major/sofia-sip/su_source.h

%_datadir/sofia-sip

%_pkgconfigdir/sofia-sip-ua.pc

%files -n libsofia-sip-glib-devel
%_libdir/libsofia-sip-ua-glib.so

%_includedir/sofia-sip-%major/sofia-sip/su_glib.h
%_includedir/sofia-sip-%major/sofia-sip/su_source.h

%_pkgconfigdir/sofia-sip-ua-glib.pc

%if_with doxygen
%files docs
%doc manual
%endif

%files utils
%_bindir/localinfo
%_bindir/addrinfo
%_bindir/sip-options
%_bindir/sip-date
%_bindir/sip-dig
%_bindir/stunc
%_man1dir/*

%changelog
* Mon Aug 31 2020 Anton Farygin <rider@altlinux.ru> 1.13.1-alt0.d10a3d268c
- 1.13.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.12.11-alt2.1.qa1
- NMU: applied repocop patch

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.12.11-alt2.1
- NMU: Rebuild with new openssl 1.1.0.

* Sun Aug 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.11-alt2
- added few bugfixes originated from freeswitch

* Wed Aug 10 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.11-alt1
- 1.12.11 released

* Wed Nov 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.10-alt4
- updated to upstream git.a948bebd

* Sun Jul 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.10-alt3
- darcs shapshot @20090708

* Fri Jan 16 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.10-alt2
- few headers added to devel subpackage

* Tue Jan 13 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.10-alt1
- 1.12.10 released

* Tue Jan 13 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.9-alt1
- 1.12.9 released

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.12.8-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Mar 09 2008 Igor Zubkov <icesik@altlinux.org> 1.12.8-alt1
- 1.12.7 -> 1.12.8

* Wed Dec 05 2007 Igor Zubkov <icesik@altlinux.org> 1.12.7-alt1
- build for Sisyphus

* Thu Dec  7 2006 Pekka Pessi <ppessi at gmail.com> - 1.12.4-1
- Silenced all rpmlint warnings on FC6.

* Wed Dec  6 2006 Pekka Pessi <ppessi at gmail.com> - 1.12.4-0
- Fixing optional values on Fedora. rpmlinted. No doxygen docs.

* Tue Dec  5 2006 Pekka Pessi <ppessi at gmail.com> - 1.12.4
- Bumped version. rpmlinted.

* Tue Dec  5 2006 Kai Vehmanen <first.lastname at nokia.com>
- The 'nua-glib' module, and the related dependency to gobject, has been 
  removed from the sofia-sip package

* Fri Oct  6 2006 Pekka Pessi <ppessi at gmail.com> - 1.12.3
- Autodetecting openssl, glib and gobject support with pkg-config
  (use --with openssl --with glib and --with gobject to force them)

* Mon Sep 18 2006 Kai Vehmanen <first.lastname at nokia.com>
- Removed *.m4 files from the distribution package.

* Fri Aug 11 2006 Kai Vehmanen <first.lastname at nokia.com>
- Modified the install location of the awk scripts.

* Thu Jun 15 2006 Kai Vehmanen <first.lastname at nokia.com>
- Added library soname to sofia-sip-glib package name.
- Modified dependencies - the glib subpackages do not depend
  on a specific version of sofia-sip anymore.

* Wed Mar 08 2006 Kai Vehmanen <first.lastname at nokia.com>
- Added libsofia-sip-ua-glib to the package.

* Tue Nov 15 2005 Kai Vehmanen <first.lastname at nokia.com>
- Removed the --includedir parameter. The public headers are
  now installed under includedir/sofia-sip-MAJOR.MINOR/

* Thu Oct 20 2005 Pekka Pessi <first.lastname at nokia.com>
- Using %%{_lib} instead of lib

* Thu Oct  6 2005 Pekka Pessi <first.lastname at nokia.com>
- Added sub-package utils

* Thu Oct  6 2005 Pekka Pessi <first.lastname at nokia.com> - 1.11.0
- Added %%{?dist} to release

* Sat Jul 23 2005 Pekka Pessi <first.lastname at nokia.com> - 1.10.1
- Initial build.
