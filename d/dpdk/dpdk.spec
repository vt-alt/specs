# Add option to build as static libraries (--without shared)
%def_with shared
# Add option to build without examples
%def_with examples
# Add option to build without tools
%def_with tools
# Add option to build the PDF documentation separately (--with pdfdoc)
%def_without pdfdoc
%def_without doc

# build with Mellanox nic support
%def_with mlnx

%define sdkdir  %_libdir/%name
%define docdir  %_docdir/%name
%define incdir %_includedir/%name
%define pmddir %_libdir/%name-pmds


Name: dpdk
Version: 18.11.5
Release: alt1
Url: http://dpdk.org
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

Patch0: dpdk-16.11-move-to-libdir.patch
Patch1: dpdk-18.02-aarch64-link-fix.patch
Patch3: dpdk-alt-pci.ids.patch
Patch4: dpdk-18.11-fix-redefinition.patch
Patch5: dpdk-18.08-fix-build-on-ppc64le.patch

# fedora patches
Patch102: dpdk-rte-ether-align.patch

Summary: Set of libraries and drivers for fast packet processing
Group: System/Libraries

Provides: lib%{name} = %EVR
#
# Note that, while this is dual licensed, all code that is included with this
# Pakcage are BSD licensed. The only files that aren't licensed via BSD is the
# kni kernel module which is dual LGPLv2/BSD, and thats not built for fedora.
#
License: BSD and LGPLv2 and GPLv2

#
# The DPDK is designed to optimize througput of network traffic using, among
# other techniques, carefully crafted assembly instructions.  As such it
# needs extensive work to port it to other architectures.
#
ExclusiveArch: x86_64 %{ix86} aarch64 ppc64le

# machine_arch maps between rpm and dpdk arch name, often same as _target_cpu
# machine_tmpl is the config template machine name, often "native"
# machine is the actual machine name used in the dpdk make system
%ifarch x86_64
%define machine_arch x86_64
%define machine_tmpl native
%define machine default
%endif
%ifarch %{ix86}
%define machine_arch i686
%define machine_tmpl native
%define machine default
%endif
%ifarch aarch64
%define machine_arch arm64
%define machine_tmpl armv8a
%define machine armv8a
%endif
%ifarch ppc64le
%define machine_arch ppc_64
%define machine_tmpl power8
%define machine power8
%endif

%define target %machine_arch-%machine_tmpl-linuxapp-gcc
BuildRequires(pre): rpm-build-python3
BuildRequires: glibc-kernheaders libpcap-devel zlib-devel
BuildRequires: libnuma-devel
%{?_with_doc:BuildRequires: doxygen python-module-sphinx}
%{?_with_mlnx:BuildRequires: rdma-core-devel libmnl-devel}
%if_with pdfdoc
BuildRequires: texlive-dejavu inkscape texlive-latex-bin-bin
BuildRequires: texlive-kpathsea-bin texlive-metafont-bin texlive-cm
BuildRequires: texlive-cmap texlive-ec texlive-babel-english
BuildRequires: texlive-fancyhdr texlive-fancybox texlive-titlesec
BuildRequires: texlive-framed texlive-threeparttable texlive-mdwtools
BuildRequires: texlive-wrapfig texlive-parskip texlive-upquote texlive-multirow
BuildRequires: texlive-helvetic texlive-times texlive-dvips
%endif

%description
The Data Plane Development Kit is a set of libraries and drivers for
fast packet processing in the user space.

%package devel
Summary: Data Plane Development Kit development files
Group: System/Libraries
Requires: %name = %EVR
Provides: lib%{name}-devel = %EVR
%if_without shared
Provides: %name-static = %EVR
%endif

%description devel
This package contains the headers and other files needed for developing
applications with the Data Plane Development Kit.

%package doc
Summary: Data Plane Development Kit API documentation
Group: System/Libraries
BuildArch: noarch

%description doc
API programming documentation for the Data Plane Development Kit.

%package tools
Summary: Tools for setting up Data Plane Development Kit environment
Group: Development/Documentation
Requires: %name = %EVR
Requires: kmod pciutils findutils iproute
AutoReqProv: yes, nopython

