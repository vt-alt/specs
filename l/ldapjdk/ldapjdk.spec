%define _unpackaged_files_terminate_build 1

%define _localstatedir  %_var
%define spname		ldapsp
%define filtname	ldapfilt
%define beansname	ldapbeans
%define jss_version     4.6.0

Name: ldapjdk
Epoch: 1
Version: 4.22.0
Release: alt1

Summary: LDAP SDK
License: MPL-1.1 or GPLv2+ or LGPLv2+
Group: Development/Java
# Source-git: https://github.com/dogtagpki/ldap-sdk.git
Url: https://www.dogtagpki.org/wiki/LDAP_SDK

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java

BuildRequires: /proc
BuildRequires: ant
# at least dogtag pki requires java 8 at build/runtime
# pin the Java so far
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: javapackages-local
BuildRequires: javapackages-tools
BuildRequires: jss >= %jss_version

BuildArch: noarch

Provides: ldapsdk = 1:%version-%release
Obsoletes: ldapsdk <= 1:4.18-alt1_2jpp6

Requires: jss >= %jss_version

%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

################################################################################
%package javadoc
Group: Development/Documentation
################################################################################

Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
Javadoc for %name

################################################################################
%prep
################################################################################

%setup
%patch -p1

# Remove all bundled jars, we must build against build-system jars
rm ./java-sdk/ldapjdk/lib/*

################################################################################
%build
################################################################################

pushd ./java-sdk/ldapjdk/lib
build-jar-repository -s -p . jss4

ln -s /usr/lib/jvm-exports/java/{jsse,jaas,jndi}.jar ./
pushd ../../
%ant -v dist

################################################################################
%install
################################################################################

install -d -m 755 %buildroot%_javadir
install -m 644 java-sdk/dist/packages/%name.jar %buildroot%_javadir/%name.jar
install -m 644 java-sdk/dist/packages/%spname.jar %buildroot%_javadir/%spname.jar
install -m 644 java-sdk/dist/packages/%filtname.jar %buildroot%_javadir/%filtname.jar
install -m 644 java-sdk/dist/packages/%beansname.jar %buildroot%_javadir/%beansname.jar

install -d -m 755 %buildroot%_javadir-1.3.0

pushd %buildroot%_javadir-1.3.0
	ln -fs ../java/*%spname.jar jndi-ldap.jar
popd

mkdir -p %buildroot%_mavenpomdir
sed -i 's/@VERSION@/%{version}/g' %name.pom
install -pm 644 %name.pom %buildroot%_mavenpomdir/JPP-%name.pom
%add_maven_depmap JPP-%name.pom %name.jar -a "ldapsdk:ldapsdk"

install -d -m 755 %buildroot%_javadocdir/%name
cp -r java-sdk/dist/doc/* %buildroot%_javadocdir/%name
ln -s ldapjdk.jar %buildroot%_javadir/ldapsdk.jar

################################################################################
%files -f .mfiles
################################################################################

%_javadir/%{spname}*.jar
%_javadir/%{filtname}*.jar
%_javadir/%{beansname}*.jar
%_javadir-1.3.0/*.jar
%_javadir/ldapsdk.jar

################################################################################
%files javadoc
################################################################################

%dir %_javadocdir/%name
%_javadocdir/%name/*

################################################################################
%changelog
* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 1:4.22.0-alt1
- 4.21.0 -> 4.22.0.

* Mon Aug 26 2019 Stanislav Levin <slev@altlinux.org> 1:4.21.0-alt1
- 4.20.0 -> 4.21.0.

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.20.0-alt1_2jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.19-alt2_7jpp8
- java fc28+ update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.19-alt2_5jpp8
- new fc release

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.19-alt2_1jpp8
- added BR: javapackages-local for javapackages 5

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.19-alt1_1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_19jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_18jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_17jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_13jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_12jpp7
- fc update

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_11jpp7
- fc release

* Tue Mar 30 2010 Igor Vlasenko <viy@altlinux.ru> 1:4.18-alt1_2jpp6
- new version

* Mon Sep 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:4.17-alt1_3jpp5
- fixed build with java5

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 1:4.17-alt1_3jpp1.7
- converted from JPackage by jppimport script

