Name: cups
Version: 2.3.3
Release: alt1

Summary: Common Unix Printing System - server package
License: GPL
Group: System/Servers

Url: http://www.cups.org

Source: v%version.tar.gz

# READMEs
Source10: README.alt
Source11: README.patches

# MISC
Source20: cups.control
Source21: cups.startup

# support
Source95: %name.unused
Source96: repatch_spec.sh
Source97: alt_ru.po
Source98: pofix.py

## FC patches
Patch1: FC-system-auth.patch
Patch2: FC-multilib.patch
Patch3: FC-banners.patch
Patch4: FC-no-export-ssllibs.patch
Patch5: FC-direct-usb.patch
Patch6: FC-driverd-timeout.patch
Patch7: FC-logrotate.patch
Patch8: FC-usb-paperout.patch
Patch9: FC-uri-compat.patch
Patch10: FC-hp-deviceid-oid.patch
Patch11: FC-ricoh-deviceid-oid.patch
Patch12: FC-systemd-socket.patch
Patch13: FC-freebind.patch
Patch14: FC-ipp-multifile.patch
Patch15: FC-web-devices-timeout.patch
Patch16: FC-synconclose.patch
Patch17: FC-ypbind.patch
Patch18: FC-failover-backend.patch
Patch19: FC-lspp.patch
Patch20: FC-filter-debug.patch
Patch21: FC-dymo-deviceid.patch

## Ubuntu patches
Patch101: Ubuntu-0001-Fix-hyphen-used-as-minus-sign-manpage-errors.patch
Patch102: Ubuntu-0002-Install-root-backends-world-readable.patch
Patch103: Ubuntu-0003-Fix-jobs-with-multiple-files-or-multiple-formats.patch
Patch104: Ubuntu-0004-Fix-conversion-of-PPD-InputSlot-choice-names.patch
Patch105: Ubuntu-0005-Tests-Ignore-warnings-from-colord-and-Avahi.patch
Patch106: Ubuntu-0006-Tests-ignore-usb-dnssd-backend-unexpected-exits.patch
Patch107: Ubuntu-0007-Tests-ignore-loadFile-failures.patch
Patch108: Ubuntu-0008-Tests-ignore-errors-triggered-on-ipv6-deprived-hosts.patch
Patch109: Ubuntu-0009-Tests-ignore-the-failure-to-write-uncompressed-data.patch
Patch110: Ubuntu-0010-Tests-ignore-job-held-message.patch
Patch111: Ubuntu-0011-Tests-Do-not-run-the-CUPS_EUC_JP-test-case-on-BSD-Hu.patch
Patch112: Ubuntu-0012-Tests-Make-sure-that-all-scheduled-jobs-are-finished.patch
Patch113: Ubuntu-0013-Tests-Force-LC_-environment-variables-when-testing-n.patch
Patch114: Ubuntu-0014-Tests-Use-127.0.0.1-instead-of-localhost-to-help-pbu.patch
Patch115: Ubuntu-0015-Tests-Force-LC_ALL-C-environment-variable-when-grepp.patch
Patch116: Ubuntu-0016-Tests-Do-not-test-pdftourf.patch
Patch117: Ubuntu-0017-Move-cupsd.conf.default-from-SERVERROOT-to-DATADIR.patch
Patch118: Ubuntu-0018-Patch-to-support-Apple-AirPrint-printing-from-iPhone.patch
Patch119: Ubuntu-0019-Let-snmp-backend-also-use-manufacturer-specific-MIBs.patch
Patch120: Ubuntu-0020-Disable-time-stamps-in-conffiles-to-avoid-ever-chang.patch
Patch121: Ubuntu-0021-Do-not-write-VCS-tags-into-installed-conffiles.patch
Patch122: Ubuntu-0022-Rename-the-systemd-service-file-from-org.cups.cups.-.patch
Patch123: Ubuntu-0023-Do-not-use-host-names-for-broadcasting-print-queues-.patch
Patch124: Ubuntu-0024-CUPS-removes-the-recommended-comments-of-the-NickNam.patch
Patch125: Ubuntu-0025-Make-log-files-readable-to-group-adm-if-present.patch
Patch126: Ubuntu-0026-Deactivate-CUPS-own-log-rotating-as-the-system-alrea.patch
Patch127: Ubuntu-0027-Do-not-mess-with-the-permissions-of-cupsd.conf.patch
Patch128: Ubuntu-0028-Show-compile-command-lines.patch
Patch129: Ubuntu-0029-Set-the-default-for-SyncOnClose-to-Yes.patch
Patch130: Ubuntu-0030-Set-default-job-error-policy-to-retry-job.patch
Patch131: Ubuntu-0031-Drop-dangling-references-from-cups-lpd.man.patch
Patch132: Ubuntu-0032-Use-dpkg-architecture-in-cups-config-to-make-it-arch.patch
Patch133: Ubuntu-0033-Build-mantohtml-with-the-build-architecture-compiler.patch
Patch134: Ubuntu-0034-po4a-infrastructure-and-translations-for-manpages.patch
Patch135: Ubuntu-0005-Fix-scheduler-cupsd.conf-load.patch
Patch136: Ubuntu-0006-Fix-leakage-of-ppd.patch
Patch137: Ubuntu-0025-Add-Requires-cups.socket-to-cups.service-to-make-sur.patch

## ALT patches
Patch500: ALT-1.6.1-hardening.patch
Patch501: ALT-build_po.patch
Patch502: ALT-remove_BSD.patch
Patch503: ALT-enable-631.patch
Patch504: ALT-1.6.2-lpd-utf8.patch
Patch505: ALT-1.4.6-config-libs.patch
Patch506: ALT-1.6.2-lspp-SE.patch
Patch507: ALT-1.7.0-docroot-i18n.patch
Patch508: ALT-644.patch
Patch509: ALT-1.7.2-local_ipv6.patch
Patch510: ALT-config-nolibs.patch
Patch511: ALT-pwg-raster-attributes.patch
Patch512: ALT-2.1.0-lpd-sanitizer.patch
# ALT SE related patches
Patch552: ALT-ipp-alt-extension-copy-document.patch
Patch553: ALT-lspp-context+no-filename.patch
Patch555: ALT-2.1.0-check-PPD-SE.patch
Patch556: ALT-lspp-context-via-tcp.patch
Patch557: ALT-lspp-set-context-via-ipp.patch
Patch558: ALT-lspp-in-alt-job-ft.patch
Patch559: ALT-mime-pjl-pdf.patch
Patch560: ALT-SE-ippcalls.patch

