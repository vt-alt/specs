%define haproxy_user    _haproxy
%define haproxy_group   %haproxy_user
%define haproxy_home    %_localstatedir/haproxy
%define haproxy_confdir %_sysconfdir/haproxy
%define haproxy_datadir %_datadir/haproxy

%def_enable lua

Name: haproxy
Version: 2.0.6
Release: alt1

Summary: HA-Proxy is a TCP/HTTP reverse proxy for high availability environments
License: GPLv2+
Group: System/Servers

URL: http://www.haproxy.org/
Source: %name-%version.tar
Source1: %name.cfg
Source2: %name.init
Source3: %name.logrotate

BuildRequires: libpcre2-devel zlib-devel libssl-devel libsystemd-devel
%{?_enable_lua:BuildRequires: liblua5-devel >= 5.3}

%description
HA-Proxy is a TCP/HTTP reverse proxy which is particularly suited for high
availability environments. Indeed, it can:
- route HTTP requests depending on statically assigned cookies
- spread the load among several servers while assuring server persistence
  through the use of HTTP cookies
- switch to backup servers in the event a main one fails
- accept connections to special ports dedicated to service monitoring
- stop accepting connections without breaking existing ones
- add/modify/delete HTTP headers both ways
- block requests matching a particular pattern

It needs very little resource. Its event-driven architecture allows it to easily
handle thousands of simultaneous connections on hundreds of instances without
risking the system's stability.

%prep
%setup

%build
# Recommended optimization option for x86 builds
%ifarch %ix86 x86_64
regparm_opts="USE_REGPARM=1"
%endif

%ifarch mipsel
addlib_opts=ADDLIB=-latomic
%endif

%make_build CPU="generic" TARGET="linux-glibc" USE_OPENSSL=1 USE_PCRE2=1 USE_ZLIB=1 USE_SYSTEMD=1 %{?_enable_lua:USE_LUA=1} \
	${regparm_opts:-} ${addlib_opts:-} PREFIX="%_prefix" ADDINC="$(pcre2-config --cflags)" CFLAGS="%optflags"

pushd contrib/halog
%make halog OPTIMIZE="%optflags"
popd

#pushd contrib/iprange
#%make iprange OPTIMIZE="%optflags"
#popd

pushd contrib/systemd
%make haproxy.service PREFIX="%_prefix"
popd

%install
%make_install install-bin DESTDIR=%buildroot PREFIX="%_prefix" TARGET="linux-glibc"
%make_install install-man DESTDIR=%buildroot PREFIX="%_prefix"

