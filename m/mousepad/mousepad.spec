Name: mousepad
Version: 0.4.2
Release: alt1

Summary: Mousepad - A simple text editor for Xfce
Summary (ru_RU.UTF-8): Простой текстовый редактор для Xfce
License: %gpl2plus
Group: Editors
Url: https://www.xfce.org
Packager: Xfce Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libxfconf-devel
BuildRequires: libgtk+3-devel intltool libgtksourceview3-devel libgio-devel
BuildRequires: exo-csource

Obsoletes: xfce-mousepad < %version
Provides: xfce-mousepad = %version-%release

%define _unpackaged_files_terminate_build 1

%description
Mousepad is a text editor for Xfce based on Leafpad. The initial reason
for Mousepad was to provide printing support, which would have been
difficult for Leafpad for various reasons.

%description -l ru_RU.UTF-8
Mousepad - простой текстовый редактор для Xfce основанный на Leafpad.
Одной из причин разработки нового редактора было предоставление
возможности печати, что было сложно реализуемо для редактора Leafpad
по некоторым причинам.

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag mousepad_version_tag configure.ac.in

%build
%xfce4reconf
%configure --enable-dbus \
	--enable-maintainer-mode \
	--enable-gtk3 \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang mousepad

%files -f mousepad.lang
%doc NEWS README
%_bindir/*
%_datadir/polkit-1/actions/*.policy
%_datadir/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
%_desktopdir/*

%changelog
* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Updated to 0.4.2.

* Tue Aug 28 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt2
- Enable debug (minimum level).
- Update url.
- Use _unpackaged_files_terminate_build.
- Build with GTK+3.

* Mon Jun 04 2018 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Updated to 0.4.1.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.4.0.

* Sat Jan 05 2013 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- From upstream git:
    + Set textdomain codeset to utf-8.
    + Fix desktop file.
    + Updated translations.
- Updated to 0.3.0.
- Renamed to mousepad.

* Wed Jun 09 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.99-alt2
- Fixed bug when the 'Undo' action works incorrectly with non-latin symbols.

* Sat May 22 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.99-alt1
- New development version.

* Mon May 17 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.16-alt2
- Added Debian patches for Mousepad.

* Mon May 17 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.2.16-alt1
- New version.

* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.14-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for xfce-mousepad
  * postclean-05-filetriggers for spec file

* Sun Nov 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.14-alt1
- Xfce 4.4.3 release

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 0.2.13-alt1
- Xfce 4.4.2 release
- rename package
* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.12-alt0.1
- Xfce 4.4 release

* Fri Nov 10 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.2.10-alt2
- strict build requires libgtk+2-devel

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  0.2.10-alt1
- First version of RPM package for Sisyphus.
