%define _unpackaged_files_terminate_build 1
%define oname clickhouse-driver

Name:       python3-module-%oname
Version:    0.2.0
Release:    alt1
License:    %mit
Group:      Development/Python3
Summary:    ClickHouse Python Driver with native interface support.
Url:        https://github.com/mymarilyn/clickhouse-driver
Source:     %name-%version.tar
BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

Requires: python3-module-clickhouse-cityhash

%description
ClickHouse Python Driver with native (TCP) interface support.

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

# install module for sphinx to temporary directory 
%__python3 setup.py install --skip-build --root=_build --force
export PYTHONPATH=$PWD/_build/%python3_sitelibdir
%make -C docs/ man SPHINXBUILD=sphinx-build-3

%install
%python3_install

cp -fR tests/ %buildroot%python3_sitelibdir/clickhouse_driver/
mkdir -p %buildroot/%_man1dir
install -pm0644 docs/*/man/*.1 %buildroot/%_man1dir/

%files
%doc LICENSE README.* CONTRIBUTING.rst
%python3_sitelibdir/*
%_man1dir/*.1.*
%exclude %python3_sitelibdir/clickhouse_driver/tests/

%files tests
%python3_sitelibdir/clickhouse_driver/tests/

%changelog
* Thu Feb 11 2021 Anton Farygin <rider@altlinux.org> 0.2.0-alt1
- 0.2.0

* Fri Oct 02 2020 Anton Farygin <rider@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Fri Jun 19 2020 Anton Farygin <rider@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Fri Oct 04 2019 Anton Farygin <rider@altlinux.ru> 0.1.1-alt1
- 0.1.1
- built and install man page 

* Thu Aug 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt1
- Version updated to 0.1.0

* Wed Jun 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.20-alt1
- Initial build for Sisyphus
