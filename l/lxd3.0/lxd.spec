%global import_path github.com/lxc/lxd

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no rpath=relaxed
%add_debuginfo_skiplist %go_root %_bindir

%define lxdgroup lxd
%define lxduser lxd

Name: lxd3.0
Version: 3.0.4
Release: alt1
Summary: LXD -- REST API, command line tool and OpenStack integration plugin for LXC

Group: Development/Other
License: Apache-2.0
Url: https://%import_path

Source: %name-%version.tar
#Patch:		%name-%version-%release.patch
Source3: lxd.default
Source4: lxd.dnsmasq

# services
Source11: lxd.service
Source12: lxd.socket
Source13: lxd-startup.service

Provides: lxd = %EVR
Conflicts: lxd

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

Requires: shadow-submap
Requires: lxc-libs
Requires: lxcfs
Requires: btrfs-progs
Requires: lvm2
Requires: squashfs-tools
#Requires: liblxd_sqlite3
Requires: rsync
Requires: iptables
Requires: dnsmasq

BuildRequires: libcap-devel
BuildRequires: libuv-devel
BuildRequires: libudev-devel
BuildRequires: libraft-devel
BuildRequires: libco-devel

BuildRequires: help2man
# Needed for manpages generation. Accessing to '/proc/self/...'
BuildRequires: /proc

BuildRequires: lxc-devel
BuildRequires: libacl-devel

#BuildRequires: liblxd_sqlite3-devel
#BuildRequires: libdqlite-devel
#or
# build for sqlite3
BuildRequires: libreadline-devel
BuildRequires: zlib-devel
BuildRequires: tcl-devel

%description
REST API, command line tool and OpenStack integration plugin for LXC.

%prep
%setup
#%%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR"
export CGO_ENABLED=1

mkdir $BUILDDIR
mv dist/src $BUILDDIR/
%golang_prepare

cd .build/src/%import_path

# from Makefile
ln -s $PWD/dist $BUILDDIR/deps
pushd $BUILDDIR/deps/sqlite
%autoreconf
%configure --enable-replication --disable-amalgamation --disable-tcl --libdir=%_libdir/%name
%make_build all sqlite3.pc
popd

pushd $BUILDDIR/deps/dqlite
%autoreconf
export PKG_CONFIG_PATH="$BUILDDIR/deps/sqlite/"
%configure --disable-silent-rules --libdir=%_libdir/%name
%make_build CFLAGS="-I$BUILDDIR/deps/sqlite/" LDFLAGS="-L$BUILDDIR/deps/sqlite/.libs/"
popd

# Need to use a patched version of libsqlite
export TAGS="libsqlite3"
#export CGO_CPPFLAGS="$(pkg-config --cflags lxd_sqlite3)"
#export CGO_LDFLAGS="$(pkg-config --libs lxd_sqlite3)"
#%golang_build lxd lxc fuidshift lxd-benchmark lxd-p2c lxc-to-lxd lxd/db

export CGO_CFLAGS="-I$GOPATH/deps/sqlite/ -I$GOPATH/deps/dqlite/include/"
export CGO_LDFLAGS="-L$GOPATH/deps/sqlite/.libs/ -L$GOPATH/deps/dqlite/.libs/ -Wl,-rpath,%_libdir/%name"
export LD_LIBRARY_PATH="$GOPATH/deps/sqlite/.libs/:$GOPATH/deps/dqlite/.libs/"
go install -v -tags libsqlite3 ./...
go install -v -tags libsqlite3 ./lxc
CGO_ENABLED=0 go install -v -tags netgo ./lxd-p2c

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

pushd $BUILDDIR/deps/sqlite
%makeinstall_std
popd

pushd $BUILDDIR/deps/dqlite
%makeinstall_std
popd

%golang_install

# lxc-bridge
mkdir -p -- %buildroot%_libexecdir/lxd

# configuration
install -D %SOURCE3 %buildroot%_sysconfdir/sysconfig/lxd
# configuration for dnsmasq called in lxd-bridge
install -D %SOURCE4 %buildroot%_sysconfdir/lxd/dnsmasq.conf

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
mkdir -p %buildroot%_localstatedir/lxd
mkdir -p %buildroot%_logdir/lxd

# Install the manpages
export LD_LIBRARY_PATH=%buildroot%_libdir/%name
mkdir -p %buildroot%_man1dir
help2man %buildroot%_bindir/fuidshift -n "uid/gid shifter" --no-info --no-discard-stderr > %buildroot%_man1dir/fuidshift.1
help2man %buildroot%_bindir/lxc-to-lxd -n "Convert LXC containers to LXD" --no-info --version-string=%version --no-discard-stderr > %buildroot%_man1dir/lxc-to-lxd.1
help2man %buildroot%_bindir/lxd-benchmark -n "The container lightervisor - benchmark" --no-info --no-discard-stderr > %buildroot%_man1dir/lxd-benchmark.1
%buildroot%_bindir/lxd manpage %buildroot%_man1dir/
%buildroot%_bindir/lxc manpage %buildroot%_man1dir/

# cleanup
rm -r %buildroot%go_path
rm -r %buildroot%_includedir
rm %buildroot%_bindir/{deps,macaroon-identity,sqlite3}
rm -r %buildroot%_libdir/%name/pkgconfig
rm %buildroot%_libdir/%name/{*.a,*.la,*.so}

%pre
%_sbindir/groupadd -r -f %lxdgroup 2>/dev/null || :
%_sbindir/useradd  -r -g %lxdgroup -c "LXD daemon" \
   -s /dev/null -d /dev/null %lxduser 2>/dev/null || :

%files
%doc AUTHORS COPYING
%config(noreplace) %_sysconfdir/sysconfig/*
%dir %_sysconfdir/lxd
%config(noreplace) %_sysconfdir/lxd/dnsmasq.conf
%_bindir/*
%_libdir/%name
#dir %_libexecdir/lxd
#_libexecdir/lxd/*
%_unitdir/*
%_datadir/bash-completion/completions/*
%_man1dir/*
%attr(0751,%lxduser,%lxdgroup) %dir %_localstatedir/lxd
%attr(0751,%lxduser,%lxdgroup) %dir %_logdir/lxd

%changelog
* Sun May 17 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.4-alt1
- build 3.0/stable as lxd3 package
