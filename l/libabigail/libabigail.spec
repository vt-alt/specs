Name: libabigail
Version: 1.6
Release: alt1
Summary: ABI Generic Analysis and Instrumentation Library and tools
Group: Development/Other

License: LGPLv3+
Url: https://sourceware.org/libabigail/
Source0: %name-%version.tar

# Automatically added by buildreq on Wed Mar 28 2018 (-bi)
BuildRequires: doxygen gcc-c++ libdw-devel libxml2-devel makeinfo python3-module-sphinx

%description
This package contains %summary.

%package -n libabigail0
Summary: ABI Generic Analysis and Instrumentation Library runtime
Group: System/Libraries
Conflicts: libabigail < %version

%description -n libabigail0
This package contains %summary.

%package devel
Summary: ABI Generic Analysis and Instrumentation Library development files
Group: Development/C
Requires: libabigail0 = %EVR

%description devel
This package contains %summary.

%package -n abigail-tools
Summary: ABI Generic Analysis and Instrumentation Library tools
Group: Development/Other
Requires: libabigail0 = %EVR
Provides: libabigail = %version
Obsoletes: libabigail < %version, libabigail-doc < %version

%description -n abigail-tools
This package contains %summary:
abidiff, kmidiff, abipkgdiff, abicompat, abidw, and abilint.

The abidiff command line tool compares the ABI of two ELF shared
libraries and emits meaningful textual reports about changes impacting
exported functions, variables and their types.  Simarly, the kmidiff
compares the kernel module interface of two Linux kernels, abipkgdiff
compares the ABIs of ELF binaries contained in two packages, abicompat
checks if a subsequent version of a shared library is still compatible
with an application that is linked against it, abidw emits an XML
representation of the ABI of a given ELF shared library, abilint
checks that a given XML representation of the ABI of a shared library
is correct.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-silent-rules \
	--disable-zip-archive \
	--enable-cxx11=yes \
	--disable-static \
	FOUND_SPHINX_BUILD=yes \
	#
%make_build
%make_build -C doc/manuals man info SPHINXBUILD=sphinx-build-3

%install
%makeinstall_std
find %buildroot -name '*.la' -delete

# Install man and texinfo files as they are not installed by the
# default 'install' target of the makefile.
make -C doc/manuals install-man-and-info-doc DESTDIR=%buildroot

%check
%make_build -k check

%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict

%files -n libabigail0
%_libdir/libabigail/
%_libdir/libabigail.so.*

%files devel
%_includedir/*
%_libdir/libabigail.so
%_pkgconfigdir/libabigail.pc
%_aclocaldir/abigail.m4

%files -n abigail-tools
%_bindir/*
%_mandir/man?/*
%_infodir/abigail.info*

%changelog
* Wed Mar 27 2019 Dmitry V. Levin <ldv@altlinux.org> 1.6-alt1
- 1.2 -> 1.6.

* Wed Mar 28 2018 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- 1.0.rc2 -> 1.2.
- Renamed libabigail to abigail-tools, dropped doc subpackage.

* Fri Feb 05 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.2.rc2
- Updated to 1.0.rc2.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.2.rc0.1
- NMU: added BR: texinfo

* Thu Nov 19 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.2.rc0
- Updated to 1.0.rc0.

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt0.1.git088f077
- Initial build.
