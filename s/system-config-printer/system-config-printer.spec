Name:    system-config-printer
Version: 1.5.11
Release: alt7

Summary: A printer administration tool
Group:   System/Configuration/Printing
License: GPLv2+
Url:     http://cyberelk.net/tim/software/system-config-printer/
# Git:   https://github.com/zdohnal/system-config-printer

Source: %name-%version.tar
Patch:  %name-%version-%release.patch
Patch1: fix_search_printer.patch
Patch2: about_logo.patch
Patch3: fix-translation-in-troubleshoot-menu.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-cups
BuildRequires: desktop-file-utils
BuildRequires: cups-devel
BuildRequires: libusb-devel
BuildRequires: libudev-devel
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: xmlto

Requires: %name-lib = %EVR

%add_python3_path /usr/share/system-config-printer


%description
system-config-printer is a graphical user interface that allows
the user to configure a CUPS print server.

%package lib
Summary: Libraries and share for printer tools
Group: System/Configuration/Printing
Requires: python3-module-cupshelpers = %version-%release
Requires: python3-module-cups >= 1.9.61-alt1

%description lib
Code used by both graphical and non-graphical parts

%package udev
Summary: Rules for udev for automatic configuration of USB printers
Group: System/Configuration/Printing
Requires: %name-lib = %version-%release

%description udev
The udev rules and helper programs for automatically configuring USB
printers.

%package -n python3-module-cupshelpers
Summary: Python module to configure a CUPS print server
Group: System/Configuration/Printing
BuildArch: noarch
Conflicts: python-module-cupshelpers

%description -n python3-module-cupshelpers
Python module to configure a CUPS print server

%prep
%setup -q
sed -i 's/mod.*ins.*_aft.*//' newprinter.py
%patch -p1
%patch1 -p0
%patch2 -p0
%patch3 -p1

%build
./bootstrap
%configure --with-udev-rules \
           --with-polkit-1

%install
%makeinstall_std udevrulesdir=/lib/udev/rules.d \
		 udevhelperdir=/lib/udev
install -Dm0644 tmpfiles.conf %buildroot%_tmpfilesdir/system-config-printer.conf
mv %buildroot%_datadir/{metainfo,appdata}
%find_lang system-config-printer

%post
/bin/rm -f /var/cache/foomatic/foomatic.pickle ||:
exit 0