install -p -D -m 0644 %SOURCE1 %buildroot%haproxy_confdir/%name.cfg
install -D -m 0755 %SOURCE2 %buildroot%_initrddir/haproxy
install -p -D -m 0644 contrib/systemd/haproxy.service %buildroot%_unitdir/%name.service
install -p -D -m 0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -d -m 0755 %buildroot%haproxy_home
install -d -m 0755 %buildroot%haproxy_datadir
install -d -m 0755 %buildroot%_bindir
install -p -m 0755 contrib/halog/halog %buildroot%_bindir/halog
#install -p -m 0755 contrib/iprange/iprange %buildroot%_bindir/iprange
cp -p examples/errorfiles/* %buildroot%haproxy_datadir/


%pre
%_sbindir/groupadd -r -f %haproxy_group >/dev/null 2>&1 ||:
%_sbindir/useradd -g %haproxy_group -c 'HA Proxy' \
    -d %haproxy_home -s /dev/null -r -l -M %haproxy_user >/dev/null 2>&1 ||:

%post
%post_service haproxy

%preun
%preun_service haproxy

%files
%doc CHANGELOG LICENSE README ROADMAP doc/architecture.txt doc/configuration.txt doc/intro.txt doc/management.txt doc/proxy-protocol.txt examples/*.cfg
%dir %haproxy_confdir
%config(noreplace) %haproxy_confdir/%name.cfg
%dir %haproxy_datadir
%haproxy_datadir/*
%_logrotatedir/%name
%_initrddir/%name
%_unitdir/%name.service
%_sbindir/*
%_bindir/*
%_man1dir/*
%attr(-,%haproxy_user,%haproxy_group) %dir %haproxy_home

%changelog
* Tue Sep 24 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.6-alt1
- 2.0.6

* Fri Aug 23 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.5-alt1
- 2.0.5

* Fri Aug 09 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.4-alt1
- 2.0.4 (Fixes: CVE-2019-14241)

* Tue Jul 23 2019 Ivan A. Melnikov <iv@altlinux.org> 2.0.1-alt2
- fix build on mipsel

* Sat Jun 29 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt1
- 2.0.1

* Tue May 07 2019 Alexey Shabalin <shaba@altlinux.org> 1.9.7-alt1
- 1.9.7

* Thu Jan 17 2019 Alexey Shabalin <shaba@altlinux.org> 1.9.2-alt1
- 1.9.2
- fixed start systemd unit

* Thu Jan 03 2019 Alexey Shabalin <shaba@altlinux.org> 1.9.0-alt1
- 1.9.0

* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 1.8.14-alt1
- 1.8.14

* Tue Sep 04 2018 Alexey Shabalin <shaba@altlinux.org> 1.8.13-alt2
- rebuild with openssl-1.1

* Fri Aug 24 2018 Alexey Shabalin <shaba@altlinux.org> 1.8.13-alt1
- 1.8.13

* Thu Jun 28 2018 Alexey Shabalin <shaba@altlinux.ru> 1.8.12-alt1
- 1.8.12

* Tue Jun 26 2018 Alexey Shabalin <shaba@altlinux.ru> 1.8.11-alt1
- 1.8.11

* Thu Feb 08 2018 Alexey Shabalin <shaba@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Mon Jan 29 2018 Alexey Shabalin <shaba@altlinux.ru> 1.8.3-alt1
- 1.8.3
- build with pcre2

* Wed Sep 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.9-alt1
- 1.7.9

* Sun Aug 06 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.8-alt1
- 1.7.8

* Fri Apr 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.5-alt1
- 1.7.5

* Wed Mar 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt2
- fix build options

* Tue Mar 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Mon Mar 06 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.3-alt1
- 1.7.3
- do not build contrib/iprange

* Thu Jan 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1
- build with lua support

* Thu Sep 29 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.9-alt1
- 1.6.9

* Thu Jun 30 2016 Lenar Shakirov <snejok@altlinux.ru> 1.6.5-alt2
- Pack haproxy-systemd-wrapper

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Wed Oct 21 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Mon Oct 19 2015 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Fri Aug 21 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.14-alt1
- 1.5.14
- run demon as _haproxy user
- update default config
- update init script
- add systemd unit
- build with libssl support
- build with zlib support

* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 1.4.20-alt1
- 1.4.20

* Sun Jan 08 2012 Victor Forsiuk <force@altlinux.org> 1.4.19-alt1
- 1.4.19

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 1.4.18-alt1
- 1.4.18

* Sat Aug 13 2011 Victor Forsiuk <force@altlinux.org> 1.4.16-alt1
- 1.4.16

* Sat Apr 09 2011 Victor Forsiuk <force@altlinux.org> 1.4.15-alt1
- 1.4.15

* Tue Mar 29 2011 Victor Forsiuk <force@altlinux.org> 1.4.14-alt1
- 1.4.14

* Wed Mar 23 2011 Victor Forsiuk <force@altlinux.org> 1.4.13-alt1
- 1.4.13
- Build halog (log statistics reporter).
- Enable transparent proxy and splice(2).

* Fri Feb 11 2011 Victor Forsiuk <force@altlinux.org> 1.4.11-alt1
- 1.4.11

* Tue Dec 07 2010 Victor Forsiuk <force@altlinux.org> 1.4.10-alt2
- Fix expected user in init-script (Closes: #24570).

* Mon Dec 06 2010 Victor Forsiuk <force@altlinux.org> 1.4.10-alt1
- 1.4.10

* Sat Nov 06 2010 Victor Forsiuk <force@altlinux.org> 1.4.9-alt1
- 1.4.9

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 1.4.8-alt1
- 1.4.8

* Wed Jun 09 2010 Victor Forsiuk <force@altlinux.org> 1.4.6-alt1
- 1.4.6

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue Apr 06 2010 Victor Forsiuk <force@altlinux.org> 1.4.3-alt1
- 1.4.3

* Thu Mar 18 2010 Victor Forsiuk <force@altlinux.org> 1.4.2-alt1
- 1.4.2

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Feb 16 2010 Victor Forsiuk <force@altlinux.org> 1.3.23-alt1
- 1.3.23

* Fri Oct 03 2008 Sergey Ivanov <seriv@altlinux.ru> 1.3.15.4-alt1
- Release 1.3.15.4

* Tue Jul 03 2007 Sergey Ivanov <seriv@altlinux.ru> 1.3.12-alt1
- Initial build using release 1.3.12 for Sisyphus
