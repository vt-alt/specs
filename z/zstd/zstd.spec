Name: zstd
Version: 1.4.3
Release: alt1
Summary: Zstd compression library and tools
License: BSD
Group: Archiving/Compression
Url: https://facebook.github.io/zstd/
# https://github.com/facebook/zstd
# git://git.altlinux.org/gears/z/zstd.git
Source: %name-%version-%release.tar
Requires: lib%name = %EVR
%def_enable pzstd
%{?!_disable_pzstd:BuildRequires: gcc-c++}
%{?!_disable_pzstd:%{?!_without_check:%{?!_disable_check:BuildRequires: libgtest-devel}}}

%description
Zstd, short for Zstandard, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level compression ratio.

%package -n pzstd
Summary: Parallel Zstandard tool
Group: %group
Requires: %name = %EVR

%description -n pzstd
Parallel Zstandard is a Pigz-like tool for Zstandard.

It provides Zstandard format compatible compression and decompression
that is able to utilize multiple cores.  It breaks the input up into
equal sized chunks and compresses each chunk independently into a
Zstandard frame.  It then concatenates the frames together to produce
the final compressed output.  Pzstandard will write a 12 byte header for
each frame that is a skippable frame in the Zstandard format, which
tells PZstandard the size of the next compressed frame.

PZstandard supports parallel decompression of files compressed with
PZstandard.  When decompressing files compressed with Zstandard,
PZstandard does IO in one thread, and decompression in another.

%package -n lib%name
Summary: Zstd compression shared library
Group: System/Libraries

%description -n lib%name
Zstd, short for Zstandard, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level compression ratio.

This package contains lib%name shared library.

%package -n lib%name-devel
Summary: Zstd compression development files
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Zstd, short for Zstandard, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level compression ratio.

This package contains development files required to build applications
using lib%name library.

%prep
%setup -n %name-%version-%release
# reenable recipe echoing
sed -i 's/^\([[:space:]]*\)@\$/\1\$/' Makefile */Makefile
%define make_params GZFILES= ZSTD_LEGACY_SUPPORT=0 HAVE_ZLIB=0

%build
export CFLAGS="%optflags $(getconf LFS_CFLAGS)"
export CXXFLAGS="$CFLAGS"
for dir in lib programs; do
	%make_build -C $dir all %make_params
done
%{?!_disable_pzstd:%make_build -C contrib/pzstd}

%install
export CC=false CXX=false # nothing should be compiled or linked during install
for dir in lib programs; do
	%makeinstall_std -C $dir \
		INSTALL_SCRIPT=: PREFIX=%prefix LIBDIR=%_libdir %make_params
done
%{?!_disable_pzstd:%makeinstall_std PREFIX=%prefix -C contrib/pzstd}

# Relocate shared library from %_libdir/ to /%_lib/
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
        t=$(readlink -v "$f")
	ln -rsnf %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
export CFLAGS="%optflags $(getconf LFS_CFLAGS)"
export CXXFLAGS="$CFLAGS"
%make_build -k -C tests test %make_params
%{?!_disable_pzstd:%make_build -k -C contrib/pzstd tests GTEST_INC= GTEST_LIB=}
%{?!_disable_pzstd:LD_LIBRARY_PATH=%buildroot/%_lib make -C contrib/pzstd check}

%files
%_bindir/*
%exclude %_bindir/pzstd
%_man1dir/*
%doc CHANGELOG README.md

%files -n pzstd
%_bindir/pzstd

%files -n lib%name
/%_lib/*.so.*
%doc LICENSE

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Aug 19 2019 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- 1.4.2 -> 1.4.3.

* Thu Jul 25 2019 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- 1.3.8 -> 1.4.2.

* Thu Dec 27 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.8-alt1
- 1.3.7 -> 1.3.8.

* Wed Oct 17 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.7-alt1
- 1.3.5 -> 1.3.7.

* Wed Jul 11 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt1
- 1.3.4 -> 1.3.5.

* Mon Mar 26 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.4-alt1
- 1.3.3 -> 1.3.4.

* Thu Dec 21 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt1
- 1.3.2 -> 1.3.3.

* Sun Oct 29 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt1
- 1.3.0 -> 1.3.2.

* Tue Jul 18 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0.

* Thu May 25 2017 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- 1.1.4 -> 1.2.0.

* Tue Mar 28 2017 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt2
- Moved pzstd to separate subpackage.

* Tue Mar 21 2017 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- v1.1.3-322-gebf2 == v1.1.4.
- Relocated shared library from %_libdir/ to /%_lib/.

* Fri Mar 17 2017 Dmitry V. Levin <ldv@altlinux.org> 1.1.3.0.322.ebf2-alt1
- v1.1.3-322-gebf2.
