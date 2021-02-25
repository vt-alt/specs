%def_with doc
%def_without python

Name: libalsa
Version: 1.2.4
Release: alt1
Epoch: 1

Summary: Advanced Linux Sound Architecture (ALSA) library
License: LGPLv2.1
Group: System/Libraries

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: 0001-Restore-loading-usr-share-alsa-alsa.conf.d.patch
Url: http://www.alsa-project.org

# tse3 still depends on that, argh
Provides: libalsa2 = %version
Obsoletes: libalsa2 < %version

# for fourth-party software
Provides: alsa-lib = %version

# factored out from alsa-lib.git
Requires: alsa-ucm-conf
Requires: alsa-topology-conf

# Automatically added by buildreq on Mon Dec 26 2016
# optimized out: perl python-base python-modules
%{?_with_doc:BuildRequires: doxygen}

# for smixer plugins, see commit a668a94238dc67b19ae187b52a161e027d79ee5d
%{?_with_python:BuildRequires: python-dev}

%define pkgdocdir %_docdir/%name-%version
%define modutils_oss /etc/modutils.d/oss
%define modules_conf /etc/modules.conf
%define modprobe_old %_sysconfdir/modprobe.d/alsa-modindex
%define modprobe_conf %modprobe_old.conf

%define _unpackaged_files_terminate_build 1

%description
Advanced Linux Sound Architecture (ALSA) libs. Modularized
architecture with support for a large range of ISA and PCI cards.
Fully compatible with OSS/Lite (kernel sound drivers), but
contains many enhanced features.

%package -n aserver
Summary: Sound server for alsa
Group: Sound
Requires: %name = %epoch:%version-%release

%description -n aserver
Sound server for ALSA

%package devel
Summary: Development environment for Advanced Linux Sound Architecture (ALSA)
Group: Development/C
Requires: %name = %epoch:%version-%release
Provides: libalsa2-devel = %version
Obsoletes: libalsa2-devel < %version

%description devel
Advanced Linux Sound Architecture (ALSA) libs. Modularized
architecture with support for a large range of ISA and PCI cards.
Fully compatible with OSS/Lite (kernel sound drivers), but
contains many enhanced features.

This is the development environment to compile ALSA applications.

%if_with doc
%package docs
Summary: Documentation for Advanced Linux Sound Architecture (ALSA)
Group: Development/Documentation
BuildArch: noarch

%description docs
Advanced Linux Sound Architecture (ALSA) Developer Documentation
(C library reference)
%endif

%prep
%setup
%patch0 -p1
%patch1 -p1
# Replace "include" with "__include__" in public header files
# to make them compilable by "gcc -ansi" again.
find include -type f -print0 |
	xargs -r0 grep -FZl ' inline ' -- |
	xargs -r0 sed -i 's/ inline / __inline__ /g' --

%build
%autoreconf
%configure \
	--with-configdir=%_datadir/alsa \
	%{?!_with_python:--disable-python} \
	--disable-static
%make_build
%{?_with_doc:%make doc}

%install
%makeinstall_std

find %buildroot%_libdir -name \*.la -delete

install -pDm644 asound.conf.sonicvibes_2 %buildroot%_datadir/alsa/cards/SonicVibes.conf

mkdir -p %buildroot%pkgdocdir
%if_with doc
install -pm644 NOTES MEMORY-LEAK TODO %buildroot%pkgdocdir/
cp -a doc/doxygen/html %buildroot%pkgdocdir/
%endif

mkdir -p %buildroot%_sysconfdir/modprobe.d
cat << __EOF__ >> %buildroot%modprobe_conf
## spare index=0 for a hotplug soundcard (if any)
#options snd-usb-audio index=0

## offset HDMI output compared to onboard audio (#28648)
#options snd_hda_codec_hdmi index=2,3
#options snd_hda_intel index=2,3

#options snd_intel8x0 index=2
#options snd_via82xx index=2
#options snd-bt87x index=3
#options snd_intel8x0m index=4
#options snd-atiixp-modem index=4
#options snd-via82xx-modem index=4

