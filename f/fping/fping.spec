Name: fping
Version: 4.2
Release: alt1

Summary: %name - A tool to quickly ping N number of hosts to determine their reachability
Summary(ru_RU.UTF-8): аналог ping для использования в скриптах.
License: BSD with advertising
Group: Security/Networking
Url: http://www.fping.org

Source0: %name-%version.tar.gz
Source1: fping.control

%description
fping is a ping(1) like program which uses the Internet Control Message
Protocol (ICMP) echo request to determine if a host is up. fping is
different from ping in that you can specify any number of hosts on the
command line, or specify a file containing the lists of hosts to ping.
Instead of trying one host until it timeouts or replies, fping will send out
a ping packet and move on to the next host in a round-robin fashion. If a
host replies, it is noted and removed from the list of hosts to check. If a
host does not respond within a certain time limit and/or retry limit it will
be considered unreachable.

%description -l ru_RU.UTF-8
fping это аналог известной утилиты ping(1) использующей протокол ICMP для
определения доступности удаленного хоста. fping создан для использования
в perl и shell скриптах. Поддерживает возможность сканирования диапазона
адресов.

%prep
%setup -q

%build
%configure --enable-safe-limits

%make_build

%install
%make_install install DESTDIR=%buildroot

install -d %buildroot%_controldir
%__sed -e 's|-=BINNAME=-|fping|'  < %SOURCE1 > %buildroot%_controldir/fping
chmod +x %buildroot%_controldir/fping*

%pre
%pre_control fping

%post
%post_control -s restricted fping

%files
%_sbindir/*
%config %_controldir/*
%_man8dir/*
%doc INSTALL CHANGELOG.md COPYING doc/CHANGELOG.pre-v4 doc/README.1992

%changelog
* Sat Aug 17 2019 Sergey Y. Afonin <asy@altlinux.org> 4.2-alt1
- 4.2

* Thu May 17 2018 Sergey Y. Afonin <asy@altlinux.ru> 4.0-alt1
- 4.0
- removed fping6: fping and fping6 are now unified into one binary
- built with --enable-safe-limits (was defauilt for 3.x)

* Fri Jul 21 2017 Sergey Y. Afonin <asy@altlinux.ru> 3.16-alt1
- 3.16

* Sat Jul 09 2016 Sergey Y. Afonin <asy@altlinux.ru> 3.13-alt1
- 3.13

* Fri Oct 24 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.10-alt1
- 3.10

* Fri Dec 20 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.8-alt1
- 3.8 (ALT 29657)

* Fri May 17 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4-alt2
- added "netadmin" facility for control(8), switched to "restricted"
  by default (ALT 22846#c1)

* Thu May 16 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4-alt1
- 3.4 (with IPv6)
- fixed license (now "BSD with advertising", same with FC 19 package)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.4b2-alt4.qa1
- NMU: rebuilt for debuginfo.

* Sun Apr 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.4b2-alt4
- added control(8) support (ALT #11891). Default state is restricted.

* Sun Apr 08 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.4b2-alt3
- rebuilt with latest Sisyphus

* Sat Nov 16 2002 Igor Homyakov <homyakov at altlinux dot ru> 2.4b2-alt2
- spec cleanup (grammatic mistakes, wrong URL: )

* Tue Sep 03 2002 Igor Homyakov <homyakov at altlinux dot ru> 2.4b2-alt1
- little code cleanup
- first build for ALT Linux
