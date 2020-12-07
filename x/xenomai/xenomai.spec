# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_enable docs

Name: xenomai
Version: 3.1
Release: alt3
Summary: Real-Time Framework for Linux
License: GPL-2.0+ and LGPL-2.0+ and LGPL-2.1 and MIT
Group: System/Kernel and hardware
Url: http://www.xenomai.org
Vcs: https://gitlab.denx.de/Xenomai/xenomai.git

Source0: %name-%version.tar
ExclusiveArch: x86_64
BuildRequires: banner
BuildRequires: libiniparser-devel
%if_enabled docs
BuildRequires: doxygen asciidoc asciidoc-a2x w3m
%endif

%description
Xenomai is a Free Software project in which engineers from a wide
background collaborate to build a versatile real-time framework for
the Linux platform.

The main project goal is to help migrating industrial applications
from proprietary real-time systems to Linux.

Xenomai is about making various real-time operating system APIs
available to Linux-based platforms. When the target Linux kernel
cannot meet the requirements with respect to response time
constraints, Xenomai can also supplement it for delivering stringent
real-time guarantees based on an original dual kernel approach.

This package only contains top level wrapers (xeno and xeno-config),
you will need to install appropriate Cobalt or Mercury packages
to work.

%package cobalt
Summary: Real-Time Framework for Linux (Cobalt core)
Group: System/Kernel and hardware
Provides: xenomai-runtime = %EVR

%description cobalt
This package contains tools for dual kernel version of Xenomai
(codenamed Cobalt).
For these tools to work install kernel-image-xenomai package.

%package mercury
Summary: Real-Time Framework for Linux (Mercury core)
Group: System/Kernel and hardware

%description mercury
This package contains tools for native Linux kernel version of Xenomai
(called Mercury).
 It's recommended to install kernel-image-rt kernel.

%package -n libcobalt
Summary: Xenomai (Cobalt core) system libraries (v%version)
Group: System/Libraries
Obsoletes: libxenomai  < %EVR
Obsoletes: libxenomai1 < %EVR
Provides:  libxenomai1 = %EVR

%description -n libcobalt
System libraries for dual kernel Xenomai (Cobalt core).

%package -n libmercury
Summary: Xenomai (Mercury core) system libraries (v%version)
Group: System/Libraries

%description -n libmercury
System libraries for native kernel Xenomai (Mercury core).

%package devel-common
Summary: Common Xenomai development files (v%version)
Group: Development/C
Requires: xenomai = %EVR
AutoReqProv: nocpp

%description devel-common
Common development files (such as headers) for both Xenomai cores.

%package -n libcobalt-devel
Summary: Xenomai Cobalt development libraries (v%version)
Group: Development/C
Requires: xenomai-devel-common = %EVR
Requires: libcobalt = %EVR
Provides: libxenomai-dev = %EVR

%description -n libcobalt-devel
Development libraries for dual kernel Xenomai (Cobalt core).

%package -n libmercury-devel
Summary: Xenomai Mercury development libraries (v%version)
Group: Development/C
Requires: xenomai-devel-common = %EVR
Requires: libmercury = %EVR

%description -n libmercury-devel
Development libraries for native kernel Xenomai (Mercury core).

%package -n libcobalt-devel-static
Summary: Xenomai static libraries (Cobalt) (v%version)
Group: Development/C
Requires: libcobalt-devel = %EVR

%description -n libcobalt-devel-static
Static libraries for Xenomai (Cobalt)

%package -n libmercury-devel-static
Summary: Xenomai static libraries (Mercury) (v%version)
Group: Development/C
Requires: libmercury-devel = %EVR

%description -n libmercury-devel-static
Static libraries for Xenomai (Mercury)

%package kernel-source
Summary: Xenomai (Cobalt) patch for I-pipe kernel (v%version)
Group: Development/Kernel
BuildArch: noarch
AutoReqProv: no

%description kernel-source
This package is used only internally to build Xenomai dual kernel (Cobalt).

Cobalt supplements the native Linux kernel in dual kernel configurations.

It deals with all time-critical activities, such as handling interrupts, and
scheduling real-time threads. The Cobalt kernel has higher priority over all
the native kernel activities.

Cobalt provides an implementation of the POSIX and RTDM interfaces based on
a set of generic RTOS building blocks.

%package doc
Summary: Xenomai documentation
Group: Development/Documentation
BuildArch: noarch

%description doc
This package contains Xenomai documentation and code examples.

%package checkinstall
Summary: checkinstall tests for Xenomai
Group: Development/Other
Requires(pre): libcobalt-devel = %EVR
Requires(pre): libcobalt-devel-static = %EVR
Requires(pre): libmercury-devel = %EVR
Requires(pre): libmercury-devel-static = %EVR
Requires(pre): xenomai-doc = %EVR
Requires(pre): gcc

%description checkinstall
Run checkinstall tests for xenomai -devel packages.

%prep
%setup
# Do not git "update" the docs.
sed -Ei 's/gitdoc[[:space:]]?//' doc/Makefile.am
sed -i 's/mountkernfs/$local_fs/' debian/libxenomai1.xenomai.init

