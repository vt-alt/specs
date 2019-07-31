BuildRequires: desktop-file-utils
Name: krb5-ticket-watcher
Version: 1.0.3
Release: alt18
Summary: A Tray Applet for Watching, Renewing, and Reinitializing Kerberos Tickets
Url: http://sourceforge.net/projects/krb5ticketwatch
License: %gpl2plus
Group: System/X11

Source: %name-%version.tar
Patch1: 0001-made-default-realm-the-first-one-in-list.patch
Patch2: krb5-ticket-watcher-1.0-alt-date-fix.patch
Patch3: krb5-ticket-watcher-1.0.3-alt-fix-includes.patch
Patch4: krb5-ticket-watcher-1.0.3-alt-fix-desktop-category.patch
Patch5: alt-qt5-1.patch
Patch6: alt-tray-icon.patch
Patch7: alt-wait-for-tray.patch
Patch8: alt-force-kinit.patch
Patch9: alt-password-dialog-ontop.patch
Patch10: krb5-ticket-watcher-add-pw-exp-notif.patch
Patch11: fix-deprecated-krb5-api-meth.patch

BuildRequires: kde-common-devel rpm-build-licenses rpm-build-xdg libkrb5-devel libkeyutils-devel
BuildRequires: cmake gcc-c++ libcom_err-devel qt5-base-devel qt5-tools

%description
A tray applet for watching, renewing, and reinitializing Kerberos
tickets.

%prep
%setup
%patch1 -p2
%patch2 -p1
%patch3 -p2
%patch4 -p2
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
%add_optflags -DDEBUG -I%_includedir/krb5
%ifarch %e2k
%add_optflags -std=c++11
%endif
%Kbuild

%install
%Kinstall
desktop-file-install --dir %buildroot%_desktopdir \
	%buildroot%_desktopdir/krb5-ticket-watcher.desktop
desktop-file-install --dir %buildroot/%_xdgconfigdir/autostart \
	%buildroot/%_desktopdir/krb5-ticket-watcher.desktop

%files
%_bindir/krb5-ticket-watcher
%_pixmapsdir/krb5-ticket-watcher.png
%_desktopdir/krb5-ticket-watcher.desktop
%_xdgconfigdir/autostart/krb5-ticket-watcher.desktop
%{_datadir}/locale/*/*/*.mo
%doc COPYING Changes News TODO

%changelog
* Thu Jul 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt18
- patch of fix deprecated krb5 api meth updated

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt17
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt16
- NMU: remove %ubt from release

* Tue Sep 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt15%ubt
- fixed methods in accordance with the new version

* Tue Sep 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt14%ubt
- add password expires notification

* Thu May 31 2018 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt13%ubt
- update compile flags

* Fri Apr 13 2018 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt12%ubt
- change system tray icon

* Tue Oct 24 2017 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt11%ubt
- don't raise password dialog window

* Mon Oct 23 2017 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt10%ubt
- set password dialog on top (ALT#34001)

* Mon Jul 24 2017 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt9%ubt
- fix check for auth at start

* Tue Jun 27 2017 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt8%ubt
- more check before force kinit at start

* Tue Jun 27 2017 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt7%ubt
- force kinit at start

* Thu Jun 01 2017 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt6%ubt
- wait for system tray (ALT#33518)

* Wed May 31 2017 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt5%ubt
- port to Qt5

* Tue May 30 2017 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt4%ubt
- Add XDG autostart entry

* Fri Mar 22 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt3
- Traslate desktop file into Russian

* Thu Mar 21 2013 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt2
- Fix desktop file categories (ALT #28731)

* Sat Jan 05 2013 Ivan A. Melnikov <iv@altlinux.org> 1.0.3-alt1.1
- Fixed build with new krb5;
- Minor packaging improvements.

* Thu Sep 27 2012 Andriy Stepanov <stanv@altlinux.ru> 1.0.3-alt1
- New version

* Thu Jul 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3.qa2
- Fixed build

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.2-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for krb5-ticket-watcher

* Wed Apr 08 2009 Andriy Stepanov <stanv@altlinux.ru> 1.0.2-alt3
- #19536 (fix: convert valid/expires info to local charset)

* Mon Mar 30 2009 Andriy Stepanov <stanv@altlinux.ru> 1.0.2-alt2
- Add patch: Fetch default REALM name from DNS records.

* Sun Mar 22 2009 Andriy Stepanov <stanv@altlinux.ru> 1.0.2-alt1
- New version.

* Fri Mar 20 2009 Andriy Stepanov <stanv@altlinux.ru> 1.0.1-alt1
- Initial import to Sisyphus
