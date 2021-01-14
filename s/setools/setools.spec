%define _unpackaged_files_terminate_build 1

%define libsepol_ver 3.0

Name: setools
Version: 4.3.0
Release: alt1
License: %gpl2plus
URL: https://github.com/SELinuxProject/setools/wiki
Summary: Policy analysis tools for SELinux
Group: System/Base

# https://github.com/SELinuxProject/setools.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-python3
BuildRequires: /proc
#libsetools
BuildRequires: libselinux-devel

# In libsepol defined version: POLICYDB_VERSION_MAX, so rebuild libsepol first if available.
BuildRequires: libsepol-devel >= %libsepol_ver
BuildRequires: libsepol-devel-static >= %libsepol_ver

BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(Cython)

%description
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This meta-package depends upon the main packages necessary to run
SETools.

%package -n python3-module-%name
License: %lgpl2plus
Summary: Python bindings for SELinux policy analysis
Group: Development/Python3

%description -n python3-module-%name
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

%package console
Summary: Policy analysis command-line tools for SELinux
Group: System/Base
License: %gpl2plus
Requires: libselinux

%description console
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

%package console-analyses
Summary: Policy analysis command-line tools for SELinux
Group: System/Base
License: %gpl2plus
Requires: libselinux

%description console-analyses
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

%package gui
Summary: Policy analysis graphical tools for SELinux
Group: System/Base

%description gui
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

%prep
%setup
%patch -p1

%build
CFLAGS="%{optflags}" python3 setup.py build_ext
CFLAGS="%{optflags}" %python3_build_debug

%install
%python3_install

%find_lang --with-man --all-name %name

egrep 'sediff\.1|seinfo\.1|sesearch\.1' %name.lang > %name-console.lang
egrep 'sedta\.1|seinfoflow\.1' %name.lang > %name-console-analyses.lang
egrep 'apol\.1' %name.lang > %name-gui.lang

%files -n python3-module-%name
%doc ChangeLog COPYING COPYING.GPL COPYING.LGPL KNOWN-BUGS README.md
%python3_sitelibdir/setools
%python3_sitelibdir/setools-*-py*.egg-info

%files console -f %name-console.lang
%doc ChangeLog COPYING COPYING.GPL COPYING.LGPL KNOWN-BUGS README.md
%_bindir/sediff
%_bindir/seinfo
%_bindir/sesearch
%_man1dir/sediff.1*
%_man1dir/seinfo.1*
%_man1dir/sesearch.1*

%files console-analyses -f %name-console-analyses.lang
%doc ChangeLog COPYING COPYING.GPL COPYING.LGPL KNOWN-BUGS README.md
%_bindir/sedta
%_bindir/seinfoflow
%_man1dir/sedta.1*
%_man1dir/seinfoflow.1*

%files gui -f %name-gui.lang
%doc ChangeLog COPYING COPYING.GPL COPYING.LGPL KNOWN-BUGS README.md
%_bindir/apol
%_man1dir/apol.1*
%python3_sitelibdir/setoolsgui

%changelog
* Tue Jun 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.3.0-alt1
- Updated to upstream version 4.3.0.

* Mon Mar 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.2-alt1
- Updated to upstream version 4.2.2.

* Wed Feb 27 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.1-alt1
- Updated to upstream version 4.2.1.
- New version builds with python-3 only.

* Fri Jan 11 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.1-alt4
- Updated email addresses, project name and URLs in translated files.

* Mon Dec 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.1-alt3
- Added man pages translation by Olesya Gerasimenko.

