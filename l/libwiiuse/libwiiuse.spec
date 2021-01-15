Name: libwiiuse
Version: 0.15.5
Release: alt2
Summary: The wiiuse library is used to access and control multiple Nintendo Wiimotes
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://github.com/rpavlik/wiiuse

Source: https://github.com/rpavlik/wiiuse/archive/%version/wiiuse-%version.tar.gz

BuildRequires(pre): rpm-build-ninja dos2unix
BuildRequires: gcc-c++ cmake libbluez-devel libGL-devel libfreeglut-devel libSDL-devel

%description
Wiiuse is a library written in C that connects with several Nintendo
Wii remotes.  Supports motion sensing, IR tracking, nunchuk, classic
controller, and the Guitar Hero 3 controller.  Single threaded and
nonblocking makes a light weight and clean API.

%package devel
Summary: Developer tools for the wiiuse library
Group: Development/C
Requires: libbluez-devel
Provides: pkgconfig(wiiuse)

%description devel
Header files needed to develop programs that link against the wiiuse library.

%package examples
Summary: Example programs for the wiiuse library
Group: Documentation

%description examples
Example programs to test accessing wiiremote controllers

%prep
%setup -n wiiuse-%version

dos2unix CHANGELOG.mkd README.mkd

%build
%cmake -GNinja
%ninja_build -C BUILD

%install
%ninja_install -C BUILD
# Can't use make install as it is a pathetic copy into fixed paths and won't
# work on x86_64
# install -Dpm 0755 BUILD/src/libwiiuse.so %%buildroot%%_libdir/libwiiuse.so.0
# ln -s libwiiuse.so.0 %%buildroot%%_libdir/libwiiuse.so
# install -Dpm 0644 src/wiiuse.h %%buildroot%%_includedir/wiiuse.h
# install -Dpm 0755 BUILD/example/wiiuseexample %%buildroot%%_bindir/wiiuseexample
# install -Dpm 0755 BUILD/example-sdl/wiiuseexample-sdl %%buildroot%%_bindir/wiiuseexample-sdl
# chrpath -d %%buildroot%%_bindir/wiiuseexample*
# Packed using %%doc
rm -rf %buildroot%_docdir/wiiuse

%files devel
%doc LICENSE CHANGELOG.mkd README.mkd
%_includedir/wiiuse.h
%_libdir/libwiiuse.so

%files examples
%doc example/example.c example-sdl/sdl.c
%_bindir/wiiuseexample
%_bindir/wiiuseexample-sdl

%changelog
* Tue Aug 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.5-alt2
- Removed chrpath from BR.
- Built with ninja instead make.

* Fri Jan 31 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.5-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec) (ALT #37832).
