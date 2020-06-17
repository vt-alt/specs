%define pname node-sass

Name: node-sass
Version: 4.13.1
Release: alt2

Summary: Node.js bindings to libsass

License: MIT License
Group: Development/Other
Url: https://github.com/sass/sass

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sass/node-sass/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

BuildRequires: libsass-devel

#Requires: node >= 8

#AutoReq: no
#AutoProv: no

%description
Node-sass is a library that provides binding for Node.js to LibSass,
the C version of the popular stylesheet preprocessor, Sass.

It allows you to natively compile .scss files to css at incredible speed
and automatically via a connect middleware.

%prep
%setup -a 1
rm -rfv src/libsass/
# fix deps
rm -rfv node_modules/resolve/test/

%build
ln -s %nodejs_sitelib/node-gyp node_modules/
LIBSASS_EXT=auto npm run-script build
# can't build in the simple way
#npm_build

rm -f node_modules/node-gyp
npm prune --production

#%check
#npm test

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

%npm_install
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%pname/bin/node-sass %buildroot%_bindir/node-sass
cp -a node_modules %buildroot/%nodejs_sitelib/%pname/
cp -a vendor %buildroot/%nodejs_sitelib/%pname/

%files
%doc LICENSE README.md TROUBLESHOOTING.md
%_bindir/node-sass
%nodejs_sitelib/%pname/

%changelog
* Tue Mar 03 2020 Vitaly Lipatov <lav@altlinux.ru> 4.13.1-alt2
- rewrite spec

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 4.13.1-alt1
- initial build for ALT Sisyphus
