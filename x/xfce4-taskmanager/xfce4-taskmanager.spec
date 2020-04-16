Name: xfce4-taskmanager
Version: 1.2.3
Release: alt1

Summary: Taskmanager for Xfce Desktop
Summary(ru_RU.UTF-8): Системный монитор для Xfce
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/apps/xfce4-taskmanager
Packager: Xfce Team <xfce@packages.altlinux.org>
Vcs: git://git.xfce.org/apps/xfce4-taskmanager
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: glib2-devel intltool libXmu-devel
BuildRequires: libgtk+3-devel libcairo-devel libwnck3-devel
BuildRequires: exo-csource

%define _unpackaged_files_terminate_build 1

%description
%name is taskmanager application for Xfce desktop environment.

%description -l ru_RU.UTF-8
%name -- Менеджер задач для Xfce.

%prep
%setup
%patch -p1
mkdir m4/

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-gtk3 \
	--enable-wnck3 \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_bindir/*
%_desktopdir/xfce4-taskmanager.desktop
%_iconsdir/hicolor/*/*/*.*

%changelog
* Sat Apr 11 2020 Mikhail Efremov <sem@altlinux.org> 1.2.3-alt1
- Update url.
- Add Vcs tag.
- Don't use rpm-build-licenses.
- Updated to 1.2.3.

* Wed Dec 19 2018 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2.

* Wed Dec 12 2018 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt3
- Fix memory corruption.

* Thu Aug 23 2018 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt2
- Don't require GTK+2 for GTK+3 build.
- Fix debug level.
- Build with GTK+3.
- Update url.
- Patch from upstream:
  + Better utf-8 normalization (bug 14172).
- Drop obsoleted patch.

* Mon Jun 04 2018 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1
- Revert upstream commit for UTF-8 strings, use old ALT patch
  instead.
- Updated to 1.2.1.

* Mon Feb 13 2017 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Enabled debug (minimal).
- Updated to 1.2.0.

* Mon Dec 29 2014 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- Fix build: create m4/ directory.
- Updated to 1.1.0.

* Tue Oct 14 2014 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt2
- Fix UTF-8 strings in the pretty_cmdline().
- Fix fgetc() return type.

* Thu Jan 09 2014 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated BR.
- Updated to 1.0.1.

* Wed Feb 09 2011 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2
- Spec updated, tar.gz -> tar.

* Mon Jun 21 2010 Denis Koryavov <dkoryavov@altlinux.org> 1.0.0-alt1
- New version.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version

* Mon May 19 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0-alt1
- new version

* Mon Jan 29 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.3.2-alt1
- new version

* Thu Aug 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Sun Mar 13 2005 Andrey Astafiev <andrei@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Sat Jan 29 2005 Andrey Astafiev <andrei@altlinux.ru> 0.1.0-alt1
- First build for Sisyphus.


