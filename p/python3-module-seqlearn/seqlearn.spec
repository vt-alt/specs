%define _unpackaged_files_terminate_build 1

%define oname seqlearn

Name: python3-module-%oname
Version: 0.2
Release: alt4

Summary: Sequence learning toolkit for Python
License: MIT
Group: Development/Python3
Url: http://larsmans.github.io/seqlearn/

# https://github.com/larsmans/seqlearn.git
Source0: https://pypi.python.org/packages/25/2c/95da36839f647a6b15da1fd10f68d755c7fca549c92aabb3ff734f5c682c/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-numpydoc

%py3_provides %oname


%description
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

# Don't depend on sklearn.externals.six, depend on six instead
find . -name '*.py' -type f -print0 | xargs -0 sed -i \
	-e 's:from sklearn\.externals ::g'

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir

mv %oname %oname.bak
%make -C doc pickle
%make -C doc html
mv %oname.bak %oname

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%if 0
rm -fR build
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
%endif

%files
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*


%changelog
* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2-alt4
- Fixed build with numpy.

* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt3
- build for python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2-alt2
- Updated dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- automated PyPI update

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20150324.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Mar 26 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt1.git20150324.2
- NMU: Fixed BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20150324.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150324
- New snapshot

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140922
- Initial build for Sisyphus

