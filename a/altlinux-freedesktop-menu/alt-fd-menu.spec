%def_with matelike
%def_without gnome2
%def_without kde3
%define gnome3ver 3.90

Name: altlinux-freedesktop-menu
Version: 0.67
Release: alt1

Summary: Implementation of the freedesktop.org menu specification
License: BSD or GPL
Group: Graphical desktop/Other

URL: http://altlinux.org/
Source: %name-%version.tar
Packager: Igor Vlasenko <viy@altlinux.org>
BuildArch: noarch

#BuildPreReq: rpm-build-xdg
BuildRequires: intltool glib2-devel

%if_with matelike
BuildRequires: mate-menus
%endif

%description
altlinux freedesktop.org menu

%package common
Summary: common files for altlinux freedesktop menus
Group: Graphical desktop/Other
Requires(pre): %name-icon-theme
Requires: %name-icon-theme
Requires: wm-common-freedesktop
#Conflicts: altlinux-menus < 0.5.2

%description common
%summary

%package nested-menu
Summary: altlinux freedesktop menu with shallow layout
Group: Graphical desktop/Other
Requires(pre): %name-common
Requires: %name-common
Provides: %name-provider

%description nested-menu
freedesktop.org compliant altlinux menu with nested layout

%package shallow-menu
Summary: altlinux freedesktop menu with shallow layout
Group: Graphical desktop/Other
Requires(pre): %name-common
Requires: %name-common
Provides: %name-provider
Provides: %name-gnomish-menu

%description shallow-menu
freedesktop.org compliant altlinux menu with shallow layout

%if_with matelike
%package mate-like-menu
Summary: altlinux freedesktop menu with  look and feel of Mate DE
Group: Graphical desktop/Other
Requires(pre): %name-common
Requires: %name-common
Provides: %name-provider

%description mate-like-menu
freedesktop.org compliant altlinux menu with look and feel of Mate DE
%endif

%package xfce
Summary: xfce freedesktop menu
Group: Graphical desktop/XFce
Provides: xfce-freedesktop-menu
Conflicts: libgarcon-freedesktop-menu
Obsoletes: libgarcon-freedesktop-menu
Requires: %name-provider

%description xfce
ALTLinux freedesktop.org menu for XFCE

%package enlightenment
Summary: Enlightenment freedesktop menu
Group: Graphical desktop/Other
Provides: enlightenment-freedesktop-menu
Requires(pre): %name-provider
Requires: %name-provider

%description enlightenment
ALTLinux freedesktop.org menu for Enlightenment DE

%package lxde
Summary: lxde freedesktop menu
Group: Graphical desktop/Other
Provides: lxde-freedesktop-menu
Conflicts: lxde-lxmenu-data
Obsoletes: lxde-lxmenu-data < 0.2
# specifics of lxde menu migration
Requires(pre): %name-provider
Requires: %name-provider

%description lxde
ALTLinux freedesktop.org menu for LXDE

%package mate
Summary: mate freedesktop menu
Group: Graphical desktop/Other
Provides: mate-freedesktop-menu
Conflicts: mate-menus-default
#Requires: mate-menus-resources
Requires: %name-provider

%description mate
ALTLinux freedesktop.org menu for MATE

%package gnome3
Summary: gnome3 freedesktop menu
Group: Graphical desktop/GNOME
Provides: gnome3-freedesktop-menu
Conflicts: gnome-menus-default
Provides: gnome-menus = %gnome3ver.%version
Obsoletes: gnome-menus-default < %gnome3ver.%version
Requires: %name-provider
#Provides: %name-gnome = %version
Conflicts: %name-gnome < %version
Obsoletes: %name-gnome < %version
Conflicts: libgnome-menus <= 3.8.0-alt1

%description gnome3
ALTLinux freedesktop.org menu for GNOME3

%package cinnamon
Summary: cinnamon freedesktop menu
Group: Graphical desktop/GNOME
Provides: cinnamon-freedesktop-menu
Conflicts: cinnamon <= 1.6.7-alt2
Requires: %name-provider

%description cinnamon
ALTLinux freedesktop.org menu for Cinnamon

