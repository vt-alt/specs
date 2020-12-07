# SPDX-License-Identifier: GPL-2.0-or-later
%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec
%define tuneddir %_prefix/lib/tuned

Name: tuned
Version: 2.14.0
Release: alt2

Summary: A dynamic adaptive system tuning daemon

License: GPL-2.0-or-later
Group: System/Configuration/Hardware
Url: https://tuned-project.org/
Vcs: https://github.com/redhat-performance/tuned

# Source-url: https://github.com/redhat-performance/tuned/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: tuned.init
Source2: recommend.conf

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro
BuildRequires: desktop-file-utils
BuildRequires: asciidoctor
BuildRequires: python3-dev

Requires: virt-what
Requires: ethtool
Requires: hdparm
Requires: util-linux
Requires: polkit

# BuildRequires for 'make test'
BuildRequires: rpm-build-vm

%py3_use decorator
%py3_use pyudev
%py3_use configobj
#py3_use schedutils
#py3_use linux-procfs
#py3_use perf
%py3_use dbus
%py3_use pygobject3

%description
The tuned package contains a daemon that tunes system settings dynamically.
It does so by monitoring the usage of several system components periodically.
Based on that information components will then be put into lower or higher
power saving modes to adapt to the current usage. Currently only ethernet
network and ATA harddisk devices are implemented.

%package gtk
Summary: GTK GUI for tuned
Group: System/Configuration/Other
Requires: %name = %EVR
Requires: powertop polkit

%description gtk
GTK GUI that can control tuned and provides simple profile editor.

%package utils
Group: System/Configuration/Other
Requires: %name = %EVR
Requires: powertop
Summary: Various tuned utilities

%description utils
This package contains utilities that can help you to fine tune and
debug your system and manage tuned profiles.

%package utils-systemtap
Group: System/Configuration/Other
Summary: Disk and net statistic monitoring systemtap scripts
Requires: %name = %EVR
Requires: systemtap

%description utils-systemtap
This package contains several systemtap scripts to allow detailed
manual monitoring of the system. Instead of the typical IO/sec it collects
minimal, maximal and average time between operations to be able to
identify applications that behave power inefficient (many small operations
instead of fewer large ones).

%package profiles-sap
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to SAP NetWeaver loads
Requires: %name = %EVR

%description profiles-sap
Additional tuned profile(s) targeted to SAP NetWeaver loads.

%package profiles-mssql
Group: System/Configuration/Other
Summary: Additional tuned profile(s) for MS SQL Server
Requires: %name = %EVR

%description profiles-mssql
Additional tuned profile(s) for MS SQL Server.

%package profiles-oracle
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Oracle loads
Requires: %name = %EVR

%description profiles-oracle
Additional tuned profile(s) targeted to Oracle loads.

%package profiles-sap-hana
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to SAP HANA loads
Requires: %name = %EVR

%description profiles-sap-hana
Additional tuned profile(s) targeted to SAP HANA loads.

%package profiles-atomic
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Atomic
Requires: %name = %EVR

%description profiles-atomic
Additional tuned profile(s) targeted to Atomic host and guest.

%package profiles-realtime
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to realtime
Requires: %name = %EVR
Requires: tuna

%description profiles-realtime
Additional tuned profile(s) targeted to realtime.

%package profiles-nfv-guest
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Network Function Virtualization (NFV) guest
Requires: %name = %EVR
Requires: %name-profiles-realtime = %EVR
Requires: tuna

%description profiles-nfv-guest
Additional tuned profile(s) targeted to Network Function Virtualization (NFV) guest.

%package profiles-nfv-host
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Network Function Virtualization (NFV) host
Requires: %name = %EVR
Requires: %name-profiles-realtime = %EVR
Requires: tuna
#Recommends: tuned-profiles-nfv-host-bin

%description profiles-nfv-host
Additional tuned profile(s) targeted to Network Function Virtualization (NFV) host.

%package profiles-nfv
Group: System/Configuration/Other
Summary: Additional tuned profile(s) targeted to Network Function Virtualization (NFV)
Requires: %name = %EVR
Requires: %name-profiles-nfv-guest = %EVR
Requires: %name-profiles-nfv-host = %EVR

