%define oldname glassfish-jaxb
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Conditionally build with a minimal dependency set
%bcond_without jp_minimal

Name:           glassfish-jaxb2.2
Version:        2.2.11
Release:        alt8_15jpp8
Summary:        JAXB Reference Implementation

License:        CDDL-1.1 and GPLv2 with exceptions
URL:            http://jaxb.java.net

Source0:        https://jaxb.java.net/%{version}/jaxb-ri-%{version}.src.zip
Patch0:         0001-Avoid-unnecessary-dep-on-istack-commons.patch
Patch1:         0002-Port-to-latest-version-of-args4j.patch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
#BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
%if %{without jp_minimal}
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime:2.21)
BuildRequires:  mvn(com.sun.istack:istack-commons-tools:2.21)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset:1.2.13)
BuildRequires:  mvn(com.sun.xsom:xsom:pom:20140925)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype:20020414)
%endif

Requires:       %{name}-core = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-runtime = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-txw2 = %{?epoch:%epoch:}%{version}-%{release}
%if %{without jp_minimal}
Requires:       %{name}-bom = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-bom-ext = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-codemodel = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-codemodel-annotation-compiler = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-codemodel-parent = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-external-parent = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-jxc = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-parent = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-rngom = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-runtime-parent = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-txwc2 = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-txw-parent = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{name}-xjc = %{?epoch:%epoch:}%{version}-%{release}
%endif

Obsoletes:      glassfish-jaxb1-impl                  < 2.2.11-12

BuildArch:      noarch
Source44: import.info

%description
GlassFish JAXB Reference Implementation.

%package core
Group: Development/Java
Summary:        JAXB Core

%description core
JAXB Core module. Contains sources required by XJC, JXC and Runtime
modules.

%package runtime
Group: Development/Java
Summary:        JAXB Runtime

%description runtime
JAXB (JSR 222) Reference Implementation

%package txw2
Group: Development/Java
Summary:        TXW2 Runtime

%description txw2
TXW is a library that allows you to write XML documents.

%if %{without jp_minimal}
%package codemodel
Group: Development/Java
Summary:        Codemodel Core

%description codemodel
The core functionality of the CodeModel java source code generation
library.

%package codemodel-annotation-compiler
Group: Development/Java
Summary:        Codemodel Annotation Compiler

%description codemodel-annotation-compiler
The annotation compiler ant task for the CodeModel java source code
generation library.

%package bom
Group: Development/Java
Summary:        JAXB BOM

%description bom
JAXB Bill of Materials (BOM)

%package bom-ext
Group: Development/Java
Summary:        JAXB BOM with all dependencies

%description bom-ext
JAXB Bill of Materials (BOM) with all dependencies.

%package codemodel-parent
Group: Development/Java
Summary:        Codemodel parent POM

%description codemodel-parent
This package contains codemodel parent POM.

%package external-parent
Group: Development/Java
Summary:        JAXB External parent POM

%description external-parent
JAXB External parent POM.

%package jxc
Group: Development/Java
Summary:        JAXB schema generator

%description jxc
The tool to generate XML schema based on java classes.

%package parent
Group: Development/Java
Summary:        JAXB parent POM

%description parent
This package contains parent POM.

%package runtime-parent
Group: Development/Java
Summary:        JAXB Runtime parent POM

%description runtime-parent
This package contains Runtime parent POM.

%package txw-parent
Group: Development/Java
Summary:        JAXB TXW parent POM

%description txw-parent
This package contains TXW parent POM.

%package xjc
Group: Development/Java
Summary:        JAXB XJC

%description xjc
JAXB Binding Compiler. Contains source code needed for binding
customization files into java sources. In other words: the tool to
generate java classes for the given xml representation.

%package rngom
Group: Development/Java
Summary:        RELAX NG Object Model/Parser

%description rngom
This package contains RELAX NG Object Model/Parser.

%package txwc2
Group: Development/Java
Summary:        TXW2 Compiler

%description txwc2
JAXB schema generator. The tool to generate XML schema based on java
classes.
%endif

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{oldname}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q -c

%if %{with jp_minimal}
%patch0 -p1
%endif
%patch1 -p1

#viy@: set compat versions
%if %{without jp_minimal}
#./xjc/pom.xml:            <groupId>com.sun.istack</groupId>
#./xjc/pom.xml:            <artifactId>istack-commons-tools</artifactId>
%pom_change_dep com.sun.istack: ::2.21 xjc codemodel/codemodel-annotation-compiler core
%endif

# Disable unneeded OSGi bundles
%pom_disable_module xjc bundles
%pom_disable_module jxc bundles
%pom_disable_module ri bundles
%pom_disable_module osgi bundles
%pom_disable_module core bundles

# Fix jar plug-in usage for OSGi bundles
%pom_xpath_replace "pom:useDefaultManifestFile" "
<archive>
  <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
</archive>" bundles/core bundles/runtime

