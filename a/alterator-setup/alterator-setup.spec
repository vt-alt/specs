%define _altdata_dir %_datadir/alterator

Name: alterator-setup
Version: 0.3.4
Release: alt1

Summary: Perform initial setup of an OEM installation (warning!)
License: GPLv2
Group: System/Configuration/Other

Url: http://www.altlinux.org/Alterator
Source: %name-%version.tar

BuildArch: noarch
BuildPreReq: alterator >= 4.10-alt6
BuildRequires: rpm-macros-alterator

Requires: libshell
Requires: alterator-l10n >= 2.5-alt1
Requires: alterator-browser-qt >= 2.17.0
Requires: alterator-lookout => 2.4-alt1
Requires: alterator-wizardface
Requires: alterator-notes
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-root
Requires: alterator-users

Requires(post): chkconfig
Requires(preun): chkconfig

Conflicts: alterator-livecd
Conflicts: installer-common-stage2

%description
%summary

WARNING: you really don't want to install this package
into an already configured system as it may spoil the
next boot!  Given that its sole purpose is the _initial_
configuration of a new system (like setting root password)
nobody should need that on an up-and-running host.

%prep
%setup

%install
%makeinstall

# TODO: alterator-wizardface might take a parameter
mkdir -p %buildroot%_datadir/install2
ln -s ../../..%_sysconfdir/alterator-setup/steps \
	%buildroot%_datadir/install2/installer-steps

cat >> %buildroot%_sysconfdir/alterator-setup/config << EOF
# erase %name and related packages
REMOVE_SELF=1
EOF

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_initdir/setup
%_sbindir/%name
%_alterator_datadir/steps/*
%_alterator_datadir/ui/*
%_alterator_libdir/hooks/*/*
%_alterator_backend3dir/*
%_datadir/alterator-setup/
%_datadir/install2/installer-steps
/lib/systemd/system/setup.*

# the restore is done in postinstall script
# triggered by successful completion of the module
# as it can be reused now (doesn't self destruct)
%post
%post_service setup
[ -d /etc/systemd/system ] || exit 0
mv /etc/systemd/system/default.target /etc/systemd/system/default.target.bak ||:
ln -sf /lib/systemd/system/setup.target /etc/systemd/system/default.target

# package is removed in postinstall hook, but
# 'systemd stop' stops whole setup.service with hook.
%preun
if [ -x /sbin/sd_booted ]; then
/sbin/sd_booted || %preun_service setup
fi

%changelog
* Fri Feb 14 2020 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1
- postinstall: Run indexhtml-update.

* Fri Dec 27 2019 Anton Midyukov <antohami@altlinux.org> 0.3.3-alt6
- setup.service: restart always (e.g. restart when X falls)

* Thu Dec 12 2019 Anton Midyukov <antohami@altlinux.org> 0.3.3-alt5
- add conflicts with alterator-livecd, installer-common-stage2

* Fri Dec 06 2019 Ivan A. Melnikov <iv@altlinux.org> 0.3.3-alt4
- remove rootfs-installer-features on cleanup, if present

* Fri Dec 28 2018 Ivan A. Melnikov <iv@altlinux.org> 0.3.3-alt3
- setup.service: relax dependency on plymouth-start.service

* Tue Sep 04 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.3.3-alt2
- closes: #35276

* Tue Sep 04 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.3.3-alt1.0.mips2
- Deleted now unnecessary reboot commands

* Tue Aug 21 2018 Dmitry Terekhin <jqt4@altlinux.org> 0.3.3-alt1.0.mips1
- Added forcible reboot to work around the incompatibility problem with
- systemd 238

* Tue Apr 03 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.3.3-alt1
- made service file more correct.

* Mon Apr 02 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.3.2-alt1
- fixed service file to make it work with modern systemd.

* Mon Apr 28 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.1-alt1
- preun: do not use preun_service on systemd.

* Mon Apr 21 2014 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- sysvinit support

* Wed Mar 26 2014 Michael Shigorin <mike@altlinux.org> 0.2.1-alt2
- added a warning to description

* Thu Mar 06 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.1-alt1
- Remove more packages during cleanup.

* Tue Jul 16 2013 Michael Shigorin <mike@altlinux.org> 0.2.0-alt1
- made self destruction optional (sysconfig knob)
- minor spec cleanup

* Fri Jul 12 2013 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- added license step

* Thu Jun 20 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release, thanks sem@

