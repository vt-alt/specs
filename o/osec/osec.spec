%define _unpackaged_files_terminate_build 1

Name: osec
Version: 1.3.0
Release: alt0.M90P.1

Summary: Lightweight file permission checker
License: GPL3
Group: System/Base
Url: https://github.com/legionus/osec

Source: %name-%version.tar
Patch0: %name-%version-allchanges.patch
Patch1: %name-%version-timerunit.patch

Requires(pre): shadow-utils

Provides: mtree-sec = %EVR
Obsoletes: mtree-sec

%define osec_statedir /var/lib/osec
%define osec_group osec
%define osec_user osec

# Automatically added by buildreq on Sat Apr 21 2007 (-bi)
BuildRequires: flex bison help2man libcdb-devel libcap-devel libattr-devel perl-RPM2
BuildRequires: libgcrypt-devel

%package cronjob
Summary: General scheduling framework for osec
Provides: %name-cron
Requires: %name = %EVR
Requires: %name-reporter
Group: System/Base
BuildArch: noarch

%package mailreport
Summary: Collection of reporters for osec
Group: System/Base
Provides: %name-reporter
Requires: %name = %EVR
Requires: %name-cron
Requires: /bin/mail
Requires: perl-base
Requires(pre): coreutils
BuildArch: noarch

%description
This package contains osec program which performs files integrity check
by traversing filesystem and making human readable reports about changes
and found files/directories with suspicious ownership or permissions.

%description cronjob
This package contains a general cron framework for osec and
a systemd timerunit.

%description mailreport
This package contains a set of reporters to use with osec:
osec_reporter - creates human readable reports;
osec_mailer - send mail only if some changes was detected;
osec_rpm_reporter - additional filter for osec_reporter,
add name of rpm packages for files in report.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall unitdir=%buildroot%_unitdir

cd %buildroot
#cron job file
mkdir -p -- etc/cron.d .%_datadir/osec
mv -- .%_datadir/osec.cron .%_datadir/osec/
echo '0 0 * * * root %_datadir/osec/osec.cron' > etc/cron.d/osec

#configs
mkdir -pm700 -- etc/osec
mv -- etc/dirs.conf etc/exclude.conf .%_datadir/pipe.conf etc/osec/
chmod 600 -- etc/osec/*.conf

#install directory for the databases
mkdir -p -- .%osec_statedir

%pre
/usr/sbin/groupadd -r -f %osec_group
/usr/sbin/useradd -r -g %osec_group -d /dev/null -s /dev/null -n %osec_user >/dev/null 2>&1 ||:

%triggerpostun -- %name < 0:1.0.0-alt1
rm -f %osec_statedir/osec.db.*

%files
%doc ChangeLog NEWS README src/restore data/osec-recheck
%_bindir/osec
%_bindir/osec2txt
%_bindir/txt2osec
%_bindir/osec-dbversion
%_bindir/osec-migrade-db
%_man1dir/*

%files cronjob
%config(noreplace) /etc/cron.d/osec
%dir %_datadir/osec
%attr(700,root,root) %_datadir/osec/osec.cron
%attr(770,root,%osec_group) %osec_statedir
%defattr(600,root,root,700)
%config(noreplace) /etc/osec
%config(noreplace) %_unitdir/osec.*

%files mailreport
%_bindir/osec_mailer
%_bindir/osec_reporter
%_bindir/osec_rpm_reporter

%changelog
* Wed Aug 05 2020 Paul Wolneykien <manowar@altlinux.org> 1.3.0-alt0.M90P.1
- Build version 1.3.0-alt1 for the p9 branch.
- Summarize more types of changes in the report (patch).
- Fixed extra space in the reported string (patch).
- Added systemd timer unit for OSEC (patch).

* Mon Jun 15 2020 Alexey Gladkov <legion@altlinux.ru> 1.3.0-alt1
- New version (1.3.0);
- Database creation is more error tolerant (ALT#38408, ALT#33207):
   - if osec failed to get the owner and user group by id, a numeric value will be used (ALT#33018).
   - if osec failed to read the file to calculate the checksum, an empty value will be used.
   - if osec failed to read symlink an empty value will be used.
- The mtime field includes nanoseconds.
- The basepath field has been added to the database.

* Tue May 14 2019 Alexey Gladkov <legion@altlinux.ru> 1.2.9-alt1
- New version (1.2.9);

* Mon Apr 22 2019 Alexey Gladkov <legion@altlinux.ru> 1.2.8-alt2
- Update URL.

* Fri Apr 12 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.8-alt1
- Added support for hash type switching.
- Added support for Stribog-512 hash.
- osec2txt and txt2osec utilities now properly work with xattr fields.

* Sat Dec 10 2016 Alexey Gladkov <legion@altlinux.ru> 1.2.7-alt3
- Use _FILE_OFFSET_BITS=64 (ALT#32805).
- Add default value to identify parser error (ALT#28770).

* Fri Dec 09 2016 Alexey Gladkov <legion@altlinux.ru> 1.2.7-alt2
- Add large-file support.
- Move exclude.conf to proper place.

* Sat Sep 03 2016 Alexey Gladkov <legion@altlinux.ru> 1.2.7-alt1
- New version (1.2.7);
- Fix EXCLUDE_FILE handling (ALT#30413);
- Add default exclude.conf (ALT#30413);
- dirs.conf: Add /usr/share (ALT#31706);
- Use perl-RPM2;

* Thu Oct 23 2014 Alexey Gladkov <legion@altlinux.ru> 1.2.6-alt1
- New version (1.2.6);
- Add file exclusion option;
- osec.cron: Add multiconfiguration support.

* Tue Feb 12 2013 Alexey Gladkov <legion@altlinux.ru> 1.2.5-alt3
- Fix incorrect use of xattr_nonexistent().

* Tue Jan 22 2013 Alexey Gladkov <legion@altlinux.ru> 1.2.5-alt2
- Do not check extended attributes when converting database.

* Fri Jan 18 2013 Alexey Gladkov <legion@altlinux.ru> 1.2.5-alt1
- New version (1.2.5);
- Add ability to ignore check of checksum and symlink;
- Add extended attributes support;
- report: Split xattrs in two parts: selinux and other attributies;
- osec.cron: Add number of added, deleted and changed files;
- Reduced the number of memory allocations.

* Mon Jul 23 2012 Alexey Gladkov <legion@altlinux.ru> 1.2.4-alt3
- Move cronjob from cron.daily to cron.d.

* Wed Oct 14 2009 Alexey Gladkov <legion@altlinux.ru> 1.2.4-alt2
- osec.cron: Add number of added, deleted and changed files;
- osec.cron, osec_mailer: Add IGNORE_NO_CHANGES option.

* Fri Oct 02 2009 Alexey Gladkov <legion@altlinux.ru> 1.2.4-alt1
- New version (1.2.4);
- Use fts(3) to traverse a file hierarchy;
- Add osec2txt and txt2osec utilities;
- Add simple restore utility;
- Add osec-recheck;
- Add time of last modification to report;
- osec.cron: Add allow customize ionice arguments;
- osec_mailer: Add number of added, deleted and changed files to a mail report.

* Thu Jul 30 2009 Alexey Gladkov <legion@altlinux.ru> 1.2.3-alt1
- New version (1.2.3);
- Add --ignore option;
- osec.cron: Add nice support.

* Thu Oct 30 2008 Alexey Gladkov <legion@altlinux.org> 1.2.2-alt1
- New version (1.2.2);
- Dont ignore cdb_seqnext() errors.
- Add --exclude and --exclude-from options.
- Fix for gcc-4.3.

* Thu Sep 18 2008 Alexey Gladkov <legion@altlinux.ru> 1.2.1-alt1
- New version (1.2.1);
- Create temprary database in subdirectory (ALT#9612);
- Add syslog messages in osec.cron (ALT#7099);
- Add ionice support in osec.cron;
- Small code optimization.

* Thu Jun 05 2008 Alexey Gladkov <legion@altlinux.ru> 1.2.0-alt1
- New version (1.2.0);
- Almost completely rewritten from scratch in C;
- Reduce requires (do not use openssl, libcdbxx);
- Change database format;
- Change checksum algorithm from MD5 to SHA1;
- Add osec database versioning;
- pipe.conf: Show hostname in mail subject;
- Improvements in osec:
  + track inode changes;
  + track symlink changes;

* Mon Apr 23 2007 Stanislav Ievlev <inger@altlinux.org> 1.1.0-alt1
- use std::tr1 instead of boost

* Sat Apr 21 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0.2-alt2
- Added /bin/mail to -mailreport subpackage requirements (#6137).
- Added osec to -mailreport subpackage requirements (#11589).
- Updated package description (#7098).
- Removed -mailreport %%post script.
- Made /var/lib/osec directory owned by root.
- Updated build dependencies.
- Cleaned up osec_mailer.
- Added lib64 directories to dirs.conf file.

* Thu Apr 19 2007 Stanislav Ievlev <inger@altlinux.org> 1.0.2-alt1
- fix requires

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt0.2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.org> 1.0.2-alt0.2
- rebuild

* Thu Mar 09 2006 Stanislav Ievlev <inger@altlinux.org> 1.0.2-alt0.1
- updated from CVS

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.1-alt3.1
- Rebuilt with libstdc++.so.6.

* Tue Jan 11 2005 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt3
- added new directory to list, fix building with gcc3.4

* Tue Oct 12 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt2
- update from CVS: added new directories to list, allow to work 
  with nonexistent directories

* Tue Aug 10 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt1
- 1.0.1 final: goto Sisyphus

* Tue Aug 03 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt0.rc2
- 1.0.1rc2
    osec: pathname quotation (space class symbols)
    osec_mailer: fix possible DoS

* Mon Jul 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.1-alt0.rc1
- 1.0.1rc1:
    - change ':' separator to '\t' to avoid extra quotation
    - more report filters

* Tue Jun 01 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt11
- update from CVS: fixed typo in reporter

* Tue May 18 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt10
- final

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.0-alt9.1
- Rebuilt with openssl-0.9.7d.

* Thu May 06 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt9
- rc5:
    improved filter (for files that turned into symlinks)

* Thu Apr 22 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt8
- rc4:
   improved filter (uninitialized values)
   improved cron job (save osec's exit code)

* Mon Apr 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt7
- rc3:
    added sorting to filter

* Fri Apr 02 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt6
- rc2:
   remove debug message from the report filter ;)

* Wed Mar 31 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt5
- rc1:
    minor fixes in report
    move rm -f from post to triggers

* Tue Mar 30 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt4
- minor improvements
- move post script to mailreport

* Mon Mar 29 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt3
- beta2
   improvements in reporter:
    -- print date
    -- don't print about new normal files during database init
   improvements in osec:
    -- print user and group names
    -- renice
    -- print information about processing and database init

* Fri Mar 26 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt2
- added reporter module

* Thu Mar 25 2004 Stanislav Ievlev <inger@altlinux.org> 1.0.0-alt1
- new ideas,new versions
  TODO: remove old *.db files
  
* Wed Mar 03 2004 Stanislav Ievlev <inger@altlinux.org> 0.6.0-alt2.1
- rebuild with libdb4.2
- this is a latest this osec generation release

* Wed May 14 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.0-alt2
- fix backward compatibility during delete

* Mon May 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.0-alt1
- new release

* Tue Apr 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.4-alt1
- minor features, bugfixes

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.3-alt1
- fix race during filesystem walking

* Wed Mar 12 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt4
- rebuid with latest libing

* Tue Mar 04 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt3
- fine sources

* Wed Feb 05 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt2
- unslash now in libing
- daedalus release

* Tue Feb 04 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt1
- fix map usage

* Mon Jan 27 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5.1-alt1
- minor fixes

* Thu Jan 16 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt3
- daedalus release

* Mon Jan 13 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt2
- sync with stable

* Fri Jan 10 2003 Stanislav Ievlev <inger@altlinux.ru> 0.5-alt1
- begin unstable branch

* Wed Jan 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt3
- sync with latest libing changes

* Fri Dec 27 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4.1-alt1
- development version
- ported to libing (general config file format)

* Wed Dec 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt2
- update documentation, write TODO and future plans

* Wed Dec 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt1
- final 0.4. TODO done.
- fix minor bugs, added filtering

* Mon Dec 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.6.4-alt1
- experimental: dropping privs, manpage, signal handlers
- config(noreplace) for cron.daily
- added contrib from Andy Gorev <gorev@mailru.com>

* Fri Nov 29 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.6.3-alt1
- more changes in memory work
- added support for symlink checkings ( when file became symlink )
- added command-line options

* Thu Nov 28 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.6.2-alt1
- development version. finally move to new object scheme
  added to Sisyphus 'cause previous version was too unstable (memory corruptions)
  new features will be in the next version.

* Mon Nov 25 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.5-alt1
- bugfixes, code improvements.

* Sun Nov 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.4-alt1
- light improvements in bad files' report
- more flexible config file (stage 1: checkers definitions for each directory)
  TODO: may be hash_storage object over storage?

* Wed Sep 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.3-alt2
- fixed bug in default config (database location)

* Mon Sep 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.3-alt1
- move to XML config file
  TODO: make osec more flexible (name,depth)

* Thu Aug 15 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.2-alt3
- light improvements in report and code

* Wed Aug 14 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.2-alt2
- light code cleanup

* Tue Aug 13 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.2-alt1
- Improvements. See changelog for details

* Thu Aug 08 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt2
- Added provides/obsoletes to mtree-sec

* Mon Aug 05 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3-alt1
- first release

* Fri Jul 12 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98.3-alt0.1
- fix very big first e-mails

* Thu Jul 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98.2-alt0.2
- new report style

* Wed Jul 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98.1-alt0.2
- don't see symlinks: useless thing

* Wed Jul 10 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98.1-alt0.1
- improvements

* Tue Jul 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.98-alt0.1
- Initial release for Sisyphus
