%define Name iSCSI
%define bname iscsi

Name: open-%bname
%define module_name %name
Version: 2.1.4
License: GPL-2.0-or-later
Release: alt2
Summary: Utils to operate with %Name
Group: System/Kernel and hardware
URL: http://%name.org
Source: %name-%version.tar
Source1: iscsi-gen-initiatorname.sh
Patch: %name-%version-%release.patch
Conflicts: linux-iscsi
Provides: iscsi-initiator-utils = 6.%version-%release

BuildRequires: libmount-devel
BuildRequires: libkmod-devel
BuildRequires: libssl-devel
BuildRequires: libsystemd-devel
BuildRequires: libisns-devel

%description
The Open-iSCSI project is a high-performance, transport independent,
multi-platform implementation of RFC3720 iSCSI.

%package iscsiuio
Summary: Userspace configuration daemon required for some iSCSI hardware
Group: System/Kernel and hardware
License: BSD
Requires: %name = %version-%release

%description iscsiuio
The iscsiuio configuration daemon provides network configuration help
for some iSCSI offload hardware.

%package -n libopeniscsiusr
Summary: library providing access to Open-iSCSI initiator functionality
Group: System/Libraries
License: BSD

%description -n libopeniscsiusr
The libopeniscsiusr library provides a C API for access to the Open-iSCSI
initiator. It is used by the Open-iSCSI command line tools.

%package -n libopeniscsiusr-devel
Summary: Development files for libopeniscsiusr
Group: Development/C
Requires: libopeniscsiusr = %EVR

%description -n libopeniscsiusr-devel
The libopeniscsiusr-devel package contains libraries and header files for
developing applications that use libopeniscsiusr.

%prep
%setup
%patch -p1

%build
# configure sub-packages from here
# letting the top level Makefile do it will lose setting from rpm
cd iscsiuio
%autoreconf
%configure --disable-static
cd ..

%make_build

%install
%make_install DESTDIR=%buildroot initddir=%_initdir \
    install_programs install_initd_alt install_etc install_doc install_libopeniscsiusr

install -m 0755 %SOURCE1 %buildroot/sbin/iscsi-gen-initiatorname

install -d %buildroot%_lockdir/iscsi
touch %buildroot%_lockdir/iscsi/lock

install -pm 755 usr/iscsistart %buildroot/sbin/
install -pm 644 doc/iscsistart.8 %buildroot%_man8dir/
install -pm 644 doc/iscsi-iname.8 %buildroot%_man8dir/
install -d %buildroot%_logrotatedir
install -pm 644 iscsiuio/iscsiuiolog %buildroot%_logrotatedir/

mkdir -p %buildroot%_sharedstatedir/%bname/{nodes,send_targets,static,isns,slp,ifaces}

install -d %buildroot%_unitdir
install -pm 644 etc/systemd/iscsi-init.service %buildroot%_unitdir/
install -pm 644 etc/systemd/iscsi.service %buildroot%_unitdir/
install -pm 644 etc/systemd/iscsid.service %buildroot%_unitdir/
install -pm 644 etc/systemd/iscsid.socket %buildroot%_unitdir/
install -pm 644 etc/systemd/iscsiuio.service %buildroot%_unitdir/
install -pm 644 etc/systemd/iscsiuio.socket %buildroot%_unitdir/
install -d %buildroot%_tmpfilesdir
install -pm 644 etc/systemd/iscsi.tmpfiles %buildroot%_tmpfilesdir/%bname.conf

ln -s iscsid.service %buildroot%_unitdir/open-iscsi.service

%post
if [ ! -f /etc/iscsi/initiatorname.iscsi ] ; then
    /sbin/iscsi-gen-initiatorname
fi
%post_service %name

%preun
%preun_service %name

%post iscsiuio
%post_service iscsiuio

%preun iscsiuio
%preun_service iscsiuio

