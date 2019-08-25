%def_disable snapshot
%define _unpackaged_files_terminate_build 1

%define _name hitori
%define xdg_name org.gnome.Hitori
%define ver_major 3.32
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1

Summary: GTK+ application to generate and let you play games of Hitori
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Hitori

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Provides:  %_name = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.16.0
%define cairo_ver 1.4

BuildRequires(pre): meson
BuildRequires: yelp-tools desktop-file-utils libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libcairo-devel >= %cairo_ver

%description
Hitori is a small logic puzzle in a similar vein to the more
popular Sudoku. In the game, the player starts with a square
board of numbers, and has to paint out cells until there are no
duplicate numbers in each row and column.

The following rules apply:
- There must only be one of each number in the unpainted cells in each
  row and column.
- No painted cell may be adjacent to another, vertically or horizontally.
- All the unpainted cells must be joined together vertically and
  horizontally in one group.

These are the only three rules of the game, and so there may well be
multiple solutions to a Hitori puzzle board.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%attr(2711,root,games) %_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml

%changelog
* Thu Aug 22 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Mar 04 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.92-alt1
- 3.31.92

* Sat Feb 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt2
- updated to 3.22.4-37-g7d90827
- fixed build with new autoconf-archive-2019.01.06

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Tue May 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Sun Mar 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Feb 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Nov 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Sat May 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Mar 04 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Tue Dec 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2.1-alt1
- 3.14.2.1

* Sun Oct 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- first build for Sisyphus


