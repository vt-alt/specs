Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-archiver
Version:        3.5.1
Release:        alt1_1jpp11
Epoch:          0
Summary:        Maven Archiver
License:        ASL 2.0

URL:            https://maven.apache.org/shared/maven-archiver/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver) >= 4.2.0
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation) >= 1.25
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils) >= 3.3.0
Source44: import.info

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.5.1-alt1_1jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 0:3.5.0-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.4.0-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_4jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_3jpp8
- fc27 update

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_2jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_8jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_3jpp7
- rebuild with maven-local

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_3jpp7
- new fc release

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

