Name: wine-grdwine
Version: 0.5.5
Release: alt1

Summary: Guardant usb dongle helper library for Wine
License: LGPLv2
Group: Emulators

Url: https://guardant.com
Packager: Konstantin Kondratyuk <kondratyuk@altlinux.org>

# Source-url: ftp://ftp.guardant.ru/support/linux/grdwine-%version.tar.gz
Source: %name-%version.tar

BuildRequires: libwine-devel

ExclusiveArch: %ix86 x86_64

%ifarch x86_64 aarch64
  %def_with build64
%else
  %def_without build64
%endif

%define winelibdir %_libdir/wine
%add_verify_elf_skiplist %winelibdir/grdwine.dll.so

%description
Guardant usb dongle helper library for Wine.
Implementation of the GrdWine is based on Linux USB Device
Filesystem and Linux USB HID Device Interface.

%prep
%setup

%build
#autoreconf
./bootstrap.sh

%if_with build64
%configure \
	--enable-win64 \
%else
%configure \
%endif
	--with-wineincs=%_includedir \
	--with-winedlls=%buildroot/%winelibdir

%make_build

%install
mkdir -p %buildroot/%winelibdir/
%makeinstall_std

%files
%winelibdir/grdwine.dll.so

%changelog
* Thu May 30 2019 Konstantin Kondratyuk <kondratyuk@altlinux.org> 0.5.5-alt1
- new version (0.5.5) with rpmgs script

