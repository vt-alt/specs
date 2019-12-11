%define node_module webpack-cli

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-webpack-cli
Version: 3.3.9
Release: alt1

Summary: Webpack's Command Line Interface

License: MIT License
Group: Development/Other
Url: https://webpack.js.org/api/cli

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/webpack/webpack-cli/archive/v%version.tar.gz
Source: %name-%version.tar

#Source1: %name-preloaded-%version.tar
Source2: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

# /usr/bin/tsc
BuildRequires: node-typescript >= 3.5.2

# PeerDependencies
Requires: node-webpack >= 4.41.2

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
webpack CLI provides a flexible set of commands for developers to increase speed
when setting up a custom webpack project.
As of webpack v4, webpack is not expecting a configuration file,
but often developers want to create a more custom webpack configuration based on their use-cases and needs.
webpack CLI addresses these needs by providing a set of tools to improve the setup of custom webpack configuration.

Webpack is a  bundler for javascript and friends. Packs many modules into a few bundled assets.
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

#npm install --prefix %buildroot
mkdir -p %buildroot%nodejs_sitelib/%node_module/
chmod a+x bin/*
#cp -rp bin node_modules package.json %buildroot/%nodejs_sitelib/%node_module
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/test/

mkdir -p %buildroot%_bindir/
#ln -s %nodejs_sitelib/%node_module/bin/webpack.js %buildroot%_bindir/webpack
%_ln_sr %buildroot%nodejs_sitelib/%node_module/bin/cli.js %buildroot%_bindir/webpack

#nodejs_symlink_deps

%files
%doc LICENSE README.md
%_bindir/webpack
%nodejs_sitelib/%node_module/

%changelog
* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 3.3.9-alt1
- initial build for ALT Sisyphus
