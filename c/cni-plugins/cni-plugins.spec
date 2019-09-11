
%global import_path github.com/containernetworking/plugins
%global commit 485be65581341430f9106a194a98f0f2412245fb
#%%global shortcommit %(c=%commit; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%define _libexecdir /usr/libexec
%define cni_dir %_libexecdir/cni
%define cni_etc_dir %_sysconfdir/cni

Name: cni-plugins
Version: 0.8.2
Release: alt1
Summary: Container Network Interface plugins
Group: Development/Other
License: ASL 2.0
Url: https://%import_path
Source: %name-%version.tar
ExclusiveArch: %go_arches

Provides: containernetworking-plugins = %EVR

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

%description
The CNI (Container Network Interface) project consists of a
specification and libraries for writing plugins to configure
network interfaces in Linux containers, along with a number of
supported plugins. CNI concerns itself only with network
connectivity of containers and removing allocated resources when
the container is deleted. Because of this focus, CNI has a wide
range of support and the specification is simple to implement.

These are the additional CNI network plugins provided by
the containernetworking team.

%prep
%setup -q

%build
./build_linux.sh

%install
mkdir -p %buildroot{%cni_dir,%cni_etc_dir/net.d}
install -m0755 bin/* %buildroot%cni_dir/

%files
%doc LICENSE README.md
%dir %cni_etc_dir
%dir %cni_etc_dir/net.d
%dir %cni_dir
%cni_dir/*

%changelog
* Tue Sep 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.2-alt1
- 0.8.2

* Fri Jul 19 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.1-alt1
- updated to v0.8.1-35-gb6f1a69

* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.5-alt1
- 0.7.5

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.4-alt1
- 0.7.4

* Wed Jun 13 2018 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt2%ubt
- rebuild for aarch64

* Sat May 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.7.1-alt1%ubt
- Initial package

