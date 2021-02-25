%def_with systemd

Name: alsa-utils
Version: 1.2.4
Release: alt1
Epoch: 1

Summary: Advanced Linux Sound Architecture (ALSA) utils
License: GPLv2+
Group: System/Kernel and hardware

Url: http://www.alsa-project.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: dialog
Obsoletes: alsa2-utils < 0.9.4
Provides: alsa2-utils = %version
Conflicts: alsa-utils < 1.0.9a-alt1

BuildRequires: intltool libalsa-devel libncursesw-devel xmlto libfftw3-devel
%{?_with_systemd:BuildRequires: systemd-devel}
Requires: libncursesw >= 5.7
Requires: sysfsutils

Obsoletes: alsa-bat <= 1.1.0
Provides: alsa-bat = %version

%add_findreq_skiplist %_sbindir/alsa-info.sh

%description
Advanced Linux Sound Architecture (ALSA) utils. Modularized
architecture with support for a large range of ISA and PCI cards.
Fully compatible with OSS/Lite but contains many enhanced features.

%package -n aplay
Summary: play utility for ALSA
Group: Sound

%description -n aplay
This package contains minimal client utility for ALSA:
"aplay" is traditional "play" equivalent.

%package -n amixer
Summary: Command-line mixer for ALSA soundcard driver
License: GPL-2.0-or-later
Group: Sound

%description -n amixer
amixer allows command-line control of the mixer for the ALSA soundcard
driver.  amixer supports multiple soundcards.

%prep
%setup
%patch -p1
touch config.rpath

%build
%autoreconf
%configure \
	--with-curses=ncursesw \
	%{?_with_systemd:--with-systemdsystemunitdir=%_unitdir} \
	--disable-alsaconf
%make_build

%install
%makeinstall_std
%find_lang --with-man --output=%name.lang %name

