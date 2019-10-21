Name: riot-desktop
Version: 1.4.2
Release: alt1

Summary: A glossy Matrix collaboration client

License: Apache 2.0
Url: https://riot.im/desktop.html
Group: Networking/Instant messaging

BuildArch: noarch

# Source-url: https://github.com/vector-im/riot-web/archive/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from etersoft-build-utils
# ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar
Source4: %name-production-%version.tar

Source2: %name-app-node_modules-%version.tar

Source3: riot-desktop.desktop

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
#AutoProv: no

ExclusiveArch: x86_64 i586 aarch64

BuildRequires: npm node-asar
# https://github.com/yarnpkg/yarn/issues/7251
BuildRequires: /proc yarn

%description
Riot (formerly known as Vector) is a Matrix web client built using the Matrix React SDK.

%prep
%setup -a1 -a2 -a4
rm -f scripts/check-i18n.pl

%build
# note: configure it
cat electron_app/riot.im/config.json | grep -v "update_base_url" > config.json
npm run build
#npm prune --production
#npm ERR! cb() never called!
#npm ERR! This is an error with npm itself. Please report this error at:
rm -rf node_modules/ && mv production/node_modules ./
asar pack . resources/app.asar

cat <<EOF >%name
#!/bin/sh
electron %_datadir/%name/resources/app.asar "\$@"
EOF

%install
install -m755 -D %name %buildroot%_bindir/%name
ln -s riot-desktop %buildroot/%_bindir/riot

mkdir -p %buildroot%_datadir/%name/
cp -a resources %buildroot%_datadir/%name/

for i in 16 22 24 32 48 64 128 256 512 ; do
    F=electron_app/build/icons/${i}x${i}.png
    [ -s "$F" ] || continue
    T=%buildroot%_iconsdir/hicolor/${i}x${i}/apps/
    mkdir -p $T/
    cp $F $T/%name.png
done

install -D -m644 %SOURCE3 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/riot
%_bindir/riot-desktop
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
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
