Name:     nagios-domain-discovery
Version:  0.1.1
Release:  alt1

Summary:  Domain records to Nagios host list synchronization tool
License:  GPL-3.0-or-later
Group:    Monitoring
Url:      http://git.altlinux.org/people/manowar/packages/nagios-domain-discovery.git

Packager: Paul Wolneykien <manowar@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch
BuildRequires: ronn

%description
nagios-domain-discovery is a tool to create and update the
configuration of hosts under Nagios monitoring based on the
domain records.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%dir %_sysconfdir/nagios/domain-discovery
%config(noreplace) %_sysconfdir/nagios/domain-discovery/*.conf
%_sbindir/%name
%_libexecdir/%name
%_man8dir/%{name}*.8*
%_man5dir/%{name}*.5*
%_unitdir/%name.*

%changelog
* Fri Feb 28 2020 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Fix: Do not replace the configs.
- Fixed system unit files.
- Improve host configuration parsing: trim possible comments.
- Use KEEPLIST to protect some hosts from deletion.
- Fixed various errors.

* Tue Feb 18 2020 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial version for Sisyphus.
