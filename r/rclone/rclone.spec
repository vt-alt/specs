# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%global import_path github.com/ncw/rclone
Name:     rclone
Version:  1.53.4
Release:  alt1

Summary:  rsync for cloud storage
License:  MIT
Group:    Networking/File transfer
Vcs:      https://github.com/ncw/rclone
Url:      https://rclone.org/

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): banner
BuildRequires: golang

%description
Rclone ("rsync for cloud storage") is a command line program to sync files and
directories to and from different cloud storage providers.

Google Drive, Amazon Drive, S3, Dropbox, Backblaze B2, One Drive, Swift, Hubic,
Cloudfiles, Google Cloud Storage, Yandex Files.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
banner tests
PATH=%buildroot%_bindir:$PATH
# Simplest
rclone version
# Some complicated algorithms
> /tmp/empty
rclone md5sum /tmp/empty	| grep -w d41d8cd98f00b204e9800998ecf8427e
rclone sha1sum /tmp/empty	| grep -w da39a3ee5e6b4b0d3255bfef95601890afd80709
rclone hashsum SHA-1 /tmp/empty	| grep -w da39a3ee5e6b4b0d3255bfef95601890afd80709
rclone hashsum MailruHash /tmp/empty | grep -w 0000000000000000000000000000000000000000
rclone hashsum CRC-32 /tmp/empty| grep -w 00000000
# Basic commands
rclone about .
rclone lsd .
rclone check . .		# positive
! rclone check . .. 2>/dev/null	# netagive
# Remote protocol and remote control
rclone --rc serve webdav --read-only . &
trap "kill $!" EXIT
sleep 1
rclone --webdav-url=http://127.0.0.1:8080/ check :webdav: .
rclone --webdav-url=http://127.0.0.1:8080/ copy :webdav:COPYING /tmp/
rclone rc core/stats
rclone rc core/quit
trap - EXIT

%files
%_bindir/*
%doc *.md

%changelog
* Thu Jan 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.53.4-alt1
- New version 1.53.4 (Fixes: CVE-2020-28924).

* Wed Sep 09 2020 Vitaly Chikunov <vt@altlinux.org> 1.53.0-alt1
- Update v1.53.0 (2020-09-02).

* Mon Aug 10 2020 Vitaly Chikunov <vt@altlinux.org> 1.52.3-alt1
- New version 1.52.3

* Wed Jul 01 2020 Vitaly Chikunov <vt@altlinux.org> 1.52.2-alt1
- New version 1.52.2.

* Mon Jun 15 2020 Vitaly Chikunov <vt@altlinux.org> 1.52.1-alt1
- New version 1.52.1.

* Sun May 31 2020 Vitaly Chikunov <vt@altlinux.org> 1.52.0-alt1
- New version 1.52.0.

* Sun Mar 15 2020 Vitaly Chikunov <vt@altlinux.org> 1.51.0-alt1
- Update to v1.51.0.
- Add some %%check tests.

* Fri Mar 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.46.0-alt1
- Initial build for Sisyphus
