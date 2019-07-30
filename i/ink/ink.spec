Name: ink
Version: 0.5.3
Release: alt1

Summary: A command line tool which displays the ink level of your printer.
License: GPL
Group: Monitoring

Url: http://ink.sf.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: %name-%version.tar.gz
Source1: %name.watch

BuildPreReq: libinklevel-devel >= 0.6

%description
Command line tool for displaying ink level of your printer using libinklevel.

%prep
%setup 

%build
%configure
%make_build OPTFLAGS="%optflags"

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri May 24 2019 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- 0.5.3
- minor spec cleanup/fixup

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1.qa2
- NMU: fixed bugs in watch file

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Sep 30 2010 Ilya Mashkin <oddity@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sun Jan 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version
- return from orphaned
- add watch file

* Sun Oct 10 2004 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt2
- set OPTFLAGS when building
- spec fixes
- Url changed

* Thu Dec 04 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.3-alt1
- new version

* Tue Nov 11 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt2.1
- minor spec fixes, Group changed again

* Thu Oct 23 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt2
- Group fixed

* Fri Oct 10 2003 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- built for Sisyphus
