%define nagios_grp nagiosnew

Name: nagios-nsca
Version: 2.9.2.1
Release: alt5

Summary: Nagios addon to send check results to a central monitoring server

Group: Monitoring
License: GPLv2
Url: https://sourceforge.net/projects/nagios/

Source: nsca-%version.tar

Patch0: nsca.cfg-2.9.2-alt.patch
Patch1: nsca.xinetd-2.9.2-alt.patch
Patch2: nsca-send-host-in-config-%version.patch
Patch3: nsca-custom-notifications-%version.patch

BuildRequires: libnsl2-devel libsocket libmcrypt-devel

Requires: nagios >= 3.0.6-alt12
Requires: xinetd

%description
This program is designed to accept passive service check results from
clients that use the send_nsca utility and pass them along to the
Nagios process by using the external command
interface. The program can either be run as a standalone daemon or as
a service under inetd. If you have libmcrypt installed on your systems,
you can choose from multiple crypto algorithms (DES, 3DES, CAST, xTEA,
Twofish, LOKI97, RJINDAEL, SERPENT, GOST, SAFER/SAFER+, etc.) for
encrypting the traffic between the client and the server.
Encryption is important in this addon, as it prevents unauthorized users
from sending bogus check results to Nagios. Read the included SECURITY
document for more information.

This package provides the core agent running on the Nagios server

%package send
Summary: A program to send check results to a central Nagios server
Group: Monitoring

%description send
This program is designed to accept passive service check results from
clients that use the send_nsca utility (which is included in this package)
and pass them along to the Nagios process by using the external command
interface. The program can either be run as a standalone daemon or as
a service under inetd. If you have libmcrypt installed on your systems,
you can choose from multiple crypto algorithms (DES, 3DES, CAST, xTEA,
Twofish, LOKI97, RJINDAEL, SERPENT, GOST, SAFER/SAFER+, etc.) for
encrypting the traffic between the client and the server.
Encryption is important in this addon, as it prevents unauthorized users
from sending bogus check results to Nagios. Read the included SECURITY
document for more information.

This package provides the send_nsca utility running on the client.

%prep
%setup -n nsca-%version
%patch0 -p2
%patch1 -p2
%patch2 -p1
%patch3 -p1

%build
#%autoreconf
%configure --with-nsca-grp=%nagios_grp
%make_build

%install
#%makeinstall_std
install -D -m 0644 sample-config/nsca.cfg %buildroot%_sysconfdir/nagios/nsca.cfg
install -D -m 0644 sample-config/send_nsca.cfg %buildroot%_sysconfdir/nagios/send_nsca.cfg
install -D -m 0644 sample-config/nsca.xinetd %buildroot%_sysconfdir/xinetd.d/nsca
install -D -m 0755 src/nsca %buildroot%_sbindir/nsca
install -D -m 0755 src/send_nsca %buildroot%_bindir/send_nsca

#%check
#%make_build check

%files
%config(noreplace) %_sysconfdir/xinetd.d/nsca
%_sbindir/nsca
%config(noreplace) %_sysconfdir/nagios/nsca.cfg
%doc Changelog LEGAL README SECURITY

%files send
%_bindir/send_nsca
%config(noreplace) %_sysconfdir/nagios/send_nsca.cfg
%doc Changelog LEGAL README SECURITY

%changelog
* Thu May 07 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2.1-alt5
- Document the new "host_address" client configuration option.

* Thu May 07 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2.1-alt4
- Set to use "nagiosnew" group in all configs.

* Tue Jan 28 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2.1-alt3
- Fix/improve: Log error on an unexpected message type.

* Tue Jan 28 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2.1-alt2
- Added support for sending host and service comments.

* Fri Jan 24 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2.1-alt1
- Support send/receive of custom notifications.
- send_nsca: The default configuration path is now
  /etc/nagios/send_nsca.cfg
- send_nsca: Now the host address can be specified in the
  configuration file.
- Apply the custom notifications patch
- xinetd.d/nsca: Set type = UNLISTED (thx lakostis@).

* Wed Jan 22 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2-alt2
- Fix: Do not replace xinetd.d/nsca config.
- Patching configuration files (paths).
- Fixed the xinetd.d path typo.

* Tue Jan 21 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2-alt1
- Initial release for Sisyphus.

* Tue Jan 21 2020 Paul Wolneykien <manowar@altlinux.org> 2.9.2-alt0
- Test release.
