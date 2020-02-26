%define module_name scapy

Name: scapy
Version: 2.4.3
Release: alt2

Summary: Scapy is a powerful interactive packet manipulation program written in Python

Group: Networking/Other
License: GPLv2
Url: http://www.secdev.org/projects/scapy/

# Source-url: https://github.com/secdev/scapy/archive/v%version.zip
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

Requires: python3-module-scapy = %EVR

Requires: tcpdump

BuildRequires: python3-devel python3-module-setuptools
BuildRequires(pre): rpm-build-python3

%add_python3_req_skip scapy.modules.six.moves scapy.modules.six.moves.queue

%description
Scapy is a powerful interactive packet manipulation program.
It is able to forge or decode packets of a wide number of protocols,
send them on the wire, capture them, match requests and replies, and
much more.
It can easily handle most classical tasks like scanning, tracerouting,
probing, unit tests, attacks or network discovery.

%package -n python3-module-%name
Summary: Python module for %name.
Group: Development/Python

%description -n python3-module-%name
Powerful interactive packet manipulation python module scapy.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/%name/arch/windows

%files
%_bindir/*scapy
%_man1dir/*

%files -n python3-module-scapy
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-*egg-info

%changelog
* Sun Dec 08 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt2
- fix license (GPLv2 really)

* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3 (with rpmrb script)
- switch to python3

* Fri Aug 16 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version 2.4.0 (with rpmrb script)

* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Tue Mar 01 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Tue Mar 01 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt2
- cleanup spec, separate python module
- add tcpdump require

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt1.1
- Rebuild with Python-2.7

* Tue Aug 30 2011 Denis Klimov <zver@altlinux.org> 2.1.0-alt1
- new version
- using python macros in build and install sections
- format description

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0.10-alt1.1
- Rebuilt with python 2.6

* Thu Oct 16 2008 Mikhail Pokidko <pma@altlinux.org> 2.0.0.10-alt1
- Migrating to version 2.0.0.10

* Fri Apr 25 2008 Mikhail Pokidko <pma@altlinux.org> 1.1.1-alt1
- Initial ALT build

