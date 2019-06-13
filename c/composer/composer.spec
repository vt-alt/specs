# To update package, grub new sources
#
#   gear-remotes-restore
#   git fetch upstream
#   git merge upstream/1.7
#
# and create new vendor cache for new composer version
# 
#   cd .gear
#   ./get_vendor_cache.sh
#
# OR JUST run $ rpmrb NEWVERSION instead of all above

Name: composer
Version: 1.8.5
Release: alt1

Summary: Composer helps you declare, manage and install dependencies of PHP projects, ensuring you have the right stack everywhere

License: %mit
Group: System/Configuration/Packaging
Url: https://getcomposer.org/

# Source-git: https://github.com/composer/composer
Source: %name-%version.tar

Packager: Danil Mikhailov <danil@altlinux.org>

Requires: /usr/bin/php

BuildRequires(pre): rpm-build-licenses

BuildRequires: git-core php7-openssl php7

BuildArch: noarch

%description
Composer helps you declare, manage and install dependencies of PHP projects,
ensuring you have the right stack everywhere.

%prep
%setup

%build

#Move vendor cache with build requires
mv .gear/vendor/ vendor/

#Compile need git log -n1 --pretty=ct HEAD #TODO remove it
git init
git config user.email "you@example.com"
git config user.name "Your Name"
git add bin/compile
git commit -am "Fix for compile"

#build composer.phar
php -d phar.readonly=off -d date.timezone='Europe/Moscow' bin/compile

%install
mkdir -p %buildroot/%_datadir/
cp composer.phar %buildroot/%_datadir/

mkdir -p %buildroot/%_bindir/
install -m 0755 .gear/composer.sh  %buildroot/%_bindir/%name

mkdir -p %buildroot/%_sysconfdir/sysconfig
install -m 0644 .gear/composer.sysconfig %buildroot%_sysconfdir/sysconfig/%name

%files
%doc .gear/README.ALT

%attr(755,root,root) %_bindir/%name
%attr(755,root,root) %_datadir/%name.phar
%config(noreplace)  %_sysconfdir/sysconfig/%name

%changelog
* Fri Jun 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- new version 1.8.5 (with rpmrb script)
- improve autoupdate with rpmrb NEWVERSION

* Fri Aug 17 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.7.2-alt1
- new version
- configurable memory_limit PHP setting (Closes: 33520)
- remove PHP7 requirements - composer can be used with PHP5 too

* Fri May 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6.5-alt1
- build new version
- switch to php7

* Tue Jan 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- build new version

* Tue Oct 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- build new version

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- build new version

* Mon Mar 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- build new version

* Sat Jul 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- build new version 1.1.3
- set memory_limit 256M

* Wed Nov 25 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt4
- Added php5 req

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt3
- Remove install section, added vendor cache

* Fri May 29 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt2
- Change libdir to datadir, add commets

* Thu May 28 2015 Danil Mikhailov <danil@altlinux.org> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
