%define iptables_modules_dir /%_lib/iptables

Name: ndpi-netfilter
Version: 2.6
Release: alt2
Summary: Open source deep packet inspection iptables modules
Group: Networking/Other

Url: https://github.com/vel21ripn/nDPI/tree/netfilter
License: LGPLv3

Source: %name-%version.tar

BuildRequires: libpcap-devel libiptables-devel
BuildPreReq: rpm-build-kernel

%description
Fork of nDPI is a ntop-maintained superset of the popular OpenDPI library.

%package -n kernel-source-ndpi
License: GPLv2
Summary: Open source deep packet inspection kernel module source
Group: Development/Kernel

%description -n kernel-source-ndpi
Open source deep packet inspection kernel module source

%prep
%setup

%build
sh autogen.sh

make -C src/lib ndpi_network_list.c.inc

mv ndpi-netfilter kernel-source-ndpi-%version
%__tar -c src kernel-source-ndpi-%version | %__bzip2 -c > \
	kernel-source-ndpi-%version.tar.bz2

make -C kernel-source-ndpi-%version/ipt libxt_ndpi.so


%install
mkdir -p %buildroot/%iptables_modules_dir
install -pD -m644 kernel-source-ndpi-%version/ipt/libxt_ndpi.so %buildroot%iptables_modules_dir

mkdir -p %kernel_srcdir
install -m644 kernel-source-ndpi-%version.tar.bz2 %kernel_srcdir/

%files -n kernel-source-ndpi
%_usrsrc/*

%files
%attr(644,root,root) /%_lib/iptables/libxt_ndpi.so

%changelog
* Wed Feb 05 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.6-alt2
- updated from git, build with 5.0 kernel fixed

* Fri Mar 15 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 2.6-alt1
- initial build

