Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3 rpm-macros-java
BuildRequires: python-devel python3-devel rpm-build-java
# END SourceDeps(oneline)
# optional dependencies of jpackage-utils
%filter_from_requires /^.usr.bin.jar/d
%filter_from_requires /^objectweb-asm/d
%define _unpackaged_files_terminate_build 1

BuildRequires: source-highlight python3-module-nose python3-module-setuptools
%add_python3_path /usr/share/java-utils/
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Don't generate requires on jpackage-utils and java-headless for
# provided pseudo-artifacts: com.sun:tools and sun.jdk:jconsole.
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}/maven-metadata/javapackages-metadata.xml$

%bcond_without asciidoc
%bcond_without gradle
%bcond_with tests
%bcond_with xmvn_javadoc

%if 0%{?fedora} || 0%{?rhel} > 7
%global python_prefix python3
%global python_interpreter %{__python3}
%else
%global python_prefix python
%global python_interpreter %{__python}
%global rpmmacrodir /etc/rpm
%endif

%global default_jdk %{?_root_prefix}%{!?_root_prefix:%{_prefix}}/lib/jvm/java-1.8.0-openjdk
%global default_jre %{?_root_prefix}%{!?_root_prefix:%{_prefix}}/lib/jvm/jre-1.8.0-openjdk

Name:           javapackages-tools
Version:        5.0.0
Release:        alt1_12jpp8.M90P.1

Summary:        Macros and scripts for Java packaging support

License:        BSD
URL:            https://github.com/fedora-java/javapackages
Source0:        https://github.com/fedora-java/javapackages/archive/%{version}.tar.gz
Patch0:         0001-Fix-traceback-on-corrupt-zipfile.patch

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  which
%if %{with asciidoc}
BuildRequires:  asciidoc asciidoc-a2x
BuildRequires:  xmlto
%endif
BuildRequires:  %{python_prefix}-devel
BuildRequires:  python3-module-lxml
BuildRequires:  python3-module-distribute
%if !0%{?_module_build}
# XXX python-nose is not part of any module yet, but it should get
# modularized one day, right?  mizdebsk, Sep 2017
BuildRequires:  python3-module-nose
%endif
BuildRequires:  python3-module-six

Requires:       coreutils
Requires:       findutils
Requires:       which
# default JRE

Obsoletes:      eclipse-filesystem < 2
Provides:       eclipse-filesystem = %{version}-%{release}
Provides:       jpackage-utils = %{version}-%{release}
# These could be generated automatically, but then we would need to
# depend on javapackages-local for dependency generator.
Provides:       mvn(com.sun:tools) = SYSTEM
Provides:       mvn(sun.jdk:jconsole) = SYSTEM
Source44: import.info
Patch33: macros.jpackage-alt-jvmjardir.patch
Source45: abs2rel
Source46: osgi-fc.prov.files
Source47: maven.prov.files
Source48: maven.env
Patch34: javapackages-tools-4.6.0-alt-use-enviroment.patch
Patch35: javapackages-tools-4.6.0-alt-req-headless-off.patch
Patch36: javapackages-tools-4.6.0-alt-shade-jar.patch
Patch37: macros.fjava-to-alt-rpm404.patch
Patch38: macros.fjava-alt-javadoc-package.patch
Patch39: macros.jpackage-alt-script.patch

Conflicts:       jpackage-utils < 0:5.0.1
Obsoletes:       jpackage-utils < 0:5.0.1
Provides:       jpackage-utils = 1:5.0.0

# for jvm backports
Provides: javapackages-filesystem = %version

%description
This package provides macros and scripts to support Java packaging.

%package -n rpm-macros-java
Summary: RPM helper macros to build Java packages
Group: Development/Java
Conflicts: rpm-build-java < 0:5.0.0-alt34
# comment if jnidir patch is used
BuildArch:      noarch

%description -n rpm-macros-java
These helper macros facilitate creation of RPM packages containing Java
bytecode archives and Javadoc documentation.

%package -n rpm-build-java
Summary: RPM build helpers for Java packages
Group: Development/Java
BuildArch:      noarch
Requires:       javapackages-tools = %{epoch}:%{version}-%{release}
Requires: 	rpm-macros-java >= %{epoch}:%{version}-%{release}
#Requires: rpm-build-java-osgi >= %{epoch}:%{version}-%{release}
# moved from main package; not for runtime
Requires:       python3-module-javapackages = %{epoch}:%{version}-%{release}
Requires:       python3

%description -n rpm-build-java
RPM build helpers for Java packages.



%package -n maven-local
Group: Development/Java
Summary:        Macros and scripts for Maven packaging support
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       javapackages-local = %{?epoch:%epoch:}%{version}-%{release}
Requires:       xmvn-minimal
Requires:       xmvn-mojo
Requires:       xmvn-connector-aether
# Common Maven plugins required by almost every build. It wouldn't make
# sense to explicitly require them in every package built with Maven.
Requires:       mvn(org.apache.maven.plugins:maven-compiler-plugin)
Requires:       mvn(org.apache.maven.plugins:maven-jar-plugin)
%if %{without xmvn_javadoc}
Requires:       mvn(org.apache.maven.plugins:maven-javadoc-plugin)
%endif
Requires:       mvn(org.apache.maven.plugins:maven-resources-plugin)
Requires:       mvn(org.apache.maven.plugins:maven-surefire-plugin)
# Tests based on JUnit are very common and JUnit itself is small.
# Include JUnit and JUnit provider for Surefire just for convenience.
Requires:       mvn(junit:junit)
Requires:       mvn(org.apache.maven.surefire:surefire-junit4)
# testng is quite common as well
Requires:       mvn(org.apache.maven.surefire:surefire-testng)

%description -n maven-local
This package provides macros and scripts to support packaging Maven artifacts.

%if %{with gradle}
%package -n gradle-local
Group: Development/Java
Summary:        Local mode for Gradle
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       javapackages-local = %{?epoch:%epoch:}%{version}-%{release}
Requires:       gradle >= 2.2.1
Requires:       xmvn-connector-gradle

%description -n gradle-local
This package implements local mode for Gradle, which allows artifact
resolution using XMvn resolver.
%endif

%package -n ivy-local
Group: Development/Java
Summary:        Local mode for Apache Ivy
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       javapackages-local = %{?epoch:%epoch:}%{version}-%{release}
Requires:       apache-ivy >= 2.3.0
Requires:       xmvn-connector-ivy

%description -n ivy-local
This package implements local mode for Apache Ivy, which allows
artifact resolution using XMvn resolver.

%package -n python3-module-javapackages
Group: Development/Java
Summary:        Module for handling various files for Java packaging
Requires:       python3-module-lxml
Requires:       python3-module-six
Obsoletes:      python-javapackages < %{version}-%{release}

%description -n python3-module-javapackages
Module for handling, querying and manipulating of various files for Java
packaging in Linux distributions

%package -n javapackages-local
Group: Development/Java
Summary:        Non-essential macros and scripts for Java packaging support
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       xmvn-install
Requires:       xmvn-subst
Requires:       xmvn-resolve
# Java build systems don't have hard requirement on java-devel, so it should be there
Requires:       python3-module-javapackages = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{python_prefix}

%description -n javapackages-local
This package provides non-essential macros and scripts to support Java packaging.

%prep
%setup -q -n javapackages-%{version}

%patch0 -p1

%if %{without asciidoc}
sed -i '/^manpage /d' build
sed -i '/${mandir}/d' install
%endif
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1

# alt specific shabang
sed -i -e 1,1s,/bin/bash,/bin/sh, java-utils/java-wrapper bin/*


%build
%configure --pyinterpreter=%{python_interpreter} \
    --default_jdk=%{default_jdk} --default_jre=%{default_jre} \
    --rpmmacrodir=%{_rpmmacrosdir}
./build

%install
./install

%if %{with xmvn_javadoc}
sed -i 's|mvn_build.py|& --xmvn-javadoc|' $(find %{buildroot} -name 'macros*.fjava')
%endif
sed -e 's/.[17]$/&*/' -e 's/.py$/&*/' -i files-*

%if %{without gradle}
rm -rf %{buildroot}%{_bindir}/gradle-local
rm -rf %{buildroot}%{_datadir}/gradle-local
rm -rf %{buildroot}%{_mandir}/man7/gradle_build.7
%endif

install -m755 -D %{SOURCE45} %buildroot%_bindir/abs2rel

install -m755 -D %{SOURCE47} %buildroot/usr/lib/rpm/maven.prov.files
install -m755 -D %{SOURCE47} %buildroot/usr/lib/rpm/maven.req.files

install -m755 -D %{SOURCE47} %buildroot/usr/lib/rpm/javadoc.req.files
sed -i -e s,/usr/share/maven-metadata/,/usr/share/javadoc/, %buildroot/usr/lib/rpm/javadoc.req.files

