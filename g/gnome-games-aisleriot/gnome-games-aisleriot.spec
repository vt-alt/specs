%define _unpackaged_files_terminate_build 1
%def_disable snapshot

%define _name aisleriot
%define ver_major 3.22
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.9
Release: alt1

Summary: A collection of card games
Group: Games/Cards
License: GPLv3+ and LGPLv3+ and GFDL
Url: https://wiki.gnome.org/Apps/Aisleriot

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Obsoletes: gnome-games-sol
Provides:  gnome-games-sol = %version-%release
Provides:  %_name = %version-%release

Requires(post,preun): GConf
Requires: pysol-cardsets

%define glib_ver 2.32.0
%define gtk_ver 3.0.0
%define guile_ver 22

BuildRequires: intltool desktop-file-utils yelp-tools libappstream-glib-devel libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver libGConf-devel librsvg-devel libcanberra-gtk3-devel
BuildRequires: libICE-devel libSM-devel guile%guile_ver guile%guile_ver-devel
BuildRequires: /proc

%description
AisleRiot also known as Solitaire or sol is a collection of over 80 card games
which are easy to play with the aid of a mouse.

%prep
%setup -n %_name-%version

%build
export ac_cv_path_GUILE=%_bindir/guile%guile_ver
%autoreconf
%configure \
    --with-pysol-card-theme-path=%_datadir/games/pysol
%make

%install
%makeinstall_std

%find_lang --with-gnome %_name

%post
%gconf2_install %_name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %_name
fi

%files -f %_name.lang
%attr(-,root,games) %_bindir/sol
%_libdir/%_name/
%dir %_libexecdir/%_name
%_libexecdir/%_name/ar-cards-renderer
%_desktopdir/*.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*/*/*.*
%_sysconfdir/gconf/schemas/%_name.schemas
%_datadir/glib-2.0/schemas/org.gnome.Patience.WindowState.gschema.xml
%_datadir/metainfo/sol.appdata.xml
%_man6dir/sol.*

%exclude %_libdir/valgrind/aisleriot.supp

%changelog
* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.22.9-alt1
- 3.22.9

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.22.8-alt1
- 3.22.8

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.7-alt1
- 3.22.7

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt1
- 3.22.6

* Fri Aug 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt2
- fixed guile binary name

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt1
- 3.22.5

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Apr 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt0.1
- updated to 3.22.1-9-gb30db7a
- build with guile22

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.91-alt1
- 3.7.91

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Oct 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Nov 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- first build for Sisyphus

