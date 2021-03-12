Name: alien
Version: 8.95
Release: alt9

Summary: Install Debian and Slackware Packages with RPM

Group: Archiving/Other
License: GPL
Url: https://sourceforge.net/projects/alien-pkg-convert/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-url: http://ftp.debian.org/debian/pool/main/a/alien/%{name}_%version.tar.bz2
Source: %name-%version.tar
Patch: %name-Makefile.PL.patch
Patch1: alien-dpkg-tar.xz.patch
Patch2: alien-alt-plaintext-scripts.patch
Patch3: alien-alt-fix-missing-spaces-in-control.patch

# Automatically added by buildreq on Mon Feb 13 2006
BuildRequires: perl-devel perl-podlators

# ar from binutils needs for deb unpack
Requires: /usr/bin/ar

%description
Alien allows you to convert Debian, Slackware and Stampede Packages
into RPM packages. It can also convert RPM packages into Slackware,
Debian and Stampede packages.

This is a tool only suitable for binary packages.

It is recommended install dpkg package to full dpkg support.

%prep
%setup
%patch -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir INSTALLMAN3DIR=%_man3dir

%install
%perl_vendor_install VARPREFIX=%buildroot

%files
%_bindir/%name
%perl_vendor_privlib/Alien/
%_man1dir/*
%_man3dir/*

%changelog
* Tue Mar 09 2021 Andrey Cherepanov <cas@altlinux.org> 8.95-alt9
- Fix missing spaces in control fields in deb packages.

* Mon Jun 24 2019 Andrey Cherepanov <cas@altlinux.org> 8.95-alt8
- Replace %% for %%%% in RPM scripts.

* Thu Jun 13 2019 Andrey Cherepanov <cas@altlinux.org> 8.95-alt7
- Store RPM scripts in plaintext format.

* Tue Jul 10 2018 Vitaly Lipatov <lav@altlinux.ru> 8.95-alt6
- add control.tar.xz support (ALT bug 35145)

* Sun Aug 06 2017 Vitaly Lipatov <lav@altlinux.ru> 8.95-alt5
- add /usr/bin/ar requires (ALT bug 30604)

* Sun Aug 06 2017 Vitaly Lipatov <lav@altlinux.ru> 8.95-alt4
- fix data.tar hack

* Sun Aug 06 2017 Vitaly Lipatov <lav@altlinux.ru> 8.95-alt3
- add data.tar.xz support (ALT bug 30594)

* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 8.95-alt2
- cleanup spec, fix project URL

* Thu Dec 24 2015 Hihin Ruslan <ruslandh@altlinux.ru> 8.95-alt1
- new version

* Thu Mar 29 2012 Dmitriy Kruglikov <dkr@altlinux.ru> 8.86-alt3
- Help message redirected into stdout

* Wed Mar 28 2012 Dmitriy Kruglikov <dkr@altlinux.ru> 8.86-alt2
- Added Option for adding the dependency list from file

* Wed Mar 28 2012 Dmitriy Kruglikov <dkr@altlinux.ru> 8.86-alt1
- Updated to 8.86

* Sun Dec 19 2010 Vitaly Lipatov <lav@altlinux.ru> 8.83-alt2
- cleanup spec, fix build (thanks, real@)

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 8.83-alt1
- new version 8.83 (with rpmrb script)

* Fri Jan 22 2010 Vitaly Lipatov <lav@altlinux.ru> 8.79-alt1
- new version 8.79 (with rpmrb script)

* Thu Mar 05 2009 Vitaly Lipatov <lav@altlinux.ru> 8.74-alt1
- new version 8.74 (with rpmrb script)

* Fri Feb 13 2009 Vitaly Lipatov <lav@altlinux.ru> 8.73-alt1
- new version 8.73 (with rpmrb script)

* Mon Jul 21 2008 Vitaly Lipatov <lav@altlinux.ru> 8.72-alt1
- new version 8.72 (with rpmrb script)

* Tue Jan 01 2008 Vitaly Lipatov <lav@altlinux.ru> 8.69-alt1
- new version 8.69 (with rpmrb script)

* Sun Jun 18 2006 Vitaly Lipatov <lav@altlinux.ru> 8.64-alt0.1
- new version 8.64 (with rpmrb script)
- change Source URL

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 8.63-alt1
- new version (8.63)
- remove my patch (the same in mainstream now)

* Fri Feb 17 2006 Vitaly Lipatov <lav@altlinux.ru> 8.62-alt1
- remove empty dir from package
- fix bug with dir permission unpacked with cpio -d (see bug #9106 also)

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 8.62-alt0.1
- new version

* Tue Dec 27 2005 Vitaly Lipatov <lav@altlinux.ru> 8.60-alt0.1
- new version
- cleanup spec

* Mon Oct 07 2002 Stanislav Ievlev <inger@altlinux.ru> 8.20-alt1
- 8.20

* Thu Aug 02 2001 Dmitry V. Levin <ldv@altlinux.ru> 7.27-alt1
- 7.27

* Mon Jun 25 2001 Sergie Pugachev <fd_rag@altlinux.ru> 7.24-alt2
- Rebuild with perl-5.6.1

* Wed Jun 20 2001 Sergie Pugachev <fd_rag@altlinux.ru> 7.24-alt1
- 7.24

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 7.15-ipl1mdk
- 7.15

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 7.13-ipl2mdk
- RE adaptions.

* Thu Jan 04 2001 David BAUDENS <baudens@mandrakesoft.com> 7.13-2mdk
- Requires: perl-devel
- Use %%make macro
- Fix description
- Fix make install
- Fix %%files section
- Spec clean up

* Thu Jan 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 7.13-1mdk
- updated to 7.13

* Mon Dec 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.12-1mdk
- updated to 7.12

* Thu Nov 23 2000 Daouda Lo <daouda@mandrakesoft.com> 7.10-1mdk
- release

* Fri Nov 17 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.9-1mdk
- updated to 7.9

* Tue Sep 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.8-1mdk
- updated to 0.7.8

* Thu Jul 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.5-2mdk
- BM
- macros

* Mon Jun 26 2000 Laurent Grawet <laurent.grawet@ibelgique.com> 7.5-1mdk
- version 7.5
- added /usr/lib/perl5/site_perl/5.005/Alien/* in %files section
- added %clean section

* Fri May 05 2000 Geoffrey Lee <snailtalk@linux-mandrake.com> 7.0-1mdk
- version 7.0
- various spec improvements
- some spec file fixes after it was broken when upgrading to 7.0

* Thu Apr 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 6.59-1mdk
- v6.59
- fix location of manpage
- fix group
- fix file section

* Mon Dec 06 1999 Lenny Cartier <lenny@mandrakesoft.com>
- dummy as I am I forgot the .bz2 archive, fixed.

* Fri Dec 03 1999 lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- fix filelist

