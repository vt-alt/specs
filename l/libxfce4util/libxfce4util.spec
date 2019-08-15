%def_enable introspection
%def_enable vala

Name: libxfce4util
Version: 4.14.0
Release: alt1

Summary: Utility library for the Xfce desktop environment
Summary(ru_RU.UTF-8): Библиотека утилит для рабочего стола Xfce
License: %lgpl2plus
Group: Graphical desktop/XFce
Url: https://www.xfce.org/

Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/libxfce4util
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
# Automatically added by buildreq on Wed Jan 13 2010
BuildRequires: glib2-devel gtk-doc intltool
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_vala:BuildRequires: vala-tools}

%define _unpackaged_files_terminate_build 1

%description
Basic utility non-GUI functions for Xfce.

%description -l ru_RU.UTF-8
Основные (не графические) утилиты Xfce.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for the %name library.

%if_enabled introspection
%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for %name.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name.
%endif

%if_enabled vala
%package vala
Summary: Vala bindings for %name
Group: System/Libraries
Requires: %name-devel = %EVR
BuildArch: noarch

%description vala
Vala bindings for %name.
%endif

%prep
%setup

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag libxfce4util_version_tag configure.ac.in
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	%{subst_enable introspection} \
	%{subst_enable vala} \
	--enable-gtk-doc \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS README README.Kiosk NEWS TODO
%_libdir/*.so.*
%_sbindir/*

%files devel
%doc %_datadir/gtk-doc/html/%name
%dir %_includedir/xfce4/
%_includedir/xfce4/libxfce4util
%_pkgconfigdir/*.pc
%_libdir/*.so

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/*.typelib

%files gir-devel
%_datadir/gir-1.0/*.gir
%endif

%if_enabled vala
%files vala
%_datadir/vala/vapi/%name-*
%endif

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Updated to 4.14.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.5-alt1
- Updated to 4.13.5.

* Fri Jul 05 2019 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt2
- Enable vala support.
- Enable GObject introspection support.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Updated to 4.13.4.

* Thu May 16 2019 Mikhail Efremov <sem@altlinux.org> 4.13.3-alt1
- Updated to 4.13.3.

* Tue Aug 07 2018 Mikhail Efremov <sem@altlinux.org> 4.13.2-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 4.13.2.

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Mon Feb 24 2014 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Own %_includedir/xfce4.
- Updated to 4.11.0.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.1-alt1.git20130424
- Bump version (this snapshot is newer then %name-4.10.1 release).
- Upstream git snapshot.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Updated to 4.9.0.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Drop obsoleted patches.
- Updated to 4.8.2.

* Mon Aug 29 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt5
- Updated Russian translation.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt4
- Updated Russian translation (by Artem Zolochevskiy).

* Mon Mar 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt3
- Fixed incorrect assertion in xfce_strjoin (patch from upstream).

* Tue Jan 18 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Don't build static libraries.
- Fix Group.

* Mon Jan 17 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.
- License fixed.
- Spec cleanup.

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 4.7.1-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Jan 11 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.7.1-alt1
- New version.

* Mon Jan 04 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Fix build with gtkdocize.

* Fri Oct 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Russian translation added.

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Mon Apr 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.6.0-alt1
- 4.6.0 release 
- license fixed

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Mon Oct 20 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Wed May 21 2008 Eugene Ostapets <eostapets@altlinux.ru> 4.4.2-alt2
- fix odd bug in xfce_localize_path_internal

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Wed Sep 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version 4.4rc1

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 4.2.3.2-alt1.1
- Rebuilt for new pkg-config dependencies.

* Thu Nov 17 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3.2-alt1
- 4.2.3.2

* Mon Nov 14 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Mon Dec 22 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
- 4.0.2
- Do not package %name-devel-staic by default.

* Mon Dec 01 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt2
- *.la files removed.

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.90.0-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
