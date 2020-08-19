Name: riot-desktop
Version: 1.7.2
Release: alt1

Summary: A glossy Matrix collaboration client

License: Apache 2.0
Url: https://riot.im/desktop.html
Group: Networking/Instant messaging

BuildArch: noarch

# Source-url: https://github.com/vector-im/riot-desktop/archive/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from etersoft-build-utils
# ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar

Source3: riot-desktop.desktop

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
#AutoProv: no

ExclusiveArch: x86_64 i586 aarch64

BuildRequires: npm node-asar
# https://github.com/yarnpkg/yarn/issues/7251
BuildRequires: /proc yarn

BuildRequires: riot-web = %version

Requires: electron9 >= 9.0.5
Provides: element-desktop = %version-%release

%description
Riot (formerly known as Vector) is a Matrix web client built using the Matrix React SDK.

%prep
%setup -a1
cp -a /var/www/html/riot-web webapp

%build
# note: configure it
cat element.io/release/config.json | grep -v "update_base_url" > webapp/config.json
# TODO: support hak and build matrix-seshat
#yarn run hak

#npm run build
#yarn build
#yarn dist
#npm ERR! cb() never called!
#npm ERR! This is an error with npm itself. Please report this error at:
rm -vf node_modules/.bin/{npm,npx}
npm prune --production

asar pack . resources/app.asar

cat <<EOF >%name
#!/bin/sh
electron9 %_datadir/%name/resources/app.asar "\$@"
EOF

%install
install -m755 -D %name %buildroot%_bindir/%name
ln -s riot-desktop %buildroot/%_bindir/riot
ln -s riot-desktop %buildroot/%_bindir/element-desktop

mkdir -p %buildroot%_datadir/%name/
cp -a resources %buildroot%_datadir/%name/

for i in 16 22 24 32 48 64 128 256 512 ; do
    F=build/icons/${i}x${i}.png
    [ -s "$F" ] || continue
    T=%buildroot%_iconsdir/hicolor/${i}x${i}/apps/
    mkdir -p $T/
    cp $F $T/%name.png
done

install -D -m644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/riot
%_bindir/riot-desktop
%_bindir/element-desktop
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Wed Aug 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script) (ALT bug 38786)

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
- new version (1.6.2) with rpmgs script

* Fri Apr 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.15-alt1
- new version 1.5.15 (with rpmrb script)

* Wed Oct 16 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Wed Sep 04 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)

* Thu Jun 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Sun Mar 10 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- build new version from sources

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- initial release for ALT Sisyphus
