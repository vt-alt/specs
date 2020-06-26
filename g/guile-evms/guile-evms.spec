Name: guile-evms
Version: 0.6
Release: alt1

Summary: Guile bindings for EVMS
License: GPLv2
Group: Development/Scheme

BuildRequires: guile-devel >= 2.0 libblkid-devel libe2fs-devel libevms-devel swig >= 3.0.12-alt2

Source: %name-%version-%release.tar

%description
Guile bindings for EVMS, volume management library
http://evms.sourceforge.net

%define guile_sodir %(guile-config info extensiondir)
%define guile_godir %(guile-config info siteccachedir)

%set_gcc_version 8

%prep
%setup

%build
make

%install
make install DESTDIR=%buildroot

%files
%guile_sodir/libguile-evms.so
%guile_godir/evms.go

%changelog
* Tue Jun 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt1
- disallow reassign /boot/efi on another fat partition
- do not propose /mnt/disk as default mountpoint for fat/ntfs

* Thu Dec 05 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt12
- fixed crash in alterator-vm (closes: #37572)

* Tue Dec 03 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt11
- fix FTBFS with gcc9

* Thu Jul 11 2019 Alexey Shabalin <shaba@altlinux.org> 0.5-alt10
- Add /var/lib/docker,/var/lib/lxd,/var/lib/libvirt/images to well-known-mountpoints

* Wed Jun 05 2019 Rustem Bapin <rbapin@altlinux.org> 0.5-alt9
- Fixed build on mipsel architecture.

* Thu Apr 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5-alt8
- Fixed build on ppc64le architecture.

* Tue Jul 31 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt7
- require guile >= 2.0 for build

* Tue Jan 16 2018 Paul Wolneykien <manowar@altlinux.org> 0.5-alt6
- Adapt for the E2K arch build.

* Thu Apr 27 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt5
- fixed crash in alterator-vm (closes: #33401)

* Wed Apr 26 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt4
- reswig with fixed exception wrapper

* Thu Apr 20 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt3
- sporadic fix for random crashes, hopefully (closes: #33401)

* Thu Apr 20 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt2
- fix empty option value typemap

* Wed Mar 29 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5-alt1
- rebuilt with guile-2.2

* Tue Dec 13 2016 Michael Shigorin <mike@altlinux.org> 0.4-alt17
- added /tmp to well-known mountpoints (to avoid default "noexec"
  which breaks 50-initrd trying to run make-initrd there)

* Wed Nov 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt16
- the dangerous use of an implicit declaration replaced by current guile API

* Wed Nov 16 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt15
- do not treat as error nonexistent device during BLKRRPART

* Tue Feb 05 2013 Michael Shigorin <mike@altlinux.org> 0.4-alt14
- don't suggest to mkfs /boot/efi (see also #28163)

* Wed Nov 21 2012 Michael Shigorin <mike@altlinux.org> 0.4-alt13
- initial EFI support draft (closes: #27979)

* Wed Nov 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt12
- adapted for recent swig

* Thu Jul 07 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt11
- revert back to pre-alt10 state (#25774, #25861)

* Tue Jun 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt10
- no more mkswap on already existing swap partition (#25774)

* Thu May 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt9
- recognize btrfs plugin as fsim

* Tue Sep 21 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt8
- allow / on lvm (#23801)

* Mon Dec 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt7
- buildreqs fixed

* Wed Jun 17 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt6
- offer `relatime' mount option by default

* Mon Jun  1 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt4
- disallow "/" and "/boot" placement on LVM (#19805, #19807)

* Sun Apr 12 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt3
- fix regression around swapon invocation (#19555, #19556)

* Wed Apr  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt2
- added swapon invocation at final stage

* Tue Dec  9 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- rebuilt with guile 1.8

* Fri Jul 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt12
- added missing comma in ntfs mount options string, closes \#12378

* Thu Jul 12 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt11
- changed ntfs mount options to ntfs-3g

* Wed May 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt10
- fixed vfat mount options, closes \#11821

* Tue Apr  3 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt9
- offer sane mount point & options for fat/ntfs
- added /opt to well-known mountpoints
- do not format /opt & /usr/local by default
- set default 1 for fstab's fs_freq
- do not rely on uncertain libblkid in swap case

* Fri Mar 30 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt8
- clear memoised object/plugin pool before engine open

* Mon Mar 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt7
- fixed handling of empty/nonexistent drive model
- do not force mkfs on "/home" or "/mnt/..." by default
- offer sane defaults for well-known mount point options

* Fri Mar  9 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt6
- attached context to task procs
- made inactive `check order' option

* Thu Mar  1 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt5
- fixed hang on sysfs read, \#10953

* Thu Feb 22 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt4
- fixed blkrrpart on cciss/rd devices
- revert to old value when setmntent cancelled
- disk model getter added
- be stricter on acceptable mountpoints

* Thu Feb  8 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt3
- fstab order fixed

* Tue Jan 30 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt2
- do not try to mount swaps
- fixup incorrectly assigned mntpass values

* Fri Jan 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- workaround UUID inconsistency between evms volume and bottomed partition

* Fri Dec 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt8
- installer mode: force mkfs during finalize in certain cases

* Tue Dec 19 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt7
- only `mount options' for swap
- dump all swaps into fstab
- reread partition table of each disk at exit

* Tue Dec 12 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt6
- reset possibly assigned mountpoint on fsim removal
- validate mountpoints

* Tue Dec  5 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt5
- assume swapfs as fsim
- do not expose evms names on compat volumes, if possible

* Wed Nov 29 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt4
- mount at exit all assigned volumes when in installer mode

* Mon Nov 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt3
- added wrappers for getmntent() and blkid_get_tag_value()

* Tue Nov  7 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- raise exception on unsuccessful option value setting

* Mon Oct 23 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- added task-like interface to mount-related ops
- storage names mangled to prevent clashes with alterator's naming scheme

* Mon Oct  2 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- Initial build.
