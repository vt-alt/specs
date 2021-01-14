%define _unpackaged_files_terminate_build 1

%define _libexecdir %prefix/libexec

%def_disable check

Name: libsemanage
Epoch: 1
Version: 3.1
Release: alt1
Summary: Library, which provides an interface for SELinux management
Group: System/Libraries
License: LGPLv2.1+
Url: https://github.com/SELinuxProject/selinux

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: bzlib-devel flex libustr-devel libaudit-devel
BuildRequires: libsepol-devel >= %version
BuildRequires: libselinux-devel >= %version
BuildRequires: swig python3-devel
%{!?_disable_check:BuildRequires: CUnit-devel libsepol-devel-static >= %version libselinux-devel-static >= %version }

%description
This package provides the shared libraries for the manipulation of
SELinux binary policies. It is used by checkpolicy (the policy compiler)
and similar tools, as well as by programs like load_policy that need
to perform specific transformations on binary policies such as
customizing policy boolean settings. This contains the run-time
libraries needed by such tools.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Header files and libraries for SELinux policy manipulation tools
This package provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as
well as by programs like load_policy that need to perform specific
transformations on binary policies such as customizing policy boolean
settings. It contains the static libraries and header files needed
for developing applications that manipulate SELinux binary policies.

%package devel-static
Summary: Development files for %name
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
Static libraries for SELinux policy manipulation tools.

%package utils
Summary: Utils for checking and mainplating policy binaries Security-enhanced Linux
Group: System/Configuration/Other
Provides: semanage_migrate_store = %EVR
Requires: %name = %EVR
Requires: python3-module-selinux python3-module-semanage

%description utils
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

%package -n python3-module-semanage
Summary: Python module for %name
Group: System/Configuration/Other
Requires: %name = %EVR

%description -n python3-module-semanage
Python bindings  for SELinux policy manipulation tools
This package provides python bindings for the manipulation of SELinux
binary policies.

%prep
%setup
%patch0 -p1

%build
%make_build CFLAGS="%optflags" LIBDIR=%_libdir SHLIBDIR=%_lib LIBEXECDIR=%_libexecdir all
%make_build CFLAGS="%optflags" LIBDIR=%_libdir SHLIBDIR=%_lib LIBEXECDIR=%_libexecdir pywrap PYTHON=python3

%install
%makeinstall_std LIBDIR=%_libdir SHLIBDIR=/%_lib install-pywrap PYTHON=python3
ln -sf $(relative /%_lib/libsemanage.so.1 %_libdir/libsemanage.so) %buildroot/%_libdir/libsemanage.so

# TODO: currently only man5dir is translated. If other man pages are translated, %%find_lang use should be improved
%find_lang --with-man --all-name %name

%check
%make_build test

%files -f %name.lang
%dir %_sysconfdir/selinux
%config(noreplace) %_sysconfdir/selinux/*
/%_lib/*.so.*
%_man5dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_man3dir/*

%files devel-static
%_libdir/*.a

%files utils
%_libexecdir/selinux/*

%files -n python3-module-semanage
%python3_sitelibdir/*

%changelog
* Fri Jul 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.1-alt1
- Updated to upstream version 3.1.

* Mon Mar 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0-alt1
- Updated to upstream version 3.0.

* Mon Mar 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9-alt1
- Updated to upstream version 2.9.

* Mon Dec 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt2
- Added man pages translation by Olesya Gerasimenko.

* Thu Aug 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt1
- Updated to upstream version 2.8.

* Mon Feb 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.7-alt1
- Updated to upstream version 2.7.

* Tue Nov 01 2016 Anton Farygin <rider@altlinux.ru> 1:2.5-alt1
- new version

* Thu Sep 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:2.3-alt1
- downgraded due regression (closes: #32254)
- alt-lib-install-dir.patch has been removed

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 2.4-alt1
- new version

* Thu Feb 05 2015 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- new version

* Tue Nov 19 2013 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- New version

* Wed Sep 18 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.10-alt2
- pam_mktemp workaround

* Thu Jun 27 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.10-alt1
- New version

* Sun Sep 23 2012 Led <led@altlinux.ru> 2.1.9-alt1
- 2.1.9
- cleaned up spec

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.46-alt1.1
- Rebuild with Python-2.7

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.46-alt1
- Updated to 2.0.46.
- Drop unused variable.

* Mon Nov 15 2010 Mikhail Efremov <sem@altlinux.org> 2.0.45-alt3
- Add /srv/home and /var/srv/home to home directories list.
- Use rpm-build-licenses.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.45-alt2
- .pc file: use Libs.private instead of Requires.private.
- fix build and install sections.
- use tar instead of tgz for sources.
- Drop redundant information from description.
- fix Url.
- drop Packager from spec.

* Wed Jun 09 2010 Mikhail Efremov <sem@altlinux.org> 2.0.45-alt1
- new version

* Wed Feb 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.44-alt1
- new version

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.31-alt1.1
- Rebuilt with python 2.6

* Tue Jan 13 2009 Anton Farygin <rider@altlinux.ru> 2.0.31-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.30-alt1
- new version
- fixed python-module name

* Sat Dec 20 2008 Anton Farygin <rider@altlinux.ru> 2.0.25-alt1
- new (development) version
- specfile cleanup

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.10.9-alt1
- Initial build
