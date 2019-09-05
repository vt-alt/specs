Name: fwbuilder
Version: 6.0.0
Release: alt1.beta.68.a880

Summary: Firewall Builder
License: GPLv2+
Group: Security/Networking

Url: http://www.fwbuilder.org/
# Vcs-Git: https://github.com/fwbuilder/fwbuilder.git
Source: %name-%version.tar

Obsoletes: %name-doc < %EVR
Obsoletes: %name-devel < %EVR
Obsoletes: lib%name < %EVR

Provides: %name-pf = %EVR
Provides: %name-ipf = %EVR
Provides: %name-ipfw = %EVR
Provides: %name-ipt = %EVR
Provides: %name-cisco = %EVR
Provides: %name-procurve = %EVR

Obsoletes: %name-pf < %EVR
Obsoletes: %name-ipf < %EVR
Obsoletes: %name-ipfw < %EVR
Obsoletes: %name-ipt < %EVR
Obsoletes: %name-cisco < %EVR
Obsoletes: %name-procurve < %EVR

BuildRequires: cmake rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel qt5-networkauth-devel
BuildRequires: libxml2-devel libxslt-devel zlib-devel
BuildRequires: libnet-snmp-devel
BuildRequires: libssl-devel
BuildRequires: cppunit-devel

%description
Firewall Builder consists of a GUI and set of policy compilers for various
firewall platforms. It helps users maintain a database of objects and allows
policy editing using simple drag-and-drop operations. GUI generates firewall
description in the form of XML file, which compilers then interpret and generate
platform-specific code. Several algorithms are provided for automated network
objects discovery and bulk import of data. The GUI and policy compilers are
completely independent, this provides for a consistent abstract model and the
same GUI for different firewall platforms.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
install -pm644 doc/transfer_secuwall.1 %buildroot%_man1dir/

%files
%doc %_defaultdocdir/%name
%_bindir/*
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_man1dir/*

%changelog
* Sat Aug 31 2019 Alexey Shabalin <shaba@altlinux.org> 6.0.0-alt1.beta.68.a880
- master snapshot a8802a3bc96d7f9228e670c29d7d87127afcacce
- merge all subpackages to main package

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.0.3599-alt1.1
- Fixed build with glibc 2.16

* Fri Mar 30 2012 Victor Forsiuk <force@altlinux.org> 5.1.0.3599-alt1
- 5.1.0.3599

* Tue Jan 03 2012 Victor Forsiuk <force@altlinux.org> 5.0.1.3592-alt1
- 5.0.1.3592

* Sun Jul 31 2011 Victor Forsiuk <force@altlinux.org> 5.0.0.3568-alt1
- 5.0.0.3568

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 4.2.2.3541-alt1
- 4.2.2.3541

* Fri Dec 10 2010 Victor Forsiuk <force@altlinux.org> 4.1.3-alt1
- 4.1.3

* Mon Oct 18 2010 Victor Forsiuk <force@altlinux.org> 4.1.2-alt1
- 4.1.2

* Wed Sep 08 2010 Victor Forsiuk <force@altlinux.org> 4.1.1-alt1
- 4.1.1

* Tue Aug 10 2010 Victor Forsiuk <force@altlinux.org> 4.1.0-alt1
- 4.1.0

* Fri Jun 18 2010 Victor Forsiuk <force@altlinux.org> 4.0.2-alt1
- 4.0.2

* Thu Mar 18 2010 Victor Forsiuk <force@altlinux.org> 4.0.0-alt1
- 4.0.0

* Mon Sep 28 2009 Victor Forsyuk <force@altlinux.org> 3.0.7-alt1
- 3.0.7

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 3.0.5-alt1
- 3.0.5

* Fri Dec 12 2008 Victor Forsyuk <force@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Dec 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.8-alt1
- 2.1.8

* Fri Nov 03 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.7-alt2
- fixed compilers name

* Wed Nov 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.1.7-alt1
- 2.1.7

* Sun May 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.12-alt2
- updated build dependencies

* Sun Apr 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.12-alt1
- 2.0.12

* Sun Apr 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.11-alt1
- 2.0.11

* Fri Mar 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.10-alt3
- rebuild with libbind-9.3.2

* Tue Jan 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 2.0.10-alt2
- move to freedesktop menu

* Wed Nov 16 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.10-alt1
- 2.0.10

* Sun Sep 18 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.9-alt1
- 2.0.9

* Sun Jul 10 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Sat May 14 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Mon Feb 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Mon Jan 17 2005 Valery Inozemtsev <shrek@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Sat Dec 04 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Nov 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.3-alt1.1
- Removed libelf-devel from build dependencies.

* Sun Oct 03 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Sat Sep 04 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Fri Aug 13 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.1-alt1
- bugfix release

* Wed Aug 11 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt3
- fix spec file

* Thu Jul 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt2
- 2.0.0 release

* Mon Jul 26 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt1.20040726
- the latest nightly build 2004.07.25

* Sat Jul 03 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt1.20040703
- the latest nightly build 2004.07.03

* Tue Jun 29 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt1.20040629
- the latest nightly build 2004.06.29

* Sun Jun 27 2004 Valery Inozemtsev <shrek@altlinux.ru> 2.0.0-alt1.20040625
- the latest nightly build 2004.06.25

* Fri May 14 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt2
- Rebuilt with openssl-0.9.7d

* Wed Feb 04 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- new version

* Sun Dec 14 2003 Valery Inozemtsev <shrek@altlinux.ru> 1.1.1-alt1
- New version

* Mon Nov 3 2003 Valery Inozemtsev <shrek@altlinux.ru> 1.0.11-alt1
- Build for ALT Linux Master 2.2
- Add menu entry

* Thu Jul 17 2003 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt1
- Add initialization script for firewall daemon

* Sun Jul 13 2003 Valery Inozemtsev <shrek@altlinux.ru> 1.0.10-alt0
- initial ALT Linux Master 2.2 build
