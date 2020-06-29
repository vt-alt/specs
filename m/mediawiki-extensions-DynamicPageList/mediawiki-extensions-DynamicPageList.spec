%define ShortName DynamicPageList

%define mwversion 1.34
%setup_mediawiki_ext %mwversion %ShortName

Name: mediawiki-extensions-%ShortName
Version: 1.7.0
Release: alt1.1

BuildArch: noarch

Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%ShortName
License: GPL

Summary: MediaWiki extension for build a list of pages that are listed in a set of categories

Packager: Vitaly Lipatov <lav@altlinux.ru>


BuildRequires(pre): rpm-build-mediawiki >= 0.6
Requires: mediawiki-common >= %mwversion

# Source-url: https://github.com/wikimedia/mediawiki-extensions-intersection/archive/%MWREL.zip
Source: %name-%version.tar

%description
DynamicPageList is a MediaWiki extension which allows wiki users to
create a list of pages that are listed in a set of categories.

%prep
%setup

%install
%mediawiki_ext_install 50 %ShortName

%files -f %ShortName.files

%changelog
* Fri May 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1.1
- new version (1.7.0) with rpmgs script

* Tue Jul 29 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- initial build for ALT Linux Sisyphus