# Make javax.activation an optional dep
%pom_xpath_inject "pom:configuration/pom:instructions" "
<Import-Package>javax.activation;resolution:=optional,*</Import-Package>" bundles/runtime

# Disable ancient jaxb1 runtime
%pom_disable_module jaxb1 runtime

# Fix hard-coded tools location
%pom_remove_dep com.sun:tools
%pom_add_dep_mgmt com.sun:tools
%pom_remove_dep com.sun:tools jxc
%pom_add_dep com.sun:tools jxc

# Plug-ins not useful for RPM builds
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :gfnexus-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin jxc
%pom_remove_plugin :maven-source-plugin xjc
%pom_remove_plugin :maven-javadoc-plugin

%if %{with jp_minimal}
# For minimal build disable all modules with extra deps
%pom_disable_module codemodel
%pom_disable_module external
%pom_disable_module jxc
%pom_disable_module compiler txw
%pom_disable_module xjc
# For minimal build of impl module, don't compile in support for extra deps
%pom_remove_dep org.jvnet.staxex:stax-ex runtime/impl
%pom_remove_dep com.sun.xml.fastinfoset:FastInfoset runtime/impl
rm runtime/impl/src/main/java/com/sun/xml/bind/v2/runtime/unmarshaller/{FastInfoset,StAXEx}Connector.java
rm runtime/impl/src/main/java/com/sun/xml/bind/v2/runtime/output/{FastInfoset,StAXEx}StreamWriterOutput.java
%endif

%mvn_alias org.glassfish.jaxb:jaxb-xjc "com.sun.xml.bind:jaxb-xjc"

# Package OSGi version of runtime with the non-OSGi version
%mvn_package com.sun.xml.bind:jaxb-impl jaxb-runtime

# Don't install bundles parent pom
%mvn_package com.sun.xml.bind.mvn:jaxb-bundles __noinstall

%if %{with jp_minimal}
# Don't install aggregator poms or boms for minimal build
%mvn_package com.sun.xml.bind.mvn: __noinstall
%mvn_package :jaxb-bom* __noinstall
%endif

%mvn_compat_version : 2.2.6 2.2.7 %{version}

%build
%mvn_build -f -s -j -- -Ddev -DbuildNumber=unknown

%install
%mvn_install

%files
%doc --no-dereference License.txt licenceheader.txt License.html

%files core -f .mfiles-jaxb-core
%doc --no-dereference License.txt licenceheader.txt License.html

%files runtime -f .mfiles-jaxb-runtime
%doc --no-dereference License.txt licenceheader.txt License.html

%files txw2 -f .mfiles-txw2
%doc --no-dereference License.txt licenceheader.txt License.html

%if %{without jp_minimal}
%files codemodel -f .mfiles-codemodel
%doc --no-dereference License.txt licenceheader.txt License.html

%files codemodel-annotation-compiler -f .mfiles-codemodel-annotation-compiler

%files bom -f .mfiles-jaxb-bom
%doc --no-dereference License.txt licenceheader.txt License.html

%files bom-ext -f .mfiles-jaxb-bom-ext

%files codemodel-parent -f .mfiles-jaxb-codemodel-parent

%files external-parent -f .mfiles-jaxb-external-parent

%files jxc -f .mfiles-jaxb-jxc
%doc --no-dereference License.txt licenceheader.txt License.html

%files parent -f .mfiles-jaxb-parent

%files runtime-parent -f .mfiles-jaxb-runtime-parent

%files txw-parent -f .mfiles-jaxb-txw-parent

%files xjc -f .mfiles-jaxb-xjc

%files rngom -f .mfiles-rngom
%doc --no-dereference License.txt licenceheader.txt License.html

%files txwc2 -f .mfiles-txwc2
%doc --no-dereference License.txt licenceheader.txt License.html
%endif

#%files javadoc -f .mfiles-javadoc
#%doc --no-dereference License.txt licenceheader.txt License.html


%changelog
* Wed Jun 09 2021 Igor Vlasenko <viy@altlinux.org> 0:2.2.11-alt8_15jpp8
- compat build

* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0:2.2.11-alt7_15jpp8
- build with compat glassfish-fastinfoset

* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0:2.2.11-alt6_15jpp8
- build with compat xsom

* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0:2.2.11-alt5_15jpp8
- build with compat relaxngDatatype

* Sun Jun 06 2021 Igor Vlasenko <viy@altlinux.org> 0:2.2.11-alt4_15jpp8
- fixed build

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 0:2.2.11-alt3_15jpp8
- fixed build

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt2_15jpp8
- update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt2_11jpp8
- fc update & java 8 build

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt2_10jpp8
- fc29 update

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt2_9jpp8
- fc28+ update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt1_9jpp8
- java fc28+ update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.2.11-alt1_3jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.5-alt1_3jpp7
- fc version
- jaxb 2.2 api
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt3_7jpp6
- built with java 6

* Fri Feb 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt2_7jpp6
- removed compat symlink

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1.9-alt1_7jpp6
- new version

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_7jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.4-alt1_6jpp5
- converted from JPackage by jppimport script

