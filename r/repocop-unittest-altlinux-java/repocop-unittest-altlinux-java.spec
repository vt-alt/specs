#define testname spec-has-obsolete-macroses

Name: repocop-unittest-altlinux-java
Version: 0.14
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>
Url: http://repocop.altlinux.org

Summary: repocop package checks for conformance with Java Packaging Policy.
Group: Development/Other
License: GPLv2+ or Artistic
Source: %name-%version.tar

Requires: repocop >= 0.59

%description
set of ALTLinux-specific integration tests for repocop test platform.
The tests checks packages for conformance with Java Packaging Policy.

%prep
%setup

%build

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

for i in *.distrotest; do
    testname=`echo $i | sed -e s,.distrotest\$,,`
    install -pD -m 755 $testname.distrotest %buildroot%_datadir/repocop/pkgtests/$testname/distrotest
done

install -d -m 755 %buildroot%_datadir/repocop/fixscripts/
#install -m 644 *.pl %buildroot%_datadir/repocop/fixscripts/

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/*
#%_datadir/repocop/fixscripts/*

%changelog
* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- updated altlinux-java-forbidden-requires.posttest

* Mon Jul 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- added distrotest

* Wed Nov 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- updated tests

* Mon Nov 09 2009 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- removed obsolete altlinux-java-not-buildrequires-rpm-build-java

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- posttests migration

* Wed May 27 2009 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added exception for java-1.x.x-gcj

* Fri May 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- fixes in forbidden-requires

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- repocop 0.10 support

* Wed Dec 24 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added altlinux-java-forbidden-requires test 

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added altlinux-java-obsolete-java4.done

* Sat Nov 29 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added altlinux-java-not-buildrequires-rpm-build-java test

* Mon Aug 11 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- fixes in duplicate jar test

* Fri Aug 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added altlinux-java-duplicate-jars test

* Tue Aug 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
