Name: pam-config
Version: 1.9.0
Release: alt4

Summary: Systemwide PAM config files for Linux-PAM
License: GPLv2+
Group: System/Base
BuildArch: noarch

Source0: %name-%version.tar

Source2: pam_mktemp.control
Source3: system-auth.control
Source4: system-auth-chooser.in
Source5: system-policy.control
Source6: system-auth.filetrigger
Source7: system-policy.filetrigger
Source8: pam_access.control

%define _pamdir %_sysconfdir/pam.d

Requires(pre,postun): %name-control = %version-%release
Requires: libpasswdqc >= 0:1.1.0-alt0.2
Requires: libcrypt >= 4.4.4
Requires: pam_tcb >= 1.1.0.1
Provides: %_pamdir, /etc/security
Provides: pam-common = %version-%release
Obsoletes: pam-common < %version-%release
Provides: pam0-config = %version-%release
Obsoletes: pam0-config < %version-%release
# Compatibility.
Provides: pam(system-auth), pam(system-auth-use_first_pass), pam(other)
# These requirements are optional.
%filter_from_requires /^PAM(pam_\(ccreds\|krb5\|ldap\|pkcs11\|winbind\)\.so)/d

# due to %_pamdir/other
Conflicts: pam < 0:0.75-alt21
# due to pam_mktemp.so
Conflicts: openssh-server < 0:4.6p1

BuildPreReq: rpm-macros-pam

%package control
Summary: Control rules for the systemwide PAM config files
Group: System/Base

%description
PAM (Pluggable Authentication Modules) is a system security tool
which allows system administrators to set authentication policy
without having to recompile programs which do authentication.

This package contains systemwide config files for Linux-PAM.

%description control
This package contains control rules for systemwide PAM config files.
See control(8) for details.

%prep
%setup

%build
template='%_sourcedir/system-auth-chooser.in'
for only in system-auth-*-only; do
	target="${only%%-only}"
	method="${target##*-}"
	[ "$method" != 'local' ] || continue
	base="${target%%-$method}"
	{
		echo '#%%PAM-1.0'
		for type in auth account password session; do
			grep -q "^$type" "$only" || continue
			sed -e "s/@TYPE@/$type/" \
			    -e "s/@BASE@/$base/" \
			    -e "s/@METHOD@/$method/" \
			    "$template"
		done
	} > "$target"
done

%install
mkdir -p %buildroot{%_pamdir,%_controldir,/etc/security}

cp -a * %buildroot%_pamdir/
chmod 644 %buildroot%_pamdir/*

for f in pam_access pam_mktemp system-auth system-policy; do
	install -pm755 %_sourcedir/$f.control %buildroot%_controldir/$f
done

for f in system-auth system-policy; do
	install -Dm0755 %_sourcedir/$f.filetrigger %buildroot%_rpmlibdir/$f.filetrigger
done

%pre
%pre_control pam_mktemp
%pre_control pam_access
for f in %_pamdir/system-auth %_pamdir/system-auth-use_first_pass %_pamdir/system-policy; do
	if [ -f "$f" -a ! -L "$f" ]; then
		mv -f "$f" "$f-local" &&
		ln -f "$f-local" "$f-local.rpmsave" &&
		touch "/var/run/${f##*/}-local.update" &&
		ln -s "${f##*/}-local" "$f" ||:
	fi
done
%pre_control system-auth
if [ -f "%_pamdir/system-policy" ]; then
	%pre_control system-policy
fi

%post
cd %_pamdir
for f in system-auth system-auth-use_first_pass system-policy; do
	if [ -f "/var/run/$f-local.update" -a -f "$f-local.rpmsave" ]; then
		[ -f "$f-local.rpmnew" ] ||
			ln -f "$f-local" "$f-local.rpmnew" ||:
		mv -f "$f-local.rpmsave" "$f-local" &&
			rm -f "/var/run/$f-local.update" ||:
		cmp -s "$f-local" "$f-local.rpmnew" &&
			rm -f "$f-local.rpmnew" ||:
	fi
