%define _unpackaged_files_terminate_build 1
%global import_path k8s.io/helm
Name:     helm
Version:  3.1.2
Release:  alt1

Summary:  The Kubernetes Package Manager
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/helm/helm

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Helm is a tool for managing Kubernetes charts. Charts are packages of
pre-configured Kubernetes resources.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="\
    -X k8s.io/helm/pkg/version.Version=%version \
    -X k8s.io/helm/pkg/version.BuildMetadata= \
    -X k8s.io/helm/pkg/version.GitCommit=2e55dbe1fdb5fdb96b75ff144a339489417b146b \
    -X k8s.io/helm/pkg/version.GitTreeState=clean \
    $LDFLAGS \
"

%golang_prepare

pushd "$BUILDDIR"/src/%import_path
%golang_build cmd/helm
popd
"$BUILDDIR"/bin/helm completion bash > helm-bash-completion
"$BUILDDIR"/bin/helm completion zsh > helm-zsh-completion

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dm 644 helm-zsh-completion %buildroot/%_datadir/zsh/site-functions/_%name
install -Dm 644 helm-bash-completion %buildroot/%_sysconfdir/bash_completion.d/%name

%files
%doc README.md
%_bindir/%name
%_datadir/zsh/site-functions/_%name
%_sysconfdir/bash_completion.d/%name

%changelog
* Fri Mar 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.1.2-alt1
- new version 3.1.2

* Wed Oct 03 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.11.0-alt1
- Initial build for Sisyphus
