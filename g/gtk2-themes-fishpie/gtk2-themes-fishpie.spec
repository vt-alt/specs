%define base gtk2-themes
%define _name fishpie

Name: %base-%_name
Version: 0.0
Release: alt1

Summary: A GTK+2 theme - Fish Pie
License: GPL
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org/pub/gnome/teams/art.gnome.org/themes/gtk2/

Source: %name.tar.gz

BuildArch: noarch
Requires: gtk-engines-pixmap

%description
This GTK2 theme is derivved completely from "fishing the sky" by Paul
Hendrick. All was changed the pngs.  This theme goes pretty well with
the "meta marker" theme for metacity, just like the original.

%prep
%setup -q -n %_name

%install
%__mkdir_p %buildroot%_datadir/themes/%_name
%__cp -r gtk-2* %buildroot%_datadir/themes/%_name

%files
%_datadir/themes/*
%doc README

%changelog
* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.0-alt1
- First build for Sisyphus.