install -m755 -D %{SOURCE46} %buildroot/usr/lib/rpm/osgi-fc.prov.files
install -m755 -D %{SOURCE46} %buildroot/usr/lib/rpm/osgi-fc.req.files

chmod 755 %buildroot/usr/lib/rpm/*.req* %buildroot/usr/lib/rpm/*.prov*
sed -i -e 's,^#!python,#!/usr/bin/python,' %buildroot/usr/lib/rpm/*.req* %buildroot/usr/lib/rpm/*.prov*

install -m755 -D %{SOURCE48} %buildroot%_rpmmacrosdir/maven.env

# altlinux python support
sed -i -e 's,python?\.?,python*,' files-python
# in rpm-build-java or useless in alt
sed -i -e '/usr\/lib\/rpm/d' files-common files-local
rm -rf %buildroot/usr/lib/rpm/fileattrs

# useless on alt and requires python
sed -i -e '/usr\/bin\/xmvn-builddep/d' files-common files-local
rm -rf %buildroot/usr/bin/xmvn-builddep

pushd %buildroot%_rpmmacrosdir/
mv macros.fjava javapackages-fjava
mv macros.jpackage javapackages-jpackage
#mv macros.scl-java-template javapackages-scl-java-template
popd

pushd %buildroot/usr/lib/rpm/
mv osgi.prov osgi-fc.prov
mv osgi.req osgi-fc.req
popd



%if %{with tests}
%if !0%{?_module_build}
%check
./check
%endif
%endif

%files -f files-common

%files -n javapackages-local -f files-local
# alt python3 cache
%_datadir/java-utils/__pycache__

%files -n rpm-macros-java
%_rpmmacrosdir/javapackages-fjava
%_rpmmacrosdir/javapackages-jpackage
#%_rpmmacrosdir/javapackages-scl-java-template

%files -n rpm-build-java
/usr/lib/rpm/maven.*
/usr/lib/rpm/javadoc.*
/usr/lib/rpm/osgi-fc.*
%_rpmmacrosdir/maven.env
#%_bindir/xmvn-builddep
#%_datadir/java-utils/maven_depmap.py
#%_datadir/java-utils/pom_editor.py
#%_datadir/java-utils/request-artifact.py
#%_datadir/java-utils/__pycache__/maven_depmap.*
#%_datadir/java-utils/__pycache__/pom_editor.*
#%_datadir/java-utils/__pycache__/request-artifact.*


%files -n maven-local

%if %{with gradle}
%files -n gradle-local -f files-gradle
%endif

%files -n ivy-local -f files-ivy

%files -n python3-module-javapackages -f files-python
%doc --no-dereference LICENSE

%changelog
* Sun Dec 13 2020 Igor Vlasenko <viy@altlinux.ru> 1:5.0.0-alt1_12jpp8.M90P.1
- added Provides: javapackages-filesystem for jvm 9-11 backports

* Thu May 10 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.0.0-alt1_12jpp8
- java update

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:5.0.0-alt1_9jpp8.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.0.0-alt1_9jpp8
- full version for xmvn 3

* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.0.0-alt1_0jpp8
- new version - pre for old xmvn

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.7.0-alt3_17jpp8
- removed lua and python code from javapackages-tools

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.7.0-alt2_17jpp8
- move xmvn config back to local

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.7.0-alt1_17jpp8
- new jpp release

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.7.0-alt1_15jpp8
- new jpp release

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt11_15jpp8
- fixed interpackage dependencies

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt10_15jpp8
- update

* Tue Oct 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.6.0-alt10_14jpp8.1
- Fixed build with new python-module-lxml.

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt10_14jpp8
- update

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.6.0-alt9_12jpp8.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.6.0-alt9_12jpp8.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt9_12jpp8
- temporatily disabled gradle patch

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt8_12jpp8
- %%_jnidir set to /usr/lib/java

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt7_12jpp8
- fixes in shade-jar (javapackages-tools-4.6.0-alt-shade-jar.patch)

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt6_12jpp8
- enabled gradle-local

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt5_12jpp8
- fixes in fjava macros

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt4_12jpp8
- fixes in script patch

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt3_12jpp8
- fixes in script macro

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt2_12jpp8
- explicitly cleaned jar dependency
- moved python to rpm-build-java

* Thu Jan 14 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.6.0-alt1_12jpp8
- new version

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 4.6.0-alt1_11jpp7
- new version

