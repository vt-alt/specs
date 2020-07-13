Name: prosody
Version: 0.11.5
Release: alt2

Summary: Modern XMPP communication server

Group: System/Servers
License: MIT
Url: https://prosody.im/

BuildRequires: openssl lua5 liblua5-devel libidn-devel libssl-devel

Requires: openssl lua-module-luaexpat lua-module-luasocket lua-module-luafilesystem lua-module-luasec

Source0: %name-%version.tar
Source1: prosody.cfg.lua
Source2: prosody.service
Source3: prosody.init
Source4: prosody.tmpfiles
Source10: autobuild.watch

Patch1: prosody-0.11.5-alt-user.patch

%description
%summary

%prep
%setup
%autopatch -p2

%build
./configure --prefix=/usr
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%systemd_unitdir
mkdir -p %buildroot/%_localstatedir/prosody
mv %buildroot/%_sysconfdir/prosody/prosody.cfg.lua %buildroot/%_sysconfdir/prosody/prosody.cfg.example.lua
cp %SOURCE1 %buildroot/%_sysconfdir/prosody
cp %SOURCE2 %buildroot/%systemd_unitdir
install -Dpm755 %SOURCE3 %buildroot/%_initdir/prosody
install -Dpm644 %SOURCE4 %buildroot/%_tmpfilesdir/prosody.conf

%pre
/usr/sbin/groupadd -r -f _prosody
/usr/sbin/useradd -r -g _prosody -d %_localstatedir/%name -s /sbin/nologin -n -c "%summary" _prosody >/dev/null 2>&1 ||:

%preun
%preun_service prosody

%post
%post_service prosody

%files
%_bindir/*
%_libexecdir/prosody
%config(noreplace) %_sysconfdir/prosody
%systemd_unitdir/prosody.service
%_initdir/prosody
%attr(0755,_prosody,_prosody) %dir %_localstatedir/prosody
%_tmpfilesdir/prosody.conf
%_man1dir/*

%changelog
* Fri May 15 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.11.5-alt2
- Fixed default user and group for ch[ug]id: use _prosody as these system
  user and group were created by package installation.
- Added tmpfiles config.
- prosody.service: Added reload action.
- Added SYSV init file.
- spec: Fixed license field.

* Thu Mar 26 2020 Grigory Ustinov <grenka@altlinux.org> 0.11.5-alt1
- Automatically updated to 0.11.5.

* Wed Feb 05 2020 Grigory Ustinov <grenka@altlinux.org> 0.11.4-alt1
- new version 0.11.4
- add watch file

* Mon Oct 14 2019 Grigory Ustinov <grenka@altlinux.org> 0.11.3-alt1
- Build new version.

* Fri Jan 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.11.2-alt1
- Build new version.

* Fri Dec 14 2018 Grigory Ustinov <grenka@altlinux.org> 0.11.1-alt1
- Build new version (Closes: #33835).

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.10-alt3.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Aug 31 2017 Eugene Prokopiev <enp@altlinux.ru> 0.9.10-alt3
- rebuild with lua5.3 fir sisyphus

* Sat Nov 05 2016 Eugene Prokopiev <enp@altlinux.ru> 0.9.10-alt2
- remove lua-posix dependency

* Tue Nov 01 2016 Eugene Prokopiev <enp@altlinux.ru> 0.9.10-alt1
- new version
- add unit and minimal config

* Tue Jul 05 2016 Eugene Prokopiev <enp@altlinux.ru> 0.9.8-alt1
- inital build

