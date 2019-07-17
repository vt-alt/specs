%global import_path github.com/prometheus/prometheus
%global commit e5b22494857deca4b806f74f6e3a6ee30c251763
%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: prometheus
Version: 2.11.1
Release: alt1
Summary: Prometheus monitoring system and time series database

Group: Development/Other
License: ASL 2.0
Url: https://%import_path
Source: %name-%version.tar

Source2: %name.sysconfig
Source3: %name.init
Source4: %name.service
Source5: %name.tmpfiles

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: promu
BuildRequires: /proc

Requires: %name-common = %EVR

%description
Prometheus is an open-source systems monitoring and alerting toolkit.

Prometheus's main features are:
 - a multi-dimensional data model with time series data
   identified by metric name and key/value pairs
 - a flexible query language to leverage this dimensionality
 - no reliance on distributed storage; single server nodes are autonomous
 - time series collection happens via a pull model over HTTP
 - pushing time series is supported via an intermediary gateway
 - targets are discovered via service discovery or static configuration
 - multiple modes of graphing and dashboarding support
 - support for hierarchical and horizontal federation

%package common
Summary: Common package for Prometheus
Group: Development/Other
BuildArch: noarch

%description common
Prometheus is an open-source systems monitoring and alerting toolkit.

This package contains the common files and settings for Prometheus.

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
mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_tmpfilesdir,%_sysconfdir/sysconfig,{%_sysconfdir,%_datadir,%_localstatedir}/%name}

install -m0755 prometheus %buildroot%_bindir/%name
install -m0755 promtool %buildroot%_bindir/promtool
cp -frv console_libraries consoles %buildroot%_datadir/%name/
install -m0644 documentation/examples/prometheus.yml %buildroot%_sysconfdir/%name/%name.yml
install -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service
install -m0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf

%pre common
%_sbindir/groupadd -r -f %name > /dev/null 2>&1 ||:
%_sbindir/useradd -r -g %name -d %_localstatedir/%name -s /dev/null -c "Prometheus services" %name > /dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md docs documentation/examples
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/%name/*
%dir %_datadir/%name
%_datadir/%name/*

%files common
%dir %_sysconfdir/%name
%_tmpfilesdir/%name.conf
%dir %attr(775, root, %name) %_localstatedir/%name

%changelog
* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 2.11.1-alt1
- 2.11.1

* Wed Mar 06 2019 Alexey Shabalin <shaba@altlinux.org> 2.7.2-alt1
- 2.7.2

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 2.6.1-alt1
- 2.6.1

* Thu May 10 2018 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt2%ubt
- move adduser, tmpfiles and /etc/prometheus to prometheus-common package
- update systemd unit

* Tue May 08 2018 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1%ubt
- Initial build for ALT.

