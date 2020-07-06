%def_enable watchdog
%def_enable monitoring
%def_enable snmp
%def_enable dbus
%def_enable systemd
%def_enable xmlconf
%def_enable augeas
%def_enable nozzle
%def_enable vqsim
%define _localstatedir %_var

Name: corosync
Version: 3.0.4
Release: alt2
Summary: The Corosync Cluster Engine and Application Programming Interfaces
License: BSD
Group: System/Base

Url: http://corosync.github.io/corosync/

# https://github.com/corosync/corosync.git
Source0: %name-%version.tar
Source1: corosync-init
Source2: corosync-notifyd-init

# fixed systemd units
Source11: corosync.service

Provides: corosync2 = %version-%release
Obsoletes: corosync2 < %version-%release
Requires: lib%name = %version-%release
# NSS crypto plugin should be always installed
Requires: libknet1-crypto-nss-plugin

BuildRequires: doxygen libqb-devel graphviz libsocket-devel zlib-devel libknet-devel
%{?_enable_monitoring:BuildRequires: libstatgrab-devel}
%{?_enable_snmp:BuildRequires: libnet-snmp-devel}
%{?_enable_dbus:BuildRequires: libdbus-devel}
%{?_enable_nozzle:BuildRequires: libnozzle-devel}
%{?_enable_systemd:BuildRequires: systemd-devel}
%{?_enable_xmlconf:BuildRequires: libxslt-devel}
%{?_enable_augeas:BuildRequires: augeas libaugeas-devel}
%{?_enable_vqsim:BuildRequires: libreadline-devel}

%description
This package contains the Corosync Cluster Engine Executive, several
default APIs and libraries, default configuration files, and an init
script.

%package -n lib%name
Summary: The Corosync Cluster Engine Libraries
Group: System/Libraries
Conflicts: libcorosync
Provides: libcorosync2 = %version-%release
Obsoletes: libcorosync2 < %version-%release

%description -n lib%name
This package contains corosync libraries.

%package -n lib%name-devel
Summary: The Corosync Cluster Engine Development Kit
Group: Development/C
Requires: lib%name = %version-%release
Provides: libcorosync2-devel = %version-%release
Obsoletes: libcorosync2-devel < %version-%release

%description -n lib%name-devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%package vqsim
Summary: The Corosync Cluster Engine - Votequorum Simulator
Group: System/Base

%description vqsim
A command-line simulator for the corosync votequorum subsystem.
It uses the same code as the corosync quorum system but forks
them into subprocesses to simulate nodes.
Nodes can be added and removed as well as partitioned (to simulate
network splits)

%prep
%setup

echo %version > .version
#if release version (= tarball)
#in checked-out repository it uses git describe
cp .version .tarball-version
mkdir -p m4

%build
%autoreconf

%configure \
	%{subst_enable watchdog} \
	%{subst_enable monitoring} \
	%{subst_enable snmp} \
	%{subst_enable dbus} \
	%{subst_enable systemd} \
	%{subst_enable xmlconf} \
	%{subst_enable augeas} \
	%{subst_enable nozzle} \
	%{subst_enable vqsim} \
	--with-systemddir=%_unitdir

%make_build

%install
%makeinstall_std
%makeinstall_std -C init
touch %buildroot%_sysconfdir/corosync/corosync.conf
%if_enabled dbus
install -p -D -m644 %_builddir/%name-%version/conf/corosync-signals.conf %buildroot/%_sysconfdir/dbus-1/system.d/corosync-signals.conf
%endif

#Initscripts
install -p -D -m755 %SOURCE1 %buildroot%_initdir/corosync
install -p -D -m755 %SOURCE2 %buildroot%_initdir/corosync-notifyd

#fixed native systemd units
install -p -D -m644 %SOURCE11 %buildroot%_unitdir/corosync.service

## tree fixup
# drop static libs
rm -f %buildroot%_libdir/*.a
# drop docs and html docs for now
rm -rf %buildroot%_docdir/*

mkdir -p %buildroot%_sysconfdir/sysconfig

# /etc/sysconfig/corosync-notifyd
install -p -m 644 tools/corosync-notifyd.sysconfig.example %buildroot%_sysconfdir/sysconfig/corosync-notifyd
# /etc/sysconfig/corosync
install -p -m 644 init/corosync.sysconfig.example %buildroot%_sysconfdir/sysconfig/corosync

rm -f %buildroot%_sysconfdir/corosync/corosync.conf.example
ln -r -s \
    %buildroot%_defaultdocdir/%name-%version/corosync.conf.example \
    %buildroot%_sysconfdir/corosync/corosync.conf.example

%check
%make check

%post
%post_service corosync
%post_service corosync-notifyd

%preun
%preun_service corosync
%preun_service corosync-notifyd

%files
%doc AUTHORS README* LICENSE conf/corosync.conf.example
%_bindir/*
%_sbindir/*
%dir %_sysconfdir/corosync
%dir %_sysconfdir/corosync/service.d
%dir %_sysconfdir/corosync/uidgid.d
%ghost %config(noreplace) %_sysconfdir/corosync/corosync.conf
%_sysconfdir/corosync/corosync.conf.example
%config(noreplace) %_sysconfdir/sysconfig/corosync-notifyd
%config(noreplace) %_sysconfdir/sysconfig/corosync
%config(noreplace) %_logrotatedir/corosync
%_unitdir/corosync.service
%_unitdir/corosync-notifyd.service
%if_enabled dbus
%_sysconfdir/dbus-1/system.d/corosync-signals.conf
%endif
%_initrddir/corosync
%_initrddir/corosync-notifyd
%_datadir/corosync
%_datadir/snmp/mibs/COROSYNC-MIB.txt
%if_enabled augeas
%_datadir/augeas/lenses/*
%endif
%dir %_localstatedir/lib/corosync
%attr(750, root, adm) %_logdir/cluster
%_man5dir/*
%_man7dir/*
%_man8dir/*

%if_enabled vqsim
%exclude %_bindir/corosync-vqsim
%exclude %_man8dir/corosync-vqsim.8*
%endif

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/corosync
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%if_enabled vqsim
%files vqsim
%doc LICENSE
%_bindir/corosync-vqsim
%_man8dir/corosync-vqsim.8*
%endif

%changelog
* Thu May 14 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.4-alt2
- update systemd units

* Fri May 01 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.4-alt1
- 3.0.4

* Sat Apr 04 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.3.0.18.g89b0d-alt2
- package empty %%_sysconfdir/corosync/corosync.conf as %%ghost

* Wed Dec 18 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.3.0.18.g89b0d-alt1
- upstream snapshot 89b0d62f8bd9d5ba90db5a37866c029b821da838

* Tue Jul 23 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.2-alt3
- add libknet1-crypto-nss-plugin dependency

* Mon Jun 17 2019 Michael Shigorin <mike@altlinux.org> 3.0.2-alt2
- fix augeas knob
- minor spec cleanup

* Sun Jun 16 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.1-alt1
- 3.0.1

* Thu Jun 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt2
- Fixed build for new toolchain

* Wed Sep 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1
- rename to corosync

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1
- Version 2.3.4

* Mon Nov 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.2-alt1
- New version

* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.1-alt1
- New version

* Tue Feb 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.0-alt1
- New version

* Tue Sep 20 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.1-alt1
- Initial build (using Fedora spec)
