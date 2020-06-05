%global import_path github.com/VictoriaMetrics/vmctl
%global commit 69bb0024a7e3ec3d7d74656bf7d6b99553356694

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: victoriametrics-vmctl
Version: 0.0.2
Release: alt1
Summary: Victoria metrics command-line tool

Group: Development/Other
License: Apache-2.0
Url: https://victoriametrics.com/
Source0: %name-%version.tar
Provides: vmctl = %EVR

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

%description
VictoriaMetrics - the best long-term remote storage for Prometheus
vmctl - Victoria metrics command-line tool

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

make build

%install
install -m 0755 -d %buildroot%_bindir
cd .gopath/src/%import_path
install -m 0755 bin/vmctl %buildroot%_bindir/vmctl

%files
%_bindir/vmctl

%changelog
* Tue Apr 21 2020 Alexey Shabalin <shaba@altlinux.org> 0.0.2-alt1
- Initial build.
