%set_verify_elf_method unresolved=strict

Name: gnustep-OresmeKit
Version: 0.1
Release: alt5
Summary: Oresme is a plotting framework for GNUstep
License: GPLv2+
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/oresmekit/index.html
Packager: Andrey Cherepanov <cas@altlinux.org>

# http://svn.savannah.nongnu.org/svn/gap/trunk/libs/Oresme/OresmeKit/
Source: %name-%version.tar
Patch1: link-libs.patch

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: lib%name = %EVR
Requires: gnustep-back

%description
OresmeKit, a plotting and charting framework for Objective-C, GNUstep
(and Cocoa/Macintosh).

The kit offers custom Views that can be embedded in the application and
display data at need.

Why OresmeKit? In honour of Nicolas Oresme the antique philosopher who
thought about coordinates long before Cartesius. Because Cartesius was
too predictable as a name and too tied to X-Y plotting, while OresmeKit
shall support more chart types in the future.

%package -n lib%name
Summary: Shared libraries of OresmeKit
Group: System/Libraries

%description -n lib%name
OresmeKit, a plotting and charting framework for Objective-C, GNUstep
(and Cocoa/Macintosh).

This package contains shared libraries of OresmeKit.

%package -n lib%name-devel
Summary: Development files of OresmeKit
Group: Development/Objective-C
Provides: %name-devel = %EVR
Requires: %name = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
OresmeKit, a plotting and charting framework for Objective-C, GNUstep
(and Cocoa/Macintosh).

This package contains development files of OresmeKit.

%prep
%setup
%patch1 -p1

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	CONFIG_SYSTEM_LIBS='-lgnustep-gui -lgnustep-base '
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

pushd %buildroot%_libdir
for j in OresmeKit; do
	for i in lib$j.so*; do
		rm -f $i
		mv GNUstep/Frameworks/$j.framework/Versions/Current/$i ./
		for k in lib$j.so.*.*; do
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$i
			rm GNUstep/Frameworks/$j.framework/Versions/Current/$j
			ln -s %_libdir/$k GNUstep/Frameworks/$j.framework/Versions/Current/$j
		done
	done
done
popd

%files
%_libdir/GNUstep
%exclude %_libdir/GNUstep/Frameworks/OresmeKit.framework/Versions/0.1/Headers
%exclude %_libdir/GNUstep/Frameworks/OresmeKit.framework/Headers

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/GNUstep/Frameworks/OresmeKit.framework/Versions/0.1/Headers
%_libdir/GNUstep/Frameworks/OresmeKit.framework/Headers

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt5
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt4
- Build without libgnustep-objc2-devel.

* Tue Mar 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.svn20140221
- New snapshot

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.cvs20140127
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.cvs20140127
- Added Requires: gnustep-back

* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.cvs20140127
- Initial build for Sisyphus

