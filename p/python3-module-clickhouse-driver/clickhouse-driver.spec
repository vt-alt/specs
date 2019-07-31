%define _unpackaged_files_terminate_build 1
%define oname clickhouse-driver


Name:       python3-module-%oname
Version:    0.0.20
Release:    alt1
BuildArch:  noarch

License:    %mit
Group:      Development/Python3
Summary:    ClickHouse Python Driver with native interface support.

Url:        https://github.com/mymarilyn/clickhouse-driver
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-sphinx


%description
ClickHouse Python Driver with native (TCP) interface support.

%package    docs
Group:      Development/Documentation
Summary:    ClickHouse Python Driver with native interface support.

%description docs
ClickHouse Python Driver with native (TCP) interface support.

Package contains documentation for %name.

%package    tests
Group:      Development/Python3
Summary:    ClickHouse Python Driver with native interface support.

Requires:   python3-module-%oname = %EVR

%description tests
ClickHouse Python Driver with native (TCP) interface support.

Package contains tests for %name.

%prep
%setup

%build
%python3_build

export PYTHONPATH=$PWD
%make -C docs/ man

%install
%python3_install

cp -fR tests/ %buildroot%python3_sitelibdir/clickhouse_driver/

%files
%doc LICENSE README.* CONTRIBUTING.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/clickhouse_driver/tests/

%files docs
%doc docs/*/man/*

%files tests
%python3_sitelibdir/clickhouse_driver/tests/


%changelog
* Wed Jun 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.20-alt1
- Initial build for Sisyphus
