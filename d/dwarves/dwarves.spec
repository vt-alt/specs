# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define libname libdwarves
%define libver 1

Name: dwarves
Version: 1.19
Release: alt1
Summary: Debugging Information Manipulation Tools (pahole & friends)
Group: Development/Tools
Provides: pahole
License: GPL-2.0-only
Url: http://acmel.wordpress.com
#Vcs: https://github.com/acmel/dwarves
Vcs: https://git.kernel.org/pub/scm/devel/pahole/pahole.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: elfutils-devel
BuildRequires: libdw-devel
BuildRequires: git-core

%description
dwarves is a set of tools that use the debugging information inserted in
ELF binaries by compilers such as GCC, used by well known debuggers such as
GDB, and more recent ones such as systemtap.

Utilities in the dwarves suite include pahole, that can be used to find
alignment holes in structs and classes in languages such as C, C++, but not
limited to these.

It also extracts other information such as CPU cacheline alignment, helping
pack those structures to achieve more cache hits.

These tools can also be used to encode and read the BTF type information format
used with the Linux kernel bpf syscall, using 'pahole -J' and 'pahole -F btf'.

A diff like tool, codiff can be used to compare the effects changes in source
code generate on the resulting binaries.

Another tool is pfunct, that can be used to find all sorts of information about
functions, inlines, decisions made by the compiler about inlining, etc.

One example of pfunct usage is in the fullcircle tool, a shell that drivers
pfunct to generate compileable code out of a .o file and then build it using
gcc, with the same compiler flags, and then use codiff to make sure the
original .o file and the new one generated from debug info produces the same
debug info.

The btfdiff utility compares the output of pahole from BTF and DWARF to make
sure they produce the same results.

%package -n %libname%libver
Summary: Debugging information processing library
Group: System/Libraries

%description -n %libname%libver
Debugging information processing library.

%package -n %libname%libver-devel
Summary: Debugging information library development files
Group: Development/C
Requires: %libname%libver = %version-%release

%description -n %libname%libver-devel
Debugging information processing library development files.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install install DESTDIR=%buildroot
chmod a+x %buildroot%_datadir/dwarves/runtime/python/ostra.py

%check
cd BUILD
export LD_LIBRARY_PATH=$PWD PATH=$PWD:$PATH
# Pahole examples @ https://lwn.net/Articles/335942/
pahole -C tag pahole
pahole --packable pahole

%files
%doc README.ctracer README.btf NEWS COPYING
%_bindir/*
%_datadir/dwarves
%_man1dir/pahole.1*

%files -n %libname%libver
%_libdir/%{libname}*.so.*

%files -n %libname%libver-devel
%doc MANIFEST README
%_includedir/dwarves
%_libdir/%{libname}*.so

%changelog
* Sun Dec 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.19-alt1
- Update to v1.19 (2020-11-20).

* Mon Oct 05 2020 Vitaly Chikunov <vt@altlinux.org> 1.18-alt1
- Update to v1.18 (2020-10-02).

* Thu Apr 16 2020 Vitaly Chikunov <vt@altlinux.org> 1.17-alt1
- Initial build for Sisyphus of v1.17 (released 2020-03-13).
