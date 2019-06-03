%define base_name design-bootloader

Name: %base_name-source
Version: 7.2
Release: alt3

Group: Graphics
Summary: Graphical boot logo sources
License: GPL

BuildArch: noarch

BuildRequires: perl-Encode

Source: %name-%version.tar

Obsoletes: design-bootloader-installer-source  design-bootloader-livecd-source  design-bootloader-system-source

Conflicts: fonts-ttf-droid <= 1.0-alt1

%description
Sources of macros for generating graphical boot logo. Needed for building packages design-bootloader-{distro}


%prep
%setup

%install
mkdir -p %buildroot/usr/src/%base_name-source
cp -a * %buildroot/usr/src/%base_name-source


%files -n %base_name-source
/usr/src/%base_name-source

%changelog
* Sun Jun 02 2019 Anton Midyukov <antohami@altlinux.org> 7.2-alt3
- Fixed russian translation (closes: #36840)

* Mon Apr 24 2017 Oleg Solovyov <mcpain@altlinux.org> 7.2-alt2
- Fixed exiting message translation

* Wed Dec 02 2015 Aleksey Avdeev <solo@altlinux.org> 7.2-alt1
- Fix use 'defined(%hash)' (for perl 5.22)

* Thu Apr 02 2015 Mikhail Efremov <sem@altlinux.org> 7.1-alt1
- Fix Droid fonts path.

* Tue Feb 11 2014 Michael Shigorin <mike@altlinux.org> 7.0-alt1
- updated Spanish, Portuguese and Tatar translations
  to fix the order broken by adding a few entries
  in the middle of already existing ones

* Fri Mar 22 2013 Michael Shigorin <mike@altlinux.org> 6.9-alt1
- added Kazakh translation by Baurzhan Muftakhidinov (closes: #28715)

* Mon Nov 19 2012 Sergey V Turchin <zerg@altlinux.org> 6.0-alt6
- fix detect isohybrid image booted as disk

* Mon Sep 10 2012 Andrey Cherepanov <cas@altlinux.org> 6.0-alt5
- Language item should be in English because it's one way to change
  language for English-speaking people

* Mon Feb 13 2012 Andriy Stepanov <stanv@altlinux.ru> 6.0-alt4
- Addedd altlinux entry

* Sat Sep 17 2011 Radik Usupov <radik@altlinux.org> 6.0-alt3
- Added tt language (by ainur@)

* Tue Aug 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt2
- autoinstall label translation from timon4@

* Fri Jul 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 6.0-alt1
- fix default install source when isohybrid image booted as disk
  with syslinux 3.86 -- zerg@
- add "removable" boot item possibility -- zerg@

* Mon Jun 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt8
- uk translation for automatcic videomode added

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt7
- fixed ramdisk_size deleted

* Mon Jun 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt6
- automatic 800x600 in virtualbox

* Thu May 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt5
- kroete animation removed

* Sat May 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt4
- don't set vga= by default

* Thu Nov 18 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt3
- label:ALT* added to defaul disk parameters

* Mon Aug 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt2
- more fonts added

* Tue May 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.9-alt1
- installation media autoselection

* Mon Oct 12 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt21
- fixed installation in english

* Wed Sep 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt20
- labels in installation type fixed

* Fri May 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt19
- beep turned off

* Mon Apr 20 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt18.1
- languages menu in LILO fixed

* Fri Apr 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt18
- translations for txt_session fixed

* Fri Apr 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt17
- languages menu fixed

* Mon Apr 06 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt16
- es_ES added to languages
- fkey_kernelopts defined

* Fri Apr 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt15
- help for kernelopts from cas@

* Thu Apr 02 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt14
- Spanish language added
- translations fixes

* Tue Mar 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt13
- 1024x768 really disabled

* Wed Feb 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt12
- 1024x768 disabled

* Tue Feb 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt11
- 1024x768 enabled
- really build font

* Wed Feb 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt10
- added 'lang' and 'splash' to list of kernel options with defaults

* Mon Feb 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt9
- fixed /boot/splash/message oversize

* Fri Feb 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt8
- default languages list changed

* Fri Feb 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt7
- merged additions from stanv@

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt6
- merged translations from cas@

* Fri Jan 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt5
- removed 'openSUSE' from LiveCD label

* Thu Dec 25 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt4
- forced 800x600

* Thu Dec 25 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- install source selection fixed

* Mon Dec 15 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- animation, pinguins, driver update disabled

* Wed Nov 12 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- completly new code from suse

* Fri Apr 04 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.0-alt2
- merged translations from cas@

* Fri Mar 28 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.1.0-alt1
- porting SuSe two-line menus

* Wed Nov 14 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.6.1
- fixed typos in help

* Thu Aug 16 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.6.0
- separating package on source and designs

* Tue Aug 14 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.5.5
- color and size of titlebars in desktop changed

* Fri Aug 10 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.5.4
- Name of distribution on graphics changed

* Mon Aug 06 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.5.3
- set ramdisk_size=65535

* Wed Jul 18 2007 Dmitry V. Levin <ldv@altlinux.org> 4.0.0-alt0.5.2
- Set default language to "ru_RU".
- Always propagate language to cmdline.

* Tue Jul 10 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.5.1
- pinguns disabled

* Mon Jul 02 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.5.0
- split to installer/livecd/system

* Thu Jun 28 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.4.7
- fonts changed to DevaVuSans 16

* Tue Jun 26 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.4.6
- added design for desktop

* Tue Jun 05 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.4.5
- language changed to country, added titles to menus

* Tue May 29 2007 Dmitry V. Levin <ldv@altlinux.org> 4.0.0-alt0.4.4.1
- Reverted default language change introduced in 4.0.0-alt0.4.3.

* Fri May 25 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.4.4
- added lang to dups clean list

* Wed May 23 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.4.3
- default language set to Russian, russian help rewritten

* Tue May 22 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0.0-alt0.4.2
- bootsplash resolution set to 800x600, vesa mode removed

* Mon Apr 23 2007 Dmitry V. Levin <ldv@altlinux.org> 4.0.0-alt0.4.1
- Removed backup files.
- Uncompressed tarballs.
- design-bootloader/common.inc: Passed vga=normal in text mode.
- design-bootloader/po (txt_text_mode): Renamed "Base" to "Base Mode".

* Thu Apr 19 2007 Sergey V Turchin <zerg at altlinux dot org> 4.0.0-alt0.4
- remove "Driver Update Disk" option
- rename "Text Mode" menu entry to "Base"

* Mon Apr 16 2007 Sergey V Turchin <zerg at altlinux dot org> 4.0.0-alt0.3
- add graphics for -server
- more split colors into desing themes

* Wed Apr 11 2007 Sergey V Turchin <zerg at altlinux dot org> 4.0.0-alt0.2
- cleanup uk help text; thanks gvy@alt

* Tue Apr 10 2007 Sergey V Turchin <zerg at altlinux dot org> 4.0.0-alt0.1
- cut design to separated tarballs
- cleanup en,ru help text
- bump version

* Tue Apr 03 2007 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt0.7
- don't cut leading '/' from networking directory

* Mon Mar 19 2007 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt0.6
- add Tatar and Kazakh to defualt languages list

* Wed Mar 14 2007 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt0.5
- set ramdisk_size=50000 for ftp/http install methods

* Fri Mar 09 2007 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt0.4
- fix default options to automatic=method:cdrom

* Fri Mar 02 2007 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt0.3
- fix "automatic" kernel options by F4
- turn off startup animation
- drop unused languages

* Thu Mar 01 2007 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt0.2
- change kernel options and menu for install method menu
- small graphics update

* Wed Dec 13 2006 Sergey V Turchin <zerg at altlinux dot org> 3.1.0-alt0.1
- testing variant of new format

* Tue Aug 09 2005 Anton D. Kachalov <mouse@altlinux.org> 2.9.8-alt1.1
- added x86_64 to BuildArch

* Mon Jun 27 2005 Anton Farygin <rider@altlinux.ru> 2.9.8-alt1
- belarusian translations added
- fixed #6664 (menu item down after keys from panel pressing)

* Tue Jun 07 2005 Anton Farygin <rider@altlinux.ru> 2.9.7-alt1
- updated translation

* Sat May 14 2005 Anton Farygin <rider@altlinux.ru> 2.9.6-alt1
- updated help and font for uk (#6829)

* Mon Apr 04 2005 Anton Farygin <rider@altlinux.ru> 2.9.4-alt1
- post scripts added

* Mon Apr 04 2005 Anton Farygin <rider@altlinux.ru> 2.9.3-alt1
- updated isolinux parameters

* Wed Mar 16 2005 Anton Farygin <rider@altlinux.ru> 2.9.2-alt1
- prepare for ALT Linux 3.0 Compact

* Thu Dec 23 2004 Anton Farygin <rider@altlinux.ru> 2.9.1-alt1
- prepare for next Master

* Tue Jun 15 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- updated for Master 2.4

* Wed Feb 12 2003 Stanislav Ievlev <inger@altlinux.ru> 2.2-alt1.1
- update boot picture

* Tue Feb 11 2003 Rider <rider@altlinux.ru> 2.2-alt1
- first build for ALT Linux

