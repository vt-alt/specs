# This spec is backported to ALTLinux t7 automatically by rpmbph script. Do not edit it.
#
Name: rkhunter
Version: 1.4.2
Release: alt4

Summary: Rootkit scans for rootkits, backdoors and local exploits
License: GPLv2
Group: Monitoring

Url: http://rkhunter.sourceforge.net/

BuildArch: noarch

Source: %name-%version.tar
Source2: rkhunter.sysconfig
Source3: printosnumber.sh
Source4: ru.lng
Source5: rkhunter.conf

#
# Fix issue with ipcs command and locales
#
Patch1: rkhunter-1.4.2-ipcs-locale.patch

Patch2: fix-lang-update-grep.patch

Requires: crontabs
Requires: su, binutils, kmod, findutils, grep
Requires: libe2fs, procps, lsof, wget
Requires: perl, mailx, logrotate

BuildPreReq: mailx crontabs perl-base perl-Digest-SHA1
# Note: mailx and crontabs are not needed to be noticed explicitly,
#       but are placed here for better manageability at install stage
#       and for suppress warnings from find-requires at build stage.

Summary(ru_RU.UTF8): Поиск троянских коней и закладок в программах

# ToDo: /usr/bin/rkhunter strictly lookups helper scripts in /usr/lib/%name.
#       More correct should be to place them to /usr/share/%name (%_datadir/%name)
#       because they are platform-independent.
%define util_dir     %_libexecdir/%name
%define scripts_dir  %util_dir/scripts
%define runonce_dir  %util_dir/adminutils

%define data_dir     %_localstatedir/%name
%define tmp_dir      %data_dir/tmp
%define db_dir       %data_dir/db
%define hash_list    defaulthashes.dat

%define doc_dir      %_docdir/%name-%version
%define cron_daily   %_sysconfdir/cron.daily
%define cron_script  %cron_daily/01-%name

%description
Rootkit scanner is scanning tool to ensure you for about 99.9%% you're
clean of nasty tools. This tool scans for rootkits, backdoors and local
exploits by running tests like:
	- MD5 hash compare
	- Look for default files used by rootkits
	- Wrong file permissions for binaries
	- Look for suspected strings in LKM and KLD modules
	- Look for hidden files
	- Optional scan within plaintext and binary files
	- Software version checks
	- Application tests

Rootkit Hunter is released as a GPL licensed project
and free for everyone to use.

%description -l ru_RU.UTF8
Сканер Rootkit проверяет вашу систему на наличие закладок и троянских коней.
Для этого используются следующие тесты:
	- проверка контрольных сумм MD5
	- поиск файлов, используемых закладками
	- неверные права доступа к программам
	- сигнатуры закладок в модулях ядра
	- поиск невидимых файлов
	- дополнительное сканирование внутри текстовых и двоичных файлов
	- проверка версий программ
	- тесты для приложений

%prep
%setup -n %name
cp %SOURCE3 files/development

%patch1 -p1
%patch2 -p1

install %SOURCE4 files/i18n/ru
install %SOURCE5 files/

cat <<'EOF' >%name.logrotate
%_logdir/%name/%name.log {
    weekly
    notifempty
    create 640 root root
}
EOF

%build
# We have nothing to configure... yet...
files/development/rpmhashes.sh files/ > files/%hash_list

%install
mkdir -p %buildroot{%_bindir,%_sysconfdir,%_man8dir}
mkdir -p %buildroot{%scripts_dir,%runonce_dir,%doc_dir,%db_dir,%tmp_dir}
mkdir -p %buildroot%db_dir/i18n

install -d  %buildroot%_logdir/%name