%description tools
%summary

%package examples
Summary: Data Plane Development Kit example applications
Group: Development/Tools
BuildRequires: libvirt-devel

%description examples
Example applications utilizing the Data Plane Development Kit, such
as L2 and L3 forwarding.

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch3 -p2
#%patch4 -p2
%patch5 -p2

%patch102 -p1

%build
# set up a method for modifying the resulting .config file
function setconf() {
	if grep -q ^$1= %target/.config; then
		sed -i "s:^$1=.*$:$1=$2:g" %target/.config
	else
		echo $1=$2 >> %target/.config
	fi
}

# In case dpdk-devel is installed, we should ignore its hints about the SDK directories
unset RTE_SDK RTE_INCLUDE RTE_TARGET

# Avoid appending second -Wall to everything, it breaks upstream warning
# disablers in makefiles. Strip expclit -march= from optflags since they
# will only guarantee build failures, DPDK is picky with that.
export EXTRA_CFLAGS="$(echo %optflags | sed -e 's:-Wall::g' -e 's:-march=[[:alnum:]]* ::g') -Wformat -fPIC -I/etc/sysconfig/kernel/include"
%ifarch x86_64 i686
export EXTRA_CFLAGS="$EXTRA_CFLAGS -fcf-protection=full"
%endif

%make_build V=1 O=%target T=%target config

setconf CONFIG_RTE_MACHINE '"%machine"'
# Disable experimental features
setconf CONFIG_RTE_NEXT_ABI n
setconf CONFIG_RTE_LIBRTE_MBUF_OFFLOAD n
# Disable unmaintained features
setconf CONFIG_RTE_LIBRTE_POWER n

# Enable automatic driver loading from this path
setconf CONFIG_RTE_EAL_PMD_PATH '"%pmddir"'

setconf CONFIG_RTE_LIBRTE_BNX2X_PMD y
setconf CONFIG_RTE_LIBRTE_PMD_PCAP y
setconf CONFIG_RTE_LIBRTE_VHOST_NUMA y

setconf CONFIG_RTE_EAL_IGB_UIO n
setconf CONFIG_RTE_LIBRTE_KNI n
setconf CONFIG_RTE_KNI_KMOD n
setconf CONFIG_RTE_KNI_PREEMPT_DEFAULT n

setconf CONFIG_RTE_APP_EVENTDEV n

setconf CONFIG_RTE_LIBRTE_NFP_PMD y

%ifarch aarch64
setconf CONFIG_RTE_LIBRTE_DPAA_BUS n
setconf CONFIG_RTE_LIBRTE_DPAA_MEMPOOL n
setconf CONFIG_RTE_LIBRTE_DPAA_PMD n
%endif

%if_with shared
setconf CONFIG_RTE_BUILD_SHARED_LIB y
%endif

%if_with mlnx
setconf CONFIG_RTE_LIBRTE_MLX4_PMD y
setconf CONFIG_RTE_LIBRTE_MLX5_PMD y
%endif

%make_build V=1 O=%target
%if_with doc
%make_build V=1 O=%target doc-api-html doc-guides-html %{?with_pdfdoc: guides-pdf}
%endif

%if_with examples
%make_build V=1 O=%target/examples T=%target examples
%endif

%install
# In case dpdk-devel is installed
unset RTE_SDK RTE_INCLUDE RTE_TARGET

%makeinstall_std O=%target prefix=%_usr libdir=%_libdir

%if_without tools
rm -rf %buildroot%sdkdir/usertools
rm -rf %buildroot%_sbindir/dpdk_nic_bind
rm -f %buildroot%_bindir/dpdk-test-crypto-perf
rm -f %buildroot%_bindir/testbbdev
%else
mv %buildroot%_bindir/testbbdev %buildroot%_bindir/dpdk-test-bbdev
%endif
rm -f %buildroot%sdkdir/usertools/setup.sh
rm -f %buildroot%sdkdir/usertools/meson.build

