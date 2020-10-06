%define  modulename pychromecast

Name:    python3-module-%modulename
Version: 0.7
Release: alt1

Summary: Library for Python 3 to communicate with the Google Chromecast.
License: MIT
Group:   Development/Python3
URL:     https://github.com/home-assistant-libs/pychromecast

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Sun Sep 27 2020 Anton Midyukov <antohami@altlinux.org> 0.7-alt1
- Initial build for Sisyphus
