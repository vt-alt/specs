%define _unpackaged_files_terminate_build 1

Name: libselinux
Epoch: 1
Version: 3.1
Release: alt1
Summary: SELinux library
License: Public Domain
Group: System/Libraries
Url: https://github.com/SELinuxProject/selinux/wiki

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libpcre-devel
BuildRequires: python3-devel
BuildRequires: swig >= 3.0.12-alt4
BuildRequires: libsepol-devel >= %version
BuildRequires: libsepol-devel-static >= %version

%description
libselinux provides an API for SELinux applications to get and set
process and file security contexts and to obtain security policy
decisions.

%package devel
Summary: SELinux development library and header files
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development library and header files needed
for developing SELinux applications.

%package devel-static
Summary: Static SELinux library
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
This package contains static SELinux library needed for developing
statically linked SELinux applications.

%package utils
Summary: SELinux utilities
Group: System/Configuration/Other
Requires: %name = %EVR

%description utils
This package provides utility programs to get and set process and
file security contexts and to obtain security policy decisions.

%package -n python3-module-selinux
Summary: Python 3.x module for %name
Group: System/Configuration/Other
Requires: %name = %EVR

%description -n python3-module-selinux
This package contains SELinux python 3.x bindings.

%prep
%setup
%patch0 -p1

%build
%make_build CFLAGS="%optflags $(pkg-config libpcre --cflags)" LIBDIR=%_libdir all
%make_build CFLAGS="%optflags" LIBDIR=%_libdir PYTHON=%_bindir/python3 pywrap

%install
%makeinstall_std LIBDIR=%_libdir SHLIBDIR=/%_lib LIBSEPOLA=%_libdir/libsepol.a PYTHON=/usr/bin/python3 install-pywrap
install -d -m 0755 %buildroot%_runtimedir/setrans

mv %buildroot%_sbindir/getdefaultcon %buildroot%_sbindir/selinuxdefcon
mv %buildroot%_sbindir/getconlist %buildroot%_sbindir/selinuxconlist

%find_lang --with-man --all-name %name

egrep -v 'booleans\.8|selinux\.8' %name.lang > %name-utils.lang
egrep    'booleans\.8|selinux\.8' %name.lang > %name-files.lang

%check
# Some vital PAM modules are linked with libselinux and therefore
# we cannot allow libselinux to be linked with libpthread.
if ldd -r %buildroot%_libdir/libselinux.so 2>&1 |grep -Fq libpthread; then
	echo >&2 'ERROR: libselinux pulls in libpthread.'
	exit 1
fi

%files -f %name-files.lang
/%_lib/*.so.*
%_man8dir/booleans.*
%_man8dir/selinux.*
%dir %_runtimedir/setrans

%files devel
%_libdir/*.so
%_includedir/selinux
%_pkgconfigdir/*
%_man3dir/*

%files devel-static
%_libdir/*.a

%files utils -f %name-utils.lang
%_sbindir/*
%_man5dir/*
%_man8dir/*
%exclude %_man8dir/booleans.*
%exclude %_man8dir/selinux.*

%files -n python3-module-selinux
%python3_sitelibdir/*

%changelog
* Fri Jul 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.1-alt1
- Updated to upstream version 3.1.

* Mon Mar 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0-alt1
- Updated to upstream version 3.0.

* Mon Mar 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9-alt2
- Fixed build with python-3.8.

* Mon Mar 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.9-alt1
- Updated to upstream version 2.9.
- Disabled support for python-2.

* Mon Dec 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt2
- Added man pages translation by Olesya Gerasimenko.

* Thu Aug 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.8-alt1
- Updated to upstream version 2.8.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.7-alt1
- Updated to upstream version 2.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.5-alt4.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Sep 26 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.5-alt4
- Rebuild with fixed trouble in swig for import python modules

* Fri Sep 08 2017 Mikhail Efremov <sem@altlinux.org> 1:2.5-alt3
- Build Python 3.x module.

* Tue Nov 22 2016 Anton Farygin <rider@altlinux.ru> 1:2.5-alt2
- upstream fixes for /proc mounting (closes: #32778)

* Thu Oct 27 2016 Anton Farygin <rider@altlinux.ru> 1:2.5-alt1
- new version

* Thu Sep 29 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:2.3-alt1
- downgraded due regression (closes: #32254)

* Wed Feb 10 2016 Sergey V Turchin <zerg@altlinux.org> 2.4-alt1
- new version

* Thu Feb 05 2015 Anton Farygin <rider@altlinux.ru> 2.3-alt1
- new version

* Wed Apr 09 2014 Andriy Stepanov <stanv@altlinux.ru> 2.2.2-alt2
- rpm_execcon helper for rpm acts as it doesn't exist at all

* Tue Jan 21 2014 Andriy Stepanov <stanv@altlinux.ru> 2.2.2-alt1
- new version

* Tue Nov 19 2013 Anton Farygin <rider@altlinux.ru> 2.2.1-alt1
- new version

* Mon Jul 15 2013 Dmitry V. Levin <ldv@altlinux.org> 2.1.13-alt3
- Reverted commit libselinux-2.1.12-57-g1d40332 because some vital
  PAM modules are linked with libselinux and therefore we cannot
  allow libselinux to be linked with libpthread.
- %%post: removed manual telinit invocation, this is no longer
  needed because rpm >= 4.0.4-alt100.55 does it automatically.

* Mon Jul 08 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.13-alt2
- Add patch from Fedora: upstream bug.

* Thu Jun 27 2013 Andriy Stepanov <stanv@altlinux.ru> 2.1.13-alt1
- New version

* Sun Sep 23 2012 Led <led@altlinux.ru> 2.1.12-alt1
- 2.1.12
- cleaned up spec

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.98-alt2.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Mikhail Efremov <sem@altlinux.org> 2.0.98-alt2
- Fix License.
- Rebuilt for debuginfo.

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.98-alt1
- Updated to 2.0.98.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt6
- .pc file: use Libs.private instead of Requires.private.

* Mon Sep 13 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt5
- Add /var/run/setrans directory.

* Tue Aug 31 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt4
- Cleanup is_selinux_enabled() (by Dmitry V. Levin).
- Fix %%post to avoid circular dependence on SysVinit (by Dmitry V. Levin).

* Mon Aug 30 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt3
- utils: fix is_selinux_enabled() return value handling.
- Run 'telinit u' in %%post (closes #23987).

* Thu Aug 26 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt2
- Fix errors messages.

* Wed Aug 25 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt1
- Updated to 2.0.96.
- Made 10 symbols hidden (by Dmitry V. Levin).
- Relocated load_setlocaldefs definition (by Dmitry V. Levin).
- Fixed specfile to use %%optflags for build.

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 2.0.94-alt2
- Ugly hackaround for 'load policy' bug.
- fix selinuxenabled.

* Wed Jun 09 2010 Mikhail Efremov <sem@altlinux.org> 2.0.94-alt1
- new version

* Wed Mar 10 2010 Mikhail Efremov <sem@altlinux.org> 2.0.90-alt2
- devel package: fix description and group.
- package the static libraries.

* Wed Feb 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.90-alt1
- new version

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.80-alt1.1
- Rebuilt with python 2.6

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 2.0.80-alt1
- new version

* Tue Jan 13 2009 Anton Farygin <rider@altlinux.ru> 2.0.77-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.76-alt1
- new version

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 2.0.65-alt1
- new (development) version
- specfile cleanup
- use static libsepol for build (mainstream)
- move man3 and man5 to devel package

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.34.15-alt1
- Initial build
