# check deps/npm/package.json for it
%define npmver 6.14.5
# separate build npm
%def_without npm
# in other case, note: we will npm-@npmver-@release package! fix release if npmver is unchanged

%define major 14.3

#we need ABI virtual provides where SONAMEs aren't enough/not present so deps
#break when binary compatibility is broken
%global nodejs_abi 14

%global napi 6

# TODO: really we have no configure option to build with shared libv8
# V8 presently breaks ABI at least every x.y release while never bumping SONAME,
# so we need to be more explicit until spot fixes that
%global v8_abi 7.9
%def_without systemv8

# supports only openssl >= 1.0.2
# see https://github.com/nodejs/node/issues/2783
%define openssl_version 1.0.2n
%def_with systemssl

%global libuv_abi 1.37.0
%def_with systemuv

# use 5.6 as c8
%global libicu_abi 5.6
%def_with systemicu
# TODO: node has to use icu:: for ICU names
#add_optflags -DU_USING_ICU_NAMESPACE=1

%global libnghttp2_abi 1.40.0
%def_with systemnghttp2

# to use internal llhttp
%def_without systemhttp-parser

%def_disable check

# https://nodejs.org/api/n-api.html
# https://github.com/nodejs/abi-stable-node
%def_with nodejs_abi

%define oversion %version

Name: node
Version: %major.0
Release: alt1

Summary: Evented I/O for V8 Javascript

Group: Development/Tools
License: MIT License
Url: http://nodejs.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

##Source-git: https://github.com/nodejs/node.git
# Source-url: https://nodejs.org/dist/v%version/node-v%version.tar.gz
Source: %name-%version.tar
Source7: nodejs_native.req.files

BuildRequires(pre): rpm-macros-nodejs
BuildRequires(pre): rpm-build-intro >= 2.1.5

BuildRequires: python3-devel gcc-c++ zlib-devel

BuildRequires: gyp
BuildRequires: python3-module-simplejson

%if_with systemv8
%define libv8_package libv8-nodejs
BuildRequires: %libv8_package-devel >= %v8_abi-devel
%endif

%if_with systemssl
BuildRequires: openssl-devel >= %openssl_version openssl
# for require strict library version
Requires: openssl >= %openssl_version
%endif

%if_with systemuv
BuildRequires: libuv-devel >= %libuv_abi
%endif

%if_with systemicu
BuildRequires: libicu-devel >= %libicu_abi
%endif

%if_with systemnghttp2
BuildRequires: libnghttp2-devel >= %libnghttp2_abi
%endif

%if_with systemhttp-parser
BuildRequires: libhttp-parser-devel >= 2.9.2-alt2
%endif
BuildRequires: libcares-devel >= 1.11.0

BuildRequires: curl
Provides: nodejs(engine) = %version
Provides: nodejs = %version-%release
Provides: node.js = %version-%release
Obsoletes: nodejs < %version-%release
Obsoletes: node.js < %version-%release

Provides: nodejs(abi) = %{nodejs_abi}
Provides: nodejs(v8-abi) = %{v8_abi}
Provides: nodejs(napi) = %{napi}

Provides: bundled(llhttp) = 2.0.4

# /usr/bin/ld.default: failed to set dynamic section sizes: memory exhausted
%ifarch %ix86
%define optflags_debug -g0
%endif

# use no more than system_memory/1400 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
%_tune_parallel_build_by_procsize 1400

