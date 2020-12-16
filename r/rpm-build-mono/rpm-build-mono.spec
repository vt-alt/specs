%define _unpackaged_files_terminate_build 1

Name: rpm-build-mono
Version: 2.1.0
Release: alt1

Summary: RPM helper macros and dependency utils to build Mono packages
License: GPL
Group: Development/Other

Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: rpm >= 4.0.4-alt96.13
Conflicts: rpm-build-mono4

%description
These helper macros and dependency calculation utils facilitate creation
of RPM packages containing Mono bytecode archives etc.
Based on rpm-build-mono4, but for mono-5.x.

%prep
%setup

%install
install -pD -m644 rpm-build-mono.macros %buildroot%_rpmmacrosdir/mono
install -pD -m755 mono.req %buildroot%_rpmlibdir/mono.req
ln -s mono.req %buildroot%_rpmlibdir/monolib.req
ln -s mono.req %buildroot%_rpmlibdir/mono.prov
install -pD -m755 mono.req.files %buildroot%_rpmlibdir/mono.req.files
ln -s mono.req.files %buildroot%_rpmlibdir/monolib.req.files
install -pD -m755 mono.prov.files %buildroot%_rpmlibdir/mono.prov.files

%files
%_rpmmacrosdir/mono
%_rpmlibdir/mono*

%changelog
* Thu Nov 12 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Updated stdlibs list.

* Mon Jul 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt4
- Updated build dependencies.

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3
- NMU: remove %%ubt from release

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2
- Rebuilt with support of %%ubt macro.

* Mon Jul 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Imported files from rpm-build-mono4 and updated for mono-5

* Wed Apr 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2.1-alt1
- mono.req: re-written the suffix (e.g.: ()(64bit)) computation in
  non-lib64-centric way. (For easier porting to other platforms.)
  (Borrowed from rpm-build-python3-0.1.9.1-alt1.)

* Mon Nov 24 2008 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt2
- define %%_monodocdir as /usr/share/monodoc/sources
- install mono macros to /usr/lib/rpm/macros.d

* Sun Mar 09 2008 Alexey Tourbin <at@altlinux.ru> 1.3.2-alt1
- trap errors which monodis(1) prints to stdout (#14578)

* Mon Jan 14 2008 Alexey Tourbin <at@altlinux.ru> 1.3.1-alt1
- monolib.req: added check to prevent soname dependencies in noarch packages

* Mon Dec 03 2007 Alexey Tourbin <at@altlinux.ru> 1.3-alt1
- reworked self-requires elimination algorithm, to allow dependencies
  on private libraries between subpackages; now we emit file-level
  dependencies for private libraries, e.g. /usr/lib/beagle/Beagle.dll

* Sun Nov 25 2007 Alexey Tourbin <at@altlinux.ru> 1.2-alt2
- rebuild for new dependencies on rpm

* Mon Nov 05 2007 Alexey Tourbin <at@altlinux.ru> 1.2-alt1
- monolib.req: improved soname detection
- mono.prov: provide only "public" DLLs under /usr/lib/mono/gac
- mono.req: implemented self-requires elimination, to allow private DLLs
- mono.req: use simplified 2-digit versioning for standard DLLs

* Mon Sep 24 2007 Alexey Tourbin <at@altlinux.ru> 1.1-alt1
- adapted mono.req and mono.prov scripts for new rpm-build
- monolib.req: extract soname dependencies from *.dll.config files

* Wed Nov 08 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt6
- one more small error, will it work atlast?

* Tue Oct 31 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt5
- fix a small error from previous release

* Tue Oct 31 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt4
- fix for x86_64 arch

* Tue Oct 10 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt3
- added %%_monodocdir to rpm-build-mono.macros

* Mon Oct 09 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt2
- fixed rpm-build-mono.macros

* Thu Oct 05 2006 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt1
- Initial release
