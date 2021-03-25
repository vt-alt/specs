%define _unpackaged_files_terminate_build 1

Name: GTS
Version: 2.5.1
Release: alt1
Summary: A scanning tool developed by Studio Ghibli
Group: Graphics
License: BSD-3-Clause
URL: https://opentoonz.github.io/e/

# https://github.com/opentoonz/GTS.git
Source: %name-%version.tar

Patch1: %name-%version-alt-return-type.patch

BuildRequires: gcc-c++
BuildRequires: libtiff-devel
BuildRequires: libfltk-devel
BuildRequires: libGLEW-devel
BuildRequires: libsane-devel
# dependencies below this comment belong to libfltk-devel
BuildRequires: libXrender-devel
BuildRequires: libXcursor-devel
BuildRequires: libXfixes-devel
BuildRequires: libXext-devel
BuildRequires: libXft-devel
BuildRequires: fontconfig-devel
BuildRequires: libXinerama-devel

%description
GTS is a scanning tool developed by Studio Ghibli.
It's specialized in hand-drawn animation frames.
GTS uses TWAIN on Windows and SANE on other operating systems,
so you need scanner drivers that support these APIs in order to run it.
The interface is in English and scanned images are saved as TIFF/Targa.

%prep
%setup
%patch1 -p1

# remove unbundled libraries
rm -rf thirdparty

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc LICENSE.txt
%doc README.md ChangeLog.txt
%_bindir/*
%_datadir/%name

%changelog
* Thu Jul 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.1-alt1
- Initial build for ALT
