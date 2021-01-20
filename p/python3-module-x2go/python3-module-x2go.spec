%define modulename x2go

Name:    python3-module-%modulename
Version: 0.6.1.3
Release: alt2
Summary: Python module providing X2Go client API
Group:	 Communications 

License: AGPL-3.0-or-later
URL:     https://www.x2go.org/
Source0: %name-%version.tar
Patch0:  fix-sshbroker-error.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires:      python3-dev
BuildRequires:      python3-module-setuptools
BuildRequires:      /usr/bin/2to3
BuildRequires:      python3-module-gevent
BuildRequires:      python3-module-paramiko
BuildRequires:      python3-module-requests
BuildRequires:      python3-module-simplejson
BuildRequires:      python3-module-xlib
Requires:           nxproxy
Requires:           python3-module-gevent
Requires:           python3-module-paramiko
Requires:           python3-module-requests
Requires:           python3-module-simplejson
Requires:           python3-module-xlib

%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - session brokerage support
   - client side mass storage mounting support
   - audio support
   - authentication by smartcard and USB stick

This Python module allows you to integrate X2Go client support into your
Python applications by providing a Python-based X2Go client API.

%prep
%setup -q
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%doc ChangeLog README* TODO COPYING
%python3_sitelibdir/x2go*

%changelog
* Wed Jan 13 2021 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.6.1.3-alt2
- Fix sshbroker error

* Fri Dec 18 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.6.1.3-alt1
- Initial build for Sysiphus

