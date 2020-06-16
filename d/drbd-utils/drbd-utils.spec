%def_without xen
%define githash b24b0f7e42d500d3538d7eeffa017ec78d08f918
%define gitdiff c6e62702d5e4fb2cf6b3fa27e67cb0d4b399a30b
%define _localstatedir %_var

Name: drbd-utils
Version: 9.13.1
Release: alt1

Summary: DRBD user-land tools and scripts
License: GPLv2+
Group: System/Kernel and hardware

Url: http://www.drbd.org/
Source0: %name-%version.tar
Source1: %name-headers-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: docbook-style-xsl flex xsltproc
BuildRequires: gcc-c++ po4a udev libsystemd-devel

Conflicts: drbd-tools drbd83-tools

%description
DRBD refers to block devices designed as a building block to form high
availability (HA) clusters. This is done by mirroring a whole block device
via an assigned network. DRBD can be understood as network based raid-1.

This packages includes the DRBD administration tools.

%package xen
Summary: Xen block device management script for DRBD
Group: System/Kernel and hardware
Requires: %name = %version-%release
Requires: xen
BuildArch: noarch

%description xen
This package contains a Xen block device helper script for DRBD, capable of
promoting and demoting DRBD resources as necessary.

%package pacemaker
Summary: Pacemaker resource agent for DRBD
Group: System/Kernel and hardware
Requires: %name = %version-%release
Requires: pacemaker
License: GPLv2
BuildArch: noarch

%description pacemaker
This package contains the master/slave DRBD resource agent for the
Pacemaker High Availability cluster manager.

%package rgmanager
Summary: Red Hat Cluster Suite agent for DRBD
Group: System/Kernel and hardware
Requires: %name = %version-%release
BuildArch: noarch

%description rgmanager
This package contains the DRBD resource agent for the Red Hat Cluster Suite
resource manager.

%package bash-completion
Summary: Programmable bash completion support for drbdadm
Group: System/Kernel and hardware
Requires: %name = %version-%release
BuildArch: noarch

%description bash-completion
This package contains programmable bash completion support for the drbdadm
management utility.

%prep
%setup -a1
tar -xf %SOURCE1 -C drbd-headers
%patch0 -p1
(echo -e "#define GITHASH \"%githash\""; \
 echo -e "#define GITDIFF \"%gitdiff\"") > user/shared/drbd_buildtag.h

%build
%autoreconf
%configure \
    --with-udev \
    %{subst_with xen} \
    --with-pacemaker \
    --with-rgmanager \
    --with-distro=generic
sed -i "s|WITH_DRBDMON[[:space:]]*=[[:space:]]*no|WITH_DRBDMON = yes|" Makefile user/drbdmon/Makefile
sed -i "s|--pedantic-errors|-pedantic-errors|" user/drbdmon/Makefile
%make_build

%install
%makeinstall_std

rm -rf %buildroot%_mandir/ja
rm -f  %buildroot/etc/init.d/drbd	# NB: _not_ %%_initdir here
install -pDm644 drbd.service %buildroot%_unitdir/drbd.service
install -pDm644 scripts/drbd %buildroot%_initdir/drbd

%post
%post_service drbd

%preun
%preun_service drbd

%files
%doc scripts/drbd.conf.example COPYING ChangeLog README.md
%config(noreplace) %_sysconfdir/drbd.conf
%dir %_sysconfdir/drbd.d
%config(noreplace) %_sysconfdir/drbd.d/global_common.conf
%_sysconfdir/ha.d/resource.d/*
%_initdir/drbd
%_unitdir/drbd.service
%_sbindir/drbdsetup
%_sbindir/drbdadm
%_sbindir/drbdmeta
%_sbindir/drbdmon
%dir /lib/drbd
/lib/drbd/drbdadm-*
/lib/drbd/drbdsetup-*
/lib/udev/rules.d/65-drbd.rules
%exclude /usr/lib/drbd/crm-*fence-peer.sh
%exclude /usr/lib/drbd/stonith_admin-fence-peer.sh
%dir /usr/lib/drbd
/usr/lib/drbd/*.sh
/usr/lib/drbd/rhcs_fence
%dir %_var/lib/drbd
%_man8dir/drbd*
%_man7dir/*
%_man5dir/drbd*

%if_with xen
%files xen
%_sysconfdir/xen/scripts/block-drbd
%endif

%files pacemaker
%dir /usr/lib/ocf/resource.d/linbit
/usr/lib/ocf/resource.d/linbit/drbd
/usr/lib/ocf/resource.d/linbit/drbd.shellfuncs.sh
/usr/lib/drbd/crm-*fence-peer.sh
/usr/lib/drbd/stonith_admin-fence-peer.sh

%files rgmanager
%_datadir/cluster/drbd.sh
%_datadir/cluster/drbd.metadata

%files bash-completion
%_sysconfdir/bash_completion.d/drbdadm*

%changelog
* Thu May 14 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.13.1-alt1
- 9.13.1

* Mon Apr 20 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.12.2-alt1
- 9.12.2

* Tue Mar 24 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.12.1-alt1
- 9.12.1

* Sat Mar 07 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.12.0-alt1.1
- Avoid undocumented option form (for lcc on e2k actually) (mike@)
- Minor spec cleanup (mike@)

* Wed Feb 19 2020 Andrew A. Vasilyev <andy@altlinux.org> 9.12.0-alt1
- 9.12.0

* Tue Apr 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 8.9.6-alt1
- 8.9.6

* Fri May 27 2016 Mikhail Efremov <sem@altlinux.org> 8.9.0-alt3
- Disable xen support.

* Tue Jan 26 2016 Lenar Shakirov <snejok@altlinux.ru> 8.9.0-alt2
- Fixed build (man page packaging)

* Mon Sep 01 2014 Lenar Shakirov <snejok@altlinux.ru> 8.9.0-alt1
- First build for ALT as separate package "%name" (based on Fedora 8.9.0-8.fc21.src)

