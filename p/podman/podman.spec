%global import_path github.com/containers/libpod
Name:     podman
Version:  1.8.2
Release:  alt1

Summary:  Manage pods, containers, and container images
License:  Apache-2.0
Group:    System/Configuration/Other
# https://github.com/containers/libpod
Url:      https://podman.io/

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Patch1: fix-source-name-in-man.patch
Patch2: makefile_not_create_link_docs.patch
Patch3: makefile_remove_prefix_tmpfile_and_systemd.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-md2man
BuildRequires: libseccomp-devel glib2-devel libgpgme-devel libbtrfs-devel
BuildRequires: libgio-devel libostree-devel libselinux-devel libdevmapper-devel
BuildRequires: libassuan-devel libsystemd-devel
BuildRequires: /proc

Requires: conmon >= 2.1
Requires: cni cni-plugins containers-common

%description
%summary.

%package docker
Summary:  Emulate Docker CLI using podman
Group:    System/Configuration/Other
Conflicts: docker-ce

%description docker
%summary.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export BUILDTAGS='seccomp ostree varlink containers_image_ostree_stub systemd'

%make_build

%install
%makeinstall_std install.completions install.config install.docker PREFIX=/usr

%files docker
%_bindir/docker
%_man1dir/docker*

%files
%_bindir/%{name}*
%_datadir/containers/libpod.conf
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_unitdir/io.%name.*
/lib/systemd/user/io.%name.*
%_sysconfdir/cni/net.d/87-podman-bridge.conflist
%_tmpfilesdir/%name.conf
%_tmpfilesdir/%name-docker.conf
%_man1dir/*
%exclude %_man1dir/docker*
%_man5dir/*
%doc *.md

%changelog
* Sat Mar 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.8.2-alt1
- new version 1.8.2

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.8.1-alt1
- new version 1.8.1

* Thu Dec 12 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.4-alt1
- new version 1.6.4

* Tue Oct 29 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.2-alt1
- new version 1.6.2

* Fri Sep 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.1-alt2
- Use make to build
- Add podman-docker subpackage

* Tue Sep 17 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.1-alt1
- new version 1.5.1

* Thu Jul 25 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.4-alt1
- new version 1.4.4

* Sat Mar 16 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Mon Jan 07 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.1.2-alt1
- Initial build for Sisyphus
