Name: xfce4-appfinder
Version: 4.14.0
Release: alt1

Summary: Application finder for the Xfce4 Desktop Environment
Summary (ru_RU.UTF-8): Утилита поиска приложений для Xfce
License: %gpl2plus
Url: https://www.xfce.org/
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/xfce4-appfinder
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4ui-gtk3-devel libxfconf-devel >= 4.6.0 libgarcon-devel >= 0.1.2
BuildPreReq: exo-csource
BuildRequires: intltool libstartup-notification-devel

# xfrun4 was replaced with xfce4-appfinder
Conflicts: xfce-utils < 4.8.3-alt3

%define _unpackaged_files_terminate_build 1

%description
%name permits to find every application in the system supporting
Desktop entry format.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе утилиту поиска приложений для окружения
рабочего стола Xfce.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfce4_appfinder_version_tag configure.ac.in
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_bindir/*
%_desktopdir/*
%_datadir/metainfo/*.xml

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Updated to 4.14.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.5-alt1
- Updated to 4.13.5.

* Sun Jun 30 2019 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Updated to 4.13.4.

* Mon May 20 2019 Mikhail Efremov <sem@altlinux.org> 4.13.3-alt1
- Updated to 4.13.3.

* Mon Dec 10 2018 Mikhail Efremov <sem@altlinux.org> 4.13.2-alt1
- Updated to 4.13.2.

* Tue Sep 04 2018 Mikhail Efremov <sem@altlinux.org> 4.13.1-alt2
- Ignore menu items without name (closes: #35328).

* Mon Aug 27 2018 Mikhail Efremov <sem@altlinux.org> 4.13.1-alt1
- Updated to 4.13.1.

* Fri Aug 17 2018 Mikhail Efremov <sem@altlinux.org> 4.13.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 4.13.0.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Mon Feb 24 2014 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 4.11.0.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.1-alt1.git20130425
- Bump version (this snapshot is newer then %name-4.10.1 release).
- Upstream git snapshot.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Drop obsoleted patches.
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.5-alt1
- Updated to 4.9.5.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 4.9.4-alt1
- Updated to 4.9.4.

* Fri Jan 27 2012 Mikhail Efremov <sem@altlinux.org> 4.9.3-alt3
- Don't use altlinux-applications.directory.

* Tue Jan 10 2012 Mikhail Efremov <sem@altlinux.org> 4.9.3-alt2
- Replace xfrun4 from xfce-utils with xfce4-appfinder.

* Fri Dec 30 2011 Mikhail Efremov <sem@altlinux.org> 4.9.3-alt1
- Updated to 4.9.3.

* Fri Nov 25 2011 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Remove obsoleted patches.
- Updated to 4.9.2.

* Thu Oct 13 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt4
- Don't show hidden applications.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt3
- Updated Russian translation.

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt2
- Updated Russian translation (by Artem Zolochevskiy).

* Wed Jan 26 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- additional-category.patch updated.
- tar.bz2 -> tar.
- Updated to 4.8.0.

* Wed Nov 18 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Repocop warnings is taken into account.

* Thu May 14 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Russian translation updated

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
- Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
- Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Sun Oct 01 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- 4.4rc1

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
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
- First version of RPM package for Sisyphus.
