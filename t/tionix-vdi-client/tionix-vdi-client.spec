Name: tionix-vdi-client
Version: 2.6.0
Release: alt5

Summary: Tionix VDI client
License: GPL-2.0
Group: Communications

Url: http://tionix.ru
Source: %name-%version-src.zip
Patch: %name-%version.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-requests
BuildRequires: python3-module-prettytable
BuildRequires: python3-module-PyQt5
BuildRequires: python3-module-pyasn1
BuildRequires: python3-module-OpenSSL
BuildRequires: python3-module-pykcs11
BuildRequires: python3-module-Cython
BuildRequires: unzip
# for version test
BuildRequires: libfreerdp

Requires: openvpn
Requires: xfreerdp
Requires: freerdp-plugins-standard

%description
%summary.

%prep
%setup -c %name-%version
%patch -p1

# p9_e2k still with freerdp 2.0.0 barfing at this argument for 2.1+
[ -f %_prefix/%_lib/libfreerdp2.so.2.0.0 ] &&
	sed -i 's,/cert:tofu ,,' tionix_vdi_client/settings.py

%filter_from_requires /^python3(tionix_client.*)/d
%filter_from_requires /^python3(mock)/d
%filter_from_requires /^python3(pbr)/d

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install

%files
%_bindir/tionix_vdi_client
%python3_sitelibdir/*

%changelog
* Tue Sep 08 2020 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt5
- This software is licensed under the terms of GPLv2.

* Tue May 26 2020 Michael Shigorin <mike@altlinux.org> 2.6.0-alt4
- Add missing R:, suppress superfluous generated ones.
- Fix xfreerdp 2.0 support (for p9_e2k).
- Fix License:.

* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt3
- Fix Python3 migration in smartcard support part.
- Support old version of xfreerdp.

* Sun May 24 2020 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt2
- Remove python-module-cliff requirement, use PyQt5 instead of PySide2.
- Build with Python3.
- Do not show messagebox with error caused by session logout on server.

* Sun May 17 2020 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- Initial build.
