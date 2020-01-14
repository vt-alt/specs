%define oname openssh
Name: openssh-gostcrypto
Version: 7.9p1
Release: alt3.gost

Summary: OpenSSH free Secure Shell (SSH) implementation
License: BSD-style
Group: Networking/Remote access
Url: http://www.openssh.com/portable.html
# git://git.altlinux.org/gears/o/openssh.git
Source: %name-%version-%release.tar

%define confdir %_sysconfdir/%oname
%define _chrootdir /var/empty
%define docdir %_docdir/%name-%version
%def_with pam_userpass
%def_with libedit
%def_with libaudit
%def_with kerberos5
%def_with selinux
%def_with openssl
%def_with ssl_engine
%def_with ssh1

%{expand: %%global _libexecdir %_libexecdir/openssh}
%define _pamdir /etc/pam.d

Conflicts: openssh
Requires: %oname-clients-gostcrypto = %EVR
Requires: %oname-server-gostcrypto = %EVR

# Automatically added by buildreq on Wed Apr 04 2007
BuildRequires: libssl-devel >= 1.1.0j-alt2
BuildRequires: pam_userpass-devel
BuildRequires: zlib-devel
%{?_with_libedit:BuildRequires: libedit-devel}
%{?_with_libaudit:BuildRequires: libaudit-devel}
%{?_with_kerberos5:BuildRequires: libkrb5-devel}
%{?_with_selinux:BuildRequires: libselinux-devel}

%package -n %oname-common-gostcrypto
Summary: OpenSSH common files
Group: Networking/Remote access
Provides: openssh-common = %EVR
Conflicts: openssh-common
Conflicts: %name < %EVR

%package -n %oname-clients-gostcrypto
Summary: OpenSSH Secure Shell protocol clients
Group: Networking/Remote access
Provides: openssh-clients = %EVR
Conflicts: openssh-clients
Requires: %oname-common-gostcrypto = %EVR
Requires: openssl-gost-engine >= 1.1.0.3.0.255.ge3af41d-alt1

%package -n %oname-keysign-gostcrypto
Summary: OpenSSH helper program for hostbased authentication
Group: Networking/Remote access
Provides: openssh-keysign = %EVR
Conflicts: openssh-keysign
Requires: %oname-clients-gostcrypto = %EVR

%package -n %oname-server-gostcrypto
Summary: OpenSSH Secure Shell protocol daemon
Group: System/Servers
Provides: openssh-server = %EVR
Conflicts: openssh-server
Requires(pre,post): %oname-server-control-gostcrypto = %EVR
Requires: %_chrootdir, syslogd-daemon
Requires: openssl-gost-engine >= 1.1.0.3.0.255.ge3af41d-alt1
# Because of /etc/syslog.d/ feature.
Conflicts: syslogd < 1.4.1-alt11

%package -n %oname-server-control-gostcrypto
Summary: Control rules for the OpenSSH server configuration
License: GPLv2+
Group: System/Servers
Provides: openssh-server-control = %EVR
Conflicts: openssh-server-control
Requires: %oname-common-gostcrypto = %EVR

%package -n %oname-askpass-common-gostcrypto
Summary: OpenSSH common passphrase dialog infrastructure
Group: Networking/Remote access
Provides: openssh-askpass-common = %EVR
Conflicts: openssh-askpass-common
Requires: %oname-common-gostcrypto = %EVR
Provides: %_libexecdir

%description
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine.  It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network.  X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing it
up to date in terms of security and features, as well as removing all
patented algorithms to seperate libraries (OpenSSL).

%description -n %oname-common-gostcrypto
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine.  It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network.  X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing it
up to date in terms of security and features, as well as removing all
patented algorithms to seperate libraries (OpenSSL).

This package includes common files necessary for both the OpenSSH
client and server.

%description -n %oname-clients-gostcrypto
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine.  It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network.  X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing it
up to date in terms of security and features, as well as removing all
patented algorithms to seperate libraries (OpenSSL).

This package includes the clients necessary to make encrypted connections
to SSH servers.

%description -n %oname-keysign-gostcrypto
ssh-keysign is used by ssh(1) to access the local host keys and generate
the digital signature required during hostbased authentication with SSH
protocol version 2.  ssh-keysign is not intended to be invoked by the
user, but from ssh(1).  See ssh(1) and sshd(8) for more information about
hostbased authentication.

