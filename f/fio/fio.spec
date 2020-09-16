%def_enable gfio
%def_enable numa
%def_enable gfapi
%def_enable rdmacm
%ifarch %ix86 %arm %mips32 ppc
%def_disable rbd
%else
%def_enable rbd
%endif
%def_enable http

Name: fio
Version: 3.23
Release: alt1

Summary: IO testing tool
License: GPLv2
Group: System/Kernel and hardware

Url: http://git.kernel.dk/?p=fio.git;a=summary
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libaio-devel zlib-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%{?_enable_gfio:BuildRequires: libgtk+2-devel}
%{?_enable_numa:BuildRequires: libnuma-devel }
%{?_enable_rbd:BuildRequires: ceph-devel}
%{?_enable_gfapi:BuildRequires: libglusterfs-devel}
%{?_enable_rdmacm:BuildRequires: librdmacm-devel}
%{?_enable_http:BuildRequires: libcurl-devel libssl-devel}

Conflicts: python3-module-fiona

%description
fio is a tool that will spawn a number of threads or processes doing a
particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.


%package tools
Summary: Analyze tools for %name
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description tools
fio2gnuplot - analyze a set of fio's log files to turn them into a set of graphical traces using gnuplot tool.
fio_generate_plots - Generate plots for Flexible I/O Tester

%package -n gfio
Summary: Gtk frontend for %name
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description -n gfio
fio is a tool that will spawn a number of threads or processes doing a
particular type of io action as specified by the user. fio takes a
number of global parameters, each inherited by the thread unless
otherwise parameters given to them overriding that setting is given.
The typical use of fio is to write a job file matching the io load
one wants to simulate.

This package conteon gtk frontend for %name


%prep
%setup
%patch -p1
find tools -type f | xargs subst "s|/usr/bin/python2.7|%__python3|"

%build
./configure \
	--prefix=%_prefix \
	--disable-optimizations \
	%{subst_enable gfio} \
	--extra-cflags="%optflags"

%make_build V=1 EXTFLAGS="%optflags"
%make_build -C doc html SPHINXBUILD=sphinx-build-3

%install
%make_install DESTDIR=%buildroot install prefix=%_prefix mandir=%_mandir

%files
%doc HOWTO README REPORTING-BUGS examples doc/output/html
%_bindir/genfio
%_bindir/%name
%_man1dir/%name.1.*

%files tools
%_bindir/*
%_datadir/%name
%_man1dir/*
%exclude %_bindir/gfio
%exclude %_bindir/fio
%exclude %_bindir/genfio
%exclude %_man1dir/%name.1.*

%files -n gfio
%_bindir/gfio

%changelog
* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 3.23-alt1
- new version 3.23 (with rpmrb script)

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.17-alt1.1
- NMU: real drop python2 deps

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.17-alt1
- NMU: build new version
- use libglusterfs-devel instead of libglusterfs3-devel
- use python3 only

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 3.13-alt1
- 3.13
- disable support ceph on 32-bit arch
- build with http support for WebDAV and S3

* Tue Aug 29 2017 Terechkov Evgenii <evg@altlinux.org> 3.0-alt2
- Build documentation

* Tue Aug 29 2017 Terechkov Evgenii <evg@altlinux.org> 3.0-alt1
- 3.0

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.12-alt1
- 2.12
- build with support numa, ceph, gluster, rdmacm

* Sun Jan 19 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.4-alt1
- 2.1.4
- add packages fio-tools and gfio

* Thu Dec 13 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.11-alt1
- 2.0.11

* Fri Nov 30 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.10-alt1
- 2.0.10

* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 2.0.7-alt1
- 2.0.7

* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 2.0.6-alt1
- 2.0.6

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.59-alt1
- 1.59

* Fri Jul 22 2011 Victor Forsiuk <force@altlinux.org> 1.57-alt1
- 1.57

* Sun Jun 12 2011 Victor Forsiuk <force@altlinux.org> 1.55-alt1
- 1.55

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 1.37-alt1
- 1.36 -> 1.37

* Wed Dec 16 2009 Igor Zubkov <icesik@altlinux.org> 1.36-alt1
- 1.34 -> 1.36

* Thu Oct 01 2009 Igor Zubkov <icesik@altlinux.org> 1.34-alt1
- 1.24 -> 1.34

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 1.24-alt1
- 1.23 -> 1.24

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.23-alt1
- 1.21 -> 1.23

* Sat Jul 19 2008 Igor Zubkov <icesik@altlinux.org> 1.21-alt1
- 1.17.2 -> 1.21

* Thu Nov 01 2007 Igor Zubkov <icesik@altlinux.org> 1.17.2-alt1
- build for Sisyphus

