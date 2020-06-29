%define oname SecureHTML

Name: mediawiki-extensions-%oname
Version: 3.0
Release: alt2

Summary: This MediaWiki extension provides a secure way to include raw HTML code on a page

License: No license specified
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: rpm-build-mediawiki >= 0.3

Requires: mediawiki-common >= 1.30

#Requires: mediawiki-extensions-StubManager

# Source-url: https://github.com/wikimedia/mediawiki-extensions-SecureHTML/archive/v%version.tar.gz
Source: %oname-%version.tar

%description
This extension allows editors to add HTML section(s) or pages on a wiki page.
This extension can only be used on protected pages,
but allows an editor to add a protected template on an unprotected, editable page.

%prep
%setup -n %oname-%version

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Thu Oct 31 2019 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt2
- drop StubManager require 

* Mon May 14 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- new version (3.0) with rpmgs script

* Wed May 26 2010 Vitaly Lipatov <lav@altlinux.ru> 2.3.0.r1223-alt1
- initial build for ALT Linux Sisyphus

