%define _unpackaged_files_terminate_build 1
%define rpmstate /run/openvswitch-rpm-state-

Name: ovn
Version: 20.09.0
Release: alt7

Summary: Open Virtual Network support
License: Apache-2.0 AND LGPL-2.1-only AND SISSL
Group: Networking/Other

URL: http://www.openvswitch.org/
Source0: %name-%version.tar
Source1: ovs.tar
Source2: %name.tmpfiles

Patch11: 0001-ovn-fix-linking.patch
Patch12: 0002-ovn-var_run-to-run.patch
Patch13: 0003-execute-ovn-as-openvswitch-user.patch

Provides: openvswitch-ovn-common = %EVR
Obsoletes: openvswitch-ovn-common < 2.14.0
Provides: openvswitch-ovn = %EVR
Obsoletes: openvswitch-ovn < 2.14.0
Requires: lib%name = %EVR
Requires: openvswitch >= 2.14.0

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: graphviz libssl-devel openssl groff
BuildRequires: libopenvswitch-devel
BuildRequires: libcap-ng-devel
BuildRequires: libunwind-devel
BuildRequires: libunbound-devel
BuildRequires: glibc-kernheaders
BuildRequires: python3-devel python3-module-setuptools python3-module-OpenSSL python3-module-sphinx

%define ovs_dir %_builddir/ovs

%description
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package -n lib%name
License: Apache-2.0
Summary: Open Virtual Network core libraries
Group: System/Libraries

%description -n lib%name
This subpackage contains the OVN shared libraries.

%package -n lib%name-devel
Summary: Development files for Open Virtual Network
License: Apache-2.0
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Devel libraries and headers for Open Virtual Network.

%package central
Summary: Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Provides: openvswitch-ovn-central = %EVR
Obsoletes: openvswitch-ovn-central < 2.14.0

%description central
OVN DB servers and ovn-northd running on a central node.

%package host
Summary: Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Provides: openvswitch-ovn-host = %EVR
Obsoletes: openvswitch-ovn-host < 2.14.0

%description host
OVN controller running on each host.

%package vtep
Summary: Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
Requires: %name = %EVR
Provides: openvswitch-ovn-vtep = %EVR
Obsoletes: openvswitch-ovn-vtep < 2.14.0

%description vtep
OVN vtep controller

%package docker
Summary: Open Virtual Network support
License: Apache-2.0
Group: Networking/Other
BuildArch: noarch
Requires: %name = %EVR
Provides: openvswitch-ovn-docker = %EVR
Obsoletes: openvswitch-ovn-docker < 2.14.0

%description docker
Docker network plugins for OVN.

%package debugtools
Group: Networking/Other
License: Apache-2.0
Summary: Open Virtual Network bug reporting tool
BuildArch: noarch
Requires: %name = %EVR

%description debugtools
This package contains ovn-bugtool to generate a debug bundle
with useful information about Open Virtual Network on this system.

%prep
%setup
mkdir -p %ovs_dir
tar -xf %SOURCE1 -C %ovs_dir

%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
export PYTHON3=%__python3

# OVN source code is now separate.
# Build openvswitch first.
pushd %ovs_dir
%autoreconf
%configure \
    --disable-static \
    --enable-shared \
    --enable-ndebug \
    --enable-ssl \
    --with-rundir=/run/openvswitch \
    --with-logdir=%_logdir/openvswitch \
    --with-dbdir=%_localstatedir/openvswitch \
    --with-pkidir=%_localstatedir/openvswitch/pki

%make_build
popd

%autoreconf
%configure \
    --with-ovs-source=%ovs_dir \
    --disable-static \
    --enable-shared \
    --enable-ssl \
    --with-rundir=/run/%name \
    --with-logdir=%_logdir/%name \
    --with-dbdir=%_localstatedir/%name \
    --with-pkidir=%_localstatedir/openvswitch/pki
%make_build

%install
export PYTHON3=%__python3
%makeinstall_std

install -dm0755 %buildroot%_localstatedir/%name
install -dm0750 %buildroot%_logdir/%name

install -pDm0644 rhel/usr_share_ovn_scripts_systemd_sysconfig.template \
        %buildroot%_sysconfdir/sysconfig/%name
install -pDm0644 rhel/etc_logrotate.d_ovn \
        %buildroot%_logrotatedir/%name
for service in ovn-controller ovn-controller-vtep ovn-northd; do
    install -pDm0644 \
            rhel/usr_lib_systemd_system_${service}.service \
            %buildroot%_unitdir/${service}.service
done

install -pDm644 %SOURCE2 %buildroot%_tmpfilesdir/%name.conf

#install -d %buildroot%_prefix/lib/firewalld/services
#install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-central-firewall-service.xml \
#        %buildroot%_prefix/lib/firewalld/services/ovn-central-firewall-service.xml
#install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-host-firewall-service.xml \
#        %buildroot%_prefix/lib/firewalld/services/ovn-host-firewall-service.xml

