%def_disable qt4
%def_enable qt5
%define git_rev 7d856c17

Name:    qtcurve
Version: 1.9.0
Release: alt1.git%git_rev
Epoch:   2

Summary: A set of widget styles for GTK+ and Qt widget toolkits
License: LGPL-2.1+
Group:   Graphical desktop/Other
Url:     https://github.com/KDE/qtcurve

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch1: qtcurve-1.8.18-no_env.patch
Patch2: maint.patch
Patch3: qtcurve-1.9.0-build_testing.patch
Patch4: qtcurve-1.9.0-gcc9.patch
Patch5: qtcurve-1.9.0-libreoffice-crashfix.patch
Patch6: qtcurve-1.9.0-no-X-buildfix.patch
Patch7: qtcurve-1.9.0-qt-5.15.patch

BuildRequires(pre): kde-common-devel rpm-macros-qt3 rpm-macros-qt4 cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ libgtk+2-devel
%if_enabled qt4
BuildRequires: kde4libs-devel
BuildRequires: kde4base-workspace-devel
%endif
BuildRequires: git-core
BuildRequires: pkgconfig(x11-xcb)
%if_enabled qt5
BuildRequires(pre): rpm-build-kf5
BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5Svg) pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kdelibs4support-devel
BuildRequires: kf5-kemoticons-devel
BuildRequires: kf5-kitemmodels-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: kf5-frameworkintegration-devel
%endif

Requires: %name-gtk2 = %version-%release
%if_enabled qt4
Requires: %name-qt4 = %version-%release
%endif
%if_enabled qt5
Requires: %name-qt5 = %version-%release
Requires: %name-kf5 = %version-%release
%endif

%description
QtCurve is a desktop theme for the GTK+ and Qt widget toolkits, allowing
users to achieve a uniform look between these widget toolkits.

%package libs
Summary: Runtime libraries for QtCurve
Group:   Graphical desktop/Other

%description libs
Runtime libraries for QtCurve

%package -n gtk2-themes-%name
Summary: The QtCurve engine for GTK2
Group:   Graphical desktop/GNOME
Provides: gtk-engines-%name
Provides: %name-gtk2 = %version-%release
Obsoletes: gtk-engines-%name < %version-%release gtk1-themes-%name < %version-%release

%description -n gtk2-themes-%name
The QtCurve engine for GTK2

%if_enabled qt4
%package -n qt4-styles-%name
Group:   Graphical desktop/KDE
Summary: QtCurve style for Qt4
Provides: kde4-styles-%name = %version-%release
Obsoletes: kde4-styles-%name < %version-%release
Provides: %name-qt4 = %version-%release

%description -n qt4-styles-%name
This is a set of widget styles for Qt4
%endif

%if_enabled qt5
%package -n qt5-styles-%name
Group:   Graphical desktop/KDE
Summary: QtCurve style for Qt5
Provides: %name-qt5 = %version-%release

%description -n qt5-styles-%name
This is a set of widget styles for Qt5

%package -n kf5-styles-%name
Group:   Graphical desktop/KDE
Summary: QtCurve style for KF5
Provides: %name-kf5 = %version-%release

%description -n kf5-styles-%name
This is a set of widget styles for KF5
%endif

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%cmake  -GNinja \
	-DENABLE_QT5:BOOL=%{?_enable_qt5:ON}%{!?_enable_qt5:OFF} \
	-DQTC_QT4_ENABLE_KDE:BOOL=OFF
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

# unpackaged files
rm -fv %buildroot%_libdir/libqtcurve-{cairo,utils}.so
rm -f %buildroot%_datadir/kxmlgui5/QtCurve/QtCurveui.rc

# Move KF5 file to appropriate place
mkdir -p %buildroot%_K5data/kstyle/themes/
mv %buildroot%_datadir/kstyle/themes/qtcurve.themerc %buildroot%_K5data/kstyle/themes/

%files

%files libs
%doc AUTHORS Bugs.md README.md TODO.md ChangeLog.md COPYING
%_libdir/libqtcurve-utils.so.2*

