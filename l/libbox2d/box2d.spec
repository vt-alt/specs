Name:		libbox2d
Version:	2.4.1
Release:	alt1
Summary:	A 2D physics engine for games
Group:		System/Libraries
License:	MIT
URL:		http://www.box2d.org
Source:		box2d-%version.tar.gz

# Automatically added by buildreq on Sat Feb 13 2021
# optimized out: cmake-modules fontconfig-devel glibc-kernheaders-generic glibc-kernheaders-x86 libICE-devel libSM-devel libX11-devel libXau-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libfreetype-devel libsasl2-3 libstdc++-devel libxcb-devel pkg-config python2-base sh4 xorg-proto-devel
BuildRequires: cmake doxygen gcc-c++ libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel libxkbfile-devel

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
%setup -n box2d-%version

%build
%cmake -DBOX2D_BUILD_DOCS=ON -DBOX2D_INSTALL=ON -DBOX2D_BUILD_SHARED=ON -DBUILD_SHARED_LIBS:BOOL=ON 
%cmake_build

%install
%makeinstall_std -C BUILD

%files
%doc *.md
%_libdir/*.so.*

%files devel
%doc %_defaultdocdir/box2d
%_libdir/lib*.so
%_includedir/*
%_libdir/cmake/*

%changelog
* Sat Feb 13 2021 Fr. Br. George <george@altlinux.ru> 2.4.1-alt1
- Submajor version update
- Upstream switch to GH

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt2.1
- NMU: fix build

* Tue Apr 26 2011 Fr. Br. George <george@altlinux.ru> 2.1.2-alt2
- Fix debuginfo build

* Mon Jul 05 2010 Fr. Br. George <george@altlinux.ru> 2.1.2-alt1
- Initial build for ALT

