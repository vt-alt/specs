%define ver_major 3.32

Name: gnome3
Version: %ver_major.1
Release: alt1

Summary: GNOME 3 Desktop installers
License: %gpl3plus
Group: Graphical desktop/GNOME

BuildArch: noarch

BuildPreReq: rpm-build-licenses

# The following are required versions of those packages that
# do not follow GNOME version numbers.
## Core components
%define session_ver %ver_major
%define keyring_ver 3.31.91

## Applications
%define nautilus_ver %ver_major
%define seahorse_ver %ver_major
%define utils_ver 3.20
%define games_ver 3.28.0
%define weather_ver 3.26
%define pm_ver 3.26
%define yelp_ver %ver_major
%define dconf_editor_ver 3.31.91
%define contacts_ver 3.31.90
%define roller_ver %ver_major
%define eog_ver 3.28.4
%define network_manager_ver 1.8
%define terminal_ver %ver_major
%define epiphany_ver %ver_major
%define pidgin_ver 2.6.3
%define evince_ver 3.31.91
%define applets_ver %ver_major
%define gedit_ver %ver_major
%define gedit_plugins_ver %ver_major
%define gud_ver %ver_major
%define gdm_ver 3.31.91
%define gdu_ver %ver_major
%define evo_ver %ver_major
%define emp_ver 3.12.11
%define brasero_ver 3.12.2
%define accerciser_ver 3.22
%define recorder_ver 3.28.0
%define todo_ver 3.28.1
%define characters_ver 3.30.0
%define music_ver %ver_major
%define photos_ver 3.31.91
## Engines, themes
%define engines_ver %ver_major
%define icon_theme_ver %ver_major
%define themes_ver 3.28
%define gtk_theme_prefix gtk3-theme
%define gnome_theme_prefix gnome-theme
## a11y
%define orca_ver %ver_major

%description
A set of virtual packages for GNOME Desktop version 3 installation.

%package minimal
Summary: GNOME 3 Desktop minimal installer
Group: Graphical desktop/GNOME
Obsoletes: gnome-sisyphus-minimal
Provides: gnome-sisyphus-minimal = %version-%release
Obsoletes: gnome-minimal
Provides: gnome-minimal = %version-%release

# GNOME Desktop Core
Requires: gnome-session >= %session_ver
#Requires: gnome-panel >= %ver_major
Requires: pulseaudio-daemon
Requires: gnome-control-center >= %ver_major
Requires: xorg-drv-libinput
Requires: gnome-shell >= %ver_major
Requires: gnome-shell-extensions >= %ver_major
# user settings utility
Requires: gnome-tweaks >= %ver_major
Requires: dconf-editor >= %dconf_editor_ver

# default font
Requires: fonts-otf-abattis-cantarell
# backgrounds
Requires: gnome-backgrounds

# Help browser
Requires: yelp >= %yelp_ver
#Requires: gnome-menus >= %ver_major

# GNOME Utilities
Requires: gnome-system-monitor >= %ver_major
Requires: gnome-logs >= %ver_major
Requires: gucharmap >= %ver_major
Requires: gnome-calculator >= %ver_major
Requires: gnome-calendar >= %ver_major
#Requires: gnome-todo >= %todo_ver
Requires: gnome-characters >= %characters_ver

# Applications
## Default file manager
Requires: nautilus >= %nautilus_ver
## Default terminal emulator
Requires: gnome-terminal >= %terminal_ver
## Default archiving tool
Requires: file-roller >= %roller_ver
## Default text editor
Requires: gedit >= %gedit_ver

# Look & Feel
## Default themes
Requires: gnome-icon-theme >= 3.12
Requires: gnome-icon-theme-symbolic >= 3.12
Requires: gnome-themes-extra >= %themes_ver
#Requires: libgtk3-engine-adwaita
Requires: libgtk2-engine-adwaita

# And, of course, the documentation
Requires: gnome-user-docs >= %ver_major
Requires: gnome-getting-started-docs

