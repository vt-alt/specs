Name: glusterfs-coreutils
Version: 0.3.1
Release: alt1

Summary: Core Utilities for the Gluster Distributed File System

License: GPLv3
Group: System/Base
Url: https://github.com/gluster/glusterfs-coreutils

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildRequires: gcc-c++ gnulib help2man libreadline-devel libstdc++-devel

BuildRequires: libglusterfs-api-devel >= 3.6.0
BuildRequires: help2man >= 1.36

#Requires: libglusterfs3-api >= 3.6.0

# Source-url: https://github.com/gluster/glusterfs-coreutils/archive/v%version.tar.gz
Source: %name-%version.tar

%description
gluster-coreutils provides a set of basic utilities such as cat, mkdir, ls, and
tail that are implemented specifically using the GlusterFS API.

%prep
%setup
%__subst "s|m4_esyscmd(.*)|[%version]|" ./configure.ac
%__subst "s|1\.15|1.14|" ./configure.ac
gnulib-tool --import human

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/gfcat
%_bindir/gfcli
%_bindir/gfcp
%_bindir/gfls
%_bindir/gfmkdir
%_bindir/gfput
%_bindir/gfrm
%_bindir/gfstat
%_bindir/gftail
%_bindir/gftouch
%_bindir/gftruncate
%_bindir/gfclear
%_bindir/gfmv
%_bindir/gfrmdir

%_man1dir/gfcat.1.*
%_man1dir/gfcli.1.*
%_man1dir/gfcp.1.*
%_man1dir/gfls.1.*
%_man1dir/gfmkdir.1.*
%_man1dir/gfput.1.*
%_man1dir/gfrm.1.*
%_man1dir/gfstat.1.*
%_man1dir/gftail.1.*
%_man1dir/gftouch.1.*
%_man1dir/gftruncate.1.*
%_man1dir/gfrmdir.1.xz

%changelog
* Sun Jan 19 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version (0.3.1) with rpmgs script
- switch to build from tarball

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1.1
- autorebuild with libreadline7

* Sat Dec 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- new version 0.2.0 (with rpmrb script)

* Wed Nov 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1
- build from https://github.com/moonblade/glusterfs-coreutils.git

* Wed Jun 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.0-alt1
- initial build for ALT Linux Sisyphus

