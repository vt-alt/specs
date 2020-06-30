
Name: linstor-client
Summary: Linstor Client
Version: 1.1.2
Release: alt1
Group: Development/Python3
License: GPLv3
URL: https://github.com/LINBIT/linstor-client
Source: http://www.linbit.com/downloads/linstor/linstor-client-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-linstor

%description
User space client to ease DRBD9 resource management.
Linstor, developed by LINBIT, is a software that manages DRBD replicated LVM/ZFS volumes
across a group of machines. It maintains DRBD configuration on the participating machines.
It creates/deletes the backing LVM/ZFS volumes.
It automatically places the backing LVM/ZFS volumes among the participating machines.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%_bindir/*
%_sysconfdir/bash_completion.d/*
%_man8dir/*
%python3_sitelibdir/*

%changelog
* Sat Jun 29 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- Initial build for ALT
