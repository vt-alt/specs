Name:           jitsi-meet
Version:        4109
Release:        alt0.2

Summary:        Jitsi Meet - WebRTC JavaScript video conferences
#Group:          Networking/Instant messaging
Group:          System/Servers
License:        Apache-2.0
URL:            http://www.jitsi.org

BuildArch:      noarch

# Source0-url:  https://github.com/jitsi/jitsi-meet/archive/%version.tar.gz
Source0:        %name-%version.tar
Source1:        %name-development-%version.tar

#BuildRequires(pre): rpm-macros-nodejs
#BuildRequires:  rpm-build-nodejs
BuildRequires(pre): rpm-build-intro >= 1.9.18
BuildRequires:  npm node-devel

BuildRequires: node-sass >= 4.13.1
BuildRequires: node-webpack-cli
# >= 4.27.1

# requires of the meta package
#Requires: jicofo = 1.0
Requires: jitsi-meet-web = %EVR
#Requires: jitsi-meet-web-config = %EVR
#Requires: jitsi-meet-prosody = %EVR

%description
Jitsi Meet is a WebRTC JavaScript application that uses Jitsi
Videobridge to provide high quality, scalable video conferences.

%package -n jitsi-meet-doc
Summary: Inline documentation for various components of Jitsi Meet
Group: Documentation

%description -n jitsi-meet-doc
Jitsi Meet is a WebRTC JavaScript application that uses Jitsi
Videobridge to provide high quality, scalable video conferences.

This package includes upstream documentation and various configuration examples
for most Jitsi Meet components from the source code repository.

%package -n jitsi-meet-web
Summary: WebRTC JavaScript video conferences
#Group:          Networking/Instant messaging
Group:          System/Servers

%description -n jitsi-meet-web
Jitsi Meet is a WebRTC JavaScript application that uses Jitsi
Videobridge to provide high quality, scalable video conferences.

It is a web interface to Jitsi Videobridge for audio and video
forwarding and relaying.

%package -n jitsi-meet-web-config
Summary: Configuration for web serving of Jitsi Meet
Group: System/Servers
#Requires: openssl nginx | nginx-full | nginx-extras | apache2

%description -n jitsi-meet-web-config
Jitsi Meet is a WebRTC JavaScript application that uses Jitsi
Videobridge to provide high quality, scalable video conferences.

It is a web interface to Jitsi Videobridge for audio and video
forwarding and relaying, using a webserver Nginx or Apache2.

This package contains configuration for Nginx to be used with
Jitsi Meet.

%package -n jitsi-meet-prosody
Summary: Prosody plugins and configuration for Jitsi Meet
Group: System/Servers
#Requires: openssl prosody | prosody-trunk | prosody-0.11
# The first release of 0.11 branch was 0.11.1
Requires: prosody >= 0.11.1

%description -n jitsi-meet-prosody
Jitsi Meet is a WebRTC JavaScript application that uses Jitsi
Videobridge to provide high quality, scalable video conferences.

It is a web interface to Jitsi Videobridge for audio and video
forwarding and relaying.

This package contains example configuration for Prosody to be used with
Jitsi Meet, as well as plugins to implement XEP-0340 and other essential
XMPP extensions.

%if 0
%package -n jitsi-meet-tokens
Summary: Prosody token authentication plugin for Jitsi Meet
Group: System/Servers
#Requires: ${misc:Depends} prosody-trunk (>= 1nightly747) | prosody-0.11 | prosody (>= 0.11.2) libssl-devel luarocks jitsi-meet-prosody

%package -n jitsi-meet-turnserver
Summary: Configures coturn to be used with Jitsi Meet
Group: System/Servers
#Requires: ${misc:Depends} nginx (>= 1.13.10) | nginx-full (>= 1.13.10) | nginx-extras (>= 1.13.10) jitsi-meet-prosody coturn dnsutils
%endif

