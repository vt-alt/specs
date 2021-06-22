Name: alterator-netinst
Version: 1.9.1
Release: alt4

Source:%name-%version.tar

Summary: alterator module for network installations management
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.11-alt1
Requires: alterator-l10n >= 2.7-alt5
Requires: tftp-server nfs-server
Requires: syslinux-data
Requires: alterator-net-iptables >= 1.6

Conflicts: alterator-fbi < 5.19-alt4
Conflicts: alterator-dhcp < 0.5-alt4

BuildArch: noarch

BuildPreReq: alterator >= 4.11-alt1


%description
alterator module for network installations management

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%_datadir/alterator/applications/*
%_bindir/alterator-netinst

%changelog
* Tue Jun 08 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.9.1-alt4
- Copy /boot from new images to syslinux directory.
- Remove user menu.
- Copy pxelinux.0 from image if exists.

* Mon Aug 27 2018 Paul Wolneykien <manowar@altlinux.org> 1.9.1-alt3
- Make the package noarch again depending on syslinux-data.

* Mon Aug 27 2018 Paul Wolneykien <manowar@altlinux.org> 1.9.1-alt2
- Build exclusively for x86 (due to syslinux).

* Mon Aug 20 2018 Paul Wolneykien <manowar@altlinux.org> 1.9.1-alt1
- Restrict the "image" parameter to integer type.
- Download files as the unprivileged user "nobody".

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 1.9.0-alt3
- Do not delete all of the pxelinux.cfg

* Wed Oct 09 2013 Fr. Br. George <george@altlinux.ru> 1.9.0-alt2
- Add translation anchors

* Wed Oct 02 2013 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Implement pxelinux.cfg/default label selection

* Fri Nov 09 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.9-alt1
- workaround for mount bug: udf mages are not supported now

* Thu Oct 13 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.8-alt1
- blocksize for cdrom fixed

* Wed Sep 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.7-alt1
- add 'krb5' option for all boot types

* Thu Sep 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.6-alt3
- fix gonfig generation when 'ui' syslinux style is used

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.6-alt2
- get image from cdrom fixed

* Fri Jun 10 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.6-alt1
- add to live 'krb5' option if SERVER_ROLE=master

* Wed Mar 02 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.5-alt4
- fix lang setting
- revert using mounted image (impossible to change image when used)

* Tue Mar 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.5-alt3
- set default to live if no 'label linux' found

* Mon Feb 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.5-alt2
- lang added to kernel command line
- use directory with mounted image instead of image

* Mon Nov 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.5-alt1
- size calculation fixed (closes #23516)

* Mon Nov 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.4-alt2
- default boot fixed

* Mon Sep 20 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.4-alt1
- isolinux cooking fixed
- dependensy on nfs-server added

* Fri Apr 09 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.3-alt1
- VNC setup improvments
- translations

* Fri Apr 09 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.2-alt1
- fetch from cdrom fixed

* Thu Apr 08 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8.1-alt1
- no /dev/cdrom now. Using HAL :(

* Wed Mar 24 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8-alt1
- installation via VNC setup

* Tue Oct 13 2009 Stanislav Ievlev <inger@altlinux.org> 1.7-alt3
- alterator-netinst: always print parameters, even for nonexistent images

* Fri Sep 25 2009 Stanislav Ievlev <inger@altlinux.org> 1.7-alt2
- wait ui: resurrect url printing

* Tue Sep 22 2009 Stanislav Ievlev <inger@altlinux.org> 1.7-alt1
- ui:
    * use workflow 'none' (closes: #21649)
    * use modern effects library,
    * improve progress style
- backend:
   * improve localization
   * improve error handling

* Fri Aug 07 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.6-alt2.1
- compatibility with syslinux 3.63 

* Wed Apr 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt2
- fix symlink dereferencing in DATADIR

* Wed Apr 29 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.6-alt1
- add timezone from /etc/sysconfig/clock to kernel parameter 'tz'
  in syslinux config

* Mon Apr 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt1
- alterator-netinst
  + fix problems with non-existent DATADIR
  + don't use getopt (we always work with single option)

* Thu Apr 23 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.4-alt1
- fix handling of downloading stop - 3
- add ajax progress (by inger@)

* Tue Apr 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt2
- fix handling of downloading stop - 2

* Tue Apr 21 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- fix handling of downloading stop

* Wed Apr 15 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
- dereference symlinks in DATADIR

* Thu Apr 09 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- improve messages

* Wed Apr 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- getting images from CD-ROM

* Wed Apr 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.8-alt1
- update desktop translations
- move to Categories=X-Alterator-Servers

* Fri Mar 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- little interface improvements
- relocate datadir to /srv/public

* Wed Mar 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt1
- update translation in desktop-file
- don't run umount if it is not needed

* Tue Mar 10 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.6-alt1
- alterator-netinst script:
  + change error handling on empty url
  + do not set interface in pxelinux.cfg

* Thu Mar 05 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- alterator-netinst script:
  + add fstab entry for /srv/netinst/mnt

* Thu Mar 05 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt1
- alterator-netinst script:
  + change pxelinux.cfg: timeout=100, add interface=eth0 in section linux,
    add sections eth{1,2,3} with interface=eth{1,2,3}
  + add DHCP setup

* Wed Mar 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- alterator-netinst script:
  + fix error in downloader
  + small fix in -D action
  + fix help

* Tue Mar 03 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt1
- alterator-netinst:
  + fix kernel parameters for propagator;
  + update help
  + show downloading errors

* Tue Feb 17 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt1
- first version

