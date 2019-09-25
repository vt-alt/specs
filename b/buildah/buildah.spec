%global provider        github
%global provider_tld    com
%global project         containers
%global repo            buildah
# https://github.com/containers/buildah
%global provider_prefix %provider.%provider_tld/%project/%repo
%global import_path     %provider_prefix
%global commit         0bafbfe9cb10a177509622010220fd1fc6027f16
%global shortcommit    %(c=%commit; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: buildah
# Bump version in buildah.go too
Version: 1.11.2
Release: alt1
Summary: A command line tool used to creating OCI Images
Group: Development/Other
License: ASL 2.0
Url: https://%provider_prefix
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: go-md2man
BuildRequires: libgpgme-devel
BuildRequires: libdevmapper-devel
BuildRequires: libbtrfs-devel
BuildRequires: libassuan-devel
BuildRequires: libseccomp-devel
BuildRequires: glib2-devel
BuildRequires: libostree-devel
Requires: runc >= 1.0.0
Requires: containers-common
Requires: slirp4netns >= 0.3

%description
The buildah package provides a command line tool which can be used to
* create a working container from scratch
or
* create a working container from an image as a starting point
* mount/umount a working container's root file system for manipulation
* save container's root file system layer to create a new image
* delete a working container or an image

%prep
%setup
%patch -p1
sed -i '/docs install/d' Makefile

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export VERSION=%version
export COMMIT=%commit
export BRANCH=altlinux

%golang_prepare
pushd .gopath/src/%import_path
%golang_build cmd/%name
popd

GOMD2MAN=go-md2man %make -C docs

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

%golang_install
rm -rf -- %buildroot%_datadir
%make DESTDIR=%buildroot PREFIX=%prefix install.completions
%make DESTDIR=%buildroot PREFIX=%prefix -C docs install

%files
%doc LICENSE
%doc README.md
%_bindir/%name
%_man1dir/buildah*
%_datadir/bash-completion/completions/*

%changelog
* Sun Sep 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1
- Initial build for ALT

