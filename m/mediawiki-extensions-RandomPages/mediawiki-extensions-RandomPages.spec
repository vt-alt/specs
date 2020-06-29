%define oname RandomPages

%define mwversion 1.34
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 0.5
Release: alt1

Summary: RandomPages adds a new MediaWiki wiki parser for get random pages

License: GPL v3
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.6

Requires: mediawiki-common >= %mwversion

# Source-url: https://github.com/wikimedia/mediawiki-extensions-RandomPages/archive/%MWREL.zip
Source: %name-%version.tar

%description
RandomPages adds a new MediaWiki wiki parser tag: <randompages />
Available options:
* limit int, to control how many links should be
  fetched randomly from the database, defaults to 150
* namespace bool, true to restrict only to the global namspace, defaults to false
* levels int, levels of CSS applyed to each entry, defaluts to 5

%prep
%setup

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Fri May 01 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- new version (0.5) with rpmgs script - for 1.34

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- update version

* Sat Jun 05 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus

