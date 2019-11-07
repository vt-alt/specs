# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-tcl rpm-helper
BuildRequires: libelf-devel perl(Curses.pm) perl(ExtUtils/testlib.pm) perl(Sys/Hostname.pm) perl(Time/Local.pm) perl(autouse.pm) perl(subs.pm) pkgconfig(check) zlib-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name torque
%define version 6.1.2
%define         _disable_ld_no_undefined   1

%define         major              2
%define         libname            lib%{name}%{major}
%define         devname            lib%{name}-devel

%define         clientname         %{name}-client
%define         servername         %{name}-server
%define         schedname          %{name}-sched
%define         momname            %{name}-mom
%define         guiname            %{name}-gui


#default is /var/spool/torque: if you change this, you'll break some
#scripts coming along with the source files
%define         torquedir          /var/spool/torque
%define         srcversion         %{version}

Name:           torque
Summary:        The Torque resource and queue manager
Group:          Sciences/Computer science
Version:        6.1.2
Release:        alt2_3
License:        TORQUEv1.1
URL:            http://www.adaptivecomputing.com/products/open-source/torque/

Source0:        %{name}-%{srcversion}.tar.gz
Source1:        mom_config
Source2:        README.mga
Source3:        pbs_mom.service
Source4:        pbs_sched.service
Source5:        pbs_server.service
Source6:        trqauthd.service
Source7:        torque_addport
Source8:        torque_createdb
Source9:        openmp.pbs
Patch1:         torque-6.1.1.1-gcc7.patch

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  groff-base groff-dvi groff-extra groff-lbp groff-lj4
BuildRequires:  groff-base groff-ps
BuildRequires:  xauth
BuildRequires:  gperf
BuildRequires:  graphviz
BuildRequires:  texlive
BuildRequires:  texlive-texmf
BuildRequires:  doxygen
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  tclx
BuildRequires:  openssh-clients
BuildRequires:  libreadline-devel
BuildRequires:  gcc-fortran
BuildRequires:  gcc-c++
%ifarch %ix86 x86_64
BuildRequires:  libquadmath-devel
%endif
BuildRequires:  libpam0-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  boost-complete

Requires:       openssh-clients
Requires:     torque-mom
Source44: import.info

%description
The Tera-scale Open-source Resource and QUEue manager provides control
over batch jobs and distributed computing resources. It is an advanced
open-source product based on the original PBS project* and
incorporates the best of both community and professional
development. It incorporates significant advances in the areas of
scalability, reliability, and functionality and is currently in use at
tens of thousands of leading government, academic, and commercial
sites throughout the world. Please check out the README.mga file provided in
%{_docdir}/%{name} for setting up a minimal running system.

"TORQUE is a modification of OpenPBS which was developed by NASA Ames
Research Center, Lawrence Livermore National Laboratory, and Veridian
Information Solutions, Inc. Visit www.clusterresources.com/products/
for more information about TORQUE and to download TORQUE".



%package -n     %{libname}
Summary:        Shared libraries for Torque
Group:          System/Libraries
Provides:       lib%{name} = %{version}-%{release}

%description -n %{libname}
%{summary}.



%package -n     %{devname}
Summary:        Development files for Torque
Group:          Development/Other
Requires:       %{libname} = %{version}-%{release}
Provides:       lib%{name}-devel  = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{devname}
%{summary}.



%package -n    %{clientname}
Summary:        Command line utilities for Torque
Group:          System/Kernel and hardware
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}

%description -n %{clientname}
%{summary}.



%package -n     %{servername}
Summary:        The Torque server
Group:          System/Kernel and hardware
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:     %{schedname} = %{version}-%{release}
Requires(post): rpm-helper
Requires(preun):rpm-helper

%description -n %{servername}
%{summary}.



%package -n     %{schedname}
Summary:        The scheduler for Torque server
Group:          System/Kernel and hardware
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       %{servername} = %{version}-%{release}
Requires(post): rpm-helper
Requires(preun):rpm-helper

%description -n %{schedname}
%{summary}.



%package -n     %{momname}
Summary:        Node manager programs for Torque
Group:          System/Kernel and hardware
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       openssh-server
Requires(post): rpm-helper
Requires(preun):rpm-helper

%description -n %{momname}
%{summary}.



%package -n     %{guiname}
Summary:        Graphical clients for Torque
Group:          Monitoring
Requires:       tk
Requires:       tcl
Requires:       %{libname} = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-client = %{version}-%{release}
Obsoletes:      torque-xpbs <= 2.5.3

