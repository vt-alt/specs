%define oname tqdm

%def_disable check

Name: python3-module-%oname
Version: 4.48.0
Release: alt1

Summary: A fast, extensible progress bar for Python and CLI

License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/tqdm

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-nose python3-module-flake8 python3-module-coverage

%py3_provides %oname

%description
tqdm means "progress" in Arabic (taqadum) and an abbreviation
for "I love you so much" in Spanish (te quiero demasiado).

Instantly make your loops show a smart progress meter -
just wrap any iterable with tqdm(iterable), and you're done!

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
%python3_test
py.test3

%files
%doc *.rst
%_bindir/tqdm
%python3_sitelibdir/*

%changelog
* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.48.0-alt1
- 4.48.0 released

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 4.42.1-alt2
- add conflicts/obsoletes for python-module-tqdm (due bindir/tqdm)

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 4.42.1-alt1
- build separate python3 module
- new version 4.42.1 (with rpmrb script)

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.15.0-alt1
- Initial build for ALT.
