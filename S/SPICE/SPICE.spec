
%def_disable celt051
%def_enable opus
%def_enable lz4
%def_enable gstreamer
%def_disable manual

Name: SPICE
Version: 0.14.2
Release: alt1
Summary: Implements the SPICE protocol
Group: Graphical desktop/Other
License: LGPLv2+
Url: http://www.spice-space.org/

# VCS: https://gitlab.freedesktop.org/spice/spice.git
Source: %name-%version.tar
Source2: spice-common.tar
Source3: spice-common-recorder.tar
Patch1: fix-alt.patch

BuildRequires: gcc-c++
BuildRequires(pre): meson >= 0.48
BuildRequires: libjpeg-devel libpixman-devel >= 0.17.7 zlib-devel
BuildRequires: libssl-devel >= 1.1.0 libsasl2-devel openssl
BuildRequires: libcacard-devel >= 2.5.1
BuildRequires: python3-module-six python3-module-pyparsing
BuildRequires: glib2-devel >= 2.38 libgio-devel >= 2.38
BuildRequires: libgdk-pixbuf-devel >= 2.26
BuildRequires: spice-protocol >= 0.14.0
%{?_enable_manual:BuildRequires: asciidoc asciidoc-a2x}
%{?_enable_celt051:BuildRequires: libcelt051-devel >= 0.5.1.1}
%{?_enable_opus:BuildRequires: libopus-devel >= 0.9.14}
%{?_enable_lz4:BuildRequires: liblz4-devel}
%{?_enable_gstreamer:BuildRequires: gstreamer1.0-devel gst-plugins1.0-devel gst-plugins1.0-gir-devel liborc-devel}

%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

%package -n libspice-server
Summary: Implements the server side of the SPICE protocol
Group: System/Libraries

%description -n libspice-server
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the run-time libraries for any application that wishes
to be a SPICE server.

%package -n libspice-server-devel
Summary: Header files, libraries and development documentation for spice-server
Group: Development/C
Requires: libspice-server = %version-%release

%description -n libspice-server-devel
This package contains the header files, static libraries and development
documentation for spice-server. If you like to develop programs
using spice-server, you will need to install spice-server-devel.

%prep
%setup
mkdir -p subprojects
tar -xf %SOURCE2 -C subprojects/spice-common
tar -xf %SOURCE3 -C subprojects/spice-common/common/recorder
# version in .tarball-version file
echo "%version" > .tarball-version
%patch1 -p1

%build
rm -f GITVERSION
%meson
%meson_build \
    %{?_disable_gstreamer:-Dgstreamer=no}

%install
%meson_install
rm -f %buildroot%_libdir/libspice-server.a
rm -f %buildroot%_libdir/libspice-server.la

%files -n libspice-server
%doc COPYING README NEWS
%_libdir/libspice-server.so.*

%files -n libspice-server-devel
%_includedir/spice-server
%_libdir/libspice-server.so
%_pkgconfigdir/spice-server.pc

%changelog
* Fri May 31 2019 Alexey Shabalin <shaba@altlinux.org> 0.14.2-alt1
- 0.14.2 (fixes: CVE-2019-3813)
- build with gstreamer support

* Thu Sep 06 2018 Pavel Skrylev <majioa@altlinux.org> 0.14.1-alt2
- Moved forward to opensll 1.1.

* Fri Aug 31 2018 Alexey Shabalin <shaba@altlinux.org> 0.14.1-alt1
- 0.14.1 (fixes: CVE-2018-10873)

* Fri Nov 03 2017 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Mon Sep 04 2017 Alexey Shabalin <shaba@altlinux.ru> 0.13.90-alt1
- 0.13.90

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 0.13.3-alt2
- Fix detect new version of lz4

* Fri Dec 23 2016 Alexey Shabalin <shaba@altlinux.ru> 0.13.3-alt1
- 0.13.3

* Tue May 17 2016 Alexey Shabalin <shaba@altlinux.ru> 0.12.7-alt1
- 0.12.7

* Mon Oct 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.12.6-alt1
- 0.12.6

* Tue Jan 27 2015 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt4
- upstream git snapshot 3c6b4e415fa1e2ce212d09ba15c90cd58b4ec4b4

* Thu Dec 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt3
- upstream git snapshot 69f3f86ff79360d208f6f31e4914fbe3f0a14f61

* Thu Sep 11 2014 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt2
- upstream git snapshot 5eb9967dbc508d99a4b2bec49a51f3510c91e022

* Wed May 21 2014 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt1
- 0.12.5

* Fri Apr 18 2014 Alexey Shabalin <shaba@altlinux.ru> 0.12.4-alt2.gite3da0c4
- upstream git snapshot e3da0c4f01f16e504d48793bb9a5b37b65fa345e
- switch from celt051 to opus
- disable build spice-client

* Wed Nov 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.4-alt1.2
- Fixed build

* Tue Sep 17 2013 Sergey Y. Afonin <asy@altlinux.ru> 0.12.4-alt1.1
- NMU: rebuilt with cyrus-sasl 2.1.26

* Mon Jul 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.4-alt1
- 0.12.4

* Fri Jul 05 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.3-alt2
- upstream snapshot b83c0fbf7f2eea9c66933bf51554778872f98174

* Mon May 20 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.3-alt1
- 0.12.3

* Mon Feb 18 2013 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt1
- upstream snapshot

* Thu Feb 14 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.12.0-alt2
- Build for armh too

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 0.11.3-alt1
- 0.11.3

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.1
- Fixed build

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Thu Nov 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0
- build for 32-bit too

* Thu Sep 01 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt2
- add empty packages libspice-server and libspice-server-devel for fix autorebuild qemu on i586

* Mon Aug 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt2
- rebuild with cegui06-devel

* Fri May 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1 (thx to prividen@)

* Wed Mar 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Tue Jan 25 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Wed Jan 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt2
- don't build server for i586

* Wed Jan 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1
- 0.7.1
- enable smartcard support
- build server for i586 too

* Sat Nov 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
