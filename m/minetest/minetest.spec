%def_without l10n
%define _hardened_build 1
%global gitname celeron55

Name:		minetest
Version:	5.2.0
Release:	alt1
Summary:	Multiplayer infinite-world block sandbox with survival mode

Group:		Games/Other
License:	LGPLv2+ and CC-BY-SA
URL:		http://minetest.net/index.php

# VCS (executable): https://github.com/minetest/minetest.git
# VCS (data files): https://github.com/minetest/minetest_game.git


# curl -L -O http://github.com/celeron55/minetest/tarball/0.4.3/minetest-0.4.3.tar.gz
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.desktop
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.service
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.rsyslog
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.logrotate
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.README

Source0:	%name-%version.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.service
Source3:	%{name}.rsyslog
Source4:	%{name}.logrotate
Source5:	%{name}.README
Source6:	%{name}_game-%version.tar.gz
Source7:	http://www.gnu.org/licenses/lgpl-2.1.txt

BuildRequires:	cmake >= 2.6.0
BuildRequires:	gcc-c++
BuildRequires:	libirrlicht-devel
BuildRequires:	bzip2-devel jthread-devel libsqlite3-devel
BuildRequires:	libpng-devel libjpeg-devel libXxf86vm-devel libGL-devel
BuildRequires:	libopenal-devel libvorbis-devel
BuildRequires:	libfreetype-devel
BuildRequires:	systemd
BuildRequires:	gettext-tools

Requires:	%name-server = %version-%release
Requires:	icon-theme-hicolor

%description 
Game of mining, crafting and building in the infinite world of cubic
blocks with optional hostile creatures, features both single and the
network multiplayer mode.

%package	server
Summary:	Minetest multiplayer server
Group:		Games/Other

Requires(pre):		shadow-utils

%description	server
Minetest multiplayer server. This package does not require X Window
System.

%prep
%setup -q -n %gitname-%name

pushd games
tar xf %SOURCE6
mv %gitname-%{name}_game %{name}_game
popd

cp %SOURCE7 doc/

%build
%cmake_insource \
%if_with l10n
	-DENABLE_GETTEXT=TRUE \
%endif
	-DJTHREAD_INCLUDE_DIR=%_builddir/%gitname-%name/src/jthread 
%make_build

%install
%makeinstall_std 

# Add desktop file
install -D -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Systemd unit file
mkdir -p %buildroot%_unitdir
cp -p %SOURCE2 %buildroot%_unitdir

# /etc/rsyslog.d/minetest.conf
mkdir -p %buildroot%_sysconfdir/rsyslog.d
cp -p %SOURCE3 %buildroot%_sysconfdir/rsyslog.d/%{name}.conf

# /etc/logrotate.d/minetest
mkdir -p %buildroot/%{_sysconfdir}/logrotate.d
cp -p %SOURCE4 %buildroot/%{_sysconfdir}/logrotate.d/%{name}-server

# /var/lib/minetest directory for server data files
mkdir -p %buildroot%{_sharedstatedir}/%{name} 

# /etc/minetest.conf
mkdir -p %buildroot%{_sysconfdir}
cp -p minetest.conf.example %buildroot%{_sysconfdir}/%{name}.conf

cp -p %SOURCE5 README

%if_with l10n
%find_lang %name
%else
touch %name.lang
%endif

%pre server
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d /var/lib/%{name} -s /sbin/nologin \
    -c "Minetest multiplayer server" %{name}
exit 0

%post server
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun server
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{name}.service > /dev/null 2>&1 || :
    /bin/systemctl stop %{name}.service > /dev/null 2>&1 || :
fi

%postun server
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%files -f %{name}.lang
%doc README.md doc/lgpl-2.1.txt README
%doc %_docdir/%name
%_bindir/%name
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/128x128/apps/%name.png
%_man6dir/minetest.*
%_datadir/metainfo/*.appdata.xml

%files server
%doc README.md doc/lgpl-2.1.txt doc/world_format.txt doc/protocol.txt README
#_bindir/%{name}server
%_unitdir/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%config(noreplace) %{_sysconfdir}/rsyslog.d/%{name}.conf
%attr(0755,minetest,minetest) %dir %{_sharedstatedir}/%{name}
%_man6dir/minetestserver.6*

%changelog
* Thu Apr 09 2020 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Tue Jan 28 2020 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Thu Apr 18 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.17.1-alt1
- New version.

* Mon Jun 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.16-alt1
- New version

* Fri Dec 30 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.15-alt1
- New version

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.14-alt1.1
- rebuild with irrlicht

* Mon Jun 06 2016 Andrey Cherepanov <cas@altlinux.org> 0.4.14-alt1
- New version

* Sun Aug 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.4.13-alt1
- New version
- minetestserver is absent. Use minetest --server

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 0.4.12-alt1
- New version

* Mon Dec 29 2014 Andrey Cherepanov <cas@altlinux.org> 0.4.11-alt1
- New version

* Tue Jul 08 2014 Andrey Cherepanov <cas@altlinux.org> 0.4.10-alt1
- New version
- Add appdata to package
- Support localization disabled by default

* Sun Jan 05 2014 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- New version

* Wed Nov 27 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt1
- New version

* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- Initial build in Sisyphus (thanks Fedora maintainers)

