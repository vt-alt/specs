Name: lilo
Version: 24.2
Release: alt2
Summary: The boot loader for Linux and other operating systems
License: MIT
Group: System/Kernel and hardware
Url: https://www.joonet.de/%name
Source0: %url/ftp/sources/%name-%version.tar
#Vcs-Git: https://salsa.debian.org/joowie-guest/upstream_lilo.git
Source1: keytab-lilo.c
Patch1: lilo-23.2-owl-makefile.patch
Patch2: lilo-23.2-alt-owl-fixes.patch
Patch3: lilo-24.2-alt-Makefile.patch
Patch11: lilo-23.0-mdk-part.patch
Patch12: lilo-24.2-alt-constants.patch
Patch13: lilo-23.1-alt-defaults.patch
Patch14: lilo-23.0-alt-lba32_linear.patch
Patch15: lilo-24.0-alt-mkrescue.patch
Patch17: lilo-24.2-alt-blkid.patch
Patch18: lilo-23.0-alt-raid_index.patch
Patch19: lilo-22.8-alt-devmapper.patch
Patch20: lilo-22.8-alt-md-devmapper.patch
Patch21: lilo-24.2-suse-gfx.patch
Patch22: lilo-24.0-alt-format.patch
ExclusiveArch: %ix86 x86_64

BuildRequires: dev86 libblkid-devel libdevmapper-devel perl(Pod/Text.pm) %_bindir/uudecode

%description
LILO (LInux LOader) is a basic system program which boots your Linux
system.  LILO loads the Linux kernel from a floppy or a hard drive, boots
the kernel and passes control of the system to the kernel.  LILO can also
boot other operating systems.


%package doc
Summary: More documentation for %name
Group: System/Kernel and hardware
BuildArch: noarch

%description doc
LILO (LInux LOader) is a basic system program which boots your Linux
system.  LILO loads the Linux kernel from a floppy or a hard drive, boots
the kernel and passes control of the system to the kernel.  LILO can also
boot other operating systems.

This package contains extra documentation for LILO.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch17 -p1
%patch18 -p1
#patch19 -p1
#patch20 -p1
%patch21 -p1
%patch22 -p1

sed -i 's/\(mkdir \)/\1-p /g' Makefile
sed -i 's/\(keytab-lilo\)\.pl/\1/g' Makefile doc/user.tex
sed -i '/^[[:blank:]]*@echo/d' images/Makefile


%build
%make_build CC=%__cc OPT="%optflags -Wno-strict-aliasing" all
%__cc %optflags -o keytab-lilo %SOURCE1
gzip -9c CHANGELOG > CHANGELOG.gz


%install
%make_install DESTDIR=%buildroot install

