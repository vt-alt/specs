Name:           nftables
Epoch:          1
Version:        0.9.2
Release:        alt1
Summary:        nftables is the project that aims to replace the existing {ip,ip6,arp,eb}tables framework
Group:          System/Libraries
License:        GPL-2.0-only
URL:            http://netfilter.org/projects/nftables
# git://git.netfilter.org/nftables
Source:        %name-%version.tar
BuildRequires: libmnl-devel libnftnl-devel flex bison libgmp-devel libreadline-devel asciidoc-a2x
BuildRequires(pre): docbook2X

%description
libnftnl is a userspace library providing a low-level netlink programming interface (API) to the
in-kernel nf_tables subsystem. The library libnftnl has been previously known as libnftables.
This library is currently used by nftables.

%prep
%setup

%build
%autoreconf
%configure --enable-debug
%make_build

%check
make check

%install
%makeinstall_std

#mkdir -p %buildroot%_sysconfdir/nftables
install -dm0755 %buildroot%_docdir/%name
rm %buildroot%_sysconfdir/nftables/*.nft
install -pDm0644 nftables.nft %buildroot%_sysconfdir/nftables/nftables.nft
install -dm0755 %buildroot%_unitdir
install -pDm0644 nftables.service %buildroot%_unitdir/nftables.service

%post
%post_service nftables

%files
%doc COPYING files/examples/*.nft files/nftables/*.nft
%dir %_sysconfdir/nftables
%dir %_sysconfdir/nftables/osf
%_sysconfdir/nftables/osf/*
%attr(644,root,root) %config %_sysconfdir/nftables/*.nft
%_libdir/lib%name.so.*
%_unitdir/*
%_sbindir/*
%_man8dir/*


%changelog
* Tue Aug 20 2019 Alexei Takaseev <taf@altlinux.org> 1:0.9.2-alt1
- Version 0.9.2

* Wed Jun 26 2019 Alexei Takaseev <taf@altlinux.org> 1:0.9.1-alt1
- Version 0.9.1

* Tue Jan 15 2019 Alexei Takaseev <taf@altlinux.org> 1:0.9.0-alt2
- Add systemd unit and simple config

* Sat Jun 09 2018 Alexei Takaseev <taf@altlinux.org> 1:0.9.0-alt1
- Version 0.9.0

* Wed May 02 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.4-alt1
- Version 0.8.4

* Sun Mar 04 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.3-alt1
- Version 0.8.3
- Remove dblatex from BR

* Mon Feb 05 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.2-alt1
- Version 0.8.2

* Fri Jan 19 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.1-alt1
- Version 0.8.1

* Fri Oct 13 2017 Alexei Takaseev <taf@altlinux.org> 1:0.8-alt1
- Version 0.8
- disable pdf

* Wed Dec 21 2016 Alexei Takaseev <taf@altlinux.org> 1:0.7-alt1
- Version 0.7

* Fri Jun 03 2016 Alexei Takaseev <taf@altlinux.org> 1:0.6-alt1
- Version 0.6

* Mon Dec 21 2015 Alexei Takaseev <taf@altlinux.org> 1:0.5-alt1
- Version 0.5

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.3-alt1.git20140915
- Version 0.3

* Tue Jan 21 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.100-alt1
- first build for ALT Linux
