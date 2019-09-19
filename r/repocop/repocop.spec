Name: repocop
Version: 0.81
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Repocop is a repository unit tests platform.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Source: %name-%version.tar

Provides: repocop-collector-rpm = 0.01

# Recommends, not requires fakeroot
Requires: fakeroot >= 1.9
# pax is preferred over cpio due to correct unpacking for unreadable directories
Requires: pax
BuildRequires: perl-devel perldoc perl-autodie
BuildRequires: perl(Data/Array2ArrayMap/Hash/XSTree.pm)
BuildRequires: perl(RPM/Header.pm) perl(RPM/Vercmp.pm) perl-DBD-SQLite
BuildRequires: perl-RPM-Source-Editor
BuildRequires: perl-File-Lock-ParentLock
BuildRequires: perl-HTML-Template-Pro
BuildRequires: perl(Source/Shared/CLI.pm) perl(Source/Shared/Resource/Verbose.pm)
Requires: perl-DBD-SQLite sqlite3

# obsolete repocop-sqlite interface
Conflicts: repocop-unittest-unmet-dependency < 0.04
# statedir
Conflicts: repocop-collector-specfile < 0.04

%description
Repocop is a repository unit tests platform.
It provides a framework for running integration tests
(unit tests) for a set of rpm files (or the whole repository).

Test results are cached, so tests are run only if necessary.

Note that tests are separate packages: repocop is a platform,
it itself contains no tests. This package contains only
the test runner, repocop-run, internal utils and the set
of report generators.
For example, to get html report of test results, run
repocop-report-html with whe same arguments as repocop-run.

%package tools
Group: Development/Other
Summary: repocop tools for auto repairing repocop packages
Conflicts: repocop < 0.78
Requires: perl-RPM-Source-Editor > 0.9215
Requires: %name = %version-%release

%description tools
%summary

%package resource-html
Group: Development/Other
Summary: repocop report in HTML form.
Conflicts: repocop < 0.79

%description resource-html
Repocop is a repository unit tests platform.
This package provides common resources for various repocop based HTML reports.

%package report-html
Group: Development/Other
Summary: repocop report in HTML form.
Conflicts: repocop < 0.79
Requires: repocop-resource-html = %EVR

%description report-html
Repocop is a repository unit tests platform.
This package provides repocop HTML reports.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install

for i in \
  %_datadir/repocop/pkgtests \
  %_datadir/repocop/srctests \
  %_datadir/repocop/pkgcollectors \
  %_datadir/repocop/srccollectors \
  %_datadir/repocop/sqlite-functions \
  %_datadir/repocop/common \
