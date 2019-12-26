%define _unpackaged_files_terminate_build 1

%define _localstatedir %_var
%define _libexecdir    /usr/libexec
%define cockpit_user   _cockpit-ws
%define cockpit_group  _cockpit-ws
%define cockpit_wsinstance_user  _cockpit-wsinstance

%def_with dashboard
%def_with basic
%def_with optional
%def_with doc

%ifarch aarch64 x86_64 ppc64le
%def_enable docker
%else
%def_disable docker
%endif
%def_with check

# currently are not packaged on ALTLinux
# https://pcp.io/
%def_without pcp
# https://github.com/dm-vdo/vdo
%def_with vdo
# http://www.freedesktop.org/software/PackageKit
%def_without packagekit
#

###############################################################################

Name: cockpit
Version: 208
Release: alt1

Summary: Web Console for Linux servers
License: LGPLv2+
Group: System/Base
# Source-git: https://github.com/cockpit-project/cockpit.git
Url: https://cockpit-project.org/
Source0: %name-%version.tar
Source1: cockpit.alt.pam
Source2: node_modules.tar.gz
Patch: %name-%version-alt.patch

BuildRequires: node
BuildRequires: libgnutls-devel
BuildRequires: libjson-glib-devel
BuildRequires: libsystemd-devel
BuildRequires: libpolkit-devel
BuildRequires: libkrb5-devel
BuildRequires: libpam0-devel

%if_with dashboard
BuildRequires: libssh-devel
%endif

%if_with doc
BuildRequires: xsltproc
BuildRequires: xmlto
%endif

%if_with pcp
BuildRequires: pcp-libs-devel
%endif

%if_with check
BuildRequires: glib-networking
BuildRequires: polkit
BuildRequires: openssh-common
BuildRequires: openssh-clients
BuildRequires: dbus
BuildRequires: /proc
BuildRequires: /dev/pts
%endif

Requires: cockpit-bridge
Requires: cockpit-ws
Requires: cockpit-system
# Optional components
%if_with dashboard
Requires: cockpit-dashboard
%endif
%if_enabled docker
Requires: cockpit-docker
%endif
Requires: cockpit-networkmanager
Requires: cockpit-storaged
%if_with packagekit
Requires: cockpit-packagekit
%endif
%if_with pcp
Requires: cockpit-pcp
%endif
Requires: cockpit-selinux

%description
The Cockpit Web Console enables users to administer GNU/Linux servers using a
web browser.

It offers network configuration, log inspection, diagnostic reports, SELinux
troubleshooting, interactive command-line sessions, and more.

###############################################################################
%if_with basic

%package bridge
Summary: Cockpit bridge server-side component
Group: System/Base
Requires: glib-networking

%description bridge
The Cockpit bridge component installed server side and runs commands on the
system on behalf of the web based user interface.

###############################################################################

%package ssh
Summary: Cockpit ssh server-side component
Group: System/Base

%description ssh
The Cockpit ssh component installed server side and runs commands on the
system on behalf of the web based user interface.

###############################################################################

%package doc
Summary: Cockpit deployment and developer guide
Group: Documentation
BuildArch: noarch

%description doc
The Cockpit Deployment and Developer Guide shows sysadmins how to
deploy Cockpit on their machines as well as helps developers who want to
embed or extend Cockpit.

###############################################################################

%package system
Summary: Cockpit admin interface package for configuring and troubleshooting a system
Group: System/Base
BuildArch: noarch
Requires: libpwquality
Requires: cockpit-bridge >= %EVR
Requires: cockpit-realmd = %EVR
Requires: cockpit-shell = %EVR
Requires: cockpit-systemd = %EVR
Requires: cockpit-tuned = %EVR
Requires: cockpit-users = %EVR
%description system
This package contains the Cockpit shell and system configuration interfaces.

###############################################################################

%package realmd
Summary: Cockpit admin interface package for configuring realmd
Group: System/Base
BuildArch: noarch

%description realmd
This package contains the Cockpit realmd configuration interfaces.

###############################################################################

%package shell
Summary: Cockpit admin interface package for configuring shell
Group: System/Base
BuildArch: noarch

%description shell
This package contains the Cockpit shell configuration interfaces.

###############################################################################

