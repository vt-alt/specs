Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           felix-bundlerepository
Version:        2.0.10
Release:        alt2_11jpp11
Summary:        Bundle repository service
License:        ASL 2.0 and MIT
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-osgi-bundle-repository.html
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/felix/org.apache.felix.bundlerepository-%{version}-source-release.tar.gz

Patch1:         0001-Unbundle-libraries.patch
Patch2:         0002-Compatibility-with-osgi-r6.patch

BuildRequires:  maven-local
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.shell)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires:  mvn(org.apache.felix:org.osgi.service.obr)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(xpp3:xpp3)
BuildRequires:  mvn(org.mockito:mockito-all)
Source44: import.info

%description
Bundle repository service

%package javadoc
Group: Development/Java
Summary:          API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n org.apache.felix.bundlerepository-%{version}
%patch1 -p1
%patch2 -p1

%pom_remove_plugin :maven-source-plugin

# Unbundle xpp3
%pom_add_dep "xpp3:xpp3:1.1.3.4.O" pom.xml "<optional>true</optional>"

# Inject junit and mockito dep
%pom_add_dep junit:junit::test
%pom_add_dep org.mockito:mockito-all::test

# Make felix utils mandatory dep
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='org.apache.felix.utils']]/pom:optional"

%pom_change_dep :easymock :::test

# Use latest OSGi implementation
%pom_change_dep :org.osgi.core org.osgi:osgi.core
%pom_change_dep :org.osgi.compendium org.osgi:osgi.cmpn

# For compatibility reasons
%mvn_file : felix/%{name}

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE LICENSE.kxml2 NOTICE
%doc DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE LICENSE.kxml2 NOTICE

%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 2.0.10-alt2_11jpp11
- fixed build

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.0.10-alt1_11jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_7jpp8
- update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_5jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_4jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_2jpp8
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt4_20jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt4_19jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt4_18jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1_7jpp7
- new release

