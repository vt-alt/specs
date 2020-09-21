%global provider        github
%global provider_tld    com
%global project         containers
%global repo            buildah
# https://github.com/containers/buildah
%global provider_prefix %provider.%provider_tld/%project/%repo
%global import_path     %provider_prefix
%global commit          0e6d94679ebddd0f2461078cfaee6ea564672684
%global shortcommit    %(c=%commit; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: buildah
# Bump version in buildah.go too
Version: 1.16.1
Release: alt2
Summary: A command line tool used to creating OCI Images
Group: Development/Other
License: Apache-2.0
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
Requires: runc >= 1.0.0
Requires: containers-common
Requires: slirp4netns >= 0.3
Requires: tzdata

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
export GIT_COMMIT=%commit
export BRANCH=altlinux
export GOMD2MAN=go-md2man

%golang_prepare
pushd .gopath/src/%import_path
#%%golang_build cmd/%name
%make_build all PREFIX=%_prefix
popd

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"

pushd .gopath/src/%import_path
#%%golang_install
# rm -rf -- %buildroot%_datadir
%make DESTDIR=%buildroot PREFIX=%prefix install
%make DESTDIR=%buildroot PREFIX=%prefix install.completions
%make DESTDIR=%buildroot PREFIX=%prefix -C docs install
popd

%files
%doc LICENSE
%doc README.md
%_bindir/%name
%_man1dir/buildah*
%_datadir/bash-completion/completions/*

%changelog
* Sat Sep 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt2
- add tzdata to Requires

* Thu Sep 17 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.1-alt1
- new version 1.16.1
- Add(): fix handling of relative paths with no ContextDir

* Wed Sep 09 2020 Alexey Shabalin <shaba@altlinux.org> 1.16.0-alt1
- new version 1.16.0

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt1
- new version 1.15.0

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.9-alt1
- new version 1.14.9

* Fri May 01 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.8-alt1
- new version 1.14.8

* Thu Apr 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.5-alt1
- new version 1.14.5 (Fixes: CVE-2020-10696)

* Wed Mar 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.3-alt1
- new version 1.14.3

* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 1.14.0-alt1
- 1.14.0

* Tue Jan 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.1-alt1
- 1.13.1

* Sun Dec 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.0-alt1
- 1.12.0

* Wed Dec 11 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.6-alt1
- 1.11.6

* Mon Oct 07 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.3-alt1
- 1.11.3

* Sun Sep 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1
- Initial build for ALT