%package systemd
Summary: Cockpit admin interface package for configuring systemd
Group: System/Base
BuildArch: noarch

%description systemd
This package contains the Cockpit systemd configuration interfaces.

###############################################################################

%package tuned
Summary: Cockpit admin interface package for configuring tuned
Group: System/Base
BuildArch: noarch

%description tuned
This package contains the Cockpit tuned configuration interfaces.

###############################################################################

%package users
Summary: Cockpit admin interface package for configuring users
Group: System/Base
BuildArch: noarch

%description users
This package contains the Cockpit users configuration interfaces.

###############################################################################

%package ws
Summary: Cockpit Web Service
Group: System/Base
Requires: glib-networking
Requires: glib2 >= 2.37.4
# drop requirement on symlink, which is created at runtime
# by cockpit.socket service
%filter_from_requires /^\/run\/cockpit\/motd$/d

%description ws
The Cockpit Web Service listens on the network, and authenticates users.

###############################################################################

%package kdump
Summary: Cockpit user interface for kernel crash dumping
Group: System/Base
BuildArch: noarch
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: kexec-tools

%description kdump
The Cockpit component for configuring kernel crash dumping.

###############################################################################

%package sosreport
Summary: Cockpit user interface for diagnostic reports
Group: System/Base
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: sos
BuildArch: noarch

%description sosreport
The Cockpit component for creating diagnostic reports with the
sosreport tool.

###############################################################################

%package networkmanager
Summary: Cockpit user interface for networking, using NetworkManager
Group: System/Base
BuildArch: noarch
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: NetworkManager

%description networkmanager
The Cockpit component for managing networking. This package uses
NetworkManager.

###############################################################################

%package selinux
Summary: Cockpit SELinux package
Group: System/Base
BuildArch: noarch
Requires: cockpit-bridge
Requires: cockpit-shell
# not packaged yet
# Requires: setroubleshoot-server

%description selinux
This package contains the Cockpit user interface integration with the
utility setroubleshoot to diagnose and resolve SELinux issues.

###############################################################################

%endif # base

%if_with optional

%package storaged
Summary: Cockpit user interface for storage, using udisks
Group: System/Base
BuildArch: noarch
Requires: cockpit-shell
Requires: udisks2
Requires: udisks2-module-lvm2
# not packaged in ALT
# Requires: udisks2-iscsi >= 2.6
Requires: multipath-tools
Requires: python-module-dbus

%description storaged
The Cockpit component for managing storage.  This package uses udisks.

###############################################################################

%package tests
Summary: Tests for Cockpit
Group: System/Base
Requires: cockpit-bridge
Requires: cockpit-system
Requires: openssh-clients

%description tests
This package contains tests and files used while testing Cockpit.
These files are not required for running Cockpit.

###############################################################################

%package machines
BuildArch: noarch
Summary: Cockpit user interface for virtual machines
Group: System/Base
Requires: cockpit-bridge
Requires: cockpit-system
Requires: libvirt
Requires: libvirt-client

%description machines
The Cockpit components for managing virtual machines.

If "virt-install" is installed, you can also create new virtual machines.

###############################################################################

%if_with pcp
%package pcp
Summary: Cockpit PCP integration
Group: System/Base
Requires: cockpit-bridge
Requires: pcp

%description pcp
Cockpit support for reading PCP metrics and loading PCP archives.
%endif

###############################################################################

%if_with dashboard
%package dashboard
Summary: Cockpit remote servers and dashboard
Group: System/Base
BuildArch: noarch
Requires: cockpit-ssh

%description dashboard
Cockpit support for connecting to remote servers (through ssh),
bastion hosts, and a basic dashboard.
%endif

###############################################################################

%package docker
Summary: Cockpit user interface for Docker containers
Group: System/Base
Requires: cockpit-bridge
Requires: cockpit-shell
Requires: docker-ce

%description docker
The Cockpit components for interacting with Docker and user interface.
This package is not yet complete.

###############################################################################

%if_with packagekit
%package packagekit
Summary: Cockpit user interface for packages
Group: System/Base
BuildArch: noarch
Requires: cockpit-bridge
# TODO package PackageKit http://www.freedesktop.org/software/PackageKit
# Requires: PackageKit

