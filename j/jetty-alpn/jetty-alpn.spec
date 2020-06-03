Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global reltag .v20181017

Name:           jetty-alpn
Version:        8.1.13
Release:        alt1_1.v20181017jpp8
# alpn-tests also contains EPL and ASL, but is not installed
License:        GPLv2+ with exceptions
Summary:        Jetty implementation of ALPN API
URL:            https://github.com/jetty-project/jetty-alpn
Source0:        https://github.com/jetty-project/%{name}/archive/alpn-project-%{version}%{reltag}.tar.gz
Patch0:         0001-Unshade-alpn-api.patch
BuildArch:      noarch

BuildRequires:  java-1.8.0-openjdk-headless
Requires:       java-1.8.0-openjdk-headless

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)
Source44: import.info

%description
A pure Java(TM) implementation of the Application Layer Protocol
Negotiation TLS Extension


%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-alpn-project-%{version}%{reltag}

# unshade jetty-alpn-api
%patch0 -p1
%pom_remove_plugin -r :maven-shade-plugin

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_disable_module alpn-tests

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 8.1.13-alt1_1.v20181017jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 8.1.12-alt1_2.v20180117jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 8.1.11-alt1_3.v20170118jpp8
- new version

