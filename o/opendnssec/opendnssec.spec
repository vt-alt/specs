%define _unpackaged_files_terminate_build 1
%define _localstatedir %_var
%def_with check

%define _pseudouser_user     _opendnssec
%define _pseudouser_group    _opendnssec
%define _pseudouser_home     %_sysconfdir/opendnssec

Name: opendnssec
Version: 1.4.14
Release: alt5

Summary: DNSSEC key and zone management software
License: BSD-2-Clause
Group: System/Servers

URL: http://www.opendnssec.org/
Source: %name-%version.tar
Source1: ods-enforcerd.service
Source2: ods-signerd.service
Source3: ods.sysconfig
Source4: conf.xml
Source5: tmpfiles-opendnssec.conf
Source6: ods-enforcerd.init
Source7: ods-signerd.init
Patch0: %name-%version-alt.patch

BuildRequires: xml-utils xsltproc
BuildRequires: libxml2-devel libsqlite3-devel libldns-devel
BuildRequires: doxygen sqlite3

Requires: softhsm
Requires: sqlite3

%if_with check
BuildRequires: CUnit-devel
BuildRequires: softhsm
%endif


%description
OpenDNSSEC was created as an open-source turn-key solution for DNSSEC.
It secures zone data just before it is published in an authoritative
name server. It requires a PKCS#11 crypto module library, such as
SoftHSM.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure \
        --localstatedir=/var \
        --sharedstatedir=%_sharedstatedir \
        --with-ldns=%_libdir \
%if_with check
        --with-dbname=sqlite3 \
%endif
        #

%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sharedstatedir/opendnssec/{tmp,signed,unsigned,signconf}
touch %buildroot%_sharedstatedir/opendnssec/{kasp.db,kasp.db.our_lock}
touch %buildroot%_sharedstatedir/opendnssec/kasp.db.backup
mkdir -p %buildroot%_runtimedir/opendnssec
mkdir -p %buildroot%_sharedstatedir/softhsm/tokens
install -Dm0644 %SOURCE1 %buildroot%_unitdir/ods-enforcerd.service
install -Dm0644 %SOURCE2 %buildroot%_unitdir/ods-signerd.service
install -Dm0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/ods
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/opendnssec/conf.xml
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/opendnssec.conf
install -Dm0755 %SOURCE6 %buildroot%_initdir/ods-enforcerd
install -Dm0755 %SOURCE7 %buildroot%_initdir/ods-signerd

%check
%make check

%pre
groupadd -r -f %_pseudouser_group ||:
groupadd -r -f ods ||:
useradd -g %_pseudouser_group -G ods -c 'OpenDNSSEC daemon account' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%post
if [ "$1" -eq 1 ]; then
	# Initialise a slot on the softhsm on first install
	su -s /bin/sh -c 'softhsm2-util --init-token --slot 0 \
		--label "OpenDNSSEC" --pin 1234 --so-pin 1234' %_pseudouser_user
	if [ ! -s %_sharedstatedir/opendnssec/kasp.db ]; then
		echo y | ods-ksmutil setup
	fi
fi

# in case we update any xml conf file
ods-ksmutil update all >/dev/null 1>&2 ||:
%post_service ods-enforcerd
%post_service ods-signerd

%preun
%preun_service ods-signerd
%preun_service ods-enforcerd

%files
%dir %attr(0770,root,%_pseudouser_group) %_sysconfdir/opendnssec
%config(noreplace) %attr(0660,root,%_pseudouser_group) %_sysconfdir/opendnssec/*.xml
%config(noreplace) %attr(0644,root,root) %_sysconfdir/sysconfig/ods
%exclude %_sysconfdir/opendnssec/*.sample
%config %_tmpfilesdir/opendnssec.conf
%config %_unitdir/ods-enforcerd.service
%config %_unitdir/ods-signerd.service
%_initdir/ods-enforcerd
%_initdir/ods-signerd
%_bindir/ods-getconf
%_bindir/ods-hsmspeed
%_bindir/ods-hsmutil
%_bindir/ods-kasp2html
%_bindir/ods-kaspcheck
%_bindir/ods-ksmutil
%_sbindir/ods-control
%_sbindir/ods-enforcerd
%_sbindir/ods-signer
%_sbindir/ods-signerd
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/signconf
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/signed
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/unsigned
%dir %attr(0770,root,%_pseudouser_group) %_sharedstatedir/opendnssec/tmp
%ghost %config(noreplace)%_sharedstatedir/opendnssec/kasp.db
%ghost %config(noreplace)%_sharedstatedir/opendnssec/kasp.db.backup
%ghost %_sharedstatedir/opendnssec/kasp.db.our_lock
%ghost %dir %attr(0755,%_pseudouser_user,%_pseudouser_group) %_runtimedir/opendnssec
%_datadir/opendnssec/
%_man1dir/*
%_man5dir/*
%_man7dir/*
%_man8dir/*

%changelog
* Sun Nov 24 2019 Stanislav Levin <slev@altlinux.org> 1.4.14-alt5
- Fixed build.

* Mon Sep 09 2019 Stanislav Levin <slev@altlinux.org> 1.4.14-alt4
- Fixed integration with FreeIPA.

* Thu Oct 18 2018 Stanislav Levin <slev@altlinux.org> 1.4.14-alt3
- Fixed filesystem intersections.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.14-alt2.qa1
- NMU: applied repocop patch

* Wed Sep 05 2018 Stanislav Levin <slev@altlinux.org> 1.4.14-alt2
- Enable tests.
- Fix requirements to sqlite3 in post script.

* Tue Sep 04 2018 Stanislav Levin <slev@altlinux.org> 1.4.14-alt1
- 1.4.12 -> 1.4.14.

* Tue Dec 13 2016 Mikhail Efremov <sem@altlinux.org> 1.4.12-alt2
- Fix dirs owner.
- Fix pidfile location.

* Wed Nov 02 2016 Mikhail Efremov <sem@altlinux.org> 1.4.12-alt1
- Initial build.

