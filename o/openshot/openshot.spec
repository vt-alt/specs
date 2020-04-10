%def_disable snapshot
%define ver_major 2.5
%define xdg_name org.openshot.OpenShot

Name: openshot
Version: %ver_major.1
Release: alt1

Summary: Non Linear Video Editor using Python and MLT
Group: Video
License: GPL-3.0
Url: http://www.openshotvideo.com/

%if_disabled snapshot
#Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-qt-%version.tar.gz
Source: https://github.com/OpenShot/openshot-qt/archive/v%version/%name-qt-%version.tar.gz
%else
# VCS: https://github.com/OpenShot/openshot-qt.git
Source: %name-%version.tar.gz
%endif

BuildArch: noarch

Requires: python3-module-%name >= 0.2.5
Requires: blender inkscape xdg-utils

%add_typelib_req_skiplist typelib(Unity)
# should be self-satisfied
%add_python3_req_skip classes classes.legacy.openshot.classes images
# should be provided by blender
%add_python3_req_skip bpy.props

%define __python %nil
BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-devel python3-module-setuptools python3-module-PyQt5

%description
OpenShot Video Editor is a free, open-source, non-linear video editor. It
can create and edit videos and movies using many popular video, audio,
and image formats. Create videos for YouTube, Flickr, Vimeo, Metacafe,
Xbox, and many more common formats.

%prep
%setup -n %name-qt-%version

%build
%python3_build

%install
%python3_install

#%find_lang --with-qt %name OpenShot
#-f OpenShot.lang

%files
%_bindir/*
%python3_sitelibdir_noarch/%{name}_qt/
%python3_sitelibdir_noarch/*.egg-info/
%_pixmapsdir/*
%_desktopdir/*
%_iconsdir/hicolor/*/*/%{name}-qt.*
%_datadir/mime/packages/*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS README*


%changelog
* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.1-alt1
- 2.5.1

* Mon Feb 10 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Sat Mar 30 2019 Yuri N. Sedunov <aris@altlinux.org> 2.4.4-alt1
- 2.4.4

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- 2.4.3

* Sat Jun 30 2018 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Nov 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Sep 08 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Fri Jun 02 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Wed Apr 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Sat Apr 01 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Thu Jan 26 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0 (qt5)

* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.alpha1.bzr20131031
- Version 1.4.4~alpha1

* Tue Oct 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.3-alt1
- New version

* Mon Apr 02 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt3
- Rebuild with Blender

* Mon Mar 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt2
- Add patch openshot-1.4.2-fix-dialog.patch for fix (ALT #25659) thanks serpiph@

* Tue Feb 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt1
- New version (bugfix release)

* Mon Jan 30 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.1-alt1
- New version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty at altlinux.ru> 1.4.0-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.0-alt1
- New version

* Tue May 10 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.1-alt1
- New version

* Sun Feb 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt1
- New version

* Wed Sep 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.2-alt1
- New version
- Close (ALT #24125)

* Mon Apr 19 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.3-alt1
- New version

* Tue Mar 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.1-alt1
- New version

* Tue Jan 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- Build for ALT
