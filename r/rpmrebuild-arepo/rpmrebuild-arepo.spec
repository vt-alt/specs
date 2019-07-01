Name: rpmrebuild-arepo
Version: 3.1.10
Release: alt1

Summary: biarch repackager for Sisyphus packages
License: GPL
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: rpmrebuild
Requires: rpm >= 4.0.4-alt100.48

%description
Arepo repackages i586 files (mostly libraries) in i586-* packages suitable
for installation on an x86_64 system. Installing these packages allows you
to emulate a biarch environment.

%package scripts
Group: Development/Other
Summary: Helper scripts for %name biarch repackager

%description scripts
Helper scripts for %name biarch repackager

%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -m755 arepo_pre.py %buildroot%_bindir/
mkdir -p %buildroot%_sysconfdir
install -m644 rpmrebuild-arepo.conf %buildroot%_sysconfdir
mkdir -p %buildroot%_libexecdir/rpmrebuild/plugins/
install -m644 arepo.plug %buildroot%_libexecdir/rpmrebuild/plugins/
install -m755 arepo.sh %buildroot%_libexecdir/rpmrebuild/plugins/

%files
%config(noreplace) %_sysconfdir/rpmrebuild-arepo.conf
%_libexecdir/rpmrebuild/plugins/arepo.*

%files scripts
%_bindir/arepo_pre.py

%changelog
* Sun Apr 28 2019 Ivan Zakharyaschev <imz@altlinux.org> 3.1.10-alt1
- Use rpmquery-strictdep for the dependency on the native package,
  which gives an additional guarantee that the dependency is actually
  provided by the package. To get a strictdep with a beginning dot
  (a deprecated format not used in any ALT repo branches anymore except p8),
  RPM macro %%_allow_deps_with_beginning_dot
  or env var $allow_deps_with_beginning_dot has to expand to 1.

* Wed Apr 17 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.9-alt1
- rpmrebuild-arepo.conf (lib_files): added /usr/lib/valgrind .

* Sat Jan 12 2019 Dmitry V. Levin <ldv@altlinux.org> 3.1.8-alt1
- arepo.sh: generate strict requirements in [E:]V-R[:D] format,
  this complements the change made in rpm-build-4.0.4-alt122.

* Fri Oct 26 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.1.7-alt1
- arepo.sh: handle dependencies like ".strictprefix-name-version-release" (ALT#35538).

* Tue Oct 23 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.1.6-alt1
- arepo.sh: generate more strict requires for arepo package if possible (ALT#35538);
- arepo.sh: generate arepo requires against AREPO_NATIVE (thnx ldv@).

* Fri Mar 21 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.5-alt1
- rpmrebuild-arepo.conf: added /usr/lib/gdk-pixbuf-[[:digit:].]+/ to
  lib_files.
- arepo.sh: added *.so(*)* to provides_filter whitelist
  (e.g. "libnss3.so(NSS_3.14.3)").

* Thu Nov 08 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.4-alt1
- rpmrebuild-arepo.conf: added /usr/lib/pango/ to lib_files.
- arepo.sh: changed scripts filtering in 'lib' mode to copy scripts
  when they differ between native and compat packages.

* Wed Jun 13 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.3-alt1
- arepo_pre.py, arepo.sh: filter out %%ghost files in 'lib' mode

* Tue Apr 24 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.2-alt1
- rpmrebuild-arepo.conf: added /etc/X11/lib to lib_files.
- arepo_pre.py: changed output format to match
  $repo/files/list/arepo-x86_64-i586.list better.

* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt1
- rpmrebuild-arepo.conf: fixed lib_files.

* Mon Apr 02 2012 Dmitry V. Levin <ldv@altlinux.org> 3.1-alt1
- rpmrebuild-arepo.conf: stuffed up lib_files.

* Sun Apr 01 2012 Dmitry V. Levin <ldv@altlinux.org> 3.0-alt1
- Changed arepo.sh interface.
- Fixed default blacklist_pkg_name regexp.
- Optimized regexps.

* Fri Mar 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1
- initial
