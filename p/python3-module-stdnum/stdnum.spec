%define _unpackaged_files_terminate_build 1
%define oname stdnum

Name:       python3-module-%oname
Version:    1.11
Release:    alt1

Summary:    A provide functions to handle, parse and validate standard numbers.
License:    LGPL-2.1
Group:      Development/Python3
Url:        https://pypi.org/project/python-stdnum/
# https://github.com/arthurdejong/python-stdnum
BuildArch:  noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools


%description
A Python module to parse, validate and reformat standard numbers and codes
in different formats. It contains a large collection of number formats.

Basically any number or code that has some validation mechanism available
or some common formatting is eligible for inclusion in this library.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A Python module to parse, validate and reformat standard numbers and codes
in different formats. It contains a large collection of number formats.

Basically any number or code that has some validation mechanism available
or some common formatting is eligible for inclusion in this library.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

install -d %buildroot%python3_sitelibdir/%oname/tests
cp -fR tests/* %buildroot%python3_sitelibdir/%oname/tests

%files
%doc README COPYING docs/
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests


%changelog
* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.11-alt1
- Initial build for Sisyphus