done
for f in system-auth system-policy; do
	if [ ! -f "$f" ]; then
		if [ -f "$f.rpmsave" ]; then
			cp -af "$f.rpmsave" "$f"
		elif [ -f "$f.rpmnew" ]; then
			cp -af "$f.rpmnew" "$f"
		fi
	fi
done
%post_control -s local system-auth
if [ $1 -ge 2 ]; then
	status_dir='/var/run/control'
	status_file="$status_dir/system-policy"
	[ -f "$status_file" ] || {
		mkdir -p "$status_dir"
		if [ "$(/usr/sbin/control system-auth)" = "local" ]; then
			echo local
		else
			echo remote
		fi > "$status_file"
	}
fi
%post_control -s local system-policy
%post_control -s enabled pam_mktemp
%post_control -s disabled pam_access

%triggerpostun -- pam <= 0:0.75-alt8
[ $2 -gt 0 ] || exit 0
cd %_pamdir
if [ ! -f system-auth ]; then
	if [ -f system-auth.rpmsave ]; then
		cp -pf system-auth.rpmsave system-auth
	elif [ -f system-auth.rpmnew ]; then
		cp -pf system-auth.rpmnew system-auth
	fi
fi

%files
%dir %_pamdir
%config %_pamdir/other
%config(noreplace) %_pamdir/system-auth-common
%config(noreplace) %_pamdir/*-local
%config(noreplace) %_pamdir/*-only
%config(noreplace) %_pamdir/*-ldap
%config(noreplace) %_pamdir/*-krb5
%config(noreplace) %_pamdir/*-krb5_ccreds
%config(noreplace) %_pamdir/*-multi
%config(noreplace) %_pamdir/*-pkcs11
%config(noreplace) %_pamdir/*-winbind
%config(noreplace) %_pamdir/*-remote
%config(noreplace) %_pamdir/common-login*
%_pamdir/system-auth
%_pamdir/system-auth-use_first_pass
%_pamdir/system-policy
%_rpmlibdir/system-auth.filetrigger
%_rpmlibdir/system-policy.filetrigger
/etc/security

%files control
%config %_controldir/*

%changelog
* Wed Jul 08 2020 Ivan Razzhivin <underwit@altlinux.org> 1.9.0-alt4
- add pam_access control

* Wed May 27 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.9.0-alt3
- Fix an error in system-policy.filetrigger in 1.9.0-alt1.

* Mon May 25 2020 Dmitry V. Levin <ldv@altlinux.org> 1.9.0-alt2
- Fix an error in %%post introduced in 1.9.0-alt1.

* Sat May 16 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.9.0-alt1
- Added configurable substack system-policy.
- Added filetriggers for system-auth and system-policy methods
  to avoid unknown state during upgrade and uninstall.
- system-auth-winbind-only: use default ccache.
- Split system-auth{,-use_first_pass}-{krb5,krb5_ccreds,ldap,winbind} (by ldv@)
  All five methods rewrited using pam_localuser as a chooser:
  if pam_localuser concludes the authenticating user is local, then use local
  method for authentication, otherwise use the corresponding non-local method.

* Wed May 13 2020 Dmitry V. Levin <ldv@altlinux.org> 1.8.0-alt1
- Removed prefix=$2y$ count=8 from pam_tcb options (closes: #36279).
- system-auth-local: split into system-auth-local-only
  and system-auth-common.
- system-auth-use_first_pass-local: likewise, split into
  system-auth-use_first_pass-local-only and system-auth-common.
- Merged pam0-config subpackage into pam-config.

* Tue Feb 03 2015 Dmitry V. Levin <ldv@altlinux.org> 1.7.0-alt1
- Added winbind authentication support (by cas@).

* Thu Nov 08 2012 Dmitry V. Levin <ldv@altlinux.org> 1.6.0-alt1
- Added krb5+ccreds authentication support (by boyarsh@).
- system-auth*-pkcs11: changed to use system-auth*-local
  instead of cut-n-pasting from there.

* Wed Sep 19 2012 Dmitry V. Levin <ldv@altlinux.org> 1.5.4-alt1
- common-login: added pam_nologin.so to account management list.

* Fri Aug 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1.5.3-alt1
- system-auth-*: changed to use the "$2y$" hash encoding prefix.

* Sat May 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.5.2-alt1
- common-login: added optional pam_systemd.so (closes: #25606).

* Wed Jun 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.5.1.1-alt1
- Moved /lib*/security to filesystem package.
- Packaged as noarch.

