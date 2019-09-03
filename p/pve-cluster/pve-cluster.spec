Name: pve-cluster
Summary: Cluster Infrastructure for PVE
Version: 6.0.6
Release: alt1
License: GPLv3
Group: System/Servers
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64 aarch64
Requires: bridge-utils chrony ntpdate corosync2 fuse rrd-cached ksmtuned openvswitch
Requires: sqlite3 vixie-cron faketime tzdata openssh-server openssh-clients

Source0: %name.tar.xz
Source1: pve-access-control.tar.xz
Source2: pve-apiclient.tar.xz

Patch0: %name.patch
Patch1: pve-access-control.patch
Patch2: pve-cluster-install_vzdump_cron_config.patch

Source3: pve-firsttime

BuildRequires: pve-common pve-doc-generator libcheck-devel librrd-devel glib2-devel libfuse-devel libcorosync2-devel libsqlite3-devel xmlto
BuildRequires: perl(ExtUtils/Embed.pm) perl(Term/ReadLine.pm) perl(Digest/HMAC_SHA1.pm) perl(XML/Parser.pm) perl(RRDs.pm)
BuildRequires: perl(Crypt/OpenSSL/Random.pm) perl(Crypt/OpenSSL/RSA.pm) perl(Net/SSLeay.pm)
BuildRequires: perl(MIME/Base32.pm) perl(Net/LDAP.pm) perl(Authen/PAM.pm) perl(UUID.pm)

%description
This package contains the Cluster Infrastructure for the PVE,
namely a distributed filesystem to store configuration data
on all nodes.

%package -n pve-access-control
Summary: PVE access control library
Version: 6.0.2
Group: Development/Perl

%description -n pve-access-control
This package contains the role based user management and access
control function used by PVE.

%prep
%setup -q -n %name -a1 -a2
%patch0 -p1
%patch1 -p0
%patch2 -p1

grep '/var/run' * -rl | while read f; do
    sed -i 's|/var/run|/run|' $f
done

%install
install -pD -m644 debian/%name.service %buildroot%systemd_unitdir/%name.service
install -pD -m644 debian/sysctl.d/pve.conf %buildroot%_sysconfdir/sysctl.d/pve-cluster.conf
cd data
%make -C PVE/Cluster DESTDIR=%buildroot install
%make PERL_DOC_INC_DIRS=" .. . ../../pve-access-control ../../pve-apiclient" DESTDIR=%buildroot install
cd ../pve-access-control
%make DESTDIR=%buildroot install
cd ../pve-apiclient
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/doc/%name
install -m644 %SOURCE3 %buildroot%_datadir/doc/%name/

mkdir -p %buildroot%_sysconfdir/cron.d
touch %buildroot%_sysconfdir/cron.d/vzdump

mkdir -p %buildroot%_localstatedir/%name

mkdir -p %buildroot%_sysconfdir/network
cat << __EOF__ > %buildroot%_sysconfdir/network/interfaces
auto lo
iface lo inet loopback
__EOF__

mkdir -p %buildroot%_sysconfdir/sysconfig
cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/%name
DAEMON_OPTS=""
__EOF__

cat << __EOF__ > %buildroot%_datadir/doc/%name/rrdcached.sysconfig
RRDCACHED_USER="root"
OPTS="-j /var/lib/rrdcached/journal/ -F -b /var/lib/rrdcached/db/ -B"
SOCKFILE="/run/rrdcached.sock"
SOCKPERMS=0660
__EOF__

%post
%post_service %name

%preun
%preun_service %name
if [ $1 -eq 0 ] ; then
        /sbin/systemctl disable %name.service >/dev/null 2>&1 || :
fi

%pre
%_sbindir/groupadd -r -f www-data 2>/dev/null ||:
%_sbindir/useradd -g www-data -c 'www-data' -d /var/www -s '/sbin/nologin' -G www-data -r www-data 2>/dev/null || :

%triggerun -- %name <= 4.0.48-alt7
if [ -L %_sysconfdir/cron.d/vzdump ]; then
	rm -f %_sysconfdir/cron.d/vzdump
fi

