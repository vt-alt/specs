Name: npm
Version: 6.13.7
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

# Note! Change version with new npm
Requires: npm(node-gyp) = 5.0.7

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
ln -s %nodejs_sitelib/%name/bin/npm-cli.js %buildroot%_bindir/npm
ln -s %nodejs_sitelib/%name/bin/npx-cli.js %buildroot%_bindir/npx

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
%_bindir/npx
%nodejs_sitelib/%name/

%changelog
* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 6.13.7-alt1
- new version 6.13.7 (with rpmrb script)

* Wed Feb 19 2020 Vitaly Lipatov <lav@altlinux.ru> 6.13.6-alt2
- pack /usr/bin/npx

* Tue Feb 18 2020 Vitaly Lipatov <lav@altlinux.ru> 6.13.6-alt1
- new version 6.13.6 (with rpmrb script)

* Wed Dec 25 2019 Vitaly Lipatov <lav@altlinux.ru> 6.13.4-alt1
- new version 6.13.4 (with rpmrb script)

* Sat Oct 26 2019 Vitaly Lipatov <lav@altlinux.ru> 6.11.3-alt1
- new version 6.11.3 (with rpmrb script)

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

