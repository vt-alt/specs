%global pypi_name validity

Name: python-%pypi_name
Version: 0.12
Release: alt0.2
Summary: Validity fingerprint sensor driver
Group: Development/Python

License: MIT
Url: https://github.com/uunicorn/%name
Source0: https://github.com/uunicorn/%name/archive/refs/tags/%version.tar.gz#/%name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: python-validity-0.12-restart-always.patch
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%package -n python3-module-%pypi_name
Summary: %summary
Group: Development/Python
Requires: innoextract
Requires: open-fprintd, fprintd-clients

%description
Validity fingerprint sensor driver.

%description -n python3-module-%pypi_name
Validity fingerprint sensor driver.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%python3_build

%install
%python3_install

install -d -m 0700 %buildroot%_sysconfdir/%name
install -d -m 0755 %buildroot%_unitdir/
install -d -m 0755 %buildroot%_udevrulesdir/
install -d -m 0755 %buildroot%_datadir/%name

install -m 0600 etc/python-validity/dbus-service.yaml %buildroot%_sysconfdir/%name/
install -m 0644 debian/python3-validity.service %buildroot%_unitdir/
install -m 0644 debian/python3-validity.udev %buildroot%_udevrulesdir/40-python3-validity.udev
install -m 0644 scripts/factory-reset.py %buildroot%_datadir/%name/playground/

%files -n python3-module-%pypi_name
%doc README.md LICENSE
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/dbus-service.yaml
%_unitdir/python3-validity.service
%_udevrulesdir/40-python3-validity.udev
%python3_sitelibdir/validitysensor/
%python3_sitelibdir/python_%pypi_name-%version-py*.egg-info/
%_bindir/validity-led-dance
%_bindir/validity-sensors-firmware
%dir %_libexecdir/%name
%_libexecdir/%name/dbus-service
%_datadir/dbus-1/system.d/io.github.uunicorn.Fprint.conf
%dir %_datadir/%name
%_datadir/%name/playground

%changelog
* Tue Jun 29 2021 L.A. Kostis <lakostis@altlinux.ru> 0.12-alt0.2
- Fix unowned dirs.

* Tue Jun 29 2021 L.A. Kostis <lakostis@altlinux.ru> 0.12-alt0.1
- Rebuild for ALTLinux.
- .spec based on Fedora.

* Tue Jun 22 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-3
- always restart service

* Wed Jun 16 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-2
- skip possible transaction errors

* Tue Nov 03 2020 Veit Wahlich <cru@zodia.de> - 0.12-1
- Initial build.
