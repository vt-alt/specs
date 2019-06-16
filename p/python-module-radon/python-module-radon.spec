%define  oname radon

Name:    python-module-%oname
Version: 3.0.3
Release: alt1

Summary: Various code metrics for Python code

License: MIT
Group:   Development/Python
URL:     https://github.com/rubik/radon

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
Radon is a Python tool that computes various metrics from the source code.
Radon can compute:

* McCabe's complexity**, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

%prep
%setup -n %oname-%version

%build
%python_build
rm -r */lib/radon/tests

%install
%python_install
%if ""=="3"
mv %buildroot%_bindir/radon %buildroot%_bindir/radon
%endif

%files
%doc CHANGELOG README.rst
%_bindir/radon
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info/

%changelog
* Mon May 20 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.3-alt1
- Build new version.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus.
