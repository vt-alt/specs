Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname build-helper-maven-plugin

Name:           maven-plugin-build-helper
Version:        3.2.0
Release:        alt1_2jpp11
Summary:        Build Helper Maven Plugin
License:        MIT

URL:            https://www.mojohaus.org/build-helper-maven-plugin/
Source0:        https://github.com/mojohaus/%{srcname}/archive/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache-extras.beanshell:bsh)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

Provides: mojo-maven2-plugin-build-helper = %version
Obsoletes: mojo-maven2-plugin-build-helper = 17


%description
This plugin contains various small independent goals to assist with
Maven build lifecycle.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{srcname}-%{srcname}-%{version}

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_2jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_11jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_9jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt3_8jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt3_6jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_6jpp7
- added jpp compatible provides

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_5jpp7
- fc version