%if_with examples
find %target/examples/ -name "*.map" | xargs rm -f
for f in %target/examples/*/%target/app/*; do
    bn=`basename ${f}`
    cp -p ${f} %buildroot%_bindir/dpdk_example_${bn}
done
%endif

# Replace /usr/bin/env python with /usr/bin/python3
find %buildroot%sdkdir/ -name "*.py" -exec \
  sed -i -e 's|#!\s*/usr/bin/env python|#!/usr/bin/python3|' {} +

# Create a driver directory with symlinks to all pmds
mkdir -p %buildroot/%pmddir
for f in %buildroot/%_libdir/*_pmd_*.so.*; do
    bn=$(basename ${f})
    ln -s ../${bn} %buildroot%pmddir/${bn}
done

# Setup RTE_SDK environment as expected by apps etc
mkdir -p %buildroot/%_sysconfdir/profile.d
cat << EOF > %buildroot/%_sysconfdir/profile.d/dpdk-sdk-%_arch.sh
if [ -z "\${RTE_SDK}" ]; then
    export RTE_SDK="%sdkdir"
    export RTE_TARGET="%target"
    export RTE_INCLUDE="%incdir"
fi
EOF

cat << EOF > %buildroot/%_sysconfdir/profile.d/dpdk-sdk-%_arch.csh
if (! -d \$?RTE_SDK ) then
    setenv RTE_SDK "%sdkdir"
    setenv RTE_TARGET "%target"
    setenv RTE_INCLUDE "%incdir"
endif
EOF

# Fixup target machine mismatch
sed -i -e 's:-%machine_tmpl-:-%machine-:g' %buildroot/%_sysconfdir/profile.d/dpdk-sdk*

%files
# BSD
%_bindir/testpmd
%_bindir/dpdk-procinfo
%if_with shared
%_libdir/*.so.*
%pmddir/
%endif

%if_with doc
%files doc
#BSD
%docdir
%endif

%files devel
#BSD
%incdir/
%sdkdir
%if_with tools
%exclude %sdkdir/usertools/
%endif
%if_with examples
%exclude %sdkdir/examples/
%endif
%_sysconfdir/profile.d/dpdk-sdk-*.*
%if_without shared
%_libdir/*.a
%else
%_libdir/*.so
%endif

%if_with tools
%files tools
%sdkdir/usertools/
%_sbindir/dpdk-devbind
%_bindir/dpdk-pdump
%_bindir/dpdk-pmdinfo
%_bindir/dpdk-test-bbdev
%_bindir/dpdk-test-crypto-perf
%endif

%if_with examples
%files examples
%_bindir/dpdk_example_*
%doc %sdkdir/examples
%endif

%changelog
* Fri Dec 27 2019 Alexey Shabalin <shaba@altlinux.org> 18.11.5-alt1
- Update to LTS release 18.11.5
- Rename testbbdev to dpdk-test-bbdev
- Fixed broken symlinks in %%pmddir

* Fri Nov 01 2019 Alexey Shabalin <shaba@altlinux.org> 18.11.3-alt1
- Update to latest LTS release 18.11.3

* Wed Jun 05 2019 Alexey Shabalin <shaba@altlinux.org> 18.11.1-alt1
- Update to latest LTS release 18.11.1
- switch to use python3

* Tue Mar 12 2019 Alexey Shabalin <shaba@altlinux.org> 18.11-alt1
- 18.11

* Wed Feb 13 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 18.08-alt2
- Fixed build on ppc64le (patch by Christian Ehrhardt).

* Tue Oct 30 2018 Alexey Shabalin <shaba@altlinux.org> 18.08-alt1
- 18.08
- build with Mellanox nic support

* Fri Jun 01 2018 Anton Farygin <rider@altlinux.ru> 18.02.1-alt1%ubt
- 18.02.1

* Wed Apr 26 2017 Alexey Shabalin <shaba@altlinux.ru> 16.11.1-alt1%ubt
- 16.11.1

* Thu Dec 08 2016 Lenar Shakirov <snejok@altlinux.ru> 16.11-alt1
- Initial build for ALT (based on 16.11-1.fc26.src)

