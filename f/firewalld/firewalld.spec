Name: firewalld
Version: 0.7.3
Release: alt1

Summary: A firewall daemon with D-BUS interface providing a dynamic firewall
License: GPLv2+
Group: System/Configuration/Networking

URL: https://www.firewalld.org/
# git://git.fedorahosted.org/firewalld.git
Source: %name-%version.tar
Source1: %name.init
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-xdg python3-devel
BuildRequires: intltool xsltproc docbook-style-xsl docbook-dtds glib2-devel libgio-devel

Requires: iptables ebtables iptables-ipv6 nftables

%allow_python3_import_path %_datadir/firewalld
%add_python3_path %_datadir/firewalld

%define _unpackaged_files_terminate_build 1

%description
firewalld is a firewall service daemon that provides a dynamic
customizable firewall with a D-BUS interface.

%package -n firewall-config
Summary: Firewall configuration application
Group: System/Configuration/Networking
Requires: %name = %version-%release
Requires: libnm-gir

%description -n firewall-config
The firewall configuration application provides an configuration interface
for firewalld.

%package -n firewall-applet
Summary: Firewall panel applet
Group: System/Configuration/Networking
Requires: firewall-config = %version-%release
Requires: libnm-gir
Requires: libnotify-gir

%description -n firewall-applet
The firewall panel applet provides a status information of firewalld and
also the firewall settings.

%package -n python3-module-firewall
Summary: Python3 bindings for firewalld
Group: Development/Python3

%description -n python3-module-firewall
Python3 bindings for firewalld.

%prep
%setup
%patch -p1

%build
%autoreconf
export PYTHON=/usr/bin/python3
%configure \
	--enable-sysconfig \
	--enable-systemd \
	--with-systemd-unitdir=%systemd_unitdir \
	--with-iptables=/sbin/iptables \
	--with-iptables-restore=/sbin/iptables-restore \
	--with-ip6tables=/sbin/ip6tables \
	--with-ip6tables-restore=/sbin/ip6tables-restore \
	--with-ebtables=/sbin/ebtables \
	--with-ebtables-restore=/sbin/ebtables-restore \
	--with-ipset=/sbin/ipset \
	--with-nft=/usr/sbin/nft
%make
make update-po

%install
%makeinstall_std PYTHON=/usr/bin/python3
pushd po
make install DESTDIR=%buildroot
popd
%find_lang %name
install -pDm755 %SOURCE1 %buildroot%_initdir/%name

# Most tests require root
#check
#make check

%post
%post_service %name

%preun
%preun_service %name

%files -f %name.lang
%_sbindir/*
%_bindir/firewall-cmd
%_bindir/firewall-offline-cmd
%attr(0750,root,root) %config(noreplace) %_sysconfdir/firewalld
%attr(0640,root,root) %config(noreplace) %_sysconfdir/firewalld/firewalld.conf
%config(noreplace) %_sysconfdir/sysconfig/firewalld
%_initdir/%name
%_usr/lib/firewalld
%systemd_unitdir/firewalld.service
%config %_sysconfdir/modprobe.d/firewalld-sysctls.conf
%config %_datadir/dbus-1/system.d/FirewallD.conf
%_datadir/polkit-1/actions/org.fedoraproject.FirewallD1.policy
%_datadir/polkit-1/actions/org.fedoraproject.FirewallD1.desktop.policy.choice
%_datadir/polkit-1/actions/org.fedoraproject.FirewallD1.server.policy.choice
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*
%_man1dir/*
%_man5dir/*
%exclude %_man1dir/firewall-config*.1*

%files -n firewall-config
%_bindir/firewall-config
%_datadir/firewalld/
%_datadir/applications/firewall-config.desktop
%_datadir/metainfo/firewall-config.appdata.xml
%_iconsdir/hicolor/*/apps/firewall-config*
%_datadir/glib-2.0/schemas/org.fedoraproject.FirewallConfig.gschema.xml
%_man1dir/firewall-config*.1*

