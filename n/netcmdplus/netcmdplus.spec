Name: netcmdplus
Version: 0.1.1
Release: alt2

Summary: Extended samba-tool (netcmd) version
License: GPLv3+
Group: System/Configuration/Other

Url: http://git.altlinux.org/people/manowar/packages/netcmdplus.git
Packager: Paul Wolneykien <manowar@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: rpm-build-python3
BuildRequires: /usr/bin/2to3

Conflicts: %name < %EVR
Obsoletes: %name < %EVR

%description
netcmdplus extends samba-tool "user" and "group" commands with additional operations.

%package -n python3-module-%name
Summary: python3 module for samba-tool-plus (netcmdplus)
License: GPLv3+
Group: Development/Python3

%description -n python3-module-%name
netcmdplus extends samba-tool "user" and "group" commands with additional operations.
This package contains Python3 module code that extends samba.netcmd package.

%prep
%setup
find . -type f -name '*.py' -exec \
    sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' '{}' +
find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' bin/samba-tool-plus
2to3 -w -n bin/samba-tool-plus

%build
%python3_build

%install
%python3_install

%files
%_bindir/samba-tool-plus

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jan 23 2020 Grigory Ustinov <grenka@altlinux.org> 0.1.1-alt2
- Transfer to python3.

* Mon May 22 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Added "group update" subcommand.

* Wed May 17 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
