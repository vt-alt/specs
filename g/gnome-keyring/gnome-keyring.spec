%def_disable snapshot

%define ver_major 3.31
%def_disable static
%def_disable gtk_doc
%def_disable debug
%def_disable valgrind
%def_enable pam
%def_enable selinux
%def_enable ssh
%def_disable check

Name: gnome-keyring
Version: %ver_major.91
Release: alt2

Summary: %name is a password keeper for GNOME
License: LGPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: gnome-keyring-3.14.0-alt-lfs.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=794848
# https://bug794848.bugzilla-attachments.gnome.org/attachment.cgi?id=370357
Patch1: gnome-keyring-3.28.2-bgo-ssh-agent_timeout.patch

%define glib_ver 2.44.0
%define dbus_ver 1.0
%define gcrypt_ver 1.2.2
%define tasn1_ver 0.3.4
%define p11kit_ver 0.23.9
%define gcr_ver 3.28.0

Requires(post): libcap-utils
Requires: p11-kit >= %p11kit_ver

# From configure.ac
BuildPreReq: gnome-common libgio-devel >= %glib_ver
BuildPreReq: intltool >= 0.35.0 gtk-doc xsltproc
BuildPreReq: libdbus-devel >= %dbus_ver
BuildPreReq: libgcrypt-devel >= %gcrypt_ver
BuildPreReq: libtasn1-devel >= %tasn1_ver  libp11-kit-devel >= %p11kit_ver
BuildPreReq: gcr-libs-devel >= %gcr_ver
BuildRequires: libtasn1-utils
BuildRequires: libcap-ng-devel
%{?_enable_pam:BuildRequires: libpam-devel}
%{?_enable_valgrind:BuildRequires: valgrind}
%{?_enable_selinux:BuildRequires: libselinux-devel}
%{?_enable_ssh:BuildRequires: %_bindir/ssh-agent %_bindir/ssh-add}
%{?_enable_check:BuildRequires: /proc xvfb-run dbus-tools-gui}

%description
%name is a program that keep password and other secrets for
users. It is run as a damon in the session, similar to ssh-agent, and
other applications can locate it by an environment variable.

%package -n pam_%name
Summary: A pam module for unlocking keyrings at login time
Group: System/Base
Requires: %name = %version-%release

%description -n pam_%name
The pam_gnome-keyring package contains a pam module that can
automatically unlock the "login" keyring when the user logs in
and start the keyring daemon.

%package ssh
Summary: SSH Key Agent for GNOME Keyring
Group: Networking/Remote access
Requires: %name = %version-%release
# since 3.27.x gnome-keyring wraps the ssh-agent as a subprocess
Requires: gcr >= %gcr_ver openssh-clients

%description ssh
GNOME Keyring ssh agent is a wrapper for stock ssh-agent from OpenSSH.

%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %_prefix/libexec/%name

%prep
%setup
%patch -p1 -b .lfs
%patch1 -p1 -b .ssh-agent

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable static} \
	%{subst_enable debug} \
	%{subst_enable valgrind} \
	%{subst_enable selinux} \
	%{?_disable_ssh:--disable-ssh-agent} \
	--enable-doc \
	--with-pam-dir=/%_lib/security

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%check
%make check

%post
setcap -q cap_ipc_lock=ep %_bindir/gnome-keyring-daemon 2>/dev/null ||:

%files -f %name.lang
%_bindir/gnome-keyring
%_bindir/gnome-keyring-3
%_bindir/gnome-keyring-daemon
%_datadir/dbus-1/services/org.gnome.keyring.service
%_datadir/dbus-1/services/org.freedesktop.secrets.service
%_sysconfdir/xdg/autostart/*.desktop
%{?_enable_ssh:%exclude %_sysconfdir/xdg/autostart/gnome-keyring-ssh.desktop}
%_datadir/glib-2.0/schemas/org.gnome.crypto.cache.gschema.xml
%_datadir/GConf/gsettings/org.gnome.crypto.cache.convert
%_datadir/p11-kit/modules/gnome-keyring.module
%_libdir/gnome-keyring/
%{?_enable_ssh:%exclude %_libdir/gnome-keyring/*/gkm-ssh-store-standalone.so}
%_libdir/pkcs11
%_man1dir/*
%doc README AUTHORS NEWS

%exclude %_libdir/pkcs11/*.la
%exclude %_libdir/gnome-keyring/*/*.la
%exclude /%_lib/security/*.la

%if_enabled ssh
%files ssh
%_libdir/gnome-keyring/*/gkm-ssh-store-standalone.so
%_sysconfdir/xdg/autostart/gnome-keyring-ssh.desktop
%endif


