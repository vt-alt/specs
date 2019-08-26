Name: iputils
%define timestamp 20190709
Version: %timestamp
Release: alt1

Summary: Utilities for IPv4/IPv6 networking
License: %bsd, %gpl2plus, AS-IS (SUN MICROSYSTEMS license)
Group: Networking/Other
Url: https://github.com/iputils/iputils

Source0: %name-%version.tar
Source1: ping.control
Source2: ninfod.init
Patch: %name-%version-%release.patch

Conflicts: netkit-base

Requires(pre): shadow-utils
Requires(pre): control >= 0.8.0-alt1
Requires: /var/resolv

BuildRequires(pre): rpm-build-licenses meson

BuildRequires: libcap-devel
BuildRequires: libsysfs-devel libssl-devel
BuildRequires: libidn2-devel
BuildRequires: docbook5-style-xsl xsltproc

%define _unpackaged_files_terminate_build 1

%define sysctl_conf_file %_sysctldir/70-iputils.conf
%define ping_real_dir %_usr/libexec/ping

%description
The iputils package contains basic utilities for monitoring a network:
+ clockdiff - measures clock difference;
+ ping/ping6 - sends ICMP ECHO_REQUEST packets to network hosts;
+ arping - ping by ARP packets;
+ rdisc - classic router discovery daemon;
+ tracepath/tracepath6 - traces path to destination discovering MTU
along this path.

%package -n ninfod
Group: Networking/Other
Summary: Node Information Query Daemon
License: %bsd

%description -n ninfod
Node Information Query (RFC4620) daemon. Responds to IPv6 Node Information
Queries.

%prep
%setup
%patch -p1

%build
%add_optflags -fno-strict-aliasing -Wstrict-prototypes -Werror
%ifarch s390 s390x
	%add_optflags -fPIE
%else
	%add_optflags -fpie
%endif

export LDFLAGS='-pie'
%meson \
	-DBUILD_TFTPD=false \
	-Dsystemdunitdir=%_unitdir \
	-DNO_SETCAP_OR_SUID=true \
	-DUSE_CAP=true \
	-DUSE_IDN=true \
	-DUSE_CRYPTO=openssl \
	-DUSE_GETTEXT=false

%meson_build -v

%install
%meson_install
mkdir -p %buildroot%ping_real_dir/
mv %buildroot%_bindir/ping %buildroot%ping_real_dir/
ln -s %ping_real_dir/ping %buildroot%_bindir/ping
ln -s %ping_real_dir/ping %buildroot%_bindir/ping6

install -pD -m755 %SOURCE1 %buildroot%_controldir/ping

mkdir -p %buildroot%_sysctldir/
touch %buildroot%sysctl_conf_file

install -pD -m755 %SOURCE2 %buildroot%_initdir/ninfod

ln -s tracepath %buildroot%_bindir/tracepath6
# for backward compatibility
mkdir -p %buildroot/bin/
for p in ping ping6 tracepath tracepath6; do
	ln -s %_bindir/"$p"  %buildroot/bin/"$p"
done

%pre
groupadd -r -f iputils ||:
useradd -r -g iputils -d /dev/null -s /dev/null -n iputils >/dev/null 2>&1 ||:
groupadd -r -f netadmin ||:

%pre_control ping

%post
# net.ipv4.ping_group_range controls both IPv4 and IPv6 sockets
if [ ! -e %sysctl_conf_file ]; then
	ALLOW_GID="$(getent group iputils | cut -f3 -d:)" ||:
	if [ -n "$ALLOW_GID" ]; then
		cat >%_sysctldir/70-iputils.conf <<EOF
# Allow ping socket creation for group iputils
net.ipv4.ping_group_range = $ALLOW_GID $ALLOW_GID
EOF
		sysctl -p %sysctl_conf_file ||:
	fi
fi

%post_control ping

# There is no rdisk init script
if sd_booted; then
	%post_service rdisc
fi

%preun
if sd_booted; then
	%preun_service rdisc
fi

%post -n ninfod
%post_service ninfod

%preun -n ninfod
%preun_service ninfod

