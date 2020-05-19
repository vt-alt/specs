Name: alterator-nagios-secondary
Version: 1.0.3
Release: alt1

Url: http://www.altlinux.org/Alterator
Source:%name-%version.tar
Packager: Paul Wolneykien <manowar@altlinux.org>

Patch0: check_timed_logs-strict.patch

BuildArch: noarch

Summary: Alterator module to configure Nagios secondary checks
License: GPL-2.0-or-later
Group: System/Configuration/Other

Requires: nagios-plugins-timed-logs = %version-%release
Requires: alterator-standalone

Conflicts: alterator-lookout < 0.9-alt5
Conflicts: alterator-wizardface < 0.5-alt7

BuildPreReq: alterator >= 3.2-alt6

BuildRequires: perl-File-ReadBackwards perl-Time-Piece

%description
Alterator module to configure Nagios secondary checks.

%package -n nagios-plugins-timed-logs
Summary: Check logs for the appearance of a given RegEx within a given time period
Group: Monitoring
License: GPL

%description -n nagios-plugins-timed-logs
Check logs for the appearance of a given RegEx within a given time period

%prep
%setup
%patch0 -p2

%build
%make_build libdir=%_libdir

%install
%makeinstall
mkdir -p %buildroot%_sysconfdir/nagios/extinfo/secondary

%files
%dir %_sysconfdir/nagios/extinfo/secondary
%config(noreplace) %_sysconfdir/nagstamon/actions/*.conf
%_datadir/alterator/ui/*/
%_datadir/alterator/applications/*
%_alterator_backend3dir/*

%files -n nagios-plugins-timed-logs
%config(noreplace) %_sysconfdir/nagios/commands/*.cfg
%_libexecdir/nagios/plugins/*

%changelog
* Wed Apr 15 2020 Paul Wolneykien <manowar@altlinux.org> 1.0.3-alt1
- Added "check-host-alerts" command.
- Added check-nagios-alerts wrapper.
- Fixed syntax and arguments in the "check-service-alerts" command.
- Use Perl strict mode in check_timed_logs (patch).
- Fix: Use service description in the regexp.
- Fix: Use uppercase status values in the service config.

* Mon Apr 13 2020 Paul Wolneykien <manowar@altlinux.org> 1.0.2-alt1
- Reload nagios after each change.
- Fixed hostgroups reading.

* Mon Apr 13 2020 Paul Wolneykien <manowar@altlinux.org> 1.0.1-alt1
- Set minimal values for warning and critical times to 0.

* Mon Apr 13 2020 Paul Wolneykien <manowar@altlinux.org> 1.0.0-alt1
- Initial version.
