%def_disable check

Name:    cloud-init
Version: 19.2
Release: alt3

Summary: Cloud instance init scripts
Group:   System/Configuration/Boot and Init
License: GPLv3
Url:     http://launchpad.net/cloud-init

Source0: %name-%version.tar

Source1: cloud-init-alt.cfg
Source2: 01_netplan.cfg
Source3: cloud-init-tmpfiles.conf

Source11: cloud-config
Source12: cloud-final
Source13: cloud-init
Source14: cloud-init-local

Patch1: %name-%version-%release.patch

%add_findreq_skiplist /lib/systemd/system-generators/cloud-init-generator

BuildArch: noarch
# /proc for tests
BuildRequires: /proc

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-distribute python3-module-nose python3-module-mocker
BuildRequires: python3-module-yaml python3-module-oauthlib
BuildRequires: systemd-devel
# For tests
BuildRequires: python3-module-requests python3-module-jsonpatch python3-module-configobj python3-module-mock python3-module-oauthlib
BuildRequires: python3-module-httpretty python3-module-serial iproute2 util-linux net-tools python3-module-jinja2 python3-module-contextlib2 python3-module-prettytable

Requires: sudo
Requires: e2fsprogs
Requires: cloud-utils-growpart
Requires: procps
Requires: iproute net-tools
Requires: shadow-utils
Requires: /bin/run-parts
Requires: netplan
Requires: dhcp-client
# add not autoreq'ed
%py3_requires Cheetah
%py3_requires jinja2

# use urllib3 for requests.packages.urllib3
%py3_requires urllib3
%filter_from_requires /python3(requests.packages.urllib3.connection)/d
%filter_from_requires /python3(requests.packages.urllib3.poolmanager)/d

%description
Cloud-init is a set of init scripts for cloud instances.  Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.

%package config-netplan
Summary: Cloud config option use netplan network render
Group:   System/Configuration/Boot and Init
License: GPLv3

%description config-netplan
%summary.

%prep
%setup
%patch1 -p1

%build
%python3_build_debug

%install
%python3_install --init-system=systemd

install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/cloud/cloud.cfg
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/cloud/cloud.cfg.d/
install -pD -m644 %SOURCE3 %buildroot%_tmpfilesdir/cloud-init.conf
install -pD -m755 %SOURCE11 %buildroot%_initdir/cloud-config
install -pD -m755 %SOURCE12 %buildroot%_initdir/cloud-final
install -pD -m755 %SOURCE13 %buildroot%_initdir/cloud-init
install -pD -m755 %SOURCE14 %buildroot%_initdir/cloud-init-local

mkdir -p %buildroot%_libexecdir
mv %buildroot/usr/libexec/%name %buildroot%_libexecdir/
mkdir -p %buildroot%_sharedstatedir/cloud

# Remove non-ALTLinux templates
rm -f %buildroot%_sysconfdir/cloud/templates/*.debian.*
rm -f %buildroot%_sysconfdir/cloud/templates/*.freebsd.*
rm -f %buildroot%_sysconfdir/cloud/templates/*.redhat.*
rm -f %buildroot%_sysconfdir/cloud/templates/*.suse.*
rm -f %buildroot%_sysconfdir/cloud/templates/*.ubuntu.*

%check
make unittest3

%post
%post_service cloud-config
%post_service cloud-final
%post_service cloud-init
%post_service cloud-init-local

%preun
%preun_service cloud-config
%preun_service cloud-final
%preun_service cloud-init
%preun_service cloud-init-local

%files config-netplan
%config            %_sysconfdir/cloud/cloud.cfg.d/01_netplan.cfg

%files
%doc ChangeLog TODO.rst
%dir               %_sysconfdir/cloud
%config(noreplace) %_sysconfdir/cloud/cloud.cfg
%dir               %_sysconfdir/cloud/cloud.cfg.d
%config(noreplace) %_sysconfdir/cloud/cloud.cfg.d/*.cfg
%exclude           %_sysconfdir/cloud/cloud.cfg.d/01_netplan.cfg
%doc               %_sysconfdir/cloud/cloud.cfg.d/README
%dir               %_sysconfdir/cloud/templates
%config(noreplace) %_sysconfdir/cloud/templates/*
%_sysconfdir/NetworkManager/dispatcher.d/hook-network-manager
%_datadir/bash-completion/completions/%name
/lib/udev/rules.d/66-azure-ephemeral.rules
%_initdir/*
%_unitdir/*
%_tmpfilesdir/*
/lib/systemd/system-generators/cloud-init-generator
%python3_sitelibdir/*
%_libexecdir/%name
%_bindir/cloud-init*
%_bindir/cloud-id
%doc %_datadir/doc/%name
%dir %_sharedstatedir/cloud

%changelog
* Mon Sep 02 2019 Mikhail Gordeev <obirvalger@altlinux.org> 19.2-alt3
- Create package cloud-init-config-netplan

* Tue Aug 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 19.2-alt2
- Pack /etc/cloud

* Thu Jul 25 2019 Mikhail Gordeev <obirvalger@altlinux.org> 19.2-alt1
- Update to 19.2
- Use netplan to render network

* Sun Dec 16 2018 Mikhail Gordeev <obirvalger@altlinux.org> 18.4-alt2
- Allow services works only in virtualization

* Thu Dec 13 2018 Mikhail Gordeev <obirvalger@altlinux.org> 18.4-alt1
- Update to 18.4
- Add support of networkd

* Thu May 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.9-alt3.git.5beecd
- Updated build dependencies.

* Tue Mar 21 2017 Alexey Shabalin <shaba@altlinux.ru> 0.7.9-alt2.git.5beecd
- update ALTLinux etcnet support

* Mon Mar 20 2017 Alexey Shabalin <shaba@altlinux.ru> 0.7.9-alt1.5beecd
- git snapshot 5beecdf88b630a397b3722ddb299e9a37ff02737

* Thu Nov 24 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.8-alt2.git9d826b88
- fixed run

* Mon Nov 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.8-alt1.git9d826b88
- git snapshot 9d826b8855797bd37e477b6da43153c49529afe8

* Wed Dec 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.6-alt2.20151202
- upstream snapshot
- add ALTLinux support
- add SysV init scripts
- don't add ec2-user user

* Thu May 28 2015 Andrey Cherepanov <cas@altlinux.org> 0.7.6-alt1
- New version

* Thu May 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.3-alt1
- initial

