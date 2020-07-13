%set_verify_elf_method textrel=relaxed

%define jicofo_user _jicofo

Name:           jicofo
Version:        1.1
Release:        alt0.3

Summary:        JItsi Meet COnference FOcus
#Group:          Networking/Instant messaging
Group:          System/Servers
License:        Apache-2.0
URL:            http://www.jitsi.org
# VCS:          https://github.com/jitsi/jicofo.git

#ExclusiveArch:  %ix86 x86_64
ExclusiveArch:  x86_64
#BuildArch: noarch

Source0:        %name-%version.tar
Source1:        m2-%name-%version.tar
#Source2:        %name.sh

AutoReqProv: yes,noosgi

BuildRequires(pre): rpm-build-java
BuildRequires:  java-devel-default
BuildRequires:  maven
BuildRequires:  unzip

Requires:	java

%description
Jicofo is a conference focus agent for Jitsi Meet.

%prep
tar -x -C ~ -f %SOURCE1
%setup

%build
mvn install -Dassembly.skipAssembly=false
mvn -DskipTests -Dassembly.skipAssembly=true package
mvn dependency:copy-dependencies -DincludeScope=runtime

%install
mkdir -p %buildroot%_datadir/jicofo/lib/ %buildroot%_sysconfdir/jitsi/jicofo/ %buildroot%_sysconfdir/logrotate.d/
install -m644 target/dependency/*             %buildroot%_datadir/jicofo/lib/
install -m644 lib/logging.properties          %buildroot%_sysconfdir/jitsi/jicofo/
install -m644 target/jicofo-%version-SNAPSHOT.jar  %buildroot%_datadir/jicofo/jicofo.jar
install -m755 resources/jicofo.sh             %buildroot%_datadir/jicofo/
install -m644 resources/collect-dump-logs.sh  %buildroot%_datadir/jicofo/
install -m644 resources/config/jicofo-logrotate.d %buildroot%_sysconfdir/logrotate.d/jicofo
mkdir -p %buildroot%_bindir/ %buildroot%_unitdir/
install -m755 resources/alt-jicofo-launcher.sh %buildroot%_bindir/jicofo
install -m644 resources/alt-jicofo.service %buildroot%_unitdir/%name.service

%files
%dir %_datadir/jicofo
%_datadir/jicofo/lib
%_datadir/jicofo/jicofo.jar
%_datadir/jicofo/jicofo.sh
%_bindir/jicofo
%_datadir/jicofo/collect-dump-logs.sh
%dir %attr(700, %jicofo_user, -) %_sysconfdir/jitsi/jicofo
%config %_sysconfdir/jitsi/jicofo/logging.properties
%config %_sysconfdir/logrotate.d/jicofo
%_unitdir/%name.service

%pre
%_sbindir/useradd -r -d /dev/null -s /dev/null -n %jicofo_user \
        2> /dev/null > /dev/null ||:

%changelog
* Wed Jun 10 2020 Arseny Maslennikov <arseny@altlinux.org> 1.1-alt0.3
- Added launcher executable.
- Added a systemd service unit.

* Thu May 28 2020 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.2
- initial build

