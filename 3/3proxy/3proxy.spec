%define _pseudouser_user     _3proxy
%define _pseudouser_group    _3proxy
#define _pseudouser_home     %_localstatedir/_3proxy
%define _pseudouser_home     /

Name: 3proxy
Version: 0.6.1
Release: alt2

Summary: Proxy server

License: GPL
Group: System/Servers
Url: http://securityvulns.ru/soft/


Source: %name-%version.tar
Source1: 3proxy.init
Source2: 3proxy.conf
Source3: 3proxy.sysconfig
Source4: README-ALT.CP1251
Source5: README-ALT.UTF8

Patch1: %name-%version-alt-droproot.patch
Patch2: %name-%version-alt-changes.patch
Patch3: CVE-2019-14495.patch

Packager: Afanasov Dmitry <ender@altlinux.org>

BuildRequires: libcap-devel

%description
3proxy -- light proxy server. 

%prep
%setup -q 
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make_build -f Makefile.Linux
cp %SOURCE5 %SOURCE4 ./

%install
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_man3dir
mkdir -p %buildroot%_man8dir
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_var/run/%name
install -m755 -D src/3proxy %buildroot%_bindir/3proxy
install -m755 -D src/dighosts %buildroot%_bindir/dighosts
install -m755 -D src/ftppr %buildroot%_bindir/ftppr
install -m755 -D src/mycrypt %buildroot%_bindir/mycrypt
install -m755 -D src/pop3p %buildroot%_bindir/pop3p
install -m755 -D src/proxy %buildroot%_bindir/proxy
install -m755 -D src/socks %buildroot%_bindir/socks
install -m755 -D src/tcppm %buildroot%_bindir/tcppm
install -m755 -D src/udppm %buildroot%_bindir/udppm
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/3proxy
install -m644 %SOURCE2 %buildroot%_sysconfdir/3proxy.conf

install -pD -m644 man/*.3 %buildroot%_man3dir
install -pD -m644 man/*.8 %buildroot%_man8dir

install -pD -m644 authors %buildroot%_datadir/%name-%version/AUTHORS
install -pD -m644 copying %buildroot%_datadir/%name-%version/COPYING
install -pD -m644 news %buildroot%_datadir/%name-%version/NEWS
install -pD -m644 Readme %buildroot%_datadir/%name-%version/README
install -pD -m644 Changelog %buildroot%_datadir/%name-%version/Changelog
install -pD -m644 README-ALT* %buildroot%_datadir/%name-%version/

%pre
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'The 3proxy daemon' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%preun
%preun_service %name

%post
%post_service %name

%files
%_bindir/*
%config(noreplace) %_sysconfdir/3proxy.conf
%config(noreplace) %_sysconfdir/sysconfig/3proxy
%_initdir/%name
%_man3dir/*
%_man8dir/*
%attr(775, root, %_pseudouser_group) %_logdir/%name
%attr(775, root, %_pseudouser_group) %_var/run/%name
%_datadir/%name-%version

%changelog
* Wed Dec 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt2
- Applied security fix from upstream (Fixes: CVE-2019-14495).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Dec 19 2009 Afanasov Dmitry <ender@altlinux.org> 0.6.1-alt1
- new version

* Tue Jun 09 2009 Afanasov Dmitry <ender@altlinux.org> 0.6-alt2
- drop some config options while rewrite droproot patch (see README.ALT)
- use capabilities when root is dropped (closes: #18060)
- use _3proxy as default user (closes: #11942)

* Thu Mar 19 2009 Afanasov Dmitry <ender@altlinux.org> 0.6-alt1
- new version (closes: #20198).
- adopt droproot code to new version.
- move droproot code into droproot patch.
- move minor change into alt-changes patch.

* Wed Dec 03 2008 Afanasov Dmitry <ender@altlinux.org> 0.5.3k-alt4
- add README-ALT.*
- set default user to root untill #11942 be fixed

* Tue Dec 02 2008 Afanasov Dmitry <ender@altlinux.org> 0.5.3k-alt3
- fix typo in initscript (Closes: #18066)
- move initscript vars to /etc/sysconfig/3proxy (e.g. username)
- remove setuid root checks from setuid patch

* Tue Nov 25 2008 Afanasov Dmitry <ender@altlinux.org> 0.5.3k-alt2
- fix bugs:
  + new initscript (#11944, #11943)
  + do not replace config (#12032)
  + pack man pages (#12032)
  + run daemon as pseudouser (#11942)

* Tue Nov 18 2008 Afanasov Dmitry <ender@altlinux.org> 0.5.3k-alt1
- new version

* Fri Apr 13 2007 Lunar Child <luch@altlinux.ru> 0.5.3h-alt1
- new version

* Wed Mar 21 2007 Lunar Child <luch@altlinux.ru> 0.5.3g-alt2
- Added init script.
- Added new trivial config file.

* Tue Mar 20 2007 Lunar Child <luch@altlinux.ru> 0.5.3g-alt1
- First build for ALT Linux Sisyphus
