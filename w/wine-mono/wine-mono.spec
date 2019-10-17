%define winemonodir %_datadir/wine/mono

Name: wine-mono
Version: 4.9.3
Release: alt1

Summary: Windows build of Mono to run .NET applications via Wine

License: MPL
Group: Office
Url: http://wiki.winehq.org/Mono

Packager: Vitaly Lipatov <lav@altlinux.ru>

# TODO: unpack automatically
# Source-url: http://dl.winehq.org/wine/wine-mono/%version/wine-mono-%version.msi
Source: wine-mono.msi

BuildArch: noarch

%description
Mono is an open-source and cross-platform implementation of the .NET
Framework. Wine can use a Windows build of Mono to run .NET applications.
For Wine releases 1.5.3 and later, the Wine Mono package is recommended.

%install
install -D -m 644 %SOURCE0 %buildroot%winemonodir/%name-%version.msi

%files
%dir %_datadir/wine/
%dir %winemonodir/
%winemonodir/%name-%version.msi

%changelog
* Sat Sep 28 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9.3-alt1
- new version 4.9.3 (with rpmrb script)

* Sat Jun 22 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9.0-alt1
- new version 4.9.0 (with rpmrb script)

* Sun May 26 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8.3-alt1
- new version 4.8.3 (with rpmrb script)

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8.1-alt1
- new version 4.8.1 (with rpmrb script)

* Tue Mar 05 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8.0-alt1
- new version 4.8.0 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 4.7.5-alt1
- new version 4.7.5 (with rpmrb script)

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 4.7.3-alt1
- new version (4.7.3) with rpmgs script

* Fri Aug 04 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.1-alt1
- new version 4.7.1

* Sat Mar 18 2017 Vitaly Lipatov <lav@altlinux.ru> 4.7.0-alt1
- new version (4.7.0) (ALT bug #33252)

* Tue Jan 31 2017 Vitaly Lipatov <lav@altlinux.ru> 4.6.4-alt1
- new version (4.6.4) (ALT bug #33065)

* Thu Jun 16 2016 Vitaly Lipatov <lav@altlinux.ru> 4.6.3-alt1
- new version (4.6.3) with rpmgs script

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 4.6.2-alt1
- update to 4.6.2

* Mon Mar 09 2015 Vitaly Lipatov <lav@altlinux.ru> 4.5.6-alt1
- update to 4.5.6

* Fri Dec 12 2014 Vitaly Lipatov <lav@altlinux.ru> 4.5.4-alt1
- update to 4.5.4

* Thu Sep 25 2014 Vitaly Lipatov <lav@altlinux.ru> 4.5.2-alt1
- update to 4.5.2

* Sat Dec 22 2012 Vitaly Lipatov <lav@altlinux.ru> 0.0.8-alt1
- update to 0.0.8

* Sat Jul 14 2012 Vitaly Lipatov <lav@altlinux.ru> 0.0.4-alt1
- initial build for ALT Linux Sisyphus (0.0.4 use since wine 1.5.6)

