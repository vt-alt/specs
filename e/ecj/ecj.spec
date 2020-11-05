Group: Development/Java
Obsoletes: ecj-standalone <= 3.4.2-alt4_0jpp6
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Epoch: 1

%global qualifier S-4.11RC1-201903010040

Summary: Eclipse Compiler for Java
Name: ecj
Version: 4.11
Release: alt1_0.1jpp9
URL: http://www.eclipse.org
License: EPL-2.0

Source0: http://download.eclipse.org/eclipse/downloads/drops4/%{qualifier}/ecjsrc-%{version}RC1.jar
Source1: ecj.sh.in
Source3: https://repo1.maven.org/maven2/org/eclipse/jdt/core/compiler/ecj/%{version}/ecj-%{version}.pom
# Extracted from https://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/%%{qualifier}/ecj-%%{version}.jar
Source4: MANIFEST.MF
# Java API stubs for newer JDKs
Source5: java10api.jar

# Always generate debug info when building RPMs (Andrew Haley)
Patch0: %{name}-rpmdebuginfo.patch

# Include java API stubs in build
Patch1: javaAPI.patch

BuildArch: noarch

BuildRequires: ant
BuildRequires: javapackages-local
Source44: import.info
# Use ECJ for GCJ
# cvs -d:pserver:anonymous@sourceware.org:/cvs/rhug \
# export -D 2013-12-11 eclipse-gcj
# tar cjf ecj-gcj.tar.bz2 eclipse-gcj
Source2: ecj-gcj.tar.bz2
Patch33: ecj-defaultto1.5.patch
Patch55: eclipse-gcj-nodummysymbol.patch
Patch34: ecj-gcj-for-4.6-api.patch

AutoReq: yes, noosgi
AutoProv: yes, noosgi

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%prep
%setup -q -c
%patch0 -p1
%patch1

sed -i -e 's|debuglevel=\"lines,source\"|debug=\"yes\"|g' build.xml

cp %{SOURCE3} pom.xml
mkdir -p scripts/binary/META-INF/
cp %{SOURCE4} scripts/binary/META-INF/MANIFEST.MF

# JDTCompilerAdapter isn't used by the batch compiler
rm -f org/eclipse/jdt/core/JDTCompilerAdapter.java

# No dep on ant needed
%pom_remove_dep org.apache.ant:ant

# Symlinks and aliases
%mvn_file :ecj ecj jdtcore
%mvn_alias org.eclipse.jdt.core.compiler:ecj \
  org.eclipse.tycho:org.eclipse.jdt.core org.eclipse.tycho:org.eclipse.jdt.compiler.apt \
  org.eclipse.jdt:core org.eclipse.jdt:ecj

# Make Java API stubs available for other packages
%mvn_artifact "org.eclipse:java10api:jar:10" %{SOURCE5}
%mvn_alias "org.eclipse:java10api:jar:10" "org.eclipse:java9api:jar:9"
%patch33 -p1

# Use ECJ for GCJ's bytecode compiler
tar jxf %{SOURCE2}
mv eclipse-gcj/org/eclipse/jdt/internal/compiler/batch/GCCMain.java \
  org/eclipse/jdt/internal/compiler/batch/
%patch55 -p1
cat eclipse-gcj/gcc.properties >> \
  org/eclipse/jdt/internal/compiler/batch/messages.properties
rm -rf eclipse-gcj
%patch34 -p1
#patch55 -p1

%build
ant -Djavaapi=%{SOURCE5}

%install
%mvn_artifact pom.xml ecj.jar
%mvn_install

# Install the ecj wrapper script
install -p -D -m0755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/ecj

# Install manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p ecj.1 $RPM_BUILD_ROOT%{_mandir}/man1/ecj.1

%files -f .mfiles
%doc --no-dereference about.html
%{_bindir}/ecj
%{_mandir}/man1/ecj*

%changelog
* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt1_0.1jpp9
- rebuild with java 9

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt1_0.1jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.7.3a-alt1_1jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.7.1-alt1_1jpp8
- new version

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.2-alt2_3jpp8
- merged eclipse-gcj code && native by glebfm@

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.2-alt1_3jpp8
- new version

* Wed Feb 03 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:4.5.1-alt2_1jpp8
- Reenabled eclipse-gcj code.
- Updated eclipse-gcj to CVS 2013-12-11.
- Restored native subpackage.

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt1_1jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.2.1-alt1_7jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt5_7jpp6.qa1
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:3.4.2-alt4_7jpp6.qa1
- NMU: rebuilt for debuginfo.

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt4_7jpp6
- removed Req: java-gcj-compat (closes: #23902)

* Thu Aug 19 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt3_7jpp6
- BR:java-gcj-compat reduced to fastjar (#23902)

* Sat Feb 20 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt2_7jpp6
- removed poms as it breaks too much builds

* Tue Jan 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:3.4.2-alt1_7jpp6
- replaces ecj-standalone

