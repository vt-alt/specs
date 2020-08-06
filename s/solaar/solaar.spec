%def_with bootstrap

Name:           solaar
Version:        1.0.3
Release:        alt1

Group:          System/Configuration/Hardware
Summary:        Device manager for Logitech Unifying Receiver
URL:            https://pwr-solaar.github.io/Solaar/
BuildArch:      noarch
License:        GPL-2.0

Packager:	Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-gir
BuildRequires:  python3-module-pyudev

Requires:  	unifying-receiver-udev

%if_with bootstrap
%add_python3_req_skip gi.repository.GObject gi.repository.Gdk
%endif

# typelib(AyatanaAppIndicator3) is not package in ALT Linux
%add_typelib_req_skiplist typelib(AyatanaAppIndicator3)

Source0:        https://github.com/pwr/Solaar/archive/%{version}.tar.gz

%description
Solaar is a device manager for Logitech's Unifying Receiver
peripherals. It is able to pair/unpair devices to the receiver, and
for most devices read battery status.

It comes in two flavors, command-line and GUI. Both are able to list
the devices paired to a Unifying Receiver, show detailed info for each
device, and also pair/unpair supported devices with the receiver.

%package doc
Group:          Documentation
Summary:        Documentation for Solaar
Requires:       %name = %version-%release
BuildArch:      noarch

%description doc
This package provides documentation for Solaar, a device manager for
Logitech's Unifying Receiver peripherals.

%prep
%setup -q -n Solaar-%version

%build
%python3_build

%install
%python3_install
install -Dm0644 share/autostart/solaar.desktop %buildroot%_sysconfdir/xdg/autostart/solaar.desktop
install -Dm0644 rules.d/42-logitech-unify-permissions.rules %buildroot%_sysconfdir/udev/rules.d/42-logitech-unify-permissions.rules

%files
%doc COPYRIGHT share/README
%config(noreplace) %_sysconfdir/xdg/autostart/solaar.desktop
%_sysconfdir/udev/rules.d/*.rules
%_bindir/solaar
%python3_sitelibdir/*
%_datadir/solaar/
%_desktopdir/solaar.desktop
%_iconsdir/hicolor/scalable/apps/solaar.svg

%files doc
%doc docs

%changelog
* Thu Aug 06 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- New version.
- Package udev rules.
- Fix License tag according to SPDX.

* Wed May 27 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version.

* Tue May 12 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version.

* Mon Apr 22 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.2.0.225.gitd021d87-alt1
- Build from recent commit for pyhon3.7 compatibility.

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.2-alt1.2
- rebuild

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- Build for Sisyphus from Fedora
