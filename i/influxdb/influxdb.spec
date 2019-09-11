%global import_path github.com/influxdata/influxdb
%global commit ff383cdc0420217e3460dabe17db54f8557d95b6

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name:		influxdb
Version:	1.7.8
Release:	alt1
Summary:	Distributed time-series database

Group:		Development/Other
License:	MIT
URL:		https://github.com/influxdata/influxdb

Source0:	%name-%version.tar

Source100: influxdb.sysconfig
Source101: influxdb.logrotate
Source102: influxdb.init
Source103: influxdb.service
Source104: influxdb.tmpfiles

Patch1: influxdb-opentsdb-fix.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: xmlto asciidoc

%description
InfluxDB is an open source time series database with
no external dependencies. It's useful for recording metrics,
events, and performing analytics.

%prep
%setup -q
%patch1 -p1

%build
# Important!!!
# The %builddir/.gopath created by the hands. It contains the dependencies required for your project.
# This is necessary because the gdm cannot work with the vendor directory and always tries to update
# all dependencies from the external servers. So, we can't use Makefile to compile.
#
# $ go get -d github.com/influxdata/influxdb
# pushd ~/go/src/github.com/influxdata/influxdb
# $ git checkout to %version
# $ dep ensure -vendor-only
# popd
# $ git rm -rf vendor
# $ cp -r ~go/src/github.com/influxdata/influxdb/vendor ./
# $ git add --force vendor
# $ git commit -m "update go pkgs by dep ensure -vendor-only"
# $ rm -rf ~/go/src/github.com/influxdata/influxdb


export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GO111MODULE=off

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

CGO_ENABLED=0 GOGC=off go install -ldflags " -s -w \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.branch=$BRANCH \
    " -a -installsuffix nocgo ./...

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot%_datadir
rm -f %buildroot%_bindir/{stress_test_server,test_client}

# Install config files
install -p -D -m 640 etc/config.sample.toml %buildroot%_sysconfdir/%name/%name.conf
# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/%name
# Install logrotate
install -p -D -m 644 %SOURCE101 %buildroot%_logrotatedir/%name
# Install sysv init scripts
install -p -D -m 644 %SOURCE100 %buildroot%_sysconfdir/sysconfig/%name
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf
# Install man files
%make_install DESTDIR=%buildroot%_prefix -C man install

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'InfluxDB Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/*
%_man1dir/*
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, %name) %_sysconfdir/%name
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_logrotatedir/%name
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0775, root, %name) %_runtimedir/%name
%dir %attr(0755, %name, %name) %_sharedstatedir/%name

%changelog
* Wed Sep 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.8-alt1
- 1.7.8

* Thu Jul 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.7-alt1
- 1.7.7

* Thu Jun 20 2019 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt2
- NMU: fix writing millisecond timestamps through opentsdb (ALT bug 36873)

* Sat Apr 20 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.6-alt1
- 1.7.6
- update sysv  init script for logging to logfile

* Thu Mar 28 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.5-alt1
- 1.7.5

* Wed Feb 27 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.4-alt1
- 1.7.4

* Mon Jan 21 2019 Alexey Shabalin <shaba@altlinux.org> 1.6.5-alt1
- 1.6.5

* Thu Oct 11 2018 Alexey Shabalin <shaba@altlinux.org> 1.6.3-alt1
- 1.6.3

* Thu Jun 21 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.3-alt1%ubt
- 1.5.3

* Sat Apr 28 2018 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1%ubt
- 1.5.2

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt1%ubt
- 1.4.3

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.7-alt1%ubt
- 1.3.7

* Fri Oct 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.6-alt1%ubt
- 1.3.6

* Mon Aug 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1%ubt
- 1.3.4

* Mon Aug 07 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1%ubt
- 1.3.2

* Mon Jul 24 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- First build for ALTLinux.

