%define _unpackaged_files_terminate_build 1

Name: libebml
Version: 1.3.10
Release: alt1

Summary: Extensible Binary Meta Language access library
License: LGPL-2.1-or-later and BSD
Group: System/Libraries

Url: http://www.matroska.org
# https://github.com/Matroska-Org/libebml.git
Source: %name-%version.tar

BuildRequires: gcc-c++ cmake

%description
A library for reading and writing files with the Extensible Binary
Meta Language, a binary pendant to XML.

%package devel
Summary: Development files for libebml
Group: Development/C++
Requires: %name = %EVR

%description devel
Files needed to build programs using libebml

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS=YES
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE*
%doc README* ChangeLog* CODE_OF_CONDUCT*
%_libdir/*.so.*

%files devel
%_includedir/ebml
%_libdir/*.so
%_libdir/cmake/*
%_pkgconfigdir/*.pc

%changelog
* Tue Feb 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.10-alt1
- Updated to upstream version 1.3.10.

* Thu Jul 25 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.9-alt1
- Updated to upstream version 1.3.9.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.7-alt2
- NMU: remove rpm-build-ubt from BR:

* Tue Apr 09 2019 Michael Shigorin <mike@altlinux.org> 1.3.7-alt1
- 1.3.7
- drop e2k workarounds for good

* Wed Jun 27 2018 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt2
- Rebuild for e2k.

* Tue May 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.6-alt1
- Updated to upstream version 1.3.6.

* Sun Apr 01 2018 Anton Farygin <rider@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Fri Sep 02 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.4-alt1
- 1.3.4 released

* Wed Jul 15 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt2
- rebuilt with gcc5

* Fri Jan 16 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.1-alt1
- 1.3.1 released

* Sun Sep 14 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Mon Dec 10 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt0.1
- 1.3.0 prerelease

* Thu Oct 13 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.2-alt1
- 1.2.2 released

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.1
- Rebuilt for soname set-versions

* Wed Aug 18 2010 Afanasov Dmitry <ender@altlinux.org> 1.0.0-alt1
- 1.0.0 release.

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libebml
  * postun_ldconfig for libebml

* Sun Apr 06 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.7.8-alt1
- 0.7.8 release.

* Sun May 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.7.7-alt1
- 0.7.7 release.

* Wed Nov 30 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.7.6-alt1
- 0.7.6 release.
- Fixed some errors in specfile.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.7.0-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Apr 27 2004 Alexey Morozov <morozov@altlinux.org> 0.7.0-alt1
- Initial build.
- Package autotoolized
