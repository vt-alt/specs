%global import_path github.com/minio/minio
%global commit 0d057c777ad62d9f612a605689b0d8ab544cf325
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global tag RELEASE.2021-02-07T01-31-02Z
%define version 2021.02.07

%global _unpackaged_files_terminate_build 1

Name: minio
Version: %version
Release: alt1
Summary: Cloud Storage Server
Group: System/Servers
License: Apache-2.0
Url: https://www.min.io/

Source: %name-%version.tar
Source2: %name.config
Source3: %name.sysconfig
Source4: %name.service

Patch: %name-%version.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

%description
MinIO is an object storage server released under Apache License v2.0.
It is compatible with Amazon S3 cloud storage service. It is best
suited for storing unstructured data such as photos, videos, log
files, backups and container / VM images. Size of an object can
range from a few KBs to a maximum of 5TiB.

%prep
%setup -q
%patch -p1


%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export TAG=%tag
export VERSION=${TAG#RELEASE.}
export COMMIT=%commit
export SCOMMIT=%shortcommit
export prefix=%import_path/cmd

# setup flags like 'go run buildscripts/gen-ldflags.go' would do
export LDFLAGS="-X $prefix.Version=$VERSION -X $prefix.ReleaseTag=$TAG -X $prefix.CommitID=$COMMIT -X $prefix.ShortCommitID=$SCOMMIT"
export TAGS="kqueue"

sed -e "s|DEVELOPMENT.GOGET|$VERSION|g" -i cmd/build-constants.go

%golang_prepare
cd .gopath/src/%import_path
CGO_ENABLED=0 %gobuild -tags kqueue -trimpath -o %name .
#CGO_ENABLED=0 %golang_build .

%install
export BUILDDIR="$PWD/.gopath"
mkdir -p -- \
        %buildroot%_bindir \
        %buildroot%_unitdir \
        %buildroot%_sysconfdir/%name \
        %buildroot%_sharedstatedir/%name \
        %buildroot%_logdir/%name

cd .gopath/src/%import_path
install -p -m 755 %name %buildroot%_bindir/%name
install -D -p -m 0644 %SOURCE2 %buildroot%_sysconfdir/%name/config.json
install -D -p -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -D -p -m 0644 %SOURCE4 %buildroot%_unitdir/%name.service

%pre
groupadd -r -f _%name
useradd -r -g _%name -c "Minio" -d %_sharedstatedir/%name -s /dev/null -n _%name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md
%_bindir/minio
%dir %attr(750,_%name,_%name) %_sysconfdir/%name
%config(noreplace) %attr(750,_%name,_%name) %_sysconfdir/%name/config.json
%config(noreplace) %attr(750,root,_%name) %_sysconfdir/sysconfig/%name
%dir %attr(750,_%name,_%name) %_sharedstatedir/%name
%dir %attr(750,_%name,_%name) %_logdir/%name
%_unitdir/%name.service

%changelog
* Mon Feb 08 2021 Alexey Shabalin <shaba@altlinux.org> 2021.02.07-alt1
- Update to RELEASE.2021-02-07T01-31-02Z

* Sun Oct 25 2020 Alexey Shabalin <shaba@altlinux.org> 2020.10.18-alt1
- Update to RELEASE.2020-10-18T21-54-12Z

* Mon Aug 17 2020 Alexey Shabalin <shaba@altlinux.org> 2020.08.16-alt1
- Update to RELEASE.2020-08-16T18-39-38Z

* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 2020.06.22-alt1
- Update to RELEASE.2020-06-22T03-12-50Z

* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 2020.05.28-alt1
- Update to RELEASE.2020-05-28T23-29-21Z

* Wed Apr 29 2020 Alexey Shabalin <shaba@altlinux.org> 2020.04.28-alt1
- Update to RELEASE.2020-04-28T23-56-56Z.

* Tue Apr 28 2020 Alexey Shabalin <shaba@altlinux.org> 2020.04.23-alt1
- Initial build.
