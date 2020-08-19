Name: riot-web
Version: 1.7.2
Release: alt1

Summary: A glossy Matrix collaboration client

License: Apache 2.0
Url: https://riot.im
Group: Networking/Instant messaging

BuildArch: noarch

# Source-url: https://github.com/vector-im/riot-web/archive/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from etersoft-build-utils
# ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
#AutoProv: no

BuildRequires: npm
# https://github.com/yarnpkg/yarn/issues/7251
BuildRequires: /proc yarn

%description
Riot (formerly known as Vector) is a Matrix web client built using the Matrix React SDK.

%prep
%setup -a1
rm -f scripts/check-i18n.pl

%build
yarn build

%install
mkdir -p %buildroot/var/www/html/
cp -a webapp %buildroot/var/www/html/%name/

%files
%doc README.md
/var/www/html/%name/

%changelog
* Wed Aug 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script)

* Sat Jul 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.8-alt1
- new version 1.6.8 (with rpmrb script)

* Tue Jun 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.7-alt1
- new version 1.6.7 (with rpmrb script)

* Tue Jun 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt1
- new version 1.6.6 (with rpmrb script)

* Sat Jun 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.4-alt1
- new version 1.6.4 (with rpmrb script)

* Thu Jun 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt1
- new version 1.6.3 (with rpmrb script)

* Fri May 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- initial release for ALT Sisyphus
