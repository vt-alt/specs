Name: igt-gpu-tools
Version: 1.24
Release: alt1

Summary: tools for debugging the Intel graphics driver
License: MIT
Group: Development/Debug

# http://cgit.freedesktop.org/xorg/app/intel-gpu-tools/
Url: http://01.org/linuxgraphics/
Source: igt-gpu-tools-%version.tar.xz

Provides: intel-gpu-tools-@version@
Obsoletes: intel-gpu-tools

# dropped by buildreq but still required
# Automatically added by buildreq on Wed Dec 11 2019
# optimized out: fontconfig fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libEGL-devel libGL-devel libX11-devel libXau-devel libXext-devel libXrender-devel libcrypt-devel libelf-devel libfreetype-devel libglvnd-devel libgraphite2-devel libharfbuzz-devel libicu-devel libjson-c4 libncurses-devel libp11-kit libpng-devel libsasl2-3 libtinfo-devel libxcb-devel libxmlrpc-client ninja-build perl pkg-config python-modules python2-base python3 python3-base python3-module-pkg_resources sh4 xz zlib-devel
BuildRequires: flex git-core gtk-doc libXrandr-devel libXv-devel libalsa-devel libcairo-devel libcurl-devel libdb4-devel libdrm-devel libdw-devel libgdbm-devel libgsl-devel libjson-c-devel libkmod-devel libpciaccess-devel libpixman-devel libprocps-devel libudev-devel libunwind-devel libxmlrpc-devel meson python3-dev

BuildRequires: xorg-util-macros
BuildRequires: libdrm-devel >= 2.4.64

# 1.6+
BuildRequires: gtk-doc xorg-dri2proto-devel swig python3-dev flex

# just to be sure...
BuildRequires: bison
BuildRequires: flex
BuildRequires: python3-module-docutils
BuildRequires: python3
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-xlib)
BuildRequires: pkgconfig(dri2proto)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libkmod)
BuildRequires: pkgconfig(libprocps)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(libunwind)
BuildRequires: pkgconfig(pciaccess)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xv)

ExclusiveArch: %ix86 x86_64

Requires: intel-gen4asm = %version

%description
igt-gpu-tools is a package of tools for debugging the Intel graphics
driver, including a GPU hang dumping program, performance monitor,
and performance microbenchmarks for regression testing the DRM.

%package -n intel-gen4asm
Summary: Intel 965 assembly language compiler
License: MIT
Group: Development/Tools

%description -n intel-gen4asm
intel-gen4asm is a program to compile an assembly language for the Intel 965
Express Chipset.  It has been used to construct programs for textured video
in the 2d driver.

%package devel-doc
Summary: GTK development documentation for %name
License: MIT
BuildArch: noarch
Group: Development/Documentation

%description devel-doc
%summary

%prep
%setup
sed -i 's/NOT-GIT/%release/g' lib/Makefile.sources

%build
%meson
%meson_build

#exit 1 
#autoreconf
#configure
#make_build

%install
%meson_install
#makeinstall_std

%files
%_bindir/*
%_libdir/*.so*
%_usr/lib/%name/
%_datadir/%name/
#_datadir/gtk-doc/html/%name/
#_mandir/*/*
%exclude %_bindir/intel-gen4asm
%exclude %_bindir/intel-gen4disasm
%exclude %_pkgconfigdir/intel-gen4asm.pc

%files devel-doc
%_datadir/gtk-doc/html/%name

%files -n intel-gen4asm
%_bindir/intel-gen4asm
%_bindir/intel-gen4disasm
%_pkgconfigdir/intel-gen4asm.pc
%doc assembler/README assembler/TODO assembler/doc/examples/

%changelog
* Wed Dec 11 2019 Fr. Br. George <george@altlinux.ru> 1.24-alt1
- Autobuild version bump to 1.24
- Rename to igt-gpu-tools
- Switch to meson build

* Thu Sep 20 2018 Fr. Br. George <george@altlinux.ru> 1.22-alt1
- Autobuild version bump to 1.22

* Thu Sep 20 2018 Fr. Br. George <george@altlinux.ru> 1.20-alt1
- Autobuild version bump to 1.20

* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.19-alt1
- Updated to upstream version 1.19

* Thu Dec 08 2016 Michael Shigorin <mike@altlinux.org> 1.17-alt2
- moved intel-gen4asm into a subpackage of its own
  (replacing the pre-existing standalone one);
  thanks week@ for pointing the file confict out

* Tue Dec 06 2016 Michael Shigorin <mike@altlinux.org> 1.17-alt1
- 1.17
- buildreq (and some BRs from rosa package, thanks)

* Sun Jan 03 2016 Michael Shigorin <mike@altlinux.org> 1.13-alt1
- 1.13

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 1.6-alt1
- 1.6

* Sat Jun 08 2013 Michael Shigorin <mike@altlinux.org> 1.3-alt1
- built for ALT Linux based on opensuse and debian packages