%description -n %{guiname}
%{summary}.


%prep
%setup -q -n %{name}-%{srcversion}
%patch1 -p1


%build
autoreconf -fi
# -fpermissive added to downgrade numerous 'invalid conversion' errors to warnings
export CPPFLAGS="-DUSE_INTERP_RESULT -DUSE_INTERP_ERRORLINE -DHAVE_STDBOOL_H -fpermissive"
%configure \
                --srcdir=%{_builddir}/%{name}-%{srcversion} \
                --includedir=%{_includedir}/%{name} \
                --with-pam=%{_libdir}/security \
                --with-rcp=scp \
                --with-hwloc-path=%{_prefix} \
                --enable-docs \
                --enable-server \
                --enable-mom \
                --enable-client \
                --enable-drmaa \
                --enable-high-availability \
                --enable-syslog \
                --enable-gui \
                --disable-static \
                --with-default-server=MYSERVERNAME \
		--enable-autorun \
                --enable-cpuset \
                --without-debug
#                --enable-nvidia-gpus
#                --enable-numa-support


%make_build all \
                XPBS_DIR=%{_tcllibdir}/xpbs \
                XPBSMON_DIR=%{_tcllibdir}/xpbsmon






%install
%makeinstall_std \
                PBS_SERVER_HOME=%{torquedir} \
                mandir=%_mandir \
                XPBS_DIR=%{_tcllibdir}/xpbs \
                XPBSMON_DIR=%{_tcllibdir}/xpbsmon


find %{buildroot}%{_libdir} -name *.la -delete

#yields various service to fail if relative symlinks
export DONT_RELINK=1

#install starting scripts
mkdir -p %{buildroot}%{_unitdir}
install -p -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/pbs_mom.service
install -p -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/pbs_sched.service
install -p -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/pbs_server.service
install -p -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/trqauthd.service

rm -f %{buildroot}%{_sysconfdir}/init.d/pbs_mom
rm -f %{buildroot}%{_sysconfdir}/init.d/pbs_server
rm -f %{buildroot}%{_sysconfdir}/init.d/trqauthd

#end starting scripts

#install configuration scripts
install -p -m 755 %{SOURCE7} %{buildroot}%{_sbindir}/torque_addport
install -p -m 755 %{SOURCE8} %{buildroot}%{_sbindir}/torque_createdb
#end configuration scripts



#install config files: move them to /etc/torque
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
pushd %{buildroot}%{torquedir}
mv server_name     %{buildroot}%{_sysconfdir}/%{name}
ln -s               %{_sysconfdir}/%{name}/server_name .
popd

pushd %{buildroot}%{torquedir}/server_priv
mv nodes %{buildroot}%{_sysconfdir}/%{name}
ln -s     %{_sysconfdir}/%{name}/nodes .
popd

pushd %{buildroot}%{torquedir}/sched_priv
mv sched_config   %{buildroot}%{_sysconfdir}/%{name}
mv dedicated_time %{buildroot}%{_sysconfdir}/%{name}
mv holidays       %{buildroot}%{_sysconfdir}/%{name}
mv resource_group %{buildroot}%{_sysconfdir}/%{name}
ln -s               %{_sysconfdir}/%{name}/sched_config .
ln -s               %{_sysconfdir}/%{name}/dedicated_time .
ln -s               %{_sysconfdir}/%{name}/holidays .
ln -s               %{_sysconfdir}/%{name}/resource_group .
popd

install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}
pushd %{buildroot}%{torquedir}/mom_priv
ln -s %{_sysconfdir}/%{name}/mom_config config


popd
#end config files


#move drmaa man to the right place and install docs
##__mv #{buildroot}#{_defaultdocdir}/torque-drmaa/man/man3/* #{buildroot}#{_mandir}/man3/.
install -D -m 644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/README.mga
install -D -m 644 %{SOURCE9} %{buildroot}%{_docdir}/%{name}/openmp.pbs

#make symbolic links for tcl
pushd %{buildroot}%{_libdir}
ln -s %{_tcllibdir}/xpbs    .
ln -s %{_tcllibdir}/xpbsmon .
popd


#clean make install bugs the dirty way...
rm -f %{buildroot}%{_mandir}/man1/basl2c.1*
#__rm -f #{buildroot}#{_mandir}/man3/_*src_drmaa_src_.3*


rm -rf %buildroot/usr/share/doc/torque-drmaa/src

