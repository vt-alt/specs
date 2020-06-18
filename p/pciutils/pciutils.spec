%define libname libpci

Name: pciutils
Version: 3.7.0
Release: alt1

Summary: Linux PCI utilities
License: GPLv2
Group: System/Kernel and hardware

Url: http://mj.ucw.cz/sw/pciutils/
# git://git.kernel.org/pub/scm/utils/pciutils/pciutils.git
Source: %name-%version.tar

Requires: pciids
Requires: %libname = %version-%release
BuildRequires(pre):rpm-build-ubt

# http://www.kernel.org/pub/software/utils/pciutils/
# http://git.kernel.org/?p=utils/pciutils/pciutils.git
# git://git.kernel.org/pub/scm/utils/pciutils/pciutils.git
# http://git.ucw.cz/gitweb/?p=pciutils.git
# git://git.ucw.cz/pciutils.git

Summary(ru_RU.UTF-8): Утилиты для работы с PCI в Linux
Summary(uk_UA.UTF-8): Утиліти для роботи з PCI в Linux

%description
This package contains various utilities for inspecting
and setting devices connected to the PCI bus.

%description -l ru_RU.UTF-8
Этот пакет содержит несколько утилит для просмотра и настройки
устройств, подключенных к шине PCI.

%description -l uk_UA.UTF-8
Цей пакунок містить декілька утиліт для перегляду й налаштування
пристроїв, які підключено до шини PCI.

%package -n %libname
Summary: Linux PCI library
Group: System/Libraries

%description -n %libname
This package contains shared library for inspecting and setting
devices connected to the PCI bus.

%package -n %libname-devel
Summary: Linux PCI development library
Group: Development/C
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < 2.99.1 %name-devel-static < 2.99.1

%description -n %libname-devel
This package contains PCI library headers.

%prep
%setup

%build
%make_build \
	SHARED=yes \
	OPT="%optflags" \
	PREFIX=%_prefix \
	IDSDIR=%_datadir/misc

%install
%make_install \
	SHARED=yes \
	DESTDIR=%buildroot \
	PREFIX=%_prefix \
	install install-lib

mv %buildroot%_sbindir %buildroot%_bindir
[ "%_libdir" = "%_prefix/lib" ] || {
	mv %buildroot%_prefix/lib %buildroot%_libdir
}

%files
%_bindir/lspci
%_bindir/setpci
%_man8dir/lspci*
%_man8dir/setpci*
%doc README TODO ChangeLog *.lsm

