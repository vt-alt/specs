%def_enable boost
%def_disable boost_pool
%def_enable system_asio

Name: galera
Version: 26.4.5
Release: alt1
Summary: Synchronous multi-master wsrep provider (replication engine)
Group: System/Servers
License: GPLv2
Url: http://galeracluster.com/
# VCS-git: https://github.com/codership/galera.git
Source: %name-%version.tar

Source1: garbd.init
Source2: garbd.service
Source3: garbd.tmpfiles
Source4: garbd.conf

# git submodules
Source100: wsrep.tar

ExcludeArch: %arm

BuildRequires: gcc-c++ scons
%{?_enable_boost:BuildRequires: boost-devel boost-program_options-devel}
%{?_enable_system_asio:BuildRequires: asio-devel}

BuildRequires: libcheck-devel libssl-devel zlib-devel

%description
Galera is a fast synchronous multi-master wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see http://launchpad.net/wsrep. For a description of Galera
replication engine see http://www.codership.com.

%package garbd
Summary: Galera arbitrator
Group: System/Servers

%description garbd
Galera is a fast synchronous multi-master wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see http://launchpad.net/wsrep. For a description of Galera
replication engine see http://www.codership.com.

This package contain Galera arbitrator.

%package -n libgalera_smm
Summary: Synchronous multi-master wsrep provider (replication engine)
Group: System/Libraries

%description -n libgalera_smm
Galera is a fast synchronous multi-master wsrep provider (replication engine)
for transactional databases and similar applications. For more information
about wsrep API see http://launchpad.net/wsrep. For a description of Galera
replication engine see http://www.codership.com.

%prep
%setup
tar -xf %SOURCE100 -C wsrep/src

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
export CPPFLAGS="%optflags"
scons %{?_smp_mflags} \
    revno=%release \
    %{?_disable_boost:boost=0} \
    %{?_enable_boost_pool:boost_pool=1} \
    %{?_disable_system_asio:system_asio=0} \
    strict_build_flags=0

%install
install -D -m 755 %SOURCE1 %buildroot%_initdir/garbd
install -D -m 644 %SOURCE2 %buildroot%_unitdir/garbd.service
mkdir -p %buildroot%_runtimedir/garbd
install -D -m 644 %SOURCE3 %buildroot%_tmpfilesdir/garbd.conf
install -D -m 644 %SOURCE4 %buildroot%_sysconfdir/garbd/garbd.conf
install -D -m 755 garb/garbd %buildroot%_sbindir/garbd
install -D -m 644 libgalera_smm.so %buildroot%_libdir/galera/libgalera_smm.so
install -D -m 644 COPYING %buildroot%_docdir/galera/COPYING
install -D -m 644 asio/LICENSE_1_0.txt %buildroot%_docdir/galera/LICENSE.asio
install -D -m 644 www.evanjones.ca/LICENSE %buildroot%_docdir/galera/LICENSE.crc32
install -D -m 644 scripts/packages/README %buildroot%_docdir/galera/README
install -D -m 644 scripts/packages/README-MySQL %buildroot%_docdir/galera/README-MySQL

%post garbd
%post_service garbd

%preun garbd
%preun_service garbd

%files -n libgalera_smm
%dir %_libdir/galera
%_libdir/galera/libgalera_smm.so

%files garbd
%dir %_sysconfdir/garbd
%config(noreplace) %_sysconfdir/garbd/garbd.conf
%dir %_docdir/galera
%_sbindir/garbd
%_unitdir/garbd.service
%_initdir/garbd
%_tmpfilesdir/garbd.conf
%_runtimedir/garbd
%doc %_docdir/galera/COPYING
%doc %_docdir/galera/LICENSE.asio
%doc %_docdir/galera/LICENSE.crc32
%doc %_docdir/galera/README
%doc %_docdir/galera/README-MySQL

%changelog
* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 26.4.5-alt1
- 26.4.5

* Mon Dec 16 2019 Alexey Shabalin <shaba@altlinux.org> 26.4.3-alt1
- 26.4.3

* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 26.4.2-alt1
- 26.4.2

* Wed Apr 17 2019 Alexey Shabalin <shaba@altlinux.org> 25.3.26-alt1
- 25.3.26

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 25.3.25-alt1
- 25.3.25

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 25.3.24-alt1
- 25.3.24

* Fri Aug 31 2018 Alexey Shabalin <shaba@altlinux.org> 25.3.23-alt2
- rebuild with openssl-1.1
- build with system asio-devel

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 25.3.23-alt1
- 25.3.23

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 25.3.22-alt2
- NMU: rebuilt with boost-1.67.0

* Tue Nov 07 2017 Alexey Shabalin <shaba@altlinux.ru> 25.3.22-alt1
- 25.3.22

* Fri May 05 2017 Alexey Shabalin <shaba@altlinux.ru> 25.3.20-alt1
- 25.3.20

* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 25.3.19-alt1
- 25.3.19

* Wed Jul 06 2016 Alexey Shabalin <shaba@altlinux.ru> 25.3.16-alt1
- 25.3.16

* Fri Mar 18 2016 Alexey Shabalin <shaba@altlinux.ru> 25.3.15-alt1
- 25.3.15

* Fri Sep 04 2015 Alexey Shabalin <shaba@altlinux.ru> 25.3.12-alt3
- run daemon garbd as nobody user

* Fri Sep 04 2015 Alexey Shabalin <shaba@altlinux.ru> 25.3.12-alt2
- split galera arbitrator and wsrep provider to different packages

* Thu Sep 03 2015 Alexey Shabalin <shaba@altlinux.ru> 25.3.12-alt1
- Initial build