install -m750 -p files/rkhunter                %buildroot%_bindir/
install -m750 -p files/{*.pl,*.sh}             %buildroot%scripts_dir/
install -m750 -p files/development/{*.pl,*.sh} %buildroot%runonce_dir/
install -m644 -p files/*.8                     %buildroot%_man8dir/
install -m640 -p files/*.dat                   %buildroot%db_dir/
install -m644 -p files/i18n/en                 %buildroot%db_dir/i18n/en
install -m644 -p files/i18n/ru		       %buildroot%db_dir/i18n/ru
install -m644 -p files/{CHANGELOG,README,FAQ,ACKNOWLEDGMENTS} %buildroot%doc_dir/
install -D -m640 -p %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -D -m644 -p %name.logrotate         %buildroot%_sysconfdir/logrotate.d/%name


# (cjo) Put installation root in configuration file,
#       then copy the rest of the file from the original.
cat >> %buildroot%_sysconfdir/%name.conf << __EOF__
## Next three lines installed automatically by RPM.
## Do not change unless you know what you're doing...
INSTALLDIR=%_prefix
DBDIR=%db_dir
TMPDIR=%tmp_dir
SCRIPTDIR=%scripts_dir

__EOF__

cat files/%name.conf >> %buildroot%_sysconfdir/%name.conf
chmod 640 %buildroot%_sysconfdir/%name.conf

# Only root should use rkhunter (at least for now)
chmod o-rwx -R %buildroot{%scripts_dir,%db_dir}

# make a cron.daily file to mail us the reports
mkdir -p "%buildroot%cron_daily"
cat > "%buildroot%cron_script" << __EOF__
#!/bin/sh
( echo "Rootkit Hunter daily report"
  date
  echo "========================================="
  echo
  echo "Empty message means that no errors found."
  echo
  %_bindir/%name --cronjob --report-warnings-only
) | /bin/mail -s '%name Daily Run' root
__EOF__
chmod 750 %buildroot%cron_script

# make script for update MD5 hashes
cat > %buildroot%runonce_dir/create_defaulthashes << __EOF__
#!/bin/sh
#
#   %runonce_dir/create_defaulthashes -- part of Rootkit Hunter
#
#   Purpose: updates MD5 signatures of your binary stuff.
#
#   Uses GnuPG for signing created list:
#    - you should have already generated GPG key
#    - should be executed interactively for passing key password
#

cd %db_dir
tstamp=\$(LANG=en date '+%%Y%%m%%d_%%H%%M%%S')
for f in %hash_list %hash_list.asc %hash_list.sig; do
    test -f "\$f" && mv -f "\$f" "\$f.saved.\$tstamp"
done


cd %runonce_dir
./rpmhashes.sh > %db_dir/%hash_list
# ./createhashes.sh >> %db_dir/%hash_list

cd %db_dir
gpg --detach-sign --armor --yes %hash_list
gpg --verify %hash_list.asc

echo "
Don't forget to repeat this command after every software upgrade!"

## EOF ##
__EOF__
chmod 750 %buildroot%runonce_dir/create_defaulthashes

%post

%preun
rm -f %db_dir/%hash_list.{asc,*saved.*}


%files
%_bindir/%name
%cron_script
%util_dir
%data_dir
%attr(770,root,root) %tmp_dir
%doc_dir
%_man8dir/*
#db_dir/i18n/en
#db_dir/i18n/ru
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %verify(not mtime) %_sysconfdir/%name.conf
%config(noreplace) %verify(not mtime) %_sysconfdir/sysconfig/%name
%exclude %db_dir/%hash_list
%config(noreplace) %verify(not mtime size md5) %db_dir/%hash_list
%dir %_logdir/%name



%changelog
* Mon Jul 13 2020 Pavel Vasenkov <pav@altlinux.org> 1.4.2-alt4
- Fix STARTUP_PATHS configuration option

* Wed Apr 13 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.4.2-alt3
- Fix /etc/logrotate/rkhunter

* Tue Apr 12 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.4.2-alt2
- Add russian translate

* Thu Apr 07 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.4.2-alt1
- Updated to 1.4.2

* Fri May 01 2009 Slava Semushin <php-coder@altlinux.ru> 1.3.4-alt1
- Updated to 1.3.4
- Updated home page

* Sat Aug 09 2008 Slava Semushin <php-coder@altlinux.ru> 1.3.2-alt2
- Fixed cron script
- Added some scripts and hidden files to white list
- More strict permissions to temporary directory
- Added Packager tag (noted by repocop)

* Sun Jul 27 2008 Slava Semushin <php-coder@altlinux.ru> 1.3.2-alt1
- New maintainer
- Updated to 1.3.2 (Closes: #12778)
- Added binutils to Requires (Closes: #11871)
- More proper License and Url tags
- Updated BuildPreReq
- Spec cleanup

* Tue May 24 2005 Ilya Evseev <evseev@altlinux.ru> 1.2.7-alt1
- updated to new version, nothing interested for ALTLinux

* Wed May 11 2005 Ilya Evseev <evseev@altlinux.ru> 1.2.6-alt1
- updated to version 1.2.6

* Wed May  4 2005 Ilya Evseev <evseev@altlinux.ru> 1.2.5-alt1
- updated to version 1.2.5

* Tue Apr 26 2005 Ilya Evseev <evseev@altlinux.ru> 1.2.4-alt1
- updated to version 1.2.4
- changed cron.daily script: mail body is now always not empty

* Fri Mar 25 2005 Ilya Evseev <evseev@altlinux.ru> 1.2.3-alt1
- updated to version 1.2.3

* Sat Mar 19 2005 Ilya Evseev <evseev@altlinux.ru> 1.2.2-alt1
- updated to version 1.2.2

* Wed Feb 23 2005 Ilya Evseev <evseev@altlinux.ru> 1.2.1-alt1
- version 1.2.1, revisited patches
- changed URL in specfile
- disable '--update' feature, use updating from AltLinux repositories instead of.

* Sun Feb 13 2005 Ilya Evseev <evseev@altlinux.ru> 1.2.0-alt1
- version 1.2.0

* Sat Jan  1 2005 Ilya Evseev <evseev@altlinux.ru> 1.1.9-alt1
- version 1.1.9
- OS.dat patch is not needed now
- removed incorrect dependency from /bin/ksh,
  added strict dependencies from mailx and crontabs

* Fri Dec  3 2004 Ilya Evseev <evseev@altlinux.ru> 1.1.8-alt2
- records order in specfile is changed for workaround bug described here:
  https://bugzilla.altlinux.org/show_bug.cgi?id=5573
- package URL is changed from program site to packager site
- os.dat.diff is updated for ALM2.4
  
* Fri Oct  1 2004 Ilya Evseev <evseev@altlinux.ru> 1.1.8-alt1
- first ALT build
- added ALM22 signature to OS.dat
- added OS number autodetection, used by checksum calculation scripts,
  tested under ALM22 only, should work under any RedHat-derived Linux.
- added create_defaulthashes script for rebuilding checksum database
  after software upgrades.
- cron script calls %name with --skip-application-check option
  because builds installed from updates.altlinux.org
  already contains all needed security fixes.

* Tue Aug 10 2004 Michael Boelen - 1.1.5
- Added update script
- Extended description

* Sun Aug 08 2004 Greg Houlette - 1.1.5
- Changed the install procedure eliminating the specification of
  destination filenames (only needed if you are renaming during install)
- Changed the permissions for documentation files (root only overkill)
- Added the installation of the rkhunter Man Page
- Added the installation of the programs_{bad, good}.dat database files
- Added the installation of the LICENSE documentation file
- Added the chmod for root only to the /var/rkhunter/db directory

* Sun May 23 2004 Craig Orsinger (cjo) <cjorsinger@earthlink.net>
- version 1.1.0-1.cjo
- changed installation in accordance with new rootkit installation
  procedure
- changed installation root to conform to LSB. Use standard macros.
- added recursive remove of old build root as prep for install phase

* Wed Apr 28 2004 Doncho N. Gunchev - 1.0.9-0.mr700
- dropped Requires: perl - rkhunter works without it 
- dropped the bash alignpatch (check the source or contact me)
- various file mode fixes (.../tmp/, *.db)
- optimized the %%files section - any new files in the
  current dirs will be fine - just %%__install them.

* Mon Apr 26 2004 Michael Boelen - 1.0.8-0
- Fixed missing md5blacklist.dat

* Mon Apr 19 2004 Doncho N. Gunchev - 1.0.6-1.mr700
- added missing /usr/local/rkhunter/db/md5blacklist.dat
- patched to align results in --cronjob, I think rpm based
  distros have symlink /bin/sh -> /bin/bash
- added --with/--without alignpatch for conditional builds
  (in case previous patch breaks something)

* Sat Apr 03 2004 Michael Boelen / Joe Klemmer - 1.0.6-0
- Update to 1.0.6

* Mon Mar 29 2004 Doncho N. Gunchev - 1.0.0-0
- initial .spec file