%files -n firewall-applet
%dir %_sysconfdir/firewall
%config(noreplace) %_sysconfdir/firewall/applet.conf
%_bindir/firewall-applet
%_xdgconfigdir/autostart/firewall-applet.desktop
%_iconsdir/hicolor/*/apps/firewall-applet*

%files -n python3-module-firewall
%python3_sitelibdir_noarch/firewall

%changelog
* Tue Feb 04 2020 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1
- Spec cleanup.
- Drop rpm-build-licenses usage.
- Updated to 0.7.2.

* Fri Nov 15 2019 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1
- Updated to 0.7.2.

* Mon Sep 23 2019 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Updated to 0.7.1.

* Thu May 23 2019 Mikhail Efremov <sem@altlinux.org> 0.6.4-alt1
- Updated to 0.6.4.

* Fri Apr 05 2019 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt2
- Use iptables backend by default for now (closes: #36502).

* Fri Mar 29 2019 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1
- Use python3 in more scripts.
- Updated to 0.6.3.

* Thu Sep 20 2018 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt1
- Updated to 0.5.5.

* Wed Sep 05 2018 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1
- Updated to 0.5.4.
- Fix requires.

* Mon May 14 2018 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt1
- Updated to 0.5.3.

* Thu Mar 22 2018 Mikhail Efremov <sem@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Thu Mar 22 2018 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Drop workaround for python3-module-PyQt5.
- Use python3 in scripts.
- Split python module and firewall-config to separate packages.
- Updated to 0.5.1.

* Fri Nov 24 2017 Mikhail Efremov <sem@altlinux.org> 0.4.4.6-alt1
- Updated to 0.4.4.6.

* Wed Aug 16 2017 Mikhail Efremov <sem@altlinux.org> 0.4.4.5-alt1
- Build with python 3.x.
- Updated to 0.4.4.5 (closes: #32042).

* Mon Nov 21 2016 Terechkov Evgenii <evg@altlinux.org> 0.4.4.1-alt1
- 0.4.4.1

* Sat Aug 20 2016 Terechkov Evgenii <evg@altlinux.org> 0.4.3.3-alt1
- 0.4.3.3

* Wed Jul  6 2016 Terechkov Evgenii <evg@altlinux.org> 0.4.3.2-alt1
- 0.4.3.2

* Wed Jun 29 2016 Terechkov Evgenii <evg@altlinux.org> 0.4.3.1-alt1
- 0.4.3.1

* Tue Jun 28 2016 Terechkov Evgenii <evg@altlinux.org> 0.4.3-alt1
- 0.4.3

* Sun May  1 2016 Terechkov Evgenii <evg@altlinux.org> 0.4.1.2-alt1
- Updated to 0.4.1.2 (ALT #32042)

* Fri Feb 05 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Wed Jun 17 2015 Mikhail Efremov <sem@altlinux.org> 0.3.14.2-alt1
- Updated to 0.3.14.2.

* Fri Dec 05 2014 Mikhail Efremov <sem@altlinux.org> 0.3.13-alt1
- Updated to 0.3.13.

* Tue Oct 14 2014 Mikhail Efremov <sem@altlinux.org> 0.3.12-alt1
- Update URL.
- Updated to 0.3.12.

* Wed Aug 27 2014 Mikhail Efremov <sem@altlinux.org> 0.3.11-alt1
- Fixes from upstream git:
  + Fixed rename of zones, services and icmptypes not to create new
    entry (RBHZ#1131064);
  + Fixed Python specific D-Bus exception (RHBZ#1132441).
- Updated to 0.3.11.

* Fri Jun 06 2014 Mikhail Efremov <sem@altlinux.org> 0.3.10-alt1
- Updated to 0.3.10.

* Fri Feb 07 2014 Mikhail Efremov <sem@altlinux.org> 0.3.9.3-alt1
- Updated to 0.3.9.3.

* Mon Jan 20 2014 Mikhail Efremov <sem@altlinux.org> 0.3.9.2-alt1
- Updated to 0.3.9.2.

* Tue Jan 14 2014 Mikhail Efremov <sem@altlinux.org> 0.3.9-alt1
- Updated to 0.3.9.

* Wed Nov 06 2013 Mikhail Efremov <sem@altlinux.org> 0.3.8-alt1
- Updated to 0.3.8.

* Mon Oct 21 2013 Mikhail Efremov <sem@altlinux.org> 0.3.7-alt1
- Updated to 0.3.7.

* Tue Oct 08 2013 Mikhail Efremov <sem@altlinux.org> 0.3.6.2-alt1
- Updated to 0.3.6.2.

* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 0.3.6.1-alt1
- Updated to 0.3.6.1.

* Mon Sep 30 2013 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- Updated to 0.3.5.

* Tue Aug 13 2013 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- Use autoconf-2.68.
- Updated to 0.3.4.

* Mon Jun 17 2013 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Tue May 14 2013 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Thu Jan 24 2013 Mikhail Efremov <sem@altlinux.org> 0.2.12-alt1
- Patch from upstream git:
  + default zone in firewalld.conf was set to public with every
    restart
- Updated to 0.2.12.

* Fri Dec 14 2012 Mikhail Efremov <sem@altlinux.org> 0.2.11-alt1
- Updated to 0.2.11.

* Wed Aug 29 2012 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Updated to 0.2.7.

* Mon Jun 04 2012 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Wed Mar 14 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt2
- Fix firewalld.conf permissions.
- Fix URL.

* Mon Mar 12 2012 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Initial build (based on Fedora spec).
