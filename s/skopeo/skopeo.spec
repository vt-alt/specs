%global import_path github.com/containers/skopeo
Name: skopeo
Version: 0.1.39
Release: alt1

Summary: skopeo is a command line utility that performs various operations on container images and image repositories
License: Apache-2.0
Group: Other
Url: https://github.com/containers/skopeo

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

Source1: storage.conf
Source2: containers-storage.conf.5.md
Source3: mounts.conf
Source4: registries.conf.5.md
Source5: registries.conf
Source6: policy.json.5.md
Source7: seccomp.json
Source8: containers-transports.5.md
Source9: containers-signature.5.md
Source10: containers-registries.d.5.md
Source11: containers-registries.conf.5.md
Source12: containers-policy.json.5.md
Source13: containers-mounts.conf.5.md
Source14: containers-certs.d.5.md

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-md2man
BuildRequires: glib2-devel libgpgme-devel libbtrfs-devel
BuildRequires: libgio-devel libostree-devel libselinux-devel libdevmapper-devel
BuildRequires: libassuan-devel

%description
Skopeo works with API V2 registries such as Docker registries, the Atomic
registry, private registries, local directories and local OCI-layout
directories. Skopeo does not require a daemon to be running to perform these
operations which consist of:
- Copying an image from and to various storage mechanisms. For example you can
  copy images from one registry to another, without requiring privilege.
- Inspecting a remote image showing its properties including its layers,
  without requiring you to pull the image to the host.
- Deleting an image from an image repository.
- When required by the repository,
  skopeo can pass the appropriate credentials and certificates for
  authentication.

%package -n containers-common
Group:    System/Configuration/Other
Summary: Configuration files for working with image signatures

%description -n containers-common
%summary.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_man1dir
go-md2man -in docs/skopeo.1.md -out %buildroot%_man1dir/skopeo.1
install -Dm 644 completions/bash/%name %buildroot/%_sysconfdir/bash_completion.d/%name

# containers-common files
install -Dm 644 default-policy.json %buildroot%_sysconfdir/containers/policy.json
install -Dm 644 default.yaml %buildroot%_sysconfdir/containers/registries.d/default.yaml

install -Dm 644 %SOURCE1 %buildroot%_sysconfdir/containers/storage.conf
mkdir -p %buildroot%_man5dir
go-md2man -in %SOURCE2 -out %buildroot%_man5dir/containers-storage.conf.5
go-md2man -in %SOURCE4 -out %buildroot%_man5dir/registries.conf.5
install -p -m 644 %SOURCE5 %buildroot%_sysconfdir/containers/
go-md2man -in %SOURCE6 -out %buildroot%_man5dir/policy.json.5
go-md2man -in %SOURCE8 -out %buildroot%_man5dir/containers-transports.5
go-md2man -in %SOURCE9 -out %buildroot%_man5dir/containers-signature.5
go-md2man -in %SOURCE10 -out %buildroot%_man5dir/containers-registries.d.5
go-md2man -in %SOURCE11 -out %buildroot%_man5dir/containers-registries.conf.5
go-md2man -in %SOURCE12 -out %buildroot%_man5dir/containers-policy.json.5
go-md2man -in %SOURCE13 -out %buildroot%_man5dir/containers-mounts.conf.5
go-md2man -in %SOURCE14 -out %buildroot%_man5dir/containers-certs.d.5

mkdir -p %buildroot%_datadir/containers
install -m0644 %SOURCE3 %buildroot%_datadir/containers/mounts.conf
install -m0644 %SOURCE7 %buildroot%_datadir/containers/seccomp.json

%files -n containers-common
%_sysconfdir/containers
%_datadir/containers
%_man5dir/*

%files
%_bindir/*
%_sysconfdir/bash_completion.d/%name
%_man1dir/%{name}*
%doc *.md

%changelog
* Fri Sep 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.39-alt1
- new version 0.1.39

* Tue Jan 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.34-alt1
- Initial build for Sisyphus
