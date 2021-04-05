%define oname PyPDF3

Name: python3-module-%oname
Version: 1.0.3
Release: alt1

Summary: Pure Python PDF toolkit

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/PyPDF3/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

#Requires: python-module-Reportlab

%description
A Pure-Python library built as a PDF toolkit. It is capable of:

* extracting document information (title, author, ...)
* splitting documents page by page
* merging documents page by page
* cropping pages
* merging multiple pages into a single page
* encrypting and decrypting PDF files
* and more!

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc CHANGELOG *.md
%python3_sitelibdir/*

%changelog
* Wed Mar 31 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Sisyphus

