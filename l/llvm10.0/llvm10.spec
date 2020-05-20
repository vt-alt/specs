%global v_major 10.0
%global llvm_name llvm%v_major
%global clang_name clang%v_major
%global lld_name lld%v_major

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%ifarch %ix86 %arm
%define optflags_debug -g0
#define __nprocs 1
%else
%define optflags_debug -g1
%endif

%def_disable tests
%def_without clang

Name: %llvm_name
Version: 10.0.0
Release: alt0.1.p9
Summary: The Low Level Virtual Machine

Group: Development/C
License: NCSA
Url: http://llvm.org
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%version/llvm-%version.src.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%version/clang-%version.src.tar.xz
Source2: https://github.com/llvm/llvm-project/releases/download/llvmorg-%version/lld-%version.src.tar.xz
Source3: https://github.com/llvm/llvm-project/releases/download/llvmorg-%version/compiler-rt-%version.src.tar.xz
Patch:  clang-alt-i586-fallback.patch
Patch1: clang-9-alt-triple.patch
Patch2: llvm-alt-cmake-path.patch
Patch3: llvm-alt-fix-linking.patch
Patch4: llvm-alt-triple.patch
Patch5: compiler-rt-9-alt-i586-arch.patch
Patch6: RH-0001-CMake-Split-static-library-exports-into-their-own-ex.patch
Patch7: clang-alt-aarch64-dynamic-linker-path.patch
Patch8: 0001-Don-t-set-rpath-when-installing.patch
Patch9: lld-9-alt-mipsel-permit-textrels-by-default.patch
Patch10: llvm-10-alt-python3.patch

# ThinLTO requires /proc/cpuinfo to exists so the same does llvm
BuildPreReq: /proc

BuildRequires(pre): cmake >= 3.4.3
BuildRequires: rpm-build >= 4.0.4-alt112 libncursesw-devel
BuildRequires: chrpath libstdc++-devel libffi-devel perl-Pod-Parser perl-devel
BuildRequires: python3-module-recommonmark zip zlib-devel binutils-devel ninja-build
%if_with clang
BuildRequires: %clang_name %llvm_name-devel %lld_name
%else
BuildRequires: gcc-c++
%endif

Provides: llvm = %EVR
Obsoletes: llvm < %version
Conflicts: llvm7.0

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary
programming languages. The compiler infrastructure includes mirror sets
of programming tools as well as libraries with equivalent functionality.

%package devel
Group: Development/C
Summary: Libraries and header files for LLVM
Provides: llvm-devel = %EVR
Obsoletes: llvm-devel < %version
Conflicts: llvm7.0-devel
Requires: %name = %EVR

%description devel
This package contains library and header files needed to develop new
native programs that use the LLVM infrastructure.

%package devel-static
Summary: Static libraries for LLVM
Group: Development/C
Provides: llvm-devel-static = %EVR
Obsoletes: llvm-devel-static < %version
Conflicts: llvm7.0-devel-static
Requires: %name-devel = %EVR

%description devel-static
This package contains static libraries needed to develop new
native programs that use the LLVM infrastructure.

%package libs
Group: Development/C
Summary: LLVM shared libraries

%description libs
Shared libraries for the LLVM compiler infrastructure.

%package doc
Summary: Documentation for LLVM
Group: Documentation
BuildArch: noarch
Provides: llvm-doc = %EVR
Obsoletes: llvm-doc < %version
Conflicts: llvm7.0-doc

%description doc
Documentation for the LLVM compiler infrastructure.

%package -n %clang_name
Summary: A C language family frontend for LLVM
Group: Development/C
Requires: gcc
Provides: clang = %EVR
Obsoletes: clang < %version
Conflicts: clang7.0

%description -n %clang_name
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

%package -n %clang_name-libs
Group: Development/C
Summary: clang shared libraries

%description -n %clang_name-libs
Shared libraries for the clang compiler.

%package -n %clang_name-devel
Summary: Header files for clang
Group: Development/C
Provides: clang-devel = %EVR
Obsoletes: clang-devel < %version
Conflicts: clang7.0-devel
Requires: %clang_name = %EVR

%description -n %clang_name-devel
This package contains header files for the Clang compiler.