#install -d -m 0755 %buildroot%_prefix/lib/ocf/resource.d/ovn
#ln -s %_datadir/ovn/scripts/ovndb-servers.ocf \
#      %buildroot%_prefix/lib/ocf/resource.d/ovn/ovndb-servers

%pre central
# Save the "enabled" state across the transition of
# ownership of ovn-northd.service from openvswitch-ovn-central to
# ovn-central.
SYSTEMCTL=systemctl
if [ $1 -eq 1 ]; then
    if sd_booted && "$SYSTEMCTL" --quiet is-enabled ovn-northd; then
        touch %{rpmstate}ovn-northd ||:
    fi
    if sd_booted && [ -f /run/openvswitch/ovnnb_db.pid ]; then
        touch %{rpmstate}ovn-northd-started ||:
        "$SYSTEMCTL" --quiet stop ovn-northd ||:
    fi
fi

%post central
echo "post install central = $1"
if [ $1 -eq 1 ]; then
    # move db and log from openvswitch to ovn dir
    for db in ovnnb ovnsb; do
        [ ! -f %_localstatedir/openvswitch/${db}_db.db ] || mv -f %_localstatedir/openvswitch/${db}_db.db %_localstatedir/%name/
        [ ! -f %_localstatedir/openvswitch/.${db}_db.db.~lock~ ] || mv -f %_localstatedir/openvswitch/.${db}_db.db.~lock~ %_localstatedir/%name/
    done
    for log in ovn-northd ovsdb-server-nb ovsdb-server-sb; do
        [ ! -f %_logdir/openvswitch/${log}.log ] || mv -f %_logdir/openvswitch/${log}.log* %_logdir/%name/
    done
    chown -R openvswitch:openvswitch %_logdir/%name %_localstatedir/%name
fi
%post_service ovn-northd

%preun central
%preun_service ovn-northd

%triggerpostun central -- openvswitch-ovn-central < 2.14.0
SYSTEMCTL=systemctl
[ $2 -eq 0 ] || exit 0
if [ -e %{rpmstate}ovn-northd ]; then
    rm -f %{rpmstate}ovn-northd
    if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" --quiet enable ovn-northd ||:
    fi
fi
if [ -e %{rpmstate}ovn-northd-started ]; then
    rm -f %{rpmstate}ovn-northd-started
    if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload
        systemd-tmpfiles --create %_tmpfilesdir/%name.conf >/dev/null 2>&1 ||:
        "$SYSTEMCTL" --quiet restart ovn-northd ||:
    fi
fi

%pre host
# Save the "enabled" state across the transition of
# ownership of ovn-controller.service from openvswitch-ovn-host to
# ovn-host.
SYSTEMCTL=systemctl
if [ $1 -eq 1 ]; then
    if sd_booted && "$SYSTEMCTL" --quiet is-enabled ovn-controller; then
        touch %{rpmstate}ovn-controller ||:
    fi
    if sd_booted && [ -f /run/openvswitch/ovn-controller.pid ]; then
        touch %{rpmstate}ovn-controller-started ||:
        "$SYSTEMCTL" --quiet stop ovn-controller ||:
    fi
fi

%post host
if [ $1 -eq 1 ]; then
    # move log from openvswitch to ovn dir
    [ ! -f %_logdir/openvswitch/ovn-controller.log ] || mv -f %_logdir/openvswitch/ovn-controller.log* %_logdir/%name/
    chown -R openvswitch:openvswitch %_logdir/%name
fi
%post_service ovn-controller

%preun host
%preun_service ovn-controller

%triggerpostun host -- openvswitch-ovn-host < 2.14.0
SYSTEMCTL=systemctl
[ $2 -eq 0 ] || exit 0
if [ -e %{rpmstate}ovn-controller ]; then
    rm -f %{rpmstate}ovn-controller
    if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" --quiet enable ovn-controller ||:
    fi
fi
if [ -e %{rpmstate}ovn-controller-started ]; then
    rm -f %{rpmstate}ovn-controller-started
    if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload
        systemd-tmpfiles --create %_tmpfilesdir/%name.conf >/dev/null 2>&1 ||:
        "$SYSTEMCTL" --quiet restart ovn-controller ||:
    fi
fi

%pre vtep
# Save the "enabled" state across the transition of
# ownership of ovn-controller-vtep.service from openvswitch-ovn-vtep to
# ovn-vtep.
SYSTEMCTL=systemctl
if [ $1 -eq 1 ]; then
    if sd_booted && "$SYSTEMCTL" --quiet is-enabled ovn-controller-vtep; then
        touch %{rpmstate}ovn-controller-vtep ||:
    fi
    if sd_booted && [ -f /run/openvswitch/ovn-controller-vtep.pid ]; then
        touch %{rpmstate}ovn-controller-vtep-started ||:
        "$SYSTEMCTL" --quiet stop ovn-controller-vtep ||:
    fi
fi

%post vtep
SYSTEMCTL=systemctl
if [ $1 -eq 1 ]; then
    # move log from openvswitch to ovn dir
    [ ! -f %_logdir/openvswitch/ovn-controller-vtep.log ] || mv -f %_logdir/openvswitch/ovn-controller-vtep.log* %_logdir/%name/
    chown -R openvswitch:openvswitch %_logdir/%name