%description packagekit
The Cockpit components for installing OS updates and Cockpit add-ons,
via PackageKit.
%endif


%endif
###############################################################################

%prep
%setup
%patch -p1

tar -xzf %SOURCE2

echo '%version' > .tarball
# newusers executable is not on the user PATH
grep -q 'if newusers --help ' configure.ac || exit 1
sed -i 's/if newusers --help |/if "$NEWUSERS" --help |/' configure.ac

# systemd tmpfiles in ALTLinux are packaged into /lib/tmpfiles.d
grep -q 'tempconfdir = $(prefix)/lib/tmpfiles.d' src/ws/Makefile-ws.am || exit 1
sed -i '/tempconfdir = $(prefix)\/lib\/tmpfiles.d/{s@$(prefix)/lib/tmpfiles.d@%_tmpfilesdir@}' \
src/ws/Makefile-ws.am

# ALT uses /etc/openssh directory, not /etc/ssh one
grep -qr '/ssh/ssh_known_hosts' || exit 1
grep -rl '/ssh/ssh_known_hosts' | \
xargs sed -i 's/\/ssh\/ssh_known_hosts/\/openssh\/ssh_known_hosts/g'

# /usr/bin -> /bin
grep -qr '/usr/bin/true' || exit 1
grep -rl '/usr/bin/true' | xargs sed -i 's/\/usr\/bin\/true/\/bin\/true/g'

grep -qr '/usr/bin/false' || exit 1
grep -rl '/usr/bin/false' | xargs sed -i 's/\/usr\/bin\/false/\/bin\/false/g'

%build
%autoreconf

%configure \
    --disable-silent-rules \
    %{?_without_pcp:--disable-pcp } \
    %{?_without_doc:--disable-doc } \
    %{?_with_vdo:--with-vdo-package='"vdo"' } \
    --with-cockpit-user=%cockpit_user \
    --with-cockpit-ws-instance-user=%cockpit_wsinstance_user \
    --with-selinux-config-type=etc_t \
    --with-appstream-data-packages='[ "appstream-data" ]' \
    --with-nfs-client-package='"nfs-utils"' \
    --with-pamdir=/%_lib/security \
    %nil

%make -j4 all

%check
TMPDIR=/tmp %make -j4 check || { cat ./test-suite.log; exit 1; }

