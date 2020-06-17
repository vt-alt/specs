%define pname nan

Name: node-nan
Version: 2.14.0
Release: alt1

Summary: Native Abstractions for Node.js

License: MIT License
Group: Development/Other
Url: https://github.com/nodejs/nan

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/nodejs/nan/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs
BuildRequires: node-gyp

#AutoReq: no
#AutoProv: no

%description
Thanks to the crazy changes in V8 (and some in Node core),
keeping native addons compiling happily across versions,
particularly 0.10 to 0.12 to 4.0, is a minor nightmare.
The goal of this project is to store all logic necessary
to develop native Node.js addons without having
to inspect NODE_MODULE_VERSION and get yourself into a macro-tangle.

This project also contains some helper utilities
that make addon development a bit more pleasant.

%prep
%setup -a 1

%build
%npm_build
cd test && node-gyp rebuild && cd - >/dev/null
npm test
npm prune --production

#%check
#npm test

%install
%npm_install
rm -rf %buildroot/%nodejs_sitelib/%pname/{test,tools,doc,examples}/

%files
%doc LICENSE.md README.md
%nodejs_sitelib/%pname/

%changelog
* Fri Feb 28 2020 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt1
- initial build for ALT Sisyphus
