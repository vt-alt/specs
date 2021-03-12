%define oname sip
%define pkg_version %(echo %version | sed 's/\\./,/g')

%def_with python3
%def_with pyqt5

Name: python-module-%oname
Version: 4.19.19
Release: alt4

Summary: Python bindings generator for C++ class libraries

License: PSF
Group: Development/Python
URL: http://www.riverbankcomputing.com/software/sip/

%setup_python_module sip

# hg clone http://www.riverbankcomputing.com/hg/sip
#Source-url: https://pypi.io/packages/source/s/%oname/%oname-%version.tar.gz
#Source-url: https://prdownloads.sourceforge.net/pyqt/sip/sip-%version/sip-%version.tar.gz
# Source-url: https://www.riverbankcomputing.com/static/Downloads/sip/%version/sip-%version.tar.gz
Source: %name-%version.tar

Provides: %modulename = %version-%release
Obsoletes: %modulename <= 4.1-alt2.1

# for docs build
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif
BuildRequires(pre): rpm-build-python
BuildRequires: flex gcc-c++ python2-base python-devel


%description
Generates Python bindings for C++ class libraries from a set of class
specification files.  Also includes a Python extension module needed by all
generated bindings.

%package -n python-module-PyQt4-%oname
Summary: Python bindings generator for C++ class libraries for PyQt4
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-PyQt4-%oname
Python bindings generator for C++ class libraries for PyQt4

%package -n python-module-PyQt5-%oname
Summary: Python bindings generator for C++ class libraries for PyQt5
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-PyQt5-%oname
Python bindings generator for C++ class libraries for PyQt5

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 bindings generator for C++ class libraries
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Generates Python bindings for C++ class libraries from a set of class
specification files.  Also includes a Python extension module needed by all
generated bindings.

%package -n python3-module-PyQt4-%oname
Summary: Python 3 bindings generator for C++ class libraries for PyQt4
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-PyQt4-%oname
Python 3 bindings generator for C++ class libraries for PyQt4

%package -n python3-module-PyQt5-%oname
Summary: Python 3 bindings generator for C++ class libraries for PyQt5
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-PyQt5-%oname
Python 3 bindings generator for C++ class libraries for PyQt5

%package -n python3-module-%oname-devel
Requires: python3-module-%oname = %version-%release
Summary: Header files for sip (Python 3)
Group: Development/Python3
Requires: python3-devel

%description -n python3-module-%oname-devel
Header files for sip
%endif

%package devel
Requires: %name = %version-%release
Summary: Header files for sip
Group: Development/Python
Provides: %modulename-devel = %version-%release
%py_package_provides %modulename-devel = %version-%release
Obsoletes: %modulename-devel
Requires: python-devel

%description devel
Header files for sip

%prep
%setup

#rm -f siplib/libsip.a

# fix versions sets
#subst 's/version = (0, 1, 0)/version = (%pkg_version)/' build.py
#python build.py prepare

%build
mkdir python
pushd python
python2 ../configure.py --debug -d %python_sitelibdir

sed -i 's|^\(CPPFLAGS.*\)|\1 -g -I%python_includedir|' */Makefile
%make_build
popd

mkdir python-PyQt4
pushd python-PyQt4
python2 ../configure.py --debug -d %python_sitelibdir \
	--sip-module=PyQt4.sip
%make_build
popd

%if_with pyqt5
mkdir python-PyQt5
pushd python-PyQt5
python2 ../configure.py --debug -d %python_sitelibdir \
	--sip-module=PyQt5.sip
%make_build
popd
%endif

# docs build
#python build.py doc

%if_with python3
mkdir python3
pushd python3
python3 ../configure.py --debug -d %python3_sitelibdir
sed -i \
	's|^\(CPPFLAGS.*\)|\1 -g -I%__python3_includedir|' \
	*/Makefile
sed -i \
	's|lpython%__python3_version|l:%(basename %__libpython3)|' \
	siplib/Makefile
%make_build
popd

mkdir python3-PyQt4
pushd python3-PyQt4
python3 ../configure.py --debug -d %python3_sitelibdir \
	--sip-module=PyQt4.sip
%make_build
popd

mkdir python3-PyQt5
pushd python3-PyQt5
python3 ../configure.py --debug -d %python3_sitelibdir \
	--sip-module=PyQt5.sip
%make_build
popd
%endif

%install
%if_with python3
%makeinstall_std -C python3
%makeinstall_std -C python3-PyQt4
%makeinstall_std -C python3-PyQt5

mv %buildroot%_bindir/sip %buildroot%_bindir/sip3
sed -i 's|%_datadir/sip|%_datadir/sip3|' \
	%buildroot%python3_sitelibdir/sipconfig.py
sed -i 's|%_bindir/sip|%_bindir/sip3|' \
	%buildroot%python3_sitelibdir/sipconfig.py
%endif
%makeinstall_std -C python
%makeinstall_std -C python-PyQt4
%if_with pyqt5
%makeinstall_std -C python-PyQt5
%endif

%files
%_bindir/sip
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pyi
%exclude %python_sitelibdir/sipconfig.*
%exclude %python_sitelibdir/sipdistutils.*
%exclude %python_sitelibdir/PyQt4*
%if_with pyqt5
%exclude %python_sitelibdir/PyQt5*
%endif
%doc README NEWS LICENSE*

%files -n python-module-PyQt4-%oname
%python_sitelibdir/PyQt4*

%if_with pyqt5
%files -n python-module-PyQt5-%oname
%python_sitelibdir/PyQt5*
%endif

%files devel
%python_includedir/*
%python_sitelibdir/*.pyi
%python_sitelibdir/sipconfig.*
%python_sitelibdir/sipdistutils.*
#doc doc/*

%if_with python3
%files -n python3-module-%oname
%doc README NEWS LICENSE*
%_bindir/sip3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pyi
%exclude %python3_sitelibdir/sipconfig.*
%exclude %python3_sitelibdir/sipdistutils.*
%exclude %python3_sitelibdir/PyQt4*
%exclude %python3_sitelibdir/PyQt5*

%files -n python3-module-PyQt4-%oname
%python3_sitelibdir/PyQt4*

%files -n python3-module-PyQt5-%oname
%python3_sitelibdir/PyQt5*

%files -n python3-module-%oname-devel
# Here, we just use the same path as in the build system:
%__python3_includedir/*
%python3_sitelibdir/*.pyi
%python3_sitelibdir/sipconfig.*
%python3_sitelibdir/sipdistutils.*
#doc doc/*
%endif

%changelog
* Sun Sep 06 2020 Vitaly Lipatov <lav@altlinux.ru> 4.19.19-alt4
- add pyqt5 disable possibility

* Sat Feb 08 2020 Anton Midyukov <antohami@altlinux.org> 4.19.19-alt3
- fix PATH to sip3 (it was broken in 4.19.13-alt1)

* Thu Feb 06 2020 Vitaly Lipatov <lav@altlinux.ru> 4.19.19-alt2
- fix build: add python2-base buildreq

* Mon Oct 07 2019 Vitaly Lipatov <lav@altlinux.ru> 4.19.19-alt1
- new version 4.19.19 (with rpmrb script)

* Sun Feb 03 2019 Anton Midyukov <antohami@altlinux.org> 4.19.13-alt1
- new version (4.19.13) with rpmgs script
- build PyQt4 and PyQt5-sip modules

* Wed Aug 22 2018 Sergey V Turchin <zerg@altlinux.org> 4.19.7-alt1.3
- move sipconfig and sipdistutils to devel subpackage

* Wed Aug 22 2018 Sergey V Turchin <zerg@altlinux.org> 4.19.7-alt1.2
- move .pyi to devel subpackage

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.19.7-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Feb 14 2018 Vitaly Lipatov <lav@altlinux.ru> 4.19.7-alt1
- new version 4.19.7 (with rpmrb script)

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 4.19.3-alt1
- new version (4.19.3) with rpmgs script

* Sat Apr 02 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.16.9-alt2
- (.spec) use updated correct %%__python3_includedir and %%__libpython3.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.16.9-alt1.1
- NMU: Use buildreq for BR.

* Mon Jul 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.9-alt1
- Version 4.16.9

* Mon Jun 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.8-alt1
- Version 4.16.8

* Thu Mar 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.7-alt1
- Version 4.16.7

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.6-alt1
- Version 4.16.6

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.5-alt1
- Version 4.16.5

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.4-alt1
- Version 4.16.4

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.2-alt1
- Version 4.16.2

* Fri Jun 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16.1-alt1
- Version 4.16.1

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.16-alt1
- Version 4.16

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.15.5-alt1
- Version 4.15.5

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.15.3-alt1
- Version 4.15.3

* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.15.0-alt1
- Version 4.15.0 (ALT #29568)

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 4.14.3-alt2.1
- Simplify module version set up

* Fri Apr 05 2013 Aleksey Avdeev <solo@altlinux.ru> 4.14.3-alt2
- Fix versions sets in sipconfig.py

* Fri Mar 01 2013 Aleksey Avdeev <solo@altlinux.ru> 4.14.3-alt1
- Version 4.14.3

* Thu Dec 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.14.2-alt2
- Release up

* Thu Dec 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.14.2-alt1
- Version 4.14.2

* Mon Sep 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.3-alt1
- Version 4.13.3

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt3
- Fixed config for python3-module-sip

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.13.2-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.2-alt1
- Version 4.13.2

* Tue Jan 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.13.1-alt1
- Version 4.13.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.12.3-alt1.1
- Rebuild with Python-2.7

* Sun Jul 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.3-alt1
- Version 4.12.3

* Sun Mar 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.1-alt2
- Rebuilt for debuginfo

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.12.1-alt1
- Version 4.12.1 (ALT #24999)

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.11.2-alt1
- Version 4.11.2

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.5-alt2
- Set devel package as noarch

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.5-alt1
- Version 4.10.5

* Tue Jan 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10-alt1
- Version 4.10

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.2-alt1.1
- Rebuilt with python 2.6

* Wed Aug 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.8.2-alt1
- Update to new release

* Mon Jul 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.8.1-alt1
- Update to new release

* Tue Nov 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.9-alt1
- New version

* Sun Aug 17 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.6-alt3
- Fixed rpath problem and libpython linking (#14655)

* Tue Aug 05 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.7.6-alt2
- Push rlz@ build to Sisyphus

* Sat Jun 07 2008 Dmitry M. Maslennikov <rlz at altlinux.org> 4.7.6-alt1
- New version

* Tue Jan 01 2008 Ivan Fedorov <ns@altlinux.org> 4.7.3-alt1
- 4.7.3

* Mon Aug 20 2007 Ivan Fedorov <ns@altlinux.org> 4.7-alt1
- 4.7

* Fri Jul 13 2007 Ivan Fedorov <ns@altlinux.org> 4.6-alt1
- 4.6
- Added support for wchar_t.
- The -g command line option releases the GIL whenever a call is made to
  the wrapped library.
- Added the /HoldGIL/ annotation to explicitly retain the GIL when
  calling a particular function in the wrapped library.
- Added sipFindClass() and sipFindNamedEnum() to the public API.
- /TransferThis/ may be specified more than once.
- Added support for __truediv__ and __itruediv__.
- The SIP code generator and module may be built as universal binaries
  under MacOS/X using the -n command line option to configure.py.

* Thu Dec 28 2006 Ivan Fedorov <ns@altlinux.ru> 4.5.2-alt1
- 4.5.2
- spec clean up (rewrite buildreqs)

* Thu Nov 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.5-alt1
- 4.5

* Mon Jun 12 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.5-alt1
- 4.4.5

* Sun May 28 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.3-alt1
- 4.4.3
- fix #9616

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Sun Apr 09 2006 Ivan Fedorov <ns@altlinux.ru> 4.4-alt1
- 4.4

* Mon Mar 06 2006 Alexey Morozov <almorozov@altlinux.org> 4.3.2-alt1.0.1
- NMU: fixed provides list for -devel subpackage
- changed XFree86-devel to xorg-x11-devel

* Wed Dec 07 2005 Ivan Fedorov <ns@altlinux.ru> 4.3.2-alt1
- 4.3.2

* Sat Nov 05 2005 Ivan Fedorov <ns@altlinux.ru> 4.3.1-alt1
- 4.3.1

* Sat Mar 12 2005 Ivan Fedorov <ns@altlinux.ru> 4.2.1-alt1
- 4.2.1
- rebuild with python 2.4

* Mon Feb 21 2005 Ivan Fedorov <ns@altlinux.ru> 4.2-alt1
- 4.2

* Thu Jan 27 2005 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt2
- updating obsoleting of sip

* Tue Jan 04 2005 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt0.M24.1
- Backport to Master 2.4

* Wed Dec 22 2004 Ivan Fedorov <ns@altlinux.ru> 4.1.1-alt1
- 4.1.1

* Sun Dec 12 2004 Ivan Fedorov <ns@altlinux.ru> 4.1-alt3
- fix spec to be compatible with python policy

* Tue Sep 28 2004 Eugene V. Horohorin <genix@altlinux.ru> 4.1-alt2
- license mistake fix
- spec clean up (using %%python_site_packages_dir instead of old method of %%python_site)

* Tue Sep 21 2004 Eugene V. Horohorin <genix@altlinux.org> 4.1-alt1
- new release

* Thu Sep 02 2004 Eugene V. Horohorin <genix@altlinux.ru> 4.0.1-alt1
- new release

* Wed May 19 2004 Serge V. Sergeev <ssv@altlinux.ru> 4.0-alt0.3
- new release

* Mon Feb 16 2004 Serge V. Sergeev <ssv@altlinux.ru> 3.10-alt1
- new release

* Wed Dec 24 2003 Serge V. Sergeev <ssv@altlinux.ru> 3.9-alt2
- add definitionn of QTDIR variable ( need for new build system )

* Thu Dec 11 2003 Serge V. Sergeev <ssv@altlinux.ru> 3.9-alt1
- new release

* Fri Aug 01 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt2
- added _findprov_lib_path macro to temporary solve problem with dependencies

* Tue Jul 08 2003 Serge Sergeev <ssv@altlinux.ru> 3.7-alt1
- new release

* Mon Apr 28 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt1
- new release

* Thu Apr 10 2003 Serge Sergeev <ssv@altlinux.ru> 3.6-alt0.1
- New build from snapshot

* Fri Dec 20 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt2
- Increase release for upgrade

* Mon Dec 16 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt1
- new release

* Mon Dec 16 2002 Serge Sergeev <ssv@altlinux.ru> 3.5-alt0.1.20021205
- new release
- correct version

* Fri Dec 06 2002 Serge Sergeev <ssv@altlinux.ru> 20021205-alt1
- build from snapshot
- some documentation added in separate package

* Tue Nov 05 2002 Serge Sergeev <ssv@altlinux.ru> 3.4-alt1
- new release

* Wed Sep 04 2002 Serge Sergeev <ssv@altlinux.ru> 3.3.2-alt1
- new release

* Fri Aug 02 2002 Serge Sergeev <sergeyssv@mail.ru> 3.3-alt1
- Clean up spec file

* Thu Jul 25  2002 <sergeyssv@mail.ru>
- some fixes

* Thu Jun 06  2002 <sergeyssv@mail.ru>
- Initial release
