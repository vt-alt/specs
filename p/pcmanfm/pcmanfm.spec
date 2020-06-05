%define gtkver 2

Name: pcmanfm
Version: 1.3.1
Release: alt3

Summary: PCMan File Manager
License: GPL-2.0-or-later
Group: Graphical desktop/Other

Url: http://pcmanfm.sourceforge.net
Source: %name-%version.tar
Patch0: 0001-Avoid-undefined-isdigit-behaviour.patch
Patch1: 0003-main-set-the-GIOChannel-encoding-to-binary.patch 

Provides: pcmanfm2 = %version-%release
Obsoletes: pcmanfm2 < 1.2.0

BuildRequires: rpm-build-xdg
BuildRequires: libgtk+%gtkver-devel >= 2.18.0
BuildRequires: libfm-devel >= 1.2.0
BuildRequires: libgio-devel

BuildRequires: libdbus-glib-devel libstartup-notification-devel libgamin-devel intltool libmenu-cache-devel menu-cache

# See bug 34867
Requires: menu-cache lxde-freedesktop-menu

%description
Features:
    * Extremly fast and lightweight
    * Can be started in under a second on reasonable hardware
    * Tabbed browsing (similar to Firefox)
    * Drag&Drop support
    * Files can be dragged among tabs
    * Loads large directories in reasonable time
    * File association support (default applications)
    * Basic thumbnail support
    * Bookmarks support
    * Handles non-UTF-8 encoded filenames correctly
    * Provides icon view and detailed list view
    * Standards compliant (follows freedesktop.org)
    * Clean and user-friendly interface (GTK+%gtkver)

%package devel
Summary: Development files for %name
Group: Development/Other
Buildarch: noarch

%description devel
This package contains header files.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure \
    --enable-largefile \
    --with-gtk=%gtkver
%make_build

%install
%makeinstall_std
%find_lang %name
ln -s %name %buildroot%_bindir/pcmanfm2

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/%name
%_xdgconfigdir/%name
%_man1dir/*

%files devel
%_includedir/*

%changelog
* Fri May 22 2020 Anton Midyukov <antohami@altlinux.org> 1.3.1-alt3
- Fix system reboot delayed for 90 seconds with systemd (Closes: 38280)

* Thu Mar 26 2020 Anton Midyukov <antohami@altlinux.org> 1.3.1-alt2
- Added upstream patch for fix undefined 'isdigit()' behaviour
- Fixed license tag

* Fri Jan 04 2019 Anton Midyukov <antohami@altlinux.org> 1.3.1-alt1
- new version 1.3.1

* Sun Apr 29 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt2
- Added missing requires: menu-cache, lxde-freedesktop-menu (Closes: 34867)

* Tue Apr 24 2018 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Tue Dec 13 2016 Anton Midyukov <antohami@altlinux.org> 1.2.5-alt1
- new version 1.2.5

* Tue Oct 04 2016 Michael Shigorin <mike@altlinux.org> 1.2.4-alt1
- 1.2.4

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 1.2.2-alt1
- 1.2.2

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1
- 1.2.0
- renamed back to pcmanfm according to upstream git

* Fri Aug 16 2013 Mykola Grechukh <gns@altlinux.ru> 1.1.2-alt1
- new version (1.1.2)

* Tue Nov 06 2012 Radik Usupov <radik@altlinux.org> 1.1.0-alt1
- new version (1.1.0)

* Wed Oct 31 2012 Radik Usupov <radik@altlinux.org> 1.0.2-alt1
- new version (1.0.2)

* Wed Oct 10 2012 Andriy Grytsenko <andrej@rep.kiev.ua> 1.0.2
- New upstream RC version 1.0.2~alpha1.
- Removed all patches - upstream has changed everything since 0.9.x series.

* Wed Feb 22 2012 Radik Usupov <radik@altlinux.org> 0.9.10-alt2
- Revert "Apply patch #3438582 to fix bug #3325415 - window resize problem." (Closes: 26981)

* Tue Jan 31 2012 Radik Usupov <radik@altlinux.org> 0.9.10-alt1
- new version (0.9.10)

* Wed Aug 31 2011 Radik Usupov <radik@altlinux.org> 0.9.9-alt10
- new upstream snapshot

* Mon Aug 15 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt9
- fixed starting without arguments when daemon running

* Sun Jul 31 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt8
- quick/dirty fix for bug: daemon window lost when unmounting volume
at last (or single) tab

* Thu Jul 14 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt7
- new upstream snapshot

* Wed Jul 06 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt6
- new snapshot

* Tue May 31 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt5
- new snapshot
- fixed bug with closing daemon's last window

* Tue Apr 26 2011 Mykola Grechukh <gns@altlinux.ru> 0.9.9-alt3
- new snapshot

* Fri Apr 15 2011 Radik Usupov <radik@altlinux.org> 0.9.9-alt2
- Added requires (Closes: 25204)

* Tue Mar 01 2011 Timur Aitov <timonbl4@altlinux.org> 0.9.9-alt1
- new snapshot

* Wed Dec 08 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt6
- deselect files when clicking with right button too

* Mon Oct 25 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt5
- new snapshot

* Thu Sep 23 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt4
- new snapshot

* Wed Jul 21 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt3
- new git snapshot from upstream

* Fri Jun 11 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt2
- thanks to Alexey Borisenkov fixed #23445

* Sun May 30 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.7-alt1
- new version

* Tue May 04 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.5-alt1
- new upstream version (closes: #23425)

* Mon Apr 26 2010 Mykola Grechukh <gns@altlinux.ru> 0.9.4-alt1
- new version

* Fri Mar 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.9.3-alt1
- new version based on libfm. Package name changed to pcmanfm2