* Mon Dec 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.1-alt2
- Rebuilt with new swig and gcc (Closes: #35695)

* Tue Feb 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.1-alt1
- Updated to upstream version 4.1.1.

* Mon Feb 26 2018 Mikhail Efremov <sem@altlinux.org> 3.3.8-alt7
- Drop libJLib-devel from BR.
- Disable swig-java on e2k.
- Add knob to disable java stuff.

* Wed Mar 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.3.8-alt6.qa1
- NMU: rebuild against Tcl/Tk 8.6

* Sat Oct 29 2016 Anton Farygin <rider@altlinux.ru> 3.3.8-alt6
- rebuild with new libsepol 2.5

* Mon Feb 29 2016 Mikhail Efremov <sem@altlinux.org> 3.3.8-alt5
- Fix -Wformat-security issues (patch from Fedora).
- Fix missing parentheses in policy_define.c (patch from upstream).
- Update for 2015-02-02 Userspace release (2.4) (patch from upstream).
- Fix manpages packaging.

* Fri Nov 22 2013 Anton Farygin <rider@altlinux.ru> 3.3.8-alt4
- Rebuild with new libsepol

* Wed Jul 10 2013 Andriy Stepanov <stanv@altlinux.ru> 3.3.8-alt3
- Rebuild with new libsepol

* Wed Jun 26 2013 Andriy Stepanov <stanv@altlinux.ru> 3.3.8-alt2
- New version

* Wed Jun 26 2013 Andriy Stepanov <stanv@altlinux.ru> 3.3.8-alt1
- NewVersion

* Wed Oct 03 2012 Led <led@altlinux.ru> 3.3.7-alt4
- fixed build with recent libsepol
- added patches from openSUSE

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.7-alt3.qa1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.7-alt3.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.3.7-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for setools-gui

* Fri Oct 22 2010 Mikhail Efremov <sem@altlinux.org> 3.3.7-alt3
- rewrite seaudit.pam.

* Wed Aug 04 2010 Mikhail Efremov <sem@altlinux.org> 3.3.7-alt2
- require /proc for build.
- fixup configure.ac to expect SWIG 2.0.0.

* Fri Jun 11 2010 Mikhail Efremov <sem@altlinux.org> 3.3.7-alt1
- initial build for Sisyphus based on FC spec

* Wed May 12 2010 Chris PeBenito <cpebenito@tresys.com> 3.3.7-2
- Add missing bzip2 dependencies.

* Wed May 12 2010 Chris PeBenito <cpebenito@tresys.com> 3.3.7-1
- New upstream release.

* Tue Aug 11 2009 Dan Walsh <dwalsh@redhat.com> 3.3.6-4
- Add python bindings for sesearch and seinfo

* Tue Jul 28 2009 Dan Walsh <dwalsh@redhat.com> 3.3.6-3
- Fix qpol install of include files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Chris PeBenito <cpebenito@tresys.com> 3.3.6-1
- New upstream release.

* Sun Apr  5 2009 Dan Horák <dan[at]danny.cz> - 3.3.5-8
- don't expect that java-devel resolves as gcj

* Sun Apr  5 2009 Dan Horák <dan[at]danny.cz> - 3.3.5-7
- add support for s390x

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 04 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.3.5-5
- Rebuild for Python 2.6

* Mon Dec  1 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 3.3.5-4
- Include %%tcllibdir directory in -libs-tcl package.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.3.5-3
- Rebuild for Python 2.6

* Wed Sep 17 2008 Dennis Gilmore <dennis@ausil.us> 3.3.5-2
- fix building in sparc and s390 arches

* Tue Aug 26 2008 Chris PeBenito <cpebenito@tresys.com> 3.3.5-1
- Update to upstream version 3.3.5.

* Wed Feb 27 2008 Chris PeBenito <cpebenito@tresys.com> 3.3.4-1
- Fixes gcc 4.3, glibc 2.7, tcl 8.5, and libsepol 2.0.20 issues.
- Fix policy loading when policy on disk is higher version than the kernel.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.3.2-3
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 Chris Pebenito <cpebenito@tresys.com> 3.3.2-2.fc9
- Bump to pick up new libsepol and policy 22.

* Wed Nov 28 2007 Chris Pebenito <cpebenito@tresys.com> 3.3.2-1.fc9
- Update for 3.3.2.

* Thu Oct 18 2007 Chris PeBenito <cpebenito@tresys.com> 3.3.1-7.fc8
- Rebuild to fix ppc64 issue.

* Wed Oct 17 2007 Chris PeBenito <cpebenito@tresys.com> 3.3.1-6.fc8
- Update for 3.3.1.

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.2-4
- Rebuild for selinux ppc32 issue.

* Fri Jul 20 2007 Dan Walsh <dwalsh@redhat.com> 3.2-3
- Move to Tresys spec file

* Wed Jun 13 2007 Dan Walsh <dwalsh@redhat.com> 3.2-2
- Bump for rebuild

* Mon Apr 30 2007 Dan Walsh <dwalsh@redhat.com> 3.2-1
- Start shipping the rest of the setools command line apps

* Wed Apr 25 2007 Jason Tang <jtang@tresys.com> 3.2-0
- update to SETools 3.2 release

* Mon Feb 02 2007 Jason Tang <jtang@tresys.com> 3.1-1
- update to SETools 3.1 release

* Mon Oct 30 2006 Dan Walsh <dwalsh@redhat.com> 3.0-2.fc6
- bump for fc6
 
* Thu Oct 26 2006 Dan Walsh <dwalsh@redhat.com> 3.0-2
- Build on rawhide

* Sun Oct 15 2006 Dan Walsh <dwalsh@redhat.com> 3.0-1
- Update to upstream

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue May 23 2006 Dan Walsh <dwalsh@redhat.com> 2.4-2
- Remove sqlite include directory

* Wed May 3 2006 Dan Walsh <dwalsh@redhat.com> 2.4-1
- Update from upstream

* Mon Apr 10 2006 Dan Walsh <dwalsh@redhat.com> 2.3-3
- Fix help
- Add icons

* Tue Mar 21 2006 Dan Walsh <dwalsh@redhat.com> 2.3-2
- Remove console apps for sediff, sediffx and apol

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Dan Walsh <dwalsh@redhat.com> 2.3-1
- Update from upstream
  * apol:
        added new MLS components tab for sensitivities, 
        levels, and categories.
        Changed users tab to support ranges and default 
        levels.
        added range transition tab for searching range
        Transition rules.
        added new tab for network context components.
        added new tab for file system context components.
  * libapol:
        added binpol support for MLS, network contexts, 
        and file system contexts.
  * seinfo:
        added command line options for MLS components.
        added command line options for network contexts
        and file system contexts.
  * sesearch:
        added command line option for searching for rules
        by conditional boolean name.
  * seaudit:
        added new column in the log view for the 'comm' 
        field found in auditd log files.
        added filters for the 'comm' field and 'message'
        field.
  * manpages:
        added manpages for all tools.        



* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Wed Dec 14 2005 Dan Walsh <dwalsh@redhat.com> 2.2-4
- Fix dessktop files
- Apply fixes from bkyoung

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-3
- Move more gui files out of base into gui 

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-2
- Move sediff from gui to main package

* Thu Nov 3 2005 Dan Walsh <dwalsh@redhat.com> 2.2-1
- Upgrade to upstream version

* Thu Oct 13 2005 Dan Walsh <dwalsh@redhat.com> 2.1.3-1
- Upgrade to upstream version

* Mon Oct 10 2005 Tomas Mraz <tmraz@redhat.com> 2.1.2-3
- use include instead of pam_stack in pam config

* Thu Sep 1 2005 Dan Walsh <dwalsh@redhat.com> 2.1.2-2
- Fix spec file
 
* Thu Sep 1 2005 Dan Walsh <dwalsh@redhat.com> 2.1.2-1
- Upgrade to upstream version
 
* Thu Aug 18 2005 Florian La Roche <laroche@redhat.com>
- do not package debug files into the -devel package

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 2.1.1-3
- rebuild against new cairo

* Wed May 25 2005 Dan Walsh <dwalsh@redhat.com> 2.1.1-0
- Upgrade to upstream version

* Mon May 23 2005 Bill Nottingham <notting@redhat.com> 2.1.0-5
- put libraries in the right place (also puts debuginfo in the right
  package)
- add %%defattr for -devel too

* Thu May 12 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-4
- Move sepcut to gui apps.

* Fri May 6 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-3
- Fix Missing return code.

* Wed Apr 20 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-2
- Fix requires line

* Tue Apr 19 2005 Dan Walsh <dwalsh@redhat.com> 2.1.0-1
- Update to latest from tresys

* Tue Apr 5 2005 Dan Walsh <dwalsh@redhat.com> 2.0.0-2
- Fix buildrequires lines in spec file

* Tue Mar 2 2005 Dan Walsh <dwalsh@redhat.com> 2.0.0-1
- Update to latest from tresys

* Mon Nov 29 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-6
- add FALLBACK=true to /etc/security/console.apps/apol

* Wed Nov 10 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-3
- Add badtcl patch from Tresys.

* Mon Nov 8 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-2
- Apply malloc problem patch provided by  Sami Farin 

* Mon Nov 1 2004 Dan Walsh <dwalsh@redhat.com> 1.5.1-1
- Update to latest from Upstream

* Wed Oct 6 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-5
- Update tresys patch

* Mon Oct 4 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-4
- Fix directory ownership

* Thu Jul 8 2004 Dan Walsh <dwalsh@redhat.com> 1.4.1-1
- Latest from Tresys

* Wed Jun 23 2004 Dan Walsh <dwalsh@redhat.com> 1.4-5
- Add build requires libselinux

* Tue Jun 22 2004 Dan Walsh <dwalsh@redhat.com> 1.4-4
- Add support for policy.18

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 10 2004 Dan Walsh <dwalsh@redhat.com> 1.4-2
- Fix install locations of policy_src_dir

* Wed Jun 2 2004 Dan Walsh <dwalsh@redhat.com> 1.4-1
- Update to latest from TRESYS.

* Tue Jun 1 2004 Dan Walsh <dwalsh@redhat.com> 1.3-3
- Make changes to work with targeted/strict policy
* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-2
- Take out requirement for policy file

* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-1
- Fix doc location

* Fri Apr 16 2004 Dan Walsh <dwalsh@redhat.com> 1.3-1
- Latest from TRESYS

* Tue Apr 13 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-8
- fix location of policy.conf file

* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-7
- Obsolete setools-devel
* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-6
- Fix location of 
* Tue Apr 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-5
- Remove devel libraries
- Fix installdir for lib64

* Sat Apr 3 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-4
- Add usr_t file read to policy

* Thu Mar 25 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-3
- Use tcl8.4

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2.1-1
- New patch

* Fri Feb 6 2004 Dan Walsh <dwalsh@redhat.com> 1.2-1
- Latest upstream version

* Tue Dec 30 2003 Dan Walsh <dwalsh@redhat.com> 1.1.1-1
- New version from upstream
- Remove seuser.te.  Now in policy file.

* Tue Dec 30 2003 Dan Walsh <dwalsh@redhat.com> 1.1-2
- Add Defattr to devel
- move libs to base kit

* Fri Dec 19 2003 Dan Walsh <dwalsh@redhat.com> 1.1-1
- Update to latest code from tresys
- Break into three separate packages for cmdline, devel and gui
- Incorporate the tcl patch

* Mon Dec 15 2003 Jens Petersen <petersen@redhat.com> - 1.0.1-3
- apply setools-1.0.1-tcltk.patch to build against tcl/tk 8.4
- buildrequire tk-devel

* Thu Nov 20 2003 Dan Walsh <dwalsh@redhat.com> 1.0.1-2
- Add Bwidgets to this RPM

* Tue Nov 4 2003 Dan Walsh <dwalsh@redhat.com> 1.0.1-1
- Upgrade to 1.0.1

* Wed Oct 15 2003 Dan Walsh <dwalsh@redhat.com> 1.0-6
- Clean up build

* Tue Oct 14 2003 Dan Walsh <dwalsh@redhat.com> 1.0-5
- Update with correct seuser.te

* Wed Oct 1 2003 Dan Walsh <dwalsh@redhat.com> 1.0-4
- Update with final release from Tresys

* Mon Jun 2 2003 Dan Walsh <dwalsh@redhat.com> 1.0-1
- Initial version
