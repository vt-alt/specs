Name: imapfilter
Version: 2.7.5
Release: alt2

Summary: mail filtering utility
License: BSD
Group: System/Configuration/Networking

Url: https://github.com/lefcha/imapfilter

# Cloned from git://github.com/lefcha/imapfilter.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: lua-devel libpcre2-devel libssl-devel

%description
%name is a mail filtering utility.  It connects to remote mail servers
using the Internet Message Access Protocol (IMAP), sends searching
queries to the server and processes mailboxes based on the results. It
can be used to delete, copy, move, flag, etc.  messages residing in
mailboxes at the same or different mail servers.  The 4rev1 and 4
versions of the IMAP protocol are supported.

%prep
%setup -q
%patch -p1

%build
%make_build PREFIX=%_prefix

%install
make BINDIR=%buildroot%_bindir SHAREDIR=%buildroot%_datadir/%name MANDIR=%buildroot%_mandir install

%files
%_bindir/*
%_datadir/%name
%_mandir/*/*

%changelog
* Fri Jan 29 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.5-alt2
- Updated certificate paths to ALT-specific values.

* Fri Jan 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.5-alt1
- 2.7.5 (Fixes CVE-2016-10937).

* Tue Jan 29 2019 Vladimir Lettiev <crux@altlinux.org> 2.6.12-alt1
- 2.6.12

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.5-alt1.1
- rebuild with new lua 5.3

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 2.5.5-alt1
- New version 2.5.5

* Fri Oct 05 2012 Vladimir Lettiev <crux@altlinux.ru> 2.5.3-alt1
- New version 2.5.3

* Wed Oct 19 2011 Vladimir Lettiev <crux@altlinux.ru> 2.3-alt1
- New version 2.3
- Source cloned from upstream git

* Thu Mar 10 2011 Vladimir Lettiev <crux@altlinux.ru> 2.2.3-alt1
- New version 2.2.3
- Changed Url of project

* Thu Nov 18 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2.2-alt2
- rebuilt with libssl 1.0.0a

* Mon Mar 15 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2.2-alt1
- New version 2.2.2

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.10-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu Mar 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 2.0.10-alt1
- new version

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 1.3-alt1
- new version
- fix 10472

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.2-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Sun Nov 12 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.2.2-alt1
- new version

* Thu Nov 24 2005 Eugene Ostapets <eostapets@altlinux.ru> 1.1.1-alt1
- new version

* Thu Jul 5 2005 Eugene Ostapets <eostapets@altlinux.ru> 1.1-alt1
- build for ALT Linux