%install
%makeinstall_std
%make install-tests DESTDIR=%buildroot
mkdir -p %buildroot%_sysconfdir/pam.d
install -p -m 644 %SOURCE1 %buildroot%_sysconfdir/pam.d/cockpit
rm -f %buildroot/%_libdir/cockpit/*.so
rm -f %buildroot/usr/lib/firewalld/services/cockpit.xml

%if_without dashboard
rm -rf %buildroot/%_datadir/cockpit/dashboard
%endif

%if_without packagekit
rm -rf %buildroot/%_datadir/cockpit/packagekit
rm -rf %buildroot/%_datadir/cockpit/apps
%endif

%if_without pcp
rm -f %buildroot%_libexecdir/cockpit-pcp
rm -f %buildroot%_localstatedir/lib/pcp/config/pmlogconf/tools/cockpit
rm -rf %buildroot%_datadir/cockpit/pcp/
%endif

%if_disabled docker
rm -rf %buildroot/%_datadir/cockpit/docker/
%endif

%if_without basic
for pkg in base1 branding motd kdump networkmanager realmd selinux shell sosreport ssh static systemd tuned users; do
    rm -r %buildroot/%_datadir/cockpit/$pkg
    rm -f %buildroot/%_datadir/metainfo/org.cockpit-project.cockpit-${pkg}.metainfo.xml
done
for data in doc locale man pixmaps polkit-1; do
    rm -r %buildroot/%_datadir/$data
done
for lib in systemd tmpfiles.d; do
    rm -r %buildroot/lib/$lib
done
for libexec in cockpit-askpass cockpit-session cockpit-ws cockpit-tls cockpit-desktop; do
    rm %buildroot/%_libexecdir/$libexec
done
rm -r %buildroot/%_lib/security
rm -r %buildroot/%_sysconfdir/{pam.d,motd.d,issue.d}
rm %buildroot%_bindir/cockpit-bridge %buildroot%_sbindir/remotectl
rm -f %buildroot%_libexecdir/cockpit-ssh
rm -f %buildroot%_datadir/metainfo/cockpit.appdata.xml

%else
%find_lang cockpit
%endif

%if_without optional
for pkg in apps dashboard docker machines packagekit pcp playground storaged; do
    rm -rf %buildroot/%_datadir/cockpit/$pkg
done
rm -r %buildroot/usr/lib/cockpit-test-assets %buildroot/%_sysconfdir/cockpit/cockpit.conf
rm -r %buildroot/%_libexecdir/cockpit-pcp %buildroot/%_localstatedir/lib/pcp/
rm -f %buildroot%_datadir/metainfo/org.cockpit-project.cockpit-machines.metainfo.xml
rm -f %buildroot%_datadir/metainfo/org.cockpit-project.cockpit-storaged.metainfo.xml
%endif

# don't package css and js debug files
rm -rf %buildroot%_usrsrc/debug

# remove not default brandings, as they have broken symlinks
for brand in centos debian fedora rhel ubuntu scientific; do
    rm -r %buildroot%_datadir/cockpit/branding/$brand
done
###############################################################################

%if_with basic

%files
%doc AUTHORS COPYING README.md
%dir %_datadir/cockpit
%_datadir/metainfo/cockpit.appdata.xml
%_datadir/pixmaps/cockpit.png
%doc %_man1dir/cockpit.1.*

%files bridge
%doc %_man1dir/cockpit-bridge.1.*
%_sysconfdir/cockpit/machines.d/
%_datadir/cockpit/base1/
%_datadir/polkit-1/actions/org.cockpit-project.cockpit-bridge.policy
%_bindir/cockpit-bridge
%_libexecdir/cockpit-askpass

%files ssh
%_datadir/cockpit/ssh/
%_libexecdir/cockpit-ssh

%files doc
%_docdir/cockpit

%files system

%files realmd
%_datadir/cockpit/realmd/

%files shell
%_datadir/cockpit/shell/

%files systemd
%_datadir/cockpit/systemd/

%files tuned
%_datadir/cockpit/tuned/

%files users
%_datadir/cockpit/users/

%files ws -f cockpit.lang
%doc %_man1dir/cockpit-desktop.1.*
%doc %_man5dir/cockpit.conf.5.*
%doc %_man8dir/cockpit-ws.8.*
%doc %_man8dir/cockpit-tls.8.*
%doc %_man8dir/remotectl.8.*
%doc %_man8dir/pam_ssh_add.8.*
%config(noreplace) %_sysconfdir/cockpit/ws-certs.d/
%config(noreplace) %_sysconfdir/pam.d/cockpit
%config %_sysconfdir/issue.d/cockpit.issue
%config %_sysconfdir/motd.d/cockpit
%_datadir/cockpit/motd/update-motd
%_datadir/cockpit/motd/inactive.motd
%_unitdir/cockpit.service
%_unitdir/cockpit-motd.service
%_unitdir/cockpit.socket
%_unitdir/cockpit-wsinstance-http.socket
%_unitdir/cockpit-wsinstance-http.service
%_unitdir/cockpit-wsinstance-http-redirect.socket
%_unitdir/cockpit-wsinstance-http-redirect.service
%_unitdir/cockpit-wsinstance-https-factory.socket
%_unitdir/cockpit-wsinstance-https-factory@.service
%_unitdir/cockpit-wsinstance-https@.socket
%_unitdir/cockpit-wsinstance-https@.service
%_unitdir/system-cockpithttps.slice
%_tmpfilesdir/cockpit-tempfiles.conf
%_sbindir/remotectl
/%_lib/security/pam_ssh_add.so
%_libexecdir/cockpit-ws
%_libexecdir/cockpit-wsinstance-factory
%_libexecdir/cockpit-tls
%_libexecdir/cockpit-desktop
%attr(4710, root, %cockpit_wsinstance_user) %_libexecdir/cockpit-session
%attr(775, root, wheel) %_sharedstatedir/cockpit
%_datadir/cockpit/static/
%_datadir/cockpit/branding/

%pre ws
%_sbindir/groupadd -r -f %cockpit_group >/dev/null 2>&1 ||:
%_sbindir/useradd -r -g %cockpit_group -d %_sharedstatedir/cockpit -s \
/dev/null -c "User for cockpit web service" %cockpit_user >/dev/null 2>&1 ||:

%_sbindir/groupadd -r -f %cockpit_wsinstance_user >/dev/null 2>&1 ||:
%_sbindir/useradd -r -g %cockpit_wsinstance_user -d %_sharedstatedir/cockpit -s \
/dev/null -c "User for cockpit-ws instances" %cockpit_wsinstance_user >/dev/null 2>&1 ||:

%post ws
if [ $1 -eq 1 ] ; then
        # Initial installation
        systemctl --no-reload -q preset cockpit.socket ||:
fi

%preun ws
if [ $1 -eq 0 ] ; then
        # Package removal, not upgrade
        systemctl --no-reload -q disable cockpit.socket ||:
fi

%postun ws
if [ $1 -ge 1 ] ; then
        # Package upgrade, not uninstall
        systemctl daemon-reload ||:
        systemctl try-restart cockpit.socket ||:
        systemctl try-restart cockpit.service ||:
fi

%files kdump
%_datadir/cockpit/kdump/
%_datadir/metainfo/org.cockpit-project.cockpit-kdump.metainfo.xml

%files sosreport
%_datadir/cockpit/sosreport/
%_datadir/metainfo/org.cockpit-project.cockpit-sosreport.metainfo.xml
%_datadir/pixmaps/cockpit-sosreport.png

%files networkmanager
%_datadir/cockpit/networkmanager/

%files selinux
%_datadir/cockpit/selinux/
%_datadir/metainfo/org.cockpit-project.cockpit-selinux.metainfo.xml

%endif # build basic packages

%if_with optional

%files storaged
%_datadir/cockpit/storaged/
%_datadir/metainfo/org.cockpit-project.cockpit-storaged.metainfo.xml

%files tests
%config(noreplace) %_sysconfdir/cockpit/cockpit.conf
%_datadir/cockpit/playground/
/usr/lib/cockpit-test-assets/

%files machines
%_datadir/cockpit/machines/
%_datadir/metainfo/org.cockpit-project.cockpit-machines.metainfo.xml

%if_with pcp
%files pcp
%_libexecdir/cockpit-pcp
%_localstatedir/lib/pcp/config/pmlogconf/tools/cockpit
%_datadir/cockpit/pcp/

%post pcp
# HACK - https://bugzilla.redhat.com/show_bug.cgi?id=1185764
# We can't use "systemctl reload-or-try-restart" since systemctl might
# be out of sync with reality.
/usr/share/pcp/lib/pmlogger condrestart
%endif

%if_with dashboard
%files dashboard
%_datadir/cockpit/dashboard/
%endif

%if_enabled docker
%files docker
%_datadir/cockpit/docker/
%endif

%if_with packagekit
%files packagekit
%_datadir/cockpit/apps/
%_datadir/cockpit/packagekit/
%endif

%endif # build optional extension packages

%changelog
* Fri Nov 29 2019 Stanislav Levin <slev@altlinux.org> 208-alt1
- 202 -> 208.

* Thu Sep 05 2019 Stanislav Levin <slev@altlinux.org> 202-alt1
- 194 -> 202.

* Thu Jul 18 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 194-alt2
- Enabled docker and kubernetes subpackages on ppc64le.

* Mon May 27 2019 Stanislav Levin <slev@altlinux.org> 194-alt1
- 192 -> 194.

* Thu Apr 18 2019 Stanislav Levin <slev@altlinux.org> 192-alt1
- 191 -> 192.

* Tue Apr 16 2019 Stanislav Levin <slev@altlinux.org> 191-alt1
- 189 -> 191.
- Fixed FTBFS.

* Tue Mar 12 2019 Stanislav Levin <slev@altlinux.org> 189-alt1
- 187 -> 189.

* Thu Feb 07 2019 Stanislav Levin <slev@altlinux.org> 187-alt1
- 185 -> 187.
- Increased build timeout.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 185-alt1
- 180 -> 185.

* Wed Oct 17 2018 Stanislav Levin <slev@altlinux.org> 180-alt1
- Initial build.

