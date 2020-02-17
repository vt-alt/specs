%define git g55918d9
%define _libexec %_prefix/libexec
%def_enable test

Name: bolt
Version: 0.8
Release: alt0.1.%git
Summary: Thunderbolt device manager
Group: System/Libraries
License: LGPLv2+
Url: https://gitlab.freedesktop.org/bolt/bolt
Source0: %url/-/archive/%version/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: asciidoc-a2x
BuildRequires: libudev-devel
BuildRequires: libgio-devel
BuildRequires: libudev-devel
BuildRequires: libsystemd-devel
BuildRequires: libpolkit-devel

# for the integration test (optional)
%if_enabled test
BuildRequires: python3-module-pygobject3-devel
BuildRequires: python3-module-dbus
BuildRequires: python3-module-dbusmock
BuildRequires: libumockdev-devel
%endif

%description
bolt is a system daemon to manage thunderbolt 3 devices via a D-BUS
API.  Thunderbolt 3 features different security modes that require
devices to be authorized before they can be used. The D-Bus API can be
used to list devices, enroll them (authorize and store them in the
local database) and forget them again (remove previously enrolled
devices). It also emits signals if new devices are connected (or
removed). During enrollment devices can be set to be automatically
authorized as soon as they are connected.  A command line tool, called
boltctl, can be used to control the daemon and perform all the above
mentioned tasks.

%prep
%setup
%patch -p1

%build
%meson -Ddb-name=boltd \
       -Dman=true \
       --libexecdir=%_libexec
%meson_build

%if_enabled test
%check
%meson_test
%endif

%install
%meson_install

%files
%doc COPYING README.md
%_bindir/boltctl
%_libexec/boltd
%_unitdir/%name.service
%_udevrulesdir/*-%name.rules
%_sysconfdir/dbus-1/system.d/org.freedesktop.bolt.conf
%_datadir/dbus-1/interfaces/org.freedesktop.bolt.xml
%_datadir/polkit-1/actions/org.freedesktop.bolt.policy
%_datadir/polkit-1/rules.d/org.freedesktop.bolt.rules
%_datadir/dbus-1/system-services/org.freedesktop.bolt.service
%_man1dir/boltctl.1*
%_man8dir/boltd.8*
%ghost %dir %_localstatedir/boltd

%changelog
* Mon Jun 03 2019 L.A. Kostis <lakostis@altlinux.ru> 0.8-alt0.1.g55918d9
- Initial build for ALTLinux.
- GIT 55918d9.
