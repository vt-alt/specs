%define oname pivy
Name: python-module-%oname
Version: 0.5.0
Release: alt2.hg20100619.3.3
Serial: 2
Summary: Pivy is a Coin binding for Python
License: BSD
Group: Development/Python
Url: http://pivy.coin3d.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
#BuildArch: noarch

# hg clone http://hg.sim.no/Pivy/default
Source: %name-%version.tar.gz

%setup_python_module %oname
BuildPreReq: libcoin3d-devel swig libSoQt-devel
BuildPreReq: gcc-c++ libqt4-devel

%description
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics
library with a C++ Application Programming Interface. Coin uses
scene-graph data structures to render real-time graphics suitable for
mostly all kinds of scientific and engineering visualization
applications.

%prep
%setup
ln -s %_includedir/Inventor/SoDB.h fake_headers/Inventor/

%build
%add_optflags -I%_includedir/qt4/Qt -fno-strict-aliasing
%python_build_debug

%install
%python_install

%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/%oname \
	%buildroot%python_sitelibdir_noarch/*.egg-info \
	%buildroot%python_sitelibdir/
%endif

%files
%doc AUTHORS HACKING LICENSE NEWS THANKS docs/*
%python_sitelibdir/*

%changelog
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

