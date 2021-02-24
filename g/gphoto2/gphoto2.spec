Name: gphoto2
Version: 2.5.26
Release: alt1

Group: Graphics
Summary: Command line utilities to access digital cameras
Summary (ru_RU.UTF-8): Консольные программы для обмена данными с цифровыми фотоаппаратами
Url: http://www.gphoto.org/
License: GPLv2+
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

# Automatically added by buildreq on Mon Oct 11 2010
BuildRequires: aalib-devel libX11-devel libgphoto2-devel libgpm-devel libjpeg-devel libpopt-devel libreadline-devel libslang-devel

# Url for source code downloads now http://sourceforge.net/project/showfiles.php?group_id=8874
Source0: %name-%version.tar

%description
gPhoto is part of the GNU project - and is an universal, free
application and library framework that lets you download
images from several different digital camera models, including
the newer models with USB connnection. Note that for some older
camera models you must use the old gphoto package.

This package contains command-line gphoto2 client.

##### TRANSLATED DESCRIPTIONS  #####

%description -l ru_RU.UTF-8
gPhoto - универсальный комплект программ и библиотек, позволяющий
копировать на жёсткий диск снимки сделанные разными моделями цифровых
фотоаппаратов, в том числе новыми аппаратами с USB интерфейсом.
Обратите внимание, что с некоторыми старыми моделями необходимо
использовать старую программу gphoto.

%prep
%setup -n %name-%version

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install
/bin/cp {AUTHORS,NEWS,README} %buildroot%_datadir/doc/%name/
%find_lang --output=%name.lang %name

##### FILE LISTS FOR ALL BINARY PACKAGES #####

%files -f %name.lang
%_bindir/%name
%_man1dir/%{name}*
%dir %_datadir/doc/%name
%_datadir/doc/%name

%changelog
* Thu Oct 15 2020 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.26-alt1
- 2.5.26

* Thu Jul 25 2019 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.23-alt1
- 2.5.23

* Sun Oct 28 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.20-alt1
- 2.5.20

* Sat Apr 21 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.17-alt1
- 2.5.17

* Sun Mar 11 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.15-alt1
- 2.5.15

* Sat Aug 05 2017 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.14-alt1
- 2.5.14

* Sun Dec 18 2016 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.11-alt1
- 2.5.11

* Fri Mar 18 2016 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.9-alt1
- 2.5.9

* Mon Jul 06 2015 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.8-alt1
- 2.5.8

* Tue Mar 17 2015 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.6-alt2
- removed hard require on libgphoto2

* Tue Jan 27 2015 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.6-alt1
- 2.5.6

* Mon Oct 06 2014 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.5-alt1
- 2.5.5

* Mon Apr 07 2014 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.4-alt1
- 2.5.4

* Fri Jan 31 2014 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.3-alt1
- 2.5.3

* Sun Jun 23 2013 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.2-alt1
- 2.5.2

* Mon Feb 11 2013 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.1-alt1
- 2.5.1

* Sun Nov 04 2012 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.0-alt1
- 2.5.0

* Wed Apr 25 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.14-alt1
- 2.4.14

* Sun Dec 18 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.11-alt2
- rebuilt for fix RPATH issue
- fixed requires

* Sat Aug 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.11-alt1
- 2.4.11

* Tue Oct 12 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.10-alt2
- removed libgphoto2, it's now packaged separately

* Tue Aug 17 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.10-alt1
- 2.4.10

* Tue Mar 23 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Mon Oct 19 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.7-alt2
- removed unneeded symlink and provides

* Sat Aug 22 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.7-alt1
- 2.4.7
- removed unneeded timeout
- added usb id for Canon PowerShot A580

* Sun May 17 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.5-alt3
- added timeout into script check-ptp-camera