%define _configure_script ../configure
%build
%autoreconf
export CFLAGS=-fno-omit-frame-pointer
# --enable-smp is enabled by default on Cobalt, not on Mercury.

banner cobalt
mkdir COBALT
pushd COBALT
%configure \
        --with-core=cobalt \
              --bindir=%_libexecdir/xenomai/cobalt/bin \
             --sbindir=%_libexecdir/xenomai/cobalt/sbin \
        --with-testdir=%_libexecdir/xenomai/cobalt/testsuite \
        --with-demodir=%_libexecdir/xenomai/cobalt/demo \
          --includedir=%_includedir/xenomai \
        --enable-silent-rules \
        --enable-lazy-setsched \
        --enable-debug=symbols \
        --enable-dlopen-libs \
        %nil
%make_build --no-print-directory
popd

banner mercury
mkdir MERCURY
pushd MERCURY
%configure \
        --with-core=mercury \
              --bindir=%_libexecdir/xenomai/mercury/bin \
             --sbindir=%_libexecdir/xenomai/mercury/sbin \
        --with-testdir=%_libexecdir/xenomai/mercury/testsuite \
        --with-demodir=%_libexecdir/xenomai/mercury/demo \
          --includedir=%_includedir/xenomai \
        --enable-smp \
        --enable-silent-rules \
        --enable-debug=symbols \
        --enable-dlopen-libs \
%if_enabled docs
        --enable-doc-build \
%endif
        --enable-fortify \
        %nil
# Note: make install will rebuild docs due to some bug.
%make_build --no-print-directory
popd

%install
banner install
%makeinstall_std --no-print-directory -C COBALT  SUDO=false
mv %buildroot%_includedir/xenomai/xeno_config.h %buildroot%_includedir/xenomai/cobalt/

%makeinstall_std --no-print-directory -C MERCURY SUDO=false
mv %buildroot%_includedir/xenomai/xeno_config.h %buildroot%_includedir/xenomai/mercury/

# Install kernel sources.
mkdir -p %buildroot/usr/src/xenomai-kernel-source/config
cp -Ra  scripts \
        include \
        kernel  %buildroot/usr/src/xenomai-kernel-source/
cp config/version-{code,label} \
                %buildroot/usr/src/xenomai-kernel-source/config/

