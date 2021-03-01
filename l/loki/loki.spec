%global import_path github.com/grafana/loki
%global _unpackaged_files_terminate_build 1

Name: loki
Version: 2.1.0
Release: alt1
Summary: Loki: like Prometheus, but for logs
License: Apache-2.0
Group: Monitoring
Url: https://grafana.com/loki
Source: %name-%version.tar
Source1: loki.service
Source2: promtail.service
Source3: loki.sysconfig
Source4: promtail.sysconfig
Source5: loki.yaml
Source6: promtail.yaml

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: systemd-devel

%description
Loki is a horizontally-scalable, highly-available, multi-tenant log aggregation
system inspired by Prometheus.

%package -n promtail
Summary: Promtail is an agent which ships the contents of local logs to a Loki instance
Group: Monitoring
Provides: %name-promtail = %EVR

%description -n promtail
Promtail is an agent which ships the contents of local logs to a private Loki instance or Grafana Cloud.
It is usually deployed to every machine that has applications needed to be monitored.

It primarily:
- Discovers targets
- Attaches labels to log streams
- Pushes them to the Loki instance.

Currently, Promtail can tail logs from two sources: local log files and the systemd journal

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%define buildpkg github.com/grafana/loki/pkg/build
export CGO_ENABLED=0
export GOFLAGS="-mod=vendor -buildmode=pie -tags=netgo"
export DATE=$(date -u '+%%Y-%%m-%%d')
export GOLDFLAGS="-s -w -X %buildpkg.Version=%version \
                        -X %buildpkg.Revision=%release \
                        -X %buildpkg.Branch=master \
                        -X %buildpkg.BuildUser=alt \
                        -X %buildpkg.BuildDate=$DATE"

go build -ldflags="$GOLDFLAGS" ./cmd/loki
go build -ldflags="$GOLDFLAGS" ./cmd/logcli
CGO_ENABLED=1 go build -ldflags="$GOLDFLAGS" ./cmd/promtail

%install
# Service files for Loki and promtail
install -Dm644 %SOURCE1 %buildroot%_unitdir/loki.service
install -Dm644 %SOURCE2 %buildroot%_unitdir/promtail.service
install -Dm644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/loki
install -Dm644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/promtail

# Config files
install -Dm644 %SOURCE5 %buildroot%_sysconfdir/loki/loki.yaml
install -Dm644 %SOURCE6 %buildroot%_sysconfdir/loki/promtail.yaml

# Binaries
install -dm755 %buildroot%_bindir
install -Dm755 loki %buildroot%_bindir
install -Dm755 promtail %buildroot%_bindir
install -Dm755 logcli %buildroot%_bindir

mkdir -p %buildroot%_sharedstatedir/{loki,promtail}

%pre
groupadd -r -f _loki 2>/dev/null ||:
useradd -r -N -g _loki -c 'Loki log aggregator' \
        -s /sbin/nologin -M -d %_sharedstatedir/loki _loki 2>/dev/null ||:

%pre -n promtail
groupadd -r -f _promtail 2>/dev/null ||:
useradd -r -N -g _promtail -G systemd-journal -c 'Promtail log collector' \
        -s /sbin/nologin -M -d %_sharedstatedir/promtail _promtail 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%post -n promtail
%post_service promtail

%preun -n promtail
%preun_service promtail

%files
%doc LICENSE README.md
%_bindir/loki
%_bindir/logcli
%_unitdir/loki.service
%dir %_sysconfdir/loki
%attr(0640,root,_loki) %config(noreplace) %_sysconfdir/loki/loki.yaml
%config(noreplace) %_sysconfdir/sysconfig/loki
%attr(0770,root,_loki) %_sharedstatedir/loki

%files -n promtail
%_bindir/promtail
%_unitdir/promtail.service
%dir %_sysconfdir/loki
%attr(0640,root,_promtail) %config(noreplace) %_sysconfdir/loki/promtail.yaml
%config(noreplace) %_sysconfdir/sysconfig/promtail
%attr(0770,root,_promtail) %_sharedstatedir/promtail

%changelog
* Sat Feb 20 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- Initial build