%if_enabled pam
%files -n pam_%name
/%_lib/security/pam_gnome_keyring.so
%exclude /%_lib/security/pam_gnome_keyring.la
%endif


%changelog
* Sat Jun 22 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.91-alt2
- moved ssh part to separate subpackage
- fixed busy-loop waiting for the ssh-agent.
  See:
  https://bugzilla.gnome.org/show_bug.cgi?id=794848
  https://gitlab.gnome.org/GNOME/gnome-keyring/issues/25

* Sat Mar 02 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.91-alt1
- 3.31.91

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Sun Mar 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0.2-alt1
- 3.28.0.2

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0.1-alt1
- 3.28.0.1
- enabled ssh-agent again (since 3.27.x gnome-keyring wraps the ssh-agent as a subprocess)

* Tue Jul 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1.1
- reverted ssh support for me

* Tue Jul 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Wed Dec 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- updated to 3.20.0-16-gbf8aa97
- disabled ssh-agent (ALT #32860)

* Fri Mar 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Oct 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Tue Oct 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Sep 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sat Sep 05 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.91-alt1
- 3.17.91

* Wed Apr 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Mar 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.92-alt1
- 3.15.92

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- call setcap cap_ipc_lock=ep %%_bindir/gnome-keyring-daemon in %%post

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Thu Oct 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sun May 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Mar 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt2
- fix %%files section for libp11-kit >= 0.16.3
- enabled LFS support

* Fri Mar 01 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri May 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sat May 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Tue Oct 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Mon Dec 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Sun Oct 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- updated buildreqs

* Mon Jun 29 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sun Apr 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Sat Apr 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- fix for gnomebug #575247 from svn

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- added libtasn1-utils and valgrind to buildreqs if debug enabled

* Mon Mar 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Sun Feb 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.90-alt1
- 2.25.90

* Wed Jan 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- drop upstreamed patches

* Thu Dec 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.25.2-alt1
- 2.25.2
- updated symver.map

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- removed obsolete post{,un}_ldconfig
- use pkgconfig for tasn1-1.7 without libtasn1.m4

* Mon Oct 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.1-alt1
- 2.24.1
- don't rebuild development documentation

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0
- add versioning for old versions
- add devel-doc package(noarch)

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- 2.22.3

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1
- changed libexec dir to %_prefix/libexec/%name

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Wed Mar 05 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- 2.21.92
- build --with-root-certs=/usr/share/ca-certificates
- add gconf_install/gconf_uninstall in %%post and %%preun
- updated BuildPreReq

* Mon Jan 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.3-alt1
- 2.20.3

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- 2.20.2

* Tue Oct 16 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- 2.20.1
- remove backported patches:
  + gnome-keyring-2.20-add_new_keyrings.patch (fixed upstream)
  + gnome-keyring-2.20-no_match.patch (fixed upstream)
  + gnome-keyring-2.20-selinux-pam.patch (not actual for ALTLinux)
  + gnome-keyring-2.20-link-against-pam.patch (fixed upstream)
- fixed section install (upstream removed install-pam)
- disabled gnome-keyring-2.20-no-unset-default.patch (need this patch?)

* Sat Oct 13 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.0-alt1
- new version 2.20.0
- add packager
- add package pam
- backport patches from svn

* Mon Apr 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Thu Mar 15 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8-alt1
- new version 0.8 (with rpmrb script)

* Thu Mar 15 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8.0-alt1
- new version 0.8 (with rpmrb script)

* Sun Feb 25 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.92-alt1
- new version 0.7.92 (with rpmrb script)

* Wed Feb 14 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.91-alt1
- new version 0.7.91 (with rpmrb script)

* Fri Jan 05 2007 Alexey Rusakov <ktirf@altlinux.org> 0.7.3-alt1
- new version 0.7.3 (with rpmrb script)

* Mon Sep 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.6.0-alt1
- new version (0.6.0)

* Sat Aug 05 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)

* Sat Mar 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.4.7-alt1
- new version 0.4.7 (with rpmrb script)

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.4.6-alt1
- new version

* Thu Sep 22 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.4.5-alt1
- 0.4.5

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.4.4-alt1
- 0.4.4
- Removed more excess buildreqs.

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.4.3-alt1
- 0.4.3
- Removed excess buildreqs.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.4.1-alt1
- 0.4.1.

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Apr 19 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Mon Mar 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.90-alt1
- 0.1.90

* Wed Feb 11 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Sat Jan 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Thu Jan 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt1
- First build for Sisyphus.

