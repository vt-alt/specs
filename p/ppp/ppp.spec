%def_disable static

%def_with pam
%def_with cbcp
%def_with chapms
%def_with mppe
%def_with libatm
%def_with inet6
%def_with systemd
# https://bugzilla.redhat.com/1556132
%def_without crypt

Name: ppp
Version: 2.4.7
Release: alt6

Summary: The PPP daemon and documentation
License: distributable
Group: System/Servers

Url: http://ppp.samba.org

Source0: %name-%version.tar
Source2: ppp.pamd
Source4: ppp.control
Source5: ppp.logrotate
Source6: ppp.tmpfiles
Source7: 95-ppp.rules

# eaptls and openssl need manual conflict resolution
# TODO: %%def_with'ize those?
Patch1: %name-%version-%release.patch

PreReq: %_lockdir/serial
Obsoletes: ppp-cbcp, ppp-mppe
Obsoletes: ppp-extra

BuildRequires: libpam-devel libpcap-devel libssl-devel perl-IPC-Signal perl-Proc-Daemon perl-Proc-WaitStat libudev-devel
%{?_with_libatm:BuildRequires: libatm-devel}
%{?_with_systemd:BuildRequires: libsystemd-devel}
Requires: ppp-common libssl
Requires: kmod >= 14
Requires: udev >= 204-alt2


%add_findprov_lib_path %_libdir/pppd/%version


%package devel
Summary: Header files needed for building extra pppd plugins
Group: Development/C
Requires: %name = %version-%release
BuildArch: noarch

%package radius
Summary: RADIUS authentication plugin for pppd
Group: System/Servers
Requires: %name = %version-%release

%package pppoatm
Summary: PPP over ATM plugin for pppd
Group: System/Servers
Requires: %name = %version-%release


%package pppoe
Summary: PPP over ethernet plugin for pppd
Group: System/Servers
Requires: %name = %version-%release

%package dhcp
Summary: DHCP plugin for %{name}
Group: System/Servers
Requires: %name = %version-%release

%description
The %name package contains the PPP (Point-to-Point Protocol) daemon
and documentation for PPP support.  The PPP protocol provides a
method for transmitting datagrams over serial point-to-point links.

The %name package should be installed if your machine need to support
the PPP protocol.

%description devel
Header files needed for building extra pppd plugins.

%description radius
The Remote Authentication Dial In User Service (RADIUS) plugin for pppd
permits pppd to perform PAP, CHAP, MS-CHAP and MS-CHAPv2 authentication
against a RADIUS server instead of the usual /etc/ppp/pap-secrets and
/etc/ppp/chap-secrets files.

%description pppoatm
PPP over ATM plugin for pppd.

%description pppoe
PPP over ethernet plugin for pppd.

%description    dhcp
DHCP plugin for pppd.


%prep
%setup
%patch1 -p1

#set the right paths in radiusclient.conf
sed -i -e "s|/usr/local/etc|%_sysconfdir|" \
	     -e "s|/usr/local/sbin|%_sbindir|" pppd/plugins/radius/etc/radiusclient.conf
