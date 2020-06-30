%define GRADLE_TASKS installdist
%define GRADLE_FLAGS --offline --gradle-user-home /tmp --no-daemon --exclude-task generateJava
%define LS_PREFIX %_datadir/linstor-server
%define FIREWALLD_SERVICES %_usr/lib/firewalld/services
%define NAME_VERS %name-server-%version

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %nil

Name: linstor
Version: 1.7.1
Release: alt1
Summary: LINSTOR SDS
Group: System/Servers
License: GPLv2+
Url: https://github.com/LINBIT/linstor-server
Source0: http://www.linbit.com/downloads/linstor/linstor-server-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): /proc rpm-build-java jpackage-utils
# BuildRequires: java-1.8.0-openjdk-headless java-1.8.0-openjdk-devel
BuildRequires: java-devel-default
BuildRequires: python3
BuildRequires: gradle

%description
LINSTOR developed by LINBIT, is a software that manages replicated volumes across a group of machines.
With native integration to Kubernetes, LINSTOR makes building, running, and controlling block storage simple.
LINSTOR is open-source software designed to manage block storage devices for large Linux server clusters.
It's used to provide persistent Linux block storage for cloudnative and hypervisor environments.

%prep
%setup -n %NAME_VERS

%build
rm -rf ./build/install
gradle %GRADLE_TASKS %GRADLE_FLAGS
for p in server satellite controller; do echo "%LS_PREFIX/.$p" >> "%_builddir/%NAME_VERS/$p/jar.deps"; done

%install
mkdir -p %buildroot%LS_PREFIX
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/lib %buildroot%LS_PREFIX
rm %buildroot/%LS_PREFIX/lib/%NAME_VERS.jar
cp -r %_builddir/%NAME_VERS/server/build/install/server/lib/conf %buildroot%LS_PREFIX/lib
mkdir -p %buildroot%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/bin/Controller %buildroot%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/bin/Satellite %buildroot%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/build/install/linstor-server/bin/linstor-config %buildroot%LS_PREFIX/bin
cp -r %_builddir/%NAME_VERS/scripts/postinstall.sh %buildroot%LS_PREFIX/bin/controller.postinst.sh
mkdir -p %buildroot%_unitdir
cp -r %_builddir/%NAME_VERS/scripts/linstor-controller.service %buildroot%_unitdir
cp -r %_builddir/%NAME_VERS/scripts/linstor-satellite.service %buildroot%_unitdir
mkdir -p %buildroot%FIREWALLD_SERVICES
cp %_builddir/%NAME_VERS/scripts/firewalld/drbd.xml %buildroot%FIREWALLD_SERVICES
cp %_builddir/%NAME_VERS/scripts/firewalld/linstor-controller.xml %buildroot%FIREWALLD_SERVICES
cp %_builddir/%NAME_VERS/scripts/firewalld/linstor-satellite.xml %buildroot%FIREWALLD_SERVICES
mkdir -p %buildroot%_sysconfdir/drbd.d/
cp %_builddir/%NAME_VERS/scripts/linstor-resources.res %buildroot%_sysconfdir/drbd.d/
touch %buildroot%LS_PREFIX/{.server,.satellite,.controller}
mkdir -p %buildroot%_sysconfdir/linstor
cp %_builddir/%NAME_VERS/docs/linstor.toml-example %buildroot%_sysconfdir/linstor/

### common
%package common
Summary: Common files shared between controller and satellite
Group: System/Servers
Requires: jre-headless

%description common
Linstor shared components between linstor-controller and linstor-satellite

%files common -f server/jar.deps
%dir %LS_PREFIX
%dir %LS_PREFIX/lib
%LS_PREFIX/lib/server-%version.jar
%dir %LS_PREFIX/lib/conf
%LS_PREFIX/lib/conf/logback.xml

### controller
%package controller
Summary: Linstor controller specific files
Group: System/Servers
Requires: linstor-common = %version

%description controller
Linstor controller manages linstor satellites and persistant data storage.

%files controller -f controller/jar.deps
%dir %LS_PREFIX
%dir %LS_PREFIX/lib
%LS_PREFIX/lib/controller-%version.jar
%dir %LS_PREFIX/bin
%LS_PREFIX/bin/Controller
%LS_PREFIX/bin/linstor-config
%LS_PREFIX/bin/controller.postinst.sh
%_unitdir/linstor-controller.service
%FIREWALLD_SERVICES/linstor-controller.xml
%_sysconfdir/linstor/linstor.toml-example


%post controller
%LS_PREFIX/bin/controller.postinst.sh
%post_service linstor-controller
#test -f %_bindir/firewall-cmd && firewall-cmd --reload --quiet || :

%preun controller
%preun_service linstor-controller

### satellite
%package satellite
Summary: Linstor satellite specific files
Group: System/Servers
Requires: linstor-common = %version
Requires: lvm2 thin-provisioning-tools
Requires: drbd-utils >= 9.7.0

%description satellite
Linstor satellite, communicates with linstor-controller
and creates drbd resource files.

%files satellite -f satellite/jar.deps
%dir %LS_PREFIX
%dir %LS_PREFIX/lib
%LS_PREFIX/lib/satellite-%version.jar
%dir %LS_PREFIX/bin
%LS_PREFIX/bin/Satellite
%_unitdir/linstor-satellite.service
%FIREWALLD_SERVICES/linstor-satellite.xml
%FIREWALLD_SERVICES/drbd.xml
%config(noreplace) %_sysconfdir/drbd.d/linstor-resources.res

%post satellite
%post_service linstor-satellite
#test -f %_bindir/firewall-cmd && firewall-cmd --reload --quiet || :

%preun satellite
%preun_service linstor-satellite

%changelog
* Tue Jun 23 2020 Alexey Shabalin <shaba@altlinux.org> 1.7.1-alt1
- 1.7.1

* Thu Mar 05 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.3-alt1
- Initial build