%define docdir %_docdir/%name-%version
install -d -m 0755 %buildroot%docdir/{html,images}
install -p -m 0644 NEWS README* CHANGELOG.* COPYING QuickInst TODO %buildroot%docdir/
install -p -m 0644 doc/html/* %buildroot%docdir/html/
install -p -m 0644 images/{README,*.{bmp,dat}} %buildroot%docdir/images/


%post
if [ -f /etc/%name.conf -a -x %_sbindir/detectloader.sh -a -x %_sbindir/detectliloboot.sh -a -f /proc/partitions ]; then
	if %_sbindir/detectloader.sh $(%_sbindir/detectliloboot.sh) | grep -q '^lilo$'; then
		/sbin/%name || echo "Please run %name manually." >&2
	fi
fi


%files
/boot/*
%exclude /boot/*
%exclude %_sysconfdir/*
/sbin/*
%_sbindir/*
%_man5dir/*
%_man8dir/*
%dir %docdir
%docdir/COPYING


%files doc
%dir %docdir
%docdir/*
%exclude %docdir/COPYING


%changelog
* Mon Aug 12 2019 Alexey Shabalin <shaba@altlinux.org> 24.2-alt2
- update homapage url
- drop requires lilo from lilo-doc package

* Thu Sep 21 2017 Dmitry V. Levin <ldv@altlinux.org> 24.2-alt1
- 24.0 -> 24.2.

* Mon Mar 03 2014 Led <led@altlinux.ru> 24.0-alt1
- 24.0
- removed:
  + lilo-23.2-gcc-4.8.patch
  + lilo-24.0-alt-format.patch
- updated:
  + lilo-24.0-alt-mkrescue.patch
- added:
  + lilo-24.0-alt-Makefile.patch

* Mon Feb 17 2014 Led <led@altlinux.ru> 23.2-alt1
- 23.2
- updated BuildRequires
- removed:
  + lilo-23.0-deb-owl-man.patch
  + lilo-23.0-enlarge-max-number-of-setupsecs.patch
- updated:
  + lilo-23.2-owl-makefile.patch
  + lilo-23.2-alt-owl-fixes.patch
  + lilo-23.2-alt-format.patch
- added:
  + lilo-23.2-gcc-4.8.patch

* Sun Feb 16 2014 Led <led@altlinux.ru> 23.1-alt1
- 23.1
- updated:
  + lilo-23.1-owl-makefile.patch
  + lilo-23.1-alt-defaults.patch
  + lilo-23.1-alt-format.patch

* Mon Sep 23 2013 Led <led@altlinux.ru> 23.0-alt1
- 23.0
- removed:
  + lilo-22.7.1-owl-tmp.patch
- disabled devmapper patches

* Sun Aug 11 2013 Led <led@altlinux.ru> 22.8-alt1
- 22.8
- removed:
  + lilo-22.7.1-alt-root-uuid.patch
- updated:
  + lilo-22.8-owl-makefile.patch
  + lilo-22.8-alt-blkid.patch
  + lilo-22.8-alt-devmapper.patch
  + lilo-22.7.3-alt-md-devmapper.patch
  + lilo-22.8-suse-gfx.patch
  + lilo-22.8-alt-format.patch

* Sun Nov 04 2012 Led <led@altlinux.ru> 22.7.3-alt8
- Enlarge maximum number of sectors for kernel setup code
  (lilo-22.7.3-enlarge-max-number-of-setupsecs.patch) (ALT#27143)
- added lilo-22.7.3-alt-format.patch
- build with default %%optflags
- fixed post script
- fixed Url (ALT#23630)
- cleaned up spec

* Mon Mar 22 2010 Dmitry V. Levin <ldv@altlinux.org> 22.7.3-alt7
- Bumped MAX_IMAGE_NAME constant value once more (closes: #22616).

* Tue Nov 24 2009 Dmitry V. Levin <ldv@altlinux.org> 22.7.3-alt6
- Updated build dependencies to fix build.
- Packaged doc subpackage as noarch.

* Mon Mar 12 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 22.7.3-alt5
- Fixed raid-on-dm support.

* Fri Feb 02 2007 Dmitry V. Levin <ldv@altlinux.org> 22.7.3-alt4
- Fixed degraded raid support.

* Tue Jan 16 2007 Dmitry V. Levin <ldv@altlinux.org> 22.7.3-alt3
- Updated suse-gfx patch (zerg; #10642).

* Tue Jan 09 2007 Dmitry V. Levin <ldv@altlinux.org> 22.7.3-alt2
- Reenabled devmapper support (apparently lost during version update).

* Fri Dec 29 2006 Dmitry V. Levin <ldv@altlinux.org> 22.7.3-alt1
- Updated to 22.7.3.
- Disabled gfx patch for a while (does not apply to this version).

* Tue Dec 19 2006 Dmitry V. Levin <ldv@altlinux.org> 22.7.1-alt4
- Added UUID support (legion).
- Removed kernel-headers-std from build dependencies.

* Thu Nov 30 2006 Dmitry V. Levin <ldv@altlinux.org> 22.7.1-alt3
- Updated suse-gfx patch (zerg).

* Thu Jun 22 2006 Dmitry V. Levin <ldv@altlinux.org> 22.7.1-alt2
- Updated to 22.7.1.
- Reviewed and updated patches
  (thanks to Anton Farygin and Sergey Bolshakov for the help).
- Applied patches from lilo-22.7.1-owl2 package.
- Replaced keytab-lilo.pl script with keytab-lilo utility from Owl.

* Mon Mar 06 2006 Dmitry V. Levin <ldv@altlinux.org> 22.4.1-alt10
- Fixed build with --as-needed.

* Thu Feb 10 2005 Dmitry V. Levin <ldv@altlinux.org> 22.4.1-alt9
- Fixed build on x86_64 platform (closes #5796).

* Wed Jan 19 2005 Dmitry V. Levin <ldv@altlinux.org> 22.4.1-alt8
- Fixed compilation issues detected by gcc-3.4.3.

* Wed Dec 15 2004 Anton Farygin <rider@altlinux.ru> 22.4.1-alt7
- Updated gfxboot patch from SuSE.

* Fri Dec 10 2004 Dmitry V. Levin <ldv@altlinux.org> 22.4.1-alt6
- Implemented devmapper support,
  based on patch from Sergey Bolshakov.

* Fri Jun 25 2004 Dmitry V. Levin <ldv@altlinux.org> 22.4.1-alt5
- Fixed typo in %%post script (#3356).
- Eliminate useless "LBA32 assumed" warning (#4389).

* Wed Apr 28 2004 Stanislav Ievlev <inger@altlinux.org> 22.4.1-alt4.1
- rebuild with new glibc, add patch from RH for undefined PAGE_SIZE

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 22.4.1-alt4
- Updated build dependencies.

* Fri May 30 2003 Dmitry V. Levin <ldv@altlinux.org> 22.4.1-alt3
- Fixed mkrescue (was broken since 21.6-ipl4mdk),
  patch from Anton V. Denisov.

* Tue Feb 04 2003 Rider <rider@altlinux.ru> 22.4.1-alt2
- Added gfx image format support from SuSE.

* Mon Feb 03 2003 Dmitry V. Levin <ldv@altlinux.org> 22.4.1-alt1
- Updated to 22.4.1

* Mon Dec 09 2002 Dmitry V. Levin <ldv@altlinux.org> 22.3.4-alt1
- Updated to 22.3.4, redone patches.
- %%post: do not try to reinstall boot loader when either
  detectloader or /proc/partitions are not available.

* Tue Nov 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 22.1-alt1
- 22.1
- Splitted and ported our patches to new version.

* Mon Aug 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 21.7.5-alt1
- 21.7.5
- Relocated documentation.

* Mon Feb 26 2001 Dmitry V. Levin <ldv@fandra.org> 21.7-ipl1mdk
- 21.7

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 21.6.1-ipl2mdk
- Set our white-on-blue color scheme and title by default.

* Wed Jan 03 2001 Dmitry V. Levin <ldv@fandra.org> 21.6.1-ipl1mdk
- 21.6.1.

* Fri Dec 29 2000 Dmitry V. Levin <ldv@fandra.org> 21.6-ipl4mdk
- Rewritten argument parsing code.

* Fri Dec 15 2000 Dmitry V. Levin <ldv@fandra.org> 21.6-ipl3mdk
- Fixed argument parsing (MDK).

* Wed Oct 18 2000 Dmitry V. Levin <ldv@fandra.org> 21.6-ipl2mdk
- Merge MDK & RH patches.

* Thu Oct 05 2000 Dmitry V. Levin <ldv@fandra.org> 21.6-ipl1mdk
- 21.6
- Automatically added BuildRequires.

* Mon Aug 28 2000 Dmitry V. Levin <ldv@fandra.org> 21.5.1-ipl1mdk
- 21.5.1

* Wed Aug 16 2000 Dmitry V. Levin <ldv@fandra.org> 21.5-ipl2mdk
- BM.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 21.5-ipl1mdk
- 21.5

* Sat May 27 2000 Dmitry V. Levin <ldv@fandra.org>
- RE and Fandra adaptions

* Mon May 08 2000 Dmitry V. Levin <ldv@fandra.org>
- 21.4.3

* Wed Mar 8 2000 AEN <aen@logic.ru>
- 21.3

* Wed Feb 23 2000 Pixel <pixel@mandrakesoft.com> 0.22-19mdk
- Really is 0.22 (non <<official>> version with EDD enabled)
  (EDD means no more 1024 cylinder problem)

* Fri Feb 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.22-18mdk
- Silly me reuploading and upgrade the ChangeLog.

* Wed Feb 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.22-17mdk
- Add loopdev and second patch (r).

* Tue Oct 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Remove the EBDA patch from zab and put in the EBDA patch
  from the VA Research RPM.  This fixes the EBDA issues.(r)
- Added ONE_SHOT to the compile options so that the lilo
  prompt won't timeout once you hit a key at the boot prompt(r)

* Wed Sep 22 1999 Pixel <pixel@mandrakesoft.com>
- added defattr (no comment)

* Tue Sep 21 1999 Pixel <pixel@mandrakesoft.com>
- patched keytab-lilo.pl (again!) to make it work (better) (changed a regexp)

* Sun Sep 19 1999 Pixel <pixel@mandrakesoft.com>
- added -DONE_SHOT to patch lilo-ebda (that way timeout is disabled as soon as a
  key is pressed)
- patched keytab-lilo.pl to make it work (removed bad suffix .map)

* Sun Aug 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Add the patch to boot on Compaq Smart Array 3200.

* Wed Jul 21 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- recommend manual lilo installation if post fails

* Mon Jul 19 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added turkish description

* Mon Jul 19 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- Add french description from Gregus <gregus@etudiant.net>

* Wed Jun 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Use the ebda patch from VA-Research.

* Thu Jun 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Use -DIGNORECASE -DVARSETUP -DREWRITE_TABLE -DLCF_LARGE_EBDA
  -DLARGE_EBDA by default. LARGE_EBDA is needed for some SMP systems.

* Mon Apr 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch for Mandrake-6.0.
- Add keyab-lilo.pl to the file-list

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- handle RPM_OPT_FLAGS

* Sun Dec  6 1998 Matt Wilson <msw@redhat.com>
- updated to release 0.21
- patched to build on 2.1.x kernels

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to release 0.20
- uses a build root

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc
