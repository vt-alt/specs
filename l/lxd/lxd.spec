%global import_path github.com/lxc/lxd

#global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
#add_debuginfo_skiplist %go_root %_bindir

%define lxdgroup lxd
%define lxduser lxd

Name:		lxd
Version:	4.0.1
Release:	alt1
Summary:	LXD -- REST API, command line tool and OpenStack integration plugin for LXC.

Group:		Development/Other
License:	Apache-2.0
URL:		https://%import_path

Packager:	Denis Pynkin <dans@altlinux.ru>

Source0:	%name-%version.tar
Patch:		%name-%version-%release.patch
Source3:	lxd.default
Source4:	lxd.dnsmasq

# services
Source11:	lxd.service
Source12:	lxd.socket
Source13:	lxd-startup.service


ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

Requires:	shadow-submap
Requires:	lxc-libs
Requires:	lxcfs
Requires:	btrfs-progs
Requires:	lvm2
Requires:	squashfs-tools
Requires:	liblxd_sqlite3
Requires:	rsync
Requires:	iptables
Requires:	dnsmasq

BuildRequires: libcap-devel
BuildRequires: libuv-devel

BuildRequires: liblxd_sqlite3-devel
BuildRequires: libdqlite-devel
BuildRequires: libraft-devel
BuildRequires: libco-devel
BuildRequires: libudev-devel
BuildRequires: help2man
# Needed for manpages generation. Accessing to '/proc/self/...'
BuildRequires: /proc

BuildRequires:	lxc-devel
BuildRequires:	libacl-devel

%description
REST API, command line tool and OpenStack integration plugin for LXC.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch
Requires: golang

%description devel
%summary
This package contains library source intended for building other packages
which use the supplementary Go tools libraries with %import_path imports.


%prep
%setup -q
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"
export CGO_ENABLED=1

%golang_prepare

cd .build/src/%import_path

# Need to use a patched version of libsqlite
export TAGS="libsqlite3"
export CGO_CPPFLAGS="$(pkg-config --cflags lxd_sqlite3)"
export CGO_LDFLAGS="$(pkg-config --libs lxd_sqlite3)"
%golang_build lxd lxc fuidshift lxd-benchmark lxd-p2c lxc-to-lxd lxd/db

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

mkdir -p -- %buildroot/%go_root/bin
for f in %buildroot/%_bindir/*; do
	[ -x "$f" ] || continue
	f="${f##*/}"
	what="$(relative %_bindir/$f %go_root/bin/$f)"
	ln -s -- "$what" %buildroot/%go_root/bin/$f
done

# lxc-bridge
mkdir -p -- %buildroot%_libexecdir/lxd

# configuration
%__install -D %SOURCE3 %buildroot%_sysconfdir/sysconfig/lxd
# configuration for dnsmasq called in lxd-bridge
%__install -D %SOURCE4 %buildroot%_sysconfdir/lxd/dnsmasq.conf

#services
# systemd
mkdir -p %buildroot%_unitdir
cp -av %SOURCE11 %buildroot%_unitdir/
cp -av %SOURCE12 %buildroot%_unitdir/
cp -av %SOURCE13 %buildroot%_unitdir/

# install bash completion
mkdir -p %buildroot%_datadir/bash-completion/completions/
cp -av scripts/bash/lxd-client %buildroot%_datadir/bash-completion/completions/

# /var/{lib,log}/lxd
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name

# Install the manpages
mkdir -p %buildroot%_man1dir
help2man %buildroot%_bindir/fuidshift -n "uid/gid shifter" --no-info --no-discard-stderr > %buildroot%_man1dir/fuidshift.1
help2man %buildroot%_bindir/lxc-to-lxd -n "Convert LXC containers to LXD" --no-info --version-string=%version --no-discard-stderr > %buildroot%_man1dir/lxc-to-lxd.1
help2man %buildroot%_bindir/lxd-benchmark -n "The container lightervisor - benchmark" --no-info --no-discard-stderr > %buildroot%_man1dir/lxd-benchmark.1
%buildroot%_bindir/lxd manpage %buildroot%_man1dir/
%buildroot%_bindir/lxc manpage %buildroot%_man1dir/

