
%define oname blackbox_exporter
%global import_path github.com/prometheus/blackbox_exporter
%global commit 1cfb7512daa7e100abb32037996c8f805990d813

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: prometheus-%oname
Version: 0.14.0
Release: alt1
Summary: Prometheus blackbox prober exporter

Group: Development/Other
License: ASL 2.0
Url: https://%import_path
Source: %name-%version.tar

Source2: %name.sysconfig
Source3: %name.init
Source4: %name.service

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: promu
BuildRequires: /proc

Requires(pre): prometheus-common

%description
The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
promu build

%install
#export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
#%golang_install
#rm -rf -- %buildroot%_datadir
mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/{sysconfig,prometheus}}

install -m0755 %oname %buildroot%_bindir/%oname
install -m0644 blackbox.yml %buildroot%_sysconfdir/prometheus/blackbox.yml
install -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md CONFIGURATION.md example.yml
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/prometheus/blackbox.yml

%changelog
* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 0.14.0-alt1
- 0.14.0

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 0.13.0-alt1
- 0.13.0

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt2%ubt
- fix typo in option

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 0.12.0-alt1%ubt
- Initial build for ALT.