; do mkdir -p $RPM_BUILD_ROOT$i
done
mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/rpm/
install -m644 pkgcollectors/rpm/*.sql.* $RPM_BUILD_ROOT%_datadir/repocop/pkgcollectors/rpm/

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/fixscripts/
#install -m644 fixscripts/*.pl $RPM_BUILD_ROOT%_datadir/repocop/fixscripts/

install -m755 common/* $RPM_BUILD_ROOT%_datadir/repocop/common/

mkdir -p $RPM_BUILD_ROOT%_datadir/repocop/html/
install -m644 img/* $RPM_BUILD_ROOT%_datadir/repocop/html/

for backend in fsprefix fsmd5prefix ; do
    mkdir -p %buildroot%_prefix/libexec/repocop/backends/$backend
    cp -a libexec/backends/$backend/repocop-test-* %buildroot%_prefix/libexec/repocop/backends/$backend/
done

%files
#doc README ChangeLog
%_bindir/repocop-*
%_man1dir/repocop-*
# not supported yet
%exclude %_bindir/repocop-check-against-repository
# report-html
%exclude %_bindir/repocop-report-html
%exclude %_man1dir/repocop-report-html.*
# resource-html
%exclude %perl_vendor_privlib/Test/Repocop/Report/HTML.pm
# tools
%exclude %_bindir/repocop-report-diff
%exclude %_man1dir/repocop-report-diff.*
%exclude %_bindir/repocop-tools-*
%exclude %_man1dir/repocop-tools-*
%exclude %_bindir/repocop-nmu-*
%exclude %_man1dir/repocop-nmu-*
%exclude %perl_vendor_privlib/Test/Repocop/RepocopResource.pm
%exclude %perl_vendor_privlib/Test/Repocop/FixscriptFactory.pm
%dir %_datadir/repocop/pkgtests
%dir %_datadir/repocop/srctests
%dir %_datadir/repocop/pkgcollectors
%dir %_datadir/repocop/srccollectors
%dir %_datadir/repocop/sqlite-functions
%_datadir/repocop/common
%perl_vendor_privlib/T*
#perl_vendor_man3dir/*
%_datadir/repocop/pkgcollectors/rpm
%_prefix/libexec/repocop

%files tools
#doc fixscripts/*.pl
%dir %_datadir/repocop/fixscripts
%_bindir/repocop-tools-*
%_man1dir/repocop-tools-*
%_bindir/repocop-report-diff
%_man1dir/repocop-report-diff.*
%_bindir/repocop-nmu-*
%_man1dir/repocop-nmu-*
%perl_vendor_privlib/Test/Repocop/RepocopResource.pm
%perl_vendor_privlib/Test/Repocop/FixscriptFactory.pm

%files resource-html
%_datadir/repocop/html
%perl_vendor_privlib/Test/Repocop/Report/HTML.pm

%files report-html
%_bindir/repocop-report-html
%_man1dir/repocop-report-html.*

%changelog
* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1
- new version

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- new version

* Wed Jul 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.79-alt1
- new version; added new TestDb Status API

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- new version

* Fri Jul 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- new version; new API

* Sat Jun 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1
- fixes for p8 acl
- purge by src.rpm names for quick testing

* Wed Jun 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1
- repocop-run --swift optimization
- bugfixes in repocop-report-diff
- updated documantation

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- do not use deprecated COPYRIGHT rpm tag

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- new Shared::CLI

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- new TransformContainer fixes

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1
- use new TransformContainer.

* Wed Oct 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.70-alt5
- get rid of RPM::Constants

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.70-alt4
- use explicit RPM modules

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.70-alt3
- use RPM::Vercmp

* Wed Apr 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.70-alt2
- bugfix release

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1
- support for fresh RPM::Source::Editor

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- TestDB interface

* Sun Oct 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.68-alt2
- added fsmd5prefix backend

* Sun Oct 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- initial support for multiple backends

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.67-alt3
- repocop-report-html fixes

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.67-alt2
- skip empty dirs in diff

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1
- added repocop-report-html

* Sun Feb 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1
- added repocop-nmu-tool

* Thu Jan 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- development release

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- development release

* Thu Oct 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- repocop-check and repocop-check-against-repository

* Tue Aug 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.62-alt2
- maintainance release

* Thu Jul 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- added generic purge script

* Thu Jul 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- support for extra source collectors

* Mon Jul 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- support for external meged REPOCOP_DISTROTEST_DBDIR

* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- support for distrotests

* Sun Jul 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- pluggable acl support

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- maintainance release

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.56-alt3
- support for lowercase SQL schemas

* Tue Nov 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.56-alt2
- maintainance release

* Wed Nov 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- new version

* Sat Aug 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.55-alt4
- disabled by-packager reports

* Sat Aug 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.55-alt3
- bugfix release

* Sat Aug 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.55-alt2
- bugfix release

* Sat Aug 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- maintainance release

* Tue Aug 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.54-alt2
- bugfix release

* Mon Aug 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- maintainance release

* Tue May 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- support for RPM::Source::Editor 0.62 in fixscripts

* Tue May 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- support for fresh RPM::Source::Editor

* Sun Nov 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.51-alt2
- rebuild w/new perl

* Fri Oct 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- bugfix release

* Fri Oct 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- added perl interface for repocop-test-*

* Fri Oct 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- repocop-discard-test now destroys collectors too

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- bugfix release

* Sun Oct 17 2010 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- bugfix release

* Wed Oct 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- refactoring; test tmp dir is now available for purge also

* Tue Mar 23 2010 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- support for pluggable sql functions.

* Mon Mar 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- bugfixes in filepattern option support

* Sun Mar 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- filepattern option support

* Sat Mar 20 2010 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- support for new evrcmp in rpm

* Thu Feb 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- added strict_canonpath function to repocop-sqlite

* Tue Jan 05 2010 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- new accelerated testMtimeDB backend.

* Mon Jan 04 2010 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- new incompatible format of testdb (nested dirs) due to ext3 limitations.

* Sun Jan 03 2010 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- repocop-report-qa-robot moved to separate package

* Fri Jan 01 2010 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- fixed bug in 3-diff mail reports (thanks to icesik@)

* Tue Nov 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- txt report: added warnings

* Sat Nov 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2
- fixscripts: flexible release increment 

* Fri Nov 13 2009 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- sort by leader in txt report

* Mon Nov 09 2009 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- improvements in diff generator

* Thu Nov 05 2009 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- git-am support

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- hasher tar output support

* Sat Oct 31 2009 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- diff generator: added digest patch

* Fri Oct 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- improvements in diff generator
- removed repocop-fix-backend

* Fri Oct 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- added Fixscripts.pm as fixscripts backend.

* Thu Oct 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- repocop-cachedir-lock now works

* Sat Oct 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- qa-robot: switched to new/old/updated list

* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- repocop-report-prometeus* moved to separate package

* Wed Oct 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- separated execution of package tests and posttests

* Tue Sep 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- added preliminary support for posttests

* Sat Aug 01 2009 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- fixes in rpm unpacking

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- increased verbosity in repocop-fix-backend

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- REPOCOP_TEST_STATEDIR variable

* Sun Feb 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- options now are read once per test

* Sat Feb 14 2009 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- fixed misleading warnings

* Thu Feb 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- options support

* Mon Feb 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- purge script support

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- db schema changes:
  + rpm.db now collects VENDOR and DISTRIBUTION tags (icesik@)
  + source rpms metadata is moved to SRCRPM table.

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- repocop-sqlite interface is changed to sqlite3 compatible.

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt5
- fixed bug in rpm collector (thanks to mithraen@)

* Wed Dec 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt4
- protection from error in db init

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt3
- repocop-fix-srpm optimization: skipping not repairable tests

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- added repocop-sqlite wrapper

* Fri Nov 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- rpm.db: compatible SQL schema change

* Fri Nov 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt26
- bugfixes; added repocop/repocop-discard-test utility

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt25
- support for given list of SRPMS

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt24
- nice changelog in fixed srpms

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt23
- fixed bug for post -p with arguments

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt22
- bugfix release

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt21
- bugfix release

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt20
- repocop-tools-ls-rpmbuild-bs-environment: 
  removed conflicts in list

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt19
- added repocop-tools-ls-rpmbuild-bs-environment

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt18
- lots of new options in repocop-fix-*

* Fri Nov 14 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt17
- fixed bug for SCRIPTPROG != /bin/sh

* Thu Nov 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt16
- removed deprecated patch generators
post_ldconfig.pl
postun_ldconfig.pl
update_menus.pl 
  and those that should be deprecated:
desktop-mime-entry.pl  (desktop-file-utils)
shared-mime-info.pl    (shared-mime-info)
update_wms.pl          (xinit)

* Thu Oct 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt15
- added qa-robot reports
- removed arch dirs due to sisyphus_check constraints
  + /usr/lib*/repocop/pkgtests
  + /usr/lib*/repocop/srctests
  + /usr/lib*/repocop/pkgcollectors
  + /usr/lib*/repocop/srccollectors

