%def_enable snapshot
%def_enable numpy
%def_disable docs

%define major 2.24
Name: python-module-pygtk
Version: %major.0
Release: alt7

Summary: Python bindings for the GTK+ widget set

Group: Development/Python
License: LGPL
Url: http://www.pygtk.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

%if_enabled snapshot
Source: pygtk-%version.tar
%else
Source: http://ftp.gnome.org/pub/GNOME/sources/pygtk/%major/pygtk-%version.tar.bz2
%endif
Patch: pygtk-2.14.0-alt-configure.patch
Patch1: pygtk-2.24.0-alt-pango-1.44.patch

%setup_python_module pygtk
%add_python_req_skip gdk

Provides: pygtk2 = %version-%release
Obsoletes: pygtk2

%py_provides argtypes

%define pygobject_ver 2.26.0
%define pycairo_ver 1.4.12
%define gtk_ver 2.22.0
%define glade_ver 2.5.1

# don't reqs automatically
Requires: python-module-pycairo >= %pycairo_ver
%{?_enable_numpy:Requires:python-module-numpy python-module-numpy-addons}

BuildRequires: rpm-build-compat gtk-doc rpm-build-python python-devel gnome-common
BuildRequires: python-module-pygobject-devel >= %pygobject_ver
BuildRequires: python-module-pycairo-devel >= %pycairo_ver
BuildRequires: libgtk+2-devel >= %gtk_ver
BuildRequires: libglade-devel >= %glade_ver
%{?_enable_numpy:BuildRequires: libnumpy-devel}
# style.css from this package required to build documentation
BuildRequires: python-module-pygobject-devel-doc

%description
PyGTK is an extension module for python that gives you access to the GTK+
widget set.  Just about anything you can write in C with GTK+ you can write
in python with PyGTK (within reason), but with all the benefits of python.


%package libglade
Summary: A wrapper for the libglade library for use with PyGTK
Group: Development/Python
Requires: %name = %version-%release
%py_provides libglade

%description libglade
This module contains a wrapper for the libglade library. Libglade allows
a program to construct its user interface from an XML description, which
allows the programmer to keep the UI and program logic separate.

%package devel
Summary: files needed to build wrappers for GTK+ addon libraries
Group: Development/Python
Requires: %name = %version-%release
Requires: python-module-pygobject-devel

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with pygtk.

%package examples
Summary: PyGTK examples
Group: Development/Python
BuildArch: noarch
Requires: %name-libglade = %version-%release

%description examples
This package contains PyGTK examples

%package demo
Summary: PyGTK demo
Group: Development/Python
Requires: %name = %version-%release

%description demo
This package contains PyGTK demo

%package doc
Summary: PyGTK doc
Group: Development/Python
BuildArch: noarch

%description doc
This package contains PyGTK doc

%prep
%setup -q -n %modulename-%version
%patch
%patch1

%__subst "s|@PYTHON@|%_bindir/env python|g" pygtk-codegen-2.0.in examples/pygtk-demo/pygtk-demo.in

%build
#NOCONFIGURE=1 gnome-autogen.sh
%autoreconf -I m4
%configure --disable-static \
	%{subst_enable numpy} \
	%{subst_enable docs} \
	%{?_enable_snapshot:--enable-docs}