## Provides
Provides: %name-ppd = %version %name-common = %version
Provides: cups-libs = %version

## External dependencies
Requires: printer-testpages bc cups-filters

# Automatically added by buildreq on Tue Dec 24 2013
# optimized out: libcom_err-devel libkrb5-devel libstdc++-devel libsystemd-daemon pkg-config
BuildRequires: gcc-c++ libacl-devel libaudit-devel libavahi-devel libdbus-devel libpam-devel libpaper-devel libselinux-devel libssl-devel libsystemd-daemon-devel systemd-devel libusb-devel xdg-utils zlib-devel

BuildRequires: dbus python python-module-polib
BuildRequires: libgnutls-devel

%description
The Common Unix Printing System provides a portable printing layer for
UNIX(TM) operating systems. It has been developed by Easy Software Products
to promote a standard printing solution for all UNIX vendors and users.
CUPS provides the System V and Berkeley command-line interfaces.

This is the main package needed for CUPS servers (machines where a
printer is connected to or which host a queue for a network
printer). It can also be used on CUPS clients so that they simply pick
up broadcasted printer information from other CUPS servers and do not
need to be assigned to a specific CUPS server by an
/etc/cups/client.conf file.

%package ipptool
Summary: Common Unix Printing System - tool for performing IPP requests
Group: System/Servers
License: GPL

%description ipptool
Sends IPP requests to the specified URI and tests and/or displays the results.

%package xinetd
Summary: Common Unix Printing System - xinetd profile
Group: System/Servers
BuildArch: noarch
License: GPL

%description xinetd
Common Unix Printing System - xinetd profile

%package -n lib%name
Summary: Common Unix Printing System - CUPS library
License: LGPL
Group: System/Servers

%description -n lib%name
The Common Unix Printing System provides a portable printing layer for
UNIX(TM) operating systems. This package contains the CUPS API library
which contains common functions used by both the CUPS daemon and all
CUPS frontends (lpr-cups, xpp, qtcups, kups, ...).

%package -n lib%name-devel
Summary: Common Unix Printing System - Development environment "libcups"
License: LGPL
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version %name-ddk = %version

%description -n lib%name-devel
The Common Unix Printing System provides a portable printing layer for
UNIX(TM) operating systems. This is the development package for
creating additional printer drivers, printing software, and other CUPS
services using the main CUPS library "libcups".

%prep
%setup -n %name-%version

## FC apply patches
%patch1 -p1 -b .system-auth
#patch2 -p1 -b .multilib
%patch3 -p1 -b .banners
%patch4 -p1 -b .no-export-ssllibs
%patch5 -p1 -b .direct-usb
%patch6 -p1 -b .driverd-timeout
%patch7 -p1 -b .logrotate
%patch8 -p1 -b .usb-paperout
#patch9 -p1 -b .uri-compat
%patch10 -p1 -b .hp-deviceid-oid
%patch11 -p1 -b .ricoh-deviceid-oid
%patch12 -p1 -b .systemd-socket
%patch13 -p1 -b .freebind
%patch14 -p1 -b .ipp-multifile
%patch15 -p1 -b .web-devices-timeout
%patch16 -p1 -b .synconclose
%patch17 -p1 -b .ypbind
%patch18 -p1 -b .failover
%patch19 -p1 -b .lspp
%patch20 -p1 -b .filter-debug
%patch21 -p1 -b .dymo-deviceid

## Ubuntu apply patches
%patch101 -p1
%patch102 -p1
#patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
#patch119 -p1
%patch120 -p1
%patch121 -p1
#patch122 -p1
%patch123 -p1
%patch124 -p1
##patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
#patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
#patch134 -p1
%patch135 -p1
##patch136 -p1
##patch137 -p1

## ALT apply patches
##patch500 -p1
%patch501 -p1
%patch502 -p1
%patch503 -p1
%patch504 -p1
#patch505 -p1
%patch506 -p1
%patch507 -p1
%patch508 -p1
%patch509 -p1
#patch510 -p1
%patch511 -p1
%patch512 -p2

# ALT SE related patches
%patch552 -p1
%patch553 -p1
%patch555
%patch556 -p1
%patch557 -p1
%patch558 -p1
%patch559 -p1
%patch560 -p2

cp %SOURCE98 %SOURCE97 %SOURCE10 %SOURCE11 .
cp %SOURCE21 scheduler/cups.sh.in

# TODO help translation injecting

%build
aclocal -I config-scripts
autoconf -I config-scripts

export LIBS="-laudit -lselinux"
%configure \
   --with-system-groups='sys wheel root' \
   --with-icondir=%_iconsdir \
   --with-menudir=%_desktopdir \
   --with-xinetd=%_sysconfdir/xinetd.d \
   --enable-relro \
   --enable-dbus \
   --enable-libusb \
   --with-cups-user=lp \
   --with-cups-group=lp \
   --with-log-file-perm=0600 \
   --with-docdir=%_docdir/%name \
   --with-rcdir=%_initdir/.. \
   --localstatedir=%_var \
   --enable-avahi \
   --with-local_protocols='dnssd' \
   --enable-lspp \
   --enable-libpaper \
   --enable-debug \
   --enable-gnutls \
   %nil

%make_build

(
cd locale
make pot
mv cups_ru.po cups_old_ru.po
msgmerge cups_old_ru.po cups.pot -C ../alt_ru.po -o cups_ru.po
python2 ../pofix.py cups_ru.po
)

%install
make BUILDROOT=%buildroot install

