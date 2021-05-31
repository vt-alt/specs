%define  modulename weasyprint

%def_disable check

Name:    python3-module-%modulename
Version: 47
Release: alt1

Summary: WeasyPrint converts web documents to PDF
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/Kozea/WeasyPrint

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-pytest-runner
%if_enabled check
BuildRequires: python3-module-pytest-runner python3-module-pyphen python3-module-tinycss2
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/*.egg-info
%_bindir/%modulename
%doc *.rst

%changelog
* Sat Jun 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 47-alt1
- Initial build for Sisyphus