%description minimal
This virtual package installs GNOME Desktop with minimum components. It
installs only a few applets, necessary utilities and a minimal set of themes.
Doesn't install games and media programs.

## =========================================================================

%package default
Summary: GNOME 3 Desktop installer for optimal user's requirements
Group: Graphical desktop/GNOME
Obsoletes: gnome-sisyphus-default
Provides: gnome-sisyphus-default = %version-%release
Obsoletes: gnome-default
Provides: gnome-default = %version-%release

Requires: %name-minimal = %version-%release

# initial setup
Requires: gnome-initial-setup

## Canberra modules for both GTK+
Requires: libcanberra-gtk2
Requires: libcanberra-gtk3
## Color manager
Requires: gnome-color-manager
## Password keeper
Requires: gnome-keyring >= %keyring_ver
Requires: gnome-keyring-ssh >= %keyring_ver
# Encryption keys management
Requires: seahorse >= %seahorse_ver
Requires: pinentry-gnome3
## All gvfs-backends
Requires: gvfs-backends
Requires: fuse-gvfs
# see ALT #31129
Requires: xdg-utils
Requires: gnome-disk-utility >= %gdu_ver
## Display manager
Requires: gdm-gnome >= %gdm_ver
## Default web-browser
Requires: epiphany >=  %epiphany_ver
#Requires: mozilla-plugin-adobe-flash
## Default mailer
Requires: evolution >= %evo_ver
## Default messenger
Requires: empathy >= %emp_ver
## IRC client
Requires: polari >= %ver_major
# Und contacts manager
Requires: gnome-contacts >= %contacts_ver

## Default document reader (currently pdf, ps, tiff, dvi)
Requires: evince >= %evince_ver
Requires: mozilla-plugin-evince
## and E-Book Reader
#Requires: fbreader
## and videos from a webcam
Requires: cheese >= %ver_major
# Note editor
Requires: bijiben >= %ver_major

# Utilities
Requires: gnome-utils >= %utils_ver

## Let's have nice notifications
Requires: notification-daemon

# Applications
## Plugins for gedit
Requires: gedit-plugins >= %gedit_plugins_ver
## Stock multimedia applications
Requires: gnome-sound-recorder >= %recorder_ver
## Default music player
Requires: gnome-music >= %music_ver
## Extneded music player
Requires: rhythmbox
## All Rhythmbox plugins
Requires: rhythmbox-plugins
## Default media player
Requires: totem
# and plugins
Requires: totem-plugins
## Stock GNOME games
Requires: gnome-games-full >= %games_ver
## Default photo viewer
Requires: gnome-photos >= %photos_ver
## Default image viewer
Requires: eog >= %eog_ver
Requires: eog-plugins
## Default CD/DVD burning interface
Requires: brasero >= %brasero_ver
## Clipboard manager
Requires: gnome-shell-extension-gpaste
# Documents manager
Requires: gnome-documents
Requires: gnome-books
# A quick previewer for Nautilus
Requires: sushi
# mypaint, krita thumbnailer for Nautilus
Requires: gnome-kra-ora-thumbnailer
#  Epub thumbnailer for Nautilus
Requires: gnome-epub-thumbnailer
# Nautilus extension for terminal
Requires: gnome-terminal-nautilus
# Menu editor
#Requires: alacarte
# Weather application
Requires: gnome-weather >= %weather_ver
# Clock application
Requires: gnome-clocks >= %ver_major
# Maps application
Requires: gnome-maps >= %ver_major
# power consumption statistic
Requires: gnome-power-manager >= %pm_ver
Requires: NetworkManager-gnome >= %network_manager_ver
## Bluetooth pairing and control program
Requires: gnome-bluetooth
## VNC server for the GNOME Desktop
Requires: vino
## VNC client for the GNOME Desktop
Requires: vinagre

Requires: gnome-user-share
Requires: rygel
Requires: rygel-tracker
Requires: gnome-usage
Requires: gnome-software >= %ver_major

# flatpak
Requires: xdg-desktop-portal-gtk

