%define _unpackaged_files_terminate_build 1

%define jss_version 4.7.0
%define tomcat_version 9.0.37

Name: tomcatjss
Version: 7.5.0
Release: alt1

Summary: JSSE module for Apache Tomcat that uses JSS
License: LGPLv2+
Group: System/Libraries
# Source-git: https://github.com/dogtagpki/tomcatjss.git
Url: http://www.dogtagpki.org/wiki/TomcatJSS

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: apache-commons-logging
BuildRequires: ant
BuildRequires: jss >= %jss_version
BuildRequires: tomcat >= %tomcat_version

BuildArch: noarch
Requires: jss >= %jss_version
Requires: tomcat >= %tomcat_version
Requires: apache-commons-logging

%description
JSS Connector for Apache Tomcat, installed via the tomcatjss package,
is a Java Secure Socket Extension (JSSE) module for Apache Tomcat that
uses Java Security Services (JSS), a Java interface to Network Security
Services (NSS).

%prep
%setup
%autopatch -p1

%build

%install
# get Tomcat <major>.<minor> version number
tomcat_version=`/usr/sbin/tomcat version | sed -n 's/Server number: *\([0-9]\+\.[0-9]\+\).*/\1/p'`
if [ $tomcat_version == "9.0" ]; then
    app_server=tomcat-8.5
else
    app_server=tomcat-$tomcat_version
fi

ant -v -f build.xml \
    -Dversion=%version \
    -Dsrc.dir=$app_server \
    -Djnidir=%_jnidir \
    -Dinstall.doc.dir=%buildroot%_docdir/%name-%version \
    -Dinstall.jar.dir=%buildroot%_javadir \
    install

%files
%doc README LICENSE
%_javadir/tomcatjss.jar
%_javadir/tomcatjss-%version.jar

%changelog
* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 7.5.0-alt1
- 7.4.1 -> 7.5.0.

* Mon Aug 26 2019 Stanislav Levin <slev@altlinux.org> 7.4.1-alt1
- 7.4.0 -> 7.4.1.

* Tue May 21 2019 Stanislav Levin <slev@altlinux.org> 7.4.0-alt1
- 7.3.6 -> 7.4.0.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 7.3.6-alt1
- 7.3.5 -> 7.3.6.

* Wed Aug 29 2018 Stanislav Levin <slev@altlinux.org> 7.3.5-alt1
- 7.3.0 -> 7.3.5.

* Thu May 24 2018 Stanislav Levin <slev@altlinux.org> 7.3.0-alt1
- 7.2.4 -> 7.3.0

* Wed Nov 08 2017 Stanislav Levin <slev@altlinux.org> 7.2.4-alt2
- Remove tomcat-native from Conflicts due to tomcat dependency on
  tomcat-native

* Fri Sep 22 2017 Stanislav Levin <slev@altlinux.org> 7.2.4-alt1
- Update to upstream's 7.2.4 version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_1jpp8
- new version

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt1_2
- new version