* Wed Aug 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt14
- proper signal handling

* Wed Aug 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt13
- code cleanup

* Sat Jul 26 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt12
- added diffs for info level tests

* Tue Jul 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt11
- fix in diff generation

* Sat Jun 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt10
- added repocop-report-prometeus-dump tool

* Thu Jun 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt9
- fixes in repocop-tools

* Wed Jun 04 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt8
- fixed some warnings

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt7
- dry run optimizations

* Fri May 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt6
- patches support in prometeus

* Tue May 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt5
- packaged repocop-test-experimental

* Tue May 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt4
- support for new prometeus db layout

* Tue May 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt3
- done cleanup optimization
- added -experimental message level

* Wed Apr 30 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- RPM db schema optimization

* Tue Apr 22 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- ALTLinux acl support

* Tue Apr 22 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fixed multitest in repocop-fix-srpm

* Mon Apr 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.9
- added tools subpackage with repocop-fix-* utilities

* Wed Apr 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.8
- sharing common options and synoipsis

* Wed Apr 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.7
- support for virtual tests in repocop-run

* Sat Apr 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.6
- fixed bug in rpm_provides table
- repocop-fix-* scripts merged to .git repo
- use File::Basename

* Wed Apr 09 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.5
- new exclude/include options
- repocop-test-* now allows virtual tests

* Wed Apr 09 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.4
- refactoring: added Options.pm

* Sat Mar 29 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.3
- fixed bug for PROVIDES and OBSOLETES tables in rpm.db

* Sat Mar 29 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.2
- added info test status

* Mon Mar 24 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt0.1
- support for collectors

* Fri Mar 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- bugfix release

* Fri Mar 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- preparatinon for data to be collected in SQLite db

* Wed Mar 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.9
- use RPM::Header;
- added support for srpm tests.

* Wed Mar 19 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.8
- support for relative paths (#14986)
- added --pkgtest-dir local test dir option (#14989)

* Tue Mar 18 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.7
- repocop-run is rewritten in perl

* Mon Mar 17 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.6
- refactoring: sharing common options
- added --newer option (suggested by damir@)
- added repocop-report-stdout (suggested by damir@)
- added repocop-check (suggested by damir@)

* Fri Mar 14 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.5
- fixed bug in repocop-prometeus (thanks to Andrey (liks@))
- refactoring: common code is moved to lib

* Wed Mar 12 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.4
- added qa-robot report tools
- added support for environment variable REPOCOP_CACHEDIR 

* Tue Mar 11 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.3
- added -l to repocop-purge-*
- test upgrade detection

* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.2
- basic support for tests with state

* Wed Mar 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt0.1
- added repocop-purge-* scripts
- added prometeus report tool
- added man pages

* Sun Mar 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- changed cache structure, added metadata

* Thu Feb 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added text file report generator
- disabled using fakeroot by default.

* Mon Feb 25 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- First build for Sisyphus.
