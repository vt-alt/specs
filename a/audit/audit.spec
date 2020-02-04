%define _unpackaged_files_terminate_build 1
%def_disable static
%def_without bootstrap
%def_with ldap
%def_without prelude

Name: audit
Version: 2.8.5
Release: alt4.git.e4021a9
Summary: User space tools for Linux kernel 2.6+ auditing
License: GPL
Group: Monitoring
URL: http://people.redhat.com/sgrubb/audit/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Requires: lib%{name}1 = %EVR
Requires: service >= 0.5.26-alt1

%if_without bootstrap
# Automatically added by buildreq on Wed Mar 04 2009
BuildRequires(pre): rpm-build-python3
BuildRequires: libkrb5-devel perl-XML-Parser python-devel swig intltool
BuildRequires: python3-devel
%endif

%{?_enable_static:BuildRequires: glibc-devel-static}
%{?_with_prelude:BuildRequires: libprelude-devel}
%{?_with_ldap:BuildRequires: libldap-devel}

%description
The audit package contains the user space utilities for
storing and searching the audit records generate by
the audit subsystem in the Linux 2.6+ kernel.

%package -n lib%{name}1
Summary: Dynamic library for audit framework
License: LGPL
Group: System/Libraries
Provides: lib%name = %EVR
Obsoletes: libaudit = 2.0.4-alt1

%description -n lib%{name}1
This package contains the dynamic libraries needed for
applications to use the audit framework.

%package -n libauparse0
Summary: Dynamic library for audit framework
License: LGPL
Group: System/Libraries
Conflicts: lib%name = 2.0.4-alt1
Conflicts: lib%name < 1.7.16-alt2

%description -n libauparse0
This package contains the dynamic libraries needed for
applications to use the audit framework.

%package -n lib%name-devel
Summary: Header files and static library for libaudit
License: LGPL
Group: Development/C
Requires: lib%{name}1 = %EVR
Requires: libauparse0 = %EVR

%description -n lib%name-devel
This package contains the static libraries and header
files needed for developing applications that need to use the audit
framework libraries.

%package -n python-module-%name
Summary: Python bindings for libaudit
License: LGPL
Group: Development/Python
Requires: lib%{name}1 = %EVR

%description -n python-module-%name
The python-module-%name package contains the bindings so that libaudit
and libauparse can be used by python.

%package -n python3-module-%name
Summary: Python3 bindings for libaudit
License: LGPL
Group: Development/Python3
Requires: lib%{name}1 = %EVR

%description -n python3-module-%name
The python3-module-%name package contains the bindings so that libaudit
and libauparse can be used by python.

%prep
%setup
%patch0 -p1
sed -i 's@/etc/init.d/auditd restart@/etc/init.d/auditd stop\nservice auditd start@' \
	init.d/auditd.restart
sed -i 's@RETVAL=1@&\nstart-stop-daemon -p "/var/run/auditd.pid" -u root -K -n auditd -t >/dev/null \&\& \\@' \
	init.d/auditd.condrestart

%build
%autoreconf

%configure \
	--sbindir=/sbin \
	--libdir=%_libdir \
%if_with bootstrap
	--without-python \
	--without-python3 \
%endif
	%{?!_with_ldap:--disable-zos-remote} \
	%{subst_enable static} \
	%{subst_with prelude}

%make_build

%install
%makeinstall_std

install -d %buildroot%_logdir/%name
install -d %buildroot%_sysconfdir/audispd/plugins.d
install -d %buildroot/%_libdir/%name

#move shared library to %_lib
install -d %buildroot/%_lib
mv %buildroot/%_libdir/*.so.* %buildroot/%_lib/
for i in libaudit libauparse;do
LIBNAME=$(readlink %buildroot/%_libdir/$i.so)
ln -sf  ../../%_lib/${LIBNAME##*/}  %buildroot/%_libdir/$i.so
done



#replace init script
install -Dpm755 %name.init %buildroot/%_initdir/%{name}d

#install rotate script
install -Dpm755 %name.cron %buildroot/%_sysconfdir/cron.weekly/%{name}d

install -pD -m644 init.d/%{name}d.service %buildroot%_unitdir/%{name}d.service
install -pD -m755 init.d/%{name}d.condrestart %buildroot/usr/libexec/service/legacy-actions/%{name}d/condrestart
install -pD -m755 init.d/%{name}d.rotate %buildroot/usr/libexec/service/legacy-actions/%{name}d/rotate
install -pD -m755 init.d/%{name}d.stop %buildroot/usr/libexec/service/legacy-actions/%{name}d/stop
install -pD -m755 init.d/%{name}d.restart %buildroot/usr/libexec/service/legacy-actions/%{name}d/restart
install -pD -m644 rules/10-base-config.rules %buildroot%_sysconfdir/%name/rules.d/10-base-config.rules

%post
%post_service %{name}d
if [ $1 -gt 1 ]; then
       service %{name}d condrestart ||:
fi

%preun
%preun_service %{name}d
if [ $1 -eq 0 ]; then
	service %{name}d stop ||:
fi

%files
%doc README ChangeLog contrib rules
%config(noreplace) %_sysconfdir/cron.weekly/%{name}d
%_initdir/%{name}d
%attr(700,root,root) %_logdir/%name
%config %_unitdir/%{name}d.service

/sbin/ausearch
/sbin/aureport
%_bindir/auvirt
%attr(750,root,root) /sbin/auditctl
%attr(750,root,root) /sbin/augenrules
%attr(750,root,root) /sbin/auditd
%attr(750,root,root) /sbin/autrace
%attr(750,root,root) /sbin/audispd
%attr(750,root,root) /sbin/audisp-remote
%if_with prelude
%attr(750,root,root) /sbin/audisp-prelude
%endif
%if_with ldap
%attr(750,root,root) /sbin/audispd-zos-remote
%endif
%attr(750,root,root) %_bindir/aulastlog
%attr(750,root,root) %_bindir/aulast
%attr(750,root,root) %_bindir/ausyscall


%_man5dir/*
%_man8dir/*
%_man7dir/*

%exclude %_sysconfdir/sysconfig/%{name}d
%attr(700,root,root) %dir %_sysconfdir/%name
%config(noreplace) %attr(600,root,root) %_sysconfdir/%name/auditd.conf
%config(noreplace) %attr(600,root,root) %_sysconfdir/%name/audit-stop.rules
%attr(700,root,root) %dir %_sysconfdir/%name/rules.d
%config(noreplace) %attr(600,root,root) %_sysconfdir/%name/rules.d/*.rules

%attr(700,root,root) %dir %_sysconfdir/audispd
%attr(700,root,root) %dir %_sysconfdir/audisp
%attr(700,root,root) %dir %_sysconfdir/audisp/plugins.d
%config(noreplace) %attr(640,root,root) /etc/audisp/*.conf

%attr(700,root,root) %dir %_sysconfdir/audispd/plugins.d
%config(noreplace) %attr(640,root,root) /etc/audisp/plugins.d/*.conf

%attr(700,root,root) %dir %_libdir/audit
/usr/libexec/service/legacy-actions/%{name}d


%files -n lib%{name}1
/%_lib/libaudit.so.*
%config(noreplace) %attr(600,root,root) /etc/libaudit.conf

%files -n libauparse0
/%_lib/libauparse.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_man3dir/*
%_aclocaldir/%name.m4

%if_without bootstrap
%files -n python-module-%name
%python_sitelibdir/*

%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.5-alt4.git.e4021a9
- Ported fix from different branch.

* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.5-alt3.git.e4021a9
- Pulled updates from upstream, including memory leak fixes.

* Mon Mar 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.5-alt2
- Built python-3 bindings.

* Tue Mar 12 2019 Anton Farygin <rider@altlinux.ru> 2.8.5-alt1
- 2.8.5

* Thu Oct 04 2018 Stanislav Levin <slev@altlinux.org> 2.8.4-alt2
- Fixed log's server mode on IPV4 machines.

* Mon Jun 25 2018 Anton Farygin <rider@altlinux.ru> 2.8.4-alt1
- 2.8.4

* Fri Apr 20 2018 Stanislav Levin <slev@altlinux.org> 2.8.3-alt3
- Fix dependency to systemd in post script

* Wed Apr 18 2018 Stanislav Levin <slev@altlinux.org> 2.8.3-alt2
- Make it possible not to limit the restart of a crashed plugin

* Sat Mar 31 2018 Anton Farygin <rider@altlinux.ru> 2.8.3-alt1
- new version

* Fri Jan 26 2018 Anton Farygin <rider@altlinux.ru> 2.8.2-alt1
- new version
- disabled prelude support (code is outdated and needs to be revised)

* Sun Oct 15 2017 Anton Farygin <rider@altlinux.ru> 2.8.1-alt1
- new version

* Fri Sep 22 2017 Anton Farygin <rider@altlinux.ru> 2.7.8-alt1
- new version

* Thu Sep 07 2017 Michael Shigorin <mike@altlinux.org> 2.7.7-alt2
- BOOTSTRAP:
  + make krb5/ldap/prelude/python support conditional
  + make zos-remote plugin build depend on ldap support explicitly
  - minor spec cleanup

* Thu Jun 22 2017 Anton Farygin <rider@altlinux.ru> 2.7.7-alt1
- new version

* Mon Apr 24 2017 Anton Farygin <rider@altlinux.ru> 2.7.6-alt1
- new version

* Fri Apr 14 2017 Anton Farygin <rider@altlinux.ru> 2.7.5-alt1
- new version

* Fri Mar 10 2017 Anton Farygin <rider@altlinux.ru> 2.7.3-alt1
- new version

* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 2.7.2-alt1
- new version

* Wed Feb 08 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- new version

* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.7-alt1.1
- rebuild with libprelude

* Thu Sep 15 2016 Anton Farygin <rider@altlinux.ru> 2.6.7-alt1
- new version

* Tue Jul 19 2016 Anton Farygin <rider@altlinux.ru> 2.6.5-alt1
- new version

* Tue May 10 2016 Anton Farygin <rider@altlinux.ru> 2.5.2-alt1
- new version

* Thu Jan 14 2016 Anton Farygin <rider@altlinux.ru> 2.5-alt1
- new version

* Wed Oct 21 2015 Anton Farygin <rider@altlinux.ru> 2.4.4-alt1
- new version

* Tue May 26 2015 Anton Farygin <rider@altlinux.ru> 2.4.2-alt2
- rebuild for new environment

* Tue May 19 2015 Anton Farygin <rider@altlinux.ru> 2.4.2-alt1
- new version

* Thu Jan 22 2015 Anton Farygin <rider@altlinux.ru> 2.4.1-alt1
- new version
- added legacy actions scripts (closes: #28931, #27843)

* Wed Sep 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.1
- Rebuilt with new libprelude

* Mon Sep 08 2014 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- new version

* Thu Jun 05 2014 Anton Farygin <rider@altlinux.ru> 2.3.7-alt1
- new version

* Mon Apr 14 2014 Anton Farygin <rider@altlinux.ru> 2.3.6-alt1
- new version

* Fri Mar 21 2014 Anton Farygin <rider@altlinux.ru> 2.3.5-alt1
- new version

* Thu Feb 20 2014 Anton Farygin <rider@altlinux.ru> 2.3.3-alt1
- new version

* Mon Oct 07 2013 Anton Farygin <rider@altlinux.ru> 2.3.2-alt1
- new version

* Mon Jun 24 2013 Anton Farygin <rider@altlinux.ru> 2.3.1-alt1
- new version

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 2.2.3-alt1
- new version
- add systemd support

* Wed Sep 19 2012 Anton Farygin <rider@altlinux.ru> 2.2.1-alt1
- new version

* Tue Sep 13 2011 Anton Farygin <rider@altlinux.ru> 2.1.3-alt1
- new version

* Fri Feb 25 2011 Anton Farygin <rider@altlinux.ru> 2.0.6-alt1
- new version

* Tue Sep 28 2010 Anton Farygin <rider@altlinux.ru> 2.0.5-alt1
- new version

* Tue Jul 20 2010 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt2
- fix summaries and descriptions.
- package libauparse as separate subpackage libauparse0.
- rename libaudit -> libaudit1.

* Thu Jul 01 2010 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt1
- spec cleanup.
- drop depends on python-module-pygtk-libglade.
- new version

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.16-alt1.1
- Rebuilt with python 2.6

* Mon Nov 16 2009 Anton Farygin <rider@altlinux.ru> 1.7.16-alt1
- new version

* Tue Sep 01 2009 Anton Farygin <rider@altlinux.ru> 1.7.13-alt3
- rebuild with libldap2.4

* Sun Aug 09 2009 Anton Farygin <rider@altlinux.ru> 1.7.13-alt2
- python-dev requires changed to python-devel
- menu entry fixed for system-config-audit

* Mon Apr 27 2009 Anton Farygin <rider@altlinux.ru> 1.7.13-alt1
- new version
- fixed build

* Wed Apr 08 2009 Anton Farygin <rider@altlinux.ru> 1.7.12-alt6
- added python-module-pygtk-libglade to requires for python-module-audit (#19431)

* Wed Mar 11 2009 Anton Farygin <rider@altlinux.ru> 1.7.12-alt4
- service auditd off by default

* Tue Mar 10 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.12-alt3
- added support of libprelude

* Wed Mar 04 2009 Anton Farygin <rider@altlinux.ru> 1.7.12-alt2
- added system-config-audit subpackage with graphical utility for editing audit configuration

* Wed Mar 04 2009 Anton Farygin <rider@altlinux.ru> 1.7.12-alt1
- new version

* Thu Jan 15 2009 Anton Farygin <rider@altlinux.ru> 1.7.11-alt1
- new version
- subpackage python-module-audit added
- Packager changed

* Wed Dec 17 2008 Anton Farygin <rider@altlinux.ru> 1.7.10-alt1
- new version

* Fri Dec 12 2008 Anton Farygin <rider@altlinux.ru> 1.7.9-alt1
- new version

* Tue Sep 23 2008 Stanislav Ievlev <inger@altlinux.org> 1.7-alt2
- silent rotate

* Thu Apr 03 2008 Stanislav Ievlev <inger@altlinux.org> 1.7-alt1
- 1.7

* Fri Jul 06 2007 Stanislav Ievlev <inger@altlinux.org> 1.5.4-alt1
- 1.5.4

* Thu May 24 2007 Stanislav Ievlev <inger@altlinux.org> 1.5.3-alt1
- Initial release
