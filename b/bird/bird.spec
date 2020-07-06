%define _localstatedir %_var

Name: bird
Version: 1.6.8
Release: alt2
Summary: BIRD Internet Routing Daemon

Group: Networking/Other
License: GPL
URL: http://bird.network.cz

# Cloned from git://git.nic.cz/bird.git
Source: %name-%version.tar
Source1: %name.init
Source2: %name.service
Source3: %{name}6.init
Source4: %{name}6.service

Patch: %name-%version-alt.patch

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libreadline-devel libncurses-devel flex glibc-kernheaders OpenSP linuxdoc-tools

%description
BIRD is an Internet Routing Daemon designed to support all the routing
technology used in the today's Internet or planned to be used in near
future and to have a clean extensible architecture allowing new routing
protocols to be incorporated easily. Among other features, BIRD supports:

 * both IPv4 and IPv6 protocols
 * multiple routing tables
 * the Border Gateway Protocol (BGPv4)
 * the Routing Information Protocol (RIPv2)
 * the Open Shortest Path First protocol (OSPFv2)
 * a virtual protocol for exchange of routes between different routing
   tables on a single host
 * a command-line interface allowing on-line control and inspection of
   status of the daemon
 * soft reconfiguration (no need to use complex online commands to
   change the configuration, just edit the configuration file and notify
   BIRD to re-read it and it will smoothly switch itself to the new
   configuration, not disturbing routing protocols unless they are
   affected by the configuration changes)
 * a powerful language for route filtering

BIRD has been developed at the Faculty of Math and Physics, Charles
University, Prague, Czech Republic as a student project. It can be
freely distributed under the terms of the GNU General Public License.

%package -n bird6
Group: Networking/Other
Summary: BIRD Internet Routing Daemon, ipv6 enabled
Requires: %name = %version-%release
%description -n bird6
%summary

%prep
%setup
%patch -p1

%build
%autoreconf
%define _configure_script ../configure

# gcc detects overflow in strncpy at proto/rip/auth.c:134
# but it's false alarm, relax gcc
export CFLAGS="%optflags -D_FORTIFY_SOURCE=1"

mkdir build-bird6
pushd build-bird6
%configure --enable-ipv6 --with-protocols=all
%make_build
popd

mkdir build-bird4
pushd build-bird4
%configure --with-protocols=all
%make_build
popd

pushd doc
    make prog.sgml
    ./sgml2html prog.sgml
    ./sgml2html bird.sgml
popd

%install
%makeinstall -C build-bird6
%makeinstall -C build-bird4

install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m644 %SOURCE2 %buildroot%_unitdir/%name.service
install -pD -m755 %SOURCE3 %buildroot%_initdir/%{name}6
install -pD -m644 %SOURCE4 %buildroot%_unitdir/%{name}6.service

%post
%post_service bird

%preun
%preun_service bird

%post -n bird6
%post_service bird6

%preun -n bird6
%preun_service bird6

%files
%_initdir/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/%name.conf
%_sbindir/%name
%_sbindir/%{name}c
%_sbindir/%{name}cl
%doc NEWS README doc/*.html

%files -n bird6
%_initdir/%{name}6
%_unitdir/%{name}6.service
%config(noreplace) %_sysconfdir/%{name}6.conf
%_sbindir/%{name}6
%_sbindir/%{name}c6
%_sbindir/%{name}cl6

%changelog
* Fri Jun 26 2020 Slava Aseev <ptrnine@altlinux.org> 1.6.8-alt2
- fixed bad header length test in OSPF (adapted from bird2)

* Thu Jun 11 2020 Anton Farygin <rider@altlinux.ru> 1.6.8-alt1
- 1.6.8

* Thu Sep 12 2019 Anton Farygin <rider@altlinux.ru> 1.6.7-alt1
- 1.6.7 (Fixes: CVE-2019-16159)

* Tue May 21 2019 Anton Farygin <rider@altlinux.ru> 1.6.4-alt5
- added upstream patch against errors with clang build

* Wed Jan 16 2019 Anton Farygin <rider@altlinux.ru> 1.6.4-alt2
- cleared from %%ubt macros

* Thu Mar 22 2018 Anton Farygin <rider@altlinux.ru> 1.6.4-alt1
- new version

* Wed Jan 11 2017 Anton Farygin <rider@altlinux.ru> 1.6.3-alt1
- new version

* Thu Dec 08 2016 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- 1.6.2
- added % macros for easy backporting to stable branches

* Sun Oct 25 2015 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Sep 09 2014 Alexey Shabalin <shaba@altlinux.ru> 1.4.4-alt1
- 1.4.4
- add separate bird6 service
- add systemd unit files

* Thu Aug 28 2014 Andriy Stepanov <stanv@altlinux.ru> 1.4.3-alt2
- add status entry for init script

* Tue Apr 22 2014 Vladimir Lettiev <crux@altlinux.ru> 1.4.3-alt1
- New version 1.4.3

* Mon Nov 25 2013 Vladimir Lettiev <crux@altlinux.ru> 1.4.0-alt1
- New version 1.4.0
- Packed light client birdcl{,6}

* Sun Jan 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.3.9-alt1
- New version 1.3.9

* Thu Oct 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3.8-alt1
- New version 1.3.8

* Mon Nov 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3.4-alt1
- New version 1.3.4

* Thu Oct 06 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3.3-alt1
- New version 1.3.3
- Source cloned from upstream git
- Build html docs from sgml

* Sun Nov 28 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.5-alt2
- Implemented reload() in the init script (CLoses: #24532)

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.5-alt1
- New version 1.2.5

* Tue Aug 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.4-alt1
- New version 1.2.4

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.3-alt1
- New version 1.2.3
- Move socket to /var/run
- Patch from upstream to fix bug in topology.c

* Fri Apr 16 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.2-alt1
- New version 1.2.2
- Add patches from debian to fix ipv6 build in io.c

* Wed Mar 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt1
- New version 1.2.1

* Sun Jan 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt1
- New version 1.2.0

* Tue Dec 29 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.7-alt1
- new release

* Tue Nov 03 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.5-alt1
- new release

* Sat Oct 17 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.4-alt1
- new release

* Mon Sep 07 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.2-alt1
- new release (29bcd04)

* Sun May 31 2009 Vladimir Lettiev <crux@altlinux.ru> 1.0.15-alt1
- new release (4c2507d)

* Wed Apr 29 2009 Vladimir Lettiev <crux@altlinux.ru> 1.0.14-alt1
- initial build