%files
%config %_controldir/ping
%attr(700,root,netadmin) %verify(not mode) %dir %ping_real_dir/
%attr(2711,root,iputils) %ping_real_dir/ping
%ghost %config %sysctl_conf_file
/bin/*
%_bindir/*
%_unitdir/rdisc.service
%_sbindir/*
%_mandir/man?/*
%exclude %_sbindir/ninfod
%exclude %_man8dir/ninfod.*

%files -n ninfod
%doc ninfod/COPYING
%_unitdir/ninfod.service
%_initdir/ninfod
%_sbindir/ninfod
%_man8dir/ninfod.*

%changelog
* Thu Aug 22 2019 Mikhail Efremov <sem@altlinux.org> 20190709-alt1
- 20190515 -> 20190709.

* Fri May 17 2019 Mikhail Efremov <sem@altlinux.org> 20190515-alt1
- Fix docs build.
- 20190324 -> 20190515.

* Sun Mar 31 2019 Mikhail Efremov <sem@altlinux.org> 20190324-alt2
- Don't package tftpd (closes: #36477).

* Wed Mar 27 2019 Mikhail Efremov <sem@altlinux.org> 20190324-alt1
- ping: Fix use-after-free.
- ninfod: Drop modcap.c usage.
- Add ninfod init script.
- Don't use deprecated PreReq.
- arping: Fix packets count.
- Add note about net.ipv4.ping_group_range.
- Package rdisc.service and ninfod.service.
- meson: Fix rdisc unit file.
- meson: Install clockdiff and arping to sbindir.
- meson: Fix systemd detection.
- ping6_common.c: Fix include.
- arping: Drop unused variable.
- Build with -Werror.
- Update spec for meson build.
- Drop patches from upstream git.
- meson: Fix build with meson.
- all: Fix checks for libcap.
- 20180629 -> 20190324.

* Fri Mar 22 2019 Mikhail Efremov <sem@altlinux.org> 20180629-alt2
- Ptaches from upstream:
  + Fix Rounding Issue #123.
  + fix ping duration time error.
  + ping: do not bind to device when destination IP is on device.
  + ping: check getifaddrs(3) ifa_name data before use.
- ping: Fix interface names comparison.
- modcap: Drop useless getgid().
- modcap: Don't use GID 0 if started as root.

* Thu Aug 30 2018 Mikhail Efremov <sem@altlinux.org> 20180629-alt1
- Update licenses.
- Update url.
- Patch from upstream:
  + tracepath: Fix copying input IPv6 address.
- 20161105 -> 20180629.

* Fri Jan 26 2018 Mikhail Efremov <sem@altlinux.org> 20161105-alt3
- Add {public,netadmin}_caps facilities (closes: #34163).
- Patches from upstream:
  + Use libidn2 instead of libidn.
  + Fix ping to local IPv6 interfaces.

* Thu Sep 21 2017 Mikhail Efremov <sem@altlinux.org> 20161105-alt2
- Add /bin/* symlinks.

* Mon Sep 18 2017 Mikhail Efremov <sem@altlinux.org> 20161105-alt1
- Rename in.rdisc -> rdisc.
- Package ninfod.
- Drop ifenslave.
- ping: Drop capabilities in IPv4 mode.
- Rewrite old ALT droppriv patch.
- Updated patches descriptors fix.
- Updated to 20161105 (closes: #27995).

* Mon May 09 2011 Afanasov Dmitry <ender@altlinux.org> 20101006-alt2
- fix #25282 (thx to led@)
  + updated droppriv patch for support sysfs

* Sun Jan 23 2011 Afanasov Dmitry <ender@altlinux.org> 20101006-alt1
- version 20101006.

* Tue Sep 30 2008 Afanasov Dmitry <ender@altlinux.org> 20071127-alt4
- fix typo in control facilities descriptions

* Tue Sep 30 2008 Afanasov Dmitry <ender@altlinux.org> 20071127-alt3
- add descriptions for control facilities (fix #17321)

* Thu Sep 18 2008 Afanasov Dmitry <ender@altlinux.org> 20071127-alt2
- add bindnow patch for linking (thx to force@)
- more correct summary.
- fixed documentation build to be SMP-compatible.

* Mon Sep 15 2008 Afanasov Dmitry <ender@altlinux.org> 20071127-alt1
- version s20071127
- remove old patches
    + rh-owl-cache-reverse-lookups - replaced by fc-addrcache
    + owl-man - now man is distributed by sgml. remake patch against sgml 
      files
- add some fedora core patches
    + fc-countermeasures (print countermeasures warning in verbose only)
    + fc-addrcache
    + fc-ia64_align (call strdup on device name)
    + fc-unaligned (add warning to ping.c)
    + fc-open-max (read OPEN_MAX value from sysctl)
    + fc-ping_cleanup (more descriptive string about icmp replies)

* Wed Oct 03 2007 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt5
- Do not check kernel headers.

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 20020927-alt4.2
- moved rarpd to a package of its own;
  see http://secunia.com/advisories/25061/

* Sun Oct 15 2006 Michael Shigorin <mike@altlinux.org> 20020927-alt4.1
- use proper ifenslave.c (closes: #9695)
- disabled patch7 (doesn't apply; seems like ifenslave.c has
  changed enough so additional code review is needed to determine
  whether it's still needed or how to port it -- still unpatched
  new source is reportedly working, see the referenced bugreport)
- fixed patch5 (#7283, thanks kas@ for alert/patch^2)
- added ping6 control proposed by icesik@ (#9783)
- added Packager:

* Thu Nov 24 2005 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt4
- Relocated manual pages for commands to 1st section.

* Mon Nov 14 2005 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt3
- Removed traceroute6 in favour of the traceroute package.
- Removed backwards compatibillity symlinks from %_sbindir/.
- Removed verifying permissions and group owner for ping since it's
controlled by control(8) facility.

* Wed Aug 27 2003 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt2
- Updated build dependencies, fixed build.
- Relocated ping6, tracepath, tracepath6 and traceroute6 binaries
  from /usr/sbin to /bin; added backwards compatibility symlinks.
- Keep ping at mode 700 ("restricted") in the package, but default
  it to "public" in %%post when the package is first installed.
  This avoids a race and fail-open behavior where a "restricted"
  ping could be "public" during package upgrades (Owl).

* Wed Oct 16 2002 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt1
- Updated to ss020927 (fixes #0000711).
- Dropped ss001110-owl-warnings patch (no longer needed).
- Fixed datalen typo.
- Added group (netadmin) to restrict access to ping.
- Added control support for ping.

* Thu Apr 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt8
- arping: do drop_priv a bit later to keep functionality.
- clockdif: keep cap_net_raw capability.

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt7
- Updated droppriv patch (chroot to /var/resolv).

* Fri Apr 05 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt6
- Refined droppriv patch:
  + added file descriptors fix;
  + drop root also for tracepath and tracepath6.

* Thu Apr 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt5
- Moved ipv6calc to outstanding package.
- arping, clockdiff, ping, ping6, traceroute6: drop root also for root user.

* Tue Apr 02 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt4
- Disabled build of ipv6calc-static.
- Fixed build without kernel-source installed.

* Wed Mar 27 2002 Alexander Bokovoy <ab@altlinux.ru> 20020124-alt3
- Fixed:
    + tftpd removed from installation binaries 

* Mon Mar 25 2002 Alexander Bokovoy <ab@altlinux.ru> 20020124-alt2
- IPUtils ss020124
- IP6Calc 0.39
- Documentation now is built using SGML tools
- Various patches updated

* Thu Jan 03 2002 Stanislav Ievlev <inger@altlinux.ru> 20010805-alt2
- fixed rights on manual pages (bug  #0000292)
- fixed bonding with new interface ( 2.4.x )

* Tue Aug 14 2001 Alexander Bokovoy <ab@altlinux.ru>   20010805-alt1
- IPUtils ss010805
- Fixed: 
    + ping-deadline patch. Ping has been re-designed to eliminate this problem
    + Compiler options
    + Owl patch for ping

* Tue May 08 2001 Stanislav Ievlev <inger@altlinux.ru> 20001110-ipl2mdk
- Merge with patches from OpenWall, RH and MDK

* Fri Jan 12 2001 Dmitry V. Levin <ldv@fandra.org> 20001110-ipl1mdk
- ss001110.

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 20001011-ipl1mdk
- ss001011.
- RE adaptions.

* Tue Oct 10 2000 Jeff Johnson <jbj@redhat.com>
- update to ss001010.
- don't segfault as root with large buffers (#16677).

* Sun Oct  8 2000 Jeff Johnson <jbj@redhat.com>
- update to ss001007.

* Tue Aug  8 2000 Tim Waugh <twaugh@redhat.com>
- fix spelling mistake (#15714).

* Tue Aug  8 2000 Tim Waugh <twaugh@redhat.com>
- turn on -U on machines without TSC (#15223).

* Tue Aug  1 2000 Jeff Johnson <jbj@redhat.com>
- better doco patch (#15050).

* Tue Jul 25 2000 Jakub Jelinek <jakub@redhat.com>
- fix include-glibc/ to work with new glibc 2.2 resolver headers

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- update to ss000418.
- perform reverse DNS lookup only once for same input.

* Sun Mar  5 2000 Jeff Johnson <jbj@redhat.com>
- include README.ifenslave doco.
- "ping -i N" was broke for N >= 3 (#9929).
- update to ss000121:
-- clockdiff: preserve raw socket errno.
-- ping: change error exit code to 1 (used to be 92,93, ...)
-- ping,ping6: if -w specified, transmit until -c limit is reached.
-- ping,ping6: exit code non-zero if some packets not received within deadline.

* Tue Feb 22 2000 Jeff Johnson <jbj@redhat.com>
- man page corrections (#9690).

* Wed Feb  9 2000 Jeff Johnson <jbj@jbj.org>
- add ifenslave.

* Thu Feb  3 2000 Elliot Lee <sopwith@redhat.com>
- List /usr/sbin/rdisc in %files list.

* Thu Jan 27 2000 Jeff Johnson <jbj@redhat.com>
- add remaining binaries.
- casts to remove compilation warnings.
- terminate if -w deadline is reached exactly (#8724).

* Fri Dec 24 1999 Jeff Johnson <jbj@redhat.com>
- create (only ping for now, traceroute et al soon).
