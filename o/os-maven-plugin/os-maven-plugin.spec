Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           os-maven-plugin
Version:        1.6.2
Release:        alt1_3jpp11
Summary:        Maven plugin for generating platform-dependent properties
License:        ASL 2.0
URL:            https://github.com/trustin/os-maven-plugin/
BuildArch:      noarch

Source0:        https://github.com/trustin/%{name}/archive/%{name}-%{version}.tar.gz

Patch0:         0001-Don-t-fail-on-unknown-arch.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
os-maven-plugin is a Maven extension/plugin that generates various
useful platform-dependent project properties normalized from
${os.name} and ${os.arch}.

${os.name} and ${os.arch} are often subtly different between JVM and
operating system versions or they sometimes contain machine-unfriendly
characters such as whitespaces. This plugin tries to remove such
fragmentation so that you can determine the current operating system
and architecture reliably.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch0 -p1

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove Eclipse plugin (not needed in Fedora)
%pom_remove_dep org.eclipse:ui
%pom_remove_plugin :maven-jar-plugin
find -name EclipseStartup.java -delete
find -name plugin.xml -delete

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.6.2-alt1_3jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.2.3-alt1_14jpp11
- update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_11jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_6jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_5jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.3-alt1_4jpp8
- new version

