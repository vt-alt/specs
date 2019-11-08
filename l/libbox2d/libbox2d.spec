Name:		libbox2d
Version:	2.1.2
Release:	alt2.1
Summary:	A 2D physics engine for games
Group:		System/Libraries
License:	BSD-like
URL:		http://www.box2d.org
%define	FName Box2D
%define VName %{FName}_v%version
Source:		http://box2d.googlecode.com/files/%VName.zip
Patch:		Box2D_CMake.patch
Patch1:		%name-add-glut.patch

# Automatically added by buildreq on Tue Jul 06 2010
BuildRequires: cmake gcc-c++ libGLUT-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXext-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libglui-devel libxkbfile-devel unzip

%description
Box2D is a 2D rigid body simulation library for games. Programmers can use it
in their games to make objects move in believable ways and make the game world
more interactive. From the game's point of view a physics engine is just
a system for procedural animation.

Box2D is written in portable C++. Most of the types defined in the engine begin
with the b2 prefix. Hopefully this is sufficient to avoid name clashing with
your game engine.

%package devel
Summary:	Development files for %name
Group:		Development/C++

%description devel
Development files for %name, %summary

%prep
%setup -n %VName
%patch -p1
%patch1 -p2
# XXX incorrect dates in zipfile
find . -type f -exec touch {} \;
rm -r Box2D/glui Box2D/freeglut
ln -s /usr/include Box2D/glui
ln -s /usr/include Box2D/freeglut

%build
cd %FName/Build
      cmake .. \
	  -DCMAKE_SKIP_RPATH:BOOL=yes \
	  -DCMAKE_BUILD_TYPE=MinSizeRel \
	  -DCMAKE_C_FLAGS:STRING='-pipe -Wall -O2' \
	  -DCMAKE_CXX_FLAGS:STRING='-pipe -Wall -O2' \
	  -DCMAKE_INSTALL_PREFIX=/usr \
	  -DLIB_DESTINATION=%_lib

%make_build Box2D_shared
%make_build

%install
cd %FName/Build
%makeinstall DESTDIR=%buildroot

%files
%doc %FName/License.txt %FName/Readme.txt
%_libdir/*.so.*

%files devel
%doc %FName/Documentation
%exclude %_libdir/*.so.*
%_libdir/lib*.so
%_includedir/*


%changelog
* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt2.1
- NMU: fix build

* Tue Apr 26 2011 Fr. Br. George <george@altlinux.ru> 2.1.2-alt2
- Fix debuginfo build

* Mon Jul 05 2010 Fr. Br. George <george@altlinux.ru> 2.1.2-alt1
- Initial build for ALT

