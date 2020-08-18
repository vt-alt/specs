%ifarch %ix86
%define platform x86-linux-gcc
%else
%ifarch arm
%define platform armv5te-linux-gcc
%else
%ifarch armh
%define platform armv7-linux-gcc
%else
%ifarch %e2k aarch64
%define platform generic-gnu
%else
%define platform %_arch-linux-gcc
%endif
%endif
%endif
%endif

Name: libvpx6
Version: 1.8.2
Release: alt1
Summary: VP8 video codec
Group: Video
License: BSD
Url: http://www.webmproject.org/

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: doxygen
%ifarch %ix86 x86_64
BuildRequires: yasm
%endif

%description
VP8 is an open video codec, originally developed by On2 and released
as open source by Google Inc. It is the successor of the VP3 codec,
on which the Theora codec was based

%package -n libvpx-devel
Summary: VP8 Libraries and Header Files
Group: Development/C
Requires: %name = %EVR

%description -n libvpx-devel
%name-devel contains the libraries and header files needed to
develop programs which make use of %name

%package -n libvpx-utils
Summary: VP8 utilities and tools
Group: Video
Requires: %name = %EVR

%description -n libvpx-utils
A selection of utilities and tools for VP8, including a sample encoder
and decoder.

%prep
%setup
%patch -p1
%ifarch armh
sed -i -e 's,softfp,hard,' build/make/configure.sh
%endif

%build
%ifarch %ix86 x86_64 %arm
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%endif
./configure \
	--prefix=%prefix \
	--libdir=%_libdir \
	--enable-pic \
	--target=%platform \
	--enable-shared \
	%ifnarch x86_64
	--disable-avx \
	--disable-avx2 \
	%endif
	--disable-install-srcs \
	--enable-vp9-decoder \
	--enable-vp9-encoder \
	--enable-experimental \
	--enable-vp9-highbitdepth \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE PATENTS CHANGELOG
%_libdir/*.so.*

%files -n libvpx-devel
%_includedir/vpx
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n libvpx-utils
%_bindir/*

%changelog
* Mon Dec 23 2019 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.8.1-alt1
- 1.8.1
- enabled AVX/AVX2 on x86_64
- added libvpx-utils package with sample encoder/decoder

* Thu Feb 21 2019 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 1.6.1-alt2
- enabled spatial svc
- enabled vp9 encoder/decoder

* Tue Oct 03 2017 Anton Farygin <rider@altlinux.ru> 1.6.1-alt1
- new version, renamed to libvpx4

* Wed May 31 2017 Michael Shigorin <mike@altlinux.org> 1.5.0-alt2.1
- E2K: generic build
- minor spec cleanup

* Wed Mar 09 2016 Anton Farygin <rider@altlinux.ru> 1.5.0-alt2
- renamed to libvpx3

* Mon Jan 25 2016 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Mon Apr 06 2015 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Tue Dec 03 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Fri Mar 01 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt2
- fixed build on armh

* Fri Jan 11 2013 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat May 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Sat Jan 28 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Fri Aug 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7.1-alt1
- 0.9.7-p1

* Fri Aug 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Sat Mar 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Thu Oct 28 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Tue Sep 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Fri Jun 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sun Jun 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt2
- GIT snapshot 2010-06-03 (7aa97a35b515bfb7d7bbcdee4db376f815343e44)

* Thu May 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt1
- initial release