%nil
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_includedir/python%__python_version
mv %buildroot%_includedir/pygtk-2.0 %buildroot%_includedir/python%__python_version/pygtk
subst "s|\${includedir}/pygtk-2.0|\${includedir}/python%__python_version/pygtk|g" %buildroot/%_pkgconfigdir/*.pc

# something broken if gobject still here
test -f %buildroot%python_sitelibdir/gtk-2.0/gobject.so && exit 1

%files
%python_sitelibdir/gtk-2.0/*
%exclude %python_sitelibdir/gtk-2.0/gtk/glade.so
%doc AUTHORS NEWS README MAPPING THREADS TODO

%files examples
%doc examples/*

%files demo
%_bindir/pygtk-demo
%_libdir/%modulename/

%files libglade
%python_sitelibdir/gtk-2.0/gtk/glade.so

%files devel
%_bindir/pygtk-codegen-2.0
%python_includedir/pygtk/pygtk/
%_pkgconfigdir/pygtk*.pc
%_datadir/%modulename/

%files doc
%_datadir/gtk-doc/html/pygtk/

%changelog
* Sun Sep 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt7
- rebuilt with pango-1.44.6

* Mon Sep 30 2013 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt6
- update to c524124 (fixed BGO #660216)
- fixed build

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt5
- fixed %%install

* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt4
- -devel subpackage requires python-module-pygobject-devel

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.24.0-alt3.1
- Rebuild with Python-2.7

* Thu Apr 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt3
- numpy support turned back, some apps require it

* Thu Apr 07 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt2
- numpy support disabled

* Fri Apr 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Fri Mar 25 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.2-alt1
- 2.23.2

* Sat Mar 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt1
- 2.23.1

* Thu Mar 10 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.0-alt2
- rebuild against current numpy (2.0.0-alt1.svn20100607.6)
- added explicit dependency on python-module-numpy-addons

* Tue Feb 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.23.0-alt1
- 2.23.0

* Mon Oct 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt2
- reqs python-module-pycairo (closes #24354)

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt1
- 2.22.0

* Mon Jun 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.17.0-alt4
- rebuild against current numpy (2.0.0-alt1.svn20100607)

* Tue Feb 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.17.0-alt3
- rejected all destructive changes from previous release (closes #22872)

* Mon Jan 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.17.0-alt2.1
- Fixed for autoconf 2.6
- Added documentation

* Sun Jan 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.17.0-alt2
- updated buildreqs
- don't rebuild documentation

* Sun Dec 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.17.0-alt1
- 2.17.0

* Tue Nov 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt4
- updated buildreqs

* Mon Oct 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt3
- removed obsolete buildreq on python-module-Numeric (closes #21915)

* Mon Aug 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0
- NumPy support enabled

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.14.1-alt1
- 2.14.1

* Mon Feb 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.14.0-alt1
- 2.14.0

* Mon Dec 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.13.0-alt3
- requires latest python-module-pygobject, python-module-pycairo to
  avoid #18279 and similar bugs

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 2.13.0-alt2
- enabled x11 support (fix altbug #18115)
- built -doc and -examples subpackages as noarch

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.13.0-alt1
- 2.13.0

* Fri Mar 21 2008 Vitaly Lipatov <lav@altlinux.ru> 2.12.1-alt1
- new version 2.12.1 (with rpmrb script)

* Thu Nov 01 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt2
- build without X11 binding, add test for it

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt1
- new version 2.12.0 (with rpmrb script)

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.6-alt1
- new version 2.10.6 (with rpmrb script)

* Wed Feb 21 2007 Vitaly Lipatov <lav@altlinux.ru> 2.10.4-alt0.1
- new version, enable doc build, update buildreq
- disable GDK_TARGET_X11 (x11 specific functions)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.10.3-alt0.1
- new version 2.10.3 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.6-alt0.1
- add require pyobject version
- new version 2.9.6 (with rpmrb script)

* Mon Jul 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt0.1
- new version 2.9.0 (with rpmrb script)

* Sat Mar 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.4-alt2
- fixes for python-strict in requires (bug #4568 again)

* Thu Mar 09 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.4-alt1
- rebuild without gobject
- add test against gobject inside

* Sat Mar 04 2006 Vitaly Lipatov <lav@altlinux.ru> 2.8.4-alt0.1
- new version
- move gobject binding to standalone package
- remove COPYING link from doc
- remove gobject from this package (add buildreq to it)
- update buildrequires

* Thu Dec 08 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.2-alt2
- add require for python-module-pycairo (bug #8608)

* Tue Nov 22 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.2-alt1
- enable build cairo.gtk (#8011)

* Fri Oct 14 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.2-alt0.1
- new version

* Fri Oct 07 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt0.1
- new version

* Sun Sep 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt0.1
- new version
- move includes to python%__python_version/pygtk

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version
- build with python 2.4

* Mon Jan 24 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.3-alt1
- new version

* Sat Dec 18 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt3
- remove gtk_cell_view_set_value (due GTK API changes in 2.6.0)

* Thu Dec 16 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt2
- add fix GTK API change (fix problem marked in bug #5678)

* Sat Dec 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1.1
- rebuild

* Sat Nov 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt1
- Added module directories to %%_findprov_lib_path

* Fri Nov 05 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.4.1-alt0.1
- Updated to 2.4.1
- Versioned dependencies as required by configure
- Buildreq
- Spec cleanup

* Fri Jul 23 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3.94-alt1
- new version

* Fri Jul 23 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3.93-alt2
- backport libglade from 2.3.92 (broken XML)

* Tue Jul 20 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3.93-alt1
- new version

* Thu Jul 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3.92-alt1
- new version (from unstable 2.4)

* Tue Jul 13 2004 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- renamed
- spec cleanup (according to python policy)
- remove COPYING
- new version

* Mon Feb 09 2004 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt5
- python23 build
- separate package for examples
- changed group to Development/Python
- added gl.so

Packager: Egor S. Orlov
* Wed Oct 29 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt4
- Added python22 requires
- Aded _gtk.so to the package

* Thu Oct 23 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt3
- Added URL

* Thu Oct 23 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt2
- hasher build
- added gtkglarea2(-devel) dependency

* Mon Sep 29 2003 Egor S. Orlov <oes@altlinux.ru> 2.0.0-alt1
- New version

* Tue Nov 12 2002 AEN <aen@altlinux.ru> 1.99.12-alt1
- first build for Sisyphus

* Thu Oct 31 2002 Matt Wilson <msw@redhat.com>
- rebuild for multilib
- use %%configure

* Fri Aug 30 2002 Matt Wilson <msw@redhat.com>
- fix pixbuf leaks (#72137)
- five more pixbuf leaks plugged

* Wed Aug 28 2002 Jonathan Blandford <jrb@redhat.com>
- remover Packager tag

* Tue Aug 27 2002 Jonathan Blandford <jrb@redhat.com>
- add binding for gdk_atom_intern

* Mon Jul 29 2002 Matt Wilson <msw@redhat.com>
- 0.99.12

* Wed Jul 17 2002 Matt Wilson <msw@redhat.com>
- new version from CVS

* Thu Jun 27 2002 Tim Waugh <twaugh@redhat.com>
- Fix bug #65770.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 17 2002 Matt Wilson <msw@redhat.com>
- new version from CVS

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Jeremy Katz <katzj@redhat.com>
- 1.99.10

* Wed Feb 27 2002 Matt Wilson <msw@redhat.com>
- 1.99.8

* Mon Jan 28 2002 Matt Wilson <msw@redhat.com>
- added atkmodule.so to file list

* Thu Oct 18 2001 Matt Wilson <msw@redhat.com>
- fix devel filelist to match new header location

* Mon Oct 15 2001 Matt Wilson <msw@redhat.com>
- get the headers from their new version-specific location

* Thu Oct 11 2001 Matt Wilson <msw@redhat.com>
- fixed typo in devel filelist
- added macro that tests to see if we have libglade2, make the
  filelist a condition of that
- changed name to 'pygtk2' to avoid name conflict with pygtk
