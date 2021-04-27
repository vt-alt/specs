%define oname python-gnupg

Name: python3-module-gnupg
Version: 0.4.6
Release: alt1

Summary: A Python wrapper for GnuPG

License: BSD
Group: Development/Python
Url: https://docs.red-dove.com/python-gnupg/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro

%description
The gnupg module allows Python programs to make use of the functionality 
rovided by the GNU Privacy Guard (abbreviated GPG or GnuPG).
Using this module, Python programs can encrypt and decrypt data,
digitally sign documents and verify digital signatures,
manage (generate, list and delete) encryption keys,
using proven Public Key Infrastructure (PKI) encryption technology based on OpenPGP.

%prep
%setup

%build
%python3_build

%install
%python3_install

#%check
#%python3_test

%files
%python3_sitelibdir/*

%changelog
* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt1
- new version 0.4.6 (with rpmrb script)

* Sun Apr 12 2020 Eugene Omelyanovich <regatio@etersoft.ru> 0.4.5-alt1
- new version (0.4.5) with rpmgs script