* Tue Jun 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.5.1-alt1
- Added common-login and common-login-use_first_pass.

* Fri Aug 07 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.0.2-alt1
- NMU:
  + added PKCS#11 authentication support (closes: #20946)

* Tue Jun 30 2009 Dmitry V. Levin <ldv@altlinux.org> 1.5.0.1-alt1
- Fixed system-auth*-multi introduced in previous release.

* Fri Jun 26 2009 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- Reindented pam config files to use tabs instead of spaces.
- system-auth-*: Rewritten "sufficient" controls with conditional jumps.
- Added experimental pam configs:
  system-auth-multi, system-auth-use_first_pass-multi.

* Sun Apr 12 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.5.1-alt1
- system-auth-krb5: Added pam_mkhomedir.so to the session stack (closes: #19540).

* Fri Apr 10 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt1
- system-auth-ldap: Added pam_mkhomedir.so to the session stack (closes: #19540).

* Thu Mar 26 2009 Evgeny Sinelnikov <sin@altlinux.ru> 1.4.4.1-alt1
- pam_mktemp.control: added system config autodetection

* Fri Oct 10 2008 Ivan A. Melnikov <iv@altlinux.org> 1.4.4-alt1
- system-auth.control: added authentication method autodetection
- added kerberos 5 authentication support

* Tue Sep 18 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.1-alt1
- system-auth-use_first_pass-ldap: Fixed typo.

* Fri Jun 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- system-auth-{local,ldap}: Replaced pam_passwdqc.so parameters
  with reference to /etc/passwdqc.conf file.

* Tue Jun 05 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- Fixed system-auth upgrade.

* Sat Jun 02 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.1-alt1
- Added ldap authentication support (inger).

* Mon May 28 2007 Stanislav Ievlev <inger@altlinux.org> 1.4.0-alt1.1
- add support for ldap authentication

* Thu Apr 05 2007 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt1
- system-auth: Moved pam_mktemp.so from "account" to "session".
- Added pam_mktemp control, based on script from raorn@.

* Mon Jan 16 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt1
- Do not suppress all autogenerated dependencies (#8849).

* Thu Jan 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- Updated for new style PAM dependencies generated by rpm-build-4.0.4-alt55.

* Fri Aug 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Added "nullok" option to password management entry (#7606).

* Thu May 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- system-auth: Added "account required pam_mktemp.so" (#6814).
- Added multilib support (mouse, closes #6098).

* Sat Oct 04 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.7-alt1
- pam-config: merged pam-common into this package.

* Wed Jul 09 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.6-alt1
- Keep all configuration files in the main package, pam-config.
- Kepp all pam dependencies in pam-specific subpackages.

* Wed Jul 02 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.5-alt1
- Added -flavour subpackage and moved dependencies there.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- PAM configuration policy enforcement.

* Thu Apr 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.3-alt1
- Added prefix= and count= parameters for auth tcb methods.
  This is required to activate timing attack protection
  implemented in pam_tcb-0.9.8.4-alt1.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.1.2-alt1
- Added password entry for system-auth-use_first_pass.

* Thu Dec 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.1.1-alt1
- Changed password quality enforcement policy:
  enforce=everyone --> enforce=users.

* Mon Dec 17 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.1-alt1
- Switched to tcb.

* Mon Dec 17 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.1-alt1
- Added new config for userpass support: system-auth-use_first_pass.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0-alt1
- Initial revision.
- Updated system-auth from pam package now lives here.