%files
%doc README THANKS etc/iface.example
%dir %_sysconfdir/%bname
%config(noreplace) %_sysconfdir/%bname/%{bname}d.conf
%_sharedstatedir/%bname
%_initdir/*
%_tmpfilesdir/*
%_unitdir/*
%exclude %_unitdir/iscsiuio.*
/sbin/*
%exclude /sbin/iscsiuio
%_man8dir/*
%exclude %_man8dir/iscsiuio.8.*
%dir %_lockdir/iscsi
%ghost %_lockdir/iscsi/lock

%files iscsiuio
/sbin/iscsiuio
%_unitdir/iscsiuio.*
%config(noreplace) %_logrotatedir/iscsiuiolog
%_man8dir/iscsiuio.8.*

%files -n libopeniscsiusr
%_libdir/libopeniscsiusr.so.*

%files -n libopeniscsiusr-devel
%_libdir/libopeniscsiusr.so
%_includedir/*
%_pkgconfigdir/libopeniscsiusr.pc

%changelog
* Fri Jun 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.4-alt2
- Fixed iscsi-init.service (ALT#40195).
- Use /var/lib/iscsi/ for configs.

* Sun Apr 11 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.4-alt1
- 2.1.4

* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 2.0.877-alt1.git73652184
- master snapshot 7365218437ecf8c03860e34c002c76871abf9943

* Mon Mar 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0.873-alt1.git006270
- master snapshot 006270c0f9a1fa1e78574a7eaa04bb9ae1ef62b6 (ALT#28583)
- add systemd units
- add iscsiuio package

* Fri Aug 08 2014 Lenar Shakirov <snejok@altlinux.ru> 2.0.871-alt7
- iscsi-gen-initiatorname.sh fixed: http://en.wikipedia.org/wiki/ISCSI

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.871-alt6.1
- Fixed build with new glibc

* Wed Aug 15 2012 Terechkov Evgenii <evg@altlinux.org> 2.0.871-alt6
- Fix LSB header to work with systemd

* Wed Jan  4 2012 Terechkov Evgenii <evg@altlinux.org> 2.0.871-alt5
- Fixes fot ALT#23676 (thanks to naf@) and ALT#26775

* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.871-alt4
- reapir build

* Wed Aug 26 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.871-alt3
- Fix path to LOCKFILE

* Wed Aug 26 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.871-alt2
- Add "mount -a -O _netdev" during start
- Add {pre,post}_service %name
- Add patch from ubuntu (https://launchpad/bugs/408915)

* Thu Aug 06 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.871-alt1
- 2.0-871

* Tue May 05 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.870.3-alt3
- Add %_sysconfdir/%bname to spec

* Sun May 03 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0.870.3-alt2
- Add iscsi-gen-initiatorname.sh
- Update init script

* Sat Feb 28 2009 Led <led@altlinux.ru> 2.0.870.3-alt1
- 2.0-870.3

* Sun Feb 15 2009 Led <led@altlinux.ru> 2.0.870.2-alt1
- 2.0-870.2

* Wed May 14 2008 Led <led@altlinux.ru> 2.0.869.2-alt0.1
- 2.0-869-2
- fixed License

* Tue May 06 2008 Led <led@altlinux.ru> 2.0.869-alt0.1
- 2.0-869
- added kernel-source-%module_name subpackage

* Tue Nov 20 2007 Led <led@altlinux.ru> 2.0.865.15-alt0.1
- 2.0-865.15
- added URL
- added ChangeLog to docs

* Tue Oct 02 2007 Led <led@altlinux.ru> 2.0.865.12-alt0.1
- 2.0-865.12

* Thu Aug 16 2007 Led <led@altlinux.ru> 2.0.865.10-alt0.1
- 2.0-865.10:
  + fixes some security issues, which can be exploited by malicious,
    local users to cause a DoS (Denial of Service) (CVE-2007-3099,
    CVE-2007-3099).
  + added utils: iscsi-iname, fwparam_ibft
- fixed License

* Fri Jun 08 2007 Led <led@altlinux.ru> 2.0.754-alt0.1
- 2.0-754
- cleaned up spec
- fixed License
- cleaned up %name-alt-init.patch
- cleaned up BuildRequires
- added docs

* Wed Dec 20 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 2.0.730-alt2
- Some fixes

* Wed Dec 20 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 2.0.730-alt1
- Some minor fixes

* Mon Nov 27 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 2.0.730-alt0
- Initial build for ALTLinux
