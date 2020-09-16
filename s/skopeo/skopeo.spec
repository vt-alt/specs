%global import_path github.com/containers/skopeo
%global commit 67abbb3cefbdc876447583d5ea45e76bf441eba7

%global _unpackaged_files_terminate_build 1

Name: skopeo
Version: 1.1.1
Release: alt1

Summary: skopeo is a command line utility that performs various operations on container images and image repositories
License: Apache-2.0
Group: Other
Url: https://github.com/containers/skopeo

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

# The following files stored at https://src.fedoraproject.org/rpms/skopeo/tree/master
Source1: storage.conf
Source2: containers-storage.conf.5.md
Source3: mounts.conf
Source4: containers-registries.conf.5.md
Source5: registries.conf
Source6: containers-policy.json.5.md
Source7: seccomp.json
Source8: containers-mounts.conf.5.md
Source9: containers-signature.5.md
Source10: containers-transports.5.md
Source11: containers-certs.d.5.md
Source12: containers-registries.d.5.md
Source13: containers.conf
Source14: containers.conf.5.md
Source15: containers-auth.json.5.md
Source16: containers-registries.conf.d.5.md

Patch100: 0001--buildmodepie-is-not-supported-for-some-arch.patch

ExclusiveArch: %go_arches
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
%patch100 -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export GIT_COMMIT=%commit

%golang_prepare

pushd .gopath/src/%import_path
#%%golang_build cmd/%name
%make_build binary-local

for doc in $(find docs -name '*.1.md'); do
    go-md2man -in "$doc" -out "docs/$(basename "${doc%%.md}")"
done

popd

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"
# export IGNORE_SOURCES=1
#%%golang_install
pushd .gopath/src/%import_path
%make DESTDIR=%buildroot install
popd

install -dp %buildroot%_sysconfdir/containers/{certs.d,oci/hooks.d}
install -m0644 %SOURCE1 %buildroot%_sysconfdir/containers/storage.conf
install -m0644 %SOURCE5 %buildroot%_sysconfdir/containers/registries.conf
mkdir -p %buildroot%_man5dir
go-md2man -in %SOURCE2 -out %buildroot%_man5dir/containers-storage.conf.5
go-md2man -in %SOURCE4 -out %buildroot%_man5dir/containers-registries.conf.5
go-md2man -in %SOURCE6 -out %buildroot%_man5dir/containers-policy.json.5
go-md2man -in %SOURCE8 -out %buildroot%_man5dir/containers-mounts.conf.5
go-md2man -in %SOURCE9 -out %buildroot%_man5dir/containers-signature.5
go-md2man -in %SOURCE10 -out %buildroot%_man5dir/containers-transports.5
go-md2man -in %SOURCE11 -out %buildroot%_man5dir/containers-certs.d.5
go-md2man -in %SOURCE12 -out %buildroot%_man5dir/containers-registries.d.5
go-md2man -in %SOURCE14 -out %buildroot%_man5dir/containers.conf.5
go-md2man -in %SOURCE15 -out %buildroot%_man5dir/containers-auth.json.5
go-md2man -in %SOURCE16 -out %buildroot%_man5dir/containers-registries.conf.d.5

mkdir -p %buildroot%_datadir/containers
install -m0644 %SOURCE3 %buildroot%_datadir/containers/mounts.conf
install -m0644 %SOURCE7 %buildroot%_datadir/containers/seccomp.json
install -m0644 %SOURCE13 %buildroot%_datadir/containers/containers.conf

%files -n containers-common
%config(noreplace) %_sysconfdir/containers
%_datadir/containers
%_man5dir/*

%files
%_bindir/*
%_datadir/bash-completion/completions/%name
%_man1dir/%{name}*
%doc *.md

%changelog
* Wed Sep 09 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Wed May 13 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.0-alt1
- new version 0.2.0

* Mon Mar 23 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.41-alt2
- Change registries search order

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.41-alt1
- new version 0.1.41

* Fri Sep 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.39-alt1
- new version 0.1.39

* Tue Jan 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.34-alt1
- Initial build for Sisyphus
