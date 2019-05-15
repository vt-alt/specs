Summary: Terminal multiplexer
Name: tmux
Version: 2.9a
Release: alt1
Source0: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
License: BSD
Group: Terminals
Url: http://tmux.sourceforge.net/

# Automatically added by buildreq on Tue Mar 16 2010
BuildRequires: libevent-devel libncurses-devel

%description
tmux is a "terminal multiplexer". It allows a number of terminals (or
windows) to be accessed and controlled from a single terminal. It is
intended to be a simple, modern, BSD-licensed alternative to programs
such as GNU screen.

%prep
%setup

%build
./configure
%make_build

%install
%makeinstall

%files
%doc TODO CHANGES README
%_bindir/*
%_man1dir/*

%changelog
* Wed May 15 2019 Fr. Br. George <george@altlinux.ru> 2.9a-alt1
- Autobuild version bump to 2.9a

* Wed May 15 2019 Fr. Br. George <george@altlinux.ru> 2.9-alt1
- Autobuild version bump to 2.9

* Wed Apr 03 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.8-alt2
- fixed FTBFS: fixed build dependency

* Thu Feb 07 2019 Fr. Br. George <george@altlinux.ru> 2.8-alt1
- Autobuild version bump to 2.8

* Wed May 23 2018 Fr. Br. George <george@altlinux.ru> 2.7-alt1
- Autobuild version bump to 2.7

* Thu Mar 22 2018 Fr. Br. George <george@altlinux.ru> 2.6-alt1
- Autobuild version bump to 2.6

* Mon Sep 04 2017 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- Autobuild version bump to 2.5

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Autobuild version bump to 2.4

* Mon Oct 17 2016 Fr. Br. George <george@altlinux.ru> 2.3-alt1
- Autobuild version bump to 2.3

* Thu Jun 02 2016 Fr. Br. George <george@altlinux.ru> 2.2-alt1
- Autobuild version bump to 2.2

* Tue Oct 20 2015 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Autobuild version bump to 2.1

* Sun May 10 2015 Fr. Br. George <george@altlinux.ru> 2.0-alt1
- Autobuild version bump to 2.0

* Mon Feb 24 2014 Fr. Br. George <george@altlinux.ru> 1.9-alt1
- Autobuild version bump to 1.9

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Autobuild version bump to 1.6

* Wed Jul 20 2011 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Autobuild version bump to 1.5

* Sun Jun 19 2011 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4

* Wed Jul 28 2010 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Version up

* Wed Mar 17 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Version up

* Tue Nov 10 2009 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Version up

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Version up

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.9-alt1
- Version up

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.8-alt1
- Initial build from MDV

* Sun May 03 2009 Lev Givon <lev@mandriva.org> 0.8-1mdv2010.0
+ Revision: 371132
- Update to 0.8.

* Wed Feb 11 2009 Lev Givon <lev@mandriva.org> 0.7-1mdv2009.1
+ Revision: 339511
- Update to 0.7.

* Tue Jan 20 2009 Lev Givon <lev@mandriva.org> 0.6-1mdv2009.1
+ Revision: 331825
- import tmux

