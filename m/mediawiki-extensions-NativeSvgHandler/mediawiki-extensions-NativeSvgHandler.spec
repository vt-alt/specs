%define oname NativeSvgHandler

%define mwversion 1.35
%define revision 8d64cd5
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 1.3.1
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Url: http://www.mediawiki.org/wiki/Extension:%oname
License: GPL

Summary: Allows SVG files to be served directly to clients

Packager: Vitaly Lipatov <lav@altlinux.ru>


BuildRequires(pre): rpm-build-mediawiki >= 0.6
Requires: mediawiki-common >= %mwversion

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%revision.tar.gz
Source: %name-%version.tar

%description
The NativeSvgHandler extension allows SVG files
to be served directly to clients for client-side rendering.

%prep
%setup

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- initial build for ALT Sisyphus
