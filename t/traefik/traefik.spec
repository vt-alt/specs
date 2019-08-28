%global import_path github.com/containous/traefik
%global commit c443902a0f01da4cb844bcc8421816f105e4894dc

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: traefik
Version: 1.7.14
Release: alt1
Summary: The Cloud Native Edge Router

License: MIT
Group: System/Servers
Url: https://traefik.io/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: go-bindata
BuildRequires: npm yarn
BuildRequires: node node-devel

%description
Traefik listens to your service registry/orchestrator API and instantly
generates the routes so your microservices are connected to the outside
world -- without further intervention from your part.

Traefik is a modern HTTP reverse proxy and load balancer that makes
deploying microservices easy. Traefik integrates with your existing
infrastructure components (Docker, Swarm mode, Kubernetes, Marathon,
Consul, Etcd, Rancher, Amazon ECS, ...) and configures itself
automatically and dynamically.

Pointing Traefik at your orchestrator should be the only configuration
step you need.

Documentation: http://docs.traefik.io/

%prep
# Build the Front-end Assets
# $ cd webui
# $ git rm -r node_modules
# $ yarn install --pure-lockfile
# $ npm run build
# $ git add -f node_modules
# $ git commit -n --no-post-rewrite -m "add node js modules"

%setup
%patch -p1

# add symlink to node headers
node_ver=$(node -v | sed -e "s/v//")
mkdir -p webui/node_modules/.node-gyp/$node_ver/include
ln -s %_includedir/node webui/node_modules/.node-gyp/$node_ver/include/node
echo "9" > webui/node_modules/.node-gyp/$node_ver/installVersion


%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export PATH="$PATH:$PWD/webui/node_modules/.bin"
export npm_config_devdir="$PWD/webui/node_modules/.node-gyp"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux
export CODENAME=cheddar
export DATE=$(date -u '+%Y-%m-%d')

pushd webui
npm rebuild
npm run build
popd

mkdir -p dist

go generate
CGO_ENABLED=0 GOGC=off go build -ldflags " -s -w  \
    -X github.com/containous/traefik/version.Version=$VERSION \
    -X github.com/containous/traefik/version.Codename=$CODENAME \
    -X github.com/containous/traefik/version.BuildDate=$DATE \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.branch=$BRANCH \
    " -a -installsuffix nocgo -o dist/traefik ./cmd/traefik

%install
install -p -D -m 0755 .gopath/src/%import_path/dist/traefik %buildroot%_bindir/%name
install -p -D -m 0644 contrib/systemd/traefik.service %buildroot%_unitdir/%name.service
install -d -m 750 %buildroot%_sysconfdir/%name
install -d -m 750 %buildroot%_sysconfdir/%name/%name.d
touch %buildroot%_sysconfdir/%name/acme.json
install -p -D -m 0644 traefik.sample.toml %buildroot%_sysconfdir/%name/%name.toml
# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name
# Install logrotate
#install -p -D -m 644 %%SOURCE10 %buildroot%_logrotatedir/%name

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name -c 'Traefik reverse proxy and load balancer daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:
%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE.md
%_bindir/%name
%dir %attr(750, root, %name) %_sysconfdir/%name
%dir %attr(750, root, %name) %_sysconfdir/%name/%name.d
%config(noreplace) %attr(640, root, %name) %_sysconfdir/%name/traefik.toml
%config(noreplace) %attr(660, root, %name) %_sysconfdir/%name/acme.json
%_unitdir/%name.service
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name

%changelog
* Fri Aug 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.14-alt1
- 1.7.14
- build with golang-1.12.9 (Fixes: CVE-2019-9512, CVE-2019-9514)

* Tue May 07 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.11-alt1
- 1.7.11

* Fri Mar 29 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.10-alt1
- 1.7.10

* Thu Feb 28 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.9-alt2
- build webui
- update sample config
- listen api entryPoint on localhost by default for security reason
- update systemd unit

* Mon Feb 25 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.9-alt1
- Initial build

