%global import_path github.com/minio/mc
%global commit c44387cb3203700425fa0c576bf574798245d0d1
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global tag RELEASE.2021-02-07T02-02-05Z
%define version 2021.02.07

%global _unpackaged_files_terminate_build 1

Name: minio-mc
Version: %version
Release: alt1
Summary: Minio Client for filesystems and object storage
Group: File tools
License: Apache-2.0
Url: https://www.min.io/

Source: %name-%version.tar

Patch: %name-%version.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

%description
MinIO Client (mc) provides a modern alternative to UNIX commands
like ls, cat, cp, mirror, diff, find etc.
It supports filesystems and Amazon S3 compatible cloud storage service (AWS Signature v2 and v4).

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
        %buildroot%_bindir

cd .gopath/src/%import_path
install -p -m 755 %name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Feb 08 2021 Alexey Shabalin <shaba@altlinux.org> 2021.02.07-alt1
- Update to RELEASE.2021-02-07T02-02-05Z

* Sun Oct 25 2020 Alexey Shabalin <shaba@altlinux.org> 2020.10.03-alt1
- Update to RELEASE.2020-10-03T02-54-56Z

* Mon Aug 17 2020 Alexey Shabalin <shaba@altlinux.org> 2020.08.08-alt1
- Update to RELEASE.2020-08-08T02-33-58Z

* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 2020.06.26-alt1
- Update to RELEASE.2020-06-26T19-56-55Z

* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 2020.05.28-alt1
- Update to RELEASE.2020-05-28T23-43-36Z

* Wed Apr 29 2020 Alexey Shabalin <shaba@altlinux.org> 2020.04.25-alt1
- Initial build.
