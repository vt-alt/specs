%global import_path github.com/ansible-semaphore/semaphore
Name:     semaphore
Version:  2.5.1
Release:  alt2

Summary:  Open Source alternative to Ansible Tower
License:  MIT
Group:    Other
Url:      https://github.com/ansible-semaphore/semaphore

ExclusiveArch: %go_arches

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

# next commands need to prepare sources
# apt-get install go-task packr
# go mod vendor
# task deps:fe
# rm web/package-lock.json
# task compile

# this command is need to build source
# task build:local
%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cli

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
mv %buildroot%_bindir/{cli,%name}

%files
%_bindir/%name
%doc README.ALT
%doc *.md

%changelog
* Tue Sep 03 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.1-alt2
- Set ExclusiveArch to %%go_arches

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.1-alt1
- Update to 2.5.1

* Thu May 10 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus
