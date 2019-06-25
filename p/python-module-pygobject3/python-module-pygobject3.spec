%def_disable snapshot

%define _name pygobject
%define ver_major 3.32
%define api_ver 3.0
%define gtk_api_ver 3.0
%def_enable pycairo
%def_disable devel_doc
%def_enable tests
%def_disable check

Name: python-module-%{_name}3
Version: %ver_major.2
Release: alt1

Summary: Python bindings for GObject
Group: Development/Python
License: LGPL
Url: http://www.pygtk.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%setup_python_module pygobject3

%add_findprov_lib_path %python_sitelibdir/gi
%add_findprov_lib_path %python_sitelibdir/gtk-2.0

%add_findprov_lib_path %python3_sitelibdir/gi
%add_findprov_lib_path %python3_sitelibdir/gtk-2.0

Requires: typelib(GdkX11) = %gtk_api_ver
%add_typelib_req_skiplist typelib(Foo)
%filter_from_requires /Gst.*/d

%define glib_ver 2.48.0
%define gi_ver 1.46.0
%define pycairo_ver 1.11.1

BuildRequires(pre): meson rpm-build-gir rpm-build-python rpm-build-python3
BuildRequires: gnome-common gtk-doc
BuildRequires: glib2-devel >= %glib_ver libgio-devel libffi-devel
BuildRequires: python-devel python-modules-encodings python-module-pytest
%{?_enable_pycairo:BuildRequires: python-module-pycairo-devel >= %pycairo_ver libcairo-gobject-devel}
BuildRequires: gobject-introspection-devel >= %gi_ver
# python3
BuildRequires: python3-devel python3-module-pytest %{?_enable_pycairo:python3-module-pycairo-devel}
%{?_enable_check:BuildRequires: xvfb-run dbus-tools-gui libgtk+3-gir-devel glibc-i18ndata}

%description
GObject is a object system used by GTK+, GStreamer and other libraries.

PyGObject provides a convenient wrapper for use in Python programs when
accessing GObject libraries.

PyGObject now dynamically accesses any GObject libraries that uses
GObject Introspection. It replaces the need for separate modules such as
PyGTK, GIO and python-gnome to build a full GNOME 3.0 application. Once
new functionality is added to gobject library it is instantly available
as a Python API without the need for intermediate Python glue.

%package pygtkcompat
Summary: PyGTK compatibility layer for PyGObject
Group: Development/Python
Requires: %name = %version-%release

%description pygtkcompat
PyGTK compatibility layer.
It is recommended to not depend on this layer, but only use it as an
intermediate step when porting your application to PyGI. Compatibility
might never be 100%%, but the aim is to make it possible to run a well
behaved PyGTK application mostly unmodified on top of PyGI.

%package common-devel
Summary: Common development files for %_name
Group: Development/Python

%description common-devel
Common development files for %_name used for both python2 and python3.

%package devel
Summary: Development files for %name
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release
Requires: %name-common-devel = %version-%release

%description devel
Development files for %name.

%package -n python3-module-%{_name}3
Summary: Python3 bindings for GObject
Group: Development/Python3
Requires: typelib(GdkX11) = %gtk_api_ver

%description -n python3-module-%{_name}3
GObject is a object system used by GTK+, GStreamer and other libraries.

PyGObject provides a convenient wrapper for use in Python3 programs when
accessing GObject libraries.

PyGObject now dynamically accesses any GObject libraries that uses
GObject Introspection. It replaces the need for separate modules such as
PyGTK, GIO and python-gnome to build a full GNOME 3.0 application. Once
new functionality is added to gobject library it is instantly available
as a Python API without the need for intermediate Python glue.

%package -n python3-module-%{_name}3-pygtkcompat
Summary: PyGTK compatibility layer for PyGObject
Group: Development/Python3
Requires: python3-module-%{_name}3 = %version-%release

%description -n python3-module-%{_name}3-pygtkcompat
PyGTK compatibility layer.
It is recommended to not depend on this layer, but only use it as an
intermediate step when porting your application to PyGI. Compatibility
might never be 100%%, but the aim is to make it possible to run a well
behaved PyGTK application mostly unmodified on top of PyGI.

%package -n python3-module-%{_name}3-devel
Summary: Development files for python3-module-%{_name}3
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%{_name}3 = %version-%release
Requires: %name-common-devel = %version-%release

%description -n python3-module-%{_name}3-devel
Development files for python3-module-%{_name}3.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-common-devel < %version-%release

%description devel-doc
Development documentation for %_name.

%prep
%setup -n %_name-%version
%setup -D -c -n %_name-%version
mv %_name-%version py3build

%build
%define opts %{?_disable_pycairo:-Dpycairo=false} %{?_disable_tests:-Dtests=false}
%meson %opts -Dpython=python
%meson_build

pushd py3build
export PYTHON=python3
%meson %opts
%meson_build
popd

%install
%meson_install

pushd py3build
%meson_install
popd

%check
xvfb-run %meson_test

pushd py3build
xvfb-run %meson_test
popd

%files
%python_sitelibdir/gi/
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/gi/pygtkcompat.py*

%files pygtkcompat
%python_sitelibdir/pygtkcompat/
%python_sitelibdir/gi/pygtkcompat.py*

%files common-devel
%_includedir/%_name-%api_ver/
%_pkgconfigdir/%_name-%api_ver.pc
%doc README* NEWS examples

%files devel

%files -n python3-module-%{_name}3
%python3_sitelibdir/gi/
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/gi/pygtkcompat.py*

%files -n python3-module-%{_name}3-pygtkcompat
%python3_sitelibdir/pygtkcompat/
%python3_sitelibdir/gi/pygtkcompat.py*

%files -n python3-module-%{_name}3-devel

%if_enabled devel_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%changelog
* Sun Jun 23 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Sat Apr 20 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Sun Mar 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sat Dec 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.4-alt1
- 3.30.4

* Tue Nov 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Thu Nov 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt2
- rebuilt with pycairo-1.17.1

* Wed Sep 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1.1
- packaged *egg-info

* Fri Sep 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Thu May 31 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Thu Mar 29 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.28.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Mar 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Sat Mar 17 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Mar 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt2
- rebuilt with pycairo-1.16.3

* Fri Oct 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt2
- rebuilt for ALT #33541

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Wed Mar 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt2
- removed dependencies on old GStreamer (ALT #33183)

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Apr 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Fri Apr 01 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.20.0-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 3.20.0-alt2
- NMU LD_PRELOAD changes for Python 3.5

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sat Oct 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sun Jun 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Jul 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Thu Apr 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- moved pygtkcompat to separate subpackages (ALT #28787)

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Mar 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt0.3
- rebuilt with python-3.3

* Mon Dec 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt0.2
- built python3 module too (new python3-module-, -common-devel subpackages)

* Sat Dec 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt0.1
- 3.4.3 snapshot (c36e1236)
- enabled %%check again using xvfb-run

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1.1-alt1
- 3.4.1.1

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Fri Apr 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0
- no more libpython dependencies

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.1.93-alt1
- 3.1.93

* Mon Dec 12 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt1.1
- Rebuild with Python-2.7

* Sat Oct 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sat Oct 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sun Aug 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.90.2-alt1
- first build for Sisyphus

