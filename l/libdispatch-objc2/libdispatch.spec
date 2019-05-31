%set_verify_elf_method unresolved=strict

Name: libdispatch-objc2
Version: 1.2
Release: alt5.git20140226
Summary: Linux port of Apple's open-source concurrency library
License: Apache License v2
Group: System/Libraries
Url: http://etoileos.com/

# https://github.com/etoile/libdispatch-objc2.git
Source: %name-%version.tar

BuildRequires: clang-devel libBlocksRuntime-devel cmake
BuildRequires: libpthread_workqueue-devel libkqueue-devel
BuildRequires: gcc-c++ gnustep-corebase-devel

%description
libdispatch, aka Grand Central Dispatch (GCD) is Apple's
high-performance event-handling library, introduced in OS X Snow
Leopard. It provides asynchronous task queues, monitoring of file
descriptor read and write-ability, asynchronous I/O (for sockets and
regular files), readers-writer locks, parallel for-loops, sane signal
handling, periodic timers, semaphores and more.

%package devel
Summary: Development files for libdispatch-objc2
Group: Development/C++
Requires: %name = %EVR

%description devel
libdispatch, aka Grand Central Dispatch (GCD) is Apple's
high-performance event-handling library, introduced in OS X Snow
Leopard. It provides asynchronous task queues, monitoring of file
descriptor read and write-ability, asynchronous I/O (for sockets and
regular files), readers-writer locks, parallel for-loops, sane signal
handling, periodic timers, semaphores and more.

This package contains development files for libdispatch-objc2.

%prep
%setup

%build
# Clang doesn't support these options
%remove_optflags -frecord-gcc-switches

%add_optflags -I%_includedir/kqueue
cd libdispatch
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DCMAKE_C_COMPILER:FILEPATH=%_bindir/clang \
	-DCMAKE_CXX_COMPILER:FILEPATH=%_bindir/clang++ \
	.

%make_build VERBOSE=1
 
%install
%makeinstall_std -C libdispatch

%if "%_libexecdir" != "%_libdir"
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/*.so* %buildroot%_libdir/
%endif

%files
%doc libdispatch/Readme.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_man3dir/*

%changelog
* Fri May 31 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2-alt5.git20140226
- Fixed build on 64-bit ppc architectures.

* Tue Jan 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt4.git20140226
- Removed unsupported compiler flags.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt3.git20140226.1
- (AUTO) subst_x86_64.

* Sun Mar 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3.git20140226
- New snapshot

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.svn20140108
- Use %_includedir/objc

* Wed Feb 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20140108
- Initial build for Sisyphus