* Sun May 10 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.5-alt2
- increased max number of entries in the camera list (ALT #19752)

* Sat Apr 18 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.5-alt1
- 2.4.5
- updated build requires

* Sun Mar 29 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.4-alt1
- 2.4.4
- dropped unnecessary patch
- updated build requires
- changed the means of creating additional provides

* Sun Dec 07 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.3-alt2
- removed obsolete post{,un}_ldconfig calls

* Tue Oct 28 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Wed Sep 24 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.2-alt2
- added patch for compatibility with libusb-1 API (fix bug #17264, thanks to ab@)

* Wed Aug 27 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.2-alt1
- 2.4.2
- updated BuildRequires
- soname changed back to lib%name.so.2 (#16542) and saved so.6 for
  compatibility with previous build (thanks to eostapets@ and rider@)
- returned russian summaries and descriptions from slava@

* Sat May 24 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt2.svn10945
- moved HAL support into lib%name, lib%name-hal has deleted
- changed postinstall script (#15548)

* Thu May 22 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt1.svn10945
- hal supported (#15547, added lib%name-hal subpackage)
- perfected location of docs

* Wed Mar 26 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt0.svn10945.3
- removed *.la files

* Sun Mar 23 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt0.svn10945.2
- switched back to build with separate source code tarballs
- disabled build hotplug subpackage
- corrected content of doc. directory
- turn back requires = %%version-%%release for %name
- build with included .la files

* Sun Mar 09 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt0.svn10945.1
- updated version to 2.4.0
- svn snapshot 10945
- drop unneeded patches
- fixed bug #13823

* Mon Nov 19 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt7
- add Fuji FinePix S5700 (patch backported from svn commit 10728)
- russian summary and description removed
- license tags changed to GPLv2+ and LGPLv2+

* Sat Sep 22 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt6
- add Canon PowerShot A450 (patch from svn)
- change alt-fix-rules.patch
- enabled check ptp camera for unknown cameras

* Tue Jun 05 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt5
- disable Canon fast directory retrieval (even so patch2 imported from SVN)
- bzip ChangeLog
- added tag License into lib%name-hotplug

* Sat May 26 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt4.10
- renamed patch1
- fix fast directory retrieval on Canon PowerShot A430

* Sun Mar 11 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt4
- fix requires
- move creating udev rules back into lib%name package

* Mon Jan 29 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt3
- Requires: hotplug removed from libgphoto2 package (#10695)
- udev and hotplug communications moved into separate packages

* Fri Jan 19 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt2
- used builtin generator udev and hotplug rules

* Tue Jan 16 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt1
- new version
- renamed and little corrected udev rules
  (use udev >= 0.98)

* Sun Jan 14 2007 Alexey Morsov <swi@altlinux.ru> 2.3.0-alt2.1
- Add udev rules (fix bug #10661)
- change Packager

* Fri Dec 29 2006 Alexey Morsov <swi@altlinux.ru> 2.3.0-alt2
- NMU

* Fri Dec 08 2006 Alexey Morozov <morozov@altlinux.org> 2.3.0-alt1
- New version (2.3.0)
- static libraries made optional and skipped by default
- buildreqs cleanup
- switched to gphoto-suite for builds
- dropped obsoleted Nikon-4600-ptp-Support.c.patch (#0)

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.6-alt2.1
- Rebuilt with libreadline.so.5.

* Thu Nov 24 2005 Anton Farygin <rider@altlinux.ru> 2.1.6-alt2
- NMU:
    - updated to new version
    - removed included to mainstream pathes
    - added Nikon 4600 autodetect
    - added firsttime.d script
    - fixed postscript for use DURING_INSTALL

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1.1
- rebuild against libexif.so.12.
- removed hostinfo, libgphoto2-devel from BuildRequires.

* Sat Jan 01 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.5-alt1
- 2.1.5
- partial Russian translation
- i18n fix

* Wed Jun 23 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.4-alt3
- no update-usb.usermap call in postinstall script

* Tue Jun 08 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.4-alt2
- usbcam.group replaced by usbcam.console. Group camera removed.

* Sat Feb 21 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Fri Dec 12 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.2-alt2
- .la removed

* Tue Sep 16 2003 Sergey V Turchin <zerg at altlinux dot org> 2.1.2-alt1
- new version
- some spec cleanup
- fix requires

* Sat Aug 23 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.1-alt0.7
- Serial fix

* Sun Jun 15 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.1-alt0.6
- libgphoto2 requirements fix (hotplug).

* Wed May 28 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.1-alt0.5
- non-root execution (all users in group 'camera' can now use gphoto2)

* Wed Apr 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt0.4
- russian descriptions (slava).

* Wed Apr 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt0.3
- more improvements.
- build with new libexif.

* Sun Mar 30 2003 ZerG <zerg@altlinux.ru> 2.1.1-alt0.2
- new version
- improve spec

* Wed Oct 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.1.0-alt1
- Rebuilt in new environment
- Rebuilt with liblockdev
- Some spec fixes
- 2.1.0

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0-alt2
- Rebuild with new binutils

* Fri Mar 01 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0-alt1
- Release %name 2.0

* Thu Dec 06 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.0-alt0.3cvs20011204
- Build from CVS
- Rebuild with new libusb

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.0-alt0.2beta1
- Added devel-static package
- Some spec cleanup
- Fixed filelists

* Fri Aug 23 2001 Rider <rider@altlinux.ru> 2.0-alt0.1beta1
- first BUILD for ALT
