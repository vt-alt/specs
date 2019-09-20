%def_enable check

Name: pve-common
Summary: PVE base library
Version: 6.0.4
Release: alt2
License: GPLv3
Group: Development/Perl
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-ph
BuildRequires: perl(IO/Socket/IP.pm)
BuildRequires: perl(Filesys/Df.pm)
BuildRequires: perl(URI/Escape.pm)
BuildRequires: perl(Digest/SHA.pm)
BuildRequires: perl(String/ShellQuote.pm)
BuildRequires: perl(IO/AtomicFile.pm)
BuildRequires: perl(HTTP/Status.pm)
BuildRequires: perl(Devel/Cycle.pm)
BuildRequires: perl(Net/IP.pm)
BuildRequires: perl(Net/DBus.pm)
BuildRequires: perl(Pod/Parser.pm)
BuildRequires: perl(Clone.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(Linux/Inotify2.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(MIME/Base32.pm)
BuildRequires: perl(Crypt/OpenSSL/Random.pm)
BuildRequires: perl(Crypt/OpenSSL/RSA.pm)
BuildRequires: perl(Date/Parse.pm)
BuildRequires: perl(Net/SSLeay.pm)
BuildRequires: perl(HTTP/Daemon.pm)
BuildRequires: perl(CPAN/Meta/YAML.pm)
# alt regressive tests
BuildRequires: perl(TAP/Harness.pm)

%description
This package contains the base library used by other PVE components.

%prep
%setup -q -n %name-%version
sed -i 's|Proxmox VE|PVE|' src/PVE/Tools.pm

%install
cd src
%make DESTDIR=%buildroot install
cd ..
install -pD -m0755 pve-etcnet-to-network %buildroot%_sbindir/pve-etcnet-to-network

%if_enabled check
%check
# upstream tests
make -C test check
# etcnet tests
./runtests.pl
%endif

%files
%_sbindir/pve-etcnet-to-network
%perl_vendor_privlib/PVE

%changelog
* Thu Sep 19 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.4-alt2
- removed read_etc_timezone/write_etc_timezone

* Mon Aug 26 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.4-alt1
- 6.0-4

* Tue Jul 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 6.0.3-alt1
- 6.0-3

* Mon May 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.52-alt1
- 5.0-52

* Thu Feb 21 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.47-alt1
- 5.0-47

* Wed Jan 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.0.44-alt1
- 5.0-44

* Mon Nov 26 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.43-alt1
- 5.0-43

* Thu Nov 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.41-alt1
- 5.0-41

* Wed Jul 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 5.0.31-alt1
- 5.0-31

* Tue Dec 12 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.23-alt1
- 5.0-23

* Mon Oct 23 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.20-alt1
- 5.0-20

* Tue Oct 10 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.19-alt1
- 5.0-19

* Fri Sep 29 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.16-alt4
- brivlanport support

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.16-alt3
- bridge vids options support

* Mon Sep 25 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.16-alt0.M80C.2
- backport to c8 branch

* Fri Aug 04 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.16-alt2
- fixed check OVSPort

* Thu Jul 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 5.0.16-alt1
- 5.0-16

* Wed Jun 21 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.83-alt3
- PVE::Tools::run_command: fixed exit code

* Wed Mar 15 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.83-alt2
- ovs fixes for ovsport

* Mon Nov 28 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.83-alt1
- 4.0-83

* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.81-alt1
- 4.0-81

* Fri Oct 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.76-alt1
- 4.0-76

* Thu Oct 13 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt10
- vlan fixes

* Wed Oct 12 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt9
- skip ovpn interfaces

* Wed Oct 12 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt8
- bugfixes in vlan support

* Mon Oct 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt7
- OVS_OPTIONS uniquify

* Fri Oct 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt6
- OVS bugfixes

* Thu Oct 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt5
- BONDOPTIONS bugfixes

* Thu Oct 06 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt4
- added regression tests

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt3
- OVS fixes for ovsbond

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.74-alt2
- OVS bugfixes

* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.74-alt1
- 4.0-74

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.73-alt1
- 4.0-73

* Mon Sep 05 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.72-alt2
- Network Device: replace rate limit MB/s to MBit/s

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.72-alt1
- 4.0-72

* Fri Jul 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.71-alt1
- 4.0-71

* Thu Jul 14 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.70-alt3
- OVS bugfixes

* Sat Jul 09 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.70-alt2
- OVS fixes

* Wed Jul 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.70-alt1
- 4.0-70

* Mon Jul 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.68-alt2
- OVS support

* Tue Jun 14 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.68-alt1
- 4.0-68

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.67-alt1
- 4.0-67

* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.65-alt1
- 4.0-65

* Fri May 20 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.63-alt1
- 4.0-63

* Wed May 18 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.63-alt0.2.etcnet_reader_test2
- 2nd test release of etcnet_reader

* Sat May 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.59-alt0.2.etcnet_reader_test1
- 1st test release of etcnet_reader

* Sat May 07 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.59-alt0.1.etcnet_writer_test3
- stable release of etcnet_writer_test

* Wed May 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.59-alt0.1.etcnet_writer_test2
- 2nd test release of etcnet_writer_test

* Thu Apr 28 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.59-alt0.1.etcnet_writer_test1
- test release of etcnet_writer_test

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.46-alt1
- 4.0-46

* Mon Dec 14 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.41-alt1
- initial release