#set config dir to /etc/ppp/radius
sed -i -e "s|/etc/radiusclient|/etc/ppp/radius|g" \
		pppd/plugins/radius/{*.8,*.c,*.h} \
		pppd/plugins/radius/etc/*

find -type f -name \*.orig -print -delete
rm -f include/linux/if_pppol2tp.h

%build
%add_optflags -fPIC -Wall -D_GNU_SOURCE -fno-strict-aliasing
%configure
%make_build %{?_with_pam:USE_PAM=y} \
	    %{?_with_cbcp:CBCP=y} \
	    %{?_with_chapms:CHAPMS=y} \
	    %{?_with_crypt:USE_CRYPT=y} \
	    %{?_with_mppe:MPPE=y} \
	    %{?_with_libatm:HAVE_LIBATM=y} \
	    %{?_with_inet6:HAVE_INET6=y} \
	    %{?_with_systemd:SYSTEMD=y} \
	    COPTS="%optflags" \
	    CC="gcc" \
	    libdir=%_libdir

%install
%make_install install 	DESTDIR=%buildroot \
			BINDIR=%buildroot%_sbindir \
			INCDIR=%buildroot%_includedir \
			libdir=%_libdir \
			MANDIR=%buildroot%_man8dir \
			RUNDIR=%buildroot%_var/run/ppp \
			LOGDIR=%buildroot%_logdir/ppp
%make_install install-etcppp INSTROOT=%buildroot \
			ETCDIR=%buildroot%_sysconfdir/%name

for f in `find scripts/ sample/ -type f`; do
	chmod 644 "$f"
	if fgrep -qs /usr/local/bin/ "$f"; then
		subst -p 's|/usr/local/bin|%_bindir|g' "$f"
	fi
	if file -b "$f" |fgrep -qs 'shell script'; then
		chmod a+x "$f"
	fi
done

install -pDm640 %SOURCE2 %buildroot%_sysconfdir/pam.d/%name

mkdir -p %buildroot%_sysconfdir/%name/peers
install -pm600 sample/callback-* %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_sysconfdir/%name/radius
cp -a pppd/plugins/radius/etc/* %buildroot%_sysconfdir/%name/radius/

install -pDm755 %SOURCE4 %buildroot%_controldir/%name

# Provide pointers for people who expect stuff in old places
mkdir -p %buildroot{%_logdir,%_var/run}/%name
touch %buildroot%_logdir/%name/connect-errors
touch %buildroot%_var/run/%name/resolv.conf

ln -s ../..%_logdir/%name/connect-errors %buildroot%_sysconfdir/%name/connect-errors
ln -s ../..%_var/run/%name/resolv.conf %buildroot%_sysconfdir/%name/resolv.conf

install -pDm644 %SOURCE6 %buildroot/%_tmpfilesdir/%name.conf
install -pDm644 %SOURCE7 %buildroot/%_udevrulesdir/95-%name.rules

# Logrotate script
install -pDm644 %SOURCE5 %buildroot%_sysconfdir/logrotate.d/%name

# Install EAP-TLS config examples
install -pm600 etc.ppp/openssl.cnf %buildroot%_sysconfdir/%name/openssl.cnf

%pre
%pre_control %name

%post
%post_control -s traditional %name

%files
%attr(711,root,root) %_sbindir/*
%exclude %_sbindir/pppoe-discovery
%attr(700,root,root) %dir %_logdir/%name
%attr(755,root,root) %dir %_sysconfdir/%name
%attr(711,root,root) %dir %_sysconfdir/%name/peers
%attr(600,root,root) %config(noreplace) %_sysconfdir/%name/*-secrets
%attr(600,root,root) %config(noreplace) %_sysconfdir/%name/eaptls-*
%attr(600,root,root) %config(noreplace) %_sysconfdir/%name/openssl*
%attr(750,root,root) %config(noreplace) %_sysconfdir/%name/callback-*
%attr(644,root,root) %config(noreplace) %_sysconfdir/%name/options
%attr(600,root,root) %_sysconfdir/%name/connect-errors
%attr(644,root,root) %_sysconfdir/%name/resolv.conf
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/pam.d/%name
%_tmpfilesdir/%name.conf
%_udevrulesdir/95-%name.rules
%config %_controldir/%name
%_libdir/pppd
%_var/run/%name
%_logdir/%name/*
%{?_with_libatm:%exclude %_libdir/pppd/%version/pppoatm.so}
%exclude %_libdir/pppd/%version/rp-pppoe.so
%exclude %_libdir/pppd/%version/rad*
%exclude %_libdir/pppd/%version/dhcpc.so
%_man8dir/*.8*
%exclude %_man8dir/*rad*
%exclude %_man8dir/pppoe-discovery*
%doc PLUGINS SETUP FAQ README* scripts sample

%files devel
%_includedir/pppd

%if_with libatm
%files pppoatm
%_libdir/pppd/%version/pppoatm.so
%endif

%files pppoe
%_libdir/pppd/%version/rp-pppoe.so
%attr(755,root,root) %_sbindir/pppoe-discovery
%_man8dir/pppoe-discovery*

%files radius
%_libdir/pppd/%version/rad*.so
%_man8dir/*rad*
%config(noreplace) %_sysconfdir/%name/radius/

%files dhcp
%doc pppd/plugins/dhcp/README
%doc pppd/plugins/dhcp/AUTHORS
%doc pppd/plugins/dhcp/COPYING
%_libdir/pppd/%version/dhcpc.so

%changelog
* Tue Mar 10 2020 Alexey Shabalin <shaba@altlinux.org> 2.4.7-alt6
- Fixed: CVE-2020-8597

* Tue Oct 02 2018 Alexey Shabalin <shaba@altlinux.org> 2.4.7-alt5
- update to ppp-2.4.7-eaptls-mppe-1.101.patch
- backport patches from upstream master
- build with libsystemd for option up_sdnotify

* Sun Jul 15 2018 Michael Shigorin <mike@altlinux.org> 2.4.7-alt4
- fixed ftbfs against current libcrypt with fedora patch (thx ldv@)
- fixed libatm knob

* Mon Jan 29 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4.7-alt3
- Fixed build with modern kernel headers.

* Fri Jan 30 2015 Andriy Stepanov <stanv@altlinux.ru> 2.4.7-alt2
- Fix openl2tp socket path

* Thu Jan 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.7-alt1
- 2.4.7
- add udev rules for set GROUP=uucp (ALT #29457)

* Wed Oct 09 2013 Alexey Shabalin <shaba@altlinux.ru> 2.4.5-alt13
- drop /lib/udev/devices/ppp

* Tue Oct 08 2013 Alexey Shabalin <shaba@altlinux.ru> 2.4.5-alt12
- don't need create /dev/ppp with kmod >= 14
- ppp-2.4.5-eaptls-mppe-0.993.patch

* Thu Sep 06 2012 Mikhail Efremov <sem@altlinux.org> 2.4.5-alt11
- Enable IPv6 support (closes: #27707).

* Wed Jun 13 2012 Alexey Shabalin <shaba@altlinux.org> 2.4.5-alt10
- mv /etc/tmpfiles.d/ppp.conf -> /lib/tmpfiles.d/ppp.conf.
- update tmpfiles for create a character device /dev/ppp.

* Sun May 22 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.5-alt9
- update upstream snapshot
- merge all git branches to patches/alt-all_patches
- add config for systemd-tmpfiles
- fix link with libcrypto radius plugin
- Debian patches:
  + radius plugin enhancements
  + fix segfault in update_db_entry()
  + make sure that the linkpidfile is always created
  + using rp-pppoe pppd exits with EXIT_OK after receiving a timeout waiting
  + be sure to close /dev/ppp when reconnecting
  + always create a new process group

* Fri Mar 04 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.5-alt8
- add device to /lib/udev/devices/ppp for udev

* Tue Nov 16 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4.5-alt7
- upstream snapshot
- update eaptls patch to v0.99
- fix build pppol2tp

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 2.4.5-alt6
- oops, synchrobumped release for pptpd
- devel subpackage made noarch

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 2.4.5-alt5.1
- rebuilt against openssl-1.0.0a

* Tue Jun 29 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4.5-alt5
- upstream snapshot cab58617fd9d328029fffabc788020264b4fa91f
- ppp.pamd: use common-login
- update eaptls patch to v0.98
- fixes RH#560014 - SELinux is preventing /usr/sbin/pppd "read write" access on pppd2.tdb
- added pppoe-discovery(8) (ppp-2.4.5-manpg.patch from fedora)

* Sat Jan 16 2010 Michael Shigorin <mike@altlinux.org> 2.4.5-alt4
- rebuilt

* Wed Jan 13 2010 Michael Shigorin <mike@altlinux.org> 2.4.5-alt3
- re-added cbcp.h (#12368, thanks sem@ for spotting)

* Wed Jan 13 2010 Michael Shigorin <mike@altlinux.org> 2.4.5-alt2
- reworked branching
- minor spec cleanup

* Mon Dec 28 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.5-alt1
- 2.4.5
- update eaptls patch to v0.95
- drop broken patches

* Fri May 15 2009 Michael Shigorin <mike@altlinux.org> 2.4.4-alt12
- fixed FTBFS with current libtool

* Wed Oct 15 2008 Michael Shigorin <mike@altlinux.org> 2.4.4-alt11
- rebuilt for Sisyphus, thanks ender@

* Tue Oct 14 2008 Afanasov Dmitry <ender@altlinux.org> 2.4.4-alt10.3
- define aligned_u64 in pppoe.c to fix building

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 2.4.4-alt10.2
- include pppoe-discovery only in pppoe subpackage

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 2.4.4-alt10.1
- fix build

* Sun Dec 09 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt10
- rebuild

* Sat Dec 08 2007 Michael Shigorin <mike@altlinux.org> 2.4.4-alt9.9
- added updated ppp-2.4.3-dontwriteetc.patch from Mandriva
  as ppp-2.4.4-dontwriteetc.patch (#8386)
  + NB: %_sysconfdir/%name/connect-errors and %_sysconfdir/%name/resolv.conf
    now moved to %_var, symlinks are instead; if there was anything 
    valuable there, please backup *before* upgrading (shouldn't be)
- added logrotate script (from Mandriva thus RH)
- added updated ppp-2.4.2-minunit.patch (#9800)
  as ppp-2.4.4-alt-minunit.patch
  (modified to apply on top of current patchset)
- added updated ppp-2.4.4-alt-ipparam.patch (#10270)
- basic testing passed

* Sat Dec 08 2007 Michael Shigorin <mike@altlinux.org> 2.4.4-alt9.8
- merged control facility from jinn@'s ppp-control
  + facility renamed from pppd to %name
  + pay attention to status renaming with new facility name:
    "public" is now "traditional" (0711 root:root)
    "legacy" is now "public"      (4711 root:root)
  + added "uucp" status           (4710 root:uucp)
  + default is "traditional" (corresponding to packaged permissions)
    -- thanks ldv@ for comments on naming
- changed default %_sbindir/* permissions from 755 to 711
  so that default status is coherent
- added "nopredictor1" to default %_sysconfdir/%name/options (#4239)
- replaced patch9 (cleardefaultroute option implementation)
  with patch51 ([no]replacedefaultroute from Debian) (#9256)
  + NB: openSUSE patch from ppp-2.4.4-79 seems broken,
    while almost the same one from ppp_2.4.4rel-9 in Debian
    just works
  + there's no mention of (now obsolete) custom cleardefaultroute
    in etcnet scripts but there might be another ALT-specific
    patches or configuration files where it might appear; please
    file bugs against such packages and Cc: me too
- spec macro abuse cleanup
- basic testing passed

* Sun Dec 02 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt9
- Fix buffer overflow in radius plugin

* Sat Sep 29 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt8
- Rebuild

* Thu Sep 27 2007 Michael Shigorin <mike@altlinux.org> 2.4.4-alt7.1
- updated patch18 as patch49 (see comments where it gets applied)
- added Packager:

* Tue Aug 07 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt7
- Rebuild

* Tue Aug 07 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 2.4.4-alt6
- Install cbcp.h (Closes: #12368)

* Mon Jun 25 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt5
- Add eaptls support (Michael A. Kangin)

* Sat May 12 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt4
- Patch for CBCP patch. Now CBCP server works and always accepts "no callback"
  users (hiddenman@)
- Fixed CBCP patch by patch46. It shouldn't break chat now (hiddenman@)
- Build without patch15 (mppe+mppc) (hiddenman@)
- Completely disable commented patches (hiddenman@)

* Sun Apr 29 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt3
- Add reworked by Andrew Kornilov CBCP patch from ASP Linux (disabled)
- More correct mppe+mppc patch (by Andrew Kornilov)

* Sun Apr 08 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt2
- Add requires to ppp-common (#11382)

* Sun Mar 25 2007 Denis Smirnov <mithraen@altlinux.ru> 2.4.4-alt1
- Build 2.4.4 for Sisyphus

* Mon Mar 19 2007 Alexey Shabalin <shaba@altlinux.ru> 2.4.4-alt0.1
- 2.4.4 (Sorry - normal changelog after ...)
- fix for #11110 (cbcp)

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 2.4.2-alt7 
- Create linkpidfile when start pppd, not when connected (Valentin Lavrinenko)
- do not ignore SIGTERM before chat started (Valentin Lavrinenko)

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.4.2-alt6.1.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Sat Nov 05 2005 LAKostis <lakostis at altlinux.ru> 2.4.2-alt6.1
- add missing requires for libradiusclient-devel.
- disable -static build by default.

* Wed Mar 23 2005 Kachalov Anton <mouse@altlinux.ru> 2.4.2-alt6
- enable Radius plugin

* Fri Mar 18 2005 Kachalov Anton <mouse@altlinux.ru> 2.4.2-alt5
- disable MPPE/MPPC patch
- disable Radius plugin

* Sun Feb 13 2005 Kachalov Anton <mouse@altlinux.ru> 2.4.2-alt4
- added MPPE/MPPC support: by default, it's disabled

* Thu Feb 10 2005 Kachalov Anton <mouse@altlinux.ru> 2.4.2-alt3
- x86_64 support (#6088)

* Tue Jun 08 2004 Alexey Voinov <voins@altlinux.ru> 2.4.2-alt2
- killmypg added. [fixes some race conditions in signal handlers]
- holdoffhack added [fix for #1589]

* Fri May 28 2004 Alexey Voinov <voins@altlinux.ru> 2.4.2-alt1
- new version (2.4.2)
- patches updated [note: README.cbcp from asp path has been dropped :(]
- asp-radius-chap patch has been merged into upstream
- optsigsegv patch added [fix for #1158]
- buildreqs updated

* Wed Dec 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.1.20031003-alt2
- Implemented cleardefaultroute option (#3319).
- Do not package .la files.

* Wed Nov 12 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.1.20031003-alt1
- Updated to cvs snapshot 20031003.
- Build the radius plugin with libradiusclient dynamically,
  to avoid text relocations.
- Fixed the radius plugin to use new chap auth (ASP Linux).

* Wed Oct 08 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.1.20030923-alt1
- Updated to cvs snapshot 20030923.
- ppp-extra: fixed package dependencies.

* Tue Oct 07 2003 Victor V Ismakaev <ivv@altlinux.ru> 2.4.1.20030513-alt3
- Build with radius support.
- Added experimental CBCP support (ASP Linux) and enabled it by default.

* Thu Jul 17 2003 Alexey Voinov <voins@altlinux.ru> 2.4.1.20030513-alt2
- fixed permissions for /etc/ppp/peers to 711
- added opts patch (noauth and noipdefault into /etc/ppp/options)

* Sat May 24 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.1.20030513-alt1
- Updated to 2.4.2b3+ (snapshot 20030513).
- Rediffed patches, only five of them left.
- Packaged plugins.
- PAM configuration policy enforcement.
- Dropped pppgetpass.
- Packaged ppp-radius and radiusclient libraries (not enabled by default).

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt8
- Rebuilt in new environment
- Changed pppd URL
- Changed version string
- Added devel package - it contains headers from pppd

* Wed May 22 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt7
- Removed requires to glibc & pam & kernel - now it's bad requires...

* Mon Jan 21 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt6
- Fixed permissions on %_sysconfdir/%name/callback-* - now it's 750.
- Fixed patch5 - atdt->atdp

* Wed Jan 16 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt5
- Removed MPPE & CBCP builddefs - now these features compiled in standart
  CBCP package
- Added some patches from ASP Linux

* Tue Oct 16 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt4
- Changes to new /var/lock/serial scheme

* Fri Aug 03 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt3.2
- Added MPPE support

* Thu Aug 02 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt3.1
- Some fixes to CBCP patch
- Added DEBUG_CBCP define
- Fixed spec file

* Wed Jul 04 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt3
- Fixed CBCP debug messages
- Added option to BUILD_CBCP
- Placed CBCP configs in right place
- Updated CBCP from Bolke de Bruin release
- Added noresolv patch
- Some spec cleanup
- Added pppgetpass program from contrib

* Thu Jun 14 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt2
- Fixed CBCP_SUPPORT in Makefile

* Mon May 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.4.1-alt1
- Updated 2 new version
- Fixed cbcp compiling

* Fri Oct 13 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.0-ipl2mdk
- Updated pam configuration.

* Wed Aug 9 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.0-ipl1mdk
- Updated to 2.4.0.

* Thu Jul 13 2000 Dmitry V. Levin <ldv@fandra.org> 2.4.0b2-ipl1mdk
- Updated to 2.4.0b2.
- Patched samples to avoid unnecessary dependencies.
- Added zlib patch from James Carlson <james.d.carlson@east.sun.com>
  (see ftp://playground.sun.com/pub/carlsonj/zlib-bug.notes for details).
- Moved scripts and samples to separate package to split dependencies.

* Mon Apr 03 2000 Dmitry V. Levin <ldv@fandra.org>
- Added: noresolvconf option support.

* Thu Mar 09 2000 Dmitry V. Levin <ldv@fandra.org>
- Fixed check for pam_open_session result code
  (by Leon Kanter <leon@blackcatlinux.com>).
- Merge with Mandrake.

* Sun Jan 02 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.3.11

* Thu Nov 11 1999 Dmitry V. Levin <ldv@fandra.org>
- Merge with RH.

* Sun Oct 17 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.

* Mon Sep 20 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Fix %%post ??

* Mon Sep 20 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Fix %%post

* Mon Sep 20 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- -DCHAPMS
- -DUSE_PAM

* Tue Sep  7 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Add /dev/ppp
- Add entries in /etc/conf.modules if they aren't there yet

* Wed Aug 25 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 2.3.9 (required for kernel 2.3.14+)

* Thu Jul 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Removing unused stuff.
- Upgrade patch.
- 2.3.8.

* Sat Jul 10 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Define the .pid to /var/run/
- Glare @Chmouel

* Fri Jul 09 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Define the .pid to /var/run not to /etc/ (reported by Nikodemus Karlsson
  <nickek@algonet.se>).

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- force pppd use the glibc's logwtmp instead of implementing its own

* Thu Apr 01 1999 Preston Brown <pbrown@redhat.com>
- version 2.3.7 bugfix release

* Tue Mar 23 1999 Cristian Gafton <gafton@redhat.com>
- version 2.3.6

* Mon Mar 22 1999 Michael Johnson <johnsonm@redhat.com>
- auth patch

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Fri Jun  5 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.3.5.

* Tue May 19 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Fri May  8 1998 Jakub Jelinek <jj@ultra.linux.cz>
- make it run with kernels 2.1.100 and above.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Mar 18 1998 Cristian Gafton <gafton@redhat.com>
- requires glibc 2.0.6 or later

* Wed Mar 18 1998 Michael K. Johnson <johnsonm@redhat.com>
- updated PAM patch to not turn off wtmp/utmp/syslog logging.

* Wed Jan  7 1998 Cristian Gafton <gafton@redhat.com>
- added the /etc/pam.d config file
- updated PAM patch to include session support

* Tue Jan  6 1998 Cristian Gafton <gafton@redhat.com>
- updated to %name-2.3.3, build against glibc-2.0.6 - previous patches not
  required any more.
- added buildroot
- fixed the PAM support, which was really, completely broken and against any
  standards (session support is still not here... :-( )
- we build against running kernel and pray that it will work
- added a samples patch; updated glibc patch

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- added a patch to use our own route.h, rather then glibc's (which has
  alignment problems on Alpha's) -- I only applied this patch on the Alpha,
  though it should be safe everywhere

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- turned off the execute bit for scripts in %prefix/doc

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Integrated new patch from David Mosberger
- Improved description