%files -n %libname
%_libdir/*.so.*

%files -n %libname-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_man7dir/pcilib*

%changelog
* Mon Jun 15 2020 Anton Farygin <rider@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Thu Mar 12 2020 Anton Farygin <rider@altlinux.ru> 3.6.4-alt1
- 3.6.4

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 3.6.3-alt1
- 3.6.3

* Sat Mar 30 2019 Michael Shigorin <mike@altlinux.org> 3.6.2-alt2
- enable parallel build
- drop %%ubt

* Fri Sep 21 2018 Anton Farygin <rider@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Wed Jul 18 2018 Anton Farygin <rider@altlinux.ru> 3.6.1-alt1
- 3.6.1

* Mon Nov 27 2017 Anton Farygin <rider@altlinux.ru> 3.5.6-alt1
- new version

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 3.5.5-alt1
- new version

* Tue Mar 14 2017 Anton Farygin <rider@altlinux.ru> 3.5.4-alt1
- new version

* Fri Oct 21 2016 Anton Farygin <rider@altlinux.ru> 3.5.2-alt1
- new version

* Wed Jun 29 2016 Anton Farygin <rider@altlinux.ru> 3.5.1-alt1
- new version

* Fri Nov 14 2014 Michael Shigorin <mike@altlinux.org> 3.3.0-alt1
- 3.3.0

* Sat Dec 28 2013 Michael Shigorin <mike@altlinux.org> 3.2.1-alt1
- 3.2.1
- converted summary/description to utf-8

* Thu May 16 2013 Michael Shigorin <mike@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Aug 01 2012 Michael Shigorin <mike@altlinux.org> 3.1.10-alt1
- 3.1.10

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 3.1.9-alt2
- updated an Url:

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 3.1.9-alt1
- 3.1.9

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 3.1.7-alt1
- 3.1.7

* Sun Sep 26 2010 Michael Shigorin <mike@altlinux.org> 3.1.6-alt2
- replaced pci.ids provider: autoupdated pciids is more useful
  than manually updated hwdatabase, as discussed previously
- minor spec cleanup

* Mon Feb 15 2010 Anton Farygin <rider@altlinux.ru> 3.1.6-alt1
- new version
- pciutils: add libpci = %%version-%%release requires

* Mon Feb 16 2009 Michael Shigorin <mike@altlinux.org> 3.1.2-alt1
- 3.1.2 (forgotten push :)
  + setpci: minor bugfix

* Mon Feb 16 2009 Michael Shigorin <mike@altlinux.org> 3.1.1-alt1
- 3.1.1
  + many decoding and usability enhancements
  + minor bugfixes
  + pci.ids update
- 3.0.3 included important enhancement for lspci -k (subsystem ID)

* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 3.0.0-alt1
- 3.0.0
  + API/ABI version bump occured

* Fri Feb 22 2008 Michael Shigorin <mike@altlinux.org> 2.99.1-alt0.2
- 2.99.1-alpha2+ (git commit a2bf30a4fd407c55e8172e2f6fd158725ccb90b6):
  + added shared library, see pcilib(7)
  + added networked PCI IDs support; see -q/-Q/-O lspci options
  + access method now chosen via -A lspci/setpci switch; -P dropped
  + reworked build system
  + "Unknown device" string replaced with "Device" not to alarm
    inexperienced users for no good reason
- dropped static library build
- reworked and renamed devel subpackage
  from %name-devel to %libname-devel

* Wed Feb 13 2008 Michael Shigorin <mike@altlinux.org> 2.2.10-alt2
- fixed build on x86_64
- added Ukrainian description

* Tue Feb 12 2008 Michael Shigorin <mike@altlinux.org> 2.2.10-alt1
- 2.2.10
  + removed pcimodules patch -- now implemented as lspci -k;
    thanks Valery Inozemtsev (shrek@) for notifying
- removed update-pciids(8) on shrek@'s request

* Sat Dec 22 2007 Michael Shigorin <mike@altlinux.org> 2.2.9-alt2
- use make install, no more installation by hand

* Sat Dec 22 2007 Michael Shigorin <mike@altlinux.org> 2.2.9-alt1
- 2.2.9
- updated patch4 (hm... is it really needed?) in git
- removed patch10 (implemented upstream)
- whoops, really do install pcimodules

* Wed Nov 15 2006 Michael Shigorin <mike@altlinux.org> 2.2.4-alt1
- fixed ugly consequence of installation by hand
  (types.h was lost while updating the version)

* Mon Oct 02 2006 Michael Shigorin <mike@altlinux.org> 2.2.4-alt0.1
- 2.2.4
- updated Source: url to primary site
- updated patch4 from Gentoo
- updated patch10
- removed patch6, patch7 (sysfs support already present)
- removed patch5 (done)
- removed patch3 (seems done another way)
- removed patch2 (done)
- removed patch1 (trivially updated but didn't make it upstream,
  wasn't spotted in other distros than Mandriva up to 10.2;
  found as removed in Annvix)
- removed patch0 (done similarly)
- removed patch9 (seems done)
- removed patch8 (pass via variable)

* Thu Dec 30 2004 Anton Farygin <rider@altlinux.ru> 2.1.11-alt10
- lspci -n segfault fixed (#5799)

* Tue Dec 28 2004 Anton Farygin <rider@altlinux.ru> 2.1.11-alt9
- text reloacations fixed in libpci

* Tue Dec 28 2004 Anton Farygin <rider@altlinux.ru> 2.1.11-alt8
- fixed memory leak into libpci (thanks to dfo)

* Thu Dec 23 2004 Anton Farygin <rider@altlinux.ru> 2.1.11-alt7
- support for sysfs (%name-sysfs.diff)
- pci.ids moved to hwdatabase package

* Fri Oct 29 2004 Anton Farygin <rider@altlinux.ru> 2.1.11-alt6
- updated pci.ids

* Wed Apr 28 2004 Anton Farygin <rider@altlinux.ru> 2.1.11-alt5
- updated pci.ids

* Wed Sep 10 2003 Rider <rider@altlinux.ru> 2.1.11-alt4
- updated pci.ids from http://pciids.sourceforge.net/ (bug #2960)

* Tue Jul 08 2003 Rider <rider@altlinux.ru> 2.1.11-alt3
- add CLASS_COMMUNICATION_MODEM to header.h

* Tue Mar 11 2003 Rider <rider@altlinux.ru> 2.1.11-alt2
- fix path to pci.ids database
- russian Summary and Description

* Mon Jan 20 2003 Konstantin Volckov <goldhead@altlinux.ru> 2.1.11-alt1
- 2.1.11

* Tue Nov 05 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.1.10-alt1
- 2.1.10

* Tue Nov 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.1.9-alt1
- 2.1.9
- Added devel-static package

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.8-ipl6mdk
- RE adaptions.

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 2.1.8-6mdk
- add require for -devel

* Mon Sep 25 2000 Pixel <pixel@mandrakesoft.com> 2.1.8-5mdk
- include pci.ids patch from redhat

* Sun Sep  3 2000 Pixel <pixel@mandrakesoft.com> 2.1.8-4mdk
- fix the license

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 2.1.8-3mdk
- BM

* Wed Jun 28 2000 Pixel <pixel@mandrakesoft.com> 2.1.8-2mdk
- cleanup
- add redhat's patch

* Tue Jun  6 2000 Pixel <pixel@mandrakesoft.com> 2.1.8-1mdk
- new version

* Tue Apr 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.1.6-2mdk
- move lspci to /usr/bin since it's userspace.
- Read Cardbus info only when we are root.
- Clean-up specs.

* Mon Apr 17 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 2.1.6-1mdk
- 2.1.6
- new BuildRoot
- remove ExcludeArch armv4l
- add TODO as pciutils-devel documentation

* Sat Mar 25 2000 Pixel <pixel@mandrakesoft.com> 2.1.5-2mdk
- new group

* Wed Feb 16 2000 Pixel <pixel@mandrakesoft.com> 2.1.5-1mdk
- new version

* Sun Nov 21 1999 Pixel <pixel@mandrakesoft.com>
- removed %%config for pci.ids (someone was zealous here?)
- changed 0711 to 0755 for lspci (makes rpmlint happy :)

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- s/=>/>=//g in Requires:.

* Sun Oct 31 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- 2.1 final.

* Tue Oct 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.1-pre8.

* Wed Oct 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- NMU: Build release.

* Fri Oct  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Add pciutils-devel package.

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- 2.1pre5
- cleaning spec

* Thu Jul 15 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- update to 2.1-pre4.tar.bz2

* Wed May 19 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 2.0

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Mon Apr 19 1999 Jakub Jelinek  <jj@ultra.linux.cz>
- update to 1.99.5
- fix sparc64 operation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Feb  4 1999 Bill Nottingham <notting@redhat.com>
- initial build
