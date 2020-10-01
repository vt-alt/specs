Name: patchelf
Version: 0.10
Release: alt1
Summary: A utility for patching ELF binaries

Group: Development/Tools
License: GPLv3+
Url: http://nixos.org/patchelf.html
# repacked https://nixos.org/releases/patchelf/patchelf-%version/%name-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Mon Nov 07 2016
# optimized out: libstdc++-devel python-base
BuildRequires: gcc-c++

%description
PatchELF is a simple utility for modifying an existing ELF executable
or library.  It can change the dynamic loader ("ELF interpreter")
of an executable and change the RPATH of an executable or library.

%prep
%setup

# package ships elf.h - delete to use glibc-headers one
rm src/elf.h

%build
%configure
%make_build

%check
rc=0
make check || rc=$?
%ifnarch %arm aarch64
[ "$rc" = 0 ]
%endif

%install
%makeinstall_std

# the docs get put in a funny place, so delete and include in the
# standard way in the docs section below
rm -rf %buildroot/usr/share/doc/%name

%files
%doc COPYING README
%_bindir/patchelf
%_mandir/man1/patchelf.1*

%changelog
* Fri Aug 16 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10-alt1
- Updated to 0.10.

* Sun Jun 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.9-alt3
- NMU: build for aarch64

* Mon Nov 07 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9-alt2
- Initial build.
