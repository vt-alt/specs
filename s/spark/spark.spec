%define _unpackaged_files_terminate_build 1

%define oname spark

Name:    spark
Version: 2.6.0
Release: alt2
Summary: A simple expressive web framework for java
License: Apache-2.0
Group:   Development/Java
URL:     http://sparkjava.com/

BuildArch: noarch

# https://github.com/perwendel/spark.git
Source: %name-%version.tar

Patch1: CVE-2018-9159-upstream-patch-1.patch
Patch2: CVE-2018-9159-upstream-patch-2.patch

BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: java-devel >= 1.6
BuildRequires: javapackages-local
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.eclipse.jetty.websocket:websocket-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-webapp)

%description
A simple expressive web framework for java

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{oname}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{oname}.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%mvn_build --skip-tests

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc README.md
%doc LICENSE NOTICE

%changelog
* Thu Aug 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt2
- Applied security fixes from upstream (Fixes: CVE-2018-9159)

* Mon Nov 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Initial build for ALT.