%description profiles-nfv
Additional tuned profile(s) targeted to Network Function Virtualization (NFV).

%package profiles-cpu-partitioning
Group: System/Configuration/Other
Summary: Additional tuned profile(s) optimized for CPU partitioning
Requires: %name = %EVR

%description profiles-cpu-partitioning
Additional tuned profile(s) optimized for CPU partitioning.

%package profiles-spectrumscale
Group: System/Configuration/Other
Summary: Additional tuned profile(s) optimized for IBM Spectrum Scale (GPFS)
Requires: %name = %EVR

%description profiles-spectrumscale
Additional tuned profile(s) optimized for IBM Spectrum Scale (formerly GPFS).

%package profiles-compat
Group: System/Configuration/Other
Summary: Additional tuned profiles mainly for backward compatibility with tuned 1.0
Requires: %name = %EVR

%description profiles-compat
Additional tuned profiles mainly for backward compatibility with tuned 1.0.
It can be also used to fine tune your system for specific scenarios.

%prep
%setup
# For systemd-boot kernel-install hook.
sed -i '/^KERNELINSTALLHOOKDIR =/s/\/usr\/lib/\/lib/' Makefile
sed -i '/^KERNEL_UPDATE_HOOK_FILE =/s/\/usr\/lib/\/lib/' tuned/consts.py

# Don't install systemtap docs.
rm doc/README.{utils,scomes}

# Fix grub paths.
grep -lr -e /boot/grub2 -e grub2- | xargs sed -i s/grub2/grub/g
sed -i '/^GRUB2_DEFAULT_ENV_FILE =/s/default\/grub/sysconfig\/grub2/' tuned/consts.py

# Ezport tuned_params variable for submenu(s).
echo 'echo "export tuned_params"' >> 00_tuned

# For recommend.
sed -i '/^SYSTEM_RELEASE_FILE/s/system-release-cpe/system-release/' tuned/consts.py
cp %SOURCE2 recommend.conf

%build
make html PYTHON=%__python3

%install
%makeinstall_std DOCDIR=%_docdir/%name
%__subst 's/\(dynamic_tuning[ \t]*=[ \t]*\).*/\10/' %buildroot%_sysconfdir/tuned/tuned-main.conf
%makeinstall_std DOCDIR=%_docdir/%name install-html

mkdir -p %buildroot%_datadir/tuned/grub2
mv %buildroot%_sysconfdir/grub.d/00_tuned %buildroot%_datadir/tuned/grub2/00_tuned

mkdir -p %buildroot%_logdir/tuned
touch %buildroot%_logdir/tuned/tuned.log

# ghost for persistent storage
mkdir -p %buildroot%_var/lib/tuned

cat << __EOF__ > %buildroot%_sysconfdir/tuned/active_profile
throughput-performance
__EOF__

mkdir -p %buildroot%_initdir
install -pDm755 %SOURCE1 %buildroot%_initdir/%name

mkdir -p %buildroot%_presetdir
echo "enable tuned.service" > %buildroot%_presetdir/30-tuned.preset

# Remove systemtap scripts that we don't support.
rm %buildroot%_sbindir/{diskdevstat,netdevstat,scomes,varnetload}
rm %buildroot%_man8dir/{diskdevstat,netdevstat,scomes,varnetload}.8*

# Remove cpu-partitioning files, they require Dracut.
rm %buildroot%_sysconfdir/tuned/cpu-partitioning-variables.conf
rm %buildroot%_man7dir/tuned-profiles-cpu-partitioning.7*
rm -rf %buildroot%tuneddir/cpu-partitioning

%check
[ -w /dev/kvm ] && vm-run make test

%post
%post_service %name

# convert active_profile from full path to name (if needed)
sed -i 's|.*/\([^/]\+\)/[^\.]\+\.conf|\1|' /etc/tuned/active_profile

