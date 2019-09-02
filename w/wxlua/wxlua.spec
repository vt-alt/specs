%define luaver 5.1
Name: wxlua
Version: 2.8.12.3
Release: alt7.git.e43a6d9
Summary: Lua IDE with a GUI debugger and binding generator
License: wxWidgets License
Group: Development/Other
Url: http://wxlua.sourceforge.net/

# https://github.com/pkulchenko/wxlua/tree/wxwidgets311
Source: %name-%version.tar

BuildRequires: lua%luaver lua%luaver-devel
#BuildRequires: doxygen graphviz
# Automatically added by buildreq on Thu Oct 05 2017 (-bi)
# optimized out: at-spi2-atk cmake-modules elfutils fontconfig glibc-kernheaders-x86 libX11-devel libat-spi2-core libcairo-gobject libgdk-pixbuf libgpg-error libgst-plugins1.0 libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server lua5.3 perl python-base python-module-mpl_toolkits python-modules xorg-xproto-devel
BuildRequires: cmake desktop-file-utils gcc-c++ glibc-kernheaders-generic libGL-devel libwxGTK3.1-devel libwxstedit-devel

%description
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

Additionally, wxLua can be used in your C++ programs to embed a Lua interpreter
with the wxWidgets API.

This package contains Integrated Development Environments (IDE, written in
wxLua) with a GUI debugger, a binding generator and wxWidgets bindings usable
as a module.

%package -n lib%name
Group: System/Libraries
Summary: set of Lua bindings to the C++ wxWidgets cross-platform GUI library

%description -n lib%name
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files of lib%name
Requires: lib%name = %version-%release

%description -n lib%name-devel
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

This package contains files required for compiling and linking
applications with lib%name.

%if_enabled static
%package -n lib%name-devel-static
Group: Development/C++
Summary: Static library of %name
Requires: %name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the static library required for statically linking
applications with %name.

%endif #enabled static

%prep
%setup
rm -rf modules/{lua-*,wxstedit}/*
sed -r -i 's|LIBRARY DESTINATION .*$|LIBRARY DESTINATION %_lib|' \
	CMakeLists.txt
# Build for ZBS, hence add some patches and tricks from
#   https://github.com/pkulchenko/ZeroBraneStudio/blob/master/build/build-win32.sh#L300
sed -i 's/\(m_wxlState = wxLuaState(wxlState.GetLuaState(), wxLUASTATE_GETSTATE|wxLUASTATE_ROOTSTATE);\)/\/\/ removed by ZBS build process \/\/ \1/' modules/wxlua/wxlcallb.cpp
sed -i 's/LUA_VERSION_NUM < 502/0/' modules/wxlua/wxlcallb.cpp

# prepare external wxstedit
mkdir -p modules/wxstedit
ln -s /usr/include modules/wxstedit/
echo "project( wxStEdit )" > modules/wxstedit/CMakeLists.txt

%build
make -C bindings \
	clean all \
	LUA=%_bindir/lua%luaver

# Build for ZBS, hence add some patches and tricks from
#   https://github.com/pkulchenko/ZeroBraneStudio/blob/master/build/build-win32.sh#L316
%cmake \
	-DwxLua_LUA_LIBRARY_USE_BUILTIN=FALSE \
	-DwxStEdit_ROOT_DIR=$PWD/modules/wxstedit \
	-DCMAKE_CXX_FLAGS="-DLUA_COMPAT_MODULE" \
	-DwxWidgets_COMPONENTS="stc;gl;html;aui;adv;core;net;base" \
	-DwxLuaBind_COMPONENTS="stc;gl;html;aui;adv;core;net;base" \

%make_build -C BUILD
if [ -x /usr/bin/doxygen ]; then
	%make_build -C BUILD wxLua_doxygen
fi

%install
%makeinstall_std -C BUILD

mkdir -p \
	%buildroot%_desktopdir/ \
	%buildroot%_libdir/lua/%luaver \
	%buildroot%_iconsdir/hicolor/scalable/apps/
install -p art/wxlualogo.svg %buildroot%_iconsdir/hicolor/scalable/apps/
mv %buildroot%_libdir/libwx.so %buildroot%_libdir/lua/%luaver/wx.so
install -p distrib/autopackage/%name.desktop %buildroot%_desktopdir/
sed -r -i "s|wxluaedit|wxLuaEdit|" %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=IDE \
	%buildroot%_desktopdir/%name.desktop
rm -rf docs2distribute
mv %buildroot%_datadir/%name/doc docs2distribute
mv %buildroot%_datadir/%name/samples docs2distribute/

%files
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*
%_datadir/%name
%doc docs2distribute/*

%files -n lib%name
%_libdir/*.so
%_libdir/lua/%luaver/*.so

%files -n lib%name-devel
%_includedir/%name
#%%doc BUILD/doc-wxLua/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Jun 24 2019 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt7.git.e43a6d9
- new version, compatible with wxWidgets 3.1.2 (closes: 36870)

* Fri Jun 07 2019 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt6.git.ead9b38
- some fixes for ZeroBraneStudio

* Tue Sep 04 2018 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt5.git.ead9b38
- change upstream to https://github.com/pkulchenko/wxlua/

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.8.12.3-alt4.r246.3
- NMU: rebuild with new lua

* Sun Oct 04 2015 Anton Midyukov <antohami@altlinux.org> 2.8.12.3-alt4.r246.2
- Rebuilt for new gcc5 C++11 ABI.

* Mon Jul 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.12.3-alt3.r246.2
- Rebuilt with gcc5

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.12.3-alt3.r246.1
- Built with updated wxGTK3.1

* Mon Oct 27 2014 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt3.r246
- build with wxGTK3.1 + GTK+3
- fixed upstream

* Wed Oct 15 2014 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt2.r244
- SVN version
- build with libwxGTK3.0-devel

* Wed Oct 08 2014 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt1
- new version

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.10.0-alt1.qa4
- Rebuilt with wxGTK 2.8.12

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.10.0-alt1.qa3
- Fixed build with gcc 4.6

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.10.0-alt1.qa2

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.8.10.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for wxlua

* Thu Jun 17 2010 Ildar Mulyukov <ildar@altlinux.ru> 2.8.10.0-alt1
- initial build for ALTLinux
- disabled wxGTK Media binding
