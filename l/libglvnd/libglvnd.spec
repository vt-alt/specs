Name: libglvnd
Version: 1.3.1
Release: alt0.p9
Epoch: 7
Group: System/Libraries
Summary: The GL Vendor-Neutral Dispatch library
Url: https://gitlab.freedesktop.org/glvnd/libglvnd
License: MIT

Provides: libGLdispatch = %epoch:%version-%release
Obsoletes: libGLdispatch < %epoch:%version-%release

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: libXext-devel python-modules-compiler python-modules-distutils python-modules-xml xorg-glproto-devel

%description
libglvnd is an implementation of the vendor-neutral dispatch layer for
arbitrating OpenGL API calls between multiple vendors on a per-screen basis

%package devel
Summary: Development files for %name
Group: Development/C
Conflicts: libGL-devel < 19.2.2

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name

%package -n libOpenGL
Summary: OpenGL support for libglvnd
Group: System/Libraries

%description -n libOpenGL
libOpenGL is the common dispatch interface for the workstation OpenGL API

%package -n libGLES
Summary: GLES support for libglvnd
Group: System/Libraries

%description -n libGLES
libGLESv2 are the common dispatch interface for the GLES API

%package -n libGLES-devel
Summary: GLES development package
Group: Development/C

%description -n libGLES-devel
GLES development package

%package -n libEGL
Summary: EGL support for libglvnd
Group: System/Libraries
Requires: libEGL-mesa

%description -n libEGL
libEGL are the common dispatch interface for the EGL API

%package -n libGLX
Summary: GLX support for libglvnd
Group: System/Libraries
Requires: libGLX-mesa

%description -n libGLX
libGLX are the common dispatch interface for the GLX API

%package -n libGL
Summary: GL support for libglvnd
Group: System/Libraries

%description -n libGL
libGL are the common dispatch interface for the GLX API

%set_verify_elf_method textrel=relaxed

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-gles1
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot{%_sysconfdir,%_datadir}/glvnd/egl_vendor.d
mkdir -p %buildroot{%_sysconfdir,%_datadir}/egl/egl_external_platform.d

rm -f %buildroot%_libdir/libGLESv1*
rm -f %buildroot%_pkgconfigdir/glesv1*.pc

%files
%doc README.md
%dir %_sysconfdir/glvnd
%dir %_datadir/glvnd
%_libdir/libGLdispatch.so.*

%files -n libOpenGL
%_libdir/libOpenGL.so.*

%files -n libGLES
%_libdir/libGLES*.so.*

%files -n libGLX
%_libdir/libGLX.so.*

%files -n libGL
%_libdir/libGL.so.*

%files -n libEGL
%dir %_sysconfdir/glvnd/egl_vendor.d
%dir %_datadir/glvnd/egl_vendor.d
%dir %_sysconfdir/egl
%dir %_sysconfdir/egl/egl_external_platform.d
%dir %_datadir/egl
%dir %_datadir/egl/egl_external_platform.d
%_libdir/libEGL.so.*

%files devel
%_includedir/EGL
%_includedir/GL
%_includedir/KHR
%_includedir/glvnd
%_libdir/lib*.so
%exclude %_libdir/libGLES*.so
%_pkgconfigdir/*.pc
%exclude %_pkgconfigdir/gles*.pc

%files -n libGLES-devel
%_includedir/GLES*
%_libdir/libGLES*.so
%_pkgconfigdir/gles*.pc

%changelog
* Wed May 20 2020 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.1-alt0.p9
- backport to p9 branch

* Tue Mar 10 2020 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.1-alt1
- 1.3.1

* Wed Feb 19 2020 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.0-alt1
- 1.3.0

* Tue Nov 26 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.2.0-alt4
- fixed conflicts between libglvnd-devel and libGLES-devel

* Mon Nov 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.2.0-alt3
- git snapshot master.9ba775e

* Wed Oct 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.2.0-alt2
- update GL/gl.h to match Mesa

* Thu Oct 10 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.2.0-alt1
- 1.2.0

* Thu Mar 14 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.1.1-alt1
- 1.1.1

* Thu Nov 01 2018 Valery Inozemtsev <shrek@altlinux.ru> 7:1.1.0-alt3
- git snapshot master.012fe39

* Thu Oct 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 7:1.1.0-alt2
- 1.1.0
