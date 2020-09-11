%define oname cyrand

Name: python3-module-%oname
Version: 0.3
Release: alt2

Summary: Wrapper to Boost random numbers
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/cyrand/

# https://github.com/andrewcron/cyrand.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: boost-devel-headers boost-python3-devel
BuildRequires: gcc-c++ libnumpy-py3-devel
BuildRequires: python3-module-Cython python3-module-numpy-testing

%py3_provides %oname
%py3_requires numpy scipy matplotlib

%description
This is simply a set of cython definitions for the Boost TR1 Random
sampling library.

%prep
%setup

sed -i 's|@IS3@|3|' setup.py

ln -s $(%__python3 -c 'import numpy; \
        print(numpy.get_include() + "/numpy-py3")') numpy

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst example
%python3_sitelibdir/*


%changelog
* Tue Mar 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3-alt1.git20150228.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.git20150228.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.git20150228.1
- NMU: Use buildreq for BR.

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150228
- Initial build for Sisyphus

