Name:    codelite
Version: 13.0
Release: alt2

Summary: CodeLite is a powerful open-source, cross platform code editor for C/C++

License: GPLv2+
Group:   Development/Tools
Url:     http://codelite.sourceforge.net

Source:  %name-%version.tar

Requires: libedit-devel

BuildRequires: cmake gcc-c++ libssh-devel libedit-devel libgtk+3-devel
BuildRequires: libsqlite3-devel libwxGTK3.1-devel libatk-devel libpango-devel
BuildRequires: libpcre-devel libffi-devel libfribidi-devel libtiff-devel
BuildRequires: libmount-devel libpixman-devel libblkid-devel libuuid-devel
BuildRequires: libselinux-devel bzlib-devel libexpat-devel libXdmcp-devel
BuildRequires: libXdamage-devel libXxf86vm-devel libdrm-devel libXinerama-devel
BuildRequires: libXi-devel libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: wayland-protocols libxkbcommon-devel libwayland-cursor-devel
BuildRequires: libwayland-egl-devel libepoxy-devel libhunspell-devel
BuildRequires: libwxGTK3.1-sqlite3-devel compat-libwxGTK3.1-gtk2-devel
BuildRequires: libXtst-devel at-spi2-atk-devel libat-spi2-core-devel

%add_python_req_skip gdb

%description
CodeLite uses a sophisticated, yet intuitive interface which allows
users to easily create, build and debug complex projects.

%prep
%setup

%build
%add_optflags %(pkg-config --cflags pango)
cmake . -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_CXX_FLAGS:STRING='%optflags'

%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/mime/packages/
cp -p %name.xml %buildroot%_datadir/mime/packages/

%find_lang %name

%files -f %name.lang
%doc AUTHORS LICENSE COPYING
%_bindir/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/mime/packages/%name.xml
%_datadir/icons/hicolor/*/apps/%name.png
%_libdir/%name
%_mandir/man1/%{name}*

%changelog
* Tue Aug 20 2019 Anton Midyukov <antohami@altlinux.org> 13.0-alt2
- add_optflags (pkg-config --cflags pango) (Fix FTBFS)

* Wed Jun 19 2019 Grigory Ustinov <grenka@altlinux.org> 13.0-alt1
- Initial build for Sisyphus.
