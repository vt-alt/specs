Name: node-gyp
Version: 5.0.7
Release: alt1

Summary: Node.js native addon build tool
License: MIT
Group: Development/Tools

Url: https://github.com/TooTallNate/node-gyp

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-url: http://registry.npmjs.org/node-gyp/-/node-gyp-%version.tgz
# Source-url: https://github.com/nodejs/node-gyp/archive/v%version.tar.gz
Source: %name-%version.tar

# Note: see .gear/predownloaded-production created with rpmgs -f from etersoft-build-utils
Source2: %name-production-%version.tar

Source10: addon-rpm.gypi

BuildArch: noarch

# we do not need any module provides here
AutoProv: yes,nonodejs,noruby,notex
AutoReq: yes,nonodejs,noruby,notex

Provides: npm(node-gyp) = %version

# use RPM installed headers by default instead of downloading a source tree
# for the currently running node version
Patch1: node-gyp-addon-gypi.patch

# use the system gyp
Patch2: node-gyp-system-gyp.patch

# use system node dir (/usr)
Patch3: node-gyp-system-nodedir.patch

# use python3 only
Patch4: node-gyp-python3.patch

BuildRequires(pre): rpm-macros-nodejs

# TODO: compare with internal
#gyp is the actual build framework node-gyp uses
Requires: gyp >= 0.1.h.e87d37d6

#this is the standard set of headers expected to build any node native module
#Requires: rpm-build-nodejs
#Requires:      npm
Requires:      node-devel
# still used in node-gyp
Requires:      rpm-build-python3

#we also need a C++ compiler to actually build stuff ;-)
# TODO: what about toolchain?
# See https://bugzilla.altlinux.org/show_bug.cgi?id=37687
#Requires: gcc-c++
Requires: make

%description
node-gyp is a cross-platform command-line tool written in Node.js for compiling
native addon modules for Node.js, which takes away the pain of dealing with the
various differences in build platforms.

Install gcc-c++ package for compiling native addon modules for Node.js.

%prep
%setup -a 2
#patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p2

# use system gyp
%__subst "s|\(var gyp_script =\).*|\1 '/usr/bin/gyp'|g" lib/configure.js

# fix -fPIC using on ix86
%__subst 's| and target_arch!="ia32"||' addon.gypi

#nodejs_fixdep request 2.x
#nodejs_fixdep npmlog 3
#nodejs_fixdep nopt 3
#nodejs_fixdep semver 2.1
#patch33 -p0

# drop internal gyp
rm -rf gyp/
mkdir gyp/
# compat hack
ln -s %_bindir/gyp gyp/gyp_main.py

%build
#nothing to do

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

mkdir -p %buildroot%nodejs_sitelib/node-gyp/
cp -pr addon*.gypi bin lib gyp node_modules package.json %buildroot%nodejs_sitelib/node-gyp/
#cp -p %SOURCE10 %buildroot%nodejs_sitelib/node-gyp/addon-rpm.gypi

mkdir -p %buildroot%_bindir
ln -sf ../lib/node_modules/node-gyp/bin/node-gyp.js %buildroot%_bindir/node-gyp

# we will do bundle
#nodejs_symlink_deps

%files
%_bindir/node-gyp
%nodejs_sitelib/node-gyp/
%doc README.md LICENSE

%changelog
* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.7-alt1
- new version 5.0.7 (with rpmrb script)
- disable rpm-build-nodejs requires (break a circle)

* Mon Jan 20 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.5-alt3
- use system node include dir to binary build (ALT bug 36349)
- first use python3 to gyp run

* Thu Jan 16 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0.5-alt2
- drop buildreqs (we skip build here)
- switch to python3

* Thu Dec 26 2019 Vitaly Lipatov <lav@altlinux.ru> 5.0.5-alt1
- new version (5.0.5) with rpmgs script
- drop gcc-c++ requires (ALT bug 37687)

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 3.8.0-alt1
- new version (3.8.0) with rpmgs script

* Tue May 22 2018 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt1
- new version (3.6.2) with rpmgs script

* Sat Mar 18 2017 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt2
- build fixes

* Sun Dec 18 2016 Vitaly Lipatov <lav@altlinux.ru> 3.4.0-alt1
- new version 3.4.0 (with rpmrb script)

* Thu Aug 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt4_2
- fc import

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt4_1
- addon.gypi patched also

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt3_1
- link with libv8

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt2_1
- use -fPIC on ix86

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.6-alt1_1
- fc import

* Tue Jun 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1
- initial import

