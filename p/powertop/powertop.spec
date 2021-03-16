Name: powertop
Version: 2.13
Release: alt1
Epoch: 1

Summary: Tool that helps you find what software is using the most power
License: GPLv2
Group: System/Kernel and hardware

Url: https://01.org/powertop/
Source0: %name-%version.tar
Source1: %name.service
Source2: %name.init
Source100: %name.watch

# Automatically added by buildreq on Tue May 15 2012
# optimized out: libncurses-devel libstdc++-devel libtinfo-devel pkg-config xz
BuildRequires: gcc-c++ libncursesw-devel libnl-devel libpci-devel zlib-devel
BuildRequires: autoconf-archive

%define cachedir %_cachedir/%name

%description
PowerTOP is a Linux tool that finds the software component(s) that make
your laptop use more power than necessary while it is idle.

PowerTOP works best on a laptop computer, or at least a computer with an
Intel mobile processor (certain small non-laptop devices also contain a
mobile processor). When using PowerTOP on a laptop, do so when running
on battery.

Please note that it also runs just fine with e.g. AMD CPUs. :)

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
install -d %buildroot%cachedir
touch %buildroot%cachedir/saved_{parameters,results}.powertop
install -pDm644 %SOURCE1 %buildroot%_unitdir/%name.service
install -pDm755 %SOURCE2 %buildroot%_initdir/%name

%post
%post_service %name
# Hack for powertop not to show warnings on first start
touch %cachedir/saved_{parameters,results}.powertop

%preun
%preun_service %name

%files -f %name.lang
%_sbindir/*
%_datadir/bash-completion
%_man8dir/*
%doc README.md
%dir %cachedir
%ghost %cachedir/saved_*.powertop
%_unitdir/%name.service
%_initdir/%name

%changelog
* Fri Jun 26 2020 Anton Farygin <rider@altlinux.ru> 1:2.13-alt1
- 2.13

* Fri Apr 24 2020 Anton Farygin <rider@altlinux.ru> 1:2.12-alt1
- 2.12

* Mon Oct 07 2019 Anton Farygin <rider@altlinux.ru> 1:2.11-alt1
- 2.11

* Sat Jan 19 2019 Anton Farygin <rider@altlinux.ru> 1:2.10-alt1
- 2.10

* Sun Jun 18 2017 Anton Farygin <rider@altlinux.ru> 1:2.9-alt1
- new version (closes: #32459)

* Tue Nov 10 2015 Michael Shigorin <mike@altlinux.org> 1:2.8-alt1
- new version (watch file uupdate)

* Sun May 31 2015 Michael Shigorin <mike@altlinux.org> 1:2.7-alt2
- add the initscript

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 1:2.7-alt1
- new version (watch file uupdate)

* Mon Mar 09 2015 Michael Shigorin <mike@altlinux.org> 1:2.6.1-alt3
- added proper sysv initscript

* Mon Jan 26 2015 Michael Shigorin <mike@altlinux.org> 1:2.6.1-alt2
- rolled back to version that actually works

* Mon Jan 26 2015 Michael Shigorin <mike@altlinux.org> 2.7-alt2
- applied Fedora patches to fix --auto-tune overflow

* Wed Nov 26 2014 Michael Shigorin <mike@altlinux.org> 2.7-alt1
- new version (watch file uupdate)

* Mon May 26 2014 Michael Shigorin <mike@altlinux.org> 2.6.1-alt1
- new version (watch file uupdate)

* Sat Nov 23 2013 Michael Shigorin <mike@altlinux.org> 2.5-alt1
- new version (watch file uupdate)

* Mon Jul 22 2013 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- new version (watch file uupdate)

* Mon Apr 08 2013 Michael Shigorin <mike@altlinux.org> 2.3-alt1
- new version (watch file uupdate)

* Mon Apr 08 2013 Michael Shigorin <mike@altlinux.org> 2.1-alt2
- added watch file (thanks debian with its #695891)

* Mon Sep 03 2012 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- 2.1

* Wed May 16 2012 Michael Shigorin <mike@altlinux.org> 2.0-alt2
- re-added %_cachedir/%name created by hand
- NB: Url: has changed

* Tue May 15 2012 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- 2.0
  + autoconf based build
  + binary moved from %_bindir to %_sbindir
- added a tiny explanatory note to package description :)

* Sat Aug 20 2011 Victor Forsiuk <force@altlinux.org> 1.98-alt1
- 1.98

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 1.13-alt1
- 1.13

* Fri Jan 15 2010 Victor Forsyuk <force@altlinux.org> 1.11-alt2
- Increase config lines buffer size. Closes ALT #22750.

* Thu Jun 18 2009 Victor Forsyuk <force@altlinux.org> 1.11-alt1
- 1.11

* Tue Jun 17 2008 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- 1.10

* Thu Dec 27 2007 Victor Forsyuk <force@altlinux.org> 1.9-alt1
- 1.9

* Thu Aug 30 2007 Victor Forsyuk <force@altlinux.org> 1.8-alt1
- 1.8

* Mon Jul 09 2007 Victor Forsyuk <force@altlinux.org> 1.7-alt1
- 1.7

* Tue May 29 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt1
- 1.5

* Wed May 16 2007 Victor Forsyuk <force@altlinux.org> 1.2-alt1
- 1.2

* Mon May 14 2007 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- Initial build.
