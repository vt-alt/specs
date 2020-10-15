%define module_name     ipt-so
%define module_version  1.0
%define module_release  alt7
%define flavour         std-def

%setup_kernel_module %flavour

%define module_dir /lib/modules/%kversion-%flavour-%krelease/misc

Summary: Iptables match for Security Options (IPSO) Labels (kernel module)
Name: kernel-modules-%module_name-%flavour
Version: %module_version
Release: %module_release.%kcode.%kbuildrelease
License: GPLv2
Group: System/Kernel and hardware
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>
Url: https://github.com/vt-alt/ipt-so/

BuildRequires(pre): rpm-build-kernel
BuildRequires(pre): kernel-headers-modules-std-def
%if 0%{?!_without_check:%{?!_disable_check:1}}
BuildRequires(pre): kernel-image-%flavour = %kepoch%kversion-%krelease
BuildRequires: rpm-build-kernel-perms make-initrd
BuildRequires: iptables iproute2 iptables-devel
%ifarch i586 x86_64
BuildRequires: qemu-system-x86-core /dev/kvm
%else
%def_without check
%endif
%endif
BuildRequires: kernel-headers-modules-%flavour = %kepoch%kversion-%krelease
BuildRequires: kernel-source-%module_name = %module_version

Requires: %module_name = %module_version
Provides: kernel-modules-%module_name-%kversion-%flavour-%krelease = %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease < %version-%release
Conflicts: kernel-modules-%module_name-%kversion-%flavour-%krelease > %version-%release
PreReq: kernel-image-%flavour = %kepoch%kversion-%krelease
ExclusiveArch: %ix86 x86_64 aarch64 ppc64le armh e2k e2kv4 e2kv5 e2kv6
ExclusiveOS: Linux

%description
Iptables match for Security Options (IPSO) Labels (kernel module).

%prep
rm -rf %module_name-%module_version
tar xf %kernel_src/kernel-source-%module_name-%module_version.tar*
%setup -D -T -n %module_name-%module_version

%build
make -C %_usrsrc/linux-%kversion-%flavour-%krelease M=$(pwd) modules VERSION=%version-%release
%{?!_without_check:%{?!_disable_check:make}}

%install
install -m644 -D xt_so.ko %buildroot/%module_dir/xt_so.ko

%files
%module_dir

%check
set -e
PATH=/sbin:/usr/sbin:$PATH
cd /usr/src
mkdir -p bin; echo echo 0 > bin/id; chmod a+x bin/id
install -D %buildroot/%module_dir/xt_so.ko /lib/modules/%kversion-%flavour-%krelease/extra/xt_so.ko
install -D /sbin/ip xroot/usr/bin/ip
install -D %_builddir/%module_name-%module_version/libxt_so.so xroot/%_lib/iptables/libxt_so.so
install -d xroot/sbin
cat > xroot/sbin/init-bin <<'EOF'
#!/bin/sh
export PATH=/sbin:/usr/sbin:/bin:/usr/bin
mount -t proc proc /proc
mount -t sysfs sysfs /sys
mount -t devtmpfs -o mode=755,size=5m devfs /dev
ip addr add 127.0.0.1/8 label lo dev lo
ip link set lo up
modprobe xt_so
cd /%module_name-%module_version
./tests.sh test && echo TEST-MARKER-OF-SUCCESS
/sbin/poweroff -f
EOF
chmod a+x xroot/sbin/init-bin

cat > config.mk <<'EOF'
  STATEDIR = /tmp
  IMAGEFILE = /usr/src/initramfs.$(ARCH).img
  FEATURES += add-modules
  DISABLE_GUESS += root fstab resume ucode rdshell keyboard
  DISABLE_FEATURES += buildinfo cleanup compress
  PUT_DIRS += /usr/src/RPM/BUILD
  PUT_DIRS += /usr/src/xroot
  PUT_PROGS += /sbin/iptables /sbin/iptables-save
  PUT_PROGS += /sbin/modinfo /sbin/insmod
  PUT_PROGS += /sbin/ip
  MODULES_ADD += xt_so iptable_filter iptable_security ip_tables
EOF
echo PUT_FILES += /%_lib/iptables/lib*.so >> config.mk
if [ -e /lib/modules/*/kernel/net/bpfilter/bpfilter.ko* ]; then
  # Required for iptables since v4.18
  echo MODULES_ADD += bpfilter >> config.mk
fi
make-initrd --no-checks --config=/usr/src/config.mk --kernel=%kversion-%flavour-%krelease
%ifarch i586
%define qemu qemu-system-i386
%endif
%ifarch x86_64
%define qemu qemu-system-x86_64
%endif
timeout 60 \
%qemu -kernel /boot/vmlinuz* -initrd /usr/src/initramfs.*.img \
	-m 512 -nographic -bios bios.bin -M accel=kvm:tcg \
	-append 'console=ttyS0 panic=-1 no_timer_check' 2>&1 | tr -d \\f | tee boot.log
egrep -q ' BUG:|Call Trace:|Kernel panic|Oops' boot.log && exit 1
grep -q TEST-MARKER-OF-SUCCESS boot.log || exit 1

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Build for kernel-image-%flavour-%kversion-%krelease.