# udev rules for Xenomai kernel.
mkdir -p %buildroot/etc/udev/rules.d
for f in kernel/cobalt/udev/*.rules; do
  cp $f %buildroot/etc/udev/rules.d/
done

# Only .so is required for dlopen test
rm %buildroot%_libexecdir/xenomai/cobalt/testsuite/*.a

# Handmade wrapper for backward compatibility.
mkdir -p %buildroot/%_bindir
cp -a .gear/xeno-wrapper %buildroot/%_bindir/xeno
ln -s xeno %buildroot/%_bindir/xeno-config

mkdir -p %buildroot%_datadir/doc/xenomai
cp -a README %buildroot%_datadir/doc/xenomai/README

# Not requird.
rm %buildroot%_libexecdir/xenomai/mercury/bin/wrap-link.sh

# allowed_group setter.
install -D -p -m755 debian/libxenomai1.xenomai.init %buildroot%_initrddir/xenomai

# Some code examples to try.
cp -a demo %buildroot%_datadir/doc/xenomai/
find %buildroot%_datadir/doc/xenomai -name 'Makefile.*' -delete

%check
! test -e %buildroot/%_includedir/xenomai/xeno_config.h
grep '#define CONFIG_XENO_COBALT 1'  %buildroot%_includedir/xenomai/cobalt/xeno_config.h
grep '#define CONFIG_XENO_MERCURY 1' %buildroot%_includedir/xenomai/mercury/xeno_config.h
%buildroot%_libexecdir/xenomai/cobalt/sbin/version
%buildroot%_libexecdir/xenomai/mercury/sbin/version

%pre cobalt
# For udev rtdm.rules and allowed_group.
%_sbindir/groupadd -r -f xenomai 2> /dev/null ||:

%pre checkinstall
set -ex
OLDPATH=$PATH

# Build POSIX examples using Cobalt core.
PATH=/usr/lib/xenomai/cobalt/bin:$OLDPATH
cd /usr/share/doc/xenomai/demo/posix/cobalt
for skin in vxworks psos alchemy rtdm smokey posix cobalt; do
    for i in *.c; do
        gcc $i `xeno-config --$skin --cflags --ldflags`
        [ $skin = posix -o $skin = rtdm ] ||
        ldd a.out | grep lib$skin.so
        ldd a.out | grep libcobalt.so
        [ $skin = rtdm -o $skin = posix -o $skin = cobalt ] ||
        ldd a.out | grep libcopperplate.so
        gcc $i `xeno-config --$skin --cflags --ldflags` -static
    done
done

# Use Mercury core.
PATH=/usr/lib/xenomai/mercury/bin:$OLDPATH
for skin in vxworks psos alchemy rtdm smokey posix; do
    for i in *.c; do
        gcc $i `xeno-config --$skin --cflags --ldflags`
        [ $skin = posix -o $skin = rtdm ] ||
        ldd a.out | grep lib$skin
        ldd a.out | grep libmercury.so
        [ $skin = rtdm -o $skin = posix -o $skin = cobalt ] ||
        ldd a.out | grep libcopperplate_mercury.so
        gcc $i `xeno-config --$skin --cflags --ldflags` -static
    done
done

# Build cyclictest with Mercury core.
cd /usr/share/doc/xenomai/demo/posix/cyclictest
gcc *.c `xeno-config --posix --cflags --ldflags` -pthread -lrt -DVERSION_STRING=1.0
ldd a.out | grep libmercury.so
gcc *.c `xeno-config --posix --cflags --ldflags` -pthread -lrt -DVERSION_STRING=1.0 -static

# Build Alchemy demo.
PATH=$OLDPATH
cd /usr/share/doc/xenomai/demo/alchemy
gcc altency.c `/usr/lib/xenomai/mercury/bin/xeno-config --alchemy --cflags --ldflags` -lm
cd cobalt
gcc cross-link.c `/usr/lib/xenomai/mercury/bin/xeno-config --alchemy --cflags --ldflags`
ldd a.out | grep mercury
gcc cross-link.c `/usr/lib/xenomai/cobalt/bin/xeno-config  --alchemy --cflags --ldflags`
ldd a.out | grep cobalt
find /usr/share/doc/xenomai/demo -name a.out -delete

%files
# Common non-devel (tools) package.
# Wrappers that can guide user to install other packages.
%_bindir/xeno
%_bindir/xeno-config
%if_enabled docs
%_man1dir/xeno.1*
%endif

%files cobalt
%exclude %_libexecdir/xenomai/cobalt/bin/xeno-config
%exclude %_libexecdir/xenomai/cobalt/bin/wrap-link.sh
%dir %_libexecdir/xenomai
%_libexecdir/xenomai/cobalt
/etc/*.conf
/etc/udev/rules.d/*.rules
%_initrddir/xenomai
%if_enabled docs
%exclude %_man1dir/xeno.1*
%exclude %_man1dir/xeno-config.1*
%_man1dir/*.1*
%endif

%files mercury
%exclude %_libexecdir/xenomai/mercury/bin/xeno-config
%dir %_libexecdir/xenomai
%_libexecdir/xenomai/mercury

%files -n libcobalt
%exclude %_libdir/*mercury*
%_libdir/lib*.so.*

%files -n libmercury
%_libdir/lib*mercury*.so.*

%files devel-common
# Common -devel package.
# For bootstrap.o & bootstrap-pic.o
%_libdir/xenomai
%_libdir/dynlist.ld
%exclude %_includedir/xenomai/cobalt
%exclude %_includedir/xenomai/mercury
%_includedir/xenomai
%dir %_libexecdir/xenomai
%if_enabled docs
%_man1dir/xeno-config.1*
%endif

%files -n libcobalt-devel
%dir %_libexecdir/xenomai/cobalt
%dir %_libexecdir/xenomai/cobalt/bin
%_libexecdir/xenomai/cobalt/bin/xeno-config
%_libexecdir/xenomai/cobalt/bin/wrap-link.sh
%exclude %_libdir/*mercury*.so
%_libdir/lib*.so
%_libdir/cobalt.wrappers
%_libdir/modechk.wrappers
%_includedir/xenomai/cobalt

%files -n libmercury-devel
%dir %_libexecdir/xenomai/mercury
%dir %_libexecdir/xenomai/mercury/bin
%_libexecdir/xenomai/mercury/bin/xeno-config
%_libdir/lib*mercury*.so
%_includedir/xenomai/mercury

%files -n libcobalt-devel-static
%exclude %_libdir/*mercury*.a
%_libdir/lib*.a

%files -n libmercury-devel-static
%_libdir/lib*mercury*.a

%files kernel-source
%_usrsrc/xenomai-kernel-source

%files doc
# README, demo, pdf, html
%_datadir/doc/xenomai

%files checkinstall

%changelog
* Fri Dec 04 2020 Vitaly Chikunov <vt@altlinux.org> 3.1-alt3
- spec: Add Obsoletes for libxenomai (for p9), fixes RM#24461.

* Mon Sep 14 2020 Vitaly Chikunov <vt@altlinux.org> 3.1-alt2
- Multi-library (Cobalt and Mercury) package.
- Package docs (with demo, pdf, html).
- Add checkinstall tests.

* Sun Apr 19 2020 Vitaly Chikunov <vt@altlinux.org> 3.1-alt1
- Update to v3.1 (ABI r17).

* Sat Aug 24 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.9.0.9.ge71785fe0-alt1
- Update to v3.0.9-9-ge71785fe0.

* Fri Jun 28 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.8-alt3
- Add udev rules and groupadd.

* Thu Jun 27 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.8-alt2
- Make proper -devel package.

* Fri Jun 21 2019 Vitaly Chikunov <vt@altlinux.org> 3.0.8-alt1
- Update to 3.0.8.
- Add xenomai-kernel-source package

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.4.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jun 02 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Mon May 18 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.7-alt1
- Initial build for ALT.

