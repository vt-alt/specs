%define distro_version 5.0

%define _altdata_dir %_datadir/alterator

Name: alterator-pkg
Version: 2.7.3
Release: alt1

%add_findreq_skiplist %_libexecdir/alterator/backend3/pkg-init
%add_findreq_skiplist %_datadir/install2/initinstall.d/*
%add_findreq_skiplist %_datadir/install2/postinstall.d/*

Packager: Andrey Cherepanov <cas@altlinux.org> 

BuildArch: noarch

Source:%name-%version.tar

Summary: additional package installation
License: GPL
Group: System/Configuration/Other

Requires: alterator >= 4.6-alt3 alterator-sh-functions libshell alterator-l10n >= 2.4-alt11
Requires: alterator-browser-qt >= 2.17.0
Requires: apt >= 0.5.15lorg2-alt23
Requires: alterator-lookout => 2.4-alt1
Requires: altlinux-repos
Conflicts: alterator-fbi < 5.10-alt1

Provides: alterator-apt = %version
Obsoletes: alterator-apt

BuildPreReq: alterator >= 4.6-alt3

Conflicts: apt-conf-branch < 5.0-alt3
Conflicts: apt-conf-sisyphus < 5.0-alt4
Conflicts: apt-conf-desktop < 5.0-alt3

Provides: %name-tools = %version
Obsoletes: %name-tools

%description
additional package installation

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_libexecdir/alterator/hooks/pkg-preinstall.d
%_datadir/install2/initinstall.d/*
%_datadir/install2/postinstall.d/*
%_datadir/install2/prepkg.d
%_alterator_backend3dir/*

%changelog
* Fri Sep 06 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.7.3-alt1
- apt-mark all manifested packages as manual

* Wed Jul 10 2019 Alexey Shabalin <shaba@altlinux.org> 2.7.2-alt1
- mount separate tmpfs for /mnt/destination/run

* Tue Jul 09 2019 Alexey Shabalin <shaba@altlinux.org> 2.7.1-alt1
- add symlinks /var/run -> /run, and /var/lock -> /run/lock

* Thu Jun 07 2018 Michael Shigorin <mike@altlinux.org> 2.7-alt1
- RPM 4.13 support

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 2.6.21-alt1
- get package list with comments in group content (ALT#32734)

* Thu Apr 28 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.6.20-alt1
- size calculations errors are placed into /tmp/install2.log now

* Fri Mar 25 2016 Michael Shigorin <mike@altlinux.org> 2.6.19-alt1
- Fix for group files in subdirectories

* Mon Jan 13 2014 Michael Shigorin <mike@altlinux.org> 2.6.18-alt1
- Drop 90-pkg.sh, see also installer-feature-cdrom-add (closes: #29704)

* Sun Jan 12 2014 Evgeny Sinelnikov <sin@altlinux.ru> 2.6.17-alt1
- Add support cifs install method

* Wed Dec 04 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.16-alt1
- Show comment in group content if it exists or package list (ALT #27973)

* Sun Dec 01 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.15-alt1
- Show group content in details pane

* Thu Nov 28 2013 Michael Shigorin <mike@altlinux.org> 2.6.14-alt1
- Fix cosmetic error in 2.6.13

* Tue Oct 29 2013 Michael Shigorin <mike@altlinux.org> 2.6.13-alt1
- Create /media/cdrom and configure it for apt only when
  installation is performed off CD/DVD media

* Mon Aug 12 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.12-alt1
- Don't display text on progressbar
- Add details pane in group selection

* Tue Jun 18 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.11-alt2
- add R: altlinux-repos

* Tue Jun 11 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.11-alt1
- Localize units in total installed size

* Wed May 15 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.10-alt3
- Fix repository sources with Arepo 2.0

* Wed May 08 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.10-alt2
- Recalculate total installed size on profile change

* Mon Apr 29 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.10-alt1
- Add profile support in group selection

* Tue Apr 02 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.9-alt1
- Correct conflicts processes

* Tue Dec 13 2011 Andrey Cherepanov <cas@altlinux.org> 2.6.8-alt1
- Ignore missed trailing new line in package lists (closes: #26696)

* Fri Nov 18 2011 Michael Shigorin <mike@altlinux.org> 2.6.7-alt1
- disable apt's faulty HTTP pipelining (thanks sin@)

* Thu Oct 06 2011 Andrey Cherepanov <cas@altlinux.org> 2.6.6-alt1
- Return all parents for checked items
  (behaviour is controlled by (include-parent-items?))

* Fri Sep 09 2011 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt2
- Don't ignore punctuation to file sort order

* Thu Aug 11 2011 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- Support Arepo repository in source selection for x86_64

* Thu Aug 11 2011 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- Log messages to /tmp/pkg-install.log for install via pipe

* Thu Jul 21 2011 Michael Shigorin <mike@altlinux.org> 2.6.3-alt1
- fix the fix (was spoiling comments)

* Tue Jul 19 2011 Michael Shigorin <mike@altlinux.org> 2.6.2-alt1
- fix "package per line" assumption

* Thu Jul 14 2011 Mikhail Efremov <sem@altlinux.org> 2.6.1-alt1
- Fix 'step' slideshow parameter.
- Drop debug print.

* Thu Jul 14 2011 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1
- Requre alterator-lookout.
- Make slideshow configurable.

* Mon Jul 11 2011 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt4
- Set 30 seconds interval between slides like CentOS (closes: #25776)

* Wed Apr 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.5.1-alt3
- more manifest cleaning

* Thu Mar 31 2011 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt2
- Fix crash on size calculate error

* Fri Feb 25 2011 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt1
- Fix ignore of auto dependence selection
- Unable to continue if there is package confilct

* Mon Jan 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.5-alt1
- prepkg.d hooks dir introduced

* Thu Jan 27 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.2-alt1
- Fix crash on unknown package name in dependence list (closes #24228)

* Mon Jan 17 2011 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt2
- Add Ukrainian module name translation (thanks Roman Savochenko)

* Fri Jul 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.4.1-alt1
- default cdrom dev for fstab changed to /dev/sr0

* Tue Jul 13 2010 Andrey Cherepanov <cas@altlinux.org> 2.4-alt5
- fix dependency on alterator-lookout

* Tue Jul 13 2010 Andrey Cherepanov <cas@altlinux.org> 2.4-alt4
- initial dependence check
- sort .directory file by name in backend for group order control

* Fri Jul 09 2010 Andrey Cherepanov <cas@altlinux.org> 2.4-alt3
- support depended item (checked with current one)
- fix right checked signal

* Thu Jul 01 2010 Andrey Cherepanov <cas@altlinux.org> 2.4-alt2
- fix crash on install on next step
- simplify group selection (closes: #19611)

* Tue Jun 22 2010 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- support tree hierarchy for groups

* Tue Dec 08 2009 Sergey V Turchin <zerg at altlinux dot org> 2.3-alt1.1
- pull nails from slideshow size

* Mon Dec 07 2009 Stanislav Ievlev <inger@altlinux.org> 2.3-alt1
- allow unattended install (sbolshakov@)

* Thu Nov 26 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt5
- fix typo in pkg-groups backend

* Thu Nov 12 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt4
- pkg-groups backend: alterator_api_version=1.
- replace obsolete simple_quote with string_quote.

* Wed Sep 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.2-alt3
- always make /media/cdrom and put it into fstab

* Thu Aug 27 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt2
- pkg-init: mark newly installed system to notify installer's postinstall.d hooks

* Fri Aug 07 2009 Stanislav Ievlev <inger@altlinux.org> 2.2-alt1
- remove unused pkg-register and pkg-profiles
- improve pkg-sources:
  * fix uri handling
  * use workflow none
  * use modern form API

* Thu Jul 30 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt12
- split installation set into base and additional to minimize memory usage

* Fri May 22 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt11
- fix installation size displaying

* Thu May 07 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt10
- disable button 'previous' (closes: #19814)
- add pkg-preinstall.d hook (closes: #19814)
- translate size units (closes: #19504)
- little ui improvements (closes: #19608)

* Wed Apr 15 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt9
- fix name of default apt component

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt8
- backend3/pkg-install: Forward apt-get messages to stderr.

* Wed Apr 08 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt7
- little improvements in ajax code

* Thu Apr 02 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt6
- pkg-sources: little ui improvements (fix typo, add margin)
- pkg-groups: improve backend work with nonexistent or empty groups directory

* Tue Mar 24 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt5
- normalize sources lists after synaptic work
- more information for users when apt loading package information

* Tue Mar 17 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt4
- improve postinstall and initinstall scripts

* Fri Feb 27 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt3
- add slideshow

* Tue Feb 17 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt2
- improve pkg-sources ui: replace magic url with ajax button

* Tue Feb 10 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- use repository database from apt-conf
- use translations directly from alterator-l10n

* Thu Jan 22 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- update some backends up to alterator_api_version = 1
- use help directly from alterator-l10n

* Wed Jan 21 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- add support for chroot initialization and basesystem installation

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt6
- rebuild with new l10n

* Mon Nov 24 2008 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt5
- add new help

* Thu Nov 13 2008 Stanislav Ievlev <inger@altlinux.org> 1.5-alt4
- fix http ui work in non javascript mode

* Mon Sep 22 2008 Stanislav Ievlev <inger@altlinux.org> 1.5-alt3
- fix buildarch: package contains arch depended configs for pkg-sources

* Fri Aug 29 2008 Stanislav Ievlev <inger@altlinux.org> 1.5-alt2
- use empty redirect-url attribute instead of name-attribute hack

* Wed Aug 06 2008 Stanislav Ievlev <inger@altlinux.org> 1.5-alt1
- replace alterator-read-desktop and own library with alterator-dump-desktop

* Thu Jul 24 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt8
- replace desktop.awk with alterator-read-desktop

* Tue Jul 01 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt7
- simplify i18n declarations

* Mon Jun 23 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt6
- use effectShow
- remove requires for alterator-notes

* Wed Jun 18 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt5
- fix default repository calculation

* Mon Jun 16 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt4
- resurrect html ui
- add @version@ parameter
- use single column listbox

* Wed Jun 11 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt3
- fix backend: add empty url

* Wed Jun 11 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt2
- update translations
- use single module.mak

* Wed Jun 11 2008 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1
- rewrite pkg-sources ui (qt)
- finally remove /pkg/license

* Tue Jun 10 2008 Stanislav Ievlev <inger@altlinux.org> 1.3-alt2
- remove support for groups with licenses

* Fri Jun 06 2008 Stanislav Ievlev <inger@altlinux.org> 1.3-alt1
- replace old checklist with common checklistbox

* Fri May 30 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt2
- use own checklist widget description
- improve tempfile cleanup
- finally rename /pkg -> /pkg/groups
- join to common translation database

* Thu May 22 2008 Stanislav Ievlev <inger@altlinux.org> 1.2-alt1
- rename /pkg -> /pkg/groups
- add help for pkg-groups
- remove autoinstall backend usage

* Tue Apr 29 2008 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- update for new case-form algo
- improve ui files layout
- improve ui according alterator HIG
- drop tools subpackage

* Thu Apr 10 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt2
- fix checkbox usage
- add preinstall.d script
- remove html-messages.mak usage

* Mon Mar 31 2008 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- add 'System updates' dialog
- update sources: reorder operations

* Fri Mar 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- improve "disk size" label text
- update for latest alterator-notes
- remove template-*
- pkg-sources: imrpove sorting
- move images to design package

* Tue Feb 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- use alterator-sh-functions
- resurrect apt-sources (both gui and html versions)
- pkg-sources: fix regexp, remove support for cdrom and rpm-src
- pkg-register: it's possible to add disk without pkg-groups.tar
- add separate pkg-register ui for cdrom discs

* Thu Jan 31 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- improve pkg-install and pkg-size backends

* Tue Jan 22 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- pkg-install backend: remove extra wait call
- pkg-groups backend: add support for translation fallback
- add support for license

* Fri Dec 14 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- save error-text during cdrom exchange

* Tue Dec 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- improve disk checking

* Thu Dec 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- always umount
- fix label for the latest browser-qt

* Thu Dec 06 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- register: fix autoskip

* Wed Dec 05 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- add 'Additional disks' step
- improve translation for 'Insert CD' dialog

* Fri Nov 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add support for media change request

* Thu Nov 08 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- use different namespaces for the apt start/stop 
  notifications to avoid a race between to steps in wizard

* Fri Oct 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2.1
- git-add doc

* Fri Oct 26 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- fix requires
- add documentation

* Tue Oct 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
