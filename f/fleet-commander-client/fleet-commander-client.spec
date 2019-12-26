%define _unpackaged_files_terminate_build 1
%define _userunitdir /usr/lib/systemd/user

%def_with check

Name: fleet-commander-client
Version: 0.14.0
Release: alt1

Summary: Fleet Commander Client
License: LGPLv3+ and LGPLv2+ and MIT and BSD
Group: System/Base
BuildArch: noarch

Url: https://github.com/fleet-commander/fc-client
Source0: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: autoconf-archive
BuildRequires: libsystemd-devel
BuildRequires: python3(gi)

%if_with check
BuildRequires: python3(dbus)
BuildRequires: python3(dbusmock)
BuildRequires: python3(ldap)
BuildRequires: python3(samba)
BuildRequires: libnm-gir
BuildRequires: libjson-glib-gir
%endif

# mark Python code as Python3
%add_python3_path %_datadir/fleet-commander-client/python/
%add_python3_compile_exclude %_datadir/fleet-commander-client/python/
Requires: libnm-gir

%description
Profile data retriever for Fleet Commander client hosts. Fleet Commander is an
application that allows you to manage the desktop configuration of a large
network of users and workstations/laptops.

%prep
%setup
%patch -p1

grep -qsr '#!/usr/bin/env[[:space:]]\+python-wrapper.sh' ./tests/ || exit 1
grep -rl '#!/usr/bin/env[[:space:]]\+python-wrapper.sh' | \
xargs sed -i 's/#!\/usr\/bin\/env[[:space:]]\+python-wrapper.sh/#!\/usr\/bin\/python3/g'

# for now skip tests which require real system/session dbus
grep -qs '^TESTS[[:space:]]*=.* 09_fcclient\.sh[[:space:]]*' tests/Makefile.am || exit 1
sed -i '/^TESTS[[:space:]]*=/{s/09_fcclient\.sh//g}' tests/Makefile.am

# runuser is not on user PATH
grep -qs '^AC_PATH_PROG(\[RUNUSER\], \[runuser\])$' configure.ac || exit 1
sed -i '/^AC_PATH_PROG(\[RUNUSER\], \[runuser\])$/{s/)$/, "$PATH:\/sbin")/g}' \
configure.ac

%build
%autoreconf
%configure \
    --with-systemdsystemunitdir=%_unitdir \
    --with-systemduserunitdir=%_userunitdir
%make_build

%install
%makeinstall_std

%check
%make check || { cat ./tests/test-suite.log; exit 1; }

%post
%post_service fleet-commander-client
%post_service fleet-commander-clientad

%preun
%preun_service fleet-commander-client
%preun_service fleet-commander-clientad

if /sbin/sd_booted && /bin/systemctl --version >/dev/null 2>&1; then
    if [ "$1" -eq 0 ]; then
        # uninstall
        /bin/systemctl --no-reload -q disable --global \
            fleet-commander-adretriever ||:
    fi
fi

%files
%doc README
%dir %_datadir/fleet-commander-client
%dir %_datadir/fleet-commander-client/python
%dir %_datadir/fleet-commander-client/python/fleetcommanderclient
%_datadir/fleet-commander-client/python/fleetcommanderclient/*.py
%dir %_datadir/fleet-commander-client/python/fleetcommanderclient/adapters
%_datadir/fleet-commander-client/python/fleetcommanderclient/adapters/*.py
%dir %_datadir/fleet-commander-client/python/fleetcommanderclient/configadapters
%_datadir/fleet-commander-client/python/fleetcommanderclient/configadapters/*.py

%config(noreplace) %_sysconfdir/xdg/fleet-commander-client.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freedesktop.FleetCommanderClient.conf
%config(noreplace) %_sysconfdir/dbus-1/system.d/org.freedesktop.FleetCommanderClientAD.conf
%_unitdir/fleet-commander-client.service
%_unitdir/fleet-commander-clientad.service
%_userunitdir/fleet-commander-adretriever.service
%_datadir/dbus-1/system-services/org.freedesktop.FleetCommanderClient.service
%_datadir/dbus-1/system-services/org.freedesktop.FleetCommanderClientAD.service

%changelog
* Thu Nov 28 2019 Stanislav Levin <slev@altlinux.org> 0.14.0-alt1
- 0.10.2 -> 0.14.0.

* Thu Mar 14 2019 Stanislav Levin <slev@altlinux.org> 0.10.2-alt2
- Fixed triggering FC dbus service by SSSD.

* Fri Jan 18 2019 Stanislav Levin <slev@altlinux.org> 0.10.2-alt1
- Initial build.

