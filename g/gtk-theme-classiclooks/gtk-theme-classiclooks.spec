%define theme_name "ClassicLooks"

Name: gtk-theme-classiclooks
Version: 1.4.2
Release: alt1
Epoch: 1
Summary: ClassicLooks is a Gtk2 & Gtk3 themes
Group: Graphical desktop/XFce

License: GPLv2+
URL: http://www.itgroup.ro/classiclooks
Source: %name-%version.tar

BuildArch: noarch

Requires: gtk2-theme-classiclooks = %EVR
Requires: gtk3-theme-classiclooks = %EVR
Requires: xfwm4-theme-classiclooks = %EVR

Provides: gtk-theme-xfce-evolution = %EVR
Obsoletes: gtk-theme-xfce-evolution <= 5.8.0-alt1

%define _unpackaged_files_terminate_build 1

%description
ClassicLooks is a Gtk+ theme aimed at providing increased consistency
across the most commonly used GUI toolkits (Gtk2/3, Qt4/5, wxWidgets2/3,
OpenOffice3/4); additionally, ClassicLooks tries to be "compatible"
with the default Gtk3 theme 'Adwaita' in the sense that an application GUI
designed to look good on Adwaita should also look good on ClassicLooks.

ClassicLooks currently supports only the XFCE desktop (the XFCE panels and
the XFWM4 window manager); support for other desktop environments is planned
for future releases.

ClassicLooks relies upon, and/or is derived from:
- Xfce Evolution Theme (http://xfce-evolution.sourceforge.net)
- Gtk2 Murrine Engine (gtk2, wxWidgets2/3, qt4/5)
- Qt5 Style Plugins (qt5)

%package -n gtk2-theme-classiclooks
Summary: ClassicLooks GTK+2 themes
Group: Graphical desktop/XFce
Requires: libgtk-engine-murrine
Provides: gtk2-theme-xfce-evolution = %EVR
Obsoletes: gtk2-theme-xfce-evolution <= 5.8.0-alt1

%description -n gtk2-theme-classiclooks
Themes for GTK+2 as part of the ClassicLooks theme.

%package -n gtk3-theme-classiclooks
Summary: ClassicLooks GTK+3 themes
Group: Graphical desktop/XFce
Provides: gtk3-theme-xfce-evolution = %EVR
Obsoletes: gtk3-theme-xfce-evolution <= 5.8.0-alt1

%description -n gtk3-theme-classiclooks
Themes for GTK+3 as part of the ClassicLooks theme.

%package -n xfwm4-theme-classiclooks
Summary: ClassicLooks Xfwm4 themes
Group: Graphical desktop/XFce
Provides: xfwm4-theme-xfce-evolution = %EVR
Obsoletes: xfwm4-theme-xfce-evolution <= 5.8.0-alt1

%description -n xfwm4-theme-classiclooks
Themes for Xfwm4 as part of the ClassicLooks theme.

%prep
%setup
find -type f -executable -not -name "*.sh" -exec chmod -x '{}' \;

%install
mkdir -p %buildroot%_datadir/themes/
find -maxdepth 1 -type d -name %theme_name"*" -printf '%f\n' | while read l; do
	mkdir %buildroot%_datadir/themes/"$l"/
	for d in gtk-2.0 gtk-3.0 xfwm4; do
		[ -d "$l"/"$d" ] || continue
		cp -r "$l"/"$d"/ %buildroot%_datadir/themes/"$l"/
	done
done


%files

%files -n gtk2-theme-classiclooks
%dir %_datadir/themes/*
%_datadir/themes/*/gtk-2.0/
%exclude %_datadir/themes/*XFWM4*

%files -n gtk3-theme-classiclooks
%dir %_datadir/themes/*
%_datadir/themes/*/gtk-3.0/
%exclude %_datadir/themes/*XFWM4*

%files -n xfwm4-theme-classiclooks
%dir %_datadir/themes/*XFWM4*
%_datadir/themes/*/xfwm4/

%changelog
* Tue Jan 21 2020 Mikhail Efremov <sem@altlinux.org> 1:1.4.2-alt1
- Updated to 1.4.2.

* Thu Jan 16 2020 Mikhail Efremov <sem@altlinux.org> 1:1.4.1-alt1
- Don't use rpm-build-licenses.
- Updated to 1.4.1.

* Thu Oct 24 2019 Mikhail Efremov <sem@altlinux.org> 1:1.2.7-alt1
- Updated to 1.2.7.
- Own themes directories.

* Mon Oct 07 2019 Mikhail Efremov <sem@altlinux.org> 1:1.2.1-alt1
- Renamed to gtk-theme-classiclooks.
- Updated to 1.2.1.

* Thu Mar 07 2019 Mikhail Efremov <sem@altlinux.org> 5.8.0-alt1
- Updated to 5.8.0.

* Thu Feb 14 2019 Mikhail Efremov <sem@altlinux.org> 5.6.7-alt1
- Initial build.
