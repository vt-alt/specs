%define _unpackaged_files_terminate_build 1

%define _localstatedir %_var
%define _libexecdir    /usr/libexec
%def_without check

Name: fleet-commander-admin
Version: 0.15.1
Release: alt0.M90P.1

Summary: Fleet Commander
License: LGPLv2+ or MIT or BSD
Group: System/Base

Url: https://github.com/fleet-commander/fc-admin
Source: %name-%version.tar
Patch: %name-%version-alt.patch

ExcludeArch: %ix86
BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-python3
BuildRequires: autoconf-archive
BuildRequires: python3(dbus)
BuildRequires: python3(gi)
BuildRequires: python3(libvirt)
BuildRequires: python3(pexpect)
BuildRequires: python3(samba)
BuildRequires: spice-html5 < 0.2.2
BuildRequires: iproute2

%if_with check
BuildRequires: /proc
BuildRequires: /dev/pts
BuildRequires: libnm-gir
BuildRequires: libjson-glib-gir
BuildRequires: python3(dbusmock)
BuildRequires: python3(ipalib)
BuildRequires: python3(six)
BuildRequires: python3(sqlite3)
BuildRequires: samba-common
%endif

# don't generate Python2 auto requires
%add_python3_path %_datadir/fleet-commander-admin/python/
%add_python3_compile_exclude %_datadir/fleet-commander-admin/python/

Requires: cockpit
Requires: python3-module-freeipa-desktop-profile-client
Requires: realmd
Requires: samba-common
Requires: spice-html5 < 0.2.2

%description
Fleet Commander is an application that allows you to manage the desktop
configuration of a large network of users and workstations/laptops.

It is primarily targeted to Linux systems based on the GNOME desktop.

Fleet Commander consists on two components:

* a web service integrated with Apache that serves the dynamic application and
  the profile data to the network.
* and a client side daemon that runs on every host of the network.

Fleet Commander relies on libvirt and KVM to generate the profile data
dynamically from a template VM running the same environment as the rest of the
network.

%package -n fleet-commander-logger
Summary: Logs configuration changes in a session
Group: System/Base
# don't generate Python2 auto requires
%add_python3_path %_datadir/fleet-commander-logger/python/
%add_python3_compile_exclude %_datadir/fleet-commander-logger/python/
Requires: libnm-gir

%description -n fleet-commander-logger
Logs changes for Fleet Commander virtual sessions.

%prep
%setup
%patch -p1

# for now skip tests which require real system/session dbus
grep -qs '^TESTS[[:space:]]*=.* 01_logger_dconf\.sh .* 03_logger_nm\.py ' \
tests/Makefile.am || exit 1
sed -i '/^TESTS[[:space:]]*=/{s/01_logger_dconf\.sh//g;s/03_logger_nm\.py//g}' \
tests/Makefile.am

# udev rules are located on /lib/udev/
grep -qs '${prefix}/lib/udev/rules\.d' \
data/Makefile.am || exit 1
sed -i 's/${prefix}\/lib\/udev\/rules\.d/\/lib\/udev\/rules\.d/g' \
data/Makefile.am

# runuser is not on user PATH
grep -qs '^AC_PATH_PROG(\[RUNUSER\], \[runuser\])$' configure.ac || exit 1
sed -i '/^AC_PATH_PROG(\[RUNUSER\], \[runuser\])$/{s/)$/, "$PATH:\/sbin")/g}' \
configure.ac

grep -qsr '#!/usr/bin/env[[:space:]]\+python-wrapper.sh' ./tests/ || exit 1
grep -rl '#!/usr/bin/env[[:space:]]\+python-wrapper.sh' | \
xargs sed -i 's/#!\/usr\/bin\/env[[:space:]]\+python-wrapper.sh/#!\/usr\/bin\/python3/g'

grep -qs '#!/usr/bin/env[[:space:]]\+bash[[:space:]]*$' \
data/fleet-commander-logger.in || exit 1
sed -i 's/#!\/usr\/bin\/env[[:space:]]\+bash[[:space:]]*$/#!\/bin\/bash/g' data/fleet-commander-logger.in

