%define _libexecdir /usr/libexec

%global provider        github
%global provider_tld    com
%global project         docker
%global repo_engine     docker
%global repo_cli        cli

%global import_path_engine %{provider}.%{provider_tld}/%{project}/%{repo_engine}
%global import_path_cli %{provider}.%{provider_tld}/%{project}/%{repo_cli}
%global build_dir ./_build
%global build_dir_cli %build_dir/src/%import_path_cli
%global build_dir_engine %build_dir/src/%import_path_engine
%global commit      2d0083d657f82c47044c8d3948ba434b622fe2fd
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       docker-ce
Version:    19.03.1
Release: alt2
Summary: Automates deployment of containerized applications
License: ASL 2.0
Group: System/Configuration/Other

%global versuffix ce
%global fullversion %{version}-%{versuffix}

Url: https://github.com/docker/docker-ce
ExclusiveArch: %go_arches
Conflicts: docker

Source0: %name-%version.tar
Source1: %repo_engine.service
Source2: %repo_engine.init
Source3: %repo_engine.sysconf
Source4: %repo_engine-storage.sysconf
Source5: daemon.json

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc gcc golang >= 1.3 systemd-devel libdevmapper-devel libbtrfs-devel libseccomp-devel
BuildRequires: go-md2man
Requires: tar xz
Provides: docker-io = %version-%release
Obsoletes: docker-io <= 17.05.0
Obsoletes: docker-io-devel <= 17.05.0
Requires: /usr/bin/docker-proxy
Requires: docker-containerd >= 1.0.2-alt1
Requires: docker-runc >= 1.0.0-alt4.rc5
Requires: docker-init >= 0.17.0-alt1
Requires: iptables

# do not extract debuginfo
%define __find_debuginfo_files %nil

# do not run debugedit for them
%add_debuginfo_skiplist /usr/bin/docker

%description
Docker is an open-source engine that automates the deployment of any
application as a lightweight, portable, self-sufficient container that will
run virtually anywhere.

Docker containers can encapsulate any payload, and will run consistently on
and between virtually any server. The same container that a developer builds
and tests on a laptop will run at scale, in production*, on VMs, bare-metal
servers, OpenStack clusters, public instances, or combinations of the above.

%prep
%setup

%build

mkdir -p %{build_dir}
export GOPATH="$(pwd)/%{build_dir}:%{go_path}"

