%define  modulename metaextract

Name:    python3-module-%modulename
Version: 1.0.7
Release: alt1

Summary: Get metadata for python modules
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/toabctl/metaextract

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-pytest-runner

BuildArch: noarch

Source:  %modulename-%version.tar

%description
metaextract is a tool to collect metadata about a python module. For example
you may have a sdist tarball from the Python Package Index and you want to know
it's dependencies. metaextract can collect theses dependencies. The tool was
first developed in py2pack but is now it's own module to be useful for others,
too.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/metaextract
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Fri Jul 24 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus
