%define _unpackaged_files_terminate_build 1

Name: phpldapadmin
Version: 1.2.5
Release: alt1

Summary: Handle the adminstration of LDAP server over the web
Summary(ru_RU.UTF8): Управление LDAP сервером через web
License: GPL-2
Group: Networking/WWW

Url: http://phpldapadmin.sourceforge.net
Source: %name-%version.tar.gz
Patch0: %name-convert_to_ascii.patch

Requires: apache2-mod_php7 php7-ldap

BuildArch: noarch

BuildPreReq:rpm-build-apache2

%define pla_home %_datadir/%name

%description
%name -  is a web-based LDAP client. It provides easy, anywhere-accessible,
multi-language administration for your LDAP server. Its hierarchical tree-viewer
and advanced search functionality make it intuitive to browse and administer
your LDAP directory. Since it is a web application, this LDAP browser works on
many platforms, making your LDAP server easily manageable from any location.
%name - is the perfect LDAP browser for the LDAP professional and novice alike.
Its user base consists mostly of LDAP administration professionals.

%description -l ru_RU.UTF8
%name - доступный через сеть клиент LDAP. Он предоставляет простую, доступную,
многоязычную среду для администрирования вашего сервера LDAP. Его иерархическое
дерево просмотра и функциональные возможности ускоренного поиска делают его
интуитивно понятным, чтобы просматривать и управлять вашим каталогом LDAP.
%name - совершенный браузер LDAP для профессионала LDAP и новичков.
Его пользователи состоят главным образом из профессионалов в администрировании LDAP.

После установки откорректируйте config.php согласно вашим настройкам.

%prep
%setup -q -n %name-%version
cp config/config.php.example config/config.php

%build

%install
install -d -m755 %buildroot%pla_home
cp -a * %buildroot%pla_home


pushd %buildroot%pla_home
find . -type f -executable | xargs chmod -x
rm -r doc/ config/config.php.example
rm -r tools/
popd

install -d -m755 %buildroot%_sysconfdir/%name

mv %buildroot%pla_home/config/* \
        %buildroot%_sysconfdir/%name
rmdir %buildroot%pla_home/config
ln -s %_sysconfdir/%name \
        %buildroot%pla_home/config
cat <<EOF >%name.conf
Alias /%name "%pla_home"

<Directory %pla_home>
    DirectoryIndex index.php
    AllowOverride None
    Options FollowSymlinks
    Require local
</Directory>

EOF

install -d %buildroot%apache2_sites_available
install -m644  %name.conf %buildroot%apache2_sites_available

%files
%config %dir %_sysconfdir/%name
%attr(640,root,%apache2_user) %config(noreplace) %_sysconfdir/%name/config.php
%config(noreplace) %apache2_sites_available/%name.conf
%pla_home
%doc INSTALL.md README.md LICENSE

%changelog
* Tue May 19 2020 Nikita Obukhov <nickf@altlinux.org> 1.2.5-alt1
- Update to 1.2.5

* Sat Sep 24 2011 Alexey Tourbin <at@altlinux.ru> 1.1.0.6-alt2
- removed set_strip_method macro

* Sat Jan 10 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0.6-alt1
- Update to 1.1.0.6
- Update SOURCE1 from http://launchpadlibrarian.net
- Add patch for fix convert to ascii #18450 (thanks erthad@)

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0.5-alt2
- Add SOURCE1 for fix #18022
- Convert spec to UTF8

* Tue Feb 19 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0.5-alt1
- Update to 1.1.0.5
- Change requires from php to php5

* Mon Jan 16 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.8-alt0
- Update to 0.9.8

* Fri Nov 25 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.7.2-alt0
- Update to 0.9.7.2

* Tue Oct 25 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.7.1-alt1
- Update to 0.9.7.1-rc3

* Fri Jun 03 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.6c-alt1
- 0.9.6c
- Some spec cleanup
- Added Russian summary & description

* Fri Jan 23 2004 Michael Shigorin <mike@altlinux.ru> 0.9.3-alt1
- built for ALT Linux
