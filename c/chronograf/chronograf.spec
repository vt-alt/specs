%global import_path github.com/influxdata/chronograf
%global commit ae637397b8e6815d5ae4fe698f5e9a6a8e88c33c

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name:		chronograf
Version:	1.8.1
Release:	alt1
Summary:	Open source framework for processing, monitoring, and alerting on time series data

Group:		Development/Other
License:	MIT
URL:		https://github.com/influxdata/chronograf

Source0:	%name-%version.tar

Source100: %name.sysconfig
Source101: %name.logrotate
Source102: %name.init
Source103: %name.service
Source104: %name.tmpfiles

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: go-bindata
BuildRequires: npm yarn
BuildRequires: node node-devel
BuildRequires: fontconfig libfreetype

BuildRequires: /proc

%description
Open source framework for processing, monitoring, and alerting on time series data.

%prep
# Important!!!
# The %%builddir/.gopath created by the hands. It contains the dependencies required for your project.
# This is necessary because the gdm cannot work with the vendor directory and always tries to update
# all dependencies from the external servers. So, we can't use Makefile to compile.
#
# $ go mod vendor
# $ git add -f vendor
# $ git commit -m "add go modules"
#
# $ cd ui && yarn --no-progress --no-emoji --verbose
# $ rm -rf node_modules/node-sass
# $ rm -rf node_modules/node-gyp
# $ rm -rf node_modules/deasync/bin
# $ git add -f node_modules
# $ git commit -m "add node js modules"

%setup -q

# add symlink to node headers
node_ver=$(node -v | sed -e "s/v//")
mkdir -p ui/node_modules/.node-gyp/$node_ver/include
ln -s %_includedir/node ui/node_modules/.node-gyp/$node_ver/include/node
echo "9" > ui/node_modules/.node-gyp/$node_ver/installVersion

ln -sf %nodejs_sitelib/node-gyp ui/node_modules/node-gyp
ln -sf %nodejs_sitelib/node-sass ui/node_modules/node-sass

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"
# export PATH="$PATH:$BUILDDIR/bin"
export npm_config_devdir="$PWD/ui/node_modules/.node-gyp"
export GO111MODULE=off

export VERSION=%version
export COMMIT=%shortcommit
export BRANCH=altlinux

%golang_prepare

pushd .gopath/src/%import_path
pushd ui
npm rebuild
popd
make
popd

#%golang_build cmd/*
#go install -ldflags "-X main.version=$VERSION -X main.commit=$COMMIT -X main.branch=$BRANCH" ./...

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
export IMPORT_PATH="%import_path"
#export GOPATH="$BUILDDIR:%go_path:$PWD"
export GO111MODULE=off

pushd .gopath/src/%import_path
install -p -D -m 755 chronograf %buildroot%_bindir/%name
install -p -D -m 755 chronoctl %buildroot%_bindir/chronoctl
popd

install -d -m 755 %buildroot%_datadir/%name
cp -pr canned %buildroot%_datadir/%name
#%golang_install

#rm -rf -- %buildroot%_datadir

# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name
# Install sysconfig
install -p -D -m 640 %SOURCE100 %buildroot%_sysconfdir/sysconfig/%name
# Install logrotate
install -p -D -m 644 %SOURCE101 %buildroot%_logrotatedir/%name
# Install sysv init scripts
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'Chronograf Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/%name
%_bindir/chronoctl
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/sysconfig/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name
%_datadir/%name

%changelog
* Sat Apr 11 2020 Alexey Shabalin <shaba@altlinux.org> 1.8.1-alt1
- 1.8.1

* Wed Sep 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.14-alt1
- 1.7.14

* Mon Jan 21 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.7-alt1
- 1.7.7

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.10.0-alt1%ubt
- 1.3.10.0

* Mon Aug 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.7.0-alt1%ubt
- 1.3.7.0

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5.0-alt1%ubt
- rebuild with Universal Branch Tag
- fix run with sysv init script

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5.0-alt1
- First build for ALTLinux.

