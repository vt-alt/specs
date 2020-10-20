%define oname pivy
Name: python-module-%oname
Version: 0.6.5
Release: alt0.1.p9
Epoch: 2
Summary: Pivy is a Coin binding for Python
License: ISC
Group: Development/Python
Url: https://github.com/coin3d/pivy
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: pivy-cmake.patch

ExcludeArch: armh

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: libcoin3d-devel
BuildRequires: swig
BuildRequires: libsoqt-devel
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel

%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.

%package -n python3-module-%oname
Summary: Pivy is a Coin binding for Python3
Group: Development/Python3

%description -n python3-module-%oname
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.

%prep
%setup
%patch1 -p1
rm -rf ../python3
cp -a . ../python3

%build
#add_optflags -I%_includedir/qt4/Qt -fno-strict-aliasing
%python_build_debug
pushd ../python3
%python3_build_debug
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/%oname \
	%buildroot%python_sitelibdir_noarch/*.egg-info \
	%buildroot%python_sitelibdir/
%endif

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/%oname \
	%buildroot%python3_sitelibdir_noarch/*.egg-info \
	%buildroot%python3_sitelibdir/
%endif

%files
%doc AUTHORS HACKING NEWS THANKS docs/*
%python_sitelibdir/*

%files -n python3-module-%oname
%doc AUTHORS HACKING NEWS THANKS docs/*
%python3_sitelibdir/*

%changelog
* Tue Oct 06 2020 Andrey Cherepanov <cas@altlinux.org> 2:0.6.5-alt0.1.p9
- Backport to p9 branch.
- Exclude armh from build architectures.

* Fri Sep 18 2020 Andrey Cherepanov <cas@altlinux.org> 2:0.6.5-alt1
- New version.
- Fix License tag, project URL and maintainer.
- Build from upstream tag.

* Thu Jun 06 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2:0.5.0-alt2.hg20100619.3.3
- Fixed build on architectures with "%_lib" != lib.

* Mon Jun 11 2018 Anton Midyukov <antohami@altlinux.org> 2:0.5.0-alt2.hg20100619.3.2
- Rebuilt for aarch64

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2:0.5.0-alt2.hg20100619.3.1
- Rebuild with Python-2.7

* Sun May 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt2.hg20100619.3
- Fixed build

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt2.hg20100619.2
- Rebuilt for debuginfo

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt2.hg20100619.1
- Fixed build

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt2.hg20100619
- New snapshot

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2:0.5.0-alt1.svn20091216
- Rebuilt with new SoQt

* Fri Jan 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.svn20091716
- Initial build for Sisyphus

