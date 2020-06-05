%global import_path github.com/VictoriaMetrics/VictoriaMetrics
%global commit 0ec43cb8b019359b0e3ead38eb39d3472967bd45

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: victoriametrics
Version: 1.36.2
Release: alt1
Summary: The best long-term remote storage for Prometheus

Group: Development/Other
License: Apache-2.0
Url: https://victoriametrics.com/
Source0: %name-%version.tar
Source2: %name.service

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64
BuildRequires(pre): rpm-build-golang

%description
VictoriaMetrics - the best long-term remote storage for Prometheus

%package utils
Summary: Utils for %name
Group: Development/Other
Provides: vmutils = %EVR

%description utils
Utils for VictoriaMetrics:
 * vmagent is a tiny but brave agent,
   which helps you collecting metrics from various sources
   and storing them to VictoriaMetrics or any other Prometheus-compatible
   storage system that supports remote_write protocol.
 * vmbackup - creates VictoriaMetrics data backups
 * vmrestore - restores data from backups

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux
export BUILDINFO_TAG=v%version

make \
    victoria-metrics \
	vmagent \
	vmbackup \
	vmrestore

%install
install -m 0755 -d %buildroot%_bindir
#cp victoria-metrics-prod %buildroot%_bindir/victoria-metrics-prod
cd .gopath/src/%import_path
install -m 0755 bin/victoria-metrics %buildroot%_bindir/victoria-metrics
install -m 0755 bin/vmagent %buildroot%_bindir/vmagent
install -m 0755 bin/vmbackup %buildroot%_bindir/vmbackup
install -m 0755 bin/vmrestore %buildroot%_bindir/vmrestore

install -m 0755 -d %buildroot%_sharedstatedir/victoria-metrics-data

mkdir -p %buildroot%_unitdir
install -m644 %SOURCE2 \
    %buildroot%_unitdir/%name.service

%pre
%_sbindir/groupadd -r -f _%name 2>/dev/null ||:
%_sbindir/useradd -r -g _%name -c 'Victoria Metrics Daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/victoria-metrics-data _%name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_bindir/victoria-metrics
%dir %attr(0755, _%name, _%name) %_sharedstatedir/victoria-metrics-data
%_unitdir/%name.service

%files utils
%_bindir/vm*

%changelog
* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 1.36.2-alt1
- 1.36.2.

* Mon Apr 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.34.9-alt1
- Initial build.