%description default
This virtual package installs GNOME Desktop for an average user's
requirements. It installs components from gnome-minimal package, some
games, media programs such as mixer, audio and video players, additional
themes, and some other programs that comprise GNOME Desktop.
## =========================================================================

%package default-ru
Summary: GNOME 3 Desktop installer for optimal user's requirements, russian part
Group: Graphical desktop/GNOME
## spell checking dictionary
Requires: hunspell-ru

%description default-ru
This virtual package installs spell checking dictionary for russian language

## =========================================================================

%package full
Summary: GNOME 3 Desktop full installer
Group: Graphical desktop/GNOME
Requires: %name-default = %version-%release

# Sound & graphics & video
## CD-ripper
Requires: goobox
## Image viewer, browser and simple editor
Requires: gthumb
## Non-linear DV editor
Requires: kino
#Requires: dvgrab
## SANE (Scanner Access Now Easy) frontend
Requires: xsane
## Utilities
## Internet telephon
Requires: ekiga
## Client for ed2k network
Requires: aMule
## BitTorrent client
Requires:  transmission-gtk
# Windows (TM) communications
## RDP
Requires: freerdp
## NX
Requires: freenx
# Requires: nxlaunch
# Disks management
Requires: gparted
Requires: consolehelper

%description full
This virtual package installs full GNOME Desktop except components from
gnome-mobile and gnome-a11y packages.

## =========================================================================
%package office
Summary: GNOME 3 Desktop applications for real office users
Group: Graphical desktop/GNOME

## OpenOffice.org and GNOME extensions for it
### Some openoffice.org-langpack-* packages need to be added to distribution profiles
Requires: openoffice.org-gnome
## Diagram creation program
Requires: dia
## International dictionary (synchronize this section in -office package)
# GUI
Requires: stardict-gnome
# Some language independent StarDict dictionaries
Requires: stardict-engcom

%description office
This virtual package installs OpenOffice.org office suite with GNOME extensions and
some applicatios necessary for every office user.

## =========================================================================

%package office-ru
Summary: russian stardict dictionaries for gnome-office(-light) packages
Group: Graphical desktop/GNOME
Requires: stardict-mueller7
Requires: stardict-slovnyk_en-ru
Requires: stardict-slovnyk_ru-en

%description office-ru
This virtual package installs stardict dictionaries for russian language

## =========================================================================
%package office-light
Summary: GNOME 3 Desktop applications for real office users (light version)
Group: Graphical desktop/GNOME

## Word processor
Requires: abiword-3.0
## Spreadsheet program
Requires: gnumeric
## Vector Drawing Application
Requires: inkscape
## Diagram creation program
Requires: dia
## GIMP
Requires: gimp
## International dictionary (synchronize this section in -office package)
# GUI
#Requires: stardict-gnome
# Some StarDict dictionaries
#Requires: stardict-engcom

## Presentation tool ???

%description office-light
This virtual package installs applications necessary for every office
users such as word processor (Abiword), spreadsheet editor (Gnumeric) and
some other usefull programs

## =========================================================================
%package a11y
Summary: GNOME 3 Desktop accessibility applications
Group: Graphical desktop/GNOME
# A synonym
Provides: sisyphus-accessibility
Obsoletes: %name-sisyphus-accessibility
Provides: %name-sisyphus-accessibility = %version-%release
Requires: %name-default = %version-%release

Requires: orca >= %orca_ver
Requires: accerciser >= %accerciser_ver

%description a11y
This virtual package installs GNOME Desktop accessibility applications.
These include orca screen reader and accerciser - interactive tool for
querying accessibility information.