%files -n gtk2-themes-%name
%_libdir/gtk-2.0/*/engines/libqtcurve.so
%_libdir/libqtcurve-cairo.so.1*
%_datadir/themes/QtCurve/

%if_enabled qt4
%files -n qt4-styles-%name
%_qt4dir/plugins/styles/qtcurve.so
%endif

%if_enabled qt5
%files -n qt5-styles-%name
%_qt5_plugindir/styles/qtcurve.so

%files -n kf5-styles-%name
%_qt5_plugindir/kstyle_qtcurve5_config.so
%_K5data/kstyle/themes/qtcurve.themerc
%endif

%changelog
* Mon Sep 28 2020 Andrey Cherepanov <cas@altlinux.org> 2:1.9.0-alt1.git7d856c17
- New version from https://github.com/KDE/qtcurve.
- Fix project URL and License.
- Apply all fixes from https://github.com/KDE/qtcurve/tree/1.9.
- Build using Ninja.
- Apply patches from Gentoo.

* Thu Nov 28 2019 Ivan A. Melnikov <iv@altlinux.org> 1:1.9.1-alt3
- Fix build with gcc9 (upstream patch for https://bugs.kde.org/408286).

* Thu Mar 28 2019 Andrey Cherepanov <cas@altlinux.org> 1:1.9.1-alt2
- Drop qt4 support due to kde4libs missing.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.9.1-alt1
- New version.

* Sat Jul 30 2016 Andrey Cherepanov <cas@altlinux.org> 1:1.8.18-alt1.git3d313d5
- New version 1.8.18
- Build from upstream Git repository

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 1:1.8.15-alt2
- rebuilt against gcc5-built qt3

* Thu Jan 03 2013 Andrey Cherepanov <cas@altlinux.org> 1:1.8.15-alt1
- New versions: 1.8.15 (Gtk2), 1.8.14 (KDE4), 1.8.5 (KDE3) (ALT #27481)

* Sun Sep 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.6.3-alt1
- 1.6.3 (KDE4 & Gtk2), 1.6.2 (KDE3)

* Fri Sep 24 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.6.2-alt1
- 1.6.2 (KDE4 & Gtk2), 1.6.1 (KDE3)

* Wed Sep 15 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.6.1-alt1
- 1.6.1 (KDE4 & Gtk2), 1.6.0 (KDE3)

* Mon Sep 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.6.0-alt1
- 1.6.0

* Wed Jul 21 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.5.2-alt1
- 1.5.2 (KDE4 & Gtk2), 1.5.0 (KDE3)

* Mon Jul 12 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.5.1-alt1
- 1.5.1 (KDE4 & Gtk2), 1.5.0 (KDE3)

* Tue Jun 29 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.5.0-alt1
- 1.5.0

* Thu May 27 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.4.2-alt1
- 1.4.2 (KDE4), 1.4.1 (KDE3 & Gtk2)

* Sat May 15 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Tue Apr 13 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Fri Mar 19 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Thu Feb 25 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Fri Feb 05 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.2-alt2
- link the kde3 style plugin with -lkdecore
- add qt3-only subpackage

* Mon Feb 01 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.2-alt1
- 1.0.2 (KDE4 & Gtk2), 1.0.1 (KDE3)

* Wed Jan 13 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.1-alt1
- 1.0.1 (KDE4 & Gtk2), 1.0.0 (KDE3)

* Mon Oct 19 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.69.2-alt1
- 0.69.2 (KDE4 & Gtk2), 0.69.1 (KDE3)
- re-enable qt4-only subpackage

* Fri Oct 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.69.0-alt1
- 0.69.0 (closes: #21828)
- disable qt4-only subpackage

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.68.1-alt1
- 0.68.1

* Wed Sep 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.68.0-alt1
- 0.68.0

* Wed Aug 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.67.6-alt1
- 0.67.6 (KDE4), 0.67.5 (Gtk2), 0.67.3 (KDE3)

* Wed Aug 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.67.5-alt1
- 0.67.5 (KDE4), 0.67.4 (Gtk2), 0.67.2 (KDE3)

* Tue Aug 11 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.67.4-alt1
- 0.67.4 (KDE4), 0.67.3 (Gtk2), 0.67.1 (KDE3)

* Sat Jul 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.67.1-alt1
- 0.67.1 (KDE4 & Gtk2), 0.67.0 (KDE3)

* Tue Jul 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.66.1-alt1
- 0.66.1 (KDE4), 0.66.0 (KDE3 & Gtk2)

* Sun Jul 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.4-alt1
- 0.65.4 (KDE4 & KDE3), 0.65.3 (Gtk2)

* Sun Jul 05 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.3-alt1
- 0.65.3

* Thu Jul 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.2-alt1
- 0.65.2

* Mon Jun 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.1-alt1
- 0.65.1

* Wed Jun 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.0-alt1
- 0.65.0
- package qt4-only version

* Mon Jun 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.64.2-alt1
- 0.64.2
- use optflags for KDE3 & Gtk2

* Tue Jun 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.63.0-alt1
- 0.63.0

* Sun May 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.62.7-alt1
- 0.62.9 (KDE4), 0.62.7 (KDE3), 0.62.8 (Gtk2)
- build KDE4 window decorations
- package docs

* Tue Mar 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.62.6-alt1
- 0.62.6

* Mon Mar 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.62.4-alt1
- 0.62.4

* Sun Mar 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.61.4-alt1
- 0.61.4

* Wed Feb 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.60.0-alt1
- 0.60.0

* Thu Oct 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.7-alt2
- fixed build

* Thu Aug 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.7-alt1
- 0.59.7

* Sat Jun 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.4-alt1
- 0.59.4

* Sun May 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.1-alt1
- 0.59.1

* Thu Apr 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.0-alt1
- 0.59.0

* Wed Mar 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.58.0-alt1
- 0.58.0

* Fri Mar 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.57.1-alt1
- 0.57.1

* Thu Mar 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.57.0-alt1
- 0.57.0

* Tue Mar 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.56.3-alt1
- 0.56.3

* Thu Feb 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.56.2-alt1
- 0.56.2

* Tue Feb 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.56.1-alt1
- 0.56.1:
  + Fix crash when using corner default button indicator and no coloured mouse over
  + Fix for OpenOffice.org blanking combobox text when mouse over arrow

* Mon Feb 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.56.0-alt1
- 0.56.0

* Sat Feb 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.3-alt2
- new subpackage kde4-styles-%name

* Thu Feb 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.3-alt1
- 0.55.3

* Sat Jan 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.2-alt2
- added object-flip-horizontal, object-flip-vertical, object-rotate-left,
  object-rotate-right, x-office-presentation icons KDE3 Gtk2 substitution

* Sun Jan 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.2-alt0.M40.1
- build for branch 4.0

* Fri Jan 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.2-alt1
- 0.55.2:
  KDE3:
    1. Add ability to import qtc_*.themerc settings into config dialog.
    2. Lighten dockwidget titlebars.
  Gtk2:
    1. Fix look of disabled entry fields.
    2. Style Gtk2.12 tooltips
    3. Improve look of edit field under firefox3
    4. Fix menubar items for Firefox 3
    5. Use 32x32 as dialog icon size.
    6. Nicer tabs for Firefox 3.
    7. Better (not perfect) scrollbar types for Firefox3.

* Sat Dec 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.1-alt1
- 0.55.1:
  KDE3:
    1. Only allow coloured selected tabs if tab appearance is set to gradient.
    2. Allow triangular sliders when not rounding.
    3. Fix appearance of flat/raised disabled scrollbar buttons - more consistent with Gtk2 and KDE4
    4. Fix potential infinte loop when elliditiding title string.
    5. Also eliditude vertical titlebars.
  Gtk2:
    1. Only allow coloured selected tabs if tab appearance is set to gradient.
    2. Allow triangular sliders when not rounding.

* Fri Oct 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.0-alt2
- fixed #13106

* Thu Oct 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.0-alt1
- 0.55.0:
  KDE3:
    1. Ability to create custom themes. See Theme details in 'README' file.
    2. Supply a 'Klearlooks' QtCurve theme.
  Gtk2:
    1. Ability to create custom themes. See Theme details in 'README' file.
    2. Fix for 'inactiveHighlight' and KDE's apply colours to non-KDE apps.
  All:
    1. Allow 'flat' lines in scrollbar handles, toolbar handles, toolbar separators, and splitters.
    2. Option for 'X' style checkmarks.
    3. Option to have colour the selcted tab.
    4. Optional diagonal progressbar sripes.
    5. Use alternating dark/light for dashed toolbar handles.
    6. New 'split' style gradient.
    7. Option to specift slider style: plain, round (only when appearance=round), and triangular (plastik-ish)
    8. Modify default style: flat splitter lines, flat slider thumbs, no toolbar separators, triangular slider,
       diagonal progressbar stripes.

* Fri Sep 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.52.3-alt2
- rollback to 0.52.3

* Wed Sep 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.54.0-alt1
- 0.54.0:
  KDE3:
    1. Converted buildsystem to CMake.
    2. New option 'inactiveHighlight', if set then use a mix of highlight and background colour as highlight for inactive windows/elements.
    3. Set KDE3 colours from Qt4 settings if running under KDE4.
    4. Read in Qt3's inactive palette settings for highlight and highlightedText.
    5. If an inactive palette is set (e.g. via qtconfig), ensure that progress bar text is unaffected.
    6. Remove frames from source/destination labels of kio progress dialogs.
    7. Add gui to set shading option.
    8. Nicer look for selected tab highlight.
  Gtk2:
    1. Converted buildsystem to CMake.
    2. New option 'inactiveHighlight', if set then use a mix of highlight and background colour as highlight for inactive windows/elements.
    3. Fix broken 'Thinner Menuitems' option.
    4. Better code for alternate list view background.
    5. Also read in Qt's inactive palette.
    6. If read a font setting from /etc/qt3/qtrc,
       and there is not font setting in ~/.qt/qtrc - then use the setting from /etc/qt3/qtrc, as opposed to setting a default.
    7. When reading Qt4 settings, also read /etc/xdg/Trolltech.conf
    8. Nicer look for selected tab highlight.
    9. realloc() fix - thanks to 'hoodedone'	    
	   
* Wed Sep 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.53-alt2
- added map_kde_icons.pl

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.53-alt1
- 0.53:
  KDE3:
    1. Removed 'Shadow buttons' option, and replaced with none/shadow/etch setting - default to 'none'.
    2. Added 'passwordChar' option to set character used for password entries.
    3. Option to have frameless groupboxes - Gtk like.
    4. Add an 'Advanced' tab to config dialog.
    5. Add config item gtkButtonOrder set to 'true' to use Gtk/GNOME button order.
    6. Modified contrast settings to be more varied.
    7. Gradient background of checks and radios, if appearance is not flat/raised.
  Gtk2:
    1. Removed 'Shadow buttons' option, and replaced with none/shadow/etch setting - default to 'none'.
    2. Added 'passwordChar' option to set character used for password entries.
    3. Option to have frameless groupboxes - Gtk like.
    4. Add config item 'gtkButtonOrder' set to 'true' to use Gtk/GNOME button order.
    5. Added config item 'mapKdeIcons' to control whether to map KDE icons or not.
    6. Modified contrast settings to be more varied.
    7. Gradient background of checks and radios, if appearance is not flat/raised.
    8. Create kde-icon map on the fly - allows icon sizes to be read from kdeglobals.
    9. KDE's "apply colours to non-KDE apps" setting seems to mess up the text on progressbars, workaround this.
    10. Read alternate listview colour from KDE settings.
    11. More KDE like framed groupboxes.

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.52.3-alt1
- 0.52.3:
  KDE3:
    1. Don't lighten border of disabled check/radio buttons.
    2. Lighten trough of disabled slider.
    3. Modify khtml check to also check to see if widget name == "__khtml"
    4. Store khtml widgets in a map, to speed up checking.
    5. Fix shadow on comboboxes.
    6. Draw background of checked menuitem icons as per KDE4.
  Gtk2:
    1. Fix 1st stripe on vertical progress bar.
    2. Fix very small progress bar chunks.
    3. Fix blanked out widgets in tovid.
    4. Fix DeVeDe crash when 'fix parentless dialogs' is enabled.
	 
* Fri Jun 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.52.2-alt1
- 0.52.2:
  1. Fix crash when slider colour == button.

* Thu Jun 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.52.1-alt1
- 0.52.1:
  1. Draw emphasis around menus when not lightening.
  2. Use button colours to border entry fields.
  3. Dont allow scrollbars to be recoloured.
  4. Fix amarok menus.

* Tue Jun 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.52-alt1
- 0.52:
  1. Use 'dull glass' as the default gradient - previous default is now called 'Clean'.
  2. Darken slider mouse over colour if slider is not shaded.
  3. Use thinner slider mouse over sections if slider is not shaded.
  4. Improve look of small V arrows.
  5. Even duller dull glass, but much more useable.
  6. Fix setting of check/radio colour.
  7. Only highlight editable combo arrow when mouse over arrow, not over edit field - more Gtk like.
  8. Added one config file option (no gui):
     gtkScrollViews set to 'true' to have the scrollbars drawn outside of scrollviews. (However, doesn't look very good)
  9. Lighten combo list frame.
  10. Dont round MDI buttons.
  11. Fix opera's MDI buttons within menubars.
  12. Always assume PE_ButtonBevel is enabled - used for QtConfig's colour buttons.

* Mon Jun 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.51-alt1
- 0.51:
  1. Changed shading to use HSL colour space. This can be altered by editing
     $XDG_CONFIG_HOME/qtcurvestylerc and setting 'shading=simple' for the previous
     method, or 'shading=hsv' to use HSV.
  2. Add options:
     Border all of menu/toolbars.
     Darker borders.
     'V' arrows.
  3. Fix raised listview headers.
  4. Fix glass style menuitem appearance.
  5. Modifed look of dullglass, looks "softer"
  6. Improve look of plastik mouse-over for non coloured scrollbars.
  7. For disabled buttons, use standard fill but lighten border.
  8. Use darker colours for mouse-over and default button - helps with light colour schemes.
  9. Dont draw sunken panel around checked menuitems.
  10. If the app is a Java app, and its g_get_application_name()!="unknown", then assume
      its a SWT java app - in which case treat as a standard app. For Swing apps some
      functionality is disabled.
  11. Fix tabs in thunderbird.

* Wed May 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.50-alt4
- update QtCurve-Gtk2-0.50-alt-qtrc.patch, thanks Sergey V Turchin

* Tue May 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.50-alt3
- set icons size 22 for gtk-dnd and gtk-dialog

* Sun May 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.50-alt2
- fixed default icons path

* Fri May 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.50-alt1
- 0.50:
  1. Add settings for:
     Fill used slider
     Round menubar item top only
     Menuitem appearance
     Border menuitems
     Progressbar appearance
     Gradient progressbar groove
     Use standard buttons for sidebar buttons
     Check/radio colour
     Plastik style mouse-over
  2. Dont colour menubar items on mouse over if not colouring menubars.
  3. When drawing menubar borders, only draw bottom line.
  4. When drawing toolbar borders, only draw top/bottom or left/right - depending upon orientation.
  5. Draw checks/radios within listviews the same as standard.
  6. Use 'foreground' colour for menu text.

* Wed May 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.49-alt1
- 0.49

* Tue May 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.48.5-alt1
- 0.48.5

* Fri Apr 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.48.4-alt1
- 0.48.4

* Fri Feb 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.46.4-alt1
- 0.46.4:
  + KDE:
    1. Only draw gradients if width>0 && height>0
  + Gtk2:
    1. Only draw gradients if width>0 && height>0

* Fri Jan 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.46.3-alt1
- 0.46.3:
  + KDE:
    1. Fix look of flat/raised style menuitems and progressbars.
    2. Fix look of read-only KLineEdits.
  + Gtk2:
    1. Fix look of flat/raised style menuitems and progressbars.
    2. Use pkg-config to obtain Gtk2 libdir.

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.46.2-alt1
- 0.46.2:
  + KDE Only:
    1. Remove rgb2Hls() and hls2Rgb() unless using old style shading.
    2. Don't mouse-over disabled tabs!
    3. Fix look of flat style tabs.
  + Gtk2 Only:
    1. Remove rgb2Hls() and hls2Rgb() unless using old style shading.
    2. Use fileno() to obtain file descriptor of FILE * stream.
    3. Fix look of slider grooves for 'flat' appearance.
    4. Fix appearance of checkboxes for 'bevelled' appearance.

* Thu Dec 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.46.1-alt1
- 0.46.1

* Wed Nov 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.46-alt1
- 0.46

* Tue Nov 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45.3-alt2
- KDE Only:
  1. Correctly place check and radio buttons.
  2. Improve drawing of very small progress.

* Thu Nov 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45.3-alt1
- 0.45.3:
  + Gtk2 Only
    1. When determinging background of popup menu for AA'ing, use shade window colour, not button.
    2. Fix for "-1" warnings reported by some users.

* Mon Nov 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45.2-alt1
- 0.45.2:
  + KDE Only:
    1. Make kaffeine's sidebar buttons consistent when coloured.
    2. Fix look of dvd authoring wizard buttons.
  + Gtk2 Only
    1. Fix coloured menubars.
    2. Fix firefox 2's "stack smashing detected" errors.
    3. Remove ok/Cancel button swapping from QtCurve.css, does not work for firefox 2.x
  
* Tue Oct 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45.1-alt1
- 0.45.1:
  + Both:
    1. Restore pre 0.45 inactive window highlight. Option is still there to re-activate.
  + KDE Only:
    1. Fix dark text appearing on progressbars.
    2. Use KStyle to draw status bar elements - if enabled.
  + Gtk2 Only:
    1. Use listview header settings for listview headers!

* Thu Oct 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45-alt1
- 0.45

* Fri Oct 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.44.3-alt1
- 0.44.3

* Fri Oct 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.44.2-alt1
- 0.44.2

* Tue Oct 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.44.1-alt1
- 0.44.1

* Tue Oct 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.44-alt1
- 0.44

* Sat Sep 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.43.2-alt1
- 0.43.2

* Sun Sep 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.43-alt1
- 0.43

* Sat Sep 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.42.3-alt1
- 0.42.3

* Thu Aug 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.42-alt1
- 0.42

* Tue Aug 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.41.1-alt2
- rebuild

* Sun Aug 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.41.1-alt1
- 0.41.1

* Tue Jul 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.40-alt1
- 0.40

* Thu Jul 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.39.1-alt1
- 0.39.1

* Fri Jun 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.38-alt1
- 0.38

* Thu Jun 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.37-alt1
- 0.37

* Thu Jun 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.36-alt1
- 0.36

* Sat May 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.35.1-alt3
- obsolete subpackage gtk-engines-%name
- new subpackages gtk1-themes-%name, gtk2-themes-%name

* Wed Apr 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.35.1-alt2
- fixed build for x86_64

* Sat Apr 22 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.35.1-alt1
- 0.35.1

* Tue Mar 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.34-alt1
- 0.34

* Thu Feb 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.33-alt1
- 0.33

* Fri Feb 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.31.1-alt1
- 0.31.1

* Mon Feb 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.29.1-alt1
- 0.29.1

* Thu Feb 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.28-alt1
- 0.28

* Fri Jan 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.26-alt1
- 0.26

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.25-alt1
- 0.25

* Thu Jan 12 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.24.2-alt1
- 0.24.2

* Fri May 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.23.1-alt1
- 0.23.1

* Fri Jan 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.22-alt1.1
- rebuild with libstdc++.so.6

* Wed May 19 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.22-alt1
- new version

* Thu May 13 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.21-alt1
- new version

* Thu Apr 22 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.20-alt1
- new version

* Thu Apr 08 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.18-alt2
- rebuild for gtk+2-2.4

* Mon Apr 05 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.18-alt1
- new version

* Tue Mar 30 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt3
- add qt3 patch

* Wed Mar 03 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt2
- rebuild

* Sat Feb 14 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt1
- initial release