%add_findreq_skiplist %{_datadir}/node/sources/*

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

%package devel
Summary:        Devel package for Node.js
Group:          Development/Other
License:        MIT license
# arch depended info in .gypi
#BuildArch:      noarch
Provides:	nodejs-devel = %version-%release
Requires:	%name = %version
Requires:       gcc-c++ zlib-devel libcares-devel
%if_with systemv8
Requires:	%libv8_package-devel >= %{v8_abi}
%endif
%if_with systemssl
Requires:	openssl-devel >= %openssl_version
%endif
%if_with systemuv
Requires: libuv-devel >= %libuv_abi
%else
Conflicts:      libuv-devel
%endif

%description devel
Node.js header and build tools


%package doc
Summary: Documentation files
Group: Development/Other
Requires: %name-devel = %version-%release

BuildArch: noarch

%description doc
Documentation files for %name.

# https://bugzilla.altlinux.org/show_bug.cgi?id=38130
%if_with npm
%package -n npm
Version:	%npmver
Group:		Development/Tools
Summary:	A package manager for node
License:	MIT License
Requires:	node
BuildArch:	noarch
AutoReq:	yes,nopython
# https://bugzilla.altlinux.org/show_bug.cgi?id=38130
#%if_with nodejs_abi
Requires:	nodejs(abi) = %{nodejs_abi}
#%endif

%description -n npm
npm is a package manager for node. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.
%endif

%prep
%setup

%if_with systemv8
# hack against https://bugzilla.altlinux.org/show_bug.cgi?id=32573#c3
cp -a deps/v8/include/libplatform src
rm -rf deps/v8/
%endif

%if_with systemicu
rm -rf deps/icu-small/
%endif

%if_with systemuv
rm -rf deps/uv/
%__subst "s|deps/uv/uv.gyp ||" Makefile
%__subst "s|.*../uv/uv.gyp:libuv.*||" deps/uvwasi/uvwasi.gyp
%endif

%if_with systemnghttp2
rm -rf deps/nghttp2/
%endif

# disable external libs
# TODO:
# deps/gtest
rm -rf tools/gyp
rm -rf deps/zlib deps/openssl deps/cares
# make no sense for a first build
%__subst "s|deps/zlib/zlib.gyp||" Makefile


%if_without npm
#true
# don't use: keep internal npm (used for doc build)
rm -rf deps/npm/
ln -s %_libexecdir/node_modules/npm deps/npm
%endif

# use rpm's cflags
%__subst "s|'cflags': \[\],|'cflags': ['%optflags'],|" ./configure.py
# fix cflags wrap in outputted config.json
%__subst "s|indent=2|indent=2,width=160|" ./configure.py
# TODO: move to upstream?
%ifarch mipsel
%__subst "s|'libraries': \[\],|'libraries': ['-latomic'],|" ./configure.py
%endif

# override detected dir (detection via process.execPath does not work without /proc) with corect path
%__subst "s|path.resolve(prefixDir, 'lib', 'node')|'%nodejs_sitelib'|" lib/internal/modules/cjs/loader.js

%build
# hack against
# gyp: Error importing pymod_do_mainmodule (GN-scraper): No module named GN-scraper while loading dependencies of /tmp/.private/lav/RPM/BUILD/node-12.14.1/node.gyp
export PYTHONPATH=$(pwd)/tools/v8_gypfiles

./configure \
    --prefix=%_prefix \
    --shared-zlib \
%if_with systemicu
    --with-intl=system-icu \
%endif
%if_with systemhttp-parser
    --shared-http-parser \
%endif
    --shared-cares \
%if_with systemssl
    --shared-openssl \
    --shared-openssl-includes=%_includedir \
%endif
%if_without npm
    --without-npm \
%endif
%if_with systemuv
    --shared-libuv \
%endif
%if_with systemnghttp2
    --shared-nghttp2
%endif
%if_with systemv8
    --without-bundled-v8
%endif

%make_build BUILDTYPE=Release
# skip internal doc build (uses external modules)
#make doc
#%make jslint

%check
%make_build test

%install
mkdir -p %buildroot%nodejs_sitelib/

%makeinstall_std

%if_without systemuv
#install development headers
mkdir -p %{buildroot}%{_includedir}/node/
cp -p src/*.h %{buildroot}%{_includedir}/node
cp -p deps/uv/include/*.h %{buildroot}%{_includedir}/node
#cp -p deps/uv/include/uv-private/*.h %{buildroot}%{_includedir}/node/uv-private
%endif

%if_with npm
#node-gyp needs common.gypi too
mkdir -p %{buildroot}%{_datadir}/node
cp -p common.gypi %{buildroot}%{_datadir}/node
#tar -xf %{SOURCE0} --directory=%{buildroot}%{_datadir}/node/sources
%endif

%if_with nodejs_abi
# ensure Requires are added to every native module that match the Provides from
# the nodejs build in the buildroot
install -Dpm0755 %{SOURCE7} %buildroot%_rpmlibdir/nodejs_native.req.files
cat << EOF > %buildroot%_rpmlibdir/nodejs_native.req
#!/bin/sh
echo 'nodejs(abi) = %nodejs_abi'
echo 'nodejs(v8-abi) = %v8_abi'
EOF
chmod 0755 %buildroot%_rpmlibdir/nodejs_native.req
%endif

rm -rf %buildroot/usr/lib/dtrace/
rm -rf %buildroot/usr/share/doc/node/gdbinit
rm -rf %buildroot/usr/share/doc/node/lldb_commands.py
rm -rf %buildroot/usr/share/doc/node/lldbinit


# drop tapset file
rm -rf %buildroot%_datadir/systemtap/tapset

# pack node include tarball required to gyp building
#mkdir -p %name-v%version/include/
#cp -rp %buildroot%_includedir/%name %name-v%version/include/
#mkdir -p %buildroot%_datadir/node/
#tar -zcf %buildroot%_datadir/%name/%name-v%version-headers.tar.gz %name-v%version

#ln -s node_modules %buildroot%_prefix/lib/node

%files
%doc AUTHORS CHANGELOG.md LICENSE README.md
%_bindir/node
%dir %nodejs_sitelib
#_prefix/lib/node
#%_datadir/systemtap/tapset/node.stp
%_man1dir/*

%files doc
%doc README.md
#out/doc/api

%files devel
%dir %_includedir/node/
#%_datadir/%name/%name-v%version-headers.tar.gz
%if_without systemuv
%_includedir/node/uv*
%endif
%if_without systemv8
%_includedir/node/v8*
%endif
%_includedir/node/node*
%_includedir/node/js_native_api*
# deps/cares
#_includedir/node/ares*
%_includedir/node/common.gypi
%_includedir/node/config.gypi
%_includedir/node/libplatform/
# deps/http_parser
#_includedir/node/nameser.h
#_datadir/node/common.gypi
%if_with nodejs_abi
%_rpmlibdir/nodejs_native.req
%_rpmlibdir/nodejs_native.req.files
%endif
#%_datadir/node/sources

%if_with npm
%files -n npm
%_bindir/npm
%nodejs_sitelib/npm/
%exclude %_libexecdir/node_modules/npm/node_modules/node-gyp/gyp/tools/emacs
%endif

%changelog
* Fri May 22 2020 Vitaly Lipatov <lav@altlinux.ru> 14.3.0-alt1
- new version 14.3.0 (with rpmrb script)
- npm >= 6.14.5

* Thu May 07 2020 Vitaly Lipatov <lav@altlinux.ru> 14.2.0-alt1
- new version 14.2.0 (with rpmrb script)
- set node ABI to 14
- libuv >= 1.37.0

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 13.12.0-alt1
- new version 13.12.0 (with rpmrb script)
- npm >= 6.14.4
- libuv >= 1.35.0

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 13.11.0-alt1
- new version 13.11.0

* Tue Mar 10 2020 Vitaly Lipatov <lav@altlinux.ru> 13.10.1-alt1
- new version 13.10.1
- set node ABI to 13

* Tue Mar 03 2020 Vitaly Lipatov <lav@altlinux.ru> 13.9.0-alt3
- use direct /usr/lib/node_modules instead of detected prefix/lib/node

* Fri Feb 28 2020 Vitaly Lipatov <lav@altlinux.ru> 13.9.0-alt2
- drop profile with broken obsoleted NODE_PATH
- add /usr/lib/node symlink to /usr/lib/node_modules

* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 13.9.0-alt1
- new version 13.9.0 (security fixes)
- set libicu >= 5.6

* Tue Feb 11 2020 Vitaly Lipatov <lav@altlinux.ru> 13.8.0-alt1
- new version 13.8.0 (with rpmrb script)
- CVE-2019-15606, CVE-2019-15605, CVE-2019-15604

* Mon Jan 20 2020 Vitaly Lipatov <lav@altlinux.ru> 13.6.0-alt2
- make node-devel as arch
- drop tarball with node include headers (see ALT bug 36349)
- add fixes for ix86 build

* Thu Jan 16 2020 Vitaly Lipatov <lav@altlinux.ru> 13.6.0-alt1
- new version 13.6.0 (with rpmrb script)
- libuv >= 1.34.0
- switch to python3

* Thu Jan 16 2020 Vitaly Lipatov <lav@altlinux.ru> 12.14.1-alt1
- new version 12.14.1 (with rpmrb script)
- build without system http-parser (use bundled llhttp 2.0.1)

* Thu Jan 16 2020 Pavel Skrylev <majioa@altlinux.org> 10.18.0-alt2
- added (+) tarball for node include headers to devel package

* Thu Dec 26 2019 Vitaly Lipatov <lav@altlinux.ru> 10.18.0-alt1
- new version 10.18.0 (with rpmrb script)
- npm >= 6.13.4 (security fix)

* Sat Oct 26 2019 Vitaly Lipatov <lav@altlinux.ru> 10.17.0-alt1
- new version 10.17.0 (with rpmrb script)
- npm >= 6.11.3

* Fri Aug 30 2019 Vitaly Lipatov <lav@altlinux.ru> 10.16.3-alt1
- new version 10.16.3 (with rpmrb script)
- libnghttp2 >= 1.39.2
- CVE-2019-9511, CVE-2019-9511, CVE-2019-9513, CVE-2019-9514
- CVE-2019-9515, CVE-2019-9516, CVE-2019-9517, CVE-2019-9518

* Thu Jun 06 2019 Vitaly Lipatov <lav@altlinux.ru> 10.16.0-alt1
- new version 10.16.0 (with rpmrb script)
- 2019-05-28, Version 10.16.0 'Dubnium' (LTS), @BethGriggs
- use npm 6.9, ICU >= 6.4, libuv >= 1.28.0

* Sat Mar 09 2019 Vitaly Lipatov <lav@altlinux.ru> 10.15.3-alt1
- new version 10.15.3 (with rpmrb script)
- 2018-03-05, Version 10.15.3 'Dubnium' (LTS), @BethGriggs
- CVE-2019-5737
- fix rpm's cflags using, add -latomic on mipsel
- use external gyp

* Thu Jan 17 2019 Vitaly Lipatov <lav@altlinux.ru> 10.15.0-alt1
- new version 10.15.0 (with rpmrb script)
- 2018-12-26, Version 10.15.0 'Dubnium' (LTS), @MylesBorins
- rebuild with http-parser 2.9.0

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 10.14.2-alt1
- new version 10.14.2 (with rpmrb script)
- 2018-12-11, Version 10.14.2 'Dubnium' (LTS), @MylesBorins prepared by @codebytere

* Fri Nov 30 2018 Vitaly Lipatov <lav@altlinux.ru> 10.14.1-alt1
- new version 10.14.1 (with rpmrb script)
- disable internal doc
- 2018-11-27, Version 10.14.0 'Dubnium' (LTS), @rvagg
- CVE-2018-12121, CVE-2018-12122, CVE-2018-12123

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 10.13.0-alt1
- new version 10.13.0 (with rpmrb script)
- 2018-10-30, Version 10.13.0 'Dubnium' (LTS), @MylesBorins

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 8.12.0-alt1
- new version 8.12.0 (with rpmrb script)
- 2018-09-11, Version 8.12.0 'Carbon' (LTS)

* Wed Aug 29 2018 Vitaly Lipatov <lav@altlinux.ru> 8.11.4-alt1
- new version 8.11.4 (with rpmrb script)
- 2018-08-15, Version 8.11.4 'Carbon' (LTS), @rvagg
- CVE-2018-0732, CVE-2018-12115
- build with external libnghttp2
- fix build with ICU >= 61 (add -DU_USING_ICU_NAMESPACE=1)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 8.11.3-alt1
- new version (8.11.3) with rpmgs script
- 2018-06-12, Version 8.11.3 'Carbon' (LTS), @evanlucas
- CVE-2018-7167, CVE-2018-7161, CVE-2018-1000168

* Tue May 22 2018 Vitaly Lipatov <lav@altlinux.ru> 8.11.2-alt1
- new version (8.11.2) with rpmgs script
- 2018-05-15, Version 8.11.2 'Carbon' (LTS)

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 6.14.2-alt1
- new version 6.14.2 (with rpmrb script)
- 2018-04-30 Node.js v6.14.2 'Boron' (LTS) Release

* Tue Feb 27 2018 Alexey Shabalin <shaba@altlinux.ru> 6.13.0-alt1
- new version 6.13.0
- 2018-02-13, Version 6.13.0 'Boron' (LTS)
- fixed CVE-2017-15896, CVE-2017-3738

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 6.11.4-alt1
- new version 6.11.4 (with rpmrb script)
- 2017-10-03, Version 6.11.4 'Boron' (LTS)

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 6.11.1-alt1
- new version 6.11.1 (with rpmrb script)
- 2017-07-11 v6.11.1 'Boron' (LTS) Release

* Mon May 08 2017 Vitaly Lipatov <lav@altlinux.ru> 6.10.3-alt1
- new version 6.10.3 (with rpmrb script)
- 2017-05-02, Version 6.10.3 'Boron' (LTS)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 6.10.2-alt1
- new version 6.10.2 (with rpmrb script)
- 2017-04-04, Version 6.10.2 'Boron' (LTS), @MylesBorins

* Sat Mar 11 2017 Vitaly Lipatov <lav@altlinux.ru> 6.10.0-alt1
- new version 6.10.0 (with rpmrb script)
- 2017-02-21 Node.js v6.10.0 'Boron' (LTS) Release

* Thu Feb 02 2017 Vitaly Lipatov <lav@altlinux.ru> 6.9.3-alt1
- new version 6.9.3 (with rpmrb script)
- 2017-01-03, Version 6.9.3 'Boron' (LTS)

* Sun Dec 18 2016 Vitaly Lipatov <lav@altlinux.ru> 6.9.2-alt2
- build without npm subpackage

* Wed Dec 07 2016 Vitaly Lipatov <lav@altlinux.ru> 6.9.2-alt1
- new version 6.9.2 (with rpmrb script)
- 2016-12-06 Node.js v6.9.2 'Boron' (LTS) Release

* Wed Nov 30 2016 Vitaly Lipatov <lav@altlinux.ru> 6.9.1-alt1
- new version 6.9.1 (with rpmrb script)
- 2016-10-19 Node.js v6.9.1 'Boron' (LTS) Release

* Wed Oct 05 2016 Vitaly Lipatov <lav@altlinux.ru> 6.7.0-alt6
- new version 6.7.0 (with rpmrb script)

* Fri Sep 02 2016 Vitaly Lipatov <lav@altlinux.ru> 6.5.0-alt5
- new version 6.5.0 (with rpmrb script)

* Wed Aug 24 2016 Vitaly Lipatov <lav@altlinux.ru> 6.4.0-alt4
- build 2016-08-15 Node.js v6.4.0 (Current) Release

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 6.3.1-alt3
- build 2016-07-21 Node.js v6.3.1 (Current) Release
- build with system libicu, libhttp_parser, c-ares

* Fri Jul 15 2016 Vitaly Lipatov <lav@altlinux.ru> 6.3.0-alt2
- cleanup spec

* Thu Jul 14 2016 Evgeny Bovykin <missingdays@etersoft.ru> 6.3.0-alt1
- build 2016-07-06 Node.js v6.3.0 Release

* Thu Jun 16 2016 Vitaly Lipatov <lav@altlinux.ru> 4.4.5-alt1
- build 2016-05-24 Version 4.4.5 'Argon' (LTS)

* Wed Apr 13 2016 Vitaly Lipatov <lav@altlinux.ru> 4.4.3-alt1
- build 2016-04-12, Version 4.4.3 'Argon' (LTS)
- drop gnuplot and convert reqs from npm
- disable python reqs for npm package

* Wed Feb 10 2016 Vitaly Lipatov <lav@altlinux.ru> 4.2.6-alt2
- build with system libuv-devel 1.8.0
- fix include packing

* Tue Feb 09 2016 Vitaly Lipatov <lav@altlinux.ru> 4.2.6-alt1
- 2016-01-21 Node.js v4.2.6 "Argon" (LTS) Release (ALT bug #30191)
- build with system openssl 1.0.2
- split doc subpackage

* Mon Nov 23 2015 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt1
- build 4.2.2 LTS version
- build with static v8 4.5 and static openssl 1.0.2

* Wed Oct 02 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.20-alt1
- new version
- npm 1.3.8

* Sun Sep 15 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.18-alt1
- new version

* Sat Aug 17 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.16-alt1
- new version
- npm 1.3.8

* Sat Jul 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.15-alt2.1
- libv8 requires

* Sat Jul 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.15-alt2
- nodejs(engine) should be = %%version
- added explicit abi autorequires for binary packages
- fix for %ix86 compilation w/o -fPIC
- explicit linkage with libv8

* Fri Jul 26 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.15-alt1
- new version
- npm 1.3.5

* Sat Jul 13 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.13-alt1
- 0.10.13
- npm 1.3.2
- added node-devel (ALT #29182)

* Wed Jun 26 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.12-alt1
- 0.10.12
- npm 1.2.32
- Provides: nodejs(engine) by viy@

* Wed May 29 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.8-alt1
- 0.10.8
- npm 1.2.23

* Tue May 07 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.5-alt1
- 0.10.5

* Thu Apr 18 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.4-alt1
- 0.10.4
- npm 1.2.18

* Sat Apr 06 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.3-alt1
- 0.10.3
- npm 1.2.17
- Build with shared libuv

* Fri Mar 29 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.10.2-alt1
- 0.10.2
- npm 1.2.15

* Sun Feb 10 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.19-alt1
- 0.8.19
- nmp 1.2.10

* Fri Jan 25 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.18-alt1.1
- Fix spec
  + non-strict dependency on node
  + added %optflags on build

* Sun Jan 20 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.18-alt1
- 0.8.18
- npm 1.2.2

* Sat Oct 27 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.14-alt1
- v0.8.14
- npm v1.1.65

* Mon Jul 23 2012 Mikhail Pokidko <pma@altlinux.org> 0.8.3-alt1
- v0.8.3

* Tue Jun 26 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.8.0-alt1
- 0.8.0

* Thu Jun 21 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt4
- Fix BuildRequires
- Added rpm-build-node subpackage
- Provides nodejs node.js
- Separate package devel

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt3.1
- Conflicts with node.js

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt3
- Declare NODE_PATH

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt2
- npm is noarch package

* Sun Jun 17 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.6.19-alt1
- v0.6.19
- Separate npm package

* Sat May 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.17-alt1
- v0.6.17

* Tue Apr 10 2012 Mikhail Pokidko <pma@altlinux.org> 0.6.15-alt1
- v0.6.15

* Mon Feb 06 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.10-alt1
- v0.6.10

* Sun Jan 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.9-alt1
- v0.6.9

* Fri Dec 02 2011 Mikhail Pokidko <pma@altlinux.org> 0.6.4-alt1
- v0.6.4

* Mon Nov 28 2011 Mikhail Pokidko <pma@altlinux.org> 0.6.3-alt1
- v0.6.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.11-alt1.1
- Rebuild with Python-2.7

* Mon Aug 22 2011 Mikhail Pokidko <pma@altlinux.org> 0.4.11-alt1
- v0.4.11

* Tue Jun 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.8-alt1
- initial

