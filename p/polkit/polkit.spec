# system bus required
%def_disable check

Name: polkit
Version: 0.116
Release: alt2.M90P.1

Summary: PolicyKit Authorization Framework
License: LGPLv2+
Group: System/Libraries
URL: http://www.freedesktop.org/wiki/Software/PolicyKit
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: lib%name = %version-%release
Requires(pre): dbus

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: %name-0.109-alt-helper_path.patch

BuildRequires: gcc-c++ gobject-introspection-devel gtk-doc intltool libexpat-devel libpam-devel
BuildRequires: libmozjs60-devel libsystemd-devel
%{?_enable_check:BuildRequires: /proc dbus-tools-gui}

%description
PolicyKit is a toolkit for defining and handling authorizations.
It is used for allowing unprivileged processes to speak to privileged
processes.

%package -n lib%name
Summary: PolicyKit libraries
Group: System/Libraries
Provides: lib%{name}1 = %version-%release
Obsoletes: lib%{name}1 < %version

%description -n lib%name
Libraries for interacting with PolicyKit

%package -n lib%name-devel
Summary: Development libraries and headers for PolicyKit
Group: Development/C
Requires: lib%name = %version-%release
Provides: lib%{name}1-devel = %version-%release
Obsoletes: lib%{name}1-devel < %version

%description -n lib%name-devel
Headers, libraries and API docs for PolicyKit

%package -n lib%name-gir
Summary: GObject introspection data for the Polkit-1.0 library
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: lib%{name}1-gir = %version-%release
Obsoletes: lib%{name}1-gir < %version

%description -n lib%name-gir
GObject introspection data for the Polkit-1.0 library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Polkit-1.0 library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release lib%name-devel = %version-%release
Provides: lib%{name}1-gir-devel = %version-%release
Obsoletes: lib%{name}1-gir-devel < %version

%description -n lib%name-gir-devel
GObject introspection devel data for the Polkit-1.0 library

%prep
%setup
%patch -p1
%patch1 -p1

touch ChangeLog

%build
%ifarch %e2k
%add_optflags -std=gnu++11
%endif
%autoreconf
%configure \
	--libexecdir=%_prefix/libexec \
	--localstatedir=%_var \
	--enable-gtk-doc \
	--disable-static \
	--enable-libsystemd-login=yes
%make

%install
%makeinstall_std

%find_lang %name-1

%check
%make check

%pre
%_sbindir/groupadd -r -f polkitd 2>/dev/null ||:
%_sbindir/useradd -r -n -g polkitd -d / \
	-s /dev/null -c "User for polkitd" polkitd 2>/dev/null ||:

%files -f %name-1.lang
%dir %_sysconfdir/%name-1
%attr(0700,polkitd,root) %dir %_sysconfdir/%name-1/rules.d
%_sysconfdir/%name-1/rules.d/50-default.rules
%_datadir/dbus-1/system.d/org.freedesktop.PolicyKit1.conf
%_sysconfdir/pam.d/polkit-1
%_bindir/pk[act]*
%attr(4511,root,root) %_bindir/pkexec
%dir %_prefix/libexec/%name-1
%_prefix/libexec/%name-1/polkitd
%attr(4511,root,root) %_prefix/libexec/polkit-1/polkit-agent-helper-1
%dir %_datadir/%name-1
%dir %_datadir/%name-1/actions
%attr(0700,polkitd,root) %dir %_datadir/%name-1/rules.d
%_datadir/%name-1/actions/org.freedesktop.policykit.policy
%_datadir/dbus-1/system-services/org.freedesktop.PolicyKit1.service
%systemd_unitdir/polkit.service
%_man1dir/*.1*
%_man8dir/*.8*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gettext/its/%name.its
%_datadir/gettext/its/%name.loc
%_datadir/gtk-doc/html/%name-1/

%files -n lib%name-gir-devel
%_girdir/*.gir

# examples
%exclude %_bindir/pk-example-frobnicate
%exclude %_datadir/polkit-1/actions/org.freedesktop.policykit.examples.pkexec.policy

%changelog
* Thu Dec 17 2020 Ivan Savin <svn17@altlinux.org> 0.116-alt2.M90P.1
- Added the ability to add user_of_subject to user_identities list
  if user_of_subject is a member of the group with administrator
  rights but it is not in /etc/groups. (closes: 39420)

* Tue Dec 10 2019 Yuri N. Sedunov <aris@altlinux.org> 0.116-alt2
- updated to 0.116-10-gb806f0c (fixed memory leaks)

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 0.116-alt1
- 0.116

* Wed Jan 09 2019 Yuri N. Sedunov <aris@altlinux.org> 0.115-alt5
- updated to 0.115-26-gc898fdf (fixed CVE-2018-19788)

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 0.115-alt4
- updated to 0.115-23fd211e
- Port the JS authority to mozjs-60
- Move D-Bus policy file to /usr/share/dbus-1/system.d/
- Drop deprecated use of g_type_class_add_private()
- Allow negative uids/gids in PolkitUnixUser and Group objects (fixed CVE-2018-19788)

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.115-alt3
- updated to 0.115-11-g6e1f826

* Wed Jul 18 2018 Yuri N. Sedunov <aris@altlinux.org> 0.115-alt2
- sem@: use -std=gnu++11 on %%e2k

* Tue Jul 10 2018 Yuri N. Sedunov <aris@altlinux.org> 0.115-alt1
- 0.115 (fixed CVE-2018-1116)

* Mon Apr 16 2018 Yuri N. Sedunov <aris@altlinux.org> 0.114-alt2
- rebuilt with libmozjs52-52.7.3

* Tue Apr 03 2018 Yuri N. Sedunov <aris@altlinux.org> 0.114-alt1
- 0.114 (ported to mozjs52)

* Sun Jul 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.113-alt3
- updated to 0.113-32-g766a2ea (ported to mozjs24)

* Wed Jul 27 2016 Yuri N. Sedunov <aris@altlinux.org> 0.113-alt2
- updated to 0.113-24-g2cc5ed5

* Thu Jul 02 2015 Yuri N. Sedunov <aris@altlinux.org> 0.113-alt1
- 0.113

* Tue Jun 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.112-alt4
- updated to 264cc195e (fixed FDO bugs #90879, 90877, 76358, 90829(CVE-2015-3218))

* Mon Apr 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.112-alt3
- updated to 2291767a0 (fixed FDO #83093, 88288 (ALT #30843))

* Thu Oct 02 2014 Yuri N. Sedunov <aris@altlinux.org> 0.112-alt2
- updated to 3497a9c3 (fixed FDO #83093, 78905, 77167, 60847...)

* Thu Sep 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.112-alt1
- 0.112

* Thu Jun 06 2013 Yuri N. Sedunov <aris@altlinux.org> 0.111-alt2
- updated to f613c31 (includes a fix from FDO #65130)

* Thu May 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.111-alt1
- 0.111
- build against libmozjs17

* Wed Feb 27 2013 Yuri N. Sedunov <aris@altlinux.org> 0.110-alt1
- 0.110 release

* Mon Dec 24 2012 Yuri N. Sedunov <aris@altlinux.org> 0.109-alt1
- pre 0.110 (d6acecdd)
- removed upstreamed patches
- fixed helper path (ALT #28272)

* Wed Dec 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.108-alt3
- added libmozjs to reqs

* Wed Dec 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.108-alt2
- attempt to open the correct libmozjs185 library, otherwise polkit
  auth rules will not work unless js-devel is installed (fc patch)
- create polkitd user/group in %%pre
- fixed permissions for rules.d directories as recommended
- packaged lost polkit.service

* Wed Dec 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.108-alt1
- 0.108

* Sun Sep 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.107-alt1
- 0.107

* Sat May 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.105-alt1
- 0.105

* Thu Jan 19 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.104-alt1
- 0.104

* Fri Aug 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.102-alt1
- 0.102

* Mon Apr 25 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.101-alt2
- update to master git.7c59052 (fixed CVE-2011-1485)

* Tue Mar 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.101-alt1
- 0.101

* Tue Feb 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.100-alt1
- 0.100

* Tue Feb 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt3
- rebuild

* Wed Oct 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt2
- updated build dependencies

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt1
- 0.99

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt3
- rebuild

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt2
- rebuild

* Sat Jan 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt1
- 0.96

* Thu Nov 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.95-alt1
- 0.95

* Wed Aug 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.94-alt1
- 0.94

* Tue Aug 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.93-alt1
- 0.93

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt7
- relocated devel files

* Thu Feb 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt6
- fixed D-Bus policy (fd.o #18948)

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt5
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt4
- added suid for polkit-grant-helper-pam

* Thu Nov 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt3
- /usr/libexec/PolicyKit/polkit-*: fixed permission

* Sat Aug 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt2
- API fixed in CK 0.3

* Fri Aug 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt1
- 0.9

* Thu Apr 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt1
- 0.8
- rename subpackage libPolicyKit to libpolkit

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7-alt3
- fixed CVE-2008-1658
- drop polkit-bash-completion.sh (close #15232)

* Tue Apr 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7-alt2
- fixed read default policy on reiserfs/xfs

* Fri Jan 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7-alt1
- 0.7

* Fri Oct 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6-alt1
- 0.6

* Sun Jul 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.4-alt1
- 0.4

* Mon Jun 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.3-alt1
- 0.3

* Mon Jun 11 2007 Igor Zubkov <icesik@altlinux.org> 0.2-alt7.git20060822
- move gtk-doc documentation to devel subpackage (closes #12008)
- buildreq

* Tue Feb 20 2007 Igor Zubkov <icesik@altlinux.org> 0.2-alt6.git20060822
- fix attr's for %%_var/run/polkit

* Mon Dec 25 2006 Igor Zubkov <icesik@altlinux.org> 0.2-alt5.git20060822
- rebuild with new dbus

* Tue Nov 28 2006 Igor Zubkov <icesik@altlinux.org> 0.2-alt4.git20060822
- small fix for thresh@ changes
- s/%%make_build/make/ (fix build in hasher)
- change polkit group to _polkit
- change polkit user to _polkit

* Mon Nov 27 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.2-alt3.git20060822
- Some spec cleanup.
- Some buildrequires cleanup.
- Some descriptions cleanup.
- Fix docs packaging.
- Altify user creation in %%pre.

* Mon Nov 20 2006 Igor Zubkov <icesik@altlinux.org> 0.2-alt2.git20060822
- disable -Werror

* Mon Nov 20 2006 Igor Zubkov <icesik@altlinux.org> 0.2-alt1.git20060822
- rename spec from policykit.spec to PolicyKit.spec
- s/%%make/%%make_build/
- add HACKING to docs
- remove INSTALL from docs
- correct License from GPL to AFL/GPL
- add Packager tag
- add pam module subpackage
- build with -Werror by default
- add PolicyKit-devel-static subpackage

* Tue Nov 14 2006 Alexey Shabalin <shaba@altlinux.ru> 0.2_git20060822-alt0.1
- initial build
