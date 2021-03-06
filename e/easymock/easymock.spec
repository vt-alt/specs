Epoch: 0
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           easymock
Version:        4.2
Release:        alt1_1jpp11
Summary:        Easy mock objects
License:        ASL 2.0

URL:            http://www.easymock.org
Source0:        https://github.com/easymock/easymock/archive/easymock-%{version}.tar.gz

Patch1:         0001-Disable-android-support.patch
Patch2:         0002-Unshade-cglib-and-asm.patch
Patch3:         0003-Fix-OSGi-manifest.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.junit.vintage:junit-vintage-engine)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.testng:testng)
# xmvn-builddep misses this:
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)

Obsoletes:      %{name}3 < 3.4
Provides:       %{name}3 = %{version}-%{release}
Obsoletes:      %{name}2 < 2.5.2-10
Source44: import.info

%description
EasyMock provides Mock Objects for interfaces in JUnit tests by generating
them on the fly using Java's proxy mechanism. Due to EasyMock's unique style
of recording expectations, most refactorings will not affect the Mock Objects.
So EasyMock is a perfect fit for Test-Driven Development.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{name}-%{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1

# disable unnecessary maven plugins
%pom_remove_plugin :animal-sniffer-maven-plugin . core
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-gpg-plugin test-java8 test-junit5 test-testng
%pom_remove_plugin :maven-timestamp-plugin
%pom_remove_plugin :versions-maven-plugin

# remove android support
rm core/src/main/java/org/easymock/internal/Android*.java
rm core/src/test/java/org/easymock/tests2/ClassExtensionHelperTest.java
%pom_disable_module test-android
%pom_remove_dep :dexmaker core

# unbundle asm and cglib
%pom_disable_module test-nodeps
%pom_remove_plugin :maven-shade-plugin core

# missing test deps
%pom_disable_module test-integration
%pom_disable_module test-osgi

# For compatibility reasons
%mvn_file ":easymock{*}" easymock@1 easymock3@1

# ssh not needed during our builds
%pom_xpath_remove pom:extensions


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference core/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference core/LICENSE.txt


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_5jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_3jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_3jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_20jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_18jpp7
- fc update

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_8jpp6
- jpp 6 release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp5
- new jpackage release

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

