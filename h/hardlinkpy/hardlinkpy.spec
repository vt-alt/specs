%def_without check

Name: hardlinkpy
Version: 0.0.20180725
Release: alt1

Summary: Rewrite in python of the hardlink utility
License: GPL-2.0
Group: File tools

Url: https://github.com/akaihola/hardlinkpy
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3-devel

Obsoletes: hardlink++
Provides: hardlink++ = %name-%version

%description
A rewrite of the hardlink utility in python, which recursively parses
directory structures and creates hard links for identical files found.

%prep
%setup
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' hardlink.py

%install
install -pDm755 hardlink.py %buildroot%_bindir/%name

%check
%__python3 tests.py

%files
%_bindir/%name
%doc AUTHORS.rst COPYING README.rst

%changelog
* Wed Nov 06 2019 Anton Midyukov <antohami@altlinux.org> 0.0.20180725-alt1
- switch to git
- new snapshot
- switch to python3

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.20071114-alt1.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.20071114-alt1.1
- Rebuilt with python 2.6

* Mon Aug 10 2009 Michael Shigorin <mike@altlinux.org> 0.0.20071114-alt1
- built for ALT Linux (based on DAG's package)
- spec cleanup
