Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-java
BuildRequires: perl(Config.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(threads.pm) perl-devel rpm-build-java
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 30
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global _hardened_build 1
%global skiptests       1

Name:          zookeeper
Version:       3.4.9
Release:       alt4_13jpp8
Summary:       A high-performance coordination service for distributed applications
License:       ASL 2.0 and BSD
URL:           https://zookeeper.apache.org/
Source0:       https://www.apache.org/dist/%{name}/%{name}-%{version}.tar.gz
Source1:       %{name}-ZooInspector-template.pom
Source2:       %{name}.service
Source3:       zkEnv.sh

Patch1:        %{name}-3.4.5-zktreeutil-gcc.patch
Patch2:        %{name}-3.4.9-ivy-build.patch
Patch3:        %{name}-3.4.9-server.patch
# ZOOKEEPER-1643; patch accepted in 3.5.0
Patch4:        mt_adaptor.c.patch
Patch5:        0001-cppunit-config-no-longer-exists-use-pkg-config.patch
Patch6:        missing-pom.template.patch


BuildRequires: autoconf
BuildRequires: automake
BuildRequires: boost-complete
BuildRequires: pkgconfig(cppunit)
BuildRequires: dos2unix
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz libgraphviz
BuildRequires: java-devel
BuildRequires: java-javadoc
BuildRequires: jpackage-utils
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: python3-devel

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: apache-ivy
BuildRequires: checkstyle
BuildRequires: ivy-local
BuildRequires: javapackages-tools

BuildRequires: jtoaster
BuildRequires: junit
BuildRequires: jdiff
%if 0%{?fedora} >= 21 || 0%{?rhel} > 7
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: objectweb-pom
BuildRequires: jline1
BuildRequires: netty3
Requires:      log4j12
%else
BuildRequires: mvn(log4j:log4j)
BuildRequires: jline
BuildRequires: netty
Requires:      log4j
%endif

BuildRequires: json_simple

BuildRequires: mockito
BuildRequires: slf4j
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis

# remove later on.
BuildRequires: apache-commons-parent
BuildRequires: jetty-server
BuildRequires: jetty-servlet
BuildRequires: libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-portable systemd-services systemd-stateless systemd-sysvinit systemd-utils

Requires:      checkstyle
Requires:      jline1
Requires:      jtoaster
Requires:      junit
Requires:      mockito
Requires:      netty3
Requires:      slf4j
Requires:      java
Requires:      jpackage-utils
Requires:      %{name}-java = %{version}-%{release}
Source44: import.info

%description
ZooKeeper is a centralized service for maintaining configuration information,
naming, providing distributed synchronization, and providing group services.

##############################################
%package devel
Group: Development/Java
Summary:       Development files for the %{name} library
Requires:      %{name} = %{version}-%{release}

%description devel
Development files for the ZooKeeper C client library.

##############################################
%package java
Group: Development/Other
Summary:        Java interface for %{name}
Requires:       %{name} = %{version}-%{release}

%description java
The %{name}-java package contains Java bindings for %{name}.

##############################################
%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%package -n python3-module-zookeeper
Group: Development/Java
%{?python_provide:%python_provide python3-%{name}}
Summary:       Python support for %{name}
Requires:      %{name} = %{version}-%{release}

%description -n python3-module-zookeeper
Python bindings for %{name}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# Do not treat C compile-time warnings as errors
sed -i -e's/-Werror//' src/c/Makefile.am

iconv -f iso8859-1 -t utf-8 src/c/ChangeLog > src/c/ChangeLog.conv && mv -f src/c/ChangeLog.conv src/c/ChangeLog
sed -i 's/\r//' src/c/ChangeLog

sed -i 's|<exec executable="hostname" outputproperty="host.name"/>|<!--exec executable="hostname" outputproperty="host.name"/-->|' build.xml
sed -i 's|<attribute name="Built-On" value="${host.name}" />|<attribute name="Built-On" value="${user.name}" />|' build.xml

sed -i 's@^dataDir=.*$@dataDir=%{_sharedstatedir}/zookeeper/data\ndataLogDir=%{_sharedstatedir}/zookeeper/log@' conf/zoo_sample.cfg

%build
%ant -Divy.mode=local \
-DCLASSPATH=/usr/share/java/log4j12-1.2.17.jar \
-Dtarget.jdk=1.5 \
-Djavadoc.link.java=%{_javadocdir}/java \
-Dant.build.javac.source=1.5 \
-Dant.build.javac.target=1.5 \
package

# cppunit-config patch touches configure.ac in these dirs
pushd src/recipes/lock/src/c
autoreconf -if
popd
pushd src/recipes/queue/src/c
autoreconf -if
popd

pushd src/c
autoreconf -if
%configure --disable-static --disable-rpath
make %{?_smp_mflags}
popd

## TODO: install utilities?

%check
%if %skiptests
  echo "Testing disabled, please enable in mock"
%else
  %ant -Divy.mode=local test
%endif

%install

# the following is used to update zkEnv.sh
# find . -name "*.jar" -exec basename {} \; |sort|uniq
# remove items that don't belong and update execute build-classpath

#install the c tools
pushd src/c
%makeinstall_std
popd

# install the java dependencies.
mkdir -p %{buildroot}%{_javadir}/%{name}
install -pm 644 build/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -pm 644 build/%{name}-%{version}-test.jar %{buildroot}%{_javadir}/%{name}/%{name}-tests.jar
install -pm 644 build/contrib/ZooInspector/%{name}-%{version}-ZooInspector.jar %{buildroot}%{_javadir}/%{name}/%{name}-ZooInspector.jar

install -pm 755 bin/zkCleanup.sh %{buildroot}%{_bindir}
install -pm 755 bin/zkCli.sh %{buildroot}%{_bindir}
install -pm 755 bin/zkServer.sh %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}
install -pm 755 %{SOURCE3} %{buildroot}%{_libexecdir}

