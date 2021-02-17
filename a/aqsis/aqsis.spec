Group: Video
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install /usr/bin/swig boost-devel boost-filesystem-devel boost-program_options-devel boost-wave-devel gcc-c++ ilmbase-devel libGLU-devel libglvnd-devel python-devel rpm-build-python swig
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# force out-of-tree build for spec compatibility with older releases
%undefine __cmake_in_source_build

Name:		aqsis
Version:	1.8.2
Release:	alt4_41
Summary:	Open source 3D rendering solution adhering to the RenderMan standard

License:	GPLv2+ and LGPLv2+
URL:		http://www.aqsis.org
Source0:	http://downloads.sourceforge.net/aqsis/aqsis-%{version}.tar.gz

# fix build against ilmbase-2.x, kudos to arch linux
Patch1: imfinputfile-forward-declaration.diff
# Work-around boost-1.59 having dropped
# dropped boost/serialization/pfto.hpp
# and BOOST_MAKE_PFTO_WRAPPER
Patch2: aqsis-1.8.2-boost-1.59.patch
# Fix code to be C++11 compatible
# https://sourceforge.net/p/aqsis/bugs/433/
Patch3: aqsis-1.8.2-gcc6.patch
Patch4: aqsis-1.8.2-shared_ptr.patch
Patch5: aqsis-gcc11.patch

BuildRequires:  desktop-file-utils

BuildRequires:  bison >= 1.35.0
BuildRequires:  boost-complete >= 1.34.0
BuildRequires:  ctest cmake
BuildRequires:  doxygen
BuildRequires:  flex >= 2.5.4
BuildRequires:  libfltk-devel >= 1.1.0, libfltk-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel libtiffxx-devel
BuildRequires:  libpng-devel
BuildRequires:  libxslt xsltproc
BuildRequires:  libqt4-declarative libqt4-devel libqt4-help qt4-designer qt4-doc-html qt5-declarative-devel qt5-designer qt5-tools
#BuildRequires:  tinyxml-devel
BuildRequires:  openexr-devel
BuildRequires:  python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
BuildRequires:  zlib-devel >= 1.1.4

Requires: libqt4-core libqt4-dbus libqt4-network libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-test libqt4-xml libqt4-xmlpatterns qt4-common qt5-dbus
Requires: aqsis-core = %{version}-%{release}
Requires: aqsis-data = %{version}-%{release}
Source44: import.info
# TODO: fix build on armh
ExcludeArch: armh

%description
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains graphical utilities and desktop integration.


%package core
Group: Video
Requires:	%{name}-libs = %{version}-%{release}
Summary:	Command-line tools for Aqsis Renderer

%description core
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains a command-line renderer, a shader compiler
for shaders written using the RenderMan shading language, a texture
pre-processor for optimizing textures and a RIB processor.


%package libs
Group: System/Libraries
Summary:        Library files for Aqsis Renderer

%description libs
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains the shared libraries for Aqsis Renderer.


%package data
Group: Video
#Requires:	%{name} = %{version}-%{release}
Summary:	Example content for Aqsis Renderer
BuildArch:      noarch
#AutoReq: yes,nopython
AutoReq: no

%description data
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains example content, including additional
scenes, procedurals and shaders.


%package devel
Group: Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	aqsis-core = %{version}-%{release}
Requires:	aqsis-libs = %{version}-%{release}
Requires:	aqsis-data = %{version}-%{release}
Summary:	Development files for Aqsis Renderer

%description devel
Aqsis is a cross-platform photo-realistic 3D rendering solution,
adhering to the RenderMan interface standard defined by Pixar
Animation Studios.

This package contains various developer libraries to enable
integration with third-party applications.


%prep
%setup -q

%patch1 -p1 -b imfinputfile-forward-declaration
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1