%package kde3
Summary: kde3 freedesktop menu
Group: Graphical desktop/KDE
Provides: kde3-freedesktop-menu
Conflicts: kde3-menu-original
Obsoletes: kde3-menu-original
Requires(pre): %name-provider
Requires: %name-provider
Requires: kde3-menu-common
Conflicts: kdelibs <= 3.5.12-alt8

%description kde3
ALTLinux freedesktop.org menu for KDE3

%package kde4
Summary: kde4 freedesktop menu
Group: Graphical desktop/KDE
Provides: kde4-freedesktop-menu = %version
Conflicts: kde4-menu-original
Obsoletes: kde4-menu-original
Requires(pre): %name-provider
Requires: %name-provider
Requires(pre): %name-generic
Requires: %name-generic
#Requires: kde4-menu-common
Conflicts: altlinux-menus
Conflicts: kde4libs <= 4.6.2-alt6
Conflicts: kde4base-runtime-core <= 4.6.2-alt1

%description kde4
ALTLinux freedesktop.org menu for KDE4

%package generic
Summary: generic freedesktop menu
Group: Graphical desktop/Other
Provides: generic-freedesktop-menu
Requires(pre): %name-provider
Requires: %name-provider
Conflicts: altlinux-menus
Conflicts: kde4libs <= 4.6.2-alt6
Conflicts: kde4base-runtime-core <= 4.6.2-alt1

%description generic
ALTLinux freedesktop.org menu for a generic freedesktop-compliant DE

%prep
%setup

if ! [ -d po ]; then
	echo "Use ./mkdist.sh instead of gear!!!"
	exit 1
fi

%build
touch AUTHORS ChangeLog NEWS README
intltoolize
%autoreconf 
%configure 
%make_build

%check
cat > ignore.list <<EOF
altlinux-audiovideo-audiovideoediting.directory
altlinux-audiovideo-midi.directory
altlinux-audiovideo-player.directory
altlinux-audiovideo-recorder.directory
altlinux-audiovideo-tuner.directory
altlinux-audiovideo-tv.directory
altlinux-education-construction.directory
altlinux-education-medicalsoftware.directory
altlinux-enlightenment.directory
altlinux-game-roleplaying.directory
altlinux-graphics-rastergraphics.directory
altlinux-java.directory
altlinux-lxde.directory
altlinux-mate.directory
altlinux-network-instantmessaging.directory
altlinux-network-p2p.directory
altlinux-network-telephony.directory
altlinux-network-videoconference.directory
altlinux-office-flowchart.directory
altlinux-science-medicalsoftware.directory
altlinux-settings-java.directory
altlinux-settings-lxde.directory
altlinux-settings-mate.directory
altlinux-settings-xfce.directory
altlinux-xfce.directory
EOF

