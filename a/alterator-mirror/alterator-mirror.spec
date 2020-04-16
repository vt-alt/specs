%define _altdata_dir %_datadir/alterator

Name: alterator-mirror
Version: 0.4.9
Release: alt1

Source:%name-%version.tar

Summary: local mirrors setup and maintainance
License: GPL
Packager: Stanislav Ievlev <inger@altlinux.org>

Group: System/Configuration/Other

Requires: alterator >= 5.3 alterator-sh-functions >= 0.10-alt5 libshell
Requires: sisyphus-mirror >= 0.8.3
Requires: alterator-l10n >= 2.4-alt9 altlinux-repos
Requires: vixie-cron

BuildPreReq: alterator >= 5.0
BuildRequires: alterator-fbi

%ifarch %e2k
BuildRequires: guile20-devel libguile20-devel
%else
BuildRequires: guile22-devel
%endif

Conflicts: alterator-fbi < 5.17-alt4
Conflicts: apt-conf-sisyphus < 5.0-alt3
Conflicts: apt-conf-desktop < 5.0-alt2
Conflicts: apt-conf-branch < 5.0-alt2

%define _unpackaged_files_terminate_build 1

%description
local mirrors setup and maintainance

%prep
%setup -q

%build
%make_build

%install
%makeinstall
install -d %buildroot%_logdir/%name
install -Dpm640 %name.logrotate %buildroot%_sysconfdir/logrotate.d/%name

%files
%config(noreplace) %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/alterator/mirror
%_sbindir/*
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_datadir/alterator/type/*
%_alterator_libdir/ui/*
%_alterator_libdir/type/*
%_alterator_backend3dir/*
%attr(700,root,adm) %_logdir/%name

%changelog
* Tue Apr 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- Enable and start crond service to start scheduled execution.

* Thu Aug 30 2018 Paul Wolneykien <manowar@altlinux.org> 0.4.8-alt1
- Fixed hour:minute parsing of the input time values.

* Wed Aug 29 2018 Paul Wolneykien <manowar@altlinux.org> 0.4.7-alt1
- Fix: Use (a fixed) keyword-list type for the "arch" parameter.

* Thu Aug 23 2018 Paul Wolneykien <manowar@altlinux.org> 0.4.6-alt1
- Fix: Use "hostname" type for the branch name (can contain periods).

* Tue Aug 21 2018 Paul Wolneykien <manowar@altlinux.org> 0.4.5-alt1
- Fixed the reported time value: only hours and mins.
- Use strict data types for "name", "arch", "weekday" and "time"
  parameters.

* Fri Apr 13 2018 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt1.1.1
- NMU: Replace BuildRequires for guile on e2k arch.

* Tue Oct 31 2017 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1
- Use _unpackaged_files_terminate_build.
- Changes for guile22.
- Fix size calculation regexp.

* Mon Jul 27 2015 Aleksey Avdeev <solo@altlinux.org> 0.4.3-alt1
- fix support hardlink between repositories (ALT #31162)

* Mon Jun 10 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.2-alt1
- fix lang (ALT#21593)
- drop x86_32

* Mon Jun 03 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.1-alt2
- add R: altlinux-repos

* Fri May 04 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.1-alt1
- add support for new arepo

* Tue Aug 23 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4-alt1
- add support for arepo and arm repositories

* Tue Aug 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- use workflow 'none'
- improve schedule setup (closes: #20370)

* Mon Jun 08 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt9
- create destdir if it doesn't exists (closes: #20369)

* Thu Apr 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- fix work if /srv is a symlink

* Thu Apr 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- menu file: move to "servers" group, update translations

* Fri Mar 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- fix menu file

* Thu Mar 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- relocate module data to /srv/public
- little interface improvements

* Mon Mar 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- fix module name

* Fri Feb 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- improve local mirrors publication

* Thu Feb 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- publish updates in avahi
- fix url re

* Wed Feb 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- redesign module to use as a server for automatic updates

* Tue Feb 03 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- use external mirror and repository databases from apt-conf
- minor module update

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt3
- move translations to alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt2
- rebuild with new l10n

* Thu Nov 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

