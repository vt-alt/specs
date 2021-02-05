%define theme_name Greybird

Name: gtk-theme-greybird
Version: 3.22.14
Release: alt1
Summary: A clean minimalistic theme for Xfce, GTK+ 2 and 3
Group: Graphical desktop/XFce

License: GPLv2+ or CC-BY-SA
URL: https://shimmerproject.org/
Vcs: https://github.com/shimmerproject/Greybird
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): meson

BuildRequires: sassc xml-utils
# For glib-compile-resources
BuildRequires: libgio
# For gdk-pixbuf-pixdata
BuildRequires: libgdk-pixbuf-devel librsvg

Requires: gtk2-theme-greybird = %version-%release
Requires: gtk3-theme-greybird = %version-%release
Requires: metacity-theme-greybird = %version-%release
Requires: xfwm4-theme-greybird = %version-%release
Requires: xfce4-notifyd-theme-greybird = %version-%release

%define _unpackaged_files_terminate_build 1

%description
Greybird is a theme for GTK2/3 and xfwm4/metacity started out on the basis of
Bluebird, but aims at reworking the intense blue tone to a more neutral
grey-ish look that will be more pleasant to look at in everyday use.

%package common
Summary: Common files for Greybird GTK+ themes
Group: Graphical desktop/XFce

%description common
Common files for Greybird GTK+ themes.

%package -n gtk2-theme-greybird
Summary: Greybird GTK+2 themes
Group: Graphical desktop/XFce
Requires: %name-common = %version-%release
Requires: libgtk-engine-murrine

%description -n gtk2-theme-greybird
Themes for GTK+2 as part of the Greybird theme.

%package -n gtk3-theme-greybird
Summary: Greybird GTK+3 themes
Group: Graphical desktop/XFce
Requires: %name-common = %version-%release

%description -n gtk3-theme-greybird
Themes for GTK+3 as part of the Greybird theme.

%package -n metacity-theme-greybird
Summary: Greybird Metacity themes
Group: Graphical desktop/GNOME
Requires: %name-common = %version-%release

%description -n metacity-theme-greybird
Themes for Metacity as part of the Greybird theme.

%package -n xfwm4-theme-greybird
Summary: Greybird Xfwm4 themes
Group: Graphical desktop/XFce
Requires: %name-common = %version-%release

%description -n xfwm4-theme-greybird
Themes for Xfwm4 as part of the Greybird theme.

%package -n xfce4-notifyd-theme-greybird
Summary: Greybird Xfce4 notifyd theme
Group: Graphical desktop/XFce
Requires: %name-common = %version-%release

%description -n xfce4-notifyd-theme-greybird
Themes for Xfce4 notifyd as part of the Greybird theme.

%prep
%setup

%build
%meson
%meson_build -v

%install
%meson_install

%files

%files common
%doc LICENSE.GPL LICENSE.CC
%dir %_datadir/themes/%theme_name/
%_datadir/themes/%theme_name/index.theme
%dir %_datadir/themes/%theme_name-dark/
%_datadir/themes/%theme_name-dark/index.theme

%files -n gtk2-theme-greybird
%_datadir/themes/%theme_name/gtk-2.0/
%_datadir/themes/%theme_name-dark/gtk-2.0/

%files -n gtk3-theme-greybird
%_datadir/themes/%theme_name/gtk-3.0/
%_datadir/themes/%theme_name/gnome-shell/
%_datadir/themes/%theme_name/plank/
%_datadir/themes/%theme_name-dark/gtk-3.0/
%_datadir/themes/%theme_name-dark/gnome-shell/
%_datadir/themes/%theme_name-dark/plank/

%files -n metacity-theme-greybird
%_datadir/themes/%theme_name/metacity-1/
%_datadir/themes/%theme_name-dark/metacity-1/

%files -n xfwm4-theme-greybird
%_datadir/themes/%theme_name/xfwm4/
%dir %_datadir/themes/%theme_name-accessibility/
%_datadir/themes/%theme_name-accessibility/xfwm4/
%_datadir/themes/%theme_name-dark/xfwm4/
%dir %_datadir/themes/%theme_name-dark-accessibility/
%_datadir/themes/%theme_name-dark-accessibility/xfwm4/
%dir %_datadir/themes/%theme_name-compact/
%_datadir/themes/%theme_name-compact/xfwm4/

%files -n xfce4-notifyd-theme-greybird
%_datadir/themes/%theme_name/xfce-notify-4.0/
%dir %_datadir/themes/%theme_name-bright/
%_datadir/themes/%theme_name-bright/xfce-notify-4.0/

%exclude %_datadir/themes/%theme_name/Greybird.emerald
%exclude %_datadir/themes/%theme_name/unity
%exclude %_datadir/themes/%theme_name-dark/Greybird-dark.emerald
%exclude %_datadir/themes/%theme_name-dark/unity

%changelog
* Tue Jan 26 2021 Mikhail Efremov <sem@altlinux.org> 3.22.14-alt1
- Reduce messagedialog buttonbox size (by Simon Steinbeiss)
- Make CSD titlebars slimmer (by Maurizio Galli)
- Improve dark xfwm4 tabwin contrast (by Simon Steinbeiss)
- Improve contrast of dark entry (Fixes #263) (by Simon Steinbeiss)
- More normal-sized inline-toolbar buttons (by Simon Steinbeiss)
- Add workaround for Gnome Builder (Fixes #264) (by Simon Steinbeiss)
- Fix progressbar in unfocused windows (Fixes #284) (by Simon Steinbeiss)
- Rebase parts of the %linked code (Fixes #265) (by Simon Steinbeiss)
- Own /usr/share/themes/Greybird-dark directory
- Fix Thunar CSD when not focused (Fixes #274) (by Simon Steinbeiss)
- Fix GTK3 dark colors (by Nico Kaiser)

* Mon Oct 19 2020 Mikhail Efremov <sem@altlinux.org> 3.22.12-alt1
- 3.22.12.

* Wed Mar 18 2020 Mikhail Efremov <sem@altlinux.org> 3.22.11-alt1
- Add Vcs tag.
- 3.22.11.

* Thu Feb 14 2019 Mikhail Efremov <sem@altlinux.org> 3.22.10-alt1
- 3.22.10.

* Fri Nov 30 2018 Mikhail Efremov <sem@altlinux.org> 3.22.9-alt1.gitc60f47498d4c4
- Upstream git snapshot.

* Tue Aug 28 2018 Mikhail Efremov <sem@altlinux.org> 3.22.8-alt1.gitf8d1adb05e4da
- Initial build (based on Fedora spec).
