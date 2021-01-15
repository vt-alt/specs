Name:      pyhoca-cli
Version:   0.6.1.2
Release:   alt1
Summary:   Command line X2Go client written in Python
Group:     Communications

License:   AGPL-3.0-or-later
URL:       http://www.x2go.org/
Source0:   %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires:      python3-dev
BuildRequires:      python3-module-setuptools
Requires:           python3-module-setproctitle
Requires:           python3-module-x2go

%description
X2Go is a server based computing environment with:
   - session resuming
   - low bandwidth support
   - LDAP support
   - client side mass storage mounting support
   - client side printing support
   - audio support
   - authentication by smartcard and USB stick

PyHoca-CLI provides a simple and flexible command line client
written in Python that allows you to control X2Go client sessions
on desktops and thin clients.

%prep
%setup

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot/%_bindir
cp -p %name %buildroot/%_bindir/
mkdir -p %buildroot/%_mandir/
cp -rp man/* %buildroot/%_mandir/

%files
%doc README TODO COPYING
%_bindir/%name
%python3_sitelibdir/PyHoca_CLI-*
%python3_sitelibdir/pyhoca/
%_mandir/man1/%name.1*

%changelog
* Fri Dec 18 2020 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.6.1.2-alt1
- Initial build for Sisyphus