ok=1
for i in desktop-directories/*.directory; do
    j=`basename $i`
    if ! grep $j ignore.list >/dev/null && ! grep 'Name\[ru\]=' $i >/dev/null; then
    	echo
        echo "$j is not translated - please, update po files"
	echo
	ok=0
    fi
done
rm ignore.list
[ $ok -gt 0 ] || exit 1

%install
%makeinstall_std
install -Dm755 altlinux-freedesktop-menu-post.sh %buildroot%_sbindir/altlinux-freedesktop-menu-post
install -Dm755 altlinux-freedesktop-menu.filetrigger %buildroot%_rpmlibdir/altlinux-freedesktop-menu.filetrigger

ln -s gnome3-applications.menu %buildroot%_sysconfdir/xdg/menus/gnome-applications.menu

mkdir -p %buildroot%_sysconfdir/xdg/menus/{,enlightenment-,gnome-,gnome3-,cinnamon-,kde3-,lxde-,mate-,xfce-}applications-merged
mkdir -p %buildroot%_sysconfdir/xdg/menus/{,mate-,}settings-merged

install -D -m644 layout/kde4-merged.menu %buildroot%_sysconfdir/kde4/xdg/menus/applications-merged/50-kde4-merged.menu

install -m0644 altlinux-directories/*.directory %buildroot/%_datadir/desktop-directories/

%if_with matelike
install -m0644 %_datadir/mate/desktop-directories/*.directory %buildroot/%_datadir/desktop-directories/
%endif

# alternatives
mkdir -p %buildroot%_altdir
cat <<EOF >>%buildroot%_altdir/%name-nested-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-nested.menu	1000
EOF
%if_with matelike
cat <<EOF >>%buildroot%_altdir/%name-mate-like-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-mate-like.menu	200
EOF
%endif
cat <<EOF >>%buildroot%_altdir/%name-shallow-menu
%_sysconfdir/xdg/menus/altlinux-applications.menu	%_sysconfdir/xdg/menus/altlinux-applications-shallow.menu	100
EOF

#find_lang %name

%post lxde
# hack around lxde
touch /etc/xdg/menus/lxde-applications.menu

#files 
#-f %name.lang
#doc AUTHORS ChangeLog NEWS README

%files common
%dir %_sysconfdir/xdg/menus/applications-merged
%_datadir/desktop-directories/altlinux-*.directory
#config (noreplace) is too dangerous for unexpirienced user
%config %_sysconfdir/xdg/menus/altlinux-*.menu
%_sbindir/altlinux-freedesktop-menu-post

%files nested-menu
%_altdir/%name-nested-menu

%files shallow-menu
%_altdir/%name-shallow-menu

%if_with matelike
%files mate-like-menu
%_altdir/%name-mate-like-menu
%_datadir/desktop-directories/mate-*.directory
%endif

%files xfce
#config (noreplace) is too dangerous for unexpirienced user
%verify(not mtime) %config %_sysconfdir/xdg/menus/xfce-applications.menu
%dir %_sysconfdir/xdg/menus/xfce-applications-merged

%files lxde
#config (noreplace) is too dangerous for unexpirienced user
%verify(not mtime) %config %_sysconfdir/xdg/menus/lxde-applications.menu
%dir %_sysconfdir/xdg/menus/lxde-applications-merged

%files gnome3
%verify(not mtime) %config %_sysconfdir/xdg/menus/gnome3-applications.menu
%_sysconfdir/xdg/menus/gnome-applications.menu
%dir %_sysconfdir/xdg/menus/gnome-applications-merged
%dir %_sysconfdir/xdg/menus/gnome3-applications-merged

%files cinnamon
%verify(not mtime) %config %_sysconfdir/xdg/menus/cinnamon-applications.menu
%dir %_sysconfdir/xdg/menus/cinnamon-applications-merged

%files mate
%verify(not mtime) %config %_sysconfdir/xdg/menus/mate-applications.menu
%dir %_sysconfdir/xdg/menus/mate-applications-merged
%verify(not mtime) %config %_sysconfdir/xdg/menus/mate-settings.menu
%dir %_sysconfdir/xdg/menus/mate-settings-merged

%if_with kde3
%files kde3
%verify(not mtime) %config %_sysconfdir/xdg/menus/kde3-applications.menu
%dir %_sysconfdir/xdg/menus/kde3-applications-merged
%else
%exclude %_sysconfdir/xdg/menus/kde3-applications.menu
%endif

%files generic
%verify(not mtime) %config %_sysconfdir/xdg/menus/applications.menu

%files enlightenment
%verify(not mtime) %config %_sysconfdir/xdg/menus/enlightenment.menu
# Enlightenment is too buggy to display a proper menu :(
#%config %_sysconfdir/xdg/menus/enlightenment-applications.menu
%exclude %_sysconfdir/xdg/menus/enlightenment-applications.menu
%dir %_sysconfdir/xdg/menus/enlightenment-applications-merged

%files kde4
%config %_sysconfdir/kde4/xdg/menus/applications-merged/50-kde4-merged.menu
%dir %_sysconfdir/kde4/xdg/menus/applications-merged
%_datadir/kde4/desktop-directories/altlinux-*.directory

%changelog
* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1
- added mate-like menu

* Sun Sep 16 2018 Anton Midyukov <antohami@altlinux.org> 0.66-alt1
- fix menu Settings for Cinnamon

* Thu Sep 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.65-alt3
- disabled kde3

* Mon Sep 11 2017 Michael Shigorin <mike@altlinux.org> 0.65-alt2
- introduced kde3 knob (on by default)

* Mon Jul 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- xfce menu cleanup (closes: #28575)

* Thu Apr 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- restored gnome3 symlinks

* Thu Apr 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- support for new categories in 1.1-draft standard:
  Adult,Feed,Maps,Humanities,Spirituality.
  closes: 28739

* Thu Apr 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- added Conflicts/Obsoletes on gnome2 menu in gnome3 menu
- removed gnome2 menu

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- added Kazakhstan translation by Baurzhan Muftakhidinov (baurthefirst@)

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- %_sbindir/altlinux-freedesktop-menu-post
- altlinux-freedesktop-menu.filetrigger
- closes: #28575

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- explicitly excluded Settings in mate-applications.menu
- closes: #28121

* Fri Nov 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- bugfixes in mate-applications.menu

* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- fixed Preferences in cinnamon freedesktop menu

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- added cinnamon freedesktop menu

* Mon Nov 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- updated enlightenment menu to be compatible with its bugs (closes: 27998)

* Tue Nov 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- support for X-Teaching

* Thu Nov 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- MATE settings submenu

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt0.M60P.1
- backport

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- merged directories from altlinux-menus

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- added menu for MATE (Gnome 2)

* Sun Apr 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- layout/xfce-applications.menu - removed xfhelp4 (#27276)
- note: from now on, backports for p6 should use 0.49 as base

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- added versioned provides for kde4-freedesktop-menu

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- bumped release to allow proper version in p6 branch

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- added tatarian translation

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- support for xfce4-run.desktop (closes: 26801)

* Sun Oct 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt0.M60P.1
- backport

* Sun Oct 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- explicitly load /usr/share/gdm desktop files in LXDE menu

* Sun Aug 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.44-alt0.M60P.1
- backport

* Sun Aug 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- killed comments (against KDE4 bugs)

* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt0.M60P.1
- backport

* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- added translation check

* Mon Jul 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.42-alt0.M60P.1
- backport

* Mon Jul 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- simplified Settings > KDE (#25875)

* Mon May 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- build without gnome2, to be included in gnome3 transaction

* Tue May 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- use native gnome2 resources instead of private copy

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- independent gnome3 menu; p6 compatible

* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- full conditional support for gnome 3; still p6 compatible

* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- aded Net > Blogs, Net > Security; stil p6 compatible

* Sun May 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- submenu adjustments; p6 compatible (use gnome2)

* Thu May 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- conditional support for gnome 3

* Thu May 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- removed references to private kde applications (PATH)

* Wed May 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- added private kde4 desktop-directories

* Tue May 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- removed mergeDir from kde4 menu

* Sat May 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- added more PreReq:'s to help smooth upgrade

* Thu May 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- merge sequence is set according to the menu policy draft

* Tue May 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- enabled KDE4 menu

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- Enlightenment freedesktop menu: does not support MergeDir yet

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- added Enlightenment freedesktop menu

* Mon May 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- added generic freedesktop menu (used by Enlightenment)

* Sun May 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- added KDE4 menu (disabled)

* Sat Apr 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- more pixmaps in layouts

* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- more pixmaps in layouts

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- nested menu: added Dev>Tools, misc layout improvements 

* Tue Apr 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- added KDE3 menu

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- nested menu: added documentation, preparations for KDE

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- added DE-private merge directories
- updated categories

* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- added shallow gnomish menu (thanks to shrek@)
  based on native GNOME desktop directories.

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- GNOME menu: temporarily removed Obsoletes: gnome-menus-default

* Tue Apr 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added GNOME menu

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- use System Tools for Gnome and System for the rest

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- use System Tools in shallow menu too (thanks to aris@)

* Fri Apr 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- use System Tools for applications-system (thanks to aris@)

* Thu Mar 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added shortcut .directory files

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- support for GNOME menu

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- Network menu internally uses Internet for RH/Gnome compatibility

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added native LXDE menu.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- optimizations for LXDE and XFCE settings; ShallowSettings.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- sisyphus release

* Fri Mar 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- shallow layout fixes (thanks to sem@)

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- shallow layout fixes (thanks to gns@)

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- Initial build
