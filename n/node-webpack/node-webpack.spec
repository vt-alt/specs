%define node_module webpack

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-webpack
Version: 4.41.2
Release: alt1

Summary: A bundler for javascript and friends

License: MIT License
Group: Development/Other
Url: https://github.com/webpack/webpack

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/webpack/webpack/archive/v%version.tar.gz
Source: %name-%version.tar

#Source1: %name-preloaded-%version.tar
Source2: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

Requires: node >= 8
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

AutoReq: no
AutoProv: no
Requires: node

%description
A bundler for javascript and friends. Packs many modules into a few bundled assets.
Code Splitting allows for loading parts of the application on demand.
Through "loaders", modules can be CommonJs, AMD, ES6 modules, CSS, Images,
JSON, Coffeescript, LESS, ... and your custom stuff. 

%prep
%setup -a 2

%build

# do not work without development requires
# and needs xvfb-maybe
#%check
#npm test

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/test/

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module/

%changelog
* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 4.41.2-alt1
- initial build for ALT Sisyphus
