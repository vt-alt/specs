# Copyright (c) 2000-2008, JPackage Project
# Copyright (c) 2009-2021, Altlinux
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Summary:        Dependency Management Utility
Name:           jaranalyzer
Version:        1.2
Release:	alt1_0jpp6
Epoch:          0
License:        BSD-style
URL:            http://www.kirkk.com/main/Main/JarAnalyzer
Group:          Development/Java
Source0:        %name-%version.tar
Source1:        jaranalyzer-1.2.pom
Patch0:         jaranalyzer-1.2-build_xml.patch
Packager:	Igor Vlasenko <viy@altlinux.ru>

BuildRequires: jpackage-default
BuildRequires: /proc
BuildRequires: javapackages-local
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: bcel
BuildRequires: regexp

BuildArch:      noarch

%description
JarAnalyzer is a dependency management utility for jar files. 
It's primary purpose is to traverse through a directory, parse 
each of the jar files in that directory, and identify the 
dependencies between the jar files. The output is an xml file 
representing the PhysicalDependencies between the jar files.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
# remove all binary libs
for j in $(find lib -name "*.jar"); do
    mv $j $j.no
done

%patch0 -b .sav

%build
pushd lib
ln -sf $(build-classpath regexp) jakarta-regexp-1.3.jar
ln -sf $(build-classpath bcel) bcel-5.2.jar
popd

ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6

# request maven artifact installation
%mvn_artifact %{SOURCE1} bin/%{name}-%{version}.jar

%install
%mvn_install -J docs

%jpackage_script com.kirkk.analyzer.textui.XMLUISummary "" "" bcel/bcel:regexp/regexp:jaranalyzer/jaranalyzer runxmlsummary true
%jpackage_script com.kirkk.analyzer.textui.DOTSummary "" "" bcel/bcel:regexp/regexp:jaranalyzer/jaranalyzer rundotsummary true

%files -f .mfiles
%doc bin/license.txt
%{_bindir}/runxmlsummary
%{_bindir}/rundotsummary

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_0jpp6
- new version

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt6_2jpp6
- added BR: javapackages-local for javapackages 5

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt5_2jpp6
- build with java8

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_2jpp5
- use junit 4

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_2jpp5
- explicitly use junit3

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp5
- converted from JPackage by jppimport script

