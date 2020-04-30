Name: onedrive
Version: 2.4.0
Release: alt1

Summary: OneDrive Free Client written in D

License: GPLv3
Group: File tools
Url: https://github.com/abraunegg/onedrive

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/abraunegg/onedrive/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-dmd
BuildRequires: rpm-build-intro

BuildRequires: dmd >= 2.083.1

BuildRequires: libcurl-devel
BuildRequires: libnotify-devel
BuildRequires: libsqlite3-devel >= 3.7.15
# for pkg-config --variable=systemdsystemunitdir systemd
BuildRequires: libsystemd-devel

BuildRequires: udev-rules
#Requires(preun): udev-rules

ExclusiveArch: %dmd_arches

%description
Free CLI client for Microsoft OneDrive written in D.

%prep
%setup
# sed -i 's|version ||g' Makefile
# sed -i '/chown/d' Makefile.in
%__subst 's/-o root -g users//g' Makefile.in
%__subst 's/-o root -g root//g' Makefile.in
# sed -i '/git/d' Makefile
%__subst "s|std\.c\.|core\.stdc\.|" src/sqlite.d
echo %version > version

%build
%configure
export DFLAGS="%dmd_optflags"
export PREFIX="%prefix"
%make_build

%install
%makeinstall_std
chmod a-x %buildroot/%_man1dir/%{name}*

#%preun
#systemd_user_preun %name.service
#systemd_preun %name@.service

%files
%doc README.md LICENSE CHANGELOG.md
%_bindir/%name
%_userunitdir/%name.service
%_unitdir/%name@.service
%_man1dir/%name.1.*
%_docdir/%name
%config %_logrotatedir/onedrive

%changelog
* Tue Mar 24 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version 2.4.0 (with rpmrb script)

* Tue Mar 24 2020 Vitaly Lipatov <lav@altlinux.ru> 2.3.12-alt1
- initial build for ALT Sisyphus

* Mon Feb 10 2020 Kalev Lember <klember@redhat.com> - 2.3.12-3
- Rebuilt for ldc 1.20

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Thomas Drake-Brockman <thom@sfedb.com> - 2.3.12-1
- Update to 2.3.12

* Wed Oct 02 2019 Zamir SUN <sztsian@gmail.com> - 2.3.10-1
- Update to 2.3.10

* Mon Aug 19 2019 David Va <davidva@tuta.io> - 2.3.8-1
- Update to 2.3.8 for bug fixes

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 06 2019 Thomas Drake-Brockman <thom@sfedb.com> - 2.3.7-1
- Update to 2.3.7 for bug fixes

* Thu Jun 20 2019 Zamir SUN <zsun@fedoraproject.org> - 2.3.5-1
- Update to 2.3.5 to apply some more fixes

* Sat Jun 15 2019 Zamir SUN <zsun@fedoraproject.org> - 2.3.4-1
- Update to 2.3.4 for bug fixes

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 2.3.2-2
- Rebuilt for ldc 1.15

* Wed Apr 03 2019 Zamir SUN <zsun@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2 to bring in bugfixes.
- Resolves: 1695392

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.2.1-5
- Remove obsolete requirement for %%post scriptlet

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 2.2.1-4
- Rebuilt for ldc 1.14

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 04 2018 Zamir SUN <sztsian@gmail.com> - 2.2.1-2
- Add the source tarball

* Tue Dec 04 2018 Zamir SUN <sztsian@gmail.com> - 2.2.1-1
- Update to 2.2.1

* Fri Nov 30 2018 Zamir SUN <sztsian@gmail.com> - 2.2.0-1
- Switch upstream to more active fork in https://github.com/abraunegg/onedrive
- Update to 2.2.0

* Sun Oct 14 2018 Kalev Lember <klember@redhat.com> - 1.1.1-6
- Rebuilt for ldc 1.12

* Sun Aug 05 2018 Thomas Drake-Brockman <thom@sfedb.com> - 1.1.1-5
- Patch src/sqlite.d to use core.stc instead of std.c

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Kalev Lember <klember@redhat.com> - 1.1.1-3
- Rebuilt for ldc 1.11

* Fri Feb 23 2018 Thomas Drake-Brockman <thom@sfedb.com> - 1.1.1-2
- Bump release for rebuild on f28 branch

* Tue Feb 20 2018 Thomas Drake-Brockman <thom@sfedb.com> - 1.1.1-1
- Update to upstream version 1.1.1
- Remove %check because upstream removed the unittest action from Makefile

* Mon Feb 19 2018 Kalev Lember <klember@redhat.com> - 1.0.1-3
- Rebuilt for ldc 1.8

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Zamir SUN <sztsian@gmail.com> 1.0.1-1
- Update to upstream release version 1.0.1

* Tue Oct 25 2016 mosquito <sensor.wen@gmail.com> 0.1.1-2.giteb8d0fe
- add BReq systemd

* Thu Oct 20 2016 Zamir SUN <sztsian@gmail.com> 0.1.1-1.giteb8d0fe
- initial package
