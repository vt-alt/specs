Name: AcetoneISO2
Version: 2.4
Release: alt1

Summary: CD/DVD Image Manipulator

Group: Archiving/Other
License: GPLv3
Url: http://www.acetoneteam.org/

Packager: Anatoly Lyutin <vostok@altlinux.org>

Source: %name-%version.tar

Patch0: AcetoneISO2-2.0.3-no-poweriso-for-non-x86.patch
Patch1: acetoneiso2-2.1.1-install.patch
Patch2: acetoneiso2-2.1.1-pro.patch

Provides: acetoneiso2
Obsoletes: acetoneiso2

BuildRequires: gcc-c++ libqt4-devel

Requires: fuseiso

%description
AcetoneISO2: The CD/DVD image manipulator for Linux, it can do the following:
- Mount automatically ISO, MDF, NRG, BIN, NRG without the need to insert
  admin password! Only single-track images are supported for the moment.
- a native utility to blank your CD-RW, DVD-RW and DVD-RW discs
- A nice display which shows current images mounted and possibility to
  click on it to quickly reopen mounted image
- Convert 2 ISO all image types:
  *.bin *.mdf *.nrg *.img *.daa *.dmg *.cdi *.b5i *.bwi *.pdi and much more
- Extract images content to a folder:
  *.bin *.mdf *.nrg *.img *.daa *.dmg *.cdi *.b5i *.bwi *.pdi and much more
- Play a DVD Movie Image with Kaffeine / VLC / SMplayer with auto-cover download
  from Amazon
- Generate an ISO from a Folder or CD/DVD
- Check MD5 file of an image and/or generate it to a text file
- Calculate ShaSums of images in 128, 256 and 384 bit
- Encrypt / Decrypt an image
- Split / Merge image in X megabyte
- Compress with High Ratio an image in 7z format
- Rip a PSX cd to *.bin to make it work with epsxe/psx emulators
- Restore a lost CUE file of *.bin *.img
- Convert Mac OS *.dmg to a mountable image
- El-Torito support to create ISO bootable Cd
- Mount an image in a specified folder from the user
- Create a database of images to manage big collections
- Extract the Boot Image file of a CD/DVD or ISO
- Backup a CD-Audio to a *.bin image
- Complete localization for different languages!
- Quick and simple utility to Rip a DVD to Xvid AVI
- Quick and simple utility to convert a generic video (avi, mpeg, mov, wmv, asf)
  to Xvid AVI
- Quick and simple utility to convert a FLV video to AVI
- Utility to download videos from Youtube and Metacafe!
- Extract Audio from a video file
- Extract a *.rar archive that has a password
- Quick and simple utility to convert any video for Sony PSP Playstation Portable
- Display History that shows all images you mount in time

%prep
%setup
%patch0 -p0
%patch1 -p2
%patch2 -p2

# Fix perms
chmod -x acetoneiso/sources/*

%build
pushd acetoneiso
qmake-qt4
%make_build
popd

%install
pushd acetoneiso
make INSTALL_ROOT=%buildroot install

#icon
%__install -pD -m644 images/Acetino2.png %buildroot%_iconsdir/Acetino2.png
popd

%files
%doc AUTHORS CHANGELOG FEATURES LICENSE README TODO
%_bindir/acetoneiso
%_desktopdir/AcetoneISO.desktop
%_iconsdir/Acetino2.png

%changelog
* Thu Mar 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.4-alt1
- Build new version (Closes: #38070).

* Mon Jun 04 2018 Grigory Ustinov <grenka@altlinux.org> 2.3-alt2
- Fix extra large icon in menu (Closes: #33482).

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 15 2010 Anatoly Lyutin <vostok@altlinux.org> 2.3-alt1
- 2.3
- Added in requires fuseiso (ALT #24751)

* Fri Jul 09 2010 Anatoly Lyutin <vostok@altlinux.org> 2.2.2-alt1
- 2.2.2

* Thu Nov 26 2009 Anatoly Lyutin <vostok@altlinux.org> 2.2.1-alt3
- fix Exec key in desktop file

* Tue Nov 24 2009 Anatoly Lyutin <vostok@altlinux.org> 2.2.1-alt2
- closes: # 22307

* Thu Nov 12 2009 Anatoly Lyutin <vostok@altlinux.org> 2.2.1-alt1
- 2.2.1

* Tue Nov 10 2009 Anatoly Lyutin <vostok@altlinux.org> 2.1.1-alt2
- fixed icon place
- fixed desktop file

* Tue Oct 06 2009 Anatoly Lyutin <vostok@altlinux.org> 2.1.1-alt1
- 2.1.1

* Thu Jul 30 2009 Anatoly Lyutin <vostok@altlinux.org> 2.0.3.2-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.2-2
- forgot to tag some files

* Thu Jul 23 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.2-1
- update to 2.0.3.2

* Wed Jul  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3.1-1
- update to 2.0.3.1

* Thu Apr  9 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3-1
- update to 2.0.3 final

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-0.2.RC1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.3-0.1.RC1
- 2.0.3RC1

* Tue May 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.2-4
- only try to use PowerISO as a converter on x86 platforms (bz 447214)

* Fri May  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.2-3
- actually apply patch2
- get rid of requires on nautilus, this application works fine without it,
  it is simply enhanced by the presense of nautilus/konqueror

* Fri May  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.2-2
- fix requires, get rid of kdebase, cdrecord, k3b, xbiso, arts
- add requires on nautilus (really, it should be nautilus or konqueror,
  but there is no good way to do that)

* Wed May  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.2-1
- 2.0.2

* Wed Apr  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.1-2
- remove "Application" from desktop file (inside patch)

* Fri Apr  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.1-1
- 2.0.1

* Thu Nov  8 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.96-1
- initial build for Fedora
