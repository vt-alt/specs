%def_enable drm
%def_enable glx
%def_enable egl
%def_enable x11

Name: libva
Version: 2.7.1
Release: alt1

Summary: Video Acceleration (VA) API for Linux
License: MIT
Group: System/Libraries
Url: https://github.com/01org/libva


Source: %name-%version.tar
Patch: %name-%version-alt.patch

%if_enabled drm
BuildRequires: libdrm-devel
%endif
%if_enabled glx
BuildRequires: libGL-devel
%endif
%if_enabled egl
BuildRequires: libEGL-devel
%endif
%if_enabled x11
BuildRequires: libXext-devel libXfixes-devel
%endif
BuildRequires: gcc-c++ libwayland-client-devel libwayland-server-devel

%description
Video Acceleration (VA) API for Linux - runtime
The libva library implements the Video Acceleration (VA) API for Linux.
The library loads a hardware dependendent driver.

Note also that VAAPI intel driver now resides in own package:
libva-driver-intel

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: glibc-kernheaders
Obsoletes: libva1-devel < %version-%release

%description devel
This package provides the development environment for libva

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	%{subst_enable drm} \
	%{subst_enable glx} \
	%{subst_enable egl} \
	%{subst_enable x11} \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu May 14 2020 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Wed Apr 08 2020 Anton Farygin <rider@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Tue Feb 18 2020 Anton Farygin <rider@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Mon Jan 13 2020 Anton Farygin <rider@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Fri Aug 16 2019 Anton Farygin <rider@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Mon Feb 18 2019 Anton Farygin <rider@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Mon Oct 08 2018 Anton Farygin <rider@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Sat Jul 21 2018 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.8.3-alt2%ubt
- bump release to jump over p8

* Thu Aug 03 2017 Michael Shigorin <mike@altlinux.org> 1.8.3-alt1.1%ubt
- BOOTSTRAP: introduce wayland knob (on by default)

* Thu Jul 06 2017 Anton Farygin <rider@altlinux.ru> 1.8.3-alt1%ubt
- 1.8.3
- dummy_drv_video.so removed by upstream

* Thu Jun 01 2017 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- new version 

* Wed May 24 2017 L.A. Kostis <lakostis@altlinux.ru> 1.7.3-alt2
- Re-enabled glx/egl back (transition to GLVND is over).

* Tue May 23 2017 L.A. Kostis <lakostis@altlinux.ru> 1.7.3-alt1
- 1.7.3.
- Added fix for libva in case of GLVND setup (taken from Fedora).
- Updated radeonsi patch.

* Fri Oct 28 2016 L.A. Kostis <lakostis@altlinux.ru> 1.7.2-alt1
- 1.7.2.

* Thu Jul 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- 1.7.1 released

* Sat Feb 06 2016 L.A. Kostis <lakostis@altlinux.ru> 1.6.3-alt0.2.git1f026
- Added patches:
  + va/va.c: use libva.conf when looking for driver name.
  + va/va.c: add 'gallium' to prefer_drivers_list.
  + va/drm: use gallium driver for radeonsi.

* Sat Feb 06 2016 L.A. Kostis <lakostis@altlinux.ru> 1.6.3-alt0.1.git1f026
- GIT 1f026 snapshot.
- Start providing %%_libdir/dri as nobody doing this.

* Tue Nov 18 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Sat Jun 28 2014 L.A. Kostis <lakostis@altlinux.ru> 1.3.1-alt1
- 1.3.1.

* Fri Jan 24 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Thu Jun 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Wed Dec 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.15-alt1
- 1.0.15

* Thu Jul 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.14-alt1
- 1.0.14

* Tue May 31 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.13-alt1
- 1.0.13

* Fri Apr 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Mon Mar 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.11-alt1
- 1.0.11

* Sat Feb 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Tue Jan 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt2
- Rebuilt for soname set-versions

* Wed Aug 25 2010 Konstantin Pavlov <thresh@altlinux.org> 1.0.4-alt1
- 1.0.4 release.

* Thu Mar 18 2010 Konstantin Pavlov <thresh@altlinux.org> 0.31.0-alt3
- 0.31.0-1+sds11 release.

* Wed Jan 27 2010 Konstantin Pavlov <thresh@altlinux.ru> 0.31.0-alt2
- 0.31.0-1+sds9 release.

* Tue Sep 15 2009 Konstantin Pavlov <thresh@altlinux.org> 0.31.0-alt1
- 0.31.0-1+sds3 release.

* Tue Jul 14 2009 Konstantin Pavlov <thresh@altlinux.org> 0.30.4-alt1
- 0.30.4-1+sds3 release.

* Mon Apr 20 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.2.9-alt2
- Fix not owned path.

* Mon Apr 20 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.2.9-alt1
- Initial build for ALT Linux.