%description -n %oname-server-gostcrypto
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine.  It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network.  X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing it
up to date in terms of security and features, as well as removing all
patented algorithms to seperate libraries (OpenSSL).

This package contains the secure shell daemon.  The sshd is the server
part of the secure shell protocol and allows ssh clients to connect to
your host.

%description -n %oname-server-control-gostcrypto
This package contains control rules for OpenSSH server configuration.
See control(8) for details.

%description -n %oname-askpass-common-gostcrypto
Ssh (Secure Shell) a program for logging into a remote machine and for
executing commands in a remote machine.  It is intended to replace
rlogin and rsh, and provide secure encrypted communications between
two untrusted hosts over an insecure network.  X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's rework of the last free version of SSH, bringing it
up to date in terms of security and features, as well as removing all
patented algorithms to seperate libraries (OpenSSL).

This package contains OpenSSH passphrase dialog infrastructure.
These dialogs are intended to be called from the ssh-add program and
not invoked directly.

%prep
%setup -n %name-%version-%release

%build
%autoreconf

mkdir build
cd build
%define _configure_script ../configure

export ac_cv_path_LOGIN_PROGRAM_FALLBACK=/bin/login
export ac_cv_path_NROFF=/usr/bin/nroff
export ac_cv_path_PATH_PASSWD_PROG=/usr/bin/passwd
export ac_cv_path_PROG_LASTLOG=/usr/bin/lastlog
export ac_cv_path_xauth_path=/usr/bin/xauth

%configure \
	--sysconfdir=%confdir \
	--without-rpath \
	--disable-strip \
	--with-mantype=doc \
	--with-pam \
	--with-ipaddr-display \
	--with-privsep-user=sshd \
	--with-privsep-path=%_chrootdir \
	--with-default-path=/bin:/usr/bin:/usr/local/bin \
	--with-superuser-path=/sbin:/usr/sbin:/usr/local/sbin:/bin:/usr/bin:/usr/local/bin \
	%{subst_with kerberos5} \
	%{subst_with libedit} \
	%{subst_with openssl} \
%if_with ssl_engine
	--with-ssl-engine \
%endif
	%{subst_with selinux} \
	%{subst_with ssh1} \
	%{?_with_libaudit:--with-audit=linux} \
	#
%make_build

%install
%makeinstall_std -C build

mkdir -p %buildroot{%_libexecdir,%_sysconfdir{,/X11}/profile.d,%systemd_unitdir}
mkdir -p %buildroot%confdir/authorized_keys{,2}
install -pD -m600 alt/sshd.pamd \
	%buildroot%_pamdir/sshd
install -pD -m755 alt/sshd.init \
	%buildroot%_initdir/sshd
install -pD -m600 alt/sshd.sysconfig \
	%buildroot%_sysconfdir/sysconfig/sshd
install -p -m755 alt/rescp \
	%buildroot%_bindir/
install -p -m755 alt/ssh-agent.sh \
	%buildroot%_sysconfdir/X11/profile.d/
install -pD -m755 alt/sftp.control \
        %buildroot%_sysconfdir/control.d/facilities/sftp
install -pD -m755 alt/sshd-allow-groups.control \
        %buildroot%_sysconfdir/control.d/facilities/sshd-allow-groups
install -pD -m755 alt/sshd-password-auth.control \
        %buildroot%_sysconfdir/control.d/facilities/sshd-password-auth

install -pD -m644 alt/sshd.service \
	%buildroot%systemd_unitdir/sshd.service

sed -i 's,@LIBEXECDIR@,%_libexecdir,g' \
        %buildroot%_sysconfdir/control.d/facilities/sftp

install -p -m755 contrib/ssh-copy-id %buildroot%_bindir/
install -p -m644 contrib/ssh-copy-id.1 %buildroot%_man1dir/

