Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global githash cb6709646eed97c271d73f50ad750cc43c8e052a
Name:             paranamer
Version:          2.8
Release:          alt1_15jpp11
Summary:          Java library for accessing non-private method's parameter names at run-time
License:          BSD
URL:              https://github.com/paul-hammant/paranamer
Source0:          %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz

Patch0:           0001-Port-to-current-qdox.patch

BuildRequires:    maven-local
BuildRequires:    mvn(com.thoughtworks.qdox:qdox)
BuildRequires:    mvn(javax.inject:javax.inject)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.ant:ant)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.apache.maven:maven-plugin-api)
BuildRequires:    mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:    mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:    mvn(org.mockito:mockito-all)
BuildRequires:    mvn(org.ow2.asm:asm)

BuildArch:        noarch
Source44: import.info

%description
Paranamer is a Java library that allows the parameter names of non-private
methods and constructors to be accessed at run-time. Most compilers discard
this information; traditional Reflection on JDK <= 7 would show something like
doSomething(mypackage.Person ???) instead of doSomething(mypackage.Person toMe).
The Paranamer library fills this gap for these JDK versions.

%package ant
Group: Development/Java
Summary:          ParaNamer Ant

%description ant
This package contains the ParaNamer Ant tasks.

%package generator
Group: Development/Java
Summary:          ParaNamer Generator

%description generator
This package contains the ParaNamer Generator.

%package integration-tests
Group: Development/Java
Summary:          ParaNamer Integration Test Parent POM

%description integration-tests
ParaNamer Integration Test Parent POM.

%package it-011
Group: Development/Java
Summary:          ParaNamer Integration Test 011

%description it-011
ParaNamer IT 011: can use maven plugin defaults.

%package maven-plugin
Group: Development/Java
Summary:          ParaNamer Maven plugin

%description maven-plugin
This package contains the ParaNamer Maven plugin.

%package parent
Group: Development/Java
Summary:          ParaNamer Parent POM

%description parent
This package contains the ParaNamer Parent POM.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{githash}

%patch0 -p1

# Cleanup
find -name "*.class" -print -delete
# Do not erase test resources
find -name "*.jar" -print ! -name "test.jar" -delete

chmod -x LICENSE.txt

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

# Disable distribution module
%pom_disable_module %{name}-distribution

# Unavailable test deps
%pom_remove_dep -r net.sourceforge.f2j:
%pom_xpath_remove -r "pom:dependency[pom:classifier = 'javadoc' ]"

# package org.netlib.blas does not exist
rm -r %{name}/src/test/com/thoughtworks/paranamer/JavadocParanamerTest.java

# testRetrievesParameterNamesFromBootstrapClassLoader java.lang.AssertionError:
#       Should not find names for classes loaded by the bootstrap class loader.
rm -r %{name}/src/test/com/thoughtworks/paranamer/BytecodeReadingParanamerTestCase.java

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%mvn_build -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%doc --no-dereference LICENSE.txt

%files ant -f .mfiles-%{name}-ant

%files generator -f .mfiles-%{name}-generator
%doc --no-dereference LICENSE.txt

%files integration-tests -f .mfiles-%{name}-integration-tests
%doc --no-dereference LICENSE.txt

%files it-011 -f .mfiles-%{name}-it-011
%doc --no-dereference LICENSE.txt

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files parent -f .mfiles-%{name}-parent
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.8-alt1_15jpp11
- update

* Wed Oct 14 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_12jpp8
- fc update for new xbean

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_9jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_8jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_5jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_3jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_2jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8-alt1_1jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_6jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt2_5jpp7
- fixed build

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt1_5jpp7
- converted from JPackage by jppimport script

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_1jpp6
- use jmock1 (TODO: try jmock2)

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_1jpp6
- fixed build

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_1jpp6
- fixed build (added BR: sun-annotation-1.0-api)

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp6
- new version

