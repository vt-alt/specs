Name: sispmctl
Version: 4.8
Release: alt1

Summary: GEMBIRD Silver Shield PM Control
License: GPLv2+
Group: System/Kernel and hardware

Url: http://sispmctl.sourceforge.net
Source0: %name-%version.tar.gz
Source1: 74-sispmctl.rules
Source100: sispmctl.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Fri Sep 23 2011
BuildRequires: libusb-compat-devel

%description
SIS-PM Control for Linux aka sispmctl is an application
enabling the use of the GEMBIRD (m)SiS-PM device family
(or a Revolt Power Switch) under Linux.

Add users who need to control the device to _sispm group.

%prep
%setup

%build
%autoreconf
%configure --enable-webless
%make_build

%install
%makeinstall
install -pDm644 %SOURCE1 %buildroot%_udevrulesdir/74-sispmctl.rules
rm -rf %buildroot%_defaultdocdir/%name

%pre
%_sbindir/groupadd -r -f _sispm >/dev/null 2>&1

%files
%_bindir/*
%_man1dir/*
%_libdir/*.so.*
%config(noreplace) %_udevrulesdir/74-sispmctl.rules
%doc AUTHORS ChangeLog README.md
%doc examples/

# TODO:
# - consider web part

# THANKS:
# - darktemplar@ for explaining me a silly lapse with the shared library

%changelog
* Sat Sep 12 2020 Michael Shigorin <mike@altlinux.org> 4.8-alt1
- new version (watch file uupdate)
- %%autoreconf to get rid of rpath
- shared library subpackage

* Mon Apr 13 2020 Michael Shigorin <mike@altlinux.org> 4.7-alt1
- new version (watch file uupdate)

* Fri Apr 03 2020 Michael Shigorin <mike@altlinux.org> 4.6-alt1
- new version (watch file uupdate)

* Thu Mar 12 2020 Michael Shigorin <mike@altlinux.org> 4.5-alt1
- new version (watch file uupdate)

* Mon Mar 09 2020 Michael Shigorin <mike@altlinux.org> 4.4-alt1
- new version (watch file uupdate)

* Sun Mar 08 2020 Michael Shigorin <mike@altlinux.org> 4.3-alt1
- new version (watch file uupdate)

* Fri Sep 27 2019 Michael Shigorin <mike@altlinux.org> 4.2-alt1
- new version (watch file uupdate)

* Sun Nov 18 2018 Michael Shigorin <mike@altlinux.org> 4.1-alt1
- new version (watch file uupdate)

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for sispmctl

* Sat Feb 20 2016 Michael Shigorin <mike@altlinux.org> 4.0-alt1
- new version (watch file uupdate)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 3.1-alt2
- added watch file

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 3.1-alt1
- 3.1

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 3.0-alt1
- 3.0
- dropped patches (ours merged upstream, debian's irrelevant)

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 2.7-alt3
- introduced udev rules and a pseudogroup

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 2.7-alt2
- it works!
  + fixed a buffer overflow when scanning (thanks led@)
  + applied a tail of debian patch as well
- verified against mSIS-PM helpfully provided by these nice folks:
  http://www.e-napruga.com.ua/good_details.php?good_key=648

* Tue Jul 21 2009 Michael Shigorin <mike@altlinux.org> 2.7-alt1
- built for ALT Linux

