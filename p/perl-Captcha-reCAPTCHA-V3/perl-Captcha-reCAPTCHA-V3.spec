%define module_name Captcha-reCAPTCHA-V3
%define _unpackaged_files_terminate_build 1
Name: perl-%module_name
Version: 0.01
Release: alt1
Summary: A Perl implementation of reCAPTCHA API version v3
Group: Development/Perl
License: perl
URL: https://github.com/worthmine/Captcha-reCAPTCHA-V3

Source0: perl-%module_name-%version.tar
BuildArch: noarch
BuildRequires: perl-HTTP-Tiny
BuildRequires: perl-JSON
BuildRequires: perl-Module-Build-Tiny

%description
Captcha::reCAPTCHA::V3 - A Perl implementation of reCAPTCHA API version v3

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_privlib/C*
%perl_vendor_privlib/auto/*

%changelog
* Thu Oct 01 2020 Oleg Solovyov <mcpain@altlinux.org> 0.01-alt1
- initial build for ALT (ported from autoimports)