%prep
%setup -a1
# Makefile uses it
#ln -sv %_bindir/webpack ./node_modules/.bin/webpack
#ln -sv %_bindir/node-sass ./node_modules/.bin/node-sass
# sass does not search .css files when importing
mv -v css/_audio-preview.css css/_audio-preview.scss
mv -v css/_meter.css css/_meter.scss
mv -v css/_video-preview.css css/_video-preview.scss

%build
# install needed here only for run postinstall
#npm install
npm run postinstall
cd node_modules/lib-jitsi-meet
npm run postinstall
cd -
make

rm -fv node_modules/{nan,node-sass,webpack,webpack-cli,node-gyp}
npm prune --production

%install
mkdir -p %buildroot%_sysconfdir/jitsi/meet
#install -m 644 lib/logging.properties %buildroot%_sysconfdir/jitsi/meet/


mkdir -p %buildroot%_datadir/%name/
install -m 644 interface_config.js %buildroot%_datadir/%name/
install -m 644 logging_config.js %buildroot%_datadir/%name/
install -m 644 *.json %buildroot%_datadir/%name/
install -m 644 *.html %buildroot%_datadir/%name/
install -m 644 *.ico %buildroot%_datadir/%name/
install -m 644 -D css/all.css -t %buildroot%_datadir/%name/css
cp -r sounds %buildroot%_datadir/%name/
cp -r fonts %buildroot%_datadir/%name/
cp -r images %buildroot%_datadir/%name/
cp -r lang %buildroot%_datadir/%name/
cp -r connection_optimization %buildroot%_datadir/%name/
install -m 644 resources/robots.txt %buildroot%_datadir/%name/
#install -m 755 resources/*.sh %buildroot%_datadir/%name/scripts/
cp -r libs %buildroot%_datadir/%name/
cp -r static %buildroot%_datadir/%name/
cp -r resources/prosody-plugins %buildroot%_datadir/%name/

DESTL=%buildroot%_datadir/%name/lang
LANGUAGES=$(node -p "Object.keys(require('./lang/languages.json')).join(' ')")
COUNTRIES_DIR=node_modules/i18n-iso-countries/langs
for i in $LANGUAGES ; do
    LOCALE=$(echo $i | cut -c1-2)
    [ -f $COUNTRIES_DIR/$i.json ] && LOCALE=$i
    [ -f $COUNTRIES_DIR/$LOCALE.json ] || continue
    cp -v $COUNTRIES_DIR/$LOCALE.json $DESTL/countries-$LOCALE.json
done

mkdir -p %buildroot%_datadir/jitsi-meet-web-config
cp config.js %buildroot%_datadir/jitsi-meet-web-config/

# This should be the last step to exclude doc/debian from being packaged
# into jitsi-meet-doc — parts of this directory are split between docdirs
# of subpackages.
mv doc/debian doc_debian

%files

%files -n jitsi-meet-doc
%doc doc/**

%files -n jitsi-meet-prosody
%_datadir/%name/prosody-plugins/
%doc doc_debian/jitsi-meet-prosody/*

%files -n jitsi-meet-web
%doc LICENSE
%doc README.md
%_datadir/%name
%exclude %_datadir/%name/prosody-plugins

%files -n jitsi-meet-web-config
%doc doc_debian/jitsi-meet
%dir %_sysconfdir/jitsi
%dir %_sysconfdir/jitsi/meet
%config %_sysconfdir/jitsi/meet/
%_datadir/jitsi-meet-web-config/
#doc doc/debian/jitsi-meet/README
#%_sysconfdir/jitsi/meet/*

%if 0
%files -n jitsi-meet-tokens

%files -n jitsi-meet-turnserver
%endif

%changelog
* Thu May 21 2020 Arseny Maslennikov <arseny@altlinux.org> 4109-alt0.2
- Packaged the webroot for Jitsi Meet's web app.
- Packaged Prosody plugins for Jitsi Meet.
  No pre-set configuration is applied yet, unlike the upstream-maintained
  packages for Debian.

* Thu May 14 2020 Vitaly Lipatov <lav@altlinux.ru> 4109-alt0.1
- initial build

* Mon Apr 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.0.0-alt0.1
- initial build