## get PC speaker out of the way
options snd_pcsp index=10
__EOF__

install -d %buildroot%_localstatedir/alsa

%pre
[ ! -f %modutils_oss ] || {
	grep -q "^above snd-" %modules_conf && {
		echo '*** %modutils_oss found:'
		echo '*** commenting out "above/below snd-*-oss" lines in %modules_conf'
		subst 's/^above snd-.* snd-.*-oss$/#&/' %modules_conf ||:
	} ||:
}

%post
# newer module-init-tools barf at files missing .conf suffix
# (and rightfully so)
rm -f %modprobe_old~
for suffix in "" .rpmnew .rpmsave; do
	[ -f "%modprobe_old$suffix" ] && {
		echo '*** migrating configuration, please check:'
		mv -v "%modprobe_conf" "%modprobe_old.rpmorig"
		mv -v "%modprobe_old$suffix" "%modprobe_conf"
		exit 0
	} ||:
done

%files
%_libdir/*.so.*
%if_with python
%dir %_libdir/alsa-lib
%_libdir/alsa-lib/smixer
%endif
%config(noreplace) %modprobe_conf
%_datadir/alsa
%dir %_localstatedir/alsa

%files devel
%_includedir/sys/*
%_includedir/alsa
%_includedir/asoundlib.h
%_libdir/*.so
%_pkgconfigdir/alsa.pc
%_pkgconfigdir/alsa-topology.pc
%_datadir/aclocal/*

%if_with doc
%files docs
%dir %pkgdocdir
%pkgdocdir/[D-Z]*
%pkgdocdir/html
%endif

%files -n aserver
%_bindir/aserver

%changelog
* Wed Oct 21 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.4-alt1
- 1.2.4

* Thu Jul 09 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.3.2-alt1
- 1.2.3.2

* Sat Jun 20 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.3.1-alt1
- 1.2.3.1

* Wed Jun 10 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.3-alt1
- 1.2.3

* Thu Feb 20 2020 Michael Shigorin <mike@altlinux.org> 1:1.2.2-alt1
- 1.2.2

* Mon Dec 02 2019 Michael Shigorin <mike@altlinux.org> 1:1.2.1.2-alt1
- 1.2.1.2
- better License: tag spelling

* Fri Nov 22 2019 Michael Shigorin <mike@altlinux.org> 1:1.2.1.1-alt1
- 1.2.1.1
- fix License: tag spelling
- fix doc knob
- E2K: drop lcc 1.21 support

* Mon Nov 18 2019 Michael Shigorin <mike@altlinux.org> 1:1.2.1-alt1
- 1.2.1
- R: alsa-ucm-conf, alsa-topology-conf (maintained separately now)
- added alsa-topology.pc to -devel subpackage

* Tue May 14 2019 Dmitry V. Levin <ldv@altlinux.org> 1:1.1.9-alt2
- NMU.
- Packaged %_includedir/asoundlib.h introduced in 1.1.9 to fix builds
  of packages that use asoundlib.h header file.

* Mon May 13 2019 Michael Shigorin <mike@altlinux.org> 1:1.1.9-alt1
- 1.1.9

* Mon Feb 18 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1:1.1.8-alt2
- Patch: restore loading /usr/share/alsa/alsa.conf.d/* (Closes: 35790)

* Thu Jan 24 2019 Michael Shigorin <mike@altlinux.org> 1:1.1.8-alt1
- 1.1.8

* Wed Oct 17 2018 Michael Shigorin <mike@altlinux.org> 1:1.1.7-alt1
- 1.1.7

* Sun Sep 09 2018 Michael Shigorin <mike@altlinux.org> 1:1.1.6-alt2
- E2K: explicitly link with -lcxa

* Wed Apr 04 2018 Michael Shigorin <mike@altlinux.org> 1:1.1.6-alt1
- 1.1.6

* Wed Nov 22 2017 Michael Shigorin <mike@altlinux.org> 1:1.1.5-alt1
- 1.1.5

* Mon Jun 12 2017 Michael Shigorin <mike@altlinux.org> 1:1.1.4.1-alt1
- 1.1.4.1

* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 1:1.1.4-alt1
- 1.1.4

* Tue Dec 27 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.3-alt3
- disabed python support by default (asked by glebfm@)

* Mon Dec 26 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.3-alt2
- 1.1.3
- BOOTSTRAP: added doc, python knobs
  + enabled python support by default too

* Thu Dec 22 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.3-alt1
- 1.1.3

* Thu Oct 06 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.2-alt1
- 1.1.2

* Mon Jun 20 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.1-alt1
- 1.1.1

* Tue Feb 02 2016 Michael Shigorin <mike@altlinux.org> 1:1.1.0-alt1.1.1
- added %_localstatedir/alsa (thx aris@)

* Mon Dec 07 2015 Michael Shigorin <mike@altlinux.org> 1:1.1.0-alt1.1
- added snd-hda-codec-hdmi to alsa-modindex.conf too (see #28648)

* Mon Nov 09 2015 Michael Shigorin <mike@altlinux.org> 1:1.1.0-alt1
- 1.1.0

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 1:1.0.29-alt1
- 1.0.29

* Wed Jun 18 2014 Michael Shigorin <mike@altlinux.org> 1:1.0.28-alt1
- 1.0.28

* Wed Apr 30 2014 Michael Shigorin <mike@altlinux.org> 1:1.0.27.2-alt1
- 1.0.27.2

* Tue Apr 16 2013 Dmitry V. Levin <ldv@altlinux.org> 1:1.0.27-alt3
- libalsa-alsa: replaced "include" with "__include__", to make
  header files compilable by "gcc -ansi" as they were in 1.0.26.

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 1:1.0.27-alt2
- retag

* Sat Apr 13 2013 Michael Shigorin <mike@altlinux.org> 1:1.0.27-alt1
- 1.0.27

* Sat Mar 09 2013 Michael Shigorin <mike@altlinux.org> 1:1.0.26-alt3
- alsa-modindex.conf: promote USB audio, demote HDMI audio example
  (closes: #28648)

* Fri Sep 07 2012 Michael Shigorin <mike@altlinux.org> 1:1.0.26-alt2
- retag

* Thu Sep 06 2012 Michael Shigorin <mike@altlinux.org> 1:1.0.26-alt1
- 1.0.26
- %_datadir/alsa/pulse.conf is no more autoloaded
  (moved to %_datadir/alsa/alsa.conf.d/pulse.conf
  in corresponding alsa-plugins package)

* Tue Oct 04 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24.1-alt4
- renamed %modprobe_old
       to %modprobe_conf
  for newer module-init-tools to be happy (thx led@)

* Fri Jun 10 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24.1-alt3
- added compat Provides: alsa-lib (zerg@)

* Fri Feb 18 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24.1-alt2
- retag (thx at@)

* Wed Feb 16 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.24.1-alt1
- 1.0.24.1

* Sun Feb 13 2011 Alexey Tourbin <at@altlinux.ru> 1:1.0.23-alt6
- rebuilt for debuginfo

* Thu Jan 13 2011 Michael Shigorin <mike@altlinux.org> 1:1.0.23-alt5
- /etc/modprobe.d/alsa-modindex back (see also #24914)

* Fri Nov 26 2010 Michael Shigorin <mike@altlinux.org> 1:1.0.23-alt4
- rebuilt for set versions

* Thu Oct 21 2010 Michael Shigorin <mike@altlinux.org> 1:1.0.23-alt3
- rebuild
- minor spec cleanup

* Thu Apr 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.23-alt2
- post release fixes

* Sun Apr 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.23-alt1
- 1.0.23

* Thu Dec 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.22-alt1
- 1.0.22

* Fri Sep 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.21a-alt1
- 1.0.21a

* Tue Sep 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.21-alt1
- 1.0.21

* Sun May 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt2
- configure: fixed check libtool version

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.20-alt1
- 1.0.20

* Mon Jan 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.19-alt1
- 1.0.19

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.18-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Oct 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Mon Sep 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17a-alt2
- marked %_sysconfdir/modprobe.d/alsa-modindex is %%config(noreplace) (close #17034)

* Fri Aug 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17a-alt1
- 1.0.17a

* Sun Aug 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt2
- IEC958 definition for consumer status channel update

* Mon Jul 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt1
- 1.0.17

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.16-alt2
- build without python (close #15626)

* Thu May 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Sun Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.15-alt1
- 1.0.15
- disabled static by defaults
- spec cleanup
- update build dependencies

* Fri Aug 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.14a-alt2.1
- NMU:
  + fixed linear<->float conversion in PCM plugin
  + adapted alsa-modindex for module-init-tools

* Thu Jun 28 2007 Michael Shigorin <mike@altlinux.org> 1.0.14a-alt2
- removed linux-libc-headers build requirement to facilitate
  build on ARM (thanks kas@ for investigation)

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.14a-alt1
- 1.0.14a
- build fixes (muchos gracios, icesik@)
- removed stale patches (weren't applied anyways)
- added dmix configuration for Sonic Vibes by zerg@ (#5003)

* Mon Oct 16 2006 Michael Shigorin <mike@altlinux.org> 1.0.13-alt1
- 1.0.13

* Sat Sep 02 2006 Michael Shigorin <mike@altlinux.org> 1.0.12-alt1
- 1.0.12
- changed BuildPreReq: kernel-headers-std to linux-libc-headers
  (thanks shrek@ for success story and lakostis@ for reminders)

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- 1.0.11
- alsalisp no more installed, see changelog

* Wed Apr 05 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.4
- 1.0.11rc4

* Sat Mar 04 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.3
- 1.0.11rc3; should fix #9181 (apps hang when using dmix)
  + thanks Artem G. Delendik <u2u/nm.ru> for thorough investigation
- removed patch4 (applied already)

* Sat Dec 10 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt2
- added ALSA CVS patch for dmix:
  fixed ipc_gid initialization when gid specified as number
  + thanks Sergey Vlasov (vsu@) for a bounce/explanation
- added overlooked %_libdir/alsa-lib/smixer/
- fixed a silly typo which barred inclusion of 
  %_sysconfdir/modutils.d/alsa-modindex into a package
- spec *cleanup*

* Wed Nov 16 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- 1.0.10
- removed patch2 (merged upstream)

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt7
- updated docs Group:

* Mon Oct 17 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt7
- fixed small typo in %post (rather cosmetic)

* Tue Oct 04 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt6
- applied changes proposed in #8133 to avoid %pre failure;
  thanks Anton Farygin (rider@) for alert/fix
  
* Mon Oct 03 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt5
- attempt to workaround #8096 just in case it still applies
  ("Too deep recursion in module dependencies!")
- see also http://wiki.sisyphus.ru/admin/Sound/ModuleLoadProblem

* Fri Sep 16 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt4
- removed superfluous COPYING (standard license mentioned
  in package header data), thanks to Alexey Tourbin (at@)
  for absolute symlink warning

* Mon Jul 11 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt3
- added modutils file to let shift on-board AC97 codec drivers 
  after "real" hardware ones, if any; also some more stuff from FAQ
  (should be properly fixed within hotplug and/or alsa)

* Fri Jul 08 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt2
- added CVS patches (name clash; ALSA bug #1139)
- thanks Vitaly Lipatov (lav@) for alerting and Sergey Vlasov (vsu@)
  for identifying the problem and handing over the patches

* Thu Jun 23 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- 1.0.9
- added separate docs subpackage (#5935)

* Thu Jun 09 2005 Michael Shigorin <mike@altlinux.ru> 1.0.9-alt0
- 1.0.9

* Thu Apr 28 2005 Michael Shigorin <mike@altlinux.ru> 1.0.8-alt2
- #6697 (license fix)

* Thu Jan 13 2005 Michael Shigorin <mike@altlinux.ru> 1.0.8-alt1
- 1.0.8
- enabled static library build by default (#5580)

* Mon Nov 29 2004 Michael Shigorin <mike@altlinux.ru> 1.0.7-alt1
- 1.0.7 (err...)

* Sat Jun 26 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt2
- tiny spec cleanup/rebuild

* Mon May 31 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Sat Apr 03 2004 Michael Shigorin <mike@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sun Mar 21 2004 Michael Shigorin <mike@altlinux.ru> 1.0.3b-alt1
- 1.0.3b
- added kernel-headers-std build dep

* Sat Mar 06 2004 Michael Shigorin <mike@altlinux.ru> 1.0.3a-alt1
- 1.0.3a

* Tue Mar 02 2004 Michael Shigorin <mike@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Thu Jan 29 2004 Michael Shigorin <mike@altlinux.ru> 1.0.2-alt2
- 1.0.2, Final Upload by ALSA Project (TM) 20040129 18:35 +0200
- thanks to Sergey Vlasov (vsu@) for alerting about re-uploads

* Wed Jan 28 2004 Michael Shigorin <mike@altlinux.ru> 1.0.2-alt1
- 1.0.2
- upstream merged patch0, patch1 (alt-fpic and shm-leak)

* Tue Jan 20 2004 Michael Shigorin <mike@altlinux.ru> 1.0.1-alt3
- added patch by Adam Tla/lka <atlka pg gda pl> to fix shared
  memory leak; thanks to Sergey Vlasov (vsu@)
- added %_bindir/alsalisp to devel subpackage

* Mon Jan 19 2004 Michael Shigorin <mike@altlinux.ru> 1.0.1-alt2
- spec facelift/cleanup by Mikhail Zabaluev (mhz@):
  * doxygen'erated docs, license files installed the right way;
  * build deps refresh/cleanup
- translated package info

* Sun Jan 18 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.1-alt1.1
- build doxygen docs, package them plus readme files and symlinked license
- spec cleanup
- buildreq (WTF was this mawk thing?)
- builds fine without alsa-driver-headers (?)

* Sun Jan 11 2004 Michael Shigorin <mike@altlinux.ru> 1.0.1-alt1
- 1.0.1
- WARNING: API has changed in 1.0.x, things may break
- removed *.la
- don't package static libs by default

* Tue Nov 11 2003 Michael Shigorin <mike@altlinux.ru> 0.9.8-alt2
- fixed -fPIC-related trouble:
 * %optflags_shared
 * patch by Dmitry V. Levin (ldv@)

* Wed Oct 22 2003 Michael Shigorin <mike@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Fri Sep 26 2003 Michael Shigorin <mike@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Wed Jul 30 2003 Michael Shigorin <mike@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Tue Jul 15 2003 Michael Shigorin <mike@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Tue Jul 08 2003 Michael Shigorin <mike@altlinux.ru> 0.9.4-alt2
- fixed forcibly broken BuildRequires as kernel-source-alsa-std got fixed
  (alsa-driver-headers >= %%version)

* Mon Jun 23 2003 Michael Shigorin <mike@altlinux.ru> 0.9.4-alt1
- 0.9.4
- renamed to libalsa

* Wed Apr 02 2003 Michael Shigorin <mike@altlinux.ru> 0.9.2-alt0.1
- 0.9.2 (unofficial build)

* Tue Feb 04 2003 Rider <rider@altlinux.ru> 0.9.0rc7-alt1
- 0.9.0rc7

* Tue Nov 26 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc6-alt1
- 0.9.0rc6
- REbuilt in new environment

* Mon Jun 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc1-alt2
- Removed requires to virtual kernel alsa

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc1-alt1
- 0.9.0rc1

* Thu Feb 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta12-alt1
- 0.9.0beta12

* Wed Dec 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta10a-alt1
- 0.9.0beta10a

* Tue Nov 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta9-alt1
- 0.9.0beta9

* Fri Oct 12 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta8a-alt1
- 0.9.0beta8a
- Fixed requires
- Fixed filelists

* Fri Sep 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta7-alt1
- First build for Sisyphus