%post
%{_sbindir}/torque_addport
sed -i 's|MYSERVERNAME|'"$HOSTNAME"'|g' %{_sysconfdir}/%{name}/server_name


%post -n %{momname}
%_post_service pbs_mom
sed -i 's|MYSERVERNAME|'"$HOSTNAME"'|g' %{_sysconfdir}/%{name}/mom_config

%preun -n %{momname}
%_preun_service pbs_mom

%post -n %{servername}
%{_sbindir}/torque_createdb %{torquedir} %{_sbindir}/pbs_server
sed -i 's|MYSERVERNAME|'"$HOSTNAME"'|g' %{torquedir}/server_priv/serverdb
%_post_service pbs_server

%preun -n %{servername}
%_preun_service pbs_server

%post -n %{schedname}
%_post_service pbs_sched

%preun -n %{schedname}
%_preun_service pbs_sched

%post -n %{clientname}
%_post_service trqauthd

%preun -n %{clientname}
%_preun_service trqauthd



%files
%doc PBS_License.txt Release_Notes README.torque
%doc README.NUMA README.trqauthd README.array_changes
%{_docdir}/%{name}/README.mga
%{_docdir}/%{name}/openmp.pbs
%dir %{torquedir}
%dir %{torquedir}/checkpoint
%dir %{torquedir}/aux
%dir %{torquedir}/spool
%dir %{torquedir}/undelivered
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/server_name
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/torque.conf
%config(noreplace) %{_sysconfdir}/profile.d/torque.*
%{_sbindir}/torque_addport
%{torquedir}/server_name
%{torquedir}/pbs_environment
%{_libdir}/security/pam*
%{_mandir}/man1/pbs.1*