%build
## Do not Enable pdiff=yes Because it will conflict with Printdiff :
## /usr/bin/pdiff  from package	a2ps
%{fedora_v2_cmake} \
  -DSYSCONFDIR:STRING=%{_sysconfdir}/%{name} \
  -DAQSIS_MAIN_CONFIG_NAME=aqsisrc-%{_lib} \
  -DLIBDIR=%{_lib} \
  -DPLUGINDIR=%{_lib}/%{name} \
  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
  -DCMAKE_SKIP_RPATH:BOOL=ON \
  -DAQSIS_USE_RPATH:BOOL=OFF \
  -DAQSIS_BOOST_FILESYSTEM_LIBRARY_NAME=boost_filesystem-mt \
  -DAQSIS_BOOST_REGEX_LIBRARY_NAME=boost_regex-mt \
  -DAQSIS_BOOST_THREAD_LIBRARY_NAME=boost_thread-mt \
  -DAQSIS_BOOST_WAVE_LIBRARY_NAME=boost_wave-mt \
  -DAQSIS_ENABLE_THREADING:BOOL=ON \
  -DCMAKE_CXX_FLAGS="$CXXFLAGS -DBOOST_FILESYSTEM_VERSION=3 -pthread" \
  -DAQSIS_USE_EXTERNAL_TINYXML:BOOL=OFF

%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install

# Move aqsisrc
mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/aqsisrc \
  $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/aqsisrc-%{_lib}

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsis.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsl.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/aqsltell.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/eqsl.desktop

desktop-file-install --vendor "" --delete-original \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/piqsl.desktop




%files
%doc AUTHORS README
%doc --no-dereference COPYING
%{_bindir}/eqsl
%{_bindir}/piqsl
%{_bindir}/ptview
# Do not use the name pdiff for PerceptualDiff
# It is used by PrintDiff in a2ps
#_bindir/pdiff
%{_datadir}/applications/aqsis.desktop
%{_datadir}/applications/aqsl.desktop
%{_datadir}/applications/aqsltell.desktop
%{_datadir}/applications/eqsl.desktop
%{_datadir}/applications/piqsl.desktop
%{_datadir}/pixmaps/aqsis.png
%{_datadir}/icons/hicolor/192x192/mimetypes/aqsis-doc.png
%{_datadir}/mime/packages/aqsis.xml


%files core
%{_bindir}/aqsis
%{_bindir}/aqsl
%{_bindir}/aqsltell
%{_bindir}/miqser
%{_bindir}/teqser


%files libs
%dir %{_sysconfdir}/%{name}
## Do not use noreplace with aqsis release
## This may definitly change in future releases.
%config %{_sysconfdir}/%{name}/aqsisrc-%{_lib}
%{_libdir}/%{name}/
# Licensed under GPLv2+
%{_libdir}/libaqsis_*.so.*
# Licensed under LGPLv2+
#_libdir/libaqsis_ri2rib.so.*


%files devel
%{_includedir}/%{name}/
# Licensed under GPLv2+
%{_libdir}/libaqsis_*.so
# Licensed under LGPLv2+
#_libdir/libaqsis_ri2rib.so


%files data
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples/
%{_datadir}/%{name}/plugins/
%{_datadir}/%{name}/scripts/
%{_datadir}/%{name}/shaders/



%changelog
* Tue Jan 26 2021 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt4_41
- update to new release by fcimport

* Thu Sep 10 2020 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt4_39
- rebuild with new boost

* Mon Nov 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt4_29
- Rebuilt with boost-1.71.0.

* Mon Jun 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt3_29
- NMU: rebuilt with boost-1.67.0

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_29
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_28
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_26
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_25
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_23
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_22
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_20
- update to new release by fcimport

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.8.2-alt2_16.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_16
- update to new release by fcimport

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.8.2-alt2_13.1
- rebuild with boost 1.57.0

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_10
- update to new release by fcimport

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_9
- converted for ALT Linux by srpmconvert tools

* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2_6
- fixed build

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_5
- update to new release by fcimport

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_4
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_3
- fc update

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1_1.1
- Rebuilt with Boost 1.52.0

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1_1
- converted for ALT Linux by srpmconvert tools

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt3_3.1
- Rebuilt with libpng15

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt3_3
- rebuild with new boost

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_3
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_2
- update to new release by fcimport

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_1
- fixed build

* Thu May 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1
- new version

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1_15.1
- Rebuilt with Boost 1.49.0

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_15
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_14
- update to new release by fcimport

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1_13.1
- Rebuilt with Boost 1.48.0

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_13
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_12
- update to new release by fcimport

* Sat Jul 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_11
- initial release by fcimport