fi
%post_service ovn-controller-vtep

%preun vtep
%preun_service ovn-controller-vtep

%triggerpostun vtep -- openvswitch-ovn-vtep < 2.14.0
SYSTEMCTL=systemctl
[ $2 -eq 0 ] || exit 0
if [ -e %{rpmstate}ovn-controller-vtep ]; then
    rm -f %{rpmstate}ovn-controller-vtep
    if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" --quiet enable ovn-controller-vtep ||:
    fi
fi
if [ -e %{rpmstate}ovn-controller-vtep-started ]; then
    rm -f %{rpmstate}ovn-controller-vtep-started
    if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
        "$SYSTEMCTL" daemon-reload
        systemd-tmpfiles --create %_tmpfilesdir/%name.conf >/dev/null 2>&1 ||:
        "$SYSTEMCTL" --quiet restart ovn-controller-vtep ||:
    fi
fi

%files
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_bindir/ovn-appctl
%_bindir/ovn-nbctl
%_bindir/ovn-sbctl
%_bindir/ovn-ic-nbctl
%_bindir/ovn-ic-sbctl
%_bindir/ovn-trace
%_bindir/ovn-detrace
%dir %_datadir/%name
%dir %_datadir/%name/scripts
%_datadir/%name/scripts/ovn-ctl
%_datadir/%name/scripts/ovn-lib
%_datadir/%name/scripts/ovndb-servers.ocf
%_man8dir/ovn-appctl.*
%_man1dir/ovn-detrace.*
%_man8dir/ovn-ctl.*
%_man8dir/ovn-nbctl.*
%_man8dir/ovn-ic-nbctl.*
%_man8dir/ovn-ic-sbctl.*
%_man5dir/ovn-ic-nb.*
%_man5dir/ovn-ic-sb.*
%_man8dir/ovn-trace.*
%_man7dir/ovn-architecture.*
%_man8dir/ovn-sbctl.*
%_man5dir/ovn-nb.*
%_man5dir/ovn-sb.*
%dir %attr(0755, openvswitch, openvswitch) %_logdir/%name
%dir %attr(0755, openvswitch, openvswitch) %_localstatedir/%name
%_tmpfilesdir/%name.conf

%files -n lib%name
%_libdir/lib%{name}*.so.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%{name}*.so

%files docker
%_bindir/ovn-docker-overlay-driver
%_bindir/ovn-docker-underlay-driver

%files central
%_bindir/ovn-northd
%_bindir/ovn-ic
%_man8dir/ovn-northd.*
%_man8dir/ovn-ic.*
%_datadir/%name/ovn-nb.ovsschema
%_datadir/%name/ovn-sb.ovsschema
%_datadir/%name/ovn-ic-nb.ovsschema
%_datadir/%name/ovn-ic-sb.ovsschema
%_unitdir/ovn-northd.service
#%%_prefix/lib/firewalld/services/ovn-central-firewall-service.xml

%files host
%_bindir/ovn-controller
%_man8dir/ovn-controller.*
%_unitdir/ovn-controller.service
#%%_prefix/lib/firewalld/services/ovn-host-firewall-service.xml

%files vtep
%_bindir/ovn-controller-vtep
%_man8dir/ovn-controller-vtep.*
%_unitdir/ovn-controller-vtep.service

%files debugtools
%_datadir/%name/bugtool-plugins
%_datadir/%name/scripts/ovn-bugtool-*

%changelog
* Sat Jan 23 2021 Alexey Shabalin <shaba@altlinux.org> 20.09.0-alt7
- move detect of started and enabled services to %%pre
- fixed detect of started services based on pid file
- create runtime dir before restart services in %%triggerpostun

* Mon Jan 18 2021 Alexey Shabalin <shaba@altlinux.org> 20.09.0-alt6
- One more fix migrate from openvswitch-ovn to ovn packages name

* Wed Dec 30 2020 Alexey Shabalin <shaba@altlinux.org> 20.09.0-alt5
- Restart services for migrate form openvswitch-ovn
  even if they are not enabled, but started.

* Wed Dec 30 2020 Alexey Shabalin <shaba@altlinux.org> 20.09.0-alt4
- Build docker subpackage as noarch

* Tue Dec 29 2020 Alexey Shabalin <shaba@altlinux.org> 20.09.0-alt3
- Fix migrate from openvswitch-ovn to ovn packages name

* Sat Dec 26 2020 Alexey Shabalin <shaba@altlinux.org> 20.09.0-alt2
- own /var/log/ovn and /var/lib/ovn dirs
- add tmpfiles config

* Thu Dec 17 2020 Alexey Shabalin <shaba@altlinux.org> 20.09.0-alt1
- 20.09.0

* Fri Sep 25 2020 Alexey Shabalin <shaba@altlinux.org> 20.06.2-alt1
- Provide new OVN packages splitting from openvswitch