%files -n %{libname}
%doc CHANGELOG README.coding_notes README.building_40 README.configure
%{_libdir}/*.so.*



%files -n %{devname}
%doc %_docdir/%name
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_bindir}/pbs-config
%{_libdir}/*.so
%{_defaultdocdir}/torque-drmaa
%{_mandir}/man3/pbs_*.3*
#_mandir/man3/rpp.3*
%{_mandir}/man3/tm.3*
#_mandir/man3/drmaa.3*
#_mandir/man3/drmaa_*.3*



%files -n %{clientname}
%doc %_docdir/%name
%{_unitdir}/trqauthd.service
%{_sbindir}/trqauthd
%{_bindir}/qa*
%{_bindir}/qc*
%{_bindir}/qdel
%{_bindir}/qg*
%{_bindir}/qh*
%{_bindir}/qm*
%{_bindir}/qo*
%{_bindir}/qrerun
%{_bindir}/qrls
%{_bindir}/qsub
%{_bindir}/qstat
%{_bindir}/qsig
%{_bindir}/qselect
%{_bindir}/chk_tree
%{_bindir}/hostn
%{_bindir}/nqs2pbs
%{_bindir}/pbsnodes
%{_bindir}/qnodes
%{_bindir}/pbsdsh
%{_bindir}/qterm
%{_bindir}/qstop
%{_bindir}/qstart
%{_bindir}/qdisable
%{_bindir}/qenable
%{_bindir}/qrun
%{_mandir}/man1/q*.1*
%{_mandir}/man1/nqs2pbs.1*
%{_mandir}/man1/pbsdsh.1*
#_mandir/man3/jobs.3*
%{_mandir}/man7/pbs_*.7*
%{_mandir}/man8/pbsnodes.8*
%{_mandir}/man8/q*.8*



%files -n %{servername}
%dir %{torquedir}/server_priv
%dir %{torquedir}/server_priv/acl_svr
%dir %{torquedir}/server_priv/acl_groups
%dir %{torquedir}/server_priv/acl_hosts
%dir %{torquedir}/server_priv/acl_users
%dir %{torquedir}/server_priv/accounting
%dir %{torquedir}/server_priv/arrays
%dir %{torquedir}/server_priv/credentials
%dir %{torquedir}/server_priv/disallowed_types
%dir %{torquedir}/server_priv/hostlist
%dir %{torquedir}/server_priv/jobs
%dir %{torquedir}/server_priv/queues
%config(noreplace) %{_sysconfdir}/%{name}/nodes
%{torquedir}/server_priv/nodes
%{_unitdir}/pbs_server.service
%{_sbindir}/torque_createdb
%{_sbindir}/pbs_server
%{_sbindir}/qserverd
%{_bindir}/pbs_track
%{_bindir}/tracejob
%{_bindir}/printjob
%{_bindir}/printserverdb
%{_bindir}/printtracking
%{_mandir}/man8/pbs_server.8*




%files -n %{schedname}
%dir %{torquedir}/sched_priv
%dir %{torquedir}/sched_priv/accounting
%dir %{torquedir}/sched_logs
%config(noreplace) %{_sysconfdir}/%{name}/sched_config 
%config(noreplace) %{_sysconfdir}/%{name}/dedicated_time 
%config(noreplace) %{_sysconfdir}/%{name}/holidays 
%config(noreplace) %{_sysconfdir}/%{name}/resource_group
%{torquedir}/sched_priv/sched_config
%{torquedir}/sched_priv/dedicated_time
%{torquedir}/sched_priv/holidays
%{torquedir}/sched_priv/resource_group
%{_unitdir}/pbs_sched.service
%{_sbindir}/pbs_sched
%{_sbindir}/qschedd
%{_mandir}/man8/pbs_sched*.8*




%files -n %{momname}
%doc %_docdir/%name
%dir %{torquedir}/mom_priv
%dir %{torquedir}/mom_priv/jobs
%dir %{torquedir}/mom_logs
%config(noreplace) %{_sysconfdir}/%{name}/mom_config
%{torquedir}/mom_priv/config
%{_unitdir}/pbs_mom.service
%{_sbindir}/pbs_mom
%{_sbindir}/qnoded
%{_sbindir}/momctl
%{_sbindir}/pbs_demux
%{_mandir}/man8/pbs_mom.8*




%files -n %{guiname}
%{_bindir}/xpbs*
%{_bindir}/pbs_wish
%{_bindir}/pbs_tclsh
%{_tcllibdir}/xpbs
%{_tcllibdir}/xpbsmon
%{_libdir}/xpbs
%{_libdir}/xpbsmon
%{_mandir}/man1/xpbs*.1*



%changelog
* Sun Jul 21 2019 Igor Vlasenko <viy@altlinux.ru> 6.1.2-alt2_3
- fixed build

* Thu Feb 14 2019 Igor Vlasenko <viy@altlinux.ru> 6.1.2-alt1_3
- new version

* Sat Mar 09 2013 Denis Pynkin <dans@altlinux.org> 4.2.1-alt1
- New version

* Thu Sep 27 2012 Denis Pynkin <dans@altlinux.org> 4.1.2-alt1
- New version

* Sat Apr 30 2011 Denis Pynkin <dans@altlinux.ru> 3.0.1-alt1
- New version
- Added lsb header to init scripts

* Sun Dec 05 2010 Denis Pynkin <dans@altlinux.ru> 2.5.3-alt1
- New version from upstream

* Mon Oct 11 2010 Denis Pynkin <dans@altlinux.ru> 2.5.2-alt1
- New version from upstream

* Fri Feb 19 2010 Denis Pynkin <dans@altlinux.ru> 2.4.5-alt1
- New version from upstream

* Tue Dec 15 2009 Denis Pynkin <dans@altlinux.ru> 2.4.3-alt2
- Changed group name length to 32. request by rider@

* Sat Dec 12 2009 Denis Pynkin <dans@altlinux.ru> 2.4.3-alt1
- New version from upstream

* Mon Aug 24 2009 Denis Pynkin <dans@altlinux.ru> 2.3.7-alt1
- New version from upstream

* Tue Apr 07 2009 Denis Pynkin <dans@altlinux.ru> 2.3.6-alt2
- git repository restructurization

* Sun Feb 08 2009 Denis Pynkin <dans@altlinux.ru> 2.3.6-alt1
- New version from upstream
- removed obsoleted macroses
- added conflict with qstat package

* Mon Oct 20 2008 Denis Pynkin <dans@altlinux.ru> 2.3.3-alt1
- New version from upstream
- pbs_track - experimental version introduced

* Sat Apr 12 2008 Denis Pynkin <dans@altlinux.ru> 2.3.0-alt1
- New version from upstream

* Wed Sep 12 2007 Stanislav Ievlev <inger@altlinux.org> 2.1.9-alt1
- 2.1.9
- fix permisions to shared spool directory, undelivered directory and *_logs directories

* Thu Aug 09 2007 Stanislav Ievlev <inger@altlinux.org> 2.1.8-alt1.1
- add notes about redistribution to License

* Wed Aug 08 2007 Stanislav Ievlev <inger@altlinux.org> 2.1.8-alt1
- Initial release
