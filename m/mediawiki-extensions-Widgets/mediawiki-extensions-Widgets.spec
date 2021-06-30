%define ShortName Widgets

Name: mediawiki-extensions-%ShortName
Version: 1.3.0
Release: alt1git

BuildArch: noarch

Group: Networking/WWW
Summary: Widgets extension allows adding widgets to wiki by just creating pages in Widget namespace
Url: http://www.mediawiki.org/wiki/Extension:%ShortName

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildRequires: rpm-build-mediawiki >= 0.2
BuildRequires: rpm-build-intro
Requires: mediawiki-common >= 1.31

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://github.com/wikimedia/mediawiki-extensions-Widgets/archive/refs/heads/master.zip
Source: %name-%version.tar

Source1: %name-predownloaded-production.tar

%description
Widgets extension allows adding widgets
to wiki by just creating pages in Widget namespace.

%prep
%setup -a1
%remove_repo_info
rm -f compiled_templates/*.php
rm -rf googlecode/

%install
%mediawiki_ext_install 50 %ShortName
subst "4i\$wgGroupPermissions['sysop']['editwidgets'] = true;" %buildroot%_mediawiki_settings_dir/50-%ShortName.php

%files -f %ShortName.files

%changelog
* Sun Jun 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1git
- new version (1.3.0) with rpmgs script
- CVE-2020-9382, CVE-2020-35625

* Sun Oct 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- incorporate smarty

* Sun Oct 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- new version 1.1 (with rpmrb script)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus
