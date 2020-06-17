%global import_path github.com/grafana/grafana
%global commit ef5b586d7d9e561b78c8aaa098c4e9f1e3a78d62

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%define _runtimedir /run

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*


Name:		grafana
Version:	7.0.1
Release:	alt1
Summary:	Metrics dashboard and graph editor

Group:		Development/Other
License:	Apache-2.0
URL:		https://grafana.com

Source: %name-%version.tar
Patch: %name-%version.patch

Source100: %name-server.sysconfig
#Source101: %name.logrotate
Source102: %name-server.init
Source103: %name-server.service
Source104: %name.tmpfiles


ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang rpm-macros-nodejs
BuildRequires: npm yarn
BuildRequires: node node-devel node-gyp node-iltorb node-sass libsass
BuildRequires: fontconfig libfreetype
BuildRequires: /proc

%description
Grafana is an open source, feature rich metrics dashboard and graph editor
for Graphite, Elasticsearch, OpenTSDB, Prometheus and InfluxDB.

%prep
# Build the Front-end Assets
# $ npm install yarn
# $ ./node_modules/.bin/yarn install --pure-lockfile
# $ npm run build
# $ rm -rf node_modules/iltorb
# $ rm -rf node_modules/node-sass
# $ rm -rf node_modules/node-gyp
# $ git add -f node_modules
# $ git add -f packages/grafana-*/node_modules
# $ git commit -n --no-post-rewrite -m "add node js modules"

%setup -q
%patch -p1

# add symlink to node headers
node_ver=$(node -v | sed -e "s/v//")
mkdir -p node_modules/.node-gyp/$node_ver/include
ln -s %_includedir/node node_modules/.node-gyp/$node_ver/include/node
echo "9" > node_modules/.node-gyp/$node_ver/installVersion

ln -sf %nodejs_sitelib/node-gyp node_modules/node-gyp
ln -sf %nodejs_sitelib/node-sass node_modules/node-sass
ln -sf %nodejs_sitelib/iltorb node_modules/iltorb

%build

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export npm_config_devdir="$PWD/node_modules/.node-gyp"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

#npm rebuild
#npm run build
go run build.go build-frontend

#GO111MODULE=off CGO_ENABLED=1 go run build.go build
#%%golang_build pkg/cmd/*
CGO_ENABLED=1 go install -ldflags " -s -w  \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.buildBranch=$BRANCH \
    " -a ./pkg/cmd/grafana-server

CGO_ENABLED=1 go install -ldflags " -s -w  \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.buildBranch=$BRANCH \
    " -a ./pkg/cmd/grafana-cli

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"
export GOFLAGS="-mod=vendor"

pushd .gopath/src/%import_path
# Install Front-end Assets
install -d -m 755 %buildroot%_datadir/%name
cp -pr conf %buildroot%_datadir/%name/
cp -pr public %buildroot%_datadir/%name/
%golang_install
popd

rm -rf -- %buildroot/usr/src
rm -f -- %buildroot%_bindir/govendor
rm -f -- %buildroot%_bindir/release_publisher
rm -f -- %buildroot%_bindir/slow_proxy
#TODO: package alert_webhook_listener
rm -f -- %buildroot%_bindir/alert_webhook_listener

# Install config files
install -p -D -m 640 conf/sample.ini %buildroot%_sysconfdir/%name/%name.ini
install -p -D -m 640 conf/ldap.toml %buildroot%_sysconfdir/%name/ldap.toml
mkdir -p %buildroot%_sysconfdir/%name/provisioning/{dashboards,datasources,notifiers}
install -p -D -m 640 conf/provisioning/dashboards/sample.yaml %buildroot%_sysconfdir/%name/provisioning/dashboards/sample.yaml
install -p -D -m 640 conf/provisioning/datasources/sample.yaml %buildroot%_sysconfdir/%name/provisioning/datasources/sample.yaml
install -p -D -m 640 conf/provisioning/notifiers/sample.yaml %buildroot%_sysconfdir/%name/provisioning/notifiers/sample.yaml

# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 750 %buildroot%_sharedstatedir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name/plugins
# Install pid directory
install -d -m 775 %buildroot%_runtimedir/%name
# Install sysconfig
install -p -D -m 644 %SOURCE100 %buildroot%_sysconfdir/sysconfig/%name-server
# Install logrotate
#install -p -D -m 644 %%SOURCE101 %buildroot%_logrotatedir/%name
# Install sysv init scripts
install -p -D -m 755 %SOURCE102 %buildroot%_initdir/%name-server
# Install systemd unit services
install -p -D -m 644 %SOURCE103 %buildroot%_unitdir/%name-server.service
install -p -D -m 644 %SOURCE104 %buildroot%_tmpfilesdir/%name.conf

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name  -c 'Grafana Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name-server
# create grafana.db with secure permissions on new installations
# otherwise grafana-server is creating grafana.db on first start
# with world-readable permissions, which may leak encrypted datasource
# passwords to all users (if the secret_key in grafana.ini was not changed)
if [ "$1" = 1 ] && [ ! -f %_sharedstatedir/%name/grafana.db ]; then
    touch %_sharedstatedir/%name/grafana.db