##==========================================================================
%package regular
Summary: Virtual package for use with regular(TM) GNOME 3 distro
Group: Graphical desktop/GNOME
Requires: %name-default = %version-%release
Requires: %name-office-light = %version-%release
Requires: %name-a11y = %version-%release
# And
## CD-ripper
Requires: goobox
## Image viewer, browser and simple editor
Requires: gthumb
## scanner apps
Requires: sane
Requires: simple-scan
## Utilities
## BitTorrent client
Requires: transmission-gtk
# Disks management
Requires: gparted
## Default RSS-reader
Requires: liferea
## Video editor
#Requires: pitivi
# Other
Requires: gnome-battery-bench
Requires: gnome-multi-writer
# Additional LibreOffice packages
# (sushi requires LibreOffice-integrated, gnome-documents requires libreofficekit)
Requires: LibreOffice
Requires: LibreOffice-gnome
Requires: LibreOffice-langpack-ru

%description regular
This virtual package includes default GNOME 3 Desktop components and
some other useful GNOME and GTK applications.

%files minimal
%files default
#%files default-ru
#%files full
#%files office
#%files office-ru
%files office-light
%files a11y
%files regular

%changelog
* Sat Jun 22 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- default: removed alacarte, added gnome-keyring-ssh

* Wed Feb 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- default: added gnome-books; removed gnome-nettool (obsolete),
  totem-nautilus (removed by upstream), gnome-todo (not ready for eds-3.32)
- regular: removed pitivi

* Thu Nov 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- added gnome-software

* Tue Jun 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt3
- default: added xdg-desktop-portal-gtk (flatpak + xdg-desktop-portal)

* Fri May 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- replaced gnome-games by new gnome-games-full virtual package

* Tue May 15 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- regular: added LibreOffice-{gnome,langpack-ru} see ALT#34909

* Fri Mar 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt2
- gnome-tweak-tool -> gnome-tweaks
- gnome-themes-standard -> gnome-themes-extra

* Mon Mar 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0
- added gnome-usage to -default

* Tue Feb 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0
- dropped gvfs-utils deprecated by gvfs >= 1.31
- moved dconf-editor to -minimal

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- added xorg-drv-libinput to -minimal
- added pinentry-gnome3, gnome-todo to -default

* Thu Jul 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt2
- added xdg-utils, gvfs-utils to -default (https://bugzilla.altlinux.org/show_bug.cgi?id=31129)

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- added gnome-calendar, gnome-characters to -default

* Wed Jan 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt3
- new -regular subpackage (-default+-office-light+-a11y+some other)

* Thu Dec 18 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- added gnome-user-share, rygel{,-tracker} {rhythmbox,totem}-plugins to -default
- replaced parcellite by gnome-shell-extension-gpaste

* Tue Sep 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- added vino, vinagre, gnome-terminal-nautilus, gnome-initial-setup to -default
- removed gnome-search-tool, gconf-editor

* Wed Sep 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt2
- added lost gnome-backgrounds to minimal
- updated gedit* versions

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0
- replaced gnome-system-monitor by gnome-logs
- removed gnome-media, added gnome-sound-recorder

* Thu Jan 09 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt2
- added libcanberra-gtk{2,3}, totem-nautilus and epub, kra/ora
  thumbnailers for Nautilus to -default

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- removed gnome-screensaver
- added gnome-music, gnome-maps, gnome-photos to -default

* Thu Apr 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- Obsoletes/Provides gnome-default

* Thu Mar 21 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.1-alt2
- added pulseaudio-daemon to -minimal, gnome-shell-extensions,
  gnome-weather to -default

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.1-alt1
- removed obsolete epiphany-extensions
- removed gnome-panel, gnome-applets, metacity-gnome - no more gnome-fallback session
- gcalctool replaced by gnome-calculator
- cheese moved from -full to -default
- rhythmbox, gnome-documents, alacarte added to -default
- added gnome-initial-setup, gnome-getting-started-docs to -minimal

* Sun Jan 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- a time to add fonts-otf-abattis-cantarell

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt2
- restored gnome-games, epiphany-extensions
- added libgtk2-engine-adwaita to -default

* Fri Oct 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- added gnome-contacts in -default
- temporarily removed buggy epiphany-extensions
- temporarily relaxed gnome-games required version

* Thu Oct 13 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- added gnome-color-manager, sushi in -default

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt3
- removed seahorse-agent

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- removed gnome-menus, alacarte

* Sun Apr 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for people/gnome
