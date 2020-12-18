%define allname %name+sendfax
%define allconfdir %_sysconfdir/%allname
%define alllibdir %_libdir/%allname

Name: mgetty
Version: 1.2.1
Release: alt1

Summary: A getty replacement for use with data and fax modems
License: GPL
Group: Communications

Url: http://mgetty.greenie.net/
# ftp://mgetty.greenie.net/pub/%name/source/1.2/%name-%version.tar.gz
Source: %name-%version.tar
Source1: %name.logrotate
Source2: voice.conf-dist

Patch1: %name-1.1.5-config.patch
Patch2: %name-1.1.5-makekvg.patch
Patch3: %name-1.1.28-paths.patch
Patch5: %name-1.1.24-imakefile.patch
Patch7: %name-1.1.24-contrib.patch
Patch9: %name-1.1.21-void.patch
Patch10: %name-1.1.30-paths.patch
Patch11: %name-1.1.26-elsa.patch

Patch15: %name-1.1.25-usrvavaev.patch
Patch16: %name-1.1.26-logfile.patch
Patch17: %name-1.1.25-cid.patch
Patch18: %name-1.1.26-avc_cid.patch
patch19: %name-1.1.30.FAX_OUT_USER.patch
Patch20: %name-1.1.29-helper.patch
Patch21: %name-1.1.30-mktemp.patch
Patch22: %name-1.1.30-unioninit.new.patch
Patch30: %name-1.1.31-share-Makefile.patch
Patch31: %name-1.1.31-helper2.patch
Patch32: %name-1.1.31-no-acroread.patch
Patch33: %name-1.1.31-W-format.patch
Patch34: %name-1.1.31-policy.patch

Patch35: %name-alt-warnings.patch

# from gentoo
Patch40: mgetty-1.1.31-callback.patch
Patch42: mgetty-1.1.35-strerror.patch

# debian-based
Patch60: mgetty-1.1.37-alt-texi2roff.patch

Requires(pre): /var/lock/serial

# Automatically added by buildreq on Tue Oct 06 2009
BuildRequires: gccmakedep groff-base imake libX11-devel libXext-devel xorg-cf-files
BuildRequires: texlive-base
# explicitly added texinfo for info files
BuildRequires: texinfo

%package sendfax
Summary: Provides support for sending faxes over a modem
Group: Communications
Requires: %name = %version-%release
Conflicts: efax

%package voice
Summary: A program for using your modem and %name as an answering machine
Group: Communications
Requires: %name = %version-%release

%package viewfax
Summary: An X Window System fax viewer
Group: Communications
Requires: %name = %version-%release

%package doc
Summary: Documentation, samples and contributed stuff that comes with %name
Group: Communications
Requires: %name = %version-%release
Obsoletes: %name-contrib
BuildArch: noarch

%description
The %name package contains a "smart" getty which allows logins over a
serial line (i.e., through a modem).  If you're using a Class 2 or 2.0
modem, %name can receive faxes.  If you also need to send faxes, you'll
need to install the sendfax program.

If you'll be dialing in to your system using a modem, you should install
the %name package.  If you'd like to send faxes using %name and your
modem, you'll need to install the %name-sendfax program.  If you need a
viewer for faxes, you'll also need to install the %name-viewfax package.

%description sendfax
Sendfax is a standalone backend program for sending fax files.  The
%name program (a getty replacement for handling logins over a serial
line) plus sendfax will allow you to send faxes through a Class 2 modem.

If you'd like to send faxes over a Class 2 modem, you'll need to install
the %name-sendfax and the %name packages.

%description voice
The %name-voice package contains the vgetty system, which enables
%name and your modem to support voice capabilities.  In simple terms,
vgetty lets your modem act as an answering machine.  How well the system
will work depends upon your modem, which may or may not be able to handle
this kind of implementation.

Install %name-voice along with %name if you'd like to try having your
modem act as an answering machine.

%description viewfax
Viewfax displays the fax files received using %name in an X11 window.
Viewfax is capable of zooming in and out on the displayed fax.

If you're installing the %name-viewfax package, you'll also need to
install %name.

%description doc
Documentation, samples and contributed stuff that comes with %name.

%prep
%setup
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch5 -p2
%patch7 -p2
%patch9 -p2
%patch10 -p2
%patch11 -p2

%patch15 -p2
%patch16 -p2
%patch17 -p2
%patch18 -p2
%patch19 -p2
%patch20 -p2
%patch21 -p2
%patch22 -p2
%patch30 -p2
%patch31 -p2
%patch32 -p2
%patch33 -p2
%patch34 -p2