%pre
%_sbindir/groupadd -r -f %lxdgroup 2>/dev/null || :
%_sbindir/useradd  -r -g %lxdgroup -c "LXD daemon" \
   -s /dev/null -d /dev/null %lxduser 2>/dev/null || :

%files
%doc AUTHORS COPYING
%_bindir/*
%go_root/bin/*
%attr(0751,%lxduser,%lxdgroup) %dir %_localstatedir/%name
%attr(0751,%lxduser,%lxdgroup) %dir %_logdir/%name
#dir %_libexecdir/lxd
#_libexecdir/lxd/*

%_unitdir/*

%_datadir/bash-completion/completions/*

%config(noreplace) %_sysconfdir/sysconfig/*
%dir %_sysconfdir/lxd
%config(noreplace) %_sysconfdir/lxd/dnsmasq.conf

%_man1dir/*

%files devel
%go_path/src/*
%exclude %go_path/src/%import_path/vendor
%exclude %go_path/src/%import_path/go.mod
%exclude %go_path/src/%import_path/go.sum

%changelog
* Sun May 17 2020 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- New LTS version.

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 4.0.0-alt1
- New version.

* Tue Nov 12 2019 Denis Pynkin <dans@altlinux.org> 3.18-alt1
- New version
- Have to checkout module with:
  go get github.com/spf13/cobra@77e4d5aecc4d34e58f72e5a1c4a5a13ef55e6f44
- Fix help2man call
- Added new build requirements to libraft and libco

* Mon Sep 30 2019 Denis Pynkin <dans@altlinux.org> 3.17-alt1
- New version

* Sun Jun 02 2019 Mikhail Gordeev <obirvalger@altlinux.org> 3.10-alt3
- Add rsync, iptables and dnsmasq to requires

* Wed Mar 13 2019 Mikhail Gordeev <obirvalger@altlinux.org> 3.10-alt2
- Fix build by vendorizing build dependencies

* Wed Feb 13 2019 Denis Pynkin <dans@altlinux.org> 3.10-alt1
- Update

* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 3.8-alt1
- Update
- Add manpages generation

* Sun Jun 24 2018 Denis Pynkin <dans@altlinux.org> 3.2-alt1
- Update

* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 3.0.0-alt1
- new version

* Wed Sep 06 2017 Denis Pynkin <dans@altlinux.org> 2.17-alt1
- new version 2.17

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 2.16-alt1
- new version 2.16

* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 2.15-alt1
- new version 2.15

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.11-alt1
- new version

* Sat Nov 26 2016 Denis Pynkin <dans@altlinux.org> 2.6.2-alt1
- new version 2.6.2

* Sat Nov 26 2016 Denis Pynkin <dans@altlinux.org> 2.6-alt2
- Added cgmanager dependency back
- Patch included

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.6-alt1
- new version 2.6

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.4.1-alt1
- Release 2.4

* Sat Oct 01 2016 Denis Pynkin <dans@altlinux.org> 2.3.0-alt1
- Release 2.3
- Removed cgmanager dependency
- Removed lxd-bridge due new network API

* Mon Sep 26 2016 Denis Pynkin <dans@altlinux.org> 2.2.0-alt1
- Release 2.2
- Fixed lxc-to-lxd script

* Wed Aug 24 2016 Denis Pynkin <dans@altlinux.org> 2.1.0-alt3
- configuration fixes for lxd-bridge service

* Wed Aug 24 2016 Denis Pynkin <dans@altlinux.org> 2.1.0-alt2
- Added squashfs-tools in Requires

* Tue Aug 23 2016 Denis Pynkin <dans@altlinux.org> 2.1.0-alt1
- Release 2.1

* Thu Apr 14 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt3
- Release 2.0

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt2.rc2
- Version update

* Thu Mar 03 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt2.rc1
- Added LXD bridge start/stop and configuration
- Version update

* Mon Feb 29 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt1.beta4
- rebuild with new lxc

* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.beta4
- Version update

* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.beta3
- Version update

* Mon Feb 15 2016 Denis Pynkin <dans@altlinux.ru> 2.0.0-alt0.beta2
- Initial version
- Taken init scripts from Ubuntu
