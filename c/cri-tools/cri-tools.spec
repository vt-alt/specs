%global import_path github.com/kubernetes-incubator/cri-tools

%global _unpackaged_files_terminate_build 1

Name:     cri-tools
Version:  1.19.0
Release:  alt1

Summary:  CLI and validation tools for Kubelet Container Runtime Interface (CRI)
License:  Apache-2.0
Group:    Other
Url:      https://github.com/kubernetes-incubator/cri-tools

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: /usr/bin/go-md2man
# For creating completion
BuildRequires: /proc

%description
CLI and validation tools for Kubelet Container Runtime Interface (CRI).

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

for doc in docs/*.md; do
    go-md2man -in "$doc" -out "${doc%%md}"1
done
pushd .build/src/%import_path
%golang_build cmd/crictl
go test -buildmode=pie -o $BUILDDIR/bin/critest -c "$PWD"/cmd/critest
popd

$BUILDDIR/bin/crictl completion > crictl-bash-completion

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dpm 644 docs/*.1 -t %buildroot/%_man1dir
rm docs/*.1
install -Dpm 644 crictl-bash-completion -T %buildroot/%_datadir/bash-completion/completions/crictl

%files
%_bindir/crictl
%_bindir/critest
%_datadir/bash-completion/completions/crictl
%doc %_man1dir/*
%doc docs

%changelog
* Thu Sep 17 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.19.0-alt1
- new version 1.19.0

* Thu Aug 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.1-alt1
- Initial build for Sisyphus