# convert GRUB_CMDLINE_LINUX to GRUB_CMDLINE_LINUX_DEFAULT
if [ -r %_sysconfdir/sysconfig/grub2 ]; then
	sed -i 's/GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX \\$tuned_params"/GRUB_CMDLINE_LINUX_DEFAULT="$GRUB_CMDLINE_LINUX_DEFAULT \\$tuned_params"/' \
	  %_sysconfdir/sysconfig/grub2
fi

# conditional support for grub2, grub2 is not available on all architectures
# and tuned is noarch package, thus the following hack is needed
if [ -d %_sysconfdir/grub.d ]; then
	cp -a %_datadir/tuned/grub2/00_tuned %_sysconfdir/grub.d/00_tuned
fi

%preun
%preun_service %name
if [ $1 -eq 0 ] ; then
	# clear persistent storage
	rm -f %_var/lib/tuned/* || :
	# clear temporal storage
	rm -f /run/tuned/* || :
fi

%postun
if [ $1 -eq 0 ]; then
	rm -f %_sysconfdir/grub.d/00_tuned || :

	# unpatch /etc/default/grub
	if [ -r %_sysconfdir/sysconfig/grub2 ]; then
		sed -i '/GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT:+$GRUB_CMDLINE_LINUX_DEFAULT }\\$tuned_params"/d' \
		  %_sysconfdir/sysconfig/grub2
	fi
	# cleanup for Boot loader specification (BLS)

	# clear grubenv variables
	GRUBEDITENV=grub-editenv
	$GRUBEDITENV - unset tuned_params tuned_initrd &>/dev/null || :

	# unpatch BLS entries
	MACHINE_ID=`cat /etc/machine-id 2>/dev/null`
	if [ "$MACHINE_ID" ]; then
		for f in /boot/loader/entries/$MACHINE_ID-*.conf; do
			if [ -f "$f" -a "${f: -12}" != "-rescue.conf" ]; then
				sed -i '/^\s*options\s\+.*\$tuned_params/ s/\s\+\$tuned_params\b//g' "$f" &>/dev/null || :
				sed -i '/^\s*initrd\s\+.*\$tuned_initrd/ s/\s\+\$tuned_initrd\b//g' "$f" &>/dev/null || :
			fi
		done
	fi
fi

%files
%exclude %_docdir/%name/README.*
%doc %_docdir/%name
/lib/kernel/install.d/92-tuned.install
%_datadir/bash-completion/completions/tuned-adm
%exclude %python3_sitelibdir/tuned/gtk
%python3_sitelibdir/tuned
%_sbindir/tuned
%_sbindir/tuned-adm
%exclude %_sysconfdir/tuned/realtime*variables.conf
%dir %_sysconfdir/tuned/
%dir %_libexecdir/%name/
%dir %tuneddir/
%tuneddir/balanced/
%tuneddir/desktop/
%tuneddir/functions/
%tuneddir/hpc-compute/
%tuneddir/latency-performance/
%tuneddir/network-latency/
%tuneddir/network-throughput/
%tuneddir/powersave/
%tuneddir/recommend.d/
%tuneddir/intel-sst/
%tuneddir/throughput-performance/
%tuneddir/virtual-guest/
%tuneddir/virtual-host/
%tuneddir/accelerator-performance/
%tuneddir/optimize-serial-console/

%config(noreplace) %_sysconfdir/tuned/active_profile
%config(noreplace) %_sysconfdir/tuned/tuned-main.conf
%config(noreplace) %_sysconfdir/tuned/profile_mode
%config(noreplace) %_sysconfdir/tuned/bootcmdline
%config(noreplace) %_sysconfdir/tuned/post_loaded_profile
%_sysconfdir/dbus-1/system.d/com.redhat.tuned.conf
%_sysconfdir/modprobe.d/tuned.conf
%_tmpfilesdir/tuned.conf
%_unitdir/tuned.service
%_presetdir/*tuned.preset
%_initdir/tuned
%dir %_logdir/tuned
%ghost %_logdir/tuned/tuned.log
%_man5dir/tuned*
%_man7dir/tuned-profiles.7*
%_man8dir/tuned*
%dir %_datadir/tuned
%_datadir/tuned/grub2
%_datadir/polkit-1/actions/com.redhat.tuned.policy
%_libexecdir/tuned/defirqaffinity*

%files gtk
%_sbindir/tuned-gui
%python3_sitelibdir/tuned/gtk
%_datadir/tuned/ui
#_datadir/polkit-1/actions/com.redhat.tuned.gui.policy
%_iconsdir/hicolor/scalable/apps/tuned.svg
%_desktopdir/tuned-gui.desktop

%files utils
%doc COPYING
%_bindir/powertop2tuned
%_libexecdir/%name/pmqos-static*

# tuned-utils-systemtap#2.13.0-alt1    /usr/bin/stap
# tuned-utils-systemtap#2.13.0-alt1    systemtap
%if 0
%files utils-systemtap
%doc doc/%name/README.utils
%doc doc/%name/README.scomes
#doc COPYING
%_sbindir/varnetload
%_sbindir/netdevstat
%_sbindir/diskdevstat
%_sbindir/scomes
%_man8dir/varnetload.*
%_man8dir/netdevstat.*
%_man8dir/diskdevstat.*
%_man8dir/scomes.*
%endif

%files profiles-sap
%tuneddir/sap-netweaver
%_man7dir/tuned-profiles-sap.7*

%files profiles-sap-hana
%tuneddir/sap-hana
%_man7dir/tuned-profiles-sap-hana.7*

%files profiles-mssql
%tuneddir/mssql
%_man7dir/tuned-profiles-mssql.7*

%files profiles-oracle
%tuneddir/oracle
%_man7dir/tuned-profiles-oracle.7*

%files profiles-atomic
%tuneddir/atomic-host
%tuneddir/atomic-guest
%_man7dir/tuned-profiles-atomic.7*

%files profiles-realtime
%config(noreplace) %_sysconfdir/tuned/realtime-variables.conf
%tuneddir/realtime
%_man7dir/tuned-profiles-realtime.7*

# Requires rt-entsk from rt-setup
%files profiles-nfv-guest
%config(noreplace) %_sysconfdir/tuned/realtime-virtual-guest-variables.conf
%tuneddir/realtime-virtual-guest
%_man7dir/tuned-profiles-nfv-guest.7*

%files profiles-nfv-host
%config(noreplace) %_sysconfdir/tuned/realtime-virtual-host-variables.conf
%tuneddir/realtime-virtual-host
%_man7dir/tuned-profiles-nfv-host.7*

%files profiles-nfv
%doc %_docdir/%name/README.NFV

# tuned-profiles-cpu-partitioning#2.13.0-alt1    /lib/dracut-lib.sh
%if 0
%files profiles-cpu-partitioning
%config(noreplace) %_sysconfdir/tuned/cpu-partitioning-variables.conf
%tuneddir/cpu-partitioning
%_man7dir/tuned-profiles-cpu-partitioning.7*
%endif

%files profiles-spectrumscale
%tuneddir/spectrumscale-ece
%_man7dir/tuned-profiles-spectrumscale-ece.7*

%files profiles-compat
%tuneddir/default
%tuneddir/desktop-powersave
%tuneddir/laptop-ac-powersave
%tuneddir/server-powersave
%tuneddir/laptop-battery-powersave
%tuneddir/enterprise-storage
%tuneddir/spindown-disk
%_man7dir/tuned-profiles-compat.7*

%changelog
* Tue Nov 10 2020 Vitaly Chikunov <vt@altlinux.org> 2.14.0-alt2
- ALT specific profile recommend.

* Sun Oct 04 2020 Vitaly Chikunov <vt@altlinux.org> 2.14.0-alt1
- Update to 2.14.0.
- Enable realtime profiles.
- Add systemd-boot kernel-install hook.
- spec: Cleanup and enable %%check section.
- Add grub integration.

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 2.13.0-alt1
- sync spec with Fedora's one
- build with python3 only

* Mon Feb 27 2017 Michael Shigorin <mike@altlinux.org> 2.7.1-alt2
- added sysv initscript

* Thu Dec 29 2016 Valery Inozemtsev <shrek@altlinux.ru> 2.7.1-alt1
- initial release

