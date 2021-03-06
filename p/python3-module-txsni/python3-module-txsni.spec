%define modulename txsni

Name: python3-module-txsni
Version: 0.2.0
Release: alt1

Summary: easy-to-use SNI endpoint for twisted

Url: https://github.com/glyph/txsni
License: MIT
Group: Development/Python3

# Source-url: https://pypi.io/packages/source/T/TxSNI/TxSNI-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
Simple support for running a TLS server with Twisted.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/
%python3_sitelibdir/twisted/plugins/*

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- new version 0.2.0 (with rpmrb script)

* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1.9-alt1
- initial build for ALT Sisyphus
