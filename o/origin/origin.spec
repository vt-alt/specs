
%define _libexecdir /usr/libexec

# do not extract debuginfo
%define __find_debuginfo_files %nil

%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir %_libexecdir/origin
%brp_strip_none %_bindir/* %_libexecdir/origin/*

%global gopath      %_datadir/gocode
%global import_path github.com/openshift/origin
%global commit 07e3a8d53563c7fc72445178fa82d71e1e1cad7e
%global kube_commit d4cacc043ac762235e16cb7361d527cb4189393c
%global etcd_commit 121edf0467052d55876a817b89875fb39a99bf78
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global kube_shortcommit %(c=%{kube_commit}; echo ${c:0:7})
%global etcd_shortcommit %(c=%{etcd_commit}; echo ${c:0:7})

%global os_git_vars OS_GIT_VERSION=v3.11.0 OS_GIT_MINOR=11+ OS_GIT_COMMIT=%{shortcommit} OS_GIT_MAJOR=3 OS_GIT_TREE_STATE=clean KUBE_GIT_VERSION=v1.11.0+%{kube_shortcommit} KUBE_GIT_MAJOR=1 KUBE_GIT_MINOR=11+ KUBE_GIT_COMMIT=%{kube_shortcommit} ETCD_GIT_COMMIT=%{etcd_shortcommit} ETCD_GIT_VERSION=v3.2.16

# docker_version is the version of docker requires by packages
%global docker_version 1.13
# openvswitch_version is the version of openvswitch requires by packages
%global openvswitch_version 2.6.1
%global golang_version 1.10
%global product_name Origin

Name: origin
Version: 3.11.0
Release: alt3
Summary: Open Source Container Management
License: Apache-2.0
Group: System/Configuration/Other
Url: https://%import_path
Source: %name-%version.tar
Patch: %name-%version-%release.patch

#ExclusiveArch:  %go_arches
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-golang
BuildRequires: systemd
BuildRequires: bsdtar
BuildRequires: golang >= %golang_version
BuildRequires: libkrb5-devel
BuildRequires: rsync
BuildRequires: /proc
Requires: %name-clients = %version-%release
Requires: iptables

%description
OpenShift Origin is a distribution of Kubernetes optimized for continuous
application development and multi-tenant deployment.
OpenShift adds developer and operations-centric tools on top of Kubernetes
to enable rapid application development, easy deployment and scaling,
and long-term lifecycle maintenance for small and large teams.

%package hypershift
Summary: %product_name server commands
Group: System/Configuration/Other

%description hypershift
%summary

%package hyperkube
Summary: %product_name Kubernetes server commands
Group: System/Configuration/Other

%description hyperkube
%summary

%package master
Summary: %product_name Master
Group: System/Configuration/Other
Requires: %name = %version-%release

%description master
%summary

%package tests
Summary: %product_name Test Suite
Group: System/Configuration/Other

%description tests
%summary

%package node
Summary: %product_name Node
Group: System/Configuration/Other
Requires: %name-hyperkube = %version-%release
Requires: util-linux
Requires: socat

%description node
%summary

%package clients
Summary: %product_name Client binaries for Linux
Group: System/Configuration/Other
Requires: bash-completion

%description clients
%summary

%package pod
Summary: %product_name Pod
Group: System/Configuration/Other

%description pod
%summary

%package sdn-ovs
Summary: %product_name SDN Plugin for Open vSwitch
Group: System/Configuration/Other
Requires: openvswitch >= %openvswitch_version
Requires: %name-node = %version-%release
Requires: bridge-utils
Requires: ethtool
Requires: procps
Requires: iproute
Requires: conntrack-tools

%description sdn-ovs
%summary

%package template-service-broker
Summary: Template Service Broker
Group: System/Configuration/Other

%description template-service-broker
%summary

%prep
%setup
%patch -p1

%build
export GO111MODULE=off
# Create Binaries only for building arch
%ifarch x86_64
  BUILD_PLATFORM="linux/amd64"
%endif
%ifarch %ix86
  BUILD_PLATFORM="linux/386"
%endif
%ifarch ppc64le
  BUILD_PLATFORM="linux/ppc64le"
%endif
%ifarch aarch64
  BUILD_PLATFORM="linux/arm64"
%endif
%ifarch %arm
  BUILD_PLATFORM="linux/arm"
%endif
%ifarch s390x
  BUILD_PLATFORM="linux/s390x"
%endif
GOMAXPROCS=10 OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %os_git_vars OS_BUILD_RELEASE_ARCHIVES=n make build-cross
GOMAXPROCS=10 OS_ONLY_BUILD_PLATFORMS="${BUILD_PLATFORM}" %os_git_vars OS_BUILD_RELEASE_ARCHIVES=n make build WHAT=vendor/github.com/onsi/ginkgo/ginkgo

# Generate man pages
%os_git_vars hack/generate-docs.sh

%install
PLATFORM="$(go env GOHOSTOS)/$(go env GOHOSTARCH)"
install -d %buildroot%_bindir

# Install linux components
for bin in oc oadm openshift hypershift hyperkube template-service-broker openshift-node-config
do
  echo "+++ INSTALLING ${bin}"
  install -p -m 755 _output/local/bin/${PLATFORM}/${bin} %buildroot%_bindir/${bin}
done

# Install tests
install -d %buildroot%_libexecdir/%name
install -p -m 755 _output/local/bin/${PLATFORM}/extended.test %buildroot%_libexecdir/%name/
install -p -m 755 _output/local/bin/${PLATFORM}/ginkgo %buildroot%_libexecdir/%name/

# Install pod
install -p -m 755 _output/local/bin/${PLATFORM}/pod %buildroot%_bindir/

install -d -m 0755 %buildroot%_unitdir

mkdir -p %buildroot%_sysconfdir/sysconfig

for cmd in \
    openshift-deploy \
    openshift-docker-build \
    openshift-sti-build \
    openshift-git-clone \
    openshift-manage-dockerfile \
    openshift-extract-image-content \
    openshift-f5-router \
    openshift-recycle \
    openshift-router \
    kubectl
do
    ln -s oc %buildroot%_bindir/$cmd
done

install -d -m 0755 %buildroot%_sysconfdir/origin/{master,node}
install -d -m 0755 %buildroot%_sysconfdir/kubernetes/manifests
touch %buildroot%_sysconfdir/origin/.config_managed

# stub filed required to ensure config is not reverted during upgrades
install -m 0644 contrib/systemd/origin-node.sysconfig %buildroot%_sysconfdir/sysconfig/%name-node

# Install man1 man pages
install -d -m 0755 %buildroot%_mandir/man1
install -m 0644 docs/man/man1/* %buildroot%_mandir/man1/

mkdir -p %buildroot%_sharedstatedir/origin

# Install sdn scripts
install -d -m 0755 %buildroot%_sysconfdir/cni/net.d
install -d -m 0755 %buildroot%_libexecdir/cni
install -p -m 0755 _output/local/bin/${PLATFORM}/sdn-cni-plugin %buildroot%_libexecdir/cni/openshift-sdn
install -p -m 0755 _output/local/bin/${PLATFORM}/host-local %buildroot%_libexecdir/cni/
install -p -m 0755 _output/local/bin/${PLATFORM}/loopback %buildroot%_libexecdir/cni/

install -d -m 0755 %buildroot%_unitdir/%name-node.service.d

# Install bash completions
install -d -m 755 %buildroot%_sysconfdir/bash_completion.d/
for bin in oc openshift
do
  echo "+++ INSTALLING BASH COMPLETIONS FOR ${bin} "
  %buildroot%_bindir/${bin} completion bash > %buildroot%_sysconfdir/bash_completion.d/${bin}
  chmod 644 %buildroot%_sysconfdir/bash_completion.d/${bin}
done

# Install origin-accounting
install -d -m 755 %buildroot%_sysconfdir/systemd/system.conf.d/
install -p -m 644 contrib/systemd/origin-accounting.conf %buildroot%_sysconfdir/systemd/system.conf.d/

%files
%doc README.md
%doc LICENSE
%_bindir/openshift
%_sharedstatedir/origin
%_sysconfdir/bash_completion.d/openshift
%dir %attr(0700, root, root) %_sysconfdir/origin
%ghost %config(noreplace) %_sysconfdir/origin/.config_managed
%_mandir/man1/openshift*

%files tests
%_libexecdir/%name
%_libexecdir/%name/extended.test

%files hypershift
%_bindir/hypershift

%files hyperkube
%_bindir/hyperkube

%files master
%defattr(-,root,root,0700)
%config(noreplace) %_sysconfdir/origin/master

%files node
%_bindir/openshift-node-config
%_sysconfdir/systemd/system.conf.d/origin-accounting.conf
%config(noreplace) %_sysconfdir/sysconfig/%name-node
%defattr(-,root,root,0700)
%config(noreplace) %_sysconfdir/origin/node
%dir %_sysconfdir/kubernetes/manifests

%files sdn-ovs
%_libexecdir/cni/*

%files clients
%doc LICENSE
%_bindir/oc
%_bindir/kubectl
%_bindir/oadm
%_bindir/openshift-deploy
%_bindir/openshift-docker-build
%_bindir/openshift-sti-build
%_bindir/openshift-git-clone
%_bindir/openshift-extract-image-content
%_bindir/openshift-manage-dockerfile
%_bindir/openshift-f5-router
%_bindir/openshift-recycle
%_bindir/openshift-router
%_sysconfdir/bash_completion.d/oc
%_mandir/man1/oc*

%files pod
%_bindir/pod

%files template-service-broker
%_bindir/template-service-broker

%changelog
* Sun May 24 2020 Alexey Shabalin <shaba@altlinux.org> 3.11.0-alt3
- snapshot of release-3.11 branch (07e3a8d53563c7fc72445178fa82d71e1e1cad7e)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.11.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 3.11.0-alt1
- new version 3.11.0

* Thu Apr 19 2018 Alexey Shabalin <shaba@altlinux.ru> 3.9.0-alt1%ubt
- Initial build for ALT

