Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with     equinox
%bcond_with     groovy

Name:           xbean
Summary:        Java plugin based web server
Version:        4.15
Release:        alt2_7jpp11
License:        ASL 2.0

URL:            http://geronimo.apache.org/xbean/
Source0:        http://repo2.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Compatibility with Eclipse Luna (rhbz#1087461)
Patch1:         0002-Port-to-Eclipse-Luna-OSGi.patch
Patch2:         0003-Port-to-QDox-2.0.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-1.2-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.slf4j:slf4j-api)

%if %{with equinox}
BuildRequires:  mvn(org.eclipse:osgi)
%endif

%if %{with groovy}
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
%endif
Source44: import.info

%description
The goal of XBean project is to create a plugin based server
analogous to Eclipse being a plugin based IDE. XBean will be able to
discover, download and install server plugins from an Internet based
repository. In addition, we include support for multiple IoC systems,
support for running with no IoC system, JMX without JMX code,
lifecycle and class loader management, and a rock solid Spring
integration.


%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.


%prep
%setup -q
# build failing on this due to doxia-sitetools problems
rm src/site/site.xml

%if %{with equinox}
%patch1 -p1
%endif
%patch2 -p1

%pom_remove_parent
%pom_remove_dep mx4j:mx4j

# use osgi-core instead of felix-osgi-core
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core

# switch from log4j 1.2 compat package to log4j 1.2 API shim
%pom_change_dep -r log4j:log4j org.apache.logging.log4j:log4j-1.2-api

# Unshade ASM
%pom_remove_dep -r :xbean-asm7-shaded
%pom_remove_dep -r :xbean-finder-shaded
%pom_disable_module xbean-asm7-shaded
%pom_disable_module xbean-finder-shaded
%pom_add_dep org.apache.xbean:xbean-asm-util:%{version} xbean-reflect
%pom_xpath_remove pom:optional xbean-reflect xbean-asm-util
%pom_xpath_remove 'pom:scope[text()="provided"]' xbean-reflect xbean-asm-util
sed -i 's/org\.apache\.xbean\.asm7/org.objectweb.asm/g' `find xbean-reflect -name '*.java'`

# Springframework is not available in Fedora
%pom_remove_dep org.springframework:
%pom_disable_module xbean-blueprint
%pom_disable_module xbean-classloader
%pom_disable_module xbean-spring
%pom_disable_module maven-xbean-plugin

# Disable uneeded modules that cannot be built on JDK 11
%pom_disable_module xbean-classpath

# Disable one test that fails on JDK 11
sed -i '/testGetBytecode/i@org.junit.Ignore' xbean-finder/src/test/java/org/apache/xbean/finder/archive/MJarJarArchiveTest.java

# Unused import which is not available in OpenJDK 11
# Forwarded upstream: https://issues.apache.org/jira/browse/XBEAN-329
sed -i '/import com.sun.org.apache.regexp.internal.RE/d' xbean-reflect/src/main/java/org/apache/xbean/propertyeditor/PropertyEditors.java

%if %{without equinox}
  %pom_remove_dep :xbean-bundleutils xbean-finder
  rm -r xbean-finder/src/main/java/org/apache/xbean/finder{,/archive}/Bundle*
  %pom_disable_module xbean-bundleutils
%endif

%if %{without groovy}
%pom_disable_module xbean-telnet
%endif

# maven-xbean-plugin invocation makes no sense as there are no namespaces
%pom_remove_plugin :maven-xbean-plugin xbean-classloader

# Remove plugins useful for upstream only.
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE


%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:4.15-alt2_7jpp11
- fc34 update

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:4.15-alt2_5jpp11
- fixed build

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 0:4.15-alt1_5jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:4.14-alt1_1jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:4.9-alt1_2jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:4.8-alt1_1jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_3jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_1jpp8
- unbootsrap build

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_4jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_1jpp7
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.12-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt4_3jpp7
- fixed build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt3_3jpp7
- restored rcp dep

* Sun Mar 31 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt2_3jpp7
- bootstrapping eclipse - dropped eclipse-rcp dep

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt1_3jpp7
- new version

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt1_2jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt3_7jpp7
- fixed build

* Tue May 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt2_7jpp7
- added maven-xbean-plugin

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt1_7jpp7
- new version

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.4.3-alt1_2jpp6
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_1jpp5
- first build