# build cli
mkdir -p %{build_dir_cli}
cp -alv -- components/cli/* %{build_dir_cli}
DISABLE_WARN_OUTSIDE_CONTAINER=1 make -C %{build_dir_cli} VERSION=%{fullversion}
DISABLE_WARN_OUTSIDE_CONTAINER=1 make -C %{build_dir_cli} manpages

# build daemon
export DOCKER_GITCOMMIT="%{shortcommit}/%{version}"
export DOCKER_BUILDTAGS='selinux journald pkcs11 seccomp'
mkdir -p %{build_dir_engine}
cp -alv -- components/engine/* %{build_dir_engine}
pushd %{build_dir_engine}
hack/make.sh dynbinary
popd

%install
# install binary
install -d %{buildroot}%{_bindir}
install -p -m 755 %{build_dir_cli}/build/docker %{buildroot}%{_bindir}/docker
install -p -m 755 %{build_dir_engine}/bundles/dynbinary-daemon/dockerd-dev %{buildroot}%{_bindir}/dockerd

install -d %{buildroot}%{_libexecdir}/docker

# install manpages
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 %{build_dir_cli}/man/man1/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5
install -p -m 644 %{build_dir_cli}/man/man5/*.5 %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man8
install -p -m 644 %{build_dir_cli}/man/man8/*.8 %{buildroot}%{_mandir}/man8

# install bash completion
install -Dp -m 644 %{build_dir_cli}/contrib/completion/bash/docker %{buildroot}%{_datadir}/bash-completion/completions/docker

# install zsh completion
install -Dp -m 644 %{build_dir_cli}/contrib/completion/zsh/_docker %{buildroot}%{_datadir}/zsh/site-functions/_docker

# install fish completion
install -Dp -m 644 %{build_dir_cli}/contrib/completion/fish/docker.fish %{buildroot}%{_datadir}/fish/completions/docker.fish

# install vim syntax highlighting
# (in process of being included in default vim)
install -d %{buildroot}%{_datadir}/vim/vimfiles/{doc,ftdetect,syntax}
install -p -m 644 %{build_dir_engine}/contrib/syntax/vim/doc/dockerfile.txt %{buildroot}%{_datadir}/vim/vimfiles/doc
install -p -m 644 %{build_dir_engine}/contrib/syntax/vim/ftdetect/dockerfile.vim %{buildroot}%{_datadir}/vim/vimfiles/ftdetect
install -p -m 644 %{build_dir_engine}/contrib/syntax/vim/syntax/dockerfile.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax

# install udev rules
install -d %{buildroot}%{_sysconfdir}/udev/rules.d
install -m 644 -p %{build_dir_engine}/contrib/udev/80-docker.rules %{buildroot}%{_sysconfdir}/udev/rules.d

# install storage dir
install -d %{buildroot}%{_sharedstatedir}/%{repo_engine}

# install systemd/init scripts
install -p -D -m 644 altlinux/%{repo_engine}.service %{buildroot}%{_unitdir}/%{repo_engine}.service
install -p -D -m 755 altlinux/%{repo_engine}.init %{buildroot}%{_initddir}/%{repo_engine}

install -d %buildroot%_sysconfdir/sysconfig
install -p -m 644 altlinux/docker.sysconf %buildroot%_sysconfdir/sysconfig/docker
install -p -m 644 altlinux/docker-storage.sysconf %buildroot%_sysconfdir/sysconfig/docker-storage

install -d %buildroot%_sysconfdir/docker
install -p -m 644 altlinux/daemon.json %buildroot%_sysconfdir/docker/daemon.json

%pre
getent group docker > /dev/null || %{_sbindir}/groupadd -r docker
exit 0

%post
%post_service docker

%preun
%preun_service docker

%files
%doc components/engine/AUTHORS components/engine/LICENSE
%doc components/engine/MAINTAINERS components/engine/NOTICE
%doc CHANGELOG.md CONTRIBUTING.md README.md
%doc components/engine/contrib/syntax/vim/LICENSE
%doc components/engine/contrib/syntax/vim/README.md
%config(noreplace) %{_sysconfdir}/sysconfig/docker
%config(noreplace) %{_sysconfdir}/sysconfig/docker-storage
%config(noreplace) %{_sysconfdir}/docker/daemon.json
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_bindir}/docker
%{_bindir}/dockerd
%dir %{_libexecdir}/docker
%{_unitdir}/docker.service
%_initdir/docker
%{_datadir}/bash-completion/completions/docker
%{_datadir}/zsh/site-functions/_docker
%{_datadir}/fish/completions/docker.fish
%dir %{_sharedstatedir}/docker
%{_sysconfdir}/udev/rules.d/80-docker.rules
%{_datadir}/vim/vimfiles/doc/dockerfile.txt
%{_datadir}/vim/vimfiles/ftdetect/dockerfile.vim
%{_datadir}/vim/vimfiles/syntax/dockerfile.vim

%changelog
* Thu Sep 05 2019 Mikhail Gordeev <obirvalger@altlinux.org> 19.03.1-alt2
- Make udev rules not executable

* Wed Aug 7 2019 Vladimir Didenko <cow@altlinux.org> 19.03.1-alt1
- 19.03.1 (fixes CVE-2019-14271)

* Thu Jul 25 2019 Vladimir Didenko <cow@altlinux.org> 19.03.0-alt1
- 19.03.0

* Wed Jul 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 18.09.8-alt1
- 18.09.8

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 18.09.7-alt2
- fix spec file

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 18.09.7-alt1
- 18.09.7

* Wed May 8 2019 Vladimir Didenko <cow@altlinux.org> 18.09.6-alt1
- 18.09.6

* Wed Apr 17 2019 Vladimir Didenko <cow@altlinux.org> 18.09.5-alt1
- 18.09.5

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.org> 18.09.4-alt1
- 18.09.4

* Fri Mar 22 2019 Alexey Shabalin <shaba@altlinux.org> 18.09.3-alt1
- 18.09.3
- build with seccomp support

* Fri Mar 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 18.09.1-alt2
- Change golang-github-cpuguy83-go-md2man to go-md2man in BuildRequires

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.org> 18.09.1-alt1
- New version

* Thu Jan 17 2019 Mikhail Gordeev <obirvalger@altlinux.org> 18.09.0-alt4
- add iptables to requires

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 18.09.0-alt3
- add completions for zsh and fish

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 18.09.0-alt2
- Use overlay2 storage driver by default

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 18.09.0-alt1
- New version

* Thu Aug 30 2018 Vladimir Didenko <cow@altlinux.org> 18.06.1-alt1
- New version

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.org> 18.06.0-alt1.1
- remove unused build requirements

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.org> 18.06.0-alt1
- New version

* Mon May 14 2018 Alexey Shabalin <shaba@altlinux.ru> 18.03.1-alt2
- define ExclusiveArch as  %%go_arches

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.org> 18.03.1-alt1
- New version

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.org> 18.03.0-alt1
- New version

* Wed Feb 7 2018 Vladimir Didenko <cow@altlinux.org> 18.02.0-alt2.rc2
- Support rename of docker-init to tini

* Wed Feb 7 2018 Vladimir Didenko <cow@altlinux.org> 18.02.0-alt1.rc2
- New version

* Mon Jan 15 2018 Vladimir Didenko <cow@altlinux.org> 18.01.0-alt1
- New version

* Tue Jan 9 2018 Vladimir Didenko <cow@altlinux.org> 17.12.0-alt1
- New version
- Remove devel package (seems useless)

* Tue May 16 2017 Vladimir Didenko <cow@altlinux.org> 17.05.0-alt1
- New version

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.org> 17.04.0-alt1
- New version

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.org> 17.03.0-alt1
- New version

* Fri Feb 10 2017 Vladimir Didenko <cow@altlinux.org> 1.13.1-alt1
- New version

* Wed Jan 25 2017 Vladimir Didenko <cow@altlinux.org> 1.13.0-alt1
- New version

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.org> 1.12.5-alt1
- New version

* Tue Nov 29 2016 Vladimir Didenko <cow@altlinux.org> 1.12.3-alt1
- New version

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.org> 1.12.2-alt1
- New version

* Tue Sep 20 2016 Alexandr Boltris <alex@altlinux.org> 1.12.1-alt2
- add docker-proxy. fixes #32489

* Fri Aug 19 2016 Vladimir Didenko <cow@altlinux.org> 1.12.1-alt1
- New version

* Tue Aug 2 2016 Vladimir Didenko <cow@altlinux.org> 1.12.0-alt1
- New version

* Thu Jun 2 2016 Vladimir Didenko <cow@altlinux.org> 1.11.2-alt1
- New version

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.org> 1.11.1-alt1
- New version
- Remove manual provides

* Thu May 5 2016 Vladimir Didenko <cow@altlinux.org> 1.11.0-alt1
- New version

* Fri Mar 11 2016 Vladimir Didenko <cow@altlinux.org> 1.10.3-alt1
- New version

* Thu Feb 25 2016 Vladimir Didenko <cow@altlinux.org> 1.10.2-alt1
- New version

* Tue Feb 16 2016 Vladimir Didenko <cow@altlinux.org> 1.10.1-alt1
- New version
- Restore bash completions

* Wed Feb 10 2016 Vladimir Didenko <cow@altlinux.org> 1.10.0-alt1.1
- fix provides

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.org> 1.10.0-alt1
- New version.
- Merge devel and pkg-devel packages
- add init script for sysvinit

* Wed Nov 25 2015 Vladimir Didenko <cow@altlinux.org> 1.9.1-alt1
- New version.

* Fri Nov 6 2015 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- New version.

* Tue Oct 13 2015 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- New version.
- Return CAP_AUDIT_READ since std-def kernel supports it now
- Fix build with golang 1.5

* Mon Aug 24 2015 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version.

* Fri May 08 2015 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.1-alt1
- Update to new version with security updates
 + Fix read/write /proc paths (CVE-2015-3630)
 + Prohibit VOLUME /proc and VOLUME / (CVE-2015-3631)
 + Fix opening of file-descriptor 1 (CVE-2015-3627)
 + Fix symlink traversal on container respawn allowing
   local privilege escalation (CVE-2015-3629)
 + Prohibit mount of /sys

* Sat Apr 18 2015 Evgeny Sinelnikov <sin@altlinux.ru> 1.6.0-alt1
- Update to last stable version
- Avoid of using CAP_AUDIT_READ capability for support
  less than 3.16.x kernel versions
- Rename dockerversion to autogen (c40993777f152426ea029)

* Wed Nov 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.1-alt1
- New version.
- Updated spec to Fedora 1.3.1-2.

* Mon Sep 15 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.2.0-alt1
- New version.

* Wed Aug 13 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.2-alt1
- New version.

* Thu Jun 19 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt2
- Dropped %%_datadir/vim/vimfiles/{doc,ftdetect,syntax}.

* Wed Jun 11 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1
- New version.

* Mon May 12 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.11.1-alt1
- New version.

* Wed Apr 23 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.0-alt2
- %%post: restored creation of docker group.

* Tue Apr 22 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10.0-alt1
- New version.

* Mon Jan 06 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.3-alt1
- New version

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.2-alt1
- New version

* Tue Nov 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.0-alt1
- Release

* Mon Nov 25 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt3.rc7
- New RC

* Sat Oct 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt3.rc4
- New RC

* Fri Oct 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt2.rc3
- Update up to upstream/v0.7-rc3 branch
- Add ExclusiveArch: x86_64
- Build docker-init statically

* Wed Oct 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7-alt1.rc3
- Build for ALT
