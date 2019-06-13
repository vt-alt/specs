%define oname llfuse

Name: python3-module-llfuse
Version: 1.3.6
Release: alt1

Summary: Python Bindings for the low-level FUSE API

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: https://github.com/python-llfuse/python-llfuse
Group: Development/Python3
License: LGPLv2+

# Source-url: https://pypi.io/packages/source/l/%oname/%oname-%version.tar.bz2
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: libattr-devel libfuse-devel python3-devel python3-module-setuptools

Source44: import.info
%add_findprov_skiplist %python3_sitelibdir/.*\.so$

%description
LLFUSE is a set of Python bindings for the low level FUSE API. It requires at
least FUSE 2.8.0.

LLFUSE was originally part of S3QL, but has been factored out so that it can be
used by other projects as well.

NOTE: It is legacy module, do not use it in a real projects. See pyfuse3 instead.

%prep
%setup
rm doc/html/.buildinfo
rm -rf src/llfuse.egg-info
find -name '*.py' | xargs sed -i '1s|^#!python|#!%__python3|'

%build
%python3_build_debug

%install
%python3_install

%files
%doc Changes.rst doc/html LICENSE
%python3_sitelibdir/*

%changelog
* Wed Jun 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt1
- new version (1.3.6) with rpmgs script
- python3 module only

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.40-alt1_4.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.40-alt1_4.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.40-alt1_4.1
- NMU: Use buildreq for BR.

* Fri Aug 14 2015 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt1_4
- human build for ALT Linux Sisyphus

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_3
- update to new release by fcimport

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_1
- update to new release by fcimport

* Mon Feb 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_1
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.37.1-alt1_11
- initial fc import

