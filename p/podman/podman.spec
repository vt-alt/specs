%global import_path github.com/containers/libpod
Name:     podman
Version:  1.9.2
Release:  alt1

Summary:  Manage pods, containers, and container images
License:  Apache-2.0
Group:    System/Configuration/Other
# https://github.com/containers/libpod
Url:      https://podman.io/

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Patch2: makefile_not_create_link_docs.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-md2man
BuildRequires: libseccomp-devel glib2-devel libgpgme-devel libbtrfs-devel
BuildRequires: libgio-devel libostree-devel libselinux-devel libdevmapper-devel
BuildRequires: libassuan-devel libsystemd-devel
BuildRequires: /proc

Requires: conmon >= 2.0.16
Requires: iptables
Requires: nftables
Requires: crun
Requires: slirp4netns
Requires: cni cni-plugins >= 0.8.6 containers-common

%description
%summary.

%package docker
Summary:  Emulate Docker CLI using podman
Group:    System/Configuration/Other
Conflicts: docker-ce

%description docker
%summary.

%package remote
Group:    System/Configuration/Other
Summary: (Experimental) Remote client for managing %name containers

%description remote
Remote client for managing %name containers.

This experimental remote client is under heavy development. Please do not
run %name-remote in production.

%name-remote uses the varlink connection to connect to a %{name} client to
manage pods, containers and container images. %{name}-remote supports ssh
connections as well.

%prep
%setup
%patch2 -p1

%build
%make_build PREFIX=%_prefix TMPFILESDIR=%_tmpfilesdir SYSTEMDDIR=%_unitdir

%install
sed -s 's/^runtime[ =].*"runc/runtime = "crun/' libpod.conf  -i

%makeinstall_std PREFIX=%_prefix TMPFILESDIR=%_tmpfilesdir SYSTEMDDIR=%_unitdir \
    install.completions install.config install.docker PREFIX=/usr

# install /etc/modules-load.d/podman.conf
echo br_netfilter > %name.conf
install -dp %buildroot%_sysconfdir/modules-load.d
install -p -m 644 %name.conf %buildroot%_sysconfdir/modules-load.d/

%files
%_bindir/%name
%_datadir/containers/libpod.conf
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_unitdir/*
%_prefix/lib/systemd/user/*
%config(noreplace) %_sysconfdir/cni/net.d/87-podman-bridge.conflist
%config(noreplace) %_sysconfdir/modules-load.d/%name.conf
%_tmpfilesdir/%name.conf
%_man1dir/*
%exclude %_man1dir/docker*
%_man5dir/*
%doc *.md

%files remote
%_bindir/%name-remote
%_man1dir/%name-remote*
%_man5dir/%name-remote*

%files docker
%_bindir/docker
%_man1dir/docker*
%_tmpfilesdir/%name-docker.conf

%changelog
* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.9.2-alt1
- new version 1.9.2

* Tue Apr 21 2020 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- new version 1.9.0
- add podman-remote package
- use crun as default runtime
- add load br_netfilter kernel module
- package 87-podman-bridge.conflist as config(noreplace)
- fixed package user systemd units

* Tue Apr 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.8.2-alt2
- fix version in conmon requires

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