%package -n %clang_name-devel-static
Summary: Static libraries for clang
Group: Development/C
Provides: clang-devel-static = %EVR
Obsoletes: clang-devel-static < %version
Conflicts: clang7.0-devel-static
Requires: %clang_name-devel = %EVR

%description -n %clang_name-devel-static
This package contains static libraries for the Clang compiler.

%package -n %clang_name-analyzer
Summary: A source code analysis framework
Group: Development/C
BuildArch: noarch
Provides: clang-analyzer = %EVR
Obsoletes: clang-analyzer < %version
Conflicts: clang7.0-analyzer
Requires: %clang_name = %EVR

%description -n %clang_name-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package -n %clang_name-doc
Summary: Documentation for Clang
Group: Documentation
BuildArch: noarch
Provides: clang-doc = %EVR
Obsoletes: clang-doc < %version
Conflicts: clang7.0-doc

%description -n %clang_name-doc
Documentation for the Clang compiler front-end.

%package -n %lld_name
Summary: LLD - The LLVM Linker
Group: Development/C
Provides: lld = %EVR
Obsoletes: lld < %version

%description -n %lld_name
LLD is a linker from the LLVM project. That is a drop-in replacement for system
linkers and runs much faster than them. It also provides features that are
useful for toolchain developers.

%package -n %lld_name-devel
Summary: Header files for LLD
Group: Development/C
Provides: lld-devel = %EVR
Obsoletes: lld-devel < %version
Requires: %lld_name = %EVR

%description -n %lld_name-devel
This package contains header files for the LLD linker.

%package -n %lld_name-doc
Summary: Documentation for LLD
Group: Documentation
BuildArch: noarch
Provides: lld-doc = %EVR
Obsoletes: lld-doc < %version

%description -n %lld_name-doc
Documentation for the LLD linker.

%prep
%setup -n llvm-%version.src -a1 -a2 -a3
for pkg in clang lld; do
   mv $pkg-%version.src tools/$pkg
done
mv compiler-rt-%version.src projects/compiler-rt
%patch -p1 -b .alt-i586-fallback
%patch1 -p1 -b .alt-triple
%patch2 -p1 -b .alt-cmake-path
%patch3 -p1 -b .alt-fix-linking
%patch4 -p1 -b .alt-triple
%patch5 -p1 -b .alt-i586-arch
%patch6 -p1
%patch7 -p1 -b .alt-aarch64-dynamic-linker
%patch8 -p1
%patch9 -p1 -b .alt-mipsel-permit-textrels-by-default
%patch10 -p1

%build
%cmake -G Ninja \
	-DLLVM_PARALLEL_LINK_JOBS=1 \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_TARGETS_TO_BUILD="host;AMDGPU;BPF;NVPTX;" \
	-DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD='AVR' \
	-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
	-DLLVM_ENABLE_ZLIB:BOOL=ON \
	-DLLVM_ENABLE_FFI:BOOL=ON \
	-DLLVM_ENABLE_RTTI:BOOL=ON \
	-DLLVM_OPTIMIZED_TABLEGEN:BOOL=ON \
	-DLLVM_BINUTILS_INCDIR="%_includedir/bfd" \
	\
	-DCLANG_PLUGIN_SUPPORT:BOOL=ON \
	-DCLANG_LINK_CLANG_DYLIB=ON \
	\
	%if_with clang
	-DLLVM_ENABLE_LTO=Thin \
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DLLVM_ENABLE_LLD:BOOL=ON \
	%else
	-DLLVM_ENABLE_LTO=On \
	-DLLVM_USE_LINKER=gold \
	-DCMAKE_AR:PATH=%_bindir/gcc-ar \
	-DCMAKE_NM:PATH=%_bindir/gcc-nm \
	-DCMAKE_RANLIB:PATH=%_bindir/gcc-ranlib \
	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,-Bsymbolic" \
	%endif
	\
	-DLLVM_LIBDIR_SUFFIX="%_libsuff" \
	-DLLVM_BUILD_RUNTIME:BOOL=ON \
	\
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \
	-DLLVM_BUILD_TOOLS:BOOL=ON \
	\
	%if_enabled tests
	-DLLVM_INCLUDE_TESTS:BOOL=ON \
	-DLLVM_BUILD_TESTS:BOOL=ON \
	%endif
	\
	-DLLVM_INCLUDE_EXAMPLES:BOOL=ON \
	-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
	\
	-DLLVM_INCLUDE_UTILS:BOOL=ON \
	-DLLVM_INSTALL_UTILS:BOOL=OFF \
	\
	-DLLVM_INCLUDE_DOCS:BOOL=ON \
	-DLLVM_BUILD_DOCS:BOOL=ON \
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DSPHINX_WARNINGS_AS_ERRORS:BOOL=OFF \
	-DSPHINX_EXECUTABLE=%_bindir/sphinx-build-3 \
	-DLLVM_ENABLE_DOXYGEN:BOOL=OFF \
	-DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \
	-DPYTHON_EXECUTABLE=%_bindir/python3

sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' BUILD/build.ninja
ninja -vvv -j %__nprocs -C BUILD

%install
pushd BUILD
cmake -DCMAKE_INSTALL_PREFIX=%buildroot%prefix ../
sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' build.ninja
sed -i '/^[[:space:]]*include.*tools\/lld\/docs\/cmake_install.cmake.*/d' tools/lld/cmake_install.cmake
popd
ninja -C BUILD install

# And prepare Clang documentation
rm -rf BUILD/clang-docs
mkdir -p BUILD/clang-docs
for f in LICENSE.TXT NOTES.txt README.txt; do
  ln tools/clang/$f BUILD/clang-docs/
done
rm -rf tools/clang/docs/{doxygen*,Makefile*,*.graffle,tools}

install -m 0755 BUILD/%_lib/LLVMHello.so %buildroot%_libdir/
install -m 0755 BUILD/%_lib/BugpointPasses.so %buildroot%_libdir/
mkdir -p %buildroot%_docdir/lld

file %buildroot%_bindir/* | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d
file %buildroot%_libdir/*.so | awk -F: '$2~/ELF/{print $1}' | xargs -r chrpath -d

%ifarch %ix86
cd %buildroot%_libdir/clang/%version/lib/linux
ls *-i[3-9]86* | while read f; do ln -s $f $(echo $f | sed 's|i[3-9]86|i386|') ; done
%endif

%check
%if_enabled tests
LD_LIBRARY_PATH=%buildroot%_libdir:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
ninja -C BUILD check-all || :
%endif

%files
%doc CREDITS.TXT LICENSE.TXT README.txt
%_bindir/*
%_man1dir/*
%exclude %_bindir/llvm-config*
%exclude %_bindir/*clang*
%exclude %_bindir/c-index-test
%exclude %_bindir/scan-*
%exclude %_man1dir/llvm-config.1.*
%exclude %_man1dir/clang.1*
%exclude %_man1dir/scan-build.1*
%exclude %_bindir/lld*
%exclude %_bindir/ld*.lld
%exclude %_bindir/wasm-ld

%files libs
%_libdir/libLLVM-*.so
%_libdir/libLTO.so.*
%_libdir/libRemarks.so.*

%files devel
%_bindir/llvm-config
%_man1dir/llvm-config.1.*
%_includedir/llvm
%_includedir/llvm-c
%_libdir/libLLVM.so
%_libdir/libLTO.so
%_libdir/LLVMgold.so
%_libdir/libRemarks.so
%_libdir/LLVMHello.so
%_libdir/BugpointPasses.so
%_datadir/cmake/Modules/llvm
%exclude %_datadir/cmake/Modules/llvm/LLVMStaticExports.cmake

%files devel-static
%_libdir/*.a
%exclude %_libdir/libclang*.a
%_datadir/cmake/Modules/llvm/LLVMStaticExports.cmake

%files -n %clang_name
%doc BUILD/clang-docs/*
%_bindir/*clang*
%_bindir/c-index-test
%_man1dir/clang.1*

%files -n %clang_name-libs
%_libdir/clang
%_libdir/libclang*.so.*

%files -n %clang_name-devel
%_includedir/clang
%_includedir/clang-c
%_libdir/libclang*.so
%_datadir/cmake/Modules/clang

%files -n %clang_name-devel-static
%_libdir/libclang*.a

%files -n %clang_name-analyzer
%_prefix/libexec/*-analyzer
%_bindir/scan-build
%_bindir/scan-view
%_datadir/scan-build
%_datadir/scan-view
%_man1dir/scan-build.1*

%files -n %lld_name
%_bindir/lld*
%_bindir/ld*.lld
%_bindir/wasm-ld

%files -n %lld_name-devel
%dir %_includedir/lld
%_includedir/lld/*

%files doc
%doc %_docdir/llvm

%files -n %clang_name-doc
%doc %_docdir/clang

%files -n %lld_name-doc
%doc %_docdir/lld

%changelog
* Mon May 18 2020 Andrey Cherepanov <cas@altlinux.org> 10.0.0-alt0.1.p9
- Backport to p9 branch.
- Add conflicts to llvm7.0 packages.

* Wed Mar 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 10.0.0-alt1
- 10.0.0

* Fri Mar 20 2020 Valery Inozemtsev <shrek@altlinux.ru> 9.0.1-alt3
- use 'Release' build
- clang: fixed link with option -fsanitize=address (closes: #38250)

* Thu Feb 13 2020 Valery Inozemtsev <shrek@altlinux.ru> 9.0.1-alt2
- build with clang

* Mon Feb 10 2020 Valery Inozemtsev <shrek@altlinux.ru> 9.0.1-alt1
- 9.0.1

* Wed May 22 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.0.1-alt4.rel
- Added mipsel-alt-linux and ppc64le-alt-linux triples support.
- lld:
  + mipsel: allowed textrels by default;
  + ppc64le: backported upstream fixes for ThinLTO support and relocation
  checks.

* Mon Jan 21 2019 L.A. Kostis <lakostis@altlinux.ru> 7.0.1-alt3.rel
- Added patches from stable:
  + llvm-nm: Add --portability as alias for --format=posix.
  + llvm-objdump: Implement -z/--disassemble-zeroes.
  + AMDGPU: test for uniformity of branch instruction, not its
            condition.

* Fri Jan 04 2019 L.A. Kostis <lakostis@altlinux.ru> 7.0.1-alt2.rel
- Rebuild by clang7.0.

* Fri Dec 21 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.1-alt1.rel.1
- Bootstrap w/ gcc.

* Mon Dec 17 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.1-alt1.rel
- Updated to 7.0.1.
- Split static library exports in cmake (patch from RH).
- Build with clang.

* Sat Sep 22 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt1.rel
- First try of 7.0.0.

* Wed Sep 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt0.11.rel
- NMU: updated build with clang for aarch64.

* Tue Jun 19 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.10.rel
- llvm-ar: backported support of dashed options (chromium build
  depends on it).

* Tue Jun 12 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.0.0-alt0.9.rel
- aarch64: rebuilt with clang.

* Tue Jun 12 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.0.0-alt0.8.rel
- lld: backported upstream commit implementing --{push,pop}-state support.
- clang: changed default dynamic linker path for aarch64 architecture.
- aarch64: temporarily rebuilt with gcc to fix build from source.
- clang-alt-triple.patch: added mipsel and mips64el triplets.

* Wed Mar 28 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt0.3.r328699
- Rebased to llvm master SVN r328699.

* Tue Mar 20 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.7.rel
- Reduce debuginfo for x86_64.
- Use 'Release' build on x86_64.
- Fix provides/obsoletes.
- Move clang libs to separate pkg (to ease future migrations).

* Sun Mar 18 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt0.2.r327779
- Rebased to llvm master SVN r327779.
- Build w/ clang and lld.
- .spec: sync changes with llvm6.0.

* Thu Mar 15 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.6.rel
- Bootstrap with clang, lld and ThinLTO.
- .spec: sync with RH
  + 0001-DebugInfo-Discard-invalid-DBG_VALUE-instructions-in-.patch
  + 0001-Fixup-for-rL326769-RegState-Debug-is-being-truncated.patch
  + RH-0001-CMake-Split-static-library-exports-into-their-own-ex.patch
- .spec: move gold plugin to -devel (tnx to legion@)
- Build changes:
  + Reduce memory consumption on x86:
    + Reduce amount of debuginfo (use -g1)
    + Use Release as build target.
  + Use compiler-rt (instead of libgcc).
  + Use 8 build jobs.

* Mon Mar 12 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.5.rel
- Test build using clang and lld.
- Increase build jobs number to 16 (thanks to lld/thinLTO).

* Sun Mar 11 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.4.rel
- Prepare for LLD/clang build bootstrap.

* Sun Mar 11 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.3.rel
- Added LLD build.

* Sat Mar 10 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.2.rel
- Added flag to build with clang (should reduce memory usage for LTO).
- Reduce build jobs (workaround to reduce memory consumption).

* Fri Mar 09 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.1.rel
- Updated to 6.0.0 release.
- Build changes:
  + use LTO by default.
  + enabled gold linker.
  + use ninja build.

* Tue Feb 27 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt0.1.r326101
- Rebased to llvm master SVN r326101.

* Thu Feb 15 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt0.1.r325294
- Rebased to llvm master SVN r325294.
- Use host as build target (tnx to glebfm@).

* Sun Feb 04 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.1-alt1.3.rel
- Replaced X86 with native in the list of targets.
- Added provides and obsoletes to replace old llvm packages and its
  subpackages.

* Thu Oct 19 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1.2.rel
- NMU: changed CMake Modules install path

* Thu Sep 14 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.1-alt1.1.rel
- remove conflicts: llvm from -libs pkg (closes #33879).

* Sun Sep 10 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.1-alt1.rel
- Updated 4.0.0 release and build configuration:
  + Enabled AVR experimental target.

* Thu Sep 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt2.rel
- Installed example llvm plugins required by cmake modules.

* Sun Mar 19 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt1.rel
- Define cmake modules dir correctly (closes #33250).

* Mon Mar 13 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.9.rel
- Updated 4.0.0 release.

* Thu Dec 29 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.6.r290127
- Enabled gold plugin.

* Wed Dec 28 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.5.r290127
- Renamed clang to clang4.0 (to coexist with 3.x clang).

* Sun Dec 25 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.4.r290127
- repackage clang-analyzer, now with proper dirs.

* Thu Dec 22 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.3.r290127
- llvm: Fix segfault in libLLVM due missing /proc/cpuinfo.
- .spec: fix libs intersections between llvm and clang.
- .spec: remove unsupported stuff from clang-analyzer.

* Wed Dec 21 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.2.r290127
- Update build configuration:
  + Enabled BPF target.
  + Enabled optimisation.
  + Disabled unconditionally enabled tests.

* Mon Dec 19 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r290127
- Updated LLVM to SVN r290127.
- Enabled clang (SVN r290130).

* Tue Nov 08 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r286177
- Updated to SVN r286177.

* Fri Sep 30 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r282877
- Updated to SVN r282877.

* Fri Aug 05 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r277804
- Updated to SVN r277804.

* Sat Jun 25 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r273782
- Updated to SVN r273782.

* Wed Jun 15 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r272815
- Updated to SVN r272815.
- Enabled X86 target (for llvmpipe).

* Sun Jun 12 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r272517
- build as separate lib for Mesa-dev.

* Thu Jun 02 2016 Rudolf Kastl <rkastl@redhat.com> 3.9.0-0.1.r
- using a random svn checkout of 3.9
- removed CppBackend
- updated files section

* Thu Mar 10 2016 Dave Airlie <airlied@redhat.com> 3.8.0-1
- llvm 3.8.0 release

* Wed Mar 09 2016 Dan Horák <dan[at][danny.cz> 3.8.0-0.3
- install back memory consumption workaround for s390

* Thu Mar 03 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.2
- llvm 3.8.0 rc3 release

* Fri Feb 19 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.1
- llvm 3.8.0 rc2 release

* Tue Feb 16 2016 Dan Horák <dan[at][danny.cz> 3.7.1-7
- recognize s390 as SystemZ when configuring build

* Sat Feb 13 2016 Dave Airlie <airlied@redhat.com> 3.7.1-6
- export C++ API for mesa.

* Sat Feb 13 2016 Dave Airlie <airlied@redhat.com> 3.7.1-5
- reintroduce llvm-static, clang needs it currently.

* Fri Feb 12 2016 Dave Airlie <airlied@redhat.com> 3.7.1-4
- jump back to single llvm library, the split libs aren't working very well.

* Fri Feb 05 2016 Dave Airlie <airlied@redhat.com> 3.7.1-3
- add missing obsoletes (#1303497)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.1-1
- new upstream release
- enable gold linker

* Wed Nov 04 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- fix Requires for subpackages on the main package

* Tue Oct 06 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- initial version using cmake build system
