%define oname ConfirmAccount
%define mwversion 1.34
%define revision 3ffa446
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-ConfirmAccount
Version: 1.34
Release: alt1.%revision

Summary: This extension disables direct account creation and requires submission and approval.

License: GPL
Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-build-mediawiki >= 0.6

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%revision.tar.gz
Source: %name-%version.tar

%description
The ConfirmAccount extension disables direct account creation
and requires submission and approval of accounts by bureaucrats.
Account creations can be enabled through configuring user rights,
such as if you wanted Sysops/Bureaucrats to be able to directly make them.

%prep
%setup

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Sun Dec 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1.34-alt1.3ffa446
- new version 1.34 (with rpmrb script)

* Tue Jul 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1.31-alt1.5d98110
- new version (1.31) with rpmgs script

* Thu Jun 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.23.b0651c1-alt1
- new version (1.23.b0651c1) with rpmgs script

* Wed Feb 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.22.74fabfc-alt1
- new version (1.22.74fabfc) with rpmgs script

* Tue Sep 10 2013 Vitaly Lipatov <lav@altlinux.ru> 1.21.d8632fb-alt1
- new version 1.21.d8632fb (with rpmrb script)

* Wed Jul 24 2013 Vitaly Lipatov <lav@altlinux.ru> 1.20.83ae0c9-alt1
- new version (1.20.83ae0c9)

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r62787-alt2
- rename spec
- fixes for MW > 1.16

* Sun Aug 15 2010 Vitaly Lipatov <lav@altlinux.ru> 1.16.r62787-alt1
- new version (1.16.r62787) import in git

