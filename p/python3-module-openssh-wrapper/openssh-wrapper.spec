%define oname openssh-wrapper

Name: python3-module-%oname
Version: 0.5
Release: alt1

Summary: Python wrapper around OpenSSH client.
License: %bsd
Group: Development/Python3
Url: https://pypi.org/project/openssh-wrapper/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-build-licenses


%description
Python wrapper around OpenSSH client intended to execute commands
on remote servers.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*


%changelog
* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5-alt1
- Initial build.

