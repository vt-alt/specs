Name: npm
Version: 6.9.0
Release: alt1

Summary: A package manager for node

Group: Development/Tools
License: MIT License
Url: http://nodejs.org/

# Source-url: https://github.com/npm/cli/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs

#BuildRequires: node >= 6.9
#Requires:	node >= 6.9
Requires: npm(node-gyp) = 3.8.0

BuildArch:	noarch

# we do not need any module provides here
AutoProv: yes,nonodejs
AutoReq: yes,nonodejs

%description
npm is a package manager for node. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.

npm is configured to use npm, Inc.'s public package registry
at https://registry.npmjs.org by default.


%prep
%setup
rm -rf bin/node-gyp-bin node_modules/node-gyp/ node_modules/.bin/node-gyp node_modules/npm-lifecycle/node-gyp-bin

%build
#make man

%install
mkdir -p %buildroot%nodejs_sitelib/%name/ %buildroot%_bindir/
ln -s %nodejs_sitelib/%name/bin/npm-cli.js %buildroot%_bindir/%name

# need inet
#node cli.js install -g --prefix %buildroot%_prefix
# just copy, like in node package was
cp -a . %buildroot%nodejs_sitelib/%name/

rm -rf %buildroot%nodejs_sitelib/%name/node_modules/node-gyp/gyp/tools/emacs
# need python2.7(TestCommon)
rm -rf %buildroot%nodejs_sitelib/%name/node_modules/node-gyp/gyp/pylib/gyp/generator/ninja_test.py
# drop due empty fixtures/package.json
rm -rf %buildroot%nodejs_sitelib/test/
# drop due docker requires
rm -rf %buildroot%nodejs_sitelib/%name/node_modules/node-gyp/test/

# skip gnuplot and convert reqs
rm -rf %buildroot%nodejs_sitelib/%name/node_modules/request/node_modules/node-uuid/benchmark/

%files -n npm
%_bindir/npm
%nodejs_sitelib/%name/

%changelog
* Fri Jun 07 2019 Vitaly Lipatov <lav@altlinux.ru> 6.9.0-alt1
- new version 6.9.0 (with rpmrb script)

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 6.4.1-alt1
- new version 6.4.1 (with rpmrb script)

* Tue May 22 2018 Vitaly Lipatov <lav@altlinux.ru> 5.6.0-alt1
- new version 5.6.0 (with rpmrb script)

* Sat Mar 18 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.10-alt2
- build with external node-gyp

* Thu Feb 02 2017 Vitaly Lipatov <lav@altlinux.ru> 3.10.10-alt1
- new version 3.10.10 (with rpmrb script)

* Wed Dec 21 2016 Vitaly Lipatov <lav@altlinux.ru> 3.10.9-alt3
- drop gnuplot and convert requires

* Sun Dec 18 2016 Vitaly Lipatov <lav@altlinux.ru> 3.10.9-alt2
- new version 3.10.9 (with rpmrb script)

* Sat Oct 08 2016 Vitaly Lipatov <lav@altlinux.ru> 3.10.3-alt1
- initial build for ALT Linux Sisyphus

