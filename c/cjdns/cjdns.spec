%define _unpackaged_files_terminate_build 1

Name: cjdns
Version: 20.3
Release: alt1

Summary: Encrypted networking for regular people
License: GPLv3+
Group: Networking/Other
Url: https://github.com/cjdelisle/cjdns/

# https://github.com/cjdelisle/cjdns.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

# don't use libuv-devel since it uses bundled patched libuv to build static library
BuildRequires: nodejs python-devel gyp node-gyp /proc

%description
Cjdns implements an encrypted IPv6 network using public key cryptography
for address allocation and a distributed hash table for routing.
This provides near zero-configuration networking without many of the security
and robustness issues that regular IPv4 and IPv6 networks have.

The service is off by default.

%package tools
Summary: Nodejs tools for cjdns
Group: Networking/Other
Requires: nodejs
Requires: %name = %EVR
BuildArch: noarch

%description tools
Nodejs tools for cjdns. Highlights:
peerStats          show current peer status
cjdnslog           display cjdroute log
cjdns-traceroute   trace route to cjdns IP
sessionStats       show current crypto sessions

%package python
Summary: Python tools for cjdns
Group: Networking/Other
Requires: python
Requires: %name = %EVR
BuildArch: noarch

%description python
Python tools for cjdns.

%package graph
Summary: Python tools for cjdns
Group: Networking/Other
Requires: %name-python = %EVR
Requires: python-module-networkx
BuildArch: noarch

%description graph
Python graphing tools for cjdns.

%prep
%setup
%patch1 -p1

%build
./do

%install
mkdir -p %buildroot{%_sbindir,%_sysconfdir,%systemd_unitdir,%_exec_prefix/libexec/cjdns}
install -p -m755 cjdroute %buildroot%_sbindir/cjdroute
./cjdroute --genconf > %buildroot%_sysconfdir/cjdroute.conf
install -p -m644 contrib/systemd/cjdns*.service %buildroot%systemd_unitdir
install -pD -m755 cjdns.service %buildroot%_initdir/cjdns
install -p -m755 contrib/sh/run-cjdroute.sh %buildroot%_exec_prefix/libexec/cjdns/run-cjdroute
mkdir -p %buildroot%_sysconfdir/cjdns/up.d

# install c and nodejs tools
mkdir -p %buildroot%_exec_prefix/libexec/cjdns/contrib
install -p publictoip6 privatetopublic mkpasswd makekeys randombytes sybilsim \
        %buildroot%_exec_prefix/libexec/cjdns
rm -f node_modules/nthen/.npmignore
cp -pr tools node_modules %buildroot%_exec_prefix/libexec/cjdns

install -p -m755 cjdns-up.sh %buildroot%_exec_prefix/libexec/cjdns/cjdns-up

# symlinks for selected nodejs tools
mkdir -p %buildroot%_bindir
for t in peerStats sessionStats cjdnslog search dumpLinks dumptable \
         dumpRumorMill pathfinderTree pingAll; do
  ln -sf $(relative %_exec_prefix/libexec/cjdns/tools/$t %_bindir/$t) %buildroot%_bindir/$t
done
for t in traceroute; do
  ln -sf $(relative %_exec_prefix/libexec/cjdns/tools/$t %_bindir/cjdns-$t) %buildroot%_bindir/cjdns-$t
done

# symlinks for selected C tools that don't conflict with other packages
for t in publictoip6 randombytes makekeys; do
  ln -sf $(relative %_exec_prefix/libexec/cjdns/$t %_bindir/$t) %buildroot%_bindir/$t
done

# cjdns-online script
install -pm 755 contrib/systemd/cjdns-online.sh \
        %buildroot%_bindir/cjdns-online

# man pages
mkdir -p %buildroot%_man5dir
install -pm 644 doc/man/cjdroute.conf.5 %buildroot%_man5dir

# install python tools that pull in networkx for graphing
cp -pr contrib/python %buildroot%_exec_prefix/libexec/cjdns

# These files are installed via doc and license
rm %buildroot%_exec_prefix/libexec/cjdns/python/README.md
rm %buildroot%_exec_prefix/libexec/cjdns/python/cjdns-dynamic.conf
rm %buildroot%_exec_prefix/libexec/cjdns/python/cjdnsadmin/bencode.py.LICENSE.txt

# symlink python tools w/o conflict with nodejs tools or needing networkx
for t in pingAll.py trashroutes \
         getLinks ip6topk pktoip6 cjdnsa searches findnodes; do
  ln -sf $(relative %_exec_prefix/libexec/cjdns/python/$t %_bindir/$t) %buildroot%_bindir/$t
done

