# TODO: build for sources like in Fedora

%define geckodir %_datadir/wine/gecko

Name: wine-gecko
Version: 2.47.1
Release: alt1

Summary: Custom version of Mozilla's Gecko Layout Engine for Wine

License: MPL
Group: Office
Url: http://wiki.winehq.org/Gecko

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source1-url: http://dl.winehq.org/wine/wine-gecko/%version/wine-gecko-%version-x86.tar.bz2
Source1: %name-x86-%version.tar
# Source2-url: http://dl.winehq.org/wine/wine-gecko/%version/wine-gecko-%version-x86_64.tar.bz2
Source2: %name-x86_64-%version.tar

# TODO: it is impossible build arch packages with files in noarch
BuildArch: noarch
#ExclusiveArch: %{ix86} x86_64

AutoReq:no
AutoProv:no

%description
Wine implements its own version of Internet Explorer. The implementation
is based on a custom version of Mozilla's Gecko Layout Engine.
When your application tries to display a web page, it loads Wine's
custom Gecko from the dir /usr/share/wine/gecko/wine-gecko-%version-ARCH_STRING.

%prep
tar xfv %SOURCE1
tar xfv %SOURCE2

%install
mkdir -p %buildroot%geckodir/
cp -a $(basename %SOURCE1 .tar) %buildroot%geckodir/wine-gecko-%version-x86/
cp -a $(basename %SOURCE2 .tar) %buildroot%geckodir/wine-gecko-%version-x86_64/

%files
%dir %_datadir/wine/
%dir %geckodir/
%geckodir/wine-gecko-%version-x86/
%geckodir/wine-gecko-%version-x86_64/

%changelog
* Sun Jan 19 2020 Vitaly Lipatov <lav@altlinux.ru> 2.47.1-alt1
- new version 2.47.1
- unpack to global wine location (supported since wine 5.0)

* Sun Mar 24 2019 Vitaly Lipatov <lav@altlinux.ru> 2.47-alt2
- pack wine_gecko x86_64 too

* Thu Aug 18 2016 Vitaly Lipatov <lav@altlinux.ru> 2.47-alt1
- new version 2.47 (use with wine since 1.9.13)

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.44-alt1
- new version 2.44 (use with wine since 1.9.3)

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 2.40-alt1
- new version 2.40 (use with wine since 1.7.50)

* Mon Mar 09 2015 Vitaly Lipatov <lav@altlinux.ru> 2.36-alt1
- new version 2.36 (use with wine since 1.7.38)

* Fri Dec 12 2014 Vitaly Lipatov <lav@altlinux.ru> 2.34-alt1
- new version 2.34 (use with wine since 1.7.31)

* Mon Oct 14 2013 Vitaly Lipatov <lav@altlinux.ru> 2.24-alt1
- new version 2.24 (use with wine since 1.7.3)

* Sat Jun 22 2013 Vitaly Lipatov <lav@altlinux.ru> 2.21-alt1
- new version 2.21

* Wed Feb 06 2013 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- new version (1.9) with rpmgs script
- set noarch and pack only wine_gecko-*-x86

* Sat Dec 22 2012 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- update wine_gecko to 1.8 (use with wine 1.5.15 or later)

* Wed Aug 01 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new version 1.7 (use with wine 1.5.10 or later)

* Sun Jul 15 2012 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- new version 1.6 (use with wine 1.5.7 or later)

* Mon May 28 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (use with wine 1.5.0 or later)

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- new version 1.4 (use with wine 1.3.33 or later)

* Fri Aug 26 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- new version 1.3 (use with wine 1.3.26 and later)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (use with wine 1.3.16 and later)

* Wed Dec 22 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0

* Sun Dec 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

