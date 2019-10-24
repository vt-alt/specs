%define kernel_base_version 5.3
%define kernel_source kernel-source-%kernel_base_version
%add_verify_elf_skiplist %_libexecdir/traceevent_%kernel_base_version/plugins/*
%add_findreq_skiplist %_datadir/perf_%kernel_base_version-core/tests/*.py

# from hv_kvp_daemon.c
%define kvp_config_loc /var/lib/hyperv
%define kvp_scripts_path /usr/libexec/hypervkvpd

Name: linux-tools
Version: %kernel_base_version
Release: alt1

Summary: Performance analysis tools for Linux
License: GPLv2
Group: Development/Tools
URL: http://www.kernel.org/

BuildRequires: libaudit-devel elfutils-devel perl-devel libslang2-devel bison flex binutils-devel asciidoc xmlto libssl-devel liblzma-devel libdw-devel
BuildRequires: libdw-devel
%ifnarch %arm
BuildRequires: libnuma-devel
%endif
BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): rpm-macros-alternatives
BuildRequires: %kernel_source = 1.0.0
BuildRequires: python-devel
BuildRequires: readline-devel
# python-module-docutils is just for rst2man
BuildRequires: python-module-docutils
# python3 is just for scripts/bpf_helpers_doc.py
BuildRequires: python3

Patch1: linux-tools-alt.patch
Patch2: python-linking.patch

AutoReq: yes,noperl,nopython
AutoProv: yes,noperl,nopython

# Sources for hyperv-daemon
Source5: hv_get_dhcp_info.sh
Source6: hv_get_dns_info.sh
Source7: hv_set_ifconfig.sh
Source11: hypervkvpd.init
Source12: hypervvssd.init
Source13: hypervfcopyd.init
Source21: hypervkvpd.service
Source22: hypervvssd.service
Source23: hypervfcopyd.service
Source31: hypervkvpd.rules
Source32: hypervvssd.rules
Source33: hypervfcopyd.rules

%package -n python-module-perf
Summary: Python bindings for apps which will manipulate perf events
Group: Development/Python
Provides: python-perf

%description
Performance counters for Linux are a new kernel-based subsystem that provide
a framework for all things performance analysis. It covers hardware level
(CPU/PMU, Performance Monitoring Unit) features and software features
(software counters, tracepoints) as well.
This package contains performance analysis tools for Linux

%description -n python-module-perf
The python-perf package contains a module that permits applications
written in the Python programming language to use the interface
to manipulate perf events.

# cpupower packages
%package -n cpupower
Summary: Linux kernel tool to examine and tune power saving related features of your processor
Group: System/Kernel and hardware
BuildRequires: libpci-devel
Requires: libcpupower = %version-%release
Provides: cpufrequtils = 009-%release
Obsoletes: cpufrequtils < 009-%release

%description -n cpupower
This package contains the tools/power directory from the kernel source
and the supporting document

%package -n libcpupower
Summary: Library for cpupower
License: GPLv2
Group: System/Libraries

Conflicts: cpupower < %version-%release

%description -n libcpupower
This packages contains some library needed by cpupower.

%package -n libcpupower-devel
Summary: Development files for cpupower
Group: Development/C
Requires: libcpupower = %version-%release
Provides: cpupower-devel = %version-%release
Obsoletes: cpupower-devel < %version-%release

%description -n libcpupower-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

# hyperv-daemon packages
%package -n hyperv-daemons
Summary: HyperV daemons suite
Group: Emulators
Requires: hypervkvpd = %version-%release
Requires: hypervvssd = %version-%release
Requires: hypervfcopyd = %version-%release

%description -n hyperv-daemons
Suite of daemons that are needed when Linux guest
is running on Windows Host with HyperV.

%package -n hypervkvpd
Summary: HyperV key value pair (KVP) daemon
Group: Emulators
Provides: hv_kvp_daemon

%description -n hypervkvpd
Hypervkvpd is an implementation of HyperV key value pair (KVP)
functionality for Linux. The daemon first registers with the
kernel driver. After this is done it collects information
requested by Windows Host about the Linux Guest. It also supports
IP injection functionality on the Guest.


%package -n hypervvssd
Summary: HyperV VSS daemon
Group: Emulators
Provides: hv_vss_daemon

%description -n hypervvssd
Hypervvssd is an implementation of HyperV VSS functionality
for Linux. The daemon is used for host initiated guest snapshot
on HyperV hypervisor. The daemon first registers with the
kernel driver. After this is done it waits for instructions
from Windows Host if to "freeze" or "thaw" the filesystem
on the Linux Guest.

%package -n hypervfcopyd
Summary: HyperV host to guest copy functionality daemon
Group: Emulators
Provides: hv_fcopy_daemon

%description -n hypervfcopyd
Hypervfcopyd is an mplementation of host to guest copy.
functionality for Linux.

%package -n bpftool
Summary: Inspection and simple manipulation of eBPF programs and maps
Group: Development/Tools

%description -n bpftool
This package contains the bpftool, which allows inspection and simple
manipulation of eBPF programs and maps.

%prep
%setup -cT
tar -xf %kernel_src/%kernel_source.tar
cd %kernel_source
%patch1 -p1
%patch2 -p1

%build
# Build perf
pushd %kernel_source/tools/perf
sed -i 's|\(perfexecdir[[:blank:]]*=[[:blank:]]*\).*$|\1share/perf_%kernel_base_version-core|' Makefile.config
sed -i 's|\(plugindir[[:blank:]]*=[[:blank:]]*\).*$|\1%_libexecdir/traceevent_%kernel_base_version/plugins|' Makefile.config
sed -i 's|\(STRACE_GROUPS_DIR[[:blank:]]*=[[:blank:]]*\).*$|\1share/perf_%kernel_base_version-core/strace/groups|' Makefile.config
%make_build VERSION=%kernel_base_version \
     VF=1 \
     WERROR=0 \
     NO_GTK2=1 \
     PYTHON=python2 \
     PYTHON_CONFIG=python2-config
popd

# build bpftool
%make_build -C %kernel_source/tools/bpf/bpftool

# Build cpupower
chmod +x %kernel_source/tools/power/cpupower/utils/version-gen.sh
%make_build -C %kernel_source/tools/power/cpupower CPUFREQ_BENCH=false

%ifarch %ix86
    pushd %kernel_source/tools/power/cpupower/debug/i386
    %make_build centrino-decode powernow-k8-decode
    popd
%endif

%ifarch x86_64
    pushd %kernel_source/tools/power/cpupower/debug/x86_64
    %make_build centrino-decode powernow-k8-decode
    popd
%endif

%ifarch %ix86 x86_64
   pushd %kernel_source/tools/power/x86/x86_energy_perf_policy
   %make_build
   popd
   pushd %kernel_source/tools/power/x86/turbostat
   %make_build
   popd
%endif

# Build hyperv daemons
%ifarch %ix86 x86_64
make -C %kernel_source/tools hv
%endif

%install
# Install perf
pushd %kernel_source/tools/perf
make VERSION=%kernel_base_version \
     VF=1 \
     WERROR=0 \
     NO_GTK2=1 \
     PYTHON=python2 \
     PYTHON_CONFIG=python2-config \
     DESTDIR=%buildroot \
     prefix=%_prefix \
     install \
     install-man \
     install-python_ext

install -d -m 0755 %buildroot%_docdir/%name
install -m 0644 {CREDITS,design.txt,Documentation/examples.txt,Documentation/tips.txt} %buildroot%_docdir/%name/
popd

rm %buildroot/%_docdir/perf-tip/tips.txt
rmdir %buildroot/%_docdir/perf-tip

rename perf  perf_%kernel_base_version  %buildroot%_bindir/perf
rename trace trace_%kernel_base_version %buildroot%_bindir/trace
rename perf  perf_%kernel_base_version  %buildroot%_sysconfdir/bash_completion.d/perf
rename perf  perf_%kernel_base_version  %buildroot%_man1dir/perf*

find %buildroot%_sysconfdir/bash_completion.d \
	%buildroot%_datadir/perf_%kernel_base_version-core \
	%buildroot%_libexecdir/perf* \
	%buildroot%_docdir \
	-name bin -prune -o -type f \
	| xargs chmod a-x

make -C %kernel_source/tools/bpf/bpftool \
	DESTDIR=%buildroot \
	prefix=%_prefix \
	bash_compdir=%_sysconfdir/bash_completion.d/ \
	mandir=%_mandir \
	install \
	doc-install
# provided by man-pages
rm -f %buildroot/%_man7dir/bpf-helpers.*

# Make alternatives:
mkdir -p %buildroot%_altdir
cat <<'_EOF'_ > %buildroot%_altdir/%name
%_bindir/perf	%_bindir/perf_%kernel_base_version	20
%_bindir/trace	%_bindir/trace_%kernel_base_version	20
%_sysconfdir/bash_completion.d/perf	%_sysconfdir/bash_completion.d/perf_%kernel_base_version	20
_EOF_

# Add man alternatives:
pushd %buildroot%_man1dir
for file in *.1;do
alterfile=`echo $file|sed -e "s|_%kernel_base_version||"`
echo "%_man1dir/$alterfile.xz	%_man1dir/$file.xz	20" >> %buildroot%_altdir/%name
done
popd

# Install cpupower
%make -C %kernel_source/tools/power/cpupower DESTDIR=%buildroot libdir=%_libdir mandir=%_mandir CPUFREQ_BENCH=false install
rm -f %buildroot%_libdir/*.{a,la}
%find_lang cpupower

%ifarch %ix86
    pushd %kernel_source/tools/power/cpupower/debug/i386
    install -m755 centrino-decode %buildroot%_bindir/centrino-decode
    install -m755 powernow-k8-decode %buildroot%_bindir/powernow-k8-decode
    popd
%endif

%ifarch x86_64
    pushd %kernel_source/tools/power/cpupower/debug/x86_64
    install -m755 centrino-decode %buildroot%_bindir/centrino-decode
    install -m755 powernow-k8-decode %buildroot%_bindir/powernow-k8-decode
    popd
%endif

%ifarch %ix86 x86_64
   mkdir -p %buildroot%_mandir/man8
   pushd %kernel_source/tools/power/x86/x86_energy_perf_policy
   make DESTDIR=%buildroot install
   popd
   pushd %kernel_source/tools/power/x86/turbostat
   make DESTDIR=%buildroot install
   popd
%endif

# Install hyperv daemons
%ifarch %ix86 x86_64
#make -C %kernel_source/tools hv_install
pushd %kernel_source/tools/hv

mkdir -p %buildroot%_sbindir
install -p -m 0755 hv_kvp_daemon %buildroot%_sbindir/hypervkvpd
install -p -m 0755 hv_vss_daemon %buildroot%_sbindir/hypervvssd
install -p -m 0755 hv_fcopy_daemon %buildroot%_sbindir/hypervfcopyd

popd

mkdir -p %buildroot%kvp_scripts_path
mkdir -p %buildroot%kvp_config_loc
# Shell scripts for the KVP daemon
install -p -m 0755 %SOURCE5 %buildroot%kvp_scripts_path/hv_get_dhcp_info
install -p -m 0755 %SOURCE6 %buildroot%kvp_scripts_path/hv_get_dns_info
install -p -m 0755 %SOURCE7 %buildroot%kvp_scripts_path/hv_set_ifconfig

# SysV init scripts
mkdir -p %buildroot%_initdir
install -p -m 0755 %SOURCE11 %buildroot%_initdir/hypervkvpd
install -p -m 0755 %SOURCE12 %buildroot%_initdir/hypervvssd
install -p -m 0755 %SOURCE13 %buildroot%_initdir/hypervfcopyd

# Systemd unit file
mkdir -p %buildroot%_unitdir
install -p -m 0644 %SOURCE21 %buildroot%_unitdir/hypervkvpd.service
install -p -m 0644 %SOURCE22 %buildroot%_unitdir/hypervvssd.service
install -p -m 0644 %SOURCE23 %buildroot%_unitdir/hypervfcopyd.service

# udev rules
mkdir -p %buildroot%_udevrulesdir
install -p -m 0644 %SOURCE31 %buildroot%_udevrulesdir/hypervkvpd.rules
install -p -m 0644 %SOURCE32 %buildroot%_udevrulesdir/hypervvssd.rules
install -p -m 0644 %SOURCE33 %buildroot%_udevrulesdir/hypervfcopyd.rules

# Directory for pool files
mkdir -p %buildroot%_sharedstatedir/hyperv
%endif

%post -n hypervkvpd
# auto enable service for Hyper-V guest
if [ $1 -eq 1 ]; then
    board_vendor=
    product_name=
    [ -r /sys/class/dmi/id/board_vendor ] && board_vendor="`cat /sys/class/dmi/id/board_vendor`"
    [ -r /sys/class/dmi/id/product_name ] && board_vendor="`cat /sys/class/dmi/id/product_name`"

    if test "${board_vendor}" = "Microsoft Corporation" -a "${product_name}" = "Virtual Machine"; then
	echo "Enabling hypervkvpd on '${product_name}' from '${board_vendor}'"
	chkconfig hypervkvpd on
    fi
fi
%post_service hypervkvpd

%preun -n hypervkvpd
%preun_service hypervkvpd

%post -n hypervvssd
if [ $1 -eq 1 ]; then
    board_vendor=
    product_name=
    [ -r /sys/class/dmi/id/board_vendor ] && board_vendor="`cat /sys/class/dmi/id/board_vendor`"
    [ -r /sys/class/dmi/id/product_name ] && board_vendor="`cat /sys/class/dmi/id/product_name`"

    if test "${board_vendor}" = "Microsoft Corporation" -a "${product_name}" = "Virtual Machine"; then
	echo "Enabling hypervvssd on '${product_name}' from '${board_vendor}'"
	chkconfig hypervvssd on
    fi
fi
%post_service hypervvssd

%preun -n hypervvssd
%preun_service hypervvssd

%post -n hypervfcopyd
%post_service hypervfcopyd

%preun -n hypervfcopyd
%preun_service hypervfcopyd

%files
%_altdir/%name
%_bindir/perf_%kernel_base_version
%_bindir/trace_%kernel_base_version
%_man1dir/perf*
%_sysconfdir/bash_completion.d/perf_%kernel_base_version
%_libexecdir/traceevent_%kernel_base_version
%_libexecdir/perf
%_datadir/perf_%kernel_base_version-core
%doc %_docdir/%name

%files -n python-module-perf
%python_sitelibdir/perf*

# files cpupower
%files -n cpupower -f cpupower.lang
%_bindir/cpupower
%_man1dir/cpupower*
%ifarch %ix86 x86_64
%_man8dir/turbostat*
%_man8dir/x86_energy_perf_policy*
%_bindir/centrino-decode
%_bindir/powernow-k8-decode
%_bindir/x86_energy_perf_policy
%_bindir/turbostat
%endif

%files -n libcpupower
%_libdir/libcpupower.so.*

%files -n libcpupower-devel
%_libdir/libcpupower.so
%_includedir/cpu*.h

# files hyperv daemons
%ifarch %ix86 x86_64
%files -n hyperv-daemons
# the base package does not contain any files.

%files -n hypervkvpd
%_sbindir/hypervkvpd
%dir %kvp_config_loc
%dir %kvp_scripts_path
%kvp_scripts_path/*
%_initdir/hypervkvpd
%_unitdir/hypervkvpd.service
%_udevrulesdir/hypervkvpd.rules
%dir %_sharedstatedir/hyperv

%files -n hypervvssd
%_sbindir/hypervvssd
%_initdir/hypervvssd
%_unitdir/hypervvssd.service
%_udevrulesdir/hypervvssd.rules

%files -n hypervfcopyd
%_sbindir/hypervfcopyd
%_initdir/hypervfcopyd
%_unitdir/hypervfcopyd.service
%_udevrulesdir/hypervfcopyd.rules
%endif

%files -n bpftool
%_sbindir/bpftool
%_sysconfdir/bash_completion.d/bpftool
%_man8dir/bpftool*

%changelog
* Wed Oct 23 2019 Alexey Shabalin <shaba@altlinux.org> 5.3-alt1
- Update for 5.3
- fixed sysvinit scripts

* Tue May 21 2019 Vitaly Chikunov <vt@altlinux.org> 5.1-alt1
- Add /usr/lib/perf to perf
- Clean up .spec (fix warnings, remove duplicated files)
- Build and provide bpftool
- Use kernel-source-5.1
- Simplify linux-tools-alt.patch
- Switch from libunwind to libdw

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.19-alt1.1
- rebuild with new perl 5.28.1

* Wed Nov 21 2018 Alexey Shabalin <shaba@altlinux.org> 4.19-alt1
- Update for kernel-4.19

* Mon Feb 19 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.15-alt2
- fixed spec for non-x86 arches

* Wed Feb 07 2018 Alexey Shabalin <shaba@altlinux.ru> 4.15-alt1
- Update for kernel-4.15
- absorb cpupower package
- absorb hyperv-daemons package

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.12-alt2.1
- rebuild with new perl 5.26.1

* Wed Aug  2 2017 Terechkov Evgenii <evg@altlinux.org> 4.12-alt2
- Build exclusively for x86_64 for now, waiting for upstream fix...

* Thu Jul 13 2017 Terechkov Evgenii <evg@altlinux.org> 4.12-alt1
- Update for kernel-4.12

* Wed Mar 29 2017 Terechkov Evgenii <evg@altlinux.org> 4.10-alt1
- Update for kernel-4.10
- Fix minor repocop warning about python-dev

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt4
- Add python-module-perf subpackage

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt3
- Add patch2 to linking python

* Wed Feb  8 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt2
- Build with python support

* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 4.9-alt1.1
- rebuild with new perl 5.24.1

* Fri Feb  3 2017 Terechkov Evgenii <evg@altlinux.org> 4.9-alt1
- Update for kernel-4.9

* Wed Oct 19 2016 Terechkov Evgenii <evg@altlinux.org> 4.7-alt1
- Clone package from linux-tools-4.4
- TODO: build with python support

* Thu Jan 28 2016 Terechkov Evgenii <evg@altlinux.org> 4.4-alt1
- Clone package from linux-tools-4.3

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov  4 2015 Terechkov Evgenii <evg@altlinux.org> 4.3-alt1
- Clone package from linux-tools-4.2

* Sat Oct 10 2015 Terechkov Evgenii <evg@altlinux.org> 4.2-alt1
- Clone package from linux-tools-4.1

* Fri Oct  2 2015 Terechkov Evgenii <evg@altlinux.org> 4.1-alt1
- Clone package from linux-tools-4.0

* Mon Jul 13 2015 Terechkov Evgenii <evg@altlinux.org> 4.0-alt2
- Return bin/trace (hardlink to bin/perf) for convience
- Additional alternatives (man1dir/bash_completion/trace)

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 4.0-alt1
- Clone package from linux-tools-3.14
- Rediffed patches

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt4
- Add tools-perf-install.patch from Debian

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt3
- Add basic alternatives support
- Make different kernel versions non-conflicting

* Sun Jul 12 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt2
- Add tool-perf-version.patch from Debian

* Sat Jul 11 2015 Terechkov Evgenii <evg@altlinux.org> 3.14-alt1
- Initial build for ALT Linux