fi
 
# apply secure permissions to grafana.db if it exists
# (may not exist on upgrades, because users can choose between sqlite/mysql/postgres)
if [ -f %_sharedstatedir/%name/grafana.db ]; then
    chown %name:%name %_sharedstatedir/%name/grafana.db
    chmod 640 %_sharedstatedir/%name/grafana.db
fi

%preun
%preun_service %name-server

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/%name-cli
%_bindir/%name-server
%config(noreplace) %_sysconfdir/sysconfig/%name-server
%_initdir/%name-server
%_unitdir/%name-server.service
%_tmpfilesdir/%name.conf
%dir %attr(0750, root, %name) %_sysconfdir/%name
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning/dashboards
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning/datasources
%dir %attr(0750, root, %name) %_sysconfdir/%name/provisioning/notifiers
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.ini
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/ldap.toml
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/provisioning/*/*.yaml
#%config(noreplace) %_logrotatedir/%name
%dir %attr(0775, root, %name) %_logdir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name
%dir %attr(0755, %name, %name) %dir %_sharedstatedir/%name/plugins
%_datadir/%name

%changelog
* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 7.0.1-alt1
- 7.0.1

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 6.7.3-alt1
- 6.7.3
- create grafana.db on first installation
- change permissions of /var/lib/grafana to 750 (Fixes: CVE-2020-12458)
- change permissions of /var/lib/grafana/grafana.db to 640 and
  user/group grafana:grafana (CVE-2020-12458)

* Mon Mar 02 2020 Alexey Shabalin <shaba@altlinux.org> 6.6.2-alt1
- 6.6.2

* Sat Sep 07 2019 Alexey Shabalin <shaba@altlinux.org> 6.3.5-alt2
- fixed perm of /run/grafana in tmpfiles config
- not package /run/grafana

* Thu Sep 05 2019 Alexey Shabalin <shaba@altlinux.org> 6.3.5-alt1
- 6.3.5

* Fri Aug 30 2019 Alexey Shabalin <shaba@altlinux.org> 6.3.4-alt1
- 6.3.4 (Fixes: CVE-2019-15043)

* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 6.3.2-alt1
- 6.3.2

* Fri Jul 19 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.5-alt2
- build for all arches

* Fri Jul 12 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.5-alt1
- 6.2.5

* Thu Mar 28 2019 Alexey Shabalin <shaba@altlinux.org> 6.0.2-alt1
- 6.0.2

* Fri Mar 01 2019 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt2
- fix show version in webui
- change runtimedir from /var/run/grafana to /run/grafana

* Wed Feb 27 2019 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt1
- 6.0.0

* Wed Jan 23 2019 Alexey Shabalin <shaba@altlinux.org> 5.4.3-alt1
- 5.4.3

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 5.4.2-alt1
- 5.4.2

* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 5.3.0-alt1
- 5.3.0

* Thu Jun 21 2018 Alexey Shabalin <shaba@altlinux.ru> 5.1.4-alt2%ubt
- update init script and systemd unit
- fix package files and config

* Wed Jun 20 2018 Alexey Shabalin <shaba@altlinux.ru> 5.1.4-alt1%ubt
- 5.1.4

* Wed Feb 14 2018 Alexey Shabalin <shaba@altlinux.ru> 4.6.3-alt1%ubt
- 4.6.3

* Mon Dec 04 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.2-alt1%ubt
- 4.6.2

* Mon Oct 30 2017 Alexey Shabalin <shaba@altlinux.ru> 4.6.0-alt1%ubt
- 4.6.0

* Fri Oct 13 2017 Alexey Shabalin <shaba@altlinux.ru> 4.5.2-alt1%ubt
- 4.5.2

* Mon Aug 28 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt2%ubt
- fix start options for systemd and sysvinit

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.3-alt1%ubt
- 4.4.3
- fix pidfile path in systemd unit
- fix run with sysv init script

* Tue Aug 01 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.2-alt1
- 4.4.2
- fix systemd unit
- rm phantomjs blob

* Thu Jul 27 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt2
- fix service name in post and preun

* Tue Jul 25 2017 Alexey Shabalin <shaba@altlinux.ru> 4.4.1-alt1
- First build for ALTLinux.