%files -f %name.lang
%doc ChangeLog README*
%_udevrulesdir/*.rules
%_bindir/*
%exclude %_bindir/aplay
%exclude %_bindir/arecord
%exclude %_bindir/amixer
%_sbindir/*
%_datadir/alsa/speaker-test
%_datadir/alsa/init
%_datadir/sounds/alsa
%_man1dir/*.1*
%exclude %_man1dir/aplay.1*
%exclude %_man1dir/arecord.1*
%exclude %_man1dir/amixer.1*
%_man7dir/*.7*

%if_with systemd
%_unitdir/alsa-restore.service
%_unitdir/alsa-state.service
%_unitdir/sound.target.wants/alsa-restore.service
%_unitdir/sound.target.wants/alsa-state.service
%endif

%files -n aplay
%_bindir/aplay
%_bindir/arecord
%_man1dir/aplay.1*
%_man1dir/arecord.1*

%files -n amixer
%_bindir/amixer
%_man1dir/amixer.1*

%changelog
* Wed Oct 21 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.4-alt1
- 1.2.4

* Wed Jun 10 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.3-alt1
- 1.2.3 (closes: #38416)
- dropped 89-alsa-ucm.rules (following upstream)

* Thu Feb 20 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.2-alt1
- 1.2.2

* Mon Jan 13 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.1-alt3
- cherry-picked upstream commit 3c740d90490abe64c86c667934ba5d990817b873
  (closes: #37757)

* Sun Dec 08 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.2.1-alt2
- added systemd knob (on by default)
- spec: corrected license field (use specific SPDX identifier)

* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 1:1.2.1-alt1
- 1.2.1
- added 89-alsa-ucm.rules
- minor spec cleanup

* Mon May 13 2019 Michael Shigorin <mike@altlinux.org> 1:1.1.9-alt1
- 1.1.9

* Thu Jan 24 2019 Michael Shigorin <mike@altlinux.org> 1:1.1.8-alt1
- 1.1.8

* Wed Oct 17 2018 Michael Shigorin <mike@altlinux.org> 1:1.1.7-alt1
- 1.1.7

* Wed Nov 22 2017 Michael Shigorin <mike@altlinux.org> 1:1.1.5-alt1
- 1.1.5

* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 1:1.1.4-alt1
- 1.1.4

* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.3-alt1
- 1.1.3

* Thu Oct 06 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.2-alt1
- 1.1.2

* Thu Jun 23 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.1-alt1.1
- dropped alsa-bat subpackage: upstream renamed bat(1)
  which conflicted with existing bacula binary to alsabat(1)
- added 90-alsa-restore.rules

* Mon Jun 20 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.1-alt1
- 1.1.1

* Thu May 05 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.0-alt1.1.1
- added R: sysfsutils (closes: #32065)

* Mon Nov 09 2015 Michael Shigorin <mike@altlinux.org> 1:1.1.0-alt1.1
- added alsa-bat subpackage (Conflicts: bacula-bat over %_bindir/bat)

* Mon Nov 09 2015 Michael Shigorin <mike@altlinux.org> 1:1.1.0-alt1
- 1.1.0

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 1:1.0.29-alt2
- disabled autoreq for alsa-info.sh (R: lsb-core for no good reason)

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 1:1.0.29-alt1
- 1.0.29

* Wed Jun 18 2014 Michael Shigorin <mike@altlinux.org> 1:1.0.28-alt1
- 1.0.28

* Wed Apr 30 2014 Michael Shigorin <mike@altlinux.org> 1:1.0.27.2-alt1
- 1.0.27.2

* Wed Apr 17 2013 Michael Shigorin <mike@altlinux.org> 1:1.0.27-alt3
- post-1.0.27 fixes, see also rh#951750 (thanks ononim from opennet)

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 1:1.0.27-alt2
- retag

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 1:1.0.27-alt1
- 1.0.27

* Fri Sep 07 2012 Michael Shigorin <mike@altlinux.org> 1:1.0.26-alt2
- retag

* Thu Sep 06 2012 Michael Shigorin <mike@altlinux.org> 1:1.0.26-alt1
- 1.0.26

* Wed Mar 07 2012 Michael Shigorin <mike@altlinux.org> 1:1.0.24.2-alt2
- cherry-picked upstream commit 4c09aaa to fix alsamixer segfault
  with pulseaudio and libxcb-1.8 (debian #657538, rh #731381)

* Wed Feb 16 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24.2-alt1
- 1.0.24.2
- added alsactl_init(7) manpage
- dropped versioned libalsa dependency

* Sun Apr 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.23-alt1
- 1.0.23

* Fri Apr 09 2010 Michael Shigorin <mike@altlinux.org> 1:1.0.22-alt2.1
- slightly softened libalsa dependency (version only, dropped release)

* Sat Mar 27 2010 Michael Shigorin <mike@altlinux.org> 1:1.0.22-alt2
- merge-up: shrek@ didn't notice my 1.0.22 "test please" announce
  and did an independent update
  + reverted localized descriptions removal, no policy so far
    and I consider these useful
  + minor spec cleanup
  + re-added crude versioning of ncurses dependency (closes: #21991)

* Thu Dec 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.22-alt1
- 1.0.22

* Thu Dec 17 2009 Michael Shigorin <mike@altlinux.org> 1.0.22-alt1
- 1.0.22

* Sun Oct 25 2009 Michael Shigorin <mike@altlinux.org> 1.0.21-alt2
- added crude versioning of ncurses dependency (closes: #21991)
- _unpackaged_files_terminate_build again
- spec cleanup

* Tue Sep 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.21-alt1
- 1.0.21

* Sun May 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt2
- rebuild

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt1
- 1.0.20

* Mon Jan 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt1
- 1.0.19

* Wed Oct 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Sun Aug 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt2
- iecset update for new consumer status channel bits

* Wed Jul 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt1
- 1.0.17

* Thu May 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Sun Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.15-alt1
- 1.0.15
- spec cleanup
- update build dependencies

* Mon Aug 06 2007 Michael Shigorin <mike@altlinux.org> 1.0.14-alt3
- changes by led (thanks!):
  + added amixer subpackage (#12487)
  + moved aplay.1 to aplay subpackage
- moved arecord binary and manpage to aplay subpackage too (symlinks)

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.14-alt2
- relaxed overly strict Requires, thanks shrek@

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- 1.0.14
- set _unpackaged_files_terminate_build
- added localized manpages

* Mon Oct 16 2006 Michael Shigorin <mike@altlinux.org> 1.0.13-alt1
- 1.0.13

* Sat Sep 02 2006 Michael Shigorin <mike@altlinux.org> 1.0.12-alt1
- 1.0.12

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- 1.0.11

* Wed Apr 05 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.4
- 1.0.11rc4
- packaged translations

* Sat Mar 04 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.2
- 1.0.11rc2 (due to strict libalsa version requirement and #9181)

* Fri Feb 17 2006 Michael Shigorin <mike@altlinux.org> 1.0.10-alt2
- more strict libalsa requires (should fix #9028)

* Wed Nov 16 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- 1.0.10

* Mon Jul 04 2005 Michael Shigorin <mike@altlinux.org> 1.0.9a-alt2
- added Conflicts: for previous versions due to aplay split
  (#7279); thanks Andrey Rahmatullin (wrar@)

* Thu Jun 23 2005 Michael Shigorin <mike@altlinux.org> 1.0.9a-alt1
- 1.0.9a
- temporarily fixated libalsa requires (build/install) at 1.0.9
  since usual condition (>=%%version) would fail
- moved aplay to separate subpackage (#7156),
  required by main package
- added test sounds (were missing somehow)

* Thu Jun 09 2005 Michael Shigorin <mike@altlinux.ru> 1.0.9a-alt0
- 1.0.9a

* Mon Jan 17 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.8-alt1.1
- Rebuilt with ncurses-5.4.20050108-alt2

* Thu Jan 13 2005 Michael Shigorin <mike@altlinux.ru> 1.0.8-alt1
- 1.0.8
- updated alt-no-newt patch

* Thu Dec 16 2004 Michael Shigorin <mike@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Sat Jul 03 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt3
- *applied* the patch for #3824 from wrar@, whoops!

* Sat Jun 26 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt2
- fixed #3824, thanks to Andrey Rahmatullin (wrar@) for bug/patch
- added ru/uk package info

* Mon May 31 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Thu Apr 08 2004 Michael Shigorin <mike@altlinux.ru> 1.0.4-alt2
- removed forbidden requires: alsa

* Sat Apr 03 2004 Michael Shigorin <mike@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Mar 02 2004 Michael Shigorin <mike@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Jan 29 2004 Michael Shigorin <mike@altlinux.ru> 1.0.2-alt2
- 1.0.2, Final Upload by ALSA Project (TM) 20040129 18:35 +0200
- thanks to Sergey Vlasov (vsu@) for alerting about re-uploads

* Wed Jan 28 2004 Michael Shigorin <mike@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Jan 15 2004 Michael Shigorin <mike@altlinux.ru> 1.0.1-alt1
- 1.0.1
- added %_bindir/set_default_volume from SuSE package

* Wed Oct 22 2003 Michael Shigorin <mike@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Fri Sep 26 2003 Michael Shigorin <mike@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Wed Jul 30 2003 Michael Shigorin <mike@altlinux.ru> 0.9.6-alt1
- 0.9.6
- relaxed alsa (kernel module) dependency -- any alsa2 should suffice
  and userspace upgrade shouldn't force kernel module upgrade

* Tue Jul 15 2003 Michael Shigorin <mike@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Mon Jun 23 2003 Michael Shigorin <mike@altlinux.ru> 0.9.4-alt1
- 0.9.4
- renamed to alsa-utils

* Wed Apr 02 2003 Michael Shigorin <mike@altlinux.ru> 0.9.2-alt0.1
- 0.9.2 (unofficial build)

* Tue Feb 04 2003 Rider <rider@altlinux.ru> 0.9.0rc7-alt1
- 0.9.0rc7

* Tue Nov 26 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc6-alt1
- 0.9.0rc6
- Rebuilt in new environment

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc1-alt1
- 0.9.0rc1

* Thu Feb 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta12-alt1
- 0.9.0beta12

* Wed Dec 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta10-alt1a
- 0.9.0beta10a

* Wed Nov 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta9-alt1
- 0.9.0beta9

* Fri Oct 12 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta8-alt1
- 0.9.0beta8

* Fri Sep 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta7-alt1
- First build for Sisyphus
