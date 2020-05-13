%def_disable static
%define realname irrlicht
%define major 1
%define libname %{name}%{major}

Name: libirrlicht
Version: 1.8.4
Release: alt2

Summary: Fast Open-source 3D engine
License: BSD-style
Group: System/Libraries
Url: http://irrlicht.sourceforge.net/

Source: %realname-%version.tar

# TODO: remake for 1.8 and uncomment doc and examples
Patch0: irrlicht-1.7.1-alt-autotools.patch

# Patch1-4 from mageia irrlicht
Patch1:		irrlicht-1.8-library-makefile.patch
# corrected: see irrlicht-1.8-use-system-libs.patch.diff
Patch2:		irrlicht-1.8-use-system-libs.patch
Patch3:		irrlicht-1.8.1-mga-system-glext.patch
Patch4:		irrlicht-1.8.1-fdr-mesa10.patch

BuildRequires:  pkg-config unzip gcc-c++ zlib-devel
BuildRequires:	ImageMagick
BuildRequires:	zlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libGLU-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	libXext-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	libXft-devel
BuildRequires:	bzlib-devel
BuildRequires:	fontconfig-devel
BuildRequires:	libXcursor-devel


%description
The Irrlicht Engine is a cross-platform high performance realtime 3D
engine written in C++. It is a powerful high level API for creating
complete 3D and 2D applications like games or scientific visualizations.
It comes with an excellent documentation and integrates all the
state-of-the-art features for visual representation like dynamic
shadows, particle systems, character animation, indoor and outdoor
technology, and collision detection. All this is accessible through
a well designed C++ interface, which is extremely easy to use.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%package -n %{libname}
Summary:	Shared libraries for Irrlicht 3D engine
Group:		System/Libraries

Provides: liblibirrlicht1 = %EVR
Obsoletes: liblibirrlicht1 < %EVR
Conflicts: liblibirrlicht1 < %EVR
Provides: libirrlicht = %version
Provides: libirrlicht = %version-%release
Obsoletes: libirrlicht < 1.8
Conflicts: libirrlicht < 1.8

%description -n %{libname}
Shared libraries for Irrlicht 3D engine.

The Irrlicht Engine is a cross-platform high performance realtime 3D
engine written in C++. It is a powerful high level API for creating
complete 3D and 2D applications like games or scientific visualizations.
It comes with an excellent documentation and integrates all the
state-of-the-art features for visual representation like dynamic
shadows, particle systems, character animation, indoor and outdoor
technology, and collision detection. All this is accessible through
a well designed C++ interface, which is extremely easy to use.


%package examples
Summary: Examples for %name
Group: Development/C
Requires: %name = %version-%release

%description examples
Examples that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%prep
%setup -q -n %realname-%version
#patch0 -p2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# make readme.txt and changes.txt utf8 with LF line endings
sed -i 's/\r//' readme.txt changes.txt
iconv -o readme.txt.utf8 -f iso88591 -t utf8 readme.txt
mv readme.txt.utf8 readme.txt

# use system wide libs, see patch2
rm -rf source/Irrlicht/{jpeglib,zlib,libpng,bzip2}
# FIXME: Unbundle lzmadec if possible

# https://bugzilla.redhat.com/show_bug.cgi?id=1035757
sed -i -e '/_IRR_MATERIAL_MAX_TEXTURES_/s/4/8/' include/IrrCompileConfig.h

%build
#autoreconf -fisv
#configure %{subst_enable static}
#make_build
%make -C source/Irrlicht sharedlib NDEBUG=1

%install
#makeinstall
mkdir -p %{buildroot}%{_libdir}
make -C source/Irrlicht INSTALL_DIR=%{buildroot}%{_libdir} install
ln -s libIrrlicht.so.%{version} %{buildroot}%{_libdir}/libIrrlicht.so.%{major}

mkdir -p %{buildroot}%{_includedir}/%{realname}
cp -a include/*.h %{buildroot}%{_includedir}/%{realname}/

%files -n %{libname}
%_libdir/libIrrlicht.so.%{major}*

%files devel
%_libdir/*.so
%_includedir/irrlicht
#doc doc/html doc/index.html
%doc doc/upgrade-guide.txt
%doc readme.txt changes.txt

#%files examples
#%_bindir/*
#%_datadir/irrlicht

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Tue Jun 11 2019 Michael Shigorin <mike@altlinux.org> 1.8.4-alt2
- Added P: libirrlicht = %%version-%%release for -devel

* Tue Nov 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.4-alt1
- Updated to upstream version 1.8.4.

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1
- NMU update

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt2.1
- Fixed build with libpng15

* Sat Jan 22 2011 Damir Shayhutdinov <damir@altlinux.ru> 1.7.1-alt2
- Rebuilt with set-provides.

* Tue Mar 30 2010 Damir Shayhutdinov <damir@altlinux.ru> 1.7.1-alt1
- New version.

* Sat Nov 22 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.4.2-alt1
- New version.

* Fri Apr 13 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt4
- Moved docs to devel subpackage. Now libirrlicht is ready for biarch.

* Thu Apr 12 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt3
- Fix license tag (#11483).

* Thu Mar 22 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt2
- Packaged readme.txt and changes.txt.
- Added documentation to -devel package.

* Sat Mar 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt1
- New version. 

* Fri Mar 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.2.0-alt1
- Initial build for ALT Linux.
