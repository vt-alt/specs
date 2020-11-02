%define _unpackaged_files_terminate_build 1

%def_disable debug
%def_enable syslog
%def_enable lfs
%def_disable sdp
%def_enable gznbd
%def_with setproctitle
%def_without  static_client

Name: nbd
Version: 3.20
Release: alt1
Summary: Network Block Device user space tools
License: GPL
Group: Networking/Other
URL: http://%name.sourceforge.net/

# https://github.com/NetworkBlockDevice/nbd.git
Source: %name-%version.tar

Source1: nbd.init
Source2: nbd-server.conf
Source3: nbd.service
Source4: nbd.sysconfig

Patch1: %name-alt.patch

BuildRequires: glib2-devel docbook-utils
%{?_with_setproctitle:BuildRequires: setproctitle-devel}
%{?_enable_gznbd:BuildRequires: zlib-devel}
%{?_with_static_client:BuildRequires: dietlibc}
%{?_enable_sdp:BuildRequires: libsdp-devel}

%description
Tools for the Linux Kernel's network block device, allowing you to use
remote block devices over a TCP/IP network.

%package doc
Summary: Network Block Device user space tools documentation
Group: Documentation
BuildArch: noarch

%description doc
This package contains basic documentation for Network Block Device
user space tools.

%package server
Summary: Network Block Device server
Group: Networking/Other
Requires: %name-doc = %EVR

%description server
This package contains nbd-server - a user space daemon to serve files
for Network Block Devices on remote hosts.

%package client
Summary: Network Block Device client
Group: Networking/Other
Requires: %name-doc = %EVR

%description client
This package contains nbd-client - a user space tool needed to manage
a Network Block Device.

%if_with static_client
%package client-static
Summary: Network Block Device static client
Group: Networking/Other
Requires: %name-doc = %EVR

%description client-static
This package contains a statically linked edition of nbd-client.
%endif

%prep
%setup
%patch1 -p1

%build
./autogen.sh

%if_with static_client
%configure \
    %{subst_enable debug} \
    %{subst_enable lfs} \
    --disable-syslog \
    --disable-sdp \
    %nil

make CC="diet -Os %__cc" CFLAGS="%optflags -Os" LDADD="-lcompat" %name-client
mv %name-client{,.static}
%make_build clean
%endif

%configure \
    %{subst_enable debug} \
    %{subst_enable lfs} \
    %{subst_enable syslog} \
    %{subst_enable sdp} \
    %{subst_with setproctitle} \
    %{subst_enable gznbd} \
    %nil

%make_build

%install
%makeinstall_std
%{?_with_static_client:install -pm755 %name-client.static %buildroot%_sbindir/}
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m755 %SOURCE3 %buildroot%_unitdir/nbd.service
install -pD -m644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/nbd-server
install -pD %SOURCE2 %buildroot%_sysconfdir/%name-server/config

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 README.md tests/run/simple_test %buildroot%docdir/

%pre server
%_sbindir/groupadd -r -f _nbd
%_sbindir/useradd -r -g _nbd -d /dev/null -s /dev/null -n _nbd > /dev/null 2>&1 ||:

%post server
%post_service %name

%preun server
%preun_service %name

%files doc
%docdir

%files server
%_bindir/*
%config(noreplace) %_sysconfdir/sysconfig/nbd-server
%_man1dir/*
%_man5dir/*
%_initdir/*
%_unitdir/*.service
%defattr(600,root,_nbd,710)
%config(noreplace) %_sysconfdir/%name-server/

%files client
%_sbindir/%name-client
%_man8dir/*

%if_with static_client
%files client-static
%_sbindir/%name-client.static
%endif

%changelog
* Thu Oct 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.20-alt1
- Updated to upstream version 3.20 (Fixes: CVE-2013-6410, CVE-2013-7441, CVE-2015-0847).

* Fri Jul 06 2012 Dmitry V. Levin <ldv@altlinux.org> 3.2-alt1
- Updated to 3.2.
- Updated package decriptions.
- Enhanced interpackage dependencies.

* Tue Jun 19 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt5
- nbd-server:
  + fixed several memory leaks in connection handling code;
  + fixed potential losing of new client connections;
  + fixed signal handling;
  + added and enabled setproctitle support.

* Fri Jun 15 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt4
- nbd-client: try to reconnect harder in persist mode.
- nbd-server:
  + fixed crash in child processes on sigterm;
  + implemented -D/-dont-daemonize option for systemd;
  + fixed modernsock initialization;
  + fixed modernsock descriptor leaking to child processes.

* Fri Jun 15 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt3
- nbd-server: fixed lowering privileges code:
  + when "group" option is specified, clear supplementary groups;
  + when "user" option is specified and "group" option is not specified,
    initialize gid and supplementary groups for the user specified by
    "user" option.

* Fri Jun 15 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt2
- Updated to nbd-3.1.1-2-g314fa69.
- nbd-client: fixed wrt leaving child processes in the zombie state.
- nbd-client: implemented the oom-killer score adjustment in swap mode.

* Wed Jun 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.1-alt1
- 3.1.1
- add /etc/sysconfig/nbd-server
- add systemd service
- switch to _nbd user by default

* Thu Jul 08 2010 Michail Yakushin <silicium@altlinux.ru> 2.9.15-alt1
- 2.9.15
- turn off static client
- turn off sdp

* Sun Jan 24 2010 Led <led@altlinux.ru> 2.9.14-tmc1
- 2.9.14 with postrelease fixes

* Sat Jan 23 2010 Led <led@altlinux.ru> 2.9.13-tmc1
- 2.9.13

* Fri Dec 11 2009 Led <led@altlinux.ru> 2.9.12-alt1
- 2.9.12
- enabled sdp

* Tue Jun 10 2008 Led <led@altlinux.ru> 2.9.11-alt2
- added:
  + %name-2.9.11-configure.patch
  + %name-2.9.11-alt-doc.patch
- updated %name-2.9.11-types.patch

* Thu May 08 2008 Led <led@altlinux.ru> 2.9.11-alt1
- 2.9.11
- removed %name-2.9.6-gznbd.patch
- updated %name-2.9.11-types.patch

* Mon Dec 10 2007 Led <led@altlinux.ru> 2.9.9-alt1
- 2.9.9
- removed nbd-2.9.8-close.patch

* Fri Nov 09 2007 Led <led@altlinux.ru> 2.9.8-alt2
- added %name-2.9.8-close.patch

* Mon Oct 29 2007 Led <led@altlinux.ru> 2.9.8-alt1
- 2.9.8
- removed %name-2.9.7-prerun.patch (fixed in upstream)

* Thu Oct 18 2007 Led <led@altlinux.ru> 2.9.7-alt4
- fixed init-script for %name-server

* Mon Oct 15 2007 Led <led@altlinux.ru> 2.9.7-alt3
- cleaned up spec
- added init-script for %name-server

* Sun Oct 14 2007 Led <led@altlinux.ru> 2.9.7-alt2
- added %name-client.static
- added %name-2.9.7-prerun.patch

* Fri Sep 21 2007 Led <led@altlinux.ru> 2.9.7-alt1
- 2.9.7

* Mon Aug 06 2007 Led <led@altlinux.ru> 2.9.6-alt1
- 2.9.6
- updated %name-2.9.6-gznbd.patch

* Sat Jun 16 2007 Led <led@altlinux.ru> 2.9.3-alt1
- 2.9.3

* Fri Mar 16 2007 Led <led@altlinux.ru> 2.9.0-alt0.1
- initial build