%files lib
%_bindir/scp-dbus-service
%_datadir/dbus-1/interfaces/*.xml
%_datadir/dbus-1/services/*.service
%_datadir/%name
/etc/dbus-1/system.d/*.conf

%files udev
%_tmpfilesdir/*
/lib/udev/rules.d/*.rules
/lib/udev/udev-*-printer

%files -f system-config-printer.lang
%doc README.md COPYING
%_bindir/install-printerdriver
%_bindir/system-config-printer*
%_datadir/appdata/%name.appdata.xml
%_desktopdir/*.desktop
%_sysconfdir/xdg/autostart/*.desktop
%_man1dir/*

%files -n python3-module-cupshelpers
%config(noreplace) %_sysconfdir/cupshelpers/*.xml
%python3_sitelibdir_noarch/cupshelpers
%python3_sitelibdir_noarch/cupshelpers-*


%changelog
* Thu Jun 25 2020 Sergey V Turchin <zerg@altlinux.org> 1.5.11-alt7
- fix requires python-packagekit to work install-printerdriver (Closes: 38638)
- package bin/scp-dbus-service to -lib subpackage (Closes: 38639)

* Mon Jun 17 2019 Pavel Moseev <mars@altlinux.org> 1.5.11-alt6
- fix translation in troubleshoot menu

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.11-alt5.qa1
- NMU: applied repocop patch

* Mon Jul 02 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.5.11-alt5
- fix logo in 'About' (Closes #33002)

* Thu Jun 21 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.5.11-alt4
- fix same printer-list in search
- fix mix device-list

* Mon Jun 04 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.5.11-alt3
- Rebuild with new structure of packages.

* Tue May 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.11-alt2
- Complete localization into Russian (thanks Olesya Gerasimenko).

* Sat Apr 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.11-alt1
- New version (ALT #34774).

* Sun Jan 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt1
- new version
- complete Russian translations
- package AppStream file

* Mon Jan 09 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.5.6-alt1
- new version
- migration to python3

* Thu May 30 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.13-alt2
- /var/lib/run/... changed to /var/run and tmpfiles.d file added
  (closes #28362)

* Tue May 28 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.13-alt1
- 1.3.13

* Mon Apr 01 2013 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt2
- Complete Russian translation (ALT #28773)

* Mon Sep 10 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.11-alt1
- 1.3.11

* Thu Jul 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.9-alt1
- 1.3.9 (ALT #25875)
- fix '&mdash' in ru.po (ALT #26123)

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt1.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.7-alt1.1
- Rebuild with Python-2.7

* Wed Oct 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.7-alt1
- 1.3.7
- work with cups-1.5 fixed

* Mon Jul 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue May 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.2-alt3
- fix cupshelpers (ALT #25649) (ALT #25650)

* Tue Apr 12 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.2-alt2
- add alterator category (ALT #25420)

* Fri Apr 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3.2-alt1
- new version

* Wed Sep 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.4-alt1
- new version

* Thu Jun 10 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.17-alt2
- requires python-module-pygtk-libglade added

* Tue Jun 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.17-alt1
- New upstream version

* Wed Jan 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1.16-alt1
- build for Sisyphus

* Mon Jan 11 2010 Tim Waugh <twaugh@redhat.com> - 1.1.16-8
- Fixed traceback when copying printer with certain job options
  set (bug #554268).

* Mon Jan 11 2010 Tim Waugh <twaugh@redhat.com> - 1.1.16-7
- Fixed traceback introduced in recent fix (bug #554376).

* Thu Jan  7 2010 Tim Waugh <twaugh@redhat.com> - 1.1.16-6
- Fixed crash when using keyring for auth without password (bug #553141).

* Thu Jan  7 2010 Tim Waugh <twaugh@redhat.com> - 1.1.16-5
- Fixed typo introduced in recent fix (bug #551436).

* Wed Jan  6 2010 Tim Waugh <twaugh@redhat.com> - 1.1.16-4
- Use %%global instead of %%define.

* Wed Jan  6 2010 Tim Waugh <twaugh@redhat.com> - 1.1.16-3
- Fixed pycups IPPRequest attribute handling bug.
- Make sure there are enough ink level values (bug #541882).
- Make sure the printer we added still exists before selecting it
  (bug #551436).
- Set notification timeouts appropriately (bug #550829).
- Avoid traceback in NewPrinterGUI.init (bug #550442).
- Avoid traceback in on_jobviewer_exit (bug #550437).

* Wed Dec 23 2009 Tim Waugh <twaugh@redhat.com> - 1.1.16-2
- Prefer foomatic-recommended drivers (bug #550108).
- Pre-select correct driver when adding or changing a queue (bug #550075).
- Fixed typo (bug #550096).

* Tue Dec 22 2009 Tim Waugh <twaugh@redhat.com> - 1.1.16-1
- Updated pycups to 1.9.47.
- 1.1.16:
  - Ignore com.apple.print.recoverable state reason.
  - Prevent traceback in found_network_printer_callback (bug #547765).
  - Use asynchronous connection class for fetching device lists
    (bug #549749).
  - Prefer Foomatic/hpijs to hpcups for the time being.
  - Clear device screen each time a new dialog is presented.
  - Constraints handling fix.

* Fri Dec 18 2009 Jiri Popelka <jpopelka@redhat.com> 1.1.15-9
- Prevent traceback when no downloadable driver selected (#548449).

* Mon Dec 14 2009 Jiri Popelka <jpopelka@redhat.com> 1.1.15-8
- Prevent traceback when cancel button in troubleshooter pressed (#546821).

* Wed Dec  9 2009 Tim Waugh <twaugh@redhat.com> - 1.1.15-7
- Fixed jobviewer traceback with short-lived state reasons (bug #545733).

* Tue Dec  8 2009 Tim Waugh <twaugh@redhat.com> - 1.1.15-6
- Fixed traceback with short lpd device URIs (bug #545397).

* Mon Dec  7 2009 Tim Waugh <twaugh@redhat.com> - 1.1.15-5
- Fixed traceback when troubleshooter operation is cancelled (bug #544356).

* Thu Dec  3 2009 Tim Waugh <twaugh@redhat.com> - 1.1.15-3
- Fixed cupsd.conf parsing when lines begin with blanks (bug #544003).
- Don't overwrite BrowsePoll settings in basic settings dialog (bug #543986).

* Thu Dec  3 2009 Tim Waugh <twaugh@redhat.com> - 1.1.15-2
- Handle RuntimeError when localizing state reason (bug #543937).

* Mon Nov 30 2009 Tim Waugh <twaugh@redhat.com> 1.1.15-1
- 1.1.15:
  - Fixed traceback introduced by fix to bug #541882.

* Fri Nov 27 2009 Tim Waugh <twaugh@redhat.com> 1.1.14-1
- 1.1.14:
  - Retry when reconnection fails (bug #541741).
  - Prevent traceback with bad marker-levels attribute (bug #541882).

* Thu Nov 26 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-12
- Prevent display of marker levels from making the properties dialog
  too big (bug #540826).
- Place the window in the middle of the screen (bug #539876).
- Fixed editability of PPD options for explicit IPP queues
  (bug #541588).

* Mon Nov 23 2009 Jiri Popelka <jpopelka@redhat.com> 1.1.13-11
- Prevent traceback when PackageKit is not installed (bug #540230).

* Wed Nov 11 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-10
- Suggest installing foomatic-db-ppds when appropriate (bug #536831).

* Thu Nov  5 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-9
- Release bump.

* Thu Nov  5 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-8
- Fail gracefully if the new printer has disappeared before the user
  has responded to the test page prompt (bug #533109).

* Mon Nov  2 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-7
- Fixed typo in de.po (bug #532371).

* Fri Oct 30 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-6
- Avoid traceback in IPP notification handlers (bug #530641).
- Avoid epydoc dependency.

* Thu Oct 29 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-5
- Added upstream patch for custom state reasons (bug #531872).
- Strip 'zjs' from make-and-model as well (bug #531869).

* Wed Oct 28 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-4
- Troubleshoot: connect to the right server when choosing a network
  queue (bug #531482).
- Strip 'zxs' and 'pcl3' from make-and-model (bug #531048).
- Fixed visibility tracking for jobs window (bug #531438).
- Don't display properties dialog for first test page (bug #531490).
- Determine make/model for network printers (bug #524321).
- Auto-select the correct driver entry for raw queues.
- Avoid traceback in PhysicalDevice.py.
- Let Return key activate the Find button for Find Network Printer.

* Tue Sep 22 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-3
- Fixed missing import in probe_printer module.
- Fixed race when fetching device list (bug #521110).

* Fri Sep 18 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-2
- Iconify jobs window into status icon.
- Avoid showing the publish-printers dialog when not necessary.
- Fixed traceback when cancelling change-driver dialog.
- Fixed data button state.

* Mon Sep 14 2009 Tim Waugh <twaugh@redhat.com> 1.1.13-1
- 1.1.13:
  - Translation updates (bug #522451).

* Fri Sep  4 2009 Tim Waugh <twaugh@redhat.com> 1.1.12-8
- Further speed improvement when fetching devices.

* Thu Sep  3 2009 Tim Waugh <twaugh@redhat.com> 1.1.12-7
- Speed improvement when fetching devices.
- Allow raw devices to be changed.

* Fri Aug 28 2009 Tim Waugh <twaugh@redhat.com> 1.1.12-6
- Fixed PPD/IPP string translation.
- Fixed proxy authentication.

* Thu Aug 27 2009 Tim Waugh <twaugh@redhat.com> 1.1.12-4
- Ported to polkit-1.

* Wed Aug 26 2009 Tim Waugh <twaugh@redhat.com> 1.1.12-3
- Handle icon load failure gracefully.
- Fixed statereason icon names.

* Wed Aug 26 2009 Tim Waugh <twaugh@redhat.com> 1.1.12-2
- Fixed traceback in on_tvNPDeviceURIs_cursor_changed (bug #519367).

* Tue Aug 25 2009 Tim Waugh <twaugh@redhat.com> 1.1.12-1
- 1.1.12:
  - Troubleshooting fix.
  - Fixed applet traceback when printing test page.
  - Removed completed job notifications (trac #181).
  - Show printer status in printer icons (bug #518020).
  - Use paused icon when printer state reason is 'paused'.
  - Driver preference order fixes.
  - Job status icon and state reason display in jobs list
    (bug #518070).
  - Fixed overactive job creation times update timer.
  - Use preferred D-Bus object path for AuthenticationAgent
    (bug #518427).
  - Fixed disabling a printer when PolicyKit call fails.
  - Set appropriate status icon tooltip when configuration printer
    (bug #518007).
  - Use separate thread for verifying IPP queue (bug #518065).
  - Use newer tooltip API to avoid deprecation warnings.
  - Compare MFG/MDL case-insensitively in udev rule.
  - Support for cups-pk-helper's DevicesGet method.
  - Don't attempt to use PolicyKit if running as root.
  - Support for localized marker names (trac #183).
  - Other small fixes.

* Thu Aug 20 2009 Tim Waugh <twaugh@redhat.com> 1.1.11-6
- Applied patch from 1.1.x (52a73b6).
  - Better printer icons representing status (bug #518020).
  - Use paused ico nwhen printer state reason is 'paused'.
  - Job status icon and state reason in jobs treeview (bug #518070).
  - Job creation times display fixes.
  - Use preferred object path for AuthenticationAgent (bug #518427).

* Wed Aug 19 2009 Tim Waugh <twaugh@redhat.com> 1.1.11-5
- Applied patch from 1.1.x (3f45e96):
  - Show a 'paused' emblem for rejecting/disabled printers
    (bug #518020).
  - Set appropriate tooltip when configuring printer (bug #518007).
  - Use separate thread for verifying IPP queue (part of bug #518065).
  - Better driver preference order (bug #518045).

* Fri Aug 14 2009 Tim Waugh <twaugh@redhat.com> 1.1.11-4
- Compare MFG and MDL fields case insensitively when adding automatic
  queues, because HPLIP provides them with different case than the
  actual devices do.  Upstream HPLIP bug:
  https://bugs.launchpad.net/hplip/+bug/405804

* Fri Aug 14 2009 Tim Waugh <twaugh@redhat.com> 1.1.11-3
- Own /var/run/udev-configure-printer.

* Thu Aug 13 2009 Tim Waugh <twaugh@redhat.com> 1.1.11-2
- Updated cupspk DevicesGet call for accepted API.

* Fri Aug  7 2009 Tim Waugh <twaugh@redhat.com> 1.1.11-1
- 1.1.11:
  - Several udev-configure-printer fixes.
  - Use case-insensitive PPD matching.
  - Better URI validity testing.
  - Another stale printer status icon fix.
  - Notice when jobs stop due to backend errors.
  - Warn about job history when renaming printers.
  - Small UI improvements.

* Tue Aug  4 2009 Tim Waugh <twaugh@redhat.com> 1.1.10-8
- Dropped foomatic dependency from libs package.

* Fri Jul 31 2009 Tim Waugh <twaugh@redhat.com> 1.1.10-7
- Sync with 1.1.x.
- Added patch for cupspk DevicesGet method call.

* Mon Jul 27 2009 Matthias Clasen <mclasen@redhat.com> 1.1.10-6
- Drop no-longer-used python-sexy dep

* Sun Jul 26 2009 Tim Waugh <twaugh@redhat.com> 1.1.10-5
- Split out D-Bus service for udev helper.  Build requires
  dbus-glib-devel.

* Fri Jul 24 2009 Tim Waugh <twaugh@redhat.com> 1.1.10-3
- Removed gnome-packagekit dependency.  The presence of
  gpk-install-package-name is detected at run-time, and the program
  acts accordingly.

* Thu Jul 23 2009 Tim Waugh <twaugh@redhat.com> 1.1.10-2
- Applied some udev-configure-printer fixes from upstream.

* Wed Jul 22 2009 Tim Waugh <twaugh@redhat.com> 1.1.10-1
- 1.1.10:
  - New udev rules for adding/enabling/disabling USB printers
    automatically.
  - Now uses gnome-packagekit utility to install packages
    instead of the D-Bus API.
  - Fixed detection of stopped jobs with CUPS 1.4.
  - Fixed tracebacks when adding a new printer and when receiving
    IPP notifications.
  - Fixed 'location' field for printers added on remote CUPS servers.
  - Fixed handling of incorrect authentication.
  - Some UI and troubleshooter fixes have been made.

* Mon Jul  6 2009 Tim Waugh <twaugh@redhat.com> 1.1.8-6
- Requires gnome-packagekit for gpk-install-package-name.

* Fri Jul  3 2009 Tim Waugh <twaugh@redhat.com> 1.1.8-5
- Use gpk-install-package-name instead of trying to use the D-Bus API.
- Spot stopped jobs with CUPS 1.4 as well (trac #177).  This, along
  with the previous fix, addresses bug #509177.
- Map gutenprint filenames to the package name.
- Fixed sensitivity of class member selection arrows (bug #508653).

* Thu Jun 25 2009 Tim Waugh <twaugh@redhat.com> 1.1.8-3
- Use correct 'location' field for printers added remotely.
- Parse nmblookup failures correctly in troubleshooter.
- Prevent traceback on IPP notification after properties dialog
  cancelled.
- Fixed handling of incorrect authentication when not using
  PolicyKit (bug #508102).

* Wed Jun 24 2009 Tim Waugh <twaugh@redhat.com> 1.1.8-2
- Make sure we find https URIs from https backend (bug #507628).
- Avoid showing a non-fatal exception when adding an IPP printer
  (bug #507629).
- Fixed traceback when adding/modifying printer which could lead to
  display bugs (bug #507489).

* Thu Jun 18 2009 Tim Waugh <twaugh@redhat.com> 1.1.8-1
- Updated pycups to 1.9.46.
- Updated to 1.1.8:
  - Select a printer after adding it (trac #145).
  - Make sure the job and printer context menus cannot get out of date
    (trac #175, trac #172).
  - Fixed displayed hold time for held jobs.
  - Use grey ink-drop when there is no marker-colors value instead of
    crashing (bug #505399).
  - Scroll job list window to new job when appropriate.
  - Clean up temporary PPD files (bug #498743).
  - Fixed XML crash (Ubuntu #370469).
  - Fixed automatic printer model selection.
  - Fixed cupspk crash due to missing debugprint import (bug #496722,
    trac #161).
  - Fixed PhysicalDevice crash (bug #496722, trac #161).
  - Adjusted border padding for New Printer window (bug #493862).
  - Set glade's textdomain in the job viewer (Ubuntu #341765).
  - Fixed URI parsing when verifying IPP URIs.
  - Set relaxed PPD conformance (trac #159).
  - Make troubleshooter work again by disabling cupspk for it.

* Wed May 13 2009 Tim Waugh <twaugh@redhat.com> 1.1.7-4
- Changed requirement on notification-daemon to
  desktop-notification-daemon to allow for other implementations
  (bug #500587).

* Tue Apr 21 2009 Tim Waugh <twaugh@redhat.com> 1.1.7-3
- Moved them back again, as they are not part of the exported
  interface (bug #496808).

* Tue Apr 21 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.1.7-2
- Move files required by system-config-printer-kde to -libs (#496646)

* Tue Apr 14 2009 Tim Waugh <twaugh@redhat.com> 1.1.7-1
- Requires dbus-python (bug #495392).
- Updated to 1.1.7:
  - Updated translations.
  - Don't abort if the jobviewer couldn't show a notification.
  - Don't use setlocale() for locale-independent case conversion.
  - Don't assume the notification daemon can show action buttons.
  - Use case-insensitive matching for model names.
  - HPLIP compatibility fixes.
  - Fixed typo in jobviewer keyring support (Ubuntu #343156).
  - Added support for https device URIs (bug #478677).
  - Prevent traceback in monitor when connection failed (Ubuntu #343387).

* Fri Mar 13 2009 Tim Waugh <twaugh@redhat.com> 1.1.6-1
- No longer requires gnome-python2-gnome.
- Updated to 1.1.6:
  - Translatable string fix for authconn.
  - Romanian allow/deny translation fix (bug #489748).
  - Set glade's textdomain in the jobviewer (Ubuntu #341765).

* Tue Mar 10 2009 Tim Waugh <twaugh@redhat.com> 1.1.5-2
- Added patch for changes in 1.1.x since 1.1.5:
  - Strip " hpijs" from PPD names.
  - Handle there being no operation name set when authentication/retry
    is required.
  - Mark "Unauthorized" PolicyKit dialog strings for translation, and
    change that dialog to an error.
  - Work around marker-* attributes not being presented as lists
    (bug #489512).
  - D-Bus policy tweak.
  - Better PPD fallback searching.
  - Fixed model search oddity when no digits in model name.
  - Fixed locale save/restore in cupshelpers (bug #489313).
  - Use gtk.show_uri() instead of gnome.url_show() (trac #147).
  - Removed HPLIP probe screen (no longer needed).
  - Be certain of having the right cell when starting a rename
    (Ubuntu #333260).
  - Fixed strftime call (Ubuntu #334859).
  - Check dict before use when handling auth-info-required.
  - Handle timed operations being cancelled in the troubleshooter test
    print page (Ubuntu #325084).
  - Put pycups version requirement in monitor module.

* Tue Mar  3 2009 Tim Waugh <twaugh@redhat.com> 1.1.5-1
- 1.1.5.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Tim Waugh <twaugh@redhat.com> 1.1.4-2
- Updated from git:
  - Prevent traceback when adding new printer (bug #486587).

* Wed Feb 18 2009 Tim Waugh <twaugh@redhat.com> 1.1.4-1
- 1.1.4:
  - Skip model selection screen when adding a new printer for which we
    know the exact model.
  - Better integration for HPLIP hp and hpfax queues.
  - Work around HPLIP option parsing bug.
  - Pre-select the current device correctly.
  - Better descriptions for types of available connection.
  - Perform lowercase operations in a locale-independent manner (trac #151).

* Wed Feb 11 2009 Tim Waugh <twaugh@redhat.com> 1.1.3-7
- Updated from git:
  - Avoid tracebacks in main application (bug #484130) and job viewer.
  - Avoid unnecessary modal dialog when adding printer (bug #484960).
  - Don't use notification when authentication is required, just
    display the dialog.

* Tue Feb 10 2009 Tim Waugh <twaugh@redhat.com> 1.1.3-6
- Updated from git:
  - Better make/model discovery for multiple devices (bug #484130).

* Tue Feb 10 2009 Tim Waugh <twaugh@redhat.com> 1.1.3-5
- Updated from git:
  - Handle D-Bus failures when querying Jockey (bug #484402).
  - Set operation when fetching PPD from server (bug #484130).
  - Don't allow prompting when updating the UI for a server failure
    (bug #484130).
  - Fixed printing a test page from the applet (bug #484130).

* Mon Feb  9 2009 Tim Waugh <twaugh@redhat.com> 1.1.3-4
- Requires libxml2-python.

* Sat Feb  7 2009 Tim Waugh <twaugh@redhat.com> 1.1.3-3
- Ship the missing cupspk file (bug #484461).

* Thu Feb  5 2009 Tim Waugh <twaugh@redhat.com> 1.1.3-2
- Added in cups-pk-helper support from upstream.

* Tue Feb  3 2009 Tim Waugh <twaugh@redhat.com> 1.1.3-1
- Requires python-sexy.
- 1.1.3.

* Thu Jan 15 2009 Tim Waugh <twaugh@redhat.com> 1.1.2-1
- 1.1.2.
- Requires gnome-python2-gnomekeyring.

* Thu Jan  8 2009 Tim Waugh <twaugh@redhat.com> 1.1.1-2
- Updated pycups to 1.9.45.

* Sat Dec 20 2008 Tim Waugh <twaugh@redhat.com> 1.1.1-1
- 1.1.1.

* Fri Dec 19 2008 Tim Waugh <twaugh@redhat.com> 1.1.0-1
- 1.1.0.

* Fri Dec 19 2008 Tim Waugh <twaugh@redhat.com> 1.0.12-7
- Updated patch for 1.0.x changes:
  - Fixed stub scripts (bug #477107).

* Fri Dec 19 2008 Tim Waugh <twaugh@redhat.com> 1.0.12-6
- Updated patch for 1.0.x changes:
  - Look harder for locale/page size issues in the troubleshooter
    (trac #118).
  - Troubleshooter speed improvement (trac #123).
  - Localization fixes for authentication dialog (trac #122).
  - Character encoding fixes (trac #124).
  - Handle model names with more than one set of digits (Ubuntu #251244).
  - Catch unable-to-connect error when trying to print a test page
    (Ubuntu #286943).
  - Prevent crash when copying PPD options (Ubuntu #285133).
  - Use get_cursor for the printer properties treeview (Ubuntu #282634).
  - Fix IPP browser when trying to connect to host:port (bug #476396).
  - Make sure we're authenticating as the correct user in authconn.
  - Prevent traceback when adding printer driven by HPLIP
    (bug #477107).
  - Better display of available local HP fax devices.

* Wed Dec 17 2008 Tim Waugh <twaugh@redhat.com> 1.0.12-5
- Added patch for pycups git changes since 1.9.44:
  - Look for test page file in new location for CUPS 1.4 (bug #476612).

* Fri Dec 12 2008 Tim Waugh <twaugh@redhat.com> 1.0.12-4
- Updated patch for 1.0.x changes:
  - Fix for advanced server settings dialog.
  - Fixes for troubleshooter to restore error_log fetching.

* Wed Dec 10 2008 Tim Waugh <twaugh@redhat.com> 1.0.12-3
- Updated patch for 1.0.x changes:
  - Fixed problem that prevented authentication prompt being
    displayed.

* Fri Dec  5 2008 Tim Waugh <twaugh@redhat.com> 1.0.12-2
- Added patch for 1.0.x changes since 1.0.12:
  - Smarter PPD cache in cupshelpers module.
  - Don't write back localized versions of globalized PPDs.

* Mon Dec  1 2008 Tim Waugh <twaugh@redhat.com> 1.0.12-1
- Updated to 1.0.12:
  - Don't automatically replace network printer URIs with
    HPLIP URIs (bug #473129).
  - Fixed some file descriptor and temporary file leaks.
- Updated pycups to 1.9.44.

* Fri Nov 21 2008 Tim Waugh <twaugh@redhat.com> 1.0.11-1
- Updated to 1.0.11.
- Updated pycups to 1.9.43.

* Wed Nov 12 2008 Tim Waugh <twaugh@redhat.com> 1.0.10-2
- Updated to 1.0.10.  Applied patch from git.
- Applied pycups patch from git.

* Tue Oct 21 2008 Tim Waugh <twaugh@redhat.com> 1.0.9-1
- Updated to 1.0.9 for translations.
- Updated pysmbc to 1.0.6.  No longer need pysmbc-git patch.

* Fri Oct 17 2008 Tim Waugh <twaugh@redhat.com> 1.0.8-7
- Added patch for pysmbc changes in git to prevent getdents crashing
  (bug #465975).

* Thu Oct 16 2008 Tim Waugh <twaugh@redhat.com> 1.0.8-6
- Updated patch for 1.0.x changes:
  - Fixed SMB authentication dialog's cancel button (bug #467127).
  - Work around samba bug #5805 by sending debug output to stderr
    instead of stdout.

* Wed Oct 15 2008 Tim Waugh <twaugh@redhat.com> 1.0.8-5
- Updated patch for 1.0.x changes:
  - Fixed SMB authentication (bug #464003).

* Wed Oct 15 2008 Tim Waugh <twaugh@redhat.com> 1.0.8-4
- Updated patch for 1.0.x changes:
  - Removed unneeded debugging output.
  - Don't show the applet in KDE (bug #466945).
  - Auth/error dialog improvements for SMB as for IPP (bug #465407).

* Mon Oct 13 2008 Tim Waugh <twaugh@redhat.com> 1.0.8-3
- Added patch for 1.0.x changes since 1.0.8:
  - Don't use a LinkButton for the 'Problems?' button (bug #465407).
  - Don't use a separator for the server settings dialog (bug
    #465407).
  - Don't set non-zero page size for SpinButtons.
  - Don't show an error dialog if an IPP operation's authentication
    dialog is cancelled by the user, but show an error dialog if the
    password was incorrect (bug #465407).
  - Set Server Settings... menu entry sensitive depending on whether
    we are connected to a server (Ubuntu #280736).
  - Lots of translations updated.

* Mon Sep 29 2008 Tim Waugh <twaugh@redhat.com> 1.0.8-2
- Removed patch (no longer needed).

* Mon Sep 29 2008 Tim Waugh <twaugh@redhat.com> 1.0.8-1
- 1.0.8:
  - Use modelName from custom PPD to suggest name for new printer
    (trac #97).
  - Avoid display problem with installable options.
  - Better matching for Lexmark printers.
  - Catch exceptions from advanced server settings dialog (Ubuntu
    #267557).
  - Added some missing OpenPrinting query fields.
  - Jockey support added.
  - Lots of translations updated.

* Sat Aug 30 2008 Tim Waugh <twaugh@redhat.com> 1.0.7-2
- Handle IPP_FORBIDDEN (bug #460670).

* Fri Aug 29 2008 Tim Waugh <twaugh@redhat.com> 1.0.7-1
- 1.0.7:
  - Efficiency improvements.
  - Small UI improvements for the New Printer dialog.
  - Other small fixes.

* Fri Aug 29 2008 Tim Waugh <twaugh@redhat.com>
- Updated pysmbc to 1.0.5.
- Updated pycups to 1.9.42.

* Tue Aug 26 2008 Tim Waugh <twaugh@redhat.com> 1.0.6-1
- Requires gnome-python2-gnome (bug #460021).
- 1.0.6:
  - More delete-event fixes.
  - Fixed temporary file leak.
  - Fixed dialog leaks.
  - Small UI improvements for the New Printer dialog.
  - Other small fixes.

* Thu Aug 14 2008 Tim Waugh <twaugh@redhat.com> 1.0.5-3
- Include other fixes from upstream including:
  - OpenPrinting API change (trac #74).
  - libnotify API change for 'closed' signal.
  - Notification for job authentication (trac #91).
  - Glade delete-event fixes (trac #88).
  - Pre-fill username in job authentication dialog (trac #87).

* Wed Aug 13 2008 Tim Waugh <twaugh@redhat.com> 1.0.5-2
- Handle HTTP_FORBIDDEN.

* Mon Aug 11 2008 Tim Waugh <twaugh@redhat.com> 1.0.5-1
- 1.0.5.
- Updated pycups to 1.9.41.

* Thu Jul 10 2008 Tim Waugh <twaugh@redhat.com> 1.0.4-1
- 1.0.4.
- Applied upstream patch for pycups to fix getPrinterAttributes when
  requested_attributes is specified.

* Tue Jul  8 2008 Tim Waugh <twaugh@redhat.com> 1.0.3-2
- Better debugging for pysmbc.

* Mon Jun 30 2008 Tim Waugh <twaugh@redhat.com> 1.0.3-1
- Updated pycups to 1.9.40.
- 1.0.3.

* Fri Jun 20 2008 Tim Waugh <twaugh@redhat.com>
- Updated pysmbc to 1.0.4.

* Tue Jun 10 2008 Tim Waugh <twaugh@redhat.com> 1.0.2-1
- 1.0.2.

* Mon Jun  9 2008 Tim Waugh <twaugh@redhat.com> 1.0.1-1
- Updated pysmbc to 1.0.3.
- 1.0.1 (bug #450119).

* Thu Jun  5 2008 Tim Waugh <twaugh@redhat.com>
- Requires notify-python (bug #450139).

* Thu Jun  5 2008 Tim Waugh <twaugh@redhat.com> 1.0.0-3
- Applied patches from upstream (bug #450120).

* Tue Jun  3 2008 Tim Waugh <twaugh@redhat.com> 1.0.0-2
- Applied patches from upstream (bug #449753).

* Thu May 29 2008 Tim Waugh <twaugh@redhat.com>
- Updated pycups to 1.9.39.
- Updated libs summary.

* Tue May 27 2008 Tim Waugh <twaugh@redhat.com> 1.0.0-1
- 1.0.0.

* Fri May 23 2008 Tim Waugh <twaugh@redhat.com> 0.9.93-2
- Fixed small UI problem in SMB browser.

* Fri May 23 2008 Tim Waugh <twaugh@redhat.com> 0.9.93-1
- 0.9.93.

* Tue May 20 2008 Tim Waugh <twaugh@redhat.com> 0.9.92-1
- 0.9.92.

* Tue May 20 2008 Tim Waugh <twaugh@redhat.com> 0.9.91-3
- Sync to trunk.
- Updated pysmbc to 1.0.2.

* Sun May 18 2008 Tim Waugh <twaugh@redhat.com> 0.9.91-2
- Fixed icon search path.

* Fri May 16 2008 Tim Waugh <twaugh@redhat.com> 0.9.91-1
- No longer requires system-install-packages (bug #444645).
- Added pysmbc.  Build requires libsmbclient-devel.
- Don't install consolehelper bits any more as they are no longer needed.
- 0.9.91:
  - User interface overhaul, part 2.

* Thu Apr  3 2008 Tim Waugh <twaugh@redhat.com> 0.9.90-1
- Updated pycups to 1.9.38.
- 0.9.90:
  - User interface overhaul, part 1.

* Thu Apr  3 2008 Tim Waugh <twaugh@redhat.com> 0.7.82.2-1
- 0.7.82.2:
  - Various bug fixes.
  - Translation updates.

* Mon Mar 17 2008 Tim Waugh <twaugh@redhat.com> 0.7.82.1-3
- Updated pycups to 1.9.37.
- More fixes from upstream.

* Wed Mar  5 2008 Tim Waugh <twaugh@redhat.com> 0.7.82.1-2
- Updated pycups to 1.9.36.
- Some fixes from upstream.

* Mon Mar  3 2008 Tim Waugh <twaugh@redhat.com> 0.7.82.1-1
- Requires %_bindir/system-install-packages not pirut (bug #435622).
- 0.7.82.1:
  - More trouble-shooting improvements.
  - applet: notify user about failed jobs (bug #168370).

* Tue Feb 19 2008 Tim Waugh <twaugh@redhat.com> 0.7.82-1
- Updated to pycups-1.9.35.
- 0.7.82:
  - More trouble-shooting improvements.

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 0.7.81-1
- 0.7.81:
  - Trouble-shooting improvements and other minor fixes.

* Mon Feb 11 2008 Tim Waugh <twaugh@redhat.com> 0.7.80-2
- Rebuild for GCC 4.3.

* Mon Feb  4 2008 Tim Waugh <twaugh@redhat.com> 0.7.80-1
- Updated to pycups-1.9.34.
- 0.7.80:
  - Trouble-shooting support.

* Fri Jan 25 2008 Tim Waugh <twaugh@redhat.com> 0.7.79-1
- 0.7.79.

* Wed Jan 23 2008 Tim Waugh <twaugh@redhat.com> 0.7.78-5
- Updated to pycups-1.9.33.

* Wed Jan 16 2008 Tim Waugh <twaugh@redhat.com> 0.7.78-4
- Use config-util from new usermode (bug #428406).

* Thu Dec 20 2007 Tim Waugh <twaugh@redhat.com>
- Requires notification-daemon (Ubuntu #176929).
- Requires gnome-python2 for theme support (Ubuntu #176929).
- Requires gnome-icon-theme for printer icon (Ubuntu #176929).

* Mon Dec 17 2007 Tim Waugh <twaugh@redhat.com> 0.7.78-3
- Install Python egg-info file.
- Updated pycups to 1.9.32.

* Tue Nov 27 2007 Tim Waugh <twaugh@redhat.com> 0.7.78-2
- pycups: Applied patch from SVN to allow fetching printer attributes by URI.
- Sync to SVN 1748.

* Thu Nov 22 2007 Tim Waugh <twaugh@redhat.com> 0.7.78-1
- pycups: Fix job-sheets-default attribute.
- Updated pycups to 1.9.31.
- 0.7.78.

* Wed Nov 21 2007 Tim Waugh <twaugh@redhat.com>
- Applied patch to pycups to avoid reading uninitialised
  memory (bug #390431).

* Mon Nov 19 2007 Tim Waugh <twaugh@redhat.com>
- Updated pycups to 1.9.30.

* Tue Oct 30 2007 Tim Waugh <twaugh@redhat.com> 0.7.77-1
- 0.7.77:
  - Tooltips for the button bar buttons (bug #335601).

* Mon Oct 15 2007 Tim Waugh <twaugh@redhat.com> 0.7.76-1
- 0.7.76.

* Thu Oct  4 2007 Tim Waugh <twaugh@redhat.com> 0.7.75-1
- 0.7.75.

* Wed Oct  3 2007 Tim Waugh <twaugh@redhat.com>
- No need to run update-desktop-database because there are no MimeKey
  lines in the desktop files.
- Consistent macro style.

* Tue Oct  2 2007 Tim Waugh <twaugh@redhat.com> 0.7.74.4-1
- Changed PreReq to Requires.
- Mark console.apps file as a config file.
- Mark pam file as a config file (not replaceable).
- No need to ship empty NEWS file.
- Give cupsd.py executable permissions to satisfy rpmlint.
- Provides system-config-printer-gui.
- Mark D-Bus configuration file as a config file.
- Fixed libs summary.
- Better buildroot tag.
- Better defattr.
- Preserve timestamps on explicitly install files.
- Make example pycups program non-executable.
- 0.7.74.4:
  - Updated translations.
  - Several small bugs fixed.

* Thu Sep 27 2007 Tim Waugh <twaugh@redhat.com> 0.7.74.3-1
- 0.7.74.3:
  - Updated translations.
  - Other small bug fixes.

* Tue Sep 25 2007 Tim Waugh <twaugh@redhat.com> 0.7.74.2-3
- Pull in SVN patch from stable branch for foomatic recommended
  drivers (bug #292021).

* Fri Sep 21 2007 Tim Waugh <twaugh@redhat.com> 0.7.74.2-2
- Pull in SVN patch from stable branch for 'Allow printing from
  the Internet' check-box (bug #221003).

* Wed Sep 19 2007 Tim Waugh <twaugh@redhat.com> 0.7.74.2-1
- Updated pycups to 1.9.27.
- 0.7.74.2:
  - When a class is removed on the server, remove it from the UI.
  - When deleting a printer, select the default printer again.
  - Select newly-copied printer.
  - Updated translation (fi).
  - Better --help message.
  - Use strcoll to sort manufacturer names.
  - Avoid duplicate 'recommended' marks.
  - Remove duplicate device URIs.
  - Handle IPP_TAG_NOVALUE attributes (for CUPS 1.3.x).

* Wed Sep 12 2007 Tim Waugh <twaugh@redhat.com>
- Updated pycups to 1.9.26.
- Build requires epydoc.  Ship HTML documentation.

* Fri Sep  7 2007 Tim Waugh <twaugh@redhat.com> 0.7.74.1-1
- 0.7.74.1:
  - Updated Polish translation (bug #263001).
  - Don't select the default printer after changes to another printer have
    been made.
  - Always construct URI from input fields when changing device (bug #281551).
  - Avoid busy-cursor traceback when window is not yet displayed.

* Thu Aug 30 2007 Tim Waugh <twaugh@redhat.com> 0.7.74-1
- Updated pycups to 1.9.25.
- 0.7.74:
  - Fixed New Class dialog.
  - UI fixes.

* Sat Aug 25 2007 Tim Waugh <twaugh@redhat.com>
- More specific license tag.

* Fri Aug 24 2007 Tim Waugh <twaugh@redhat.com> 0.7.73-1
- 0.7.73.

* Fri Aug 10 2007 Tim Waugh <twaugh@redhat.com> 0.7.72-2
- Ship the applet's desktop file.

* Wed Aug  8 2007 Tim Waugh <twaugh@redhat.com> 0.7.72-1
- 0.7.72:
  - Fixed my-default-printer traceback.
  - Improvements to New Printer wizard (Till Kamppeter).

* Fri Aug  3 2007 Tim Waugh <twaugh@redhat.com> 0.7.71-1
- 0.7.71:
  - Don't discard make/model-matched devices when there are ID-matched
    devices (Till Kamppeter).
  - Fixed fallback if no text-only driver is available (Till Kamppeter).
  - Initialise the make/model list when an ID match failed (Till Kamppeter).
  - Better error-handling in default-print application (Ubuntu #129901).
  - UI tweak in admin tool (Ubuntu #128263).
  - Handle socket: URIs (Ubuntu #127074).

* Mon Jul 23 2007 Tim Waugh <twaugh@redhat.com> 0.7.70-2
- Obsoletes/provides desktop-printing.

* Mon Jul  9 2007 Tim Waugh <twaugh@redhat.com> 0.7.70-1
- Requires pirut for system-install-packages.
- 0.7.70:
  - Increased GetReady->NewPrinter timeout.
  - More binary names mapped to package named.
  - Run system-install-packages to install missing drivers (bug #246726).
  - Less debug output.
  - Desktop file fixes for KDE (bug #247299).

* Thu Jun 28 2007 Tim Waugh <twaugh@redhat.com> 0.7.69-1
- No longer requires PyXML (bug #233146).
- Moved applet to main package.
- 0.7.69:
  - Use HardwareSettings category for my-default-printer desktop
    file (bug #244935).
  - Removed unused code.
  - Filter PPDs by natural language (bug #244173).

* Mon Jun 25 2007 Tim Waugh <twaugh@redhat.com>
- The applet requires dbus-x11 (Ubuntu #119570).

* Fri Jun 15 2007 Tim Waugh <twaugh@redhat.com> 0.7.68-1
- 0.7.68:
  - Fixed the notification bubbles.
  - Ship my-default-printer utility.

* Fri Jun  8 2007 Tim Waugh <twaugh@redhat.com> 0.7.67-1
- Don't put TrayIcon or SystemSetup categories in the desktop file.
- Updated pycups to 1.9.24.
- 0.7.67:
  - Fixed desktop files to have capital letters at the start of each
    word in the Name field (bug #242859).
  - Fixed crash when saving unapplied changes.
  - Fixed Device ID parser to always split the CMD field at commas.
  - New PPDs class means we no longer parse the foomatic XML database.

* Wed May 30 2007 Tim Waugh <twaugh@redhat.com> 0.7.66-1
- 0.7.66:
  - Allow job-hold-until to be set (bug #239776).
  - Implement new printer notifications.

* Tue May 22 2007 Tim Waugh <twaugh@redhat.com> 0.7.65-1
- Build requires xmlto.
- Updated to pycups-1.9.22.
- 0.7.65:
  - Use urllib for quoting/unquoting (Val Henson, Ubuntu #105022).
  - Added kn translation.
  - Better permissions on non-scripts.
  - Added man pages.
  - Applet: status feedback.
  - Applet: fixed relative time descriptions.
  - Applet: limit refresh frequency.

* Mon Apr 16 2007 Tim Waugh <twaugh@redhat.com> 0.7.63.1-1
- 0.7.63.1:
  - Small applet fixes.

* Thu Apr  5 2007 Tim Waugh <twaugh@redhat.com> 0.7.63-1
- 0.7.63:
  - Translation updates.
  - Checked in missing file.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com>
- Updated to pycups-1.9.20 for printer-state-reasons fix.

* Mon Apr  2 2007 Tim Waugh <twaugh@redhat.com> 0.7.62-1
- 0.7.62:
  - Use standard icon for admin tool desktop file.
  - Fixed env path in Python scripts.
  - Applet: stop running when the session ends.
  - Prevent a traceback in the SMB browser (bug #225351).
  - 'Manage print jobs' desktop file.

* Fri Mar 30 2007 Tim Waugh <twaugh@redhat.com> 0.7.61-1
- 0.7.61:
  - Fixed retrieval of SMB authentication details (bug #203539).

* Tue Mar 27 2007 Tim Waugh <twaugh@redhat.com> 0.7.60-1
- Updated to pycups-1.9.19.
- Avoid %%makeinstall.
- 0.7.60:
  - Handle reconnection failure.
  - New applet name.

* Mon Mar 26 2007 Tim Waugh <twaugh@redhat.com> 0.7.59-1
- 0.7.59:
  - Fixed a translatable string.
  - Set a window icon (bug #233899).
  - Handle failure to start the D-Bus service.
  - Ellipsize the document and printer named (bug #233899).
  - Removed the status bar (bug #233899).
  - Added an icon pop-up menu for 'Hide' (bug #233899).

* Wed Mar 21 2007 Tim Waugh <twaugh@redhat.com> 0.7.57-1
- Added URL tag.
- 0.7.57:
  - Prevent traceback when removing temporary file (Ubuntu #92914).
  - Added print applet.

* Sun Mar 18 2007 Tim Waugh <twaugh@redhat.com> 0.7.56-2
- Updated to pycups-1.9.18.

* Fri Mar 16 2007 Tim Waugh <twaugh@redhat.com> 0.7.56-1
- 0.7.56:
  - Parse Boolean strings correctly in job options.
  - Small command-set list/string fix (bug #230665).
  - Handle hostname look-up failures.
  - Updated filter-to-driver map.
  - Don't parse printers.conf (bug #231826).

* Tue Feb 27 2007 Tim Waugh <twaugh@redhat.com> 0.7.55-1
- 0.7.55:
  - Use converted value for job option widgets.

* Tue Feb 27 2007 Tim Waugh <twaugh@redhat.com> 0.7.54-1
- 0.7.54:
  - Removed debugging code.

* Tue Feb 27 2007 Tim Waugh <twaugh@redhat.com> 0.7.53-1
- No longer requires rhpl (since 0.7.53).
- 0.7.53:
  - Use gettext instead of rhpl.translate.
  - Better layout for PPD options.
  - Added scrollbars to main printer list (bug #229453).
  - Set maximum width of default printer label (bug #229453).
  - Handle applying changes correctly when switching to another
    printer (bug #229378).
  - Don't crash when failing to fetch the PPD (bug #229406).
  - Make the text entry boxes sensitive but not editable for remote
    printers (bug #229381).
  - Better job options screen layout (bug #222272).

* Tue Feb 13 2007 Tim Waugh <twaugh@redhat.com> 0.7.52-1
- 0.7.52:
  - Sort models using cups.modelSort before scanning for a close
    match (bug #228505).
  - Fixed matching logic (bug #228505).

* Fri Feb  9 2007 Tim Waugh <twaugh@redhat.com> 0.7.51-1
- 0.7.51:
  - Prevent display glitch in job options list when clicking on a printer
    repeatedly.
  - List conflicting PPD options, and embolden the relevant tab
    labels (bug #226368).
  - Fixed typo in 'set default' handling that caused a traceback (bug #227936).
  - Handle interactive search a little better (bug #227935).

* Wed Feb  7 2007 Tim Waugh <twaugh@redhat.com> 0.7.50-1
- 0.7.50:
  - Fixed hex digits list (bug #223770).
  - Added bs translation.
  - Don't put the ellipsis in the real device URI (bug #227643).
  - Don't check for existing drivers for complex command lines (bug #225104).
  - Allow floating point job options (bug #224651).
  - Prevent shared/published confusion (bug #225081).
  - Fixed PPD page size setting.
  - Avoid os.remove exception (bug #226703).
  - Handle unknown job options (bug #225538).

* Tue Jan 16 2007 Tim Waugh <twaugh@redhat.com> 0.7.49-1
- 0.7.49:
  - Fixed a traceback in the driver check code.
  - Fixed a typo in the conflicts message.
  - Handle InputSlot/ManualFeed specially because libcups does (bug #222490).

* Mon Jan 15 2007 Tim Waugh <twaugh@redhat.com> 0.7.48-1
- 0.7.48:
  - Updated translations.

* Fri Jan 12 2007 Tim Waugh <twaugh@redhat.com> 0.7.47-1
- 0.7.47:
  - Fixed minor text bugs (bug #177433).
  - Handle shell builtins in the driver check (bug #222413).

* Mon Jan  8 2007 Tim Waugh <twaugh@redhat.com> 0.7.46-1
- 0.7.46:
  - Fixed page size problem (bug #221702).
  - Added 'ro' to ALL_LINGUAS.

* Wed Jan  3 2007 Tim Waugh <twaugh@redhat.com> 0.7.45-1
- Updated to pycups-1.9.17.
- 0.7.45:
  - Fixed traceback in driver check.

* Tue Jan  2 2007 Tim Waugh <twaugh@redhat.com> 0.7.44-1
- 0.7.44:
  - Fixed traceback in error display (bug #220136).
  - Preserve case in model string when dumping debug output.

* Thu Dec 21 2006 Tim Waugh <twaugh@redhat.com> 0.7.43-1
- 0.7.43:
  - Don't check against IEEE 1284 DES field at all.
  - Merged device matching code (bug #219518).
  - Catch non-fatal errors when auto-matching device.
  - Fixed driver checking bug involving pipelines (bug #220347).
  - Show PPD errors (bug #220136).

* Mon Dec 11 2006 Tim Waugh <twaugh@redhat.com> 0.7.42-1
- 0.7.42:
  - Fixed typo in command set matching code.
  - Case-insensitive matching when Device ID not known to database.

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0.7.41-2
- build against python 2.5

* Thu Dec  7 2006 Tim Waugh <twaugh@redhat.com> 0.7.41-1
- Updated pycups to 1.9.16.
- 0.7.41:
  - Reconnect smoothly after uploading new configuration.
  - Update lpoptions when setting default printer if it conflicts with
    the new setting (bug #217395).
  - Fixed typo in show_HTTP_Error (bug #217537).
  - Don't pre-select make and model when not discoverable for chosen
    device (bug #217518).
  - Set Forward button sensitive on Device screen in new-printer
    dialog (bug #217515).
  - Keep Server Settings selected after applying changes if it was selected
    before.
  - Set Connecting dialog transient for main window.
  - Center Connecting dialog on parent.
  - Optional 'reason' argument for cupshelpers.Printer.setEnabled.
  - Describe devices that have no optional parameters.

* Thu Nov 30 2006 Tim Waugh <twaugh@redhat.com>
- Provide pycups feature.

* Tue Nov 21 2006 Tim Waugh <twaugh@redhat.com> 0.7.40-1
- 0.7.40:
  - Removed username:password from hint string because we add that in
    afterwards.
  - Don't set button widths in create-printer dialog (bug #217025).

* Tue Nov 21 2006 Tim Waugh <twaugh@redhat.com> 0.7.39-1
- 0.7.39:
  - Busy cursor while loading foomatic and PPD list (bug #215527).
  - Make PPD NickName selectable.
  - Added SMB hint label on device screen (bug #212759).

* Tue Nov 14 2006 Tim Waugh <twaugh@redhat.com> 0.7.38-1
- Updated pycups to 1.9.15.
- 0.7.38:
  - Fixed a bug in the 'ieee1284'/'ppd-device-id' parsing code.

* Mon Nov 13 2006 Tim Waugh <twaugh@redhat.com> 0.7.37-1
- 0.7.37:
  - Allow cancellation of test pages (bug #215054).

* Fri Nov 10 2006 Tim Waugh <twaugh@redhat.com> 0.7.36-1
- 0.7.36:
  - Match against commandset (bug #214181).
  - Parse 'ieee1284' foomatic autodetect entries (bug #214761).
  - Don't remove foomatic PPDs from the list (bug #197331).

* Tue Nov  7 2006 Tim Waugh <twaugh@redhat.com> 0.7.35-1
- 0.7.35.

* Thu Nov  2 2006 Tim Waugh <twaugh@redhat.com>
- Updated to pycups-1.9.14 (bug #213136).

* Tue Oct 31 2006 Tim Waugh <twaugh@redhat.com>
- Update desktop database (bug #213249).

* Tue Oct 24 2006 Tim Waugh <twaugh@redhat.com>
- Build requires Python 2.4.

* Mon Oct  2 2006 Tim Waugh <twaugh@redhat.com> 0.7.32-1
- Updated to pycups-1.9.13 for HTTP_FORBIDDEN.
- 0.7.32:
  - Handle HTTP errors during connection (bug #208824).
  - Updated translations (bug #208873).

* Fri Sep 29 2006 Tim Waugh <twaugh@redhat.com> 0.7.31-1
- 0.7.31:
  - Select recommended driver automatically (bug #208606).
  - Better visibility of driver list (bug #203907).

* Fri Sep 29 2006 Tim Waugh <twaugh@redhat.com> 0.7.30-1
- 0.7.30:
  - Translations fixed properly (bug #206622).
  - Button widths corrected (bug #208556).

* Tue Sep 26 2006 Tim Waugh <twaugh@redhat.com> 0.7.28-1
- 0.7.28.  Translations fixed (bug #206622).

* Wed Aug 30 2006 Tim Waugh <twaugh@redhat.com> 0.7.27-1
- Build requires intltool.
- 0.7.27.

* Wed Aug 23 2006 Tim Waugh <twaugh@redhat.com> 0.7.26-1
- 0.7.26.  Fixes bug # 203149.

* Mon Aug 14 2006 Florian Festi <ffesti@redhat.com> 0.7.25-1
- 0.7.25. (bug #202060)

* Fri Aug 11 2006 Tim Waugh <twaugh@redhat.com>
- Fixed description (bug #202189).

* Thu Aug  3 2006 Tim Waugh <twaugh@redhat.com> 0.7.24-1
- 0.7.24.

* Mon Jul 24 2006 Tim Waugh <twaugh@redhat.com> 0.7.23-1
- 0.7.23.  Fixes bug #197866.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.7.22-1.1
- rebuild

* Fri Jul  7 2006 Tim Waugh <twaugh@redhat.com> 0.7.22-1
- 0.7.22.

* Wed Jul  5 2006 Tim Waugh <twaugh@redhat.com> 0.7.21-1
- Updated to pycups-1.9.12.
- 0.7.21.

* Mon Jul  3 2006 Tim Waugh <twaugh@redhat.com> 0.7.20-1
- 0.7.20.

* Fri Jun 30 2006 Tim Waugh <twaugh@redhat.com> 0.7.19-1
- 0.7.19.
- Remove foomatic pickle file post-install.

* Tue Jun 27 2006 Tim Waugh <twaugh@redhat.com> 0.7.18-1
- 0.7.18.
- Ship translations with libs subpackage.

* Fri Jun 23 2006 Tim Waugh <twaugh@redhat.com> 0.7.17-1
- 0.7.17.

* Fri Jun 23 2006 Tim Waugh <twaugh@redhat.com> 0.7.16-1
- 0.7.16, now with SMB browser.

* Wed Jun 22 2006 Tim Waugh <twaugh@redhat.com> 0.7.15-1
- 0.7.15.
- Build requires gettext-devel.
- Ship translations.

* Tue Jun 20 2006 Tim Waugh <twaugh@redhat.com> 0.7.14-1
- 0.7.14.

* Mon Jun 19 2006 Tim Waugh <twaugh@redhat.com> 0.7.13-1
- 0.7.13.

* Fri Jun  9 2006 Tim Waugh <twaugh@redhat.com> 0.7.12-1
- 0.7.12.

* Thu Jun  1 2006 Tim Waugh <twaugh@redhat.com> 0.7.11-3
- Fix libs dependency.

* Thu Jun  1 2006 Tim Waugh <twaugh@redhat.com> 0.7.11-2
- Moved the gtk_html2pango module to the libs package (needed by
  foomatic.py).

* Wed May 31 2006 Tim Waugh <twaugh@redhat.com> 0.7.11-1
- Split out system-config-printer-libs.
- Updated to system-config-printer-0.7.11.

* Sat May 27 2006 Tim Waugh <twaugh@redhat.com> 0.7.10-2
- Requires gobject2 (bug #192764).

* Fri May 26 2006 Tim Waugh <twaugh@redhat.com> 0.7.10-1
- Require foomatic (bug #192764).
- Updated to system-config-printer-0.7.10.

* Thu May 25 2006 Tim Waugh <twaugh@redhat.com> 0.7.9-1
- Updated to pycups-1.9.11.
- Updated to system-config-printer-0.7.9.

* Mon May 15 2006 Tim Waugh <twaugh@redhat.com> 0.7.8-1
- Updated to pycups-1.9.10.
- Updated to system-config-printer-0.7.8.

* Fri May  5 2006 Tim Waugh <twaugh@redhat.com>
- Fix pycups segfault.

* Fri May  5 2006 Tim Waugh <twaugh@redhat.com> 0.7.7-2
- Ship PAM and userhelper files.
- Requires usermode.
- Added missing options.py file.
- Fix getClasses() in pycups.

* Thu May  4 2006 Tim Waugh <twaugh@redhat.com> 0.7.7-1
- Updated to system-config-printer-0.7.7.
- Updated to pycups-1.9.9.
- Desktop file.
- Requires PyXML.

* Fri Apr 28 2006 Tim Waugh <twaugh@redhat.com>
- Make it actually run.

* Fri Apr 21 2006 Tim Waugh <twaugh@redhat.com>
- Build requires CUPS 1.2.

* Thu Apr 20 2006 Tim Waugh <twaugh@redhat.com> 0.7.5-1
- Updated to pycups-1.9.8.  No longer need threads patch.
- Updated to system-config-printer-0.7.5.

* Sat Apr 15 2006 Tim Waugh <twaugh@redhat.com>
- Updated to pycups-1.9.7.

* Thu Apr 13 2006 Tim Waugh <twaugh@redhat.com> 0.7.4-2
- Obsoletes: system-config-printer-gui <= 0.6.152

* Wed Apr 12 2006 Tim Waugh <twaugh@redhat.com> 0.7.4-1
- Updated to system-config-printer-0.7.4.

* Fri Apr  7 2006 Tim Waugh <twaugh@redhat.com> 0.7.3-1
- Added threads patch from pycups CVS.
- Updated to system-config-printer-0.7.3.

* Tue Apr  4 2006 Tim Waugh <twaugh@redhat.com>
- Updated to pycups-1.9.6.

* Fri Mar 24 2006 Tim Waugh <twaugh@redhat.com>
- Updated to pycups-1.9.5.

* Fri Mar 17 2006 Tim Waugh <twaugh@redhat.com>
- Package the actual system-config-printer command.

* Thu Mar 16 2006 Tim Waugh <twaugh@redhat.com> 0.7.1-1
- Include s-c-printer tarball.
- Updated to pycups-1.9.4.

* Wed Mar 15 2006 Tim Waugh <twaugh@redhat.com> 0.7.0-1
- Initial spec file.
