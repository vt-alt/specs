%define _unpackaged_files_terminate_build 1

Name: zathura
Version: 0.4.4
Release: alt1

Summary: A lightweight document viewer
License: %bsdstyle
Group: Office
Url: https://pwmt.org/projects/%name/
# git://pwmt.org/zathura.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses meson
BuildRequires: libgirara-devel >= 0.3.2-alt1
BuildRequires: intltool libgtk+3-devel libsqlite3-devel python3-module-docutils libmagic-devel zlib-devel
# For man pages
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink

Conflicts: zatura-pdf-poppler < 0.2.5-alt1
Conflicts: zatura-djvu < 0.2.3-alt2
Conflicts: zatura-ps < 0.2.2-alt2
Conflicts: zatura-cb < 0.1.2-alt2

%description
zathura is a highly customizable and functional document viewer based on
the girara user interface library and several document libraries.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: libgtk+3-devel libgirara-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1

%build
%meson
%meson_build -v

%install
%meson_install
#  Create directory for plugins
mkdir -p %buildroot%_libdir/zathura
%find_lang %name

%files -f %name.lang
%doc LICENSE AUTHORS
%_bindir/%name
%dir %_libdir/%name
%_desktopdir/*
%_iconsdir/*/*/*
%_datadir/metainfo/*.xml
%_man1dir/*
%_man5dir/*
%_datadir/dbus-1/interfaces/org.pwmt.*
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*
%_datadir/fish/completions/*

%files devel
%_includedir/*
%_libdir/pkgconfig/*.pc

%changelog
* Mon Sep 16 2019 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Fix URL.
- Updated to 0.4.4.

* Mon Dec 24 2018 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1
- Updated to 0.4.3.

* Tue Sep 25 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt2
- Install zsh completions to site-functions.

* Fri Sep 21 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Updated to 0.4.1.

* Fri May 25 2018 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Updated to 0.4.0.

* Wed Apr 18 2018 Mikhail Efremov <sem@altlinux.org> 0.3.9-alt1
- Updated to 0.3.9.

* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 0.3.8-alt1
- Fixed appdata location.
- Updated to 0.3.8.

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 0.3.7-alt1
- Updated to 0.3.7.

* Wed Apr 27 2016 Mikhail Efremov <sem@altlinux.org> 0.3.6-alt1
- Updated to 0.3.6.

* Mon Feb 15 2016 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1
- Drop obsoleted patch.
- Updated to 0.3.5.

* Mon Dec 21 2015 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- Fix build without libsynctex.
- Updated to 0.3.4.

* Fri Apr 17 2015 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt1
- Updated to 0.3.3.

* Mon Nov 17 2014 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt2
- Fix BR.

* Tue Nov 11 2014 Mikhail Efremov <sem@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.

* Fri Oct 24 2014 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Fri Oct 17 2014 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Package appdata file.
- Updated to 0.3.0.

* Thu Jul 03 2014 Mikhail Efremov <sem@altlinux.org> 0.2.9-alt1
- Updated to 0.2.9.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Build with GTK+3.
- Re-fix build with current libmagic.
- Updated to 0.2.7.

* Tue Nov 26 2013 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1
- Updated to 0.2.6.

* Thu Nov 14 2013 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Fri Aug 16 2013 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Fix build with current libmagic.
- Package LICENSE.
- Updated to 0.2.3.

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Wed Jan 09 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Wed Jun 13 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Enable strict aliasing rules.
- Updated to 0.2.0.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.
- Disable strict aliasing rules.

* Fri Mar 16 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Wed Mar 09 2011 Kirill A. Shutemov <kas@altlinux.org> 0.0.8.2-alt1
- 0.0.8.2-26-ga01ab17

* Tue Aug 10 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.8.1-alt1
- 0.0.8.1

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.7-alt1.1
- rebuilt with new poppler

* Tue Jun 22 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.7-alt1
- 0.0.7

* Thu Jun 03 2010 Kirill A. Shutemov <kas@altlinux.org> 0.0.5-alt1
- First build for ALT Linux Sisyphus

