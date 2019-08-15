Name: xfwm4
Version: 4.14.0
Release: alt1

%def_enable epoxy

Summary: Window manager for Xfce
Summary (ru_RU.UTF8): Менеджер окон для окружения рабочего стола Xfce
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://www.xfce.org/
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/xfwm4
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4ui-gtk3-devel libxfconf-devel

BuildRequires: gnome-doc-utils xml-utils xsltproc
BuildRequires: intltool libSM-devel libXcomposite-devel libXdamage-devel libXext-devel libXrandr-devel libglade-devel
BuildRequires: libstartup-notification-devel libwnck3-devel xorg-cf-files
BuildRequires: libXinerama-devel libXpresent-devel
# For svg support in the glib-compile-resources
BuildRequires: librsvg
%{?_enable_epoxy:BuildRequires: libepoxy-devel}

Requires: xfce4-common

%define _unpackaged_files_terminate_build 1

%description
%name is a window manager for Xfce which complies to the standards
defined at http://www.freedesktop.org/.

%description -l ru_RU.UTF8
Данный пакет содержит в себе менеджер окон для окружения рабочего стола
Xfce.

%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xfwm4_version_tag configure.ac.in
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-startup-notification \
	--enable-randr \
	--enable-render \
	--enable-xsync \
	--enable-xpresent \
	--enable-compositor \
	%{subst_enable epoxy} \
	--disable-silent-rules \
	--enable-debug=minimum

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README TODO AUTHORS
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_liconsdir/*
%_iconsdir/hicolor/scalable/apps/*
%_iconsdir/hicolor/*/actions/*
%_datadir/themes/*
%_libdir/xfce4/*

%changelog
* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Enabled libepoxy support.
- Updated to 4.14.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Updated to 4.13.4.

* Sun Jun 30 2019 Mikhail Efremov <sem@altlinux.org> 4.13.3-alt1
- Drop exo-csource from BR.
- Updated to 4.13.3.

* Sat Jun 22 2019 Mikhail Efremov <sem@altlinux.org> 4.13.2-alt3
- DIsable libepoxy support (workaround for ALT bug #36915).

* Tue May 21 2019 Mikhail Efremov <sem@altlinux.org> 4.13.2-alt2
- Build with libXpresent.
- Build with libepoxy.

* Tue May 21 2019 Mikhail Efremov <sem@altlinux.org> 4.13.2-alt1
- Updated to 4.13.2.

* Tue Aug 07 2018 Mikhail Efremov <sem@altlinux.org> 4.13.1-alt1
- Update description.
- Update url.
- Add librsvg to BR.
- Disable silent rules.
- Enable debug (minimum level).
- Updated to 4.13.1.

* Thu Aug 02 2018 Mikhail Efremov <sem@altlinux.org> 4.12.5-alt1
- Updated BR.
- Updated to 4.12.5.

* Thu Mar 16 2017 Mikhail Efremov <sem@altlinux.org> 4.12.4-alt1
- Use _unpackaged_files_terminate_build.
- Fix changelog entry.
- Updated to 4.12.4.

* Mon May 18 2015 Mikhail Efremov <sem@altlinux.org> 4.12.3-alt1
- Updated to 4.12.3.

* Mon Mar 16 2015 Mikhail Efremov <sem@altlinux.org> 4.12.2-alt1
- Updated to 4.12.2.

* Sun Mar 15 2015 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Mon Feb 16 2015 Mikhail Efremov <sem@altlinux.org> 4.11.3-alt1
- Updated to 4.11.3.

* Tue Jul 29 2014 Mikhail Efremov <sem@altlinux.org> 4.11.2-alt1
- Add missing include.
- Require xfce4-common.
- Updated to 4.11.2.

* Fri Dec 27 2013 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 4.11.1.

* Tue Sep 24 2013 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Don't include stropts.h.
- Updated to 4.11.0.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.1-alt1.git20130426
- Bump version (this snapshot is newer then %name-4.10.1 release).
- Upstream git snapshot.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Wed Apr 11 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Drop obsoleted patch.
- Updated to 4.9.0.

* Tue Dec 20 2011 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Updated to 4.8.3.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Drop obsoleted patches.
- Updated to 4.8.2.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt5
- Updated Russian documentation.
- Updated Russian translation.

* Fri Aug 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt4
- Add Russian documentation (by Artem Zolochevskiy).

* Mon Aug 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt3
- Updated Russian translation (by Artem Zolochevskiy).

* Fri Jul 08 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Fix documentation building.

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.

* Tue Jan 25 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Spec cleanup, tar.bz2 -> tar.
- Drop 01_keysym_svn_backport.patch (obsolete).
- Updated to 4.8.0.

* Thu Sep 03 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt4
- Russian translation updated

* Mon May 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Fix build with new toolchain. Added autoconf and audomake version requiremens. 

* Wed May 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Russian translation updated

* Sun Apr 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Mon Nov 12 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt2
- fix work with gtk 2.12, tnx avm@
- bug 13388

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Fri Nov 10 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt2
- strict library version build requires

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Sat Sep 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- 4.4rc1

* Fri Nov 18 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3.2-alt1
- 4.2.3.2

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

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3.1-alt1
- 4.0.3.1

* Tue Dec 23 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
- 4.0.2

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
