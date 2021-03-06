%define oname websockify

Name: python-module-websockify
Version: 0.8.0
Release: alt2
Summary: WSGI based adapter for the Websockets protocol
Group: Development/Python

License: LGPLv3
Url: https://github.com/kanaka/%oname
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
Python WSGI based adapter for the Websockets protocol

%package -n python3-module-%oname
Summary: WSGI based adapter for the Websockets protocol
Group: Development/Python3

%description -n python3-module-%oname
Python WSGI based adapter for the Websockets protocol - Python 3 version

%prep
%setup

# remove unwanted shebang
sed -i '1 { /^#!/ d }' websockify/websocket*.py
# drop unneeded executable bit
chmod -x include/web-socket-js/web_socket.js

%build
%python_build
%python3_build

%install
%python_install
mv %buildroot%_bindir/websockify %buildroot%_bindir/websockify.py2
%python3_install

rm -Rf %buildroot/usr/share/websockify

%files
%doc LICENSE.txt README.md CHANGES.txt
%python_sitelibdir/*
%_bindir/websockify.py2

%files -n python3-module-%oname
%doc LICENSE.txt README.md CHANGES.txt
%python3_sitelibdir/*
%_bindir/websockify

%changelog
* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt2
- add python2 package

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Mar 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-2.fc21.src)

