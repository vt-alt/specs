%def_disable zmq
%def_with docs
%def_with python

%define _pseudouser_user     _teamd
%define _pseudouser_group    _teamd

Name: libteam
Version: 1.30
Release: alt1

Summary: Library for controlling team network device
License: LGPLv2.1+
Group: System/Libraries
URL: http://www.libteam.org
Vcs: https://github.com/jpirko/libteam
Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: libnl-devel
BuildRequires: libdaemon-devel
BuildRequires: libjansson-devel
BuildRequires: libdbus-devel
BuildRequires: libcap-devel
%{?_with_python:BuildRequires: python3-devel python3-module-setuptools swig}
%{?_enable_zmq:BuildRequires: libzeromq-devel}
%{?_with_docs:BuildRequires: doxygen}

%define _unpackaged_files_terminate_build 1

%description
This package contains a library which is a user-space
counterpart for team network driver. It provides an API
to control team network devices.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: This package contains development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Requires: %name-devel = %version-%release

%description devel-doc
This package contains development documentation for %name

%package -n libteamdctl
Summary: Library for communication with teamd
Group: System/Libraries

%description -n libteamdctl
This is a library for communication with teamd process (via D-Bus,
Unix socket or zeromq). It is used by the teamdctl utility.

%package -n libteamdctl-devel
Summary: Development files for libteamdctl
Group: Development/C
Requires: libteamdctl = %version-%release

%description -n libteamdctl-devel
This package contains libraries and header files for
developing applications that use libteamdctl.

%package utils
Summary: Command line interface utils for %name and teamd
Group: System/Base

%description utils
This package contains various libteam utils.

%package -n teamd
Summary: Team network device control daemon
Group: System/Servers
Requires: %name = %version-%release

%description -n teamd
This package contains team network device control daemon.

%if_with python
%package -n python3-module-team
Summary: Team network device library bindings for Python3
Group: Development/Python3
Requires: %name = %version-%release

%description -n python3-module-team
This package contains a module that permits applications
written in the Python3 programming language to use the interface
supplied by team network device library.
%endif

%prep
%setup
%patch -p1
%if_with docs
# prepare example dir for -devel
mkdir -p _tmpdoc1/examples
cp -p examples/*.c _tmpdoc1/examples
%endif
%if_with python
# prepare example dir for python module
mkdir -p _tmpdoc2/examples
cp -p examples/python/*.py _tmpdoc2/examples
chmod -x _tmpdoc2/examples/*.py
%endif

%build
%autoreconf
%configure \
	--disable-static \
	%{subst_enable zmq} \
	--enable-dbus \
	--with-user=%_pseudouser_user \
	--with-group=%_pseudouser_group \
	--disable-silent-rules
%make_build
%if_with docs
%make_build html
%endif
%if_with python
cd binding/python
%python3_build
%endif

%install
%makeinstall_std
install -pDm 0644 teamd/dbus/teamd.conf %buildroot%_datadir/dbus-1/system.d/teamd.conf
install -pDm 0644 teamd/redhat/systemd/teamd@.service %buildroot%_unitdir/teamd@.service
%if_with python
cd binding/python
%python3_install
install -pm 0644 team/capi.py %buildroot%python3_sitelibdir/team/
%endif

%pre -n teamd
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'teamd user' \
        -d /dev/null -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%files
%_libdir/libteam.so.*

%files devel
%_includedir/team.h
%_libdir/libteam.so
%_pkgconfigdir/libteam.pc

%if_with docs
%files devel-doc
%doc _tmpdoc1/examples doc/api
%endif

%files -n libteamdctl
%_libdir/libteamdctl.so.*

%files -n libteamdctl-devel
%_includedir/teamdctl.h
%_libdir/libteamdctl.so
%_pkgconfigdir/libteamdctl.pc

%files utils
%_bindir/bond2team
%_bindir/teamnl
%_man1dir/bond2team.1*
%_man8dir/teamnl.8*

%files -n teamd
%doc teamd/example_configs
%_datadir/dbus-1/system.d/teamd.conf
%_unitdir/teamd@.service
%_bindir/teamd*
%_man5dir/teamd.conf.5*
%_man8dir/teamd*.8*

%if_with python
%files -n python3-module-team
%doc _tmpdoc2/examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 09 2020 Mikhail Efremov <sem@altlinux.org> 1.30-alt1
- Use Vcs tag.
- Don't use rpm-build-licenses.
- 1.29 -> 1.30.

* Fri Jul 05 2019 Mikhail Efremov <sem@altlinux.org> 1.29-alt1
- 1.28 -> 1.29.

* Mon Dec 10 2018 Mikhail Efremov <sem@altlinux.org> 1.28-alt1
- Use python3 in shebangs.
- Build python3 module instead of python2.
- 1.27 -> 1.28.

* Fri Oct 06 2017 Mikhail Efremov <sem@altlinux.org> 1.27-alt2
- Fix python module build.
- Switch to _teamd user.
- Make build of python module optional.

* Wed Oct 04 2017 Mikhail Efremov <sem@altlinux.org> 1.27-alt1
- Initial build

