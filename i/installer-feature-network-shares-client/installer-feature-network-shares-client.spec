Name: installer-feature-network-shares-client
Version: 0.9.1
Release: alt1

%define hookdir %_datadir/install2/postinstall.d

%add_findreq_skiplist %hookdir/*

Summary: Installer stage3 NFS/SMB/FTP shares hooks (client side)
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%package stage3
Summary: %summary
Group: System/Configuration/Other
Requires: coreutils libshell sed pam_mount

%description stage3
This package contains installer stage2 hooks for SMB and FTP services (client side).

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot/%hookdir
install -pm755 *.sh %buildroot/%hookdir/

%files stage3
%hookdir/*

%changelog
* Tue Jul 02 2019 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- 70-nscd.sh: Don't fail if nscd.conf is absent.

* Thu Oct 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.9-alt4
- Require pam_mount for its own operation

* Fri Oct 18 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt3
- usage of unexistent umount.cifs removed 

* Fri Nov 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt2
- add 'auth..pam_mount' also to krb5_ccreds

* Thu Nov 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt1
- nscd configuration for pam_ccreds added

* Thu Nov 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt3
- unneded controls removing fixed

* Thu Nov 22 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt2
- unneded controls removed

* Wed Nov 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- use root mount and cruid parameter to work with new cifs-utils

* Fri Mar 25 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt3
- path to u?mount.cifs fixed

* Fri Mar 18 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt2
- always hack system-auth-krb5, not default

* Thu Sep 30 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- no secure NFS from the box

* Tue Aug 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- set krb5 ccache to predicadable value
- really fixed update_pam()

* Mon Aug 10 2009 Mikhail Efremov <sem@altlinux.org> 0.5-alt1
- fixed update_pam().
- use krb5 by default for cifs.

* Wed Jun 24 2009 Andriy Stepanov <stanv@altlinux.ru> 0.4-alt1
- don't harmful symbolic link (Closes: #20548)

* Wed May 06 2009 Andriy Stepanov <stanv@altlinux.ru> 0.3-alt1
- use uid="5000-10000" instead sgrp="users"

* Mon Apr 27 2009 Andriy Stepanov <stanv@altlinux.ru> 0.2-alt1
- Add $dest_dir & exec_chroot

* Wed Apr 22 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt1
- Initial build.