grep -qs '/usr/bin/env[[:space:]]\+@PYTHON@[[:space:]]\+' \
data/fleet-commander-logger.in || exit 1
sed -i 's/#!\/usr\/bin\/env[[:space:]]\+@PYTHON@[[:space:]]\+/#!\/usr\/bin\/@PYTHON@ /g' \
data/fleet-commander-logger.in

# raise timeouts for aarch64/beehive
grep -qsF 'time.sleep(0.1)' tests/_wait_for_name.py || exit 1
sed -i 's/time\.sleep(0\.1)/time.sleep(1)/g' tests/_wait_for_name.py

# we use a packaged spice-html5 instead of bundled;
# in such a case this directory should be empty
[ ! "$(ls -A admin/cockpit/fleet-commander-admin/js/spice-html5)" ] || exit 1
rm -r admin/cockpit/fleet-commander-admin/js/spice-html5
# use here a symlink to ensure that our packaged version is synced with bundled
# one
ln -s %_datadir/spice-html5 admin/cockpit/fleet-commander-admin/js/

%build
%autoreconf
export PYTHON=python3
%configure \
    --with-systemdsystemunitdir=%_unitdir
%make_build

%install
%makeinstall_std
install -m 755 -d %buildroot/%_localstatedir/lib/fleet-commander-admin/profiles
# remove bundled spice-html5
rm -r %buildroot%_datadir/cockpit/fleet-commander-admin/js/spice-html5
ln -s %_datadir/spice-html5 %buildroot%_datadir/cockpit/fleet-commander-admin/js/

%check
%make check || { cat ./tests/test-suite.log; exit 1; }

%files
%doc README
%dir %_datadir/fleet-commander-admin
%_datadir/fleet-commander-admin/fc-goa-providers.ini
%dir %_datadir/fleet-commander-admin/python
%dir %_datadir/fleet-commander-admin/python/fleetcommander
%attr(644, root, root) %_datadir/fleet-commander-admin/python/fleetcommander/*.py

%_datadir/pixmaps/fc-admin.png
%_datadir/cockpit/fleet-commander-admin/
%_datadir/dbus-1/services/org.freedesktop.FleetCommander.service
%config(noreplace) %_xdgconfigdir/fleet-commander-admin.conf
%_localstatedir/lib/fleet-commander-admin
%attr(755, root, root) %_libexecdir/fleet-commander-admin
%_datadir/metainfo/org.freedesktop.FleetCommander.admin.metainfo.xml

%files -n fleet-commander-logger
%doc README
%attr(755, root, root) %_libexecdir/fleet-commander-logger
%attr(755, root, root) %_libexecdir/firefox-bookmark-fclogger
%dir %_datadir/fleet-commander-logger
%_datadir/fleet-commander-logger/fc-chromium-policies.json
%dir %_datadir/fleet-commander-logger/python
%attr(644, root, root) %_datadir/fleet-commander-logger/python/*.py
%_xdgconfigdir/autostart/fleet-commander-logger.desktop
%_udevrulesdir/81-fleet-commander-logger.rules
%_libdir/mozilla/native-messaging-hosts/firefox_bookmark_fclogger.json
%_datadir/mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/{c73e87a7-b5a1-4b6f-b10b-0bd70241a64d}.xpi

%changelog
* Fri Jun 05 2020 Stanislav Levin <slev@altlinux.org> 0.15.1-alt0.M90P.1
- Backported 0.15.1 to P9 from Sisyphus.

* Mon Apr 27 2020 Stanislav Levin <slev@altlinux.org> 0.15.1-alt1
- 0.14.1 -> 0.15.1.
- Applied upstream fixes.

* Thu Nov 28 2019 Stanislav Levin <slev@altlinux.org> 0.14.1-alt1
- 0.14.0 -> 0.14.1.

* Thu Mar 14 2019 Stanislav Levin <slev@altlinux.org> 0.14.0-alt2
- Fixed install public key into libvirt host.

* Wed Feb 27 2019 Stanislav Levin <slev@altlinux.org> 0.14.0-alt1
- 0.12.1 -> 0.14.0.
- Fixed display of Chrome changes in UI.

* Wed Jan 16 2019 Stanislav Levin <slev@altlinux.org> 0.12.1-alt1.gitfd695dc
- Initial build.


