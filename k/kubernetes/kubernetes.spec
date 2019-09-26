
%global import_path github.com/kubernetes/kubernetes
%global commit 67d2fcf276fcd9cf743ad4be9a9ef5828adc082f

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: kubernetes
Version: 1.15.4
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: ASL 2.0
Url: https://%import_path
Source: %name-%version.tar


Source2: genmanpages.sh
Source3: kubernetes-accounting.conf
Source4: kubeadm.conf

#systemd services
Source10: kube-apiserver.service
Source11: kube-controller-manager.service
Source12: kubelet.service
Source13: kube-proxy.service
Source14: kube-scheduler.service
#config files
Source20: apiserver
Source21: config
Source22: controller-manager
Source23: kubelet
Source24: proxy
Source25: scheduler
Source26: kubernetes.tmpfiles

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: /proc
BuildRequires: rsync
BuildRequires: go-md2man go-bindata

%description
Kubernetes is an open source system for managing containerized applications
across multiple hosts; providing basic mechanisms
for deployment, maintenance, and scaling of applications.

%package common
Summary: Kubernetes common files
Group: System/Configuration/Other

%description common
Kubernetes is an open source system for managing containerized applications
across multiple hosts; providing basic mechanisms
for deployment, maintenance, and scaling of applications.

This subpackage contains the Kubernetes common files.

%package unit-test
Summary: %summary - for running unit tests
Group: System/Configuration/Other
Requires: golang >= 1.2
Requires: etcd >= 2.0.9
Requires: hostname
Requires: rsync

%description unit-test
%summary - for running unit tests

%package master
Summary: Kubernetes services for master host
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-client = %EVR
# if node is installed with node, version and release must be the same
Conflicts: %name-node < %EVR
Conflicts: %name-node > %EVR

%description master
Kubernetes services for master host.

%package node
Summary: Kubernetes services for node host
Group: System/Configuration/Other
BuildArch: noarch
Requires: docker-ce
Requires: conntrack-tools
Requires: ethtool
Requires: iptables
Requires: socat
Requires: %name-client = %EVR
Requires: %name-kubelet = %EVR
# if master is installed with node, version and release must be the same
Conflicts: %name-master < %EVR
Conflicts: %name-master > %EVR

%description node
Kubernetes services for node host.

%package kubelet
Summary: Kubernetes kubelet daemon
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common = %EVR
# if master is installed with node, version and release must be the same
Conflicts: %name-master < %EVR
Conflicts: %name-master > %EVR

%description kubelet
Kubernetes kubelet service.

%package  kubeadm
Summary:  Kubernetes tool for standing up clusters
Group: System/Configuration/Other
Requires: %name-node = %EVR
Requires: cni-plugins >= 0.7.5
Requires: ebtables
Requires: iptables
Requires: ethtool
Requires: socat

%description kubeadm
Kubernetes tool for standing up clusters.

%package client
Summary: Kubernetes client tools
Group: System/Configuration/Other
BuildArch: noarch
Requires: %name-common = %EVR

%description client
Kubernetes client tools like kubectl

%prep
%setup -q
rm -f go.{mod,sum}

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export KUBE_GIT_COMMIT=%commit
export KUBE_GIT_TREE_STATE="clean"
export KUBE_GIT_VERSION="v%version"

%golang_prepare
pushd .gopath/src/%import_path
export KUBE_EXTRA_GOPATH=$(pwd)/Godeps/_workspace

GOMAXPROCS=10 make WHAT="cmd/hyperkube cmd/kubeadm"

# convert md to man
./hack/generate-docs.sh || true
pushd docs
pushd admin
cp kube-apiserver.md kube-controller-manager.md kube-proxy.md kube-scheduler.md kubelet.md ..
popd
cp %SOURCE2 genmanpages.sh
bash genmanpages.sh
popd
popd

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="%go_path"
#%golang_install
#rm -rf -- %buildroot%_datadir

cd .gopath/src/%import_path
%ifarch ppc64le aarch64
output_path="_output/local/go/bin"
%else
output_path="_output/local/bin/linux/%go_hostarch"
%endif

install -m 755 -d %buildroot%_bindir

echo "+++ INSTALLING hyperkube"
install -p -m 755 -t %buildroot%_bindir ${output_path}/hyperkube

echo "+++ INSTALLING kubeadm"
install -p -m 755 -t %buildroot%_bindir ${output_path}/kubeadm
install -d -m 755 %buildroot%_sysconfdir/systemd/system/kubelet.service.d
install -p -m 644 -t %buildroot/%_sysconfdir/systemd/system/kubelet.service.d %SOURCE4

for bin in kube-apiserver kube-controller-manager kube-scheduler kube-proxy kubelet kubectl ; do
  echo "+++ SYMLINKING ${bin} to hyperkube"
  ln -sr %buildroot%_bindir/hyperkube %buildroot%_bindir/${bin}
done

# install the bash completion
install -d -m 0755 %buildroot%_datadir/bash-completion/completions/
%buildroot%_bindir/kubectl completion bash > %buildroot%_datadir/bash-completion/completions/kubectl

# systemd service
install -d -m 0755 %buildroot%_unitdir
for src in %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 ; do
  install -m 0644 -t %buildroot%_unitdir/ "$src"
done

# install manpages
install -d %buildroot%_man1dir
install -p -m 644 docs/man/man1/* %buildroot%_man1dir

# install config files
install -d -m 0755 %buildroot%_sysconfdir/%name
for src in %SOURCE20 %SOURCE21 %SOURCE22 %SOURCE23 %SOURCE24 %SOURCE25 ; do
  install -m 0644 -t %buildroot%_sysconfdir/%name "$src"
done

# manifests file for the kubelet
install -d -m 0755 %buildroot%_sysconfdir/%name/manifests

# place kubernetes.tmpfiles to /lib/tmpfiles.d/kubernetes.conf
install -d -m 0755 %buildroot%_tmpfilesdir
install -D -m 0644 %SOURCE26 %buildroot%_tmpfilesdir/kubernetes.conf

# install the place the kubelet defaults to put volumes
install -d %buildroot%_localstatedir/kubelet

# enable CPU and Memory accounting
install -d -m 0755 %buildroot/%_sysconfdir/systemd/system.conf.d
install -p -m 0644 -t %buildroot/%_sysconfdir/systemd/system.conf.d %SOURCE3

%pre common
%_sbindir/groupadd -r -f kube > /dev/null 2>&1 ||:
%_sbindir/useradd -r -g kube -d %_localstatedir/%name -s /dev/null -c "Kubernetes user" kube > /dev/null 2>&1 ||:

%post master
%post_service kube-apiserver
%post_service kube-scheduler
%post_service kube-controller-manager

%preun master
%preun_service kube-apiserver
%preun_service kube-scheduler
%preun_service kube-controller-manager

%post kubelet
%post_service kubelet

%preun kubelet
%preun_service kubelet

%post node
%post_service kube-proxy

%preun node
%preun_service kube-proxy

%files common
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config
%_bindir/hyperkube
%_tmpfilesdir/%name.conf

%files master
%doc README.md LICENSE
%_man1dir/kube-apiserver.*
%_man1dir/kube-controller-manager.*
%_man1dir/kube-scheduler.*
%_man1dir/cloud-controller-manager.*
%_bindir/kube-apiserver
%_bindir/kube-controller-manager
%_bindir/kube-scheduler
%_unitdir/kube-apiserver.service
%_unitdir/kube-controller-manager.service
%_unitdir/kube-scheduler.service
%config(noreplace) %_sysconfdir/%name/apiserver
%config(noreplace) %_sysconfdir/%name/scheduler
%config(noreplace) %_sysconfdir/%name/controller-manager

%files node
%doc README.md LICENSE
%_man1dir/kube-proxy.*
%_bindir/kube-proxy
%_unitdir/kube-proxy.service
%config(noreplace) %_sysconfdir/%name/proxy
%config(noreplace) %_sysconfdir/systemd/system.conf.d/kubernetes-accounting.conf

%files kubelet
%doc README.md LICENSE
%_man1dir/kubelet.*
%_bindir/kubelet
%_unitdir/kubelet.service
%dir %_localstatedir/kubelet
%config(noreplace) %_sysconfdir/%name/kubelet
%dir %_sysconfdir/%name/manifests

%files kubeadm
%doc README.md LICENSE
%_man1dir/kubeadm*
%_bindir/kubeadm
%dir %_sysconfdir/systemd/system/kubelet.service.d
%config(noreplace) %_sysconfdir/systemd/system/kubelet.service.d/kubeadm.conf

%files client
%doc README.md LICENSE
%_man1dir/kubectl*
%_bindir/kubectl
%_datadir/bash-completion/completions/kubectl

%changelog
* Thu Sep 26 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.4-alt1
- 1.15.4

* Thu Sep 26 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.3-alt1
- 1.15.3 (Fixes: CVE-2019-9512, CVE-2019-9514)

* Tue Sep 24 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.15.2-alt2
- Remove deprecated and removed flags from kubeadm.conf

* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.2-alt1
- 1.15.2

* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.14.1-alt1
- 1.14.1

* Wed Mar 27 2019 Alexey Shabalin <shaba@altlinux.org> 1.14.0-alt1
- 1.14.0

* Sun Mar 24 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.4-alt1
- 1.13.4

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.3-alt1
- 1.13.3

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.2-alt1
- 1.13.2

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.13.0-alt1
- 1.13.0

* Mon Oct 01 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.0-alt1
- 1.12.0

* Fri Aug 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.2-alt1%ubt
- 1.11.2

* Fri Jul 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1%ubt
- 1.11.0

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.10.4-alt1%ubt
- 1.10.4

* Mon May 14 2018 Alexey Shabalin <shaba@altlinux.ru> 1.10.2-alt1%ubt
- Initial build for ALT