%patch35 -p2

%patch40 -p2
%patch42 -p2

%patch60 -p2

cp policy.h-dist policy.h

find -type f -name Makefile\* |
	xargs fgrep -l '$(INSTALL)' |
	xargs -r perl -pi -e 's|(\$\(INSTALL\).*) -o [A-Za-z$(){}]*|$1|g;s|(\$\(INSTALL\).*) -g [A-Za-z$(){}]*|$1|g'
find -type f -name Makefile\* |
	xargs fgrep -l 'install' |
	xargs -r perl -pi -e 's|(install.*) -o [A-Za-z$(){}]*|$1|g;s|(install.*) -g [A-Za-z$(){}]*|$1|g'
find -type f |
	xargs fgrep -l /usr/local |
	xargs -r perl -pi -e 's,/usr/local,%prefix,g'
find -type f |
	xargs fgrep -l /perl5 |
	xargs -r perl -pi -e 's,/perl5,/perl,g'

chmod +x ./mkidirs

%build
%make
%make -C voice
%make doc-all

pushd frontends/X11/viewfax
xmkmf
%make HELPDIR=%alllibdir CONFDIR=%allconfdir depend
%make CDEBUGFLAGS="%optflags" HELPDIR=%alllibdir CONFDIR=%allconfdir
popd

%install
%define instflags spool=%buildroot%_spooldir CONFDIR=%buildroot%allconfdir LIBDIR=%buildroot%alllibdir HELPDIR=%buildroot%alllibdir MANPATH=%buildroot%_mandir
mkdir -p %buildroot{/sbin,%alllibdir,%_man1dir}
mkdir -p %buildroot%_spooldir/voice/{messages,incoming}
%makeinstall %instflags
mv %buildroot%_sbindir/%name %buildroot/sbin
ln -s ../../sbin/%name %buildroot%_sbindir

# Voice mail extensions
%makeinstall %instflags SBINDIR=%buildroot/sbin -C voice

%makeinstall %instflags MANPATH=%buildroot%_x11mandir BINDIR=%buildroot%_x11bindir -C frontends/X11/viewfax install install.man

install -pDm640 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/%name
install -pm700 callback/callback %buildroot%_sbindir
install -pm755 callback/ct %buildroot%_bindir

# This conflicts with efax
mv %buildroot%_man1dir/fax.1 %buildroot%_man1dir/%{name}_fax.1

cat %SOURCE2 >%buildroot%allconfdir/voice.conf
chmod 0600 %buildroot%allconfdir/voice.conf

mkdir -p %buildroot/var/log/%name

# Don't ship documentation that is executable.
find samples -type f |xargs chmod a-x

%files
/sbin/%name
%_sbindir/%name
%_man8dir/%name.8*
%_man8dir/callback.8*
%_man8dir/faxrunqd.8*
#_man8dir/vgetty.8*
%_man4dir/*
%_infodir/*.info*
%dir %allconfdir
%config(noreplace) %allconfdir/login.config
%config(noreplace) %allconfdir/%name.config
%config(noreplace) %allconfdir/dialin.config
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_logdir/%name

%files sendfax
%_spooldir/fax
%_bindir/kvg
%_bindir/newslock
%_bindir/g3cat
%_bindir/sff2g3
%_bindir/g32pbm
#_bindir/g3topbm	# /*G*/ conflicts with netpm
%_bindir/pbm2g3
%_bindir/faxspool
%_bindir/faxrunq
%_bindir/faxq
%_bindir/cutbl
%_bindir/faxrm
%_bindir/ct
%_sbindir/sendfax
%_sbindir/faxrunqd
%_sbindir/callback
%dir %alllibdir
%alllibdir/faxq-helper
%alllibdir/*.pbm
%_man1dir/g32pbm.*
%_man1dir/pbm2g3.*
%_man1dir/sff2g3.*
%_man1dir/g3cat.*
%_man1dir/%{name}_fax.*
%_man1dir/faxspool.*
%_man1dir/faxrunq.*
%_man1dir/faxq.*
%_man1dir/faxrm.*
%_man1dir/coverpg.*
%_man5dir/faxqueue.*
%_man8dir/sendfax.*
%_man8dir/faxq-helper.*
%config(noreplace) %allconfdir/sendfax.config
%config(noreplace) %allconfdir/faxrunq.config
%config(noreplace) %allconfdir/faxheader
%config(noreplace) %allconfdir/faxspool.rules.sample

%files voice
%_spooldir/voice
/sbin/vgetty
%_bindir/vm
%_bindir/pvfamp
%_bindir/pvfcut
%_bindir/pvfecho
%_bindir/pvffile
%_bindir/pvffilter
%_bindir/pvfnoise
%_bindir/pvffft
%_bindir/pvfmix
%_bindir/pvfreverse
%_bindir/pvfsine
%_bindir/pvfspeed
%_bindir/pvftormd
%_bindir/rmdtopvf
%_bindir/rmdfile
%_bindir/pvftovoc
%_bindir/voctopvf
%_bindir/pvftolin
%_bindir/lintopvf
%_bindir/pvftobasic
%_bindir/basictopvf
%_bindir/pvftoau
%_bindir/autopvf
%_bindir/pvftowav
%_bindir/wavtopvf
%_man1dir/zplay.*
%_man1dir/pvf.*
%_man1dir/pvfamp.*
%_man1dir/pvfcut.*
%_man1dir/pvfecho.*
%_man1dir/pvffile.*
%_man1dir/pvffilter.*
%_man1dir/pvffft.*
%_man1dir/pvfmix.*
%_man1dir/pvfnoise.*
%_man1dir/pvfreverse.*
%_man1dir/pvfsine.*
%_man1dir/pvfspeed.*
%_man1dir/pvftormd.*
%_man1dir/rmdtopvf.*
%_man1dir/rmdfile.*
%_man1dir/pvftovoc.*
%_man1dir/voctopvf.*
%_man1dir/pvftolin.*
%_man1dir/lintopvf.*
%_man1dir/pvftobasic.*
%_man1dir/basictopvf.*
%_man1dir/pvftoau.*
%_man1dir/autopvf.*
%_man1dir/pvftowav.*
%_man1dir/wavtopvf.*
%_man8dir/vgetty.*
%config(noreplace) %allconfdir/voice.conf

%files viewfax
%_bindir/viewfax
%_man1dir/viewfax.*
%dir %alllibdir
%alllibdir/viewfax.tif
%doc frontends/X11/viewfax/{ChangeLog,README}

%files doc
%doc BUGS ChangeLog FTP THANKS TODO Recommend README.CID
%doc doc/{modems.db,*.txt,fhng-codes}
#doc doc/*.ps
%doc samples contrib

#
# TODO:
# - Update or remove patches:
#   o mgetty-1.1.24-texinfo.patch
#   o mgetty-1.1.24-faxprint.patch
# - Consider Gentoo patches

%changelog
* Wed Dec 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.1-alt1
- Updated to upstream version 1.2.1 (Fixes: CVE-2018-16741, CVE-2018-16742,
  CVE-2018-16743, CVE-2018-16744, CVE-2018-16745, CVE-2019-1010189, CVE-2019-1010190).

* Sat Feb 02 2019 Michael Shigorin <mike@altlinux.org> 1.1.37-alt2
- fix build without texi2roff

* Thu Dec 13 2018 Michael Shigorin <mike@altlinux.org> 1.1.37-alt1.1.1.1
- fix build with gcc7/lcc-1.23 with fedora patch

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.37-alt1.1.1
- NMU: added BR: texinfo

* Sat May 05 2012 Michael Shigorin <mike@altlinux.org> 1.1.37-alt1.1
- doc subpackage made noarch
- vgetty(8) manpage duplicate no longer shipped with mgetty,
  as it really belongs to mgetty-voice subpackage

* Sat May 05 2012 Michael Shigorin <mike@altlinux.org> 1.1.37-alt1
- 1.1.37-Jun05
- build docs

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.1.36-alt1
- NMU: 1.1.36
- patch12, patch41 merged upstream
- micro spec cleanup

* Tue Oct 06 2009 Grigory Batalov <bga@altlinux.ru> 1.1.35-alt2
- Rebuild with texlive.
- Remove obsolete install_info calls.
- mgetty-sendfax conflicts with efax due to %_spooldir/fax ownership.

* Sat Dec 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.35-alt1.1
- NMU: updated build dependencies

* Mon Nov 26 2007 Slava Semushin <php-coder@altlinux.ru> 1.1.35-alt1
- Updated to 1.1.35
- Spec cleanup
- Disabled mgetty-1.1.24-faxprint.patch (need more investigation)

* Thu Mar 29 2007 Michael Shigorin <mike@altlinux.org> 1.1.31-alt1.1
- NMU: an attempt to fix x86_64 build
  + updated patch5
- added gentoo patches
- spec fixes

* Sat Jan 29 2005 Fr. Br. George <george@altlinux.ru> 1.1.31-alt1
- Version upping
- Fedora core patches applied (1.1.31-2)

* Mon Jun 07 2004 Fr. Br. George <george@altlinux.ru> 1.1.30-alt3
- Removing g3topbm again (conflicts with netpbm)

* Fri Jun 04 2004 Fr. Br. George <george@altlinux.ru> 1.1.30-alt2
- Minor voice.conf bug fixed

* Tue Feb 03 2004 Fr. Br. George <george@altlinux.ru> 1.1.30-alt1
- Using new version mgetty 1.1.30

* Fri Nov 15 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.1.28-alt3
- Rebuilt in new environment

* Mon Jul 08 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.1.28-alt2
- Some path fixes
- Fixed log file creating and using

* Mon Mar 04 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.1.28-alt1
- 1.1.28

* Fri Dec 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.27-alt2
- Fixed conflict with netpbm (in filelist)

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.27-alt1
- 1.1.27
- Fixed filelist

* Tue Oct 16 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.26-alt2
- Added patches to use AON's in USR Courier's with some russian firmware
  from Sir Raorn
- Changes to new /var/lock/serial scheme
- Some spec cleanup

* Thu May 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.26-alt1
- Using new version mgetty 1.1.26
- Fixed log messages sending to syslog

* Wed Feb 28 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.1.25-ipl2mdk
- Added latest voice patch
- Fixed detecting USR Courier modems with russian firmware
- Added -DFIDO flag

* Sun Feb 04 2001 Dmitry V. Levin <ldv@fandra.org> 1.1.25-ipl1mdk
- 1.1.25
- Added faxprint patch.

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 1.1.24-ipl1mdk
- RE adaptions.
- Texinfo patch.
- Real FHSification.
- Improved logrotate support.
- Merged RH patched.

* Wed Jan 10 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.1.24-1mdk
- 1.1.24 (security fixes for tmpfile insecurities)

* Wed Jan 10 2001 Yves Duret <yduret@mandrakesoft.com> 1.1.22-3mdk
- macros
- s/Copyright/License/

* Tue Sep 26 2000 Etienne Faure  <etienne@mandraksoft.com> 1.1.22-2mdk
- Added (noreplace) tag to conffiles

* Thu Aug 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.22-1mdk
- 1.1.22 fix security.

* Tue Aug 29 2000 Etienne Faure <etienne@mandrakesoft.com> 1.1.21-8mdk
- use the _mandir & _infodir macros

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.1.21-7mdk
- automatically added BuildRequires

* Thu Jul 19 2000 Etienne Faure <etienne@mandrakesoft.com> 1.1.21-6mdk
- rebuild on kenobi
- Changed permission of source files: 664 -> 644

* Fri Mar 31 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.1.21-5mdk
- group fix.

* Fri Nov 26 1999 Florent Villard <warly@mandrakesoft.com>
- Mandrake adaptation
- clean the install script

* Sun Aug 15 1999 Nick Urbanik <nicku@vtc.edu.hk>
- Signed it.

* Sat Aug 14 1999 Nick Urbanik <nicku@vtc.edu.hk>
- updated to 1.1.21
- Created the contrib package (marginally worthwhile)
- Added more documentation to mgetty
- Added more programs to sendfax and voice.

* Tue Apr  6 1999 Bill Nottingham <notting@redhat.com>
- strip setuid bit from ct

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- better log handling

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- rebuild for glibc 2.1

* Sat Aug 22 1998 Jos Vos <jos@xos.nl>
- Use a patch for creating policy.h using policy.h-dist.
- Add viewfax subpackage (X11 fax viewing program).
- Add logrotate config files for mgetty and sendfax log files.
- Properly define ECHO in Makefile for use with bash.
- Add optional use of dialin.config (for modems supporting this).
- Change default notification address to "root" (was "faxadmin").
- Change log file names according to better defaults.
- Change default notify program to /etc/mgetty+sendfax/new_fax (was
  /usr/local/bin/new_fax).

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- add faxrunqd man page (problem #850)
- add missing pbm2g3 (and man page); remove unnecessary "rm -f pbmtog3"
- delete redundant ( cd tools; make ... )

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.1.14
- AutoPPP patch

* Thu Dec 18 1997 Mike Wangsmo <wanger@redhat.com>
- added more of the documentation files to the rpm

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info support

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- updated version

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- now requires libgr-progs instead of netpbm

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- built against glibc