# fixup funny org.cups.*.* names
( cd %buildroot%_unitdir;
for f in *; do
  case "$f" in
    org.cups.cupsd.*) ln -s "$f" cups."${f##*.}";;
    org.cups.*) ln -s "$f" "${f/org.cups./}";;
  esac;
done;
echo "###"; ls
)

### install non-upstream files
install -D scheduler/cups-lpd.xinetd %buildroot%_sysconfdir/xinetd.d/cups-lpd
install -Dpm 755 %SOURCE20 %buildroot%_controldir/%name

alternate() { # priority files \
p="$1"; shift; \
for f; do \
  case "$f" in \
  	*/sbin/*) man=8;; \
  	*/bin/*) man=1;; \
	*/etc/*|*/share/*) man=5;; \
	*) man=6;; \
  esac; \
  mp="%_mandir/man$man"; \
  n="$(basename "$f")"; fa="$f-%name"; m="$mp/$n.$man"; ma="$mp/$n-%name.$man"; \
  /bin/echo -e "$f $fa $p\n$m.gz $ma.gz $fa"; \
  mv "%buildroot$f" "%buildroot$fa"; mv "%buildroot$m" "%buildroot$ma"; \
done }

alternate 10 \
	/usr/bin/lpr \
	/usr/bin/lpq \
	/usr/bin/lprm \
	/usr/bin/lp \
	/usr/bin/cancel \
	/usr/bin/lpstat \
	/usr/sbin/lpc > %name.alternative

install -D %name.alternative %buildroot%_altdir/%name
# #36909 close
chmod 755 %buildroot/usr/lib/cups/backend/ipp

%post
%post_service cups

%preun
%preun_service cups
%files
%doc README*
%_docdir/%name
%config(noreplace) %_sysconfdir/%name
%config(noreplace) %attr(0640,root,lp) %_sysconfdir/%name/snmp.conf
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/dbus-1/system.d/*
%_controldir/%name
%_unitdir/*
%_initdir/%name
%prefix/lib/%name
%_man1dir/*
%_man5dir/*
%_man8dir/*
%_man7dir/*

%_datadir/%name
%_datadir/locale/*/*.po
%_sbindir/*
%_bindir/*
%_altdir/%name

%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/%name.desktop

%exclude %prefix/*/*/*/ipptool*
%exclude %prefix/*/*/ipptool*
%exclude %prefix/*/ipptool*
%exclude %_bindir/%name-config
%exclude %_bindir/ppd*
%exclude %_mandir/*/ppd*
%exclude %_datadir/%name/examples
%exclude %_sysconfdir/rc.d/rc*.d

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_bindir/ppd*
%_includedir/%name
%_datadir/%name/examples
%_libdir/*.so
%_man1dir/ppd*
%_man5dir/ppd*

%files ipptool
%_bindir/ipptool
%_datadir/cups/ipptool
%_man1dir/ipptool.*

%files xinetd
%config(noreplace) %_sysconfdir/xinetd.d/%name-lpd

%changelog
* Thu Jan 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.3-alt1
- Updated to upstream version 2.3.3 (Fixes CVE-2019-8842, CVE-2020-3898).
- Built with gnutls support re-enabled.
  Gnutls support may be required by cups-filters.

* Mon Aug 03 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.1-alt2
- NMU: fixed build with new selinux.

* Thu Mar 05 2020 Fr. Br. George <george@altlinux.ru> 2.3.1-alt1
- Autobuild version bump to 2.3.1
- Update patches (manual FC-lspp.patch fix)
- Separate xinetd config (closes: #38181)
- Fix backend attributes (closes: #36909)

* Fri Dec 13 2019 Ivan A. Melnikov <iv@altlinux.org> 2.2.12-alt4
- Explicitly use python2 in %%build to fix FTBFS

* Mon Nov 11 2019 Fr. Br. George <george@altlinux.ru> 2.2.12-alt3
- Add wheel to system-groups list

* Tue Aug 27 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.2.12-alt2
- ALT SE related patches added

* Mon Aug 26 2019 Fr. Br. George <george@altlinux.ru> 2.2.12-alt1
- Autobuild version bump to 2.2.12
- Update patches
- Fix LSPP patch

* Wed Mar 27 2019 Fr. Br. George <george@altlinux.ru> 2.2.11-alt1
- Autobuild version bump to 2.2.11
- Update patches

* Mon Mar 11 2019 Fr. Br. George <george@altlinux.ru> 2.2.10-alt2
- Fix UTF8->ASCII task header conversion (thanks klark@)

* Thu Feb 28 2019 Fr. Br. George <george@altlinux.ru> 2.2.10-alt1
- Autobuild version bump to 2.2.10
- Update patches

* Thu Feb 28 2019 Fr. Br. George <george@altlinux.ru> 2.2.9-alt1
- Version up
- Update patchesY

* Tue Nov 07 2017 Fr. Br. George <george@altlinux.ru> 2.2.6-alt1
- Version up
- Update patches

* Mon Feb 27 2017 Fr. Br. George <george@altlinux.ru> 2.2.2-alt1
- Version up

* Wed Nov 23 2016 Fr. Br. George <george@altlinux.ru> 2.2.1-alt1
- Version up
- Update patches

* Tue Nov 22 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.1.4-alt1
- bugfix realese
- Remove upstreamed patches:
     Patch101: Ubuntu-usb-backend-fix-infinite-loop-when-usblp-module-attached.patch
     Patch102: Ubuntu-usb-backend-delayed-closing-for-old-laserjets.patch
     Patch103: Ubuntu-fix-ppd-file-load-for-ipp-printers.patch
- refresh:
     ALT-1.6.2-lpd-utf8.patch
     FC-dnssd-deviceid.patch
     FC-libusb-quirks.patch

* Mon Jan 18 2016 Fr. Br. George <george@altlinux.ru> 2.1.0-alt2
- Fix build

* Wed Nov 11 2015 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Version up
- Refresh patches
- Keep old-style service names

* Tue Apr 28 2015 Fr. Br. George <george@altlinux.ru> 2.0.2-alt1
- Version up
- Refresh patches
- Drop port hardening patch
- Fix translation script typo

* Mon Nov 24 2014 Fr. Br. George <george@altlinux.ru> 2.0.1-alt1
- Version up (major version ups is not really major difference)

* Wed Aug 27 2014 Fr. Br. George <george@altlinux.ru> 1.7.5-alt1
- Version up

* Wed Jul 09 2014 Fr. Br. George <george@altlinux.ru> 1.7.3-alt4
- Restore part of the previous for being debian-unspecific

* Thu Jul 03 2014 Fr. Br. George <george@altlinux.ru> 1.7.3-alt3
- Remove Debian-specific config patch

* Wed Jun 25 2014 Fr. Br. George <george@altlinux.ru> 1.7.3-alt2
- Restore Mandrake init script (closes: #30137)

* Mon Jun 16 2014 Fr. Br. George <george@altlinux.ru> 1.7.3-alt1
- Version up
- Allow requests from IPV4-to-IPV6 mapped localhost (RH#737230)

* Thu Apr 24 2014 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt2
- fix perm for data (444 -> 644)
- use Makefile for install systemd units (install cups.socket too)

* Mon Apr 21 2014 Fr. Br. George <george@altlinux.ru> 1.7.2-alt1
- Version up
- Previous version unreleased, so autoclose bugs again
- (closes: #29910, #29445, #29908)

* Wed Apr 16 2014 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Version up (closes: #29910, #29445)
- Compatibility provide: cups-libs (closes: #29908)
- FC and Ubuntu patchset update
- Add post_service/preun_service

* Mon Feb 24 2014 Fr. Br. George <george@altlinux.ru> 1.7.0-alt2
- Resurrect alternatives (closes: #29825)

* Tue Dec 17 2013 Fr. Br. George <george@altlinux.ru> 1.7.0-alt1
- Total rebuild from FC and Ubuntu
- Change packaging scheme
- Revise and apply all FC and Ubuntu patches
- Prepere to separate russian translation

* Thu Oct 31 2013 Andriy Stepanov <stanv@altlinux.ru> 1.6.2-alt4
- Add patch: always pass SeLinux info

* Wed Oct 30 2013 Fr. Br. George <george@altlinux.ru> 1.6.2-alt3.2
- Apply FC dbus-utf8 patch
- Reproduce this patch to cups-lpd (Closes: #25937)

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 1.6.2-alt3.1
- Freshen LSPP patch (closes: #29477)
- Rebuild with debuginfo

* Wed May 29 2013 Alexander Plehanov <tonik@altlinux.org> 1.6.2-alt3
- Remove patches,which were applied in upstream version:
    cups-1.6.1-defconf.patch
    cups-1.5.4-rh-usblp-quirks.patch
    cups-1.6.1-ubuntu-prevent-crash-due-to-null-host-name-or-fqdn-from-avahi.patch
    cups-1.6.1-ubuntu-fix-crash-on-shutdown-caused-by-broken-avahi-config.patch
    cups-1.6.1-ubuntu-ipp-backend-abort-the-outer-loop-if-we-get-a-failure-from-send-document.patch
    cups-1.6.1-ubuntu-ipp-backend-could-get-stuck-in-an-endless-loop-on-certain-network-errors.patch
    cups-1.6.1-ubuntu-fix-another-spot-where-avahi-crashes-cupsd-because-it-does-not-handle-null-values-from-its-own-apis.patch
    cups-1.6.1-ubuntu-ipp-backend-did-not-send-cancel-request-to-printers-when-a-job-was-canceled-and-printer-did-not-support-create-job.patch
    cups-1.6.1-ubuntu-get-ppd-file-for-statically-configured-bonjour-shared-queues.patch
    cups-1.6.1-ubuntu-printers-c-recognize-remote-cups-queue-via-dnssd-uri.patch

- Remove unneeded patches:
    cups-1.6.1-ubuntu-forward-port-cups-1-5-x-cups-browsing.patch
    cups-1.6.1-alt-makefile.patch -> updated in cups-1.6.2-alt-makefile.patch

- Updated patches:
    cups-1.6.0-debian-pidfile.patch
    cups-1.6.1-rh-lspp.patch
    cups-1.6.1-ubuntu-airprint-support.patch
    cups-1.6.1-ubuntu-cupsd-no-crash-on-avahi-threaded-poll-shutdown.patch

* Tue May 21 2013 Alexander Plehanov <tonik@altlinux.org> 1.6.2-alt2
- Added FAQ localization

* Thu May 16 2013 Alexander Plehanov <tonik@altlinux.org> 1.6.2-alt1
- New version 1.6.2

* Tue Feb 12 2013 Alexander Plehanov <tonik@altlinux.org> 1.6.1-alt8
- Fix /locale/cups_ru.po localization

* Tue Feb 12 2013 Alexander Plehanov <tonik@altlinux.org> 1.6.1-alt7
- Fix russian localization

* Tue Jan 22 2013 Alexander Plehanov <tonik@altlinux.org> 1.6.1-alt6
- Edit web-interface locaization

* Fri Jan 18 2013 Alexander Plehanov <tonik@altlinux.org> 1.6.1-alt5
- /locale/cups_ru.po russian localization

* Tue Dec 18 2012 Alexander Plehanov <tonik@altlinux.org> 1.6.1-alt4
- FAQ interface localization

* Tue Nov 06 2012 Alexander Plehanov <tonik@altlinux.org> 1.6.1-alt3
- Edit russian translation

* Tue Oct 30 2012 Anton Farygin <rider@altlinux.ru> 1.6.1-alt2
- Added from ubuntu (closes: #27907):
    cups-1.4-ubuntu-default-error-policy-retry-job.patch
    cups-1.6.1-ubuntu-prevent-crash-due-to-null-host-name-or-fqdn-from-avahi.patch
    cups-1.6.1-ubuntu-fix-crash-on-shutdown-caused-by-broken-avahi-config.patch
    cups-1.6.1-ubuntu-work-around-some-broken-ipp-printers.patch
    cups-1.6.1-ubuntu-ipp-backend-abort-the-outer-loop-if-we-get-a-failure-from-send-document.patch
    cups-1.6.1-ubuntu-ipp-backend-could-get-stuck-in-an-endless-loop-on-certain-network-errors.patch
    cups-1.6.1-ubuntu-airprint-support.patch
    cups-1.6.1-ubuntu-fix-another-spot-where-avahi-crashes-cupsd-because-it-does-not-handle-null-values-from-its-own-apis.patch
    cups-1.6.1-ubuntu-ipp-backend-did-not-send-cancel-request-to-printers-when-a-job-was-canceled-and-printer-did-not-support-create-job.patch
    cups-1.6.1-ubuntu-forward-port-cups-1-5-x-cups-browsing.patch
    cups-1.6.1-ubuntu-cupsd-no-crash-on-avahi-threaded-poll-shutdown.patch
    cups-1.6.1-ubuntu-get-ppd-file-for-statically-configured-bonjour-shared-queues.patch
    cups-1.6.1-ubuntu-printers-c-recognize-remote-cups-queue-via-dnssd-uri.patch

* Wed Sep 19 2012 Anton Farygin <rider@altlinux.ru> 1.6.1-alt1
- 1.6.1
- php-cups subpackage now will be build from cups-filters
- cups now used cups-filters from same package

* Thu Jun 14 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.3-alt1
- 1.5.3
- add tmpfiles.d files for static devices and /var/run/cups stuff

* Wed Apr 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt2
- cups-1.5.2-rh-translation.patch

* Fri Mar 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.2-alt1
- 1.5.2
- build with systemd, avahi

* Tue Dec 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt7
- fix build by removing pdftoopvp filter

* Wed Oct 12 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt6
- trigger to rename /etc/modprobe.d/blacklist-cups -> blacklist-cupsconf
- enable lspp
- make cpdftocps pstopdf filters executable
- add bc to Requires (for pstopdf)

* Wed Oct 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.5.0-alt5
- fix http://www.cups.org/str.php?L3921 (ppds.dat corruption)
- rename blackist-cups to blackist-cups.conf

* Mon Oct 10 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.0-alt4
- add pdf-filters
- add filers cpdftocps pstopdf

* Sat Sep 10 2011 Anton Farygin <rider@altlinux.ru> 1.5.0-alt3
- Rebuild with php5-5.3.8.20110823-alt1

* Thu Sep 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt2
- CVE-2011-2896

* Fri Aug 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Fri Jul 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Fri May 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.6-alt6
- shaba@: add systemd support (ALT #25582)

* Wed May 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.6-alt5
- add /lib/udev/devices/lp*

* Fri Mar 25 2011 Anton Farygin <rider@altlinux.ru> 1.4.6-alt4
- rebuild with new PHP

* Wed Mar 23 2011 Alexey Tourbin <at@altlinux.ru> 1.4.6-alt3
- enabled OpenSSL encryption support
- libcups-devel: removed dependencies on libssl-devel libgnutls-devel
- cups-config: disabled dependency on zlib-devel

* Mon Feb 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.6-alt2
- change permissions for cupsd to 0755 (ALT #25086)

* Mon Jan 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.6-alt1
- 1.4.6

* Mon Nov 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt2
- remove loopback setup script from initscript

* Fri Nov 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Fri Oct 29 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.4-alt3
- CVE-2010-2941

* Fri Sep 17 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.4-alt2
- mike: use ip instead of ifconfig in initscript (closes: #24099)

* Tue Sep 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.4-alt1
- 1.4.4 (closes: #23635)

* Sat Apr 03 2010 Stanislav Ievlev <inger@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sun Mar 07 2010 Stanislav Ievlev <inger@altlinux.org> 1.4.2-alt3
- CVE-2010-0302, CVE-2009-3553

* Wed Dec 16 2009 Stanislav Ievlev <inger@altlinux.org> 1.4.2-alt2
- fix Russian translation

* Thu Nov 12 2009 Stanislav Ievlev <inger@altlinux.org> 1.4.2-alt1
- 1.4.2

* Tue Oct 20 2009 Stanislav Ievlev <inger@altlinux.org> 1.4.1-alt4
- move /usr/share/cups/ppdc from devel package into main (need for sdk based drivers)
- move /usr/share/cups/drv from devel package into main (there is a sample ready to use driver inside)

* Thu Oct 01 2009 Stanislav Ievlev <inger@altlinux.org> 1.4.1-alt3
- fix desktop-file (closes: #21786)
- fix action back links in Russian web interface (closes: #21777) (cas@)

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 1.4.1-alt2
- add blacklist for usblp kernel module (closes: #21737)

* Tue Sep 15 2009 Stanislav Ievlev <inger@altlinux.org> 1.4.1-alt1
- 1.4.1

* Thu Jun 04 2009 Stanislav Ievlev <inger@altlinux.org> 1.3.10-alt2
- fix package deps
- remove obsolete macros

* Fri Apr 17 2009 Stanislav Ievlev <inger@altlinux.org> 1.3.10-alt1
- 1.3.10 (security update)
- add support for PidFile option (closes: #19477)

* Wed Dec 17 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.9-alt2
- CVE-2008-5138, CVE-2008-5286

* Mon Oct 20 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.9-alt1
- 1.3.9

* Thu Jul 24 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.8-alt1
- 1.3.8

* Wed May 14 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.7-alt2
- CVE-2008-1722

* Wed Apr 02 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.7-alt1
- 1.3.7

* Mon Mar 24 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.6-alt2
- libcups-devel: add libgnutls-devel and libssl-devel to requires

* Tue Feb 26 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.6-alt1
- 1.3.6

* Fri Feb 01 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.5-alt2
- add translations (for command line utilities)
- remove unused and insecure pstops-wrapper

* Tue Jan 08 2008 Stanislav Ievlev <inger@altlinux.org> 1.3.5-alt1
- 1.3.5

* Thu Nov 08 2007 Stanislav Ievlev <inger@altlinux.org> 1.3.3-alt4
- CVE-2007-4045
  CVE-2007-4352
  CVE-2007-5392
  CVE-2007-5393

* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 1.3.3-alt3
- remove deps on printer-driver-utils

* Wed Oct 31 2007 Stanislav Ievlev <inger@altlinux.org> 1.3.3-alt2
- CVE-2007-4351

* Mon Oct 01 2007 Stanislav Ievlev <inger@altlinux.org> 1.3.3-alt1
- 1.3.3

* Thu Sep 06 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.12-alt4
- remove ppd subpackage (all extra ppd files are distributed with foomatic-db now)

* Fri Aug 24 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.12-alt3
- Added php5 module build

* Tue Jul 31 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.12-alt2
- CVE-2007-3387

* Tue Jul 17 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.12-alt1
- 1.2.12 (bugfix release)

* Mon May 21 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.11-alt1
- 1.2.11 (bugfix release)
- add desktop menu entry

* Fri Mar 23 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.10-alt1
- 1.2.10 (bugfix release)

* Wed Feb 28 2007 Stanislav Ievlev <inger@altlinux.org> 1.2.8-alt1
- 1.2.8 (bugfix release)
- define default policy

* Wed Nov 15 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.6-alt1
- 1.2.6 (bugfix release)
- force A4 in ppds
- cups drivers in separate package now

* Fri Oct 13 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.4-alt0.2
- cupsServer(), don't save probe results (was problems with samba)

* Fri Oct 13 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.4-alt0.1
- 1.2.4 (bugfix release)

* Wed Sep 13 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.3-alt0.1
- 1.2.3 (bugfix release)

* Mon Jun 19 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.1-alt0.5
- fixed izvrat patch

* Tue Jun 06 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.1-alt0.4
- added missing directories to package
- fixed lpstat output problem (patch from upstream)

* Wed May 31 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.1-alt0.3
- fixed alternatives update

* Tue May 30 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.1-alt0.2
- fixed .rpmsave problem

* Wed May 24 2006 Stanislav Ievlev <inger@altlinux.org> 1.2.1-alt0.1
- 1.2.1

* Thu Jun 30 2005 Anton D. Kachalov <mouse@altlinux.org> 1.1.20-alt14.1
- x86_64 fix

* Tue May 03 2005 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt14
- update backend (new format)
- cups-1.1.20-alt-usb-decode_id.patch

* Thu Apr 21 2005 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt13
- update backend (new format)

* Wed Mar 09 2005 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt12
- update alterator backend

* Mon Feb 14 2005 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt11
- added CUPS backend for alterator

* Fri Jan 28 2005 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt10
- remove duplicate in ppds
- added update-printers-db in post script

* Fri Jan 14 2005 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt9
- added patches for:
	CAN-2004-1268
	CAN-2004-1269
	CAN-2004-1270
	CAN-2005-0064

* Thu Dec 23 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt8
- xpdf security fixes again
- added support for cp866 (#5439)

* Thu Oct 21 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt7
- bump release number for sisyphus

* Tue Oct 19 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt6.1
- sec fix

* Thu Oct 07 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt6
- added additional drivers,filters,ppds

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.20-alt5.3.1
- Rebuilt with libtiff.so.4.

* Fri Sep 03 2004 Dmitry V. Levin <ldv@altlinux.org> 1.1.20-alt5.3
- Applied patch from Alvaro Martinez Echevarria, to fix DoS (CAN-2004-0558).

* Mon Aug 09 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt5.2
- replace testpage with others.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.20-alt5.1
- Rebuilt with openssl-0.9.7d.

* Wed May 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt5
- added full sets of drivers for Epson and OCE PostScript printers

* Wed Mar 17 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt4
- added drivers for EPL 6200 from Epson, PCL driver for this printer removed
- fix texttops to work with this printer.

* Tue Mar 16 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt3
- added default driver for EPSON EPL 6200 (same as ljet4 with PageSize = A4)

* Tue Mar 16 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt2
- enable and start printer by default (need by kde print manager)

* Tue Mar 16 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt1
- increase permissions for the certificates (TODO: possible change perms on certs dir)

* Tue Feb 10 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt0.9
- enable izvrat

* Wed Dec 24 2003 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt0.8
- second Daedalus release
- return all old patches instead of izvrat

* Tue Dec 02 2003 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt0.7
- Daedalus release

* Fri Nov 28 2003 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt0.6
- added locale patch, also patch from ASP
- fix shared library building

* Thu Nov 13 2003 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt0.2
- 1.1.20
- termporary remove -u from startup script
- require esp-ghostscript-cups

* Thu Nov 06 2003 Stanislav Ievlev <inger@altlinux.org> 1.1.20-alt0.1
- 1.1.20rc5
- temporary remove all aditional features
- use external ghostscript with cups device

* Mon Nov 03 2003 Stanislav Ievlev <inger@altlinux.org> 1.1.18-alt8.3
- turn on limits to maximum number of saved jobs
- fix problem with possible infinity loop

* Thu Oct 09 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt8.2
- try to fix web interface

* Mon Sep 29 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt8.1
- Added support for control

* Thu May 22 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt8
- apply bugfix patch
- use new scheme for init-script

* Wed Apr 09 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt7.2
- new alternatives config format

* Mon Mar 31 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt7.1
- ptal backend removed (hpoj maintainer request)

* Wed Mar 26 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt7
- added backend-ptal, backend-pdf
- use %%exclude instead of filelists

* Fri Mar 14 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt6
- PreReq fixes

* Thu Mar 13 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt5
- move to new alternatives scheme

* Wed Jan 29 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt4
- added patch from MDK: fix error message on host lookup failure

* Wed Jan 15 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt3
- fixed izvrat: 3770 -> 2770 on /etc/cups/certs/
- change name on startup
- init-script now only %%config without noreplace

* Tue Jan 14 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt2
- advanced izvrat

* Fri Jan 10 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.18-alt1
- 1.1.18
- removed altification of testprint, now in the printer-testpages

* Thu Dec 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.15-alt8
- added pdf2ps patch

* Mon Dec 16 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.15-alt7
- apply some fixes from idefence

* Wed Dec 04 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.15-alt5
- move serial and ncp backend into subpackage
- added contrib from Yury Konovalov <yurix@unixcenter.ru>

* Wed Oct 16 2002 AEN <aen@altlinux.ru> 1.1.15-alt4
- common Provides added

* Fri Oct 11 2002 AEN <aen@altlinux.ru> 1.1.15-alt3
- locale name fixed (bug #1396)

* Wed Jun 26 2002 AEN <aen@logic.ru> 1.1.15-alt2
- custom mime.convs added
- some pfa's from cups-1.1.14 added in val-fonts

* Mon Jun 17 2002 AEN <aen@logic.ru> 1.1.15-alt1
- new version
- restored pstoraster from 1.1.14
- patches 106, 107 merged upstream

* Thu Apr 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.14-alt3
- Added ALT documentation

* Thu Mar 28 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.14-alt2
- Added loopback setup to startup script.
  cups needs it to work

* Thu Feb 14 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Wed Feb 13 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.13-alt6
- turn off temporary light settings

* Wed Feb 13 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.13-alt5
- izvrat, stage2:
   added -u option,
   admrestart option for initscripts.

* Mon Feb 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.13-alt4
- fix locale support.

* Fri Feb 08 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.13-alt3
- first release of Izvrat patch

* Thu Feb 07 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.13-alt2
- small cleanups

* Wed Feb 06 2002 AEN <aen@logic.ru> 1.1.13-alt1
- patches 102,107,108 removed
- patches 101,103 regenerated

* Thu Dec 06 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.12-alt3
- added root in config, for some cases ...

* Thu Nov 22 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.12-alt2
- aded ncp backend by Sergey Vlasov <vsu@altlinux.ru>
- returned fax4CUPS again. Someone remove it some time ago.

* Fri Nov 16 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.12-alt1
- 1.1.12

* Thu Oct 11 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.10-alt5
- rebuild with new libpng.
- RSBAC patch temporary disabled to rebuild under 2.2 kernel

* Thu Sep 06 2001 AEN <aen@logic.ru> 1.1.10-alt4
- new fonts from Valek

* Mon Sep 03 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.10-alt3
- New solution for admin.cgi - tmpdir
  defined in config by default now.

* Mon Aug 27 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.10-alt2
- Returned Valek's fonts. Now in pfa format (CUPS bug?)

* Fri Aug 17 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.10-alt1
- 1.1.10
- removed setupbroadcusting. It's not secure to have this script.
- temporary removed fonts. Don't work with gimp-print.

* Wed Aug 08 2001 AEN <aen@logic.ru> 1.1.9-alt9
- new default fonts from Valek (frob@df.ru)
- utf fonts description changed

* Fri Aug 03 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.9-alt8
- Corrections of RSBAC support in CUPS.

* Tue Jul 31 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.9-alt7
- Changed default config to add rights for admin.cgi.

* Tue Jul 31 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.9-alt6
- New lphelp utility from Mandrake.

* Thu Jul 26 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.9-alt5
- 1.1.9-1 (bugfix release)

* Wed Jul 25 2001 AEN <aen@logic.ru> 1.1.9-alt4
- RunAsUser temporary removed

* Tue Jul 24 2001 AEN <aen@logic.ru> 1.1.9-alt3
- new encoding patch (hebrew support added)

* Thu Jul 12 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.9-alt2
- Fixed .so links (from hard links to soft)

* Wed Jul 11 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Wed Jun 20 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.8-alt2
- Added RSBAC MAC support.

* Wed Jun 13 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Mon Jun 04 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.7-alt6
- Fix update-alternatives. Force to use gzip for manuals

* Wed May 30 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.7-alt5
- Split package. Backport pstops from 1.1.6

* Tue May 29 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.7-alt4
- Added test page with our logo

* Mon May 28 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.7-alt3
- Remove menu entry for removed cupsWebAdmin Script.

* Fri May 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.1.7-alt2
- Some cleanups. Rebuild for use macros post_service and preun_service.

* Sat Feb 24 2001 AEN <aen@logic.ru>
- 1.1.6, holes fixed (?)

* Mon Jan 08 2001 AEN <aen@logic.ru>
- merged with MDK

* Thu Jan  4 2001 Till Kamppeter <till@mandrakesoft.com> 1.1.5-2mdk

- Bugfix release of CUPS 1.1.5.
- Enhancements in the documentation for setting up encrypted connections.
- Reactivate usage of implicit classes by default.
- Fixed segfault of "lppasswd -a name".

* Wed Jan  3 2001 Till Kamppeter <till@mandrakesoft.com> 1.1.5-1mdk

- Updated to CUPS 1.1.5 (encryption support enabled).
- Added README files of the source tarball to the doc directory.

* Mon Dec 25 2000 AEN <aen@logic.ru>
- pam fixed

* Tue Nov 28 2000 AEN <aen@logic.ru>
- rebuild for RE
- fix for 2.96 build
- big encodings & languages patch

* Mon Nov 27 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.4-8mdk
- Fixed RPM problem of /etc/cups/cupsd.conf.rpmnew sometimes not created.

* Thu Nov 23 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.4-7mdk
- Fixed bug of jobs sent to implicit classes not printing.

* Sat Nov 18 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.4-6mdk
- Fixed bug in the autodetection of the printer devices.

* Wed Nov 15 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.4-5mdk
- Security fix: Automatic configuration of broadcasting and printer access
  restricted to the local network(s) (eth?), printers were accessible from
  all over the internet before, and broadcasting to all networks
  (255.255.255.255) kept dial-on-demand connections permanently up.

* Tue Nov 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.4-4mdk
- Fix gcc2.96 compilation.

* Sat Oct 21 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.4-3mdk
- Security fix: lpstat and web interface displayed the SMB password before

* Tue Oct 17 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.4-2mdk
- Set default Filterlimit to 999999 in /etc/cups/cupsd.conf, the default
  value zero limited to one process instead of allowing unlimited processes.
- Fixed a bug in scaling of HPGL files.

* Sat Oct 14 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.4-1mdk
- New release with all previous bugfixes included and important fixes for
  the GIMP-Print drivers.

* Mon Oct  2 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-13mdk
- Applied patch by Michael Sweet for the test file bug in the IPP backend.

* Sun Oct  1 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-12mdk
- Fixed a bug of the IPP backend which prevented text with accented characters
  being transferred correctly to the printing server.

* Sun Oct  1 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-11mdk
- Cleaned up manufacturer entry in the CUPS PPD files
- Fixed a bug in handling lines with leading spaces in ~/.lpoptions

* Thu Sep 28 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-10mdk
- Menu call for the web interface not fixed to Netscape any more.

* Thu Sep 28 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-9mdk
- New bugfix patch of Michael Sweet for admin.cgi

* Wed Sep 27 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-8mdk
- Fixed bug in admin.cgi by a patch of Michael Sweet, no downdate to 1.1.2
  any more
- Fixed bug with duplex printing in HP LaserJet driver

* Tue Sep 26 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-7mdk
- Fixed bug in IPP backend which prevented options from
  being transferred correctly to a remote printer

* Tue Sep 26 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-6mdk
- Applied new PAM configuration

* Mon Sep 25 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-5mdk
- Program "lphelp" expanded to show also numerical options of CUPS-O-MATIC
  PPD files.

* Sat Sep 23 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-4mdk
- Mandrakized the test page
- Login/password request for command line tools

* Fri Sep 22 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-3mdk
- Revised support of accounts without password. Now XPP, KUPS and QTCUPS
  do not ask for the login/password again and again when one clicks
  "Cancel" in the login dialog.

* Wed Sep 20 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-2mdk
- Fixed bug of adding a printer with the web interface being impossible
- Make CUPS WWW interface and KUPS usable when root has no
  password

* Tue Sep 19 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.3-1mdk
- Corrected "preun" script, so that update-alternatives links do not
  get lost on update of the package.
- Updated to CUPS 1.1.3 which includes all the previous bug fix
  patches and some additional bugfixes.

* Sat Sep 16 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-22mdk
- changed default configuration to generate an /etc/printcap
  file. So non-natively CUPS supporting programs (as KDE)
  find the printers.

* Thu Sep 14 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.2-21mdk
- corrected incoherent-subsys, till sucks
- added reload

* Wed Sep 13 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-20mdk
- Replaced startup script completely to fit to the Mandrake
  standard
- Applied another development snapshot patch of Michael Sweet to fix
  bugs in pstoimage and pstoraster, and the information propafation
  between the CUPS daemons on different machines.

* Sat Sep  9 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-19mdk
- Applied another development snapshot patch of Michael Sweet to fix
  several bugs.

* Fri Sep  8 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-18mdk
- {_datadir}/locale was forgotten in files section, added

* Fri Sep  8 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-17mdk
- Added /usr/sbin/update-alternatives to "Requires:" line
  to surround a bug of version number comparing in RPM

* Thu Sep  7 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-16mdk
- Turned off feature of "Implicit classes", it is broken.
- Introduced "Requires:" line to make sure that "update-
  alternatives" is available.
- Added patch of Michael Sweet to support instances in lpq
  and lprm.

* Thu Sep  7 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-15mdk
- Applied development snapshot patch of Michael Sweet to fix
  several bugs.
- Added automatic daemon restart on update.

* Wed Sep  6 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-14mdk
- Fixed segfaults in poll_ppd_base
- Better description in cups.sh (help text for startup
  services config programs)

* Fri Sep  1 2000 Till Kamppeter <till@mandrakesoft.com> 1.1.2-13mdk
- Fixed bugs in the "files" list of specfile (definition of doc dir)

* Tue Aug 29 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-12mdk
- Added patch adjusting the USB printer autodetection to the current state

* Fri Aug 25 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-11mdk
- Menu entry for CUPS WWW Admin tool added
- Removed compatibility link /etc/init.d/cups to /etc/rc.d/init.d/cups, init
  script simply in %_initdir now.

* Fri Aug 25 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-10mdk
- Fixed compiler options for the additional tools

* Thu Aug 24 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-9mdk
- Made the cups package ready for co-existing with the old lpr printing
  system.

* Mon Aug 21 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-8mdk
- Moved "/usr/lib/libcups*.so" links from devel package to main package
  because the function overloading in XPP and QTCUPS would not work without
  these links.

* Thu Aug 17 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-7mdk
- Added program "lphelp" which lists the printer-specific options defined
  in the PPD file, so that one can make use of it in "lp", "lpr", and
  "lpoptions" commands at the command line.
- Got a bugfix from Michael Sweet to fix an htmltops problem, applied it
- Applied bugfix for HPGL recognition in /etc/cups/mime.types

* Thu Aug 17 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-6mdk
- Added program "poll_ppd_base" to get a list of all PPD files installed with
  manufacturer and model names of the printers (useful for installation/
  configuration scripts)

* Mon Aug 14 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-5mdk
- Added link libcupsimage.so --> libcupsimage.so.2 so thet drivers based
  on the CUPS driver development kit of GIMP Print compile
- Moved links "*.so" --> "*.so.2" to the development package (rpmlint
  recommends this)

* Wed Aug  9 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-4mdk
- Replaced "chown" in "%%post" by "%%attr" in file list
- Now GhostScript 5.50 is not more required by this package but by cups-drivers
- Compatibility link /etc/rc.d/init.d/cups, if /etc/rc.d/init.d/ exists

* Tue Aug  8 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-3mdk
- Let the PPDs delivered with CUPS be installed, too

* Tue Aug  8 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-2mdk
- Moved init script to from /etc/rc.d/init.d/ to /etc/init.d
- Now GhostScript 5.50 is required
- Patched chkconfig entry in /etc/init.d/cups to 2345 60 60 (as lpd)

* Tue Aug  8 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 1.1.2-1mdk
- Excluded static CUPS library to allow overloading of CUPS functions
- Patched CUPS daemon config to use Web interface for administration
- pstoraster not removed to have the flexibility to also use CUPS drivers
- Updated to version 1.1.2 with bugfix patch for the Makefile

* Tue Jul  4 2000 FranГois Pons <fpons@mandrakesoft.com> 1.1-0.b5.1mdk
- removed pstoraster from installation as drivers are in cups-drivers.
- initial release.