%if 0%{?fedora} >= 21 || 0%{?rhel} > 7
mkdir -p %{buildroot}%{_datadir}/maven-metadata
mkdir -p %{buildroot}%{_datadir}/maven-poms
install -pm 644 build/%{name}-%{version}/dist-maven/%{name}-%{version}.pom %{buildroot}%{_datadir}/maven-poms/%{name}-%{name}.pom

%add_maven_depmap %{name}-%{name}.pom %{name}/%{name}.jar
%add_maven_depmap org.apache.zookeeper:zookeeper::tests:%{version} %{name}/%{name}-tests.jar

install -pm 644 %{SOURCE1} %{buildroot}%{_datadir}/maven-poms/%{name}-%{name}-ZooInspector.pom
sed -i "s|@version@|%{version}|" %{buildroot}%{_datadir}/maven-poms/%{name}-%{name}-ZooInspector.pom
%add_maven_depmap %{name}-%{name}-ZooInspector.pom %{name}/%{name}-ZooInspector.jar
%else
mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 build/%{name}-%{version}/dist-maven/%{name}-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom

%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar
%add_maven_depmap org.apache.zookeeper:zookeeper::tests:%{version} %{name}/%{name}-tests.jar

install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-ZooInspector.pom
sed -i "s|@version@|%{version}|" %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-ZooInspector.pom
%add_maven_depmap JPP.%{name}-%{name}-ZooInspector.pom %{name}/%{name}-ZooInspector.jar
%endif

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/docs/api/* %{buildroot}%{_javadocdir}/%{name}/

pushd src/contrib/zkpython
%{__python3} src/python/setup.py build --build-base=$PWD/build \
install --root=%{buildroot} ;\
chmod 0755 %{buildroot}%{python3_sitelibdir}/zookeeper.cpython-*.so
popd

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/zookeeper
mkdir -p %{buildroot}%{_localstatedir}/log/zookeeper
mkdir -p %{buildroot}%{_sharedstatedir}/zookeeper
mkdir -p %{buildroot}%{_sharedstatedir}/zookeeper/data
mkdir -p %{buildroot}%{_sharedstatedir}/zookeeper/log
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
install -p -m 0640 conf/log4j.properties %{buildroot}%{_sysconfdir}/zookeeper
install -p -m 0640 conf/zoo_sample.cfg %{buildroot}%{_sysconfdir}/zookeeper
touch %{buildroot}%{_sysconfdir}/zookeeper/zoo.cfg
touch %{buildroot}%{_sharedstatedir}/zookeeper/data/myid

# touching all ghosts; hack for rpm 4.0.4
for rpm404_ghost in %{_sysconfdir}/zookeeper/zoo.cfg %{_sharedstatedir}/zookeeper/data/myid
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done


%pre
getent group zookeeper >/dev/null || groupadd -r zookeeper
getent passwd zookeeper >/dev/null || \
    useradd -r -g zookeeper -d %{_sharedstatedir}/zookeeper -s /sbin/nologin \
    -c "ZooKeeper service account" zookeeper

%post
%post_service zookeeper
: 

%preun
%preun_service zookeeper

%files
%{_bindir}/cli_mt
%{_bindir}/cli_st
%{_bindir}/load_gen
%{_bindir}/zk*.sh
%{_libexecdir}/zkEnv.sh
%{_libdir}/lib*.so.*

%attr(0755,root,root) %dir %{_sysconfdir}/zookeeper
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/zookeeper/zoo.cfg
%attr(0644,root,root) %{_sysconfdir}/zookeeper/zoo_sample.cfg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/zookeeper/log4j.properties

%attr(0755,zookeeper,zookeeper) %dir %{_localstatedir}/log/zookeeper
%attr(0755,root,root) %dir %{_sharedstatedir}/zookeeper
%attr(0750,zookeeper,zookeeper) %dir %{_sharedstatedir}/zookeeper/data
%attr(0640,zookeeper,zookeeper) %ghost %{_sharedstatedir}/zookeeper/data/myid
%attr(0755,zookeeper,zookeeper) %dir %{_sharedstatedir}/zookeeper/log
%{_unitdir}/zookeeper.service
%doc CHANGES.txt LICENSE.txt NOTICE.txt README.txt

%files java
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}.jar
%{_javadir}/%{name}/%{name}-tests.jar
%{_javadir}/%{name}/%{name}-ZooInspector.jar
%if 0%{?fedora} >= 21 || 0%{?rhel} > 7
%{_datadir}/maven-poms/%{name}-%{name}.pom
%{_datadir}/maven-poms/%{name}-%{name}-ZooInspector.pom
%{_datadir}/maven-metadata/%{name}.xml
%else
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-ZooInspector.pom
%endif
%doc CHANGES.txt LICENSE.txt NOTICE.txt README.txt

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%doc src/c/LICENSE src/c/NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files -n python3-module-zookeeper
%{python3_sitelibdir}/ZooKeeper-?.?-py%{__python3_version}.egg-info
%{python3_sitelibdir}/zookeeper.cpython-*.so
%doc LICENSE.txt NOTICE.txt src/contrib/zkpython/README

%changelog
* Thu Jun 27 2019 Igor Vlasenko <viy@altlinux.ru> 3.4.9-alt4_13jpp8
- use libexec as libexecdir for bash scripts to work

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.4.9-alt3_13jpp8
- new version

* Wed Jan 09 2019 Igor Vlasenko <viy@altlinux.ru> 3.4.9-alt2_12
- fixed build

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 3.4.9-alt2_7
- use boost-complete

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.9-alt1_7jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.4.9-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.4.6-alt1_16jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.4.6-alt1_15jpp8
- new version

