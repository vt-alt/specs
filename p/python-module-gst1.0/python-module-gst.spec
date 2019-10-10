%define _name gst-python
%define ver_major 1.16
%define gst_api_ver 1.0
%define _gst_libdir %_libdir/gstreamer-%gst_api_ver

%def_with python2
%def_disable check

%ifarch %valgrind_arches
%def_enable valgrind
%endif

Name: python-module-gst%gst_api_ver
Version: %ver_major.1
Release: alt1

Summary: GStreamer overrides for PyGobject
Group: Development/Python
License: LGPL2+
Url: http://gstreamer.freedesktop.org/

Provides: %_name = %version-%release
Provides: python-module-gst = %version-%release

Source: http://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz
Patch: %name-1.5.2-python-libs.patch

BuildRequires(pre): rpm-build-gir rpm-build-python3 rpm-macros-valgrind
BuildRequires: orc liborc-test-devel  gcc-c++ gst-plugins%gst_api_ver-devel >= %version
BuildRequires: python3-devel python3-module-pygobject3-devel python3-module-pytest
%if_enabled valgrind
BuildRequires: valgrind-tool-devel
%endif
%{?_enable_check:BuildRequires: /proc gstreamer%gst_api_ver gst-plugins-base%gst_api_ver}
%if_with python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-modules-distutils python-module-pygobject3-devel
BuildRequires: python-modules-compiler python-module-pytest
%endif

%description
This package provides GStreamer overrides for PyGobject.

%package -n python3-module-gst%gst_api_ver
Summary: GStreamer overrides for PyGobject
Group: Development/Python3
Provides: python3-module-gst = %version-%release

%description -n python3-module-gst%gst_api_ver
This package provides GStreamer overrides for PyGobject.

%prep
%setup -n %_name-%version -a0
mv %_name-%version py2build
for d in . %{?_with_python2:py2build}; do
pushd $d
%patch
popd
done

%build
%autoreconf
%configure PYTHON=%__python3
%make_build

%if_with python2
pushd py2build
%autoreconf
%configure PYTHON=%__python
%make_build
popd
%endif

%install
%makeinstall_std

%if_with python2
pushd py2build
%makeinstall_std
popd
%endif

%check
%make check

%if_with python2
pushd py2build
%make check
popd
%endif

%if_with python2
%files
%python_sitelibdir/gi/overrides/*
%exclude %python_sitelibdir/gi/overrides/*.la
# gstreamer plugin
%exclude %_gst_libdir/libgstpython.*
%doc AUTHORS NEWS
%endif

%files -n python3-module-gst%gst_api_ver
%python3_sitelibdir/gi/overrides/*
%exclude %python3_sitelibdir/gi/overrides/*.la
%doc AUTHORS NEWS

%changelog
* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1
- made python2 build optional

* Tue Apr 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1.1
- mike@: introduce valgrind knob (on where present)

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Wed Mar 06 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt2
- updated buildreqs

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.13.91-alt1
- 1.13.91

* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Thu May 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Feb 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Tue Nov 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Thu Jun 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Apr 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Mar 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1.1
- NMU: Use buildreq for BR.

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Oct 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Jun 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Tue Nov 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1.1
- fixed name of python3 package

* Mon Nov 03 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

