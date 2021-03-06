Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
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
# Toggle tests
# Currently failing
%bcond_without mvn_tests

# A test requires network access,
# Run mock with --enable-network --with=network
%bcond_with network

%global pretty_name jLEMS

Name:           jlems
Version:        0.9.9.1
Release:        alt1_7jpp11
Summary:        Java Interpreter for the Low Entropy Model Specification language


License:        MIT
URL:            https://github.com/LEMS/jLEMS
Source0:        https://github.com/LEMS/%{pretty_name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  janino
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-surefire-plugin

# provide this to make it easier for users to find it
Provides:  %{pretty_name} = %{version}-%{release}
Source44: import.info

# Autogenerated, not needed
# Requires:       java-headless
# Requires:       javapackages-filesystem

%description
Java Interpreter for the Low Entropy Model Specification language.

See http://lems.github.com/LEMS

For more details on LEMS see:

Robert C. Cannon, Padraig Gleeson, Sharon Crook, Gautham Ganapathy, Boris
Marin, Eugenio Piasini and R. Angus Silver, LEMS: A language for expressing
complex biological models in concise and hierarchical form and its use in
underpinning NeuroML 2, Frontiers in Neuroinformatics 2014, doi:
10.3389/fninf.2014.00079

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{pretty_name}-%{version}


# Unavilable, remove
%pom_remove_plugin  :maven-bundle-plugin
%pom_xpath_remove  "pom:packaging"

# Remove unneeded bits from the runner script
sed -i '/LEMS_HOME/ d' lems
sed -i '/CLASSPATH=/ d' lems
sed -i 's|\$CLASSPATH|%{_javadir}/%{name}/jlems.jar|' lems

# remove test that requires network if network is not available
# tested in mock with --enable-network --with=network: it PASSES
%if !%{with network}
rm -vf ./src/test/java/org/lemsml/jlems/test/URLInclusionReaderTest.java
%endif

# Specify correct location of lems in this test
sed -i 's|../jLEMS/lems|./lems|' ./src/test/java/org/lemsml/jlems/io/reader/JarResourceInclusionReaderTest.java

%build
%if %{with mvn_tests}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
%else
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
%endif


%install
%mvn_install
install -v -pm 0755 lems -D %{buildroot}/%{_bindir}/lems


%check
# Try examples as tests:
# https://github.com/LEMS/jLEMS/blob/master/.travis.yml
# Update classpath for the local script to run tests
sed -i 's|%{_javadir}|%{buildroot}/%{_javadir}|' lems

./lems src/test/resources/example1.xml -nogui
./lems src/test/resources/example2.xml -nogui
./lems src/test/resources/example3.xml -nogui
./lems src/test/resources/example4.xml -nogui
./lems src/test/resources/example5.xml -nogui
./lems src/test/resources/example6.xml -nogui
./lems src/test/resources/example7.xml -nogui
./lems src/test/resources/example8.xml -nogui
./lems src/test/resources/bounce-conditional.xml -nogui
./lems src/test/resources/bounce.xml -nogui
./lems src/test/resources/ex-flat.xml -nogui
./lems src/test/resources/test_regime_iaf.xml -nogui
./lems src/test/resources/ex-properties.xml -nogui


%files -f .mfiles
%{_bindir}/lems
%doc --no-dereference LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 0.9.9.1-alt1_7jpp11
- new version

