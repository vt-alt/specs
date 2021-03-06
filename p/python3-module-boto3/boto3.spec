%define _unpackaged_files_terminate_build 1

%define oname boto3
%def_without check

Name: python3-module-%oname
Version: 1.17.96
Release: alt1

Summary: The AWS SDK for Python

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/boto3/

BuildArch: noarch

# Source-git: https://github.com/boto/boto3.git
Source: %name-%version.tar

Patch1: %oname-alt-docs.patch
Patch2: %oname-alt-unvendor.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-unittest2 python3-module-mock
BuildRequires: python3-module-botocore python3-module-html5lib python3-module-nose python3-module-pbr
BuildRequires: python3-module-sphinx
BuildRequires: python3(s3transfer)
BuildRequires: python3(six)

%description
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

WARNING: Boto 3 is in developer preview and should not be used in
production yet! Please try it out and give feedback by opening issues or
pull requests on this repository. Thanks!

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%python3_build_debug

%install
%python3_install

%check
# skip tests depending on network
rm -rf tests/integration

nosetests3

%files
%doc LICENSE
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Thu Jun 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.17.96-alt1
- new version 1.17.96 (with rpmrb script)
- disable check (due internet depends)

* Wed Jun 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.14.56-alt2
- build python3 module separately

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.56-alt1
- Updated to upstream version 1.14.56.

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.29-alt1
- Updated to upstream version 1.7.29.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.6-alt1
- Updated to upstream version 1.4.6.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150807
- New snapshot

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150723
- Version 1.1.1

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150420
- Version 0.0.16

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1.git20150316
- Version 0.0.10

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt1.git20150219
- Version 0.0.9

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1.git20150210
- Version 0.0.8

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141218
- Version 0.0.6

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20141209
- Version 0.0.5

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20141208
- Version 0.0.4

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141126
- Version 0.0.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141120
- Version 0.0.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141111
- Initial build for Sisyphus

