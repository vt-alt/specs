%define oname soupsieve
Name: python3-module-%oname
Version: 2.0.1
Release: alt1

Summary: A modern CSS selector implementation for BeautifulSoup

License: MIT
Group: Development/Python
Url: https://github.com/facelessuser/soupsieve

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
%py3_use BeautifulSoup4
#%py3_use pytest

%description
Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4.
It aims to provide selecting, matching, and filtering using modern CSS selectors.
Soup Sieve currently provides selectors from the CSS level 1 specifications up
through the latest CSS level 4 drafts and beyond (though some are not yet implemented).

Soup Sieve was written with the intent to replace Beautiful Soup's builtin select feature,
and as of Beautiful Soup version 4.7.0.
Soup Sieve can also be imported in order to use its API directly for more controlled, specialized parsing.

Soup Sieve has implemented most of the CSS selectors up through the latest CSS draft specifications,
though there are a number that don't make sense in a non-browser environment.

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
* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Sun Apr 12 2020 Eugene Omelyanovich <regatio@etersoft.ru> 2.0-alt1
- new version (2.0) with rpmgs script