# symlink python tools that pull in networkx for graphing
for t in drawgraph dumpgraph graphStats; do
  ln -sf $(relative %_exec_prefix/libexec/cjdns/python/$t %_bindir/$t) %buildroot%_bindir/$t
done

%pre
/usr/sbin/groupadd -r -f cjdns ||:
/usr/sbin/useradd -g cjdns -c 'The cjdns daemon' \
        -d /dev/null -s /dev/null -r cjdns >/dev/null 2>&1 ||:

%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

%files
%doc LICENSE
%doc README.md README_*.md HACKING.md
%doc contrib/doc/privatetopublic.md
%doc contrib/doc/sybilsim.md
%doc contrib/doc/cjdns-online.md
%doc contrib/doc/cjdroute.md
%doc contrib/doc/makekeys.md
%doc contrib/doc/publictoip6.md
%doc contrib/doc/randombytes.md
%_sbindir/cjdroute
%attr(0600,root,root) %config(noreplace) %_sysconfdir/cjdroute.conf
%systemd_unitdir/*
%_initdir/cjdns
%dir %_exec_prefix/libexec/cjdns
%dir %_sysconfdir/cjdns
%dir %_sysconfdir/cjdns/up.d
%_exec_prefix/libexec/cjdns/run-cjdroute
%_exec_prefix/libexec/cjdns/cjdns-up
%_exec_prefix/libexec/cjdns/randombytes
%_exec_prefix/libexec/cjdns/publictoip6
%_exec_prefix/libexec/cjdns/privatetopublic
%_exec_prefix/libexec/cjdns/sybilsim
%_exec_prefix/libexec/cjdns/makekeys
%_exec_prefix/libexec/cjdns/mkpasswd
%_bindir/randombytes
%_bindir/publictoip6
%_bindir/makekeys
%_bindir/cjdns-online
%_man5dir/*

%files tools
%doc contrib/doc/traceroute.md
%doc contrib/doc/sessionStats.md
%doc contrib/doc/peerStats.md
%doc contrib/doc/sessionStats.md
%doc contrib/doc/cjdnslog.md
%_exec_prefix/libexec/cjdns/tools
%_exec_prefix/libexec/cjdns/node_modules
%_bindir/peerStats
%_bindir/sessionStats
%_bindir/cjdnslog
%_bindir/dumpRumorMill
%_bindir/dumpLinks
%_bindir/pathfinderTree
%_bindir/dumptable
%_bindir/pingAll
%_bindir/search
%_bindir/cjdns-traceroute

%files python
%doc contrib/python/cjdnsadmin/bencode.py.LICENSE.txt
%doc contrib/python/README.md contrib/python/cjdns-dynamic.conf
%dir %_exec_prefix/libexec/cjdns/python
%_exec_prefix/libexec/cjdns/python/cexec
%_exec_prefix/libexec/cjdns/python/cjdnsadminmaker.py*
%_exec_prefix/libexec/cjdns/python/cjdnslog
%_exec_prefix/libexec/cjdns/python/dumptable
%_exec_prefix/libexec/cjdns/python/dynamicEndpoints.py*
%_exec_prefix/libexec/cjdns/python/peerStats
%_exec_prefix/libexec/cjdns/python/sessionStats
%_exec_prefix/libexec/cjdns/python/cjdnsadmin
%_exec_prefix/libexec/cjdns/python/pingAll.py*
%_exec_prefix/libexec/cjdns/python/trashroutes
%_exec_prefix/libexec/cjdns/python/getLinks
%_exec_prefix/libexec/cjdns/python/ip6topk
%_exec_prefix/libexec/cjdns/python/pktoip6
%_exec_prefix/libexec/cjdns/python/cjdnsa
%_exec_prefix/libexec/cjdns/python/searches
%_exec_prefix/libexec/cjdns/python/findnodes
%_bindir/pingAll.py
%_bindir/trashroutes
%_bindir/getLinks
%_bindir/ip6topk
%_bindir/pktoip6
%_bindir/cjdnsa
%_bindir/searches
%_bindir/findnodes

%files graph
%_exec_prefix/libexec/cjdns/python/drawgraph
%_exec_prefix/libexec/cjdns/python/dumpgraph
%_exec_prefix/libexec/cjdns/python/graphStats
%_bindir/drawgraph
%_bindir/dumpgraph
%_bindir/graphStats

%changelog
* Wed May 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20.3-alt1
- Updated to upstream version 20.3.

* Tue Oct 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20.2-alt1
- Updated to upstream version 20.2.

* Wed Feb 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20.1-alt1
- Updated to upstream version 20.1.

* Wed Sep 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 20-alt2
- Updated build dependencies.

* Tue Sep 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 20-alt1
- Updated to upstream version 20.
- Built with support of %%ubt macro.

* Tue Jun 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 19.1-alt1
- First build for ALT