%files
%systemd_unitdir/%name.service
%_sysconfdir/bash_completion.d/pvecm
%dir %_sysconfdir/network
%ghost %_sysconfdir/network/interfaces
%ghost %_sysconfdir/cron.d/vzdump
%_sysconfdir/sysctl.d/pve-cluster.conf
%_bindir/create_pmxcfs_db
%_bindir/pmxcfs
%_bindir/pvecm
%dir %perl_vendor_autolib/PVE
%perl_vendor_autolib/PVE/IPCC
%dir %perl_vendor_privlib/PVE
%perl_vendor_privlib/PVE/Cluster.pm
%perl_vendor_privlib/PVE/Corosync.pm
%perl_vendor_privlib/PVE/IPCC.pm
%dir %perl_vendor_privlib/PVE/CLI
%perl_vendor_privlib/PVE/CLI/pvecm.pm
%dir %perl_vendor_privlib/PVE/APIClient
%perl_vendor_privlib/PVE/APIClient/Exception.pm
%perl_vendor_privlib/PVE/APIClient/LWP.pm
%dir %perl_vendor_privlib/PVE/Cluster
%perl_vendor_privlib/PVE/Cluster/IPCConst.pm
%dir %_localstatedir/%name
%_datadir/zsh/vendor-completions/_pvecm
%_man1dir/pvecm.1*
%_man5dir/datacenter.cfg.5*
%_man8dir/pmxcfs.8*
%_datadir/doc/%name

%files -n pve-access-control
%_sysconfdir/bash_completion.d/pveum
%_bindir/oathkeygen
%_sbindir/pveum
%dir %perl_vendor_privlib/PVE
%perl_vendor_privlib/PVE/RPCEnvironment.pm
%perl_vendor_privlib/PVE/AccessControl.pm
%dir %perl_vendor_privlib/PVE/CLI
%perl_vendor_privlib/PVE/CLI/pveum.pm
%dir %perl_vendor_privlib/PVE/API2
%perl_vendor_privlib/PVE/API2/*.pm
%dir %perl_vendor_privlib/PVE/Auth
%perl_vendor_privlib/PVE/Auth/*.pm
%_datadir/zsh/vendor-completions/_pveum
%_man1dir/pveum.1*

%changelog
* Tue Jul 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.6-alt1
- pve-cluster 6.0-6
- pve-access-control 6.0-2
- pve-apiclient 3.0-2

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.37-alt1
- pve-cluster 5.0-37
- pve-access-control 5.1-10
- pve-apiclient 2.0-5

* Thu Feb 21 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.33-alt4
- use /run instead of /var/run

* Thu Jan 31 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.33-alt3
- rebuild with perl 5.28.1

* Wed Jan 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.33-alt2
- pve-cluster 5.0-33

* Wed Dec 12 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.31-alt1
- pve-cluster 5.0-31
- pve-access-control 5.1-3

* Mon Nov 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.30-alt1
- pve-cluster 5.0-30
- pve-access-control 5.1-1
- pve-apiclient 2.0-4

* Fri Sep 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.27-alt2
- removed ubt

* Wed Jul 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.27-alt1.S1
- pve-cluster 5.0-27
- pve-access-control 5.0-8

* Wed Jan 10 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.19-alt3.S1
- fixed corosync.conf parce

* Thu Dec 14 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.19-alt1.M80P.3
- backport to p8 branch

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.19-alt3
- 5.0-19

* Tue Nov 28 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.15-alt1.M80P.1
- backport to p8 branch

* Wed Nov 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.15-alt2
- rebuild with rrd 1.7.0

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.15-alt1
- 5.0-15

* Tue Oct 10 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.14-alt1
- pve-cluster 5.0-14
- pve-access-control 5.0-7

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt0.M80C.1
- backport to c8 branch

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt1.M80P.1
- backport to p8 branch

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt2
- replace requires openntpd to ntp-server

* Thu Jul 20 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt0.M80P.1
- backport to p8 branch

* Thu Jul 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.12-alt1
- 5.0-12
- pve-access-control 5.0-5

* Thu Apr 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.49-alt8.M80P.1
- backport to p8 branch

* Fri Apr 07 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.49-alt9
- 4.0-49

* Tue Feb 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.48-alt8
- rebuild with perl 5.24.1

* Thu Dec 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.48-alt7
- don't make vzdump symlink in cron.d

* Mon Dec 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.48-alt6
- 4.0-48

* Mon Nov 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.47-alt5
- 4.0-47+git.ab224148

* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.47-alt4
- 4.0-47

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.46-alt3
- 4.0-46

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.45-alt2
- 4.0-45

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.44-alt1
- 4.0-44
- pve-access-control 4.0-19

* Thu Jul 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.43-alt2
- pve-access-control 4.0-18

* Fri Jul 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.43-alt1
- 4.0-43
- pve-access-control 4.0-17

* Thu Jun 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.42-alt6
- fixed upgrading from a previous version

* Wed Jun 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.42-alt5
- 4.0-42

* Thu Jun 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt4
- added requires openntpd, bridge-utils

* Tue Jun 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt3
- added requires faketime

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt2
- pve-access-control 4.0-16

* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt1
- 4.0-40

* Fri May 20 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.39-alt1
- 4.0-39

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.31-alt1
- 4.0-31

* Fri Dec 11 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.29-alt1
- 4.0-29

* Thu Dec 03 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.28-alt1
- initial release

