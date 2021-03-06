Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
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
# ant scripting is unused in fedora 33+
%bcond_with ant

# bsh support is unused in fedora 33+
%bcond_with beanshell

Name:           maven-plugin-tools
Version:        3.6.0
Release:        alt1_7jpp11
Epoch:          0
Summary:        Maven Plugin Tools
License:        ASL 2.0
URL:            http://maven.apache.org/plugin-tools/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugin-tools/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0000-ignore-jtidy-crashes.patch
Patch1:         0001-Port-to-plexus-utils-3.0.24.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(net.sf.jtidy:jtidy)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.surefire:maven-surefire-common)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-repository-metadata)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)

%if %{with ant}
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.codehaus.plexus:plexus-ant-factory)
%endif

%if %{with beanshell}
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.codehaus.plexus:plexus-bsh-factory)
%endif

# removed in fedora 33 with 3.6.0
Obsoletes:      maven-plugin-tools-javadoc < 0:3.6.0-1

%if %{without ant}
Obsoletes:      maven-plugin-tools-ant < %{epoch}:%{version}-%{release}
Obsoletes:      maven-script-ant < %{epoch}:%{version}-%{release}
%endif

%if %{without beanshell}
Obsoletes:      maven-plugin-tools-beanshell < %{epoch}:%{version}-%{release}
Obsoletes:      maven-script-beanshell < %{epoch}:%{version}-%{release}
%endif
Source44: import.info

%description
The Maven Plugin Tools contains the necessary tools to be able to produce Maven
Plugins in a variety of languages.

%package -n maven-plugin-annotations
Group: Development/Java
Summary:        Maven Plugin Java 5 Annotations
#Obsoletes:      maven-plugin-annotations < 0:%{version}-%{release}

%description -n maven-plugin-annotations
This package contains Java 5 annotations to use in Mojos.

%package -n maven-plugin-plugin
Group: Development/Java
Summary:        Maven Plugin Plugin

%description -n maven-plugin-plugin
The Plugin Plugin is used to create a Maven plugin descriptor for any Mojo's
found in the source tree, to include in the JAR. It is also used to generate
Xdoc files for the Mojos as well as for updating the plugin registry, the
artifact metadata and a generic help goal.

%package annotations
Group: Development/Java
Summary:        Maven Plugin Tool for Annotations

%description annotations
This package provides Java 5 annotation tools for use with Apache Maven.

%if %{with ant}
%package ant
Group: Development/Java
Summary:        Maven Plugin Tool for Ant
Obsoletes:      maven-shared-plugin-tools-ant < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-ant = 0:%{version}-%{release}

%description ant
Descriptor extractor for plugins written in Ant.
%endif

%package api
Group: Development/Java
Summary:        Maven Plugin Tools APIs
Obsoletes:      maven-shared-plugin-tools-api < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-api = 0:%{version}-%{release}

%description api
The Maven Plugin Tools API provides an API to extract information from
and generate documentation for Maven Plugins.

%if %{with beanshell}
%package beanshell
Group: Development/Java
Summary:        Maven Plugin Tool for Beanshell
Obsoletes:      maven-shared-plugin-tools-beanshell < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-beanshell = 0:%{version}-%{release}

%description beanshell
Descriptor extractor for plugins written in Beanshell.
%endif

%package generators
Group: Development/Java
Summary:        Maven Plugin Tools Generators

%description generators
The Maven Plugin Tools Generators provides content generation
(documentation, help) from plugin descriptor.

%package java
Group: Development/Java
Summary:        Maven Plugin Tool for Java
Obsoletes:      maven-shared-plugin-tools-java < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-java = 0:%{version}-%{release}

%description java
Descriptor extractor for plugins written in Java.

%package model
Group: Development/Java
Summary:        Maven Plugin Metadata Model
Obsoletes:      maven-shared-plugin-tools-model < 0:%{version}-%{release}
Provides:       maven-shared-plugin-tools-model = 0:%{version}-%{release}

%description model
The Maven Plugin Metadata Model provides an API to play with the Metadata
model.

%package -n maven-script
Group: Development/Java
Summary:        Maven Script Mojo Support

%description -n maven-script
Maven Script Mojo Support lets developer write Maven plugins/goals
with scripting languages instead of compiled Java.

%if %{with ant}
%package -n maven-script-ant
Group: Development/Java
Summary:        Maven Ant Mojo Support

%description -n maven-script-ant
This package provides %{summary}, which write Maven plugins with
Ant scripts.
%endif

%if %{with beanshell}
%package -n maven-script-beanshell
Group: Development/Java
Summary:        Maven Beanshell Mojo Support

%description -n maven-script-beanshell
This package provides %{summary}, which write Maven plugins with
Beanshell scripts.
%endif

# This "javadocs" package violates packaging guidelines as of Sep 6 2012. The
# subpackage name "javadocs" instead of "javadoc" is intentional. There was a
# consensus that current naming scheme should be kept, even if it doesn't
# conform to the guidelines.  mizdebsk, September 2012
%package javadocs
Group: Development/Java
Summary:        Javadoc for %{name}

%description javadocs
API documentation for %{name}.


%prep
%setup -q

%patch0 -p1
%patch1 -p1

%pom_remove_plugin :maven-enforcer-plugin

%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>"

%if %{without ant}
%pom_disable_module maven-script-ant maven-script
%pom_disable_module maven-plugin-tools-ant maven-script
%endif

%if %{without beanshell}
%pom_disable_module maven-script-beanshell maven-script
%pom_disable_module maven-plugin-tools-beanshell maven-script
%endif

%build
%mvn_build -s -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install


%files -f .mfiles-maven-plugin-tools
%dir %{_javadir}/%{name}
%doc --no-dereference LICENSE NOTICE

%files -n maven-plugin-annotations -f .mfiles-maven-plugin-annotations

%files -n maven-plugin-plugin -f .mfiles-maven-plugin-plugin

%files annotations -f .mfiles-maven-plugin-tools-annotations
%doc --no-dereference LICENSE NOTICE

%if %{with ant}
%files ant -f .mfiles-maven-plugin-tools-ant
%endif

%files api -f .mfiles-maven-plugin-tools-api
%doc --no-dereference LICENSE NOTICE

%if %{with beanshell}
%files beanshell -f .mfiles-maven-plugin-tools-beanshell
%endif

%files generators -f .mfiles-maven-plugin-tools-generators

%files java -f .mfiles-maven-plugin-tools-java

%files model -f .mfiles-maven-plugin-tools-model
%doc --no-dereference LICENSE NOTICE

%files -n maven-script -f .mfiles-maven-script

%if %{with ant}
%files -n maven-script-ant -f .mfiles-maven-script-ant
%doc --no-dereference LICENSE NOTICE
%endif

%if %{with beanshell}
%files -n maven-script-beanshell -f .mfiles-maven-script-beanshell
%doc --no-dereference LICENSE NOTICE
%endif

%files javadocs -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.6.0-alt1_7jpp11
- new version

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.5.1-alt2_7jpp8
- fixed build

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.5.1-alt1_7jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.5.1-alt1_5jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5.1-alt1_1jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_4jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_3jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt4_14jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt4_10jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt4_5jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt3_5jpp7
- update

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