chmod 711 %buildroot%_sbindir/*

install -p -m755 alt/ssh-askpass.{sh,csh} \
	%buildroot%_sysconfdir/profile.d/

mkdir -p %buildroot%docdir
install -pm644 CREDITS LICENCE README* PROTOCOL* alt/[CR]* alt/faq.html \
	%buildroot%docdir/

%pre -n %oname-clients-gostcrypto
/usr/sbin/groupadd -r -f sshagent

%pre -n %oname-server-gostcrypto
/usr/sbin/groupadd -r -f sshd
/usr/sbin/useradd -r -g sshd -d %_chrootdir -s /dev/null -n sshd >/dev/null 2>&1 ||:
%pre_control sftp sshd-allow-groups sshd-password-auth

%post -n %oname-server-gostcrypto
%post_control -s enabled sftp
%post_control -s disabled sshd-allow-groups
%post_control -s default sshd-password-auth
if [ $1 -ge 2 ]; then
	/sbin/service sshd condreload ||:
else
	/sbin/chkconfig --add sshd ||:
fi

%preun -n %oname-server-gostcrypto
if [ $1 = 0 ]; then
	/sbin/chkconfig --del sshd ||:
fi

%files

%files -n %oname-common-gostcrypto
%_bindir/scp
%_bindir/ssh-keygen
%_man1dir/scp.*
%_man1dir/ssh-keygen.*
%docdir/

%files -n %oname-clients-gostcrypto
%attr(751,root,root) %dir %confdir
%config(noreplace) %confdir/ssh_config
%config(noreplace) %_sysconfdir/X11/profile.d/*
%_bindir/rescp
%_bindir/sftp
%_bindir/ssh
%_bindir/ssh-add
%attr(2711,root,sshagent) %_bindir/ssh-agent
%_bindir/ssh-copy-id
%_bindir/ssh-keyscan
%attr(751,root,root) %dir %_libexecdir
%_libexecdir/ssh-pkcs11-helper
%_man1dir/sftp.*
%_man1dir/ssh.*
%_man1dir/ssh-add.*
%_man1dir/ssh-agent.*
%_man1dir/ssh-copy-id.*
%_man1dir/ssh-keyscan.*
%_man5dir/ssh_config.*
%_man8dir/ssh-pkcs11-helper.*

%files -n %oname-keysign-gostcrypto
%attr(751,root,root) %dir %_libexecdir
%_libexecdir/ssh-keysign
%_man8dir/ssh-keysign.*

%files -n %oname-server-gostcrypto
%attr(751,root,root) %dir %confdir
%attr(600,root,root) %config %confdir/moduli
%attr(600,root,root) %config(noreplace) %verify(not size md5 mtime) %confdir/sshd_config
%attr(600,root,root) %config(noreplace) %_pamdir/sshd
%attr(600,root,root) %config(noreplace) %_sysconfdir/sysconfig/sshd
%attr(755,root,root) %config %_initdir/sshd
%attr(751,root,root) %dir %confdir/authorized_keys*
%systemd_unitdir/*
%_sbindir/*
%attr(751,root,root) %dir %_libexecdir
%_libexecdir/sftp-server
%_man5dir/moduli.*
%_man5dir/sshd_config.*
%_man8dir/sshd.*
%_man8dir/sftp-server.*

%files -n %oname-server-control-gostcrypto
%attr(755,root,root) %_controldir/*

%files -n %oname-askpass-common-gostcrypto
%_sysconfdir/profile.d/ssh-askpass.*
%attr(751,root,root) %dir %_libexecdir

%changelog
* Thu Dec 19 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.9p1-alt3.gost
- Moved config dir to /etc/openssh .
- Added Conflicts to default openssh subpackages.

* Mon Nov 25 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.9p1-alt2.gost
- Add gost algorithms:
  + MACs: grasshopper-mac and hmac-streebog-{256,512};
  + Ciphers: grasshopper-{cbc,ctr} and magma-{cbc,ctr}.

* Wed Oct 24 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.9p1-alt1
- Updated to 7.9p1.

* Fri Aug 24 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.2p2-alt3
- Backported upstream fixex for CVE-2018-15473 (username enumeration).

* Thu Oct 20 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.2p2-alt2
- Backported upstream fixes for CVE-2015-8325, CVE-2016-6210,
  CVE-2016-8858.

* Thu Mar 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.2p2-alt1
- Updated to 7.2p2 (security: fixes xauth command injection).

* Thu Mar 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.2p1-alt1
- Updated to 7.2p1.

* Wed Jan 13 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.1p1-alt1
- Updated to 7.1p1.

* Thu Nov 20 2014 Dmitry V. Levin <ldv@altlinux.org> 6.7p1-alt1
- Updated to 6.7p1-29-g51b64e4.

* Fri Apr 25 2014 Dmitry V. Levin <ldv@altlinux.org> 6.6p1-alt3
- ssh-agent: fixed unintended socket removal (closes: #30029).

* Mon Apr 21 2014 Dmitry V. Levin <ldv@altlinux.org> 6.6p1-alt2
- Updated to 6.6.1p1 (fixes curve25519 KEX portability).

* Thu Mar 20 2014 Dmitry V. Levin <ldv@altlinux.org> 6.6p1-alt1
- Updated to 6.6p1.

* Fri Nov 08 2013 Dmitry V. Levin <ldv@altlinux.org> 5.9p1-alt7
- sshd: applied upstream initialization fix (CVE-2013-4548).

* Mon Apr 15 2013 Dmitry V. Levin <ldv@altlinux.org> 5.9p1-alt6
- ssh-keygen: updated fix for #24682 to libcrypto >= 1.0.1 (closes: #28850).

* Fri Apr 12 2013 Dmitry V. Levin <ldv@altlinux.org> 5.9p1-alt5
- Relaxed runtime OpenSSL version check.

* Wed Jan 09 2013 Dmitry V. Levin <ldv@altlinux.org> 5.9p1-alt4
- %name-server-control:
  added sftp-server extra arguments support (closes: #28306).

* Thu Nov 08 2012 Dmitry V. Levin <ldv@altlinux.org> 5.9p1-alt3
- sshd: updated systemd support: merged ssh-keygen.service into
  sshd.service, dropped sshd@.service and sshd.socket.

* Mon Nov 14 2011 Dmitry V. Levin <ldv@altlinux.org> 5.9p1-alt2
- Applied upstream fix for ssh -W with ControlPersistssh (bz#1943).
- Fixed %%triggerpostun exit code on dumb terminals.

* Wed Sep 14 2011 Dmitry V. Levin <ldv@altlinux.org> 5.9p1-alt1
- Updated to 5.9p1 (closes: #19085).
- ssh-keygen: forced use of SHA1 for large keys (closes: #24682).
- sshd: added systemd support (by Alexey Shabalin; closes: #25617).
- sshd: enabled UsePrivilegeSeparation=sandbox by default.
- sshd: deprecated AuthorizedKeysSystemFile*.

* Thu Oct 07 2010 Dmitry V. Levin <ldv@altlinux.org> 5.6p1-alt1
- Updated to 5.6p1.
- Enhanced AuthorizedKeysSystemFile documentation (closes: #21843).
- Renamed %name subpackage to %name-common (closes: #21603),
  reintroduced %name as a virtual subpackage.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 5.3p1-alt5
- Rebuilt with libcrypto.so.10.

* Fri Jul 02 2010 Dmitry V. Levin <ldv@altlinux.org> 5.3p1-alt4
- Rebuilt with libaudit.so.1.

* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 5.3p1-alt3
- Added sshd-allow-groups and sshd-password-auth control(8)
  facilities to control appropriate parts of sshd_config.
- Moved all control facilities to -server-control subpackage.
- sshd_config:
  + added a commented out AllowGroups directive for control(8);
  + reverted previous change related to PasswordAuthentication.

* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 5.3p1-alt2
- Enabled sftp by default.
- /etc/pam.d/sshd: Changed to use common-login.
- sshd_config: Disabled PasswordAuthentication for "wheel" group
  members (imz@; closes: #17286).

* Thu Oct 01 2009 Dmitry V. Levin <ldv@altlinux.org> 5.3p1-alt1
- Updated to 5.3p1.

* Sun Apr 12 2009 Dmitry V. Levin <ldv@altlinux.org> 5.2p1-alt2
- Enabled kerberos support (Evgeny Sinelnikov; closes: #18183).

* Thu Mar 26 2009 Anton Farygin <rider@altlinux.ru> 5.2p1-alt1.1
- Added audit support.

* Tue Feb 24 2009 Dmitry V. Levin <ldv@altlinux.org> 5.2p1-alt1
- Updated to 5.2p1.

* Tue Dec 02 2008 Dmitry V. Levin <ldv@altlinux.org> 5.1p1-alt2
- Added support for setting PermitEmptyPasswords in a Match block.
- openssh-askpass-common: Packaged as noarch.

* Fri Sep 12 2008 Dmitry V. Levin <ldv@altlinux.org> 5.1p1-alt1
- Updated to 5.1p1.

* Fri May 30 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0p1-alt3
- sshd: In key blacklisting, distinguish public keys and host keys.

* Mon May 26 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0p1-alt2
- sshd: Implemented support for RSA/DSA key blacklisting
  based on partial fingerprints.

* Mon Apr 07 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0p1-alt1
- Updated to 5.0p1.

* Fri Sep 07 2007 Dmitry V. Levin <ldv@altlinux.org> 4.7p1-alt1
- Updated to 4.7p1.

* Sun Aug 05 2007 Dmitry V. Levin <ldv@altlinux.org> 4.6p1-alt4
- In ssh-agent and ssh connections multiplexor,
  show command line of requestor process (#12209).

* Tue May 08 2007 Dmitry V. Levin <ldv@altlinux.org> 4.6p1-alt3
- Parametrized sshd process name in startup script.
- Built sftp with libedit support by default.

* Sat Apr 14 2007 Dmitry V. Levin <ldv@altlinux.org> 4.6p1-alt2
- Added summary to sftp control script.

* Thu Apr 05 2007 Dmitry V. Levin <ldv@altlinux.org> 4.6p1-alt1
- Updated to 4.6p1.
- Reviewed and updated patches (see git changelog for details).
- Changed PermitRootLogin parameter to "without-password".
- Updated Ciphers parameter to prefer strong ciphers.
- Changed SyslogFacility parameter to "AUTHPRIV".
- Changed Protocol parameter to "2".
- Enabled Send/Accept of locale environment variables by default.
- Added CHANGES and README.ALT documentation files.

* Fri Dec 29 2006 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt10
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Nov 09 2006 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt9
- Backported upstream fix for a bug in the sshd privilege separation
  monitor that weakened its verification of successful authentication
  (CVE-2006-5794).

* Tue Oct 03 2006 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt8
- Backported upstream fixes for:
  + sshd connection consumption vulnerability
    (CVE-2004-2069: low, remote, active),
  + scp local arbitrary command execution vulnerability
    (CVE-2006-0225: high, local, active),
  + sshd signal handler race condition
    (CVE-2006-5051: none, remote, active),
  + CRC compensation attack detector DoS
    (CVE-2006-4924: low, remote, active),
  + client NULL dereference on protocol error
    (CVE-2006-4925: low, remote, passive).
- Applied RH patch to plug several sftp memleaks.

* Thu Jan 12 2006 ALT QA Team Robot <qa-robot@altlinux.org> 3.6.1p2-alt7.1
- Rebuilt for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Wed Nov 30 2005 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt7
- Applied patch from Owl to sanitize packet types early on.
- Added delayed compression support for protocol 2
  (patch from Owl which is in turn backport from openssh CVS).
- Removed verify checks for sshd_config which is under control(8).
- Fixed sftp control facility and added help (#8536).
- Relocated helper directory (#8565).

* Mon May 10 2004 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt6
- Backported fix for rcp directory traversal bug (CAN-2004-0175).
- Build with openssl-0.9.7d.

* Mon Apr 26 2004 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt5
- Backported UT_LINESIZE fix (#3980).

* Wed Sep 17 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt4
- Included the buffer and channels memory reallocation fixes from
  http://www.openssh.com/txt/buffer.adv (2nd revision).
- Reviewed all uses of *realloc(), resulting in four more fixes
  of this nature (Owl).
- Corrected startup script to honor $EXTRAOPTIONS in check mode too.

* Tue Sep 16 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt3
- Fixed scp return status
  (http://bugzilla.mindrot.org/show_bug.cgi?id=638).
- Fixed memory allocation error in buffer_append_space.

* Mon Aug 25 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt2
- Removed explicit kernel dependence.
- Backported from CVS:
  + copy argv correctly to fix potential restart after SIGHUP
    problem;
  + replace deprecated VerifyReverseMapping option with new
    option, UseDNS (Owl) (CVE-2003-0386).

* Mon Jun 02 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p2-alt1
- Updated to 3.6.1p2.
- When we know we're going to fail authentication for reasons
  external to PAM, pass there a hopefully incorrect password to
  have it behave the same for correct and incorrect passwords (Owl).

* Sat May 24 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p1-alt4
- PAM configuration policy enforcement.
- Added nodelay option to pam auth method.

* Sun Apr 27 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p1-alt3
- Rewritten start/stop script to new rc scheme.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p1-alt2
- Changed %_pamdir/sshd to use tcb authentication explicitly.
- Added back the now more complete patch to always run PAM with
  password authentication, even for non-existent or not allowed
  usernames (Owl).
- Tell pam_tcb to not log failed authentication attempts when a
  blank password is tried (blank_nolog) as this is attempted
  automatically (Owl).

* Thu Apr 10 2003 Dmitry V. Levin <ldv@altlinux.org> 3.6.1p1-alt1
- Updated to 3.6.1p1.
- Updated faq.html to 2002/04/03 and removed openssh-closing.txt.
- Updated Owl patches to 3.6.1p1-owl1.
- Updated ALT patches.
- Merged upstream patches:
  alt-pam_service
- Dropped patches:
  alt-log_MSGBUFSIZ
- Reworked patches:
  alt-socketcred (due to privsep)
- Added control(8) support for sftp subsystem and disabled it
  in default configuration.
- Dropped upgrade support from ssh-server. No need to bother.
- Built with libpam_userpass.so.1.

* Sat Feb 22 2003 Dmitry V. Levin <ldv@altlinux.org> 3.4p1-alt5
- Backported ssh-add from 3.5p1.
- Backported ssh-agent from 3.5p1.
- Moved ssh-keysign to separate subpackage.
- Package x11 and gtk passphrase dialogs separately. Keep common
  passphrase dialog infrastructure in -askpass-common subpackage.

* Wed Jan 29 2003 Dmitry V. Levin <ldv@altlinux.org> 3.4p1-alt4
- %%post: Execute "service sshd condreload" on upgrade (#0001756).
- app-defaults/SshAskpass: Fixed file permissions (#0002068).
- ssh-keygen: Fixed default key length (#0002097).

* Tue Nov 12 2002 Dmitry V. Levin <ldv@altlinux.org> 3.4p1-alt3
- Merged Owl changes:
  * Sun Jul 28 2002 Solar Designer <solar@owl.openwall.com>
  - Install the packet_close() cleanup for the client as well.
  * Sun Jul 07 2002 Solar Designer <solar@owl.openwall.com>
  - Install the packet_close() cleanup for root logins as well (which are
    not privilege separated because that wouldn't make sense and thus were
    handled by a different code path which I initially have missed).
  * Sat Jul 06 2002 Solar Designer <solar@owl.openwall.com>
  - Re-initialize logging after calls into PAM module stacks, make use of
    log_reinit() where the original code needed that kind of functionality.
  * Fri Jul 05 2002 Solar Designer <solar@owl.openwall.com>
  - Re-enable the password changing code (disabled in 3.3p1 and 3.4p1) for
    non-privsep case, disallowing any forwardings (such that the session may
    not be actually used while still not changing the expired password).
  - Limit three of the cleanup functions to apply to just the proper sshd
    processes, make sure session_pty_cleanup() happens before packet_close().
  * Tue Jul 02 2002 Solar Designer <solar@owl.openwall.com>
  - In the PAM conversation, queue any text messages appearing in initial
    login mode for printing later, similarly to what the original code did.
    This is needed to pass password expiration warnings on to the user.
  * Sat Jun 29 2002 Solar Designer <solar@owl.openwall.com>
  - Keep the /dev/log fd open and only close it before executing other
    programs, to enable direct logging from chrooted child processes.
- Build with -lwrap dynamically.

* Tue Jul 02 2002 Dmitry V. Levin <ldv@altlinux.org> 3.4p1-alt2
- Initialize the resolver before chroot (Kevin Steves).
- Added zeroing out the written-to pages on mm_destroy (Owl).

* Thu Jun 27 2002 Dmitry V. Levin <ldv@altlinux.org> 3.4p1-alt1
- 3.4p1 (with ChallengeResponseAuthentication fix).

* Mon Jun 24 2002 Dmitry V. Levin <ldv@altlinux.org> 3.3p1-alt1
- 3.3p1 (with privilege separation), updated our and Owl's patches.
- If MAP_ANON|MAP_SHARED fails (is unsupported on Linux 2.2), fallback
  to using SysV shm, and, if that fails too (SysV shm is a compile-time
  kernel option), to MAP_SHARED with sparse and unlinked swap files. (Owl)
- Set chroot for privsep user to %_chrootdir, added /dev/log there.
- startup script: added new targets: check, condreload.

* Sun Mar 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.1p1-alt1
- 3.1p1, updated our and Owl's patches.
- Disabled restricted_forwarding patch (use "permitopen=" option instead).

* Thu Mar 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.0.2p1-alt4
- Fixed %%triggerpostun script.

* Mon Mar 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.0.2p1-alt3
- Set more strict versioned libssl requires.
- Placed %confdir/moduli to server subpackage.
- Added %_sysconfdir/X11/profile.d/%name-agent.sh to client subpackage
  (for xinitrc >= 2.4.6-alt1).
- Updated buildrequires.

* Thu Mar 07 2002 Dmitry V. Levin <ldv@alt-linux.org> 3.0.2p1-alt2
- Fixed channel code error (marcus).
- Fixed %confdir/authorized_keys* permissions (0750 --> 0751).
- Fixed server subpackage dependencies (openssl --> libssl).
- Fixed startup script: use "%_sbindir/sshd" instead of "sshd".
- Fixed reload with incomplete argv[0] (#0000503).
- Removed pam_lastlog from %_pamdir/sshd (PrintLastLog=yes by default).
- Added "--without" logic to *_askpass build.

* Fri Dec 28 2001 Dmitry V. Levin <ldv@alt-linux.org> 3.0.2p1-alt1
- 3.0.2p1, updated our and Owl's patches.
- x11-ssh-askpass-1.2.4.1
- Added libpam_userpass support.
- Updated faq.
- Dropped make-ssh-known-hosts.

* Sat Sep 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.9p2-alt3
- Moved socket fchowning to socketcred.
- Updated faq.

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.9p2-alt2
- authorized_keys2 IP based access control restriction checking fix.
- x11-ssh-askpass-1.2.4.

* Tue Jun 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.9p2-alt1
- Updated to 2.9p2.
- Merged in some third-party patches (including owl and rh).
- Added %_sysconfdir/profile.d/ssh-askpass.* files.
- %name-clients no longer requires %name-askpass to be installed.

* Thu Jun 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.5.2p2-alt6
- Fixed build with new imake.

* Mon May 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.5.2p2-alt5
- Fixed typo in readconf.c (use id_dsa again, #35).
- Use major part of OPENSSL_VERSION_NUMBER.

* Wed Apr 04 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.5.2p2-alt4
- x11-ssh-askpass-1.2.2.

* Wed Mar 28 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.5.2p2-alt3
- Minor fixes from RH.

* Tue Mar 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.5.2p2-alt2
- Fixed typo made in recent merge.

* Mon Mar 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.5.2p2-alt1
- 2.5.2p2 release.

* Mon Mar 26 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.5.1p2-ipl2mdk
- Added "ssh-agent -u" feature.

* Thu Mar 01 2001 Dmitry V. Levin <ldv@fandra.org> 2.5.1p2-ipl1mdk
- 2.5.1p2 release.

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 2.5.1p1-ipl2mdk
- Added two new options for sshd.

* Tue Feb 20 2001 Dmitry V. Levin <ldv@fandra.org> 2.5.1p1-ipl6mdk
- 2.5.1p1 release.
- Merged all patches into single unified patch.

* Sun Feb 11 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.0p1-ipl6mdk
- Updated socket chowning patch.
- Fixed auth-options reset time.
- Fixed setting PAM rhost.
- Workaround for xauth bug.

* Fri Jan 26 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.0p1-ipl5mdk
- Rewritten ssh-copy-id script.
- Updated ssh-copy-id.1 manpage.
- Patched ssh-keygen to properly use dsa mode when necessary.

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.0p1-ipl4mdk
- Updated x11-ssh-askpass version 1.1.1.
- Applied TransmitInterlude patch.

* Fri Jan 12 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.0p1-ipl3mdk
- Enabled PasswordAuthentication by default for client and server.

* Sat Jan 06 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.0p1-ipl2mdk
- Rebuilt with db2.

* Tue Nov 07 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.0p1-ipl1mdk
- Updated:
  + openssh-2.3.0p1;
  + x11-ssh-askpass-1.1.0;
  + our patches.
- Added:
  + http://www.openssh.com/faq.html

* Thu Oct 12 2000 Dmitry V. Levin <ldv@fandra.org> 2.2.0p1-ipl3mdk
- Updated:
  + x11-ssh-askpass-1.0.2;
  + pam configuration.
- Fixed (by Nalin Dahyabhai <nalin@redhat.com>):
  + ssh-add to try to add both identity and id_dsa,
    and to error only when neither exists;
  + Set the default path to be the same as the one supplied
    by /bin/login, but also add /usr/X11R6/bin;
  + try to handle obsoletion of ssh-server more cleanly.
- Automatically added BuildRequires.

* Wed Sep 13 2000 Dmitry V. Levin <ldv@fandra.org> 2.2.0p1-ipl2mdk
- Use update-alternatives for askpass-* packages.

* Mon Sep 04 2000 Dmitry V. Levin <ldv@fandra.org> 2.2.0p1-ipl1mdk
- Updated:
  + openssh-2.2.0p1;
  + x11-ssh-askpass-1.0.1.
- Changed:
  + rescp script;
  + moved keygen calls to sshd.init (now generate keys at runtime);
  + made building of X11-askpass and gnome-askpass optional;
  + removed autorestart of the server after upgrade.

* Thu Aug 17 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.1p4-ipl2mdk
- Changed StrictHostKeyChecking parameter in ssh_config from "yes" to "ask".
- Added usage to ssh-copy-id script.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.1p4-ipl1
- 2.1.1p4

* Wed Jul 12 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.1p3-ipl1
- 2.1.1p3

* Wed Jul 05 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.1p2-ipl1
- 2.1.1p2

* Fri Jun 30 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.1p1-ipl2
- configure/bash bug workaround.

* Tue Jun 27 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.1p1-ipl1
- 2.1.1p1
- Use FHS-compatible macros.

* Wed May 31 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.0p3-ipl1
- 2.1.0p3

* Sun May 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.0p2-ipl1
- 2.1.0p2

* Mon May 15 2000 Dmitry V. Levin <ldv@fandra.org> 2.1.0-ipl1
- Fixes:
  + xauth bug;
  + shutdown typo;
- Features:
  + rescp script from Solar;
  + TCP/IP sockets belong to user;
  + configurable software version as it will be reported to peer;
  + restricted forwarding;
  + permitted keys in system directory.
- RE and Fandra adaptions.

* Wed Mar 15 2000 Damien Miller <djm@ibs.com.au>
- Updated for new location
- Updated for new gnome-ssh-askpass build

* Sun Dec 26 1999 Damien Miller <djm@mindrot.org>
- Added Jim Knoble's <jmknoble@pobox.com> askpass

* Mon Nov 15 1999 Damien Miller <djm@mindrot.org>
- Split subpackages further based on patch from jim knoble <jmknoble@pobox.com>

* Sat Nov 13 1999 Damien Miller <djm@mindrot.org>
- Added 'Obsoletes' directives

* Tue Nov 09 1999 Damien Miller <djm@ibs.com.au>
- Use make install
- Subpackages

* Mon Nov 08 1999 Damien Miller <djm@ibs.com.au>
- Added links for slogin
- Fixed perms on manpages

* Sat Oct 30 1999 Damien Miller <djm@ibs.com.au>
- Renamed init script

* Fri Oct 29 1999 Damien Miller <djm@ibs.com.au>
- Back to old binary names

* Thu Oct 28 1999 Damien Miller <djm@ibs.com.au>
- Use autoconf
- New binary names

* Wed Oct 27 1999 Damien Miller <djm@ibs.com.au>
- Initial RPMification, based on Jan "Yenya" Kasprzak's <kas@fi.muni.cz> spec.
