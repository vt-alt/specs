Name: npm
Version: 6.14.10
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
#Requires: npm(node-gyp) = 5.0.7

BuildArch:	noarch

# we do not need any module provides here
AutoProv: yes,nonodejs
AutoReq: yes,nonodejs

%description
npm is a package manager for node. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.

npm is configured to use npm, Inc.'s public package registry
at https://registry.npmjs.org by default.

It is not recommended to build binary libraries within npm module,
but you can install node-gyp package to support that.
In most cases it is enough to install appropriate node- subpackage (like node-sass).

%prep
%setup
rm -rf bin/node-gyp-bin node_modules/node-gyp/ node_modules/.bin/node-gyp node_modules/npm-lifecycle/node-gyp-bin
# fix 
# npm ERR! code MODULE_NOT_FOUND
# npm ERR! Cannot find module 'node-gyp/bin/node-gyp
%__subst "s|const DEFAULT_NODE_GYP_PATH = .*|const DEFAULT_NODE_GYP_PATH = '/usr/bin/node-gyp'|" node_modules/npm-lifecycle/index.js

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
* Fri Feb 05 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.10-alt1
- new version 6.14.10 (with rpmrb script)

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.8-alt1
- new version 6.14.8 (with rpmrb script)

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.7-alt1
- new version 6.14.7 (with rpmrb script)

* Sat Jun 27 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.5-alt3
- fix npm ERR without module 'node-gyp/bin/node-gyp'

* Tue Jun 23 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.5-alt2
- drop node-gyp requires (to avoid toolchain requires)

* Fri May 22 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.5-alt1
- new version 6.14.5 (with rpmrb script)

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 6.14.4-alt1
- new version 6.14.4 (with rpmrb script)

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

