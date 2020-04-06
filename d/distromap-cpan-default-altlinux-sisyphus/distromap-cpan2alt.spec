# BEGIN SourceDeps(oneline):
BuildRequires: perl(Pod/Usage.pm) perl(Source/Repository/Matcher/CPAN2ALT.pm) perl(Pod/Text.pm)
# END SourceDeps(oneline)
%define orepo cpan
%define obranch default
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.285
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPLv2+ or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

BuildRequires: rpm-build-perl

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/%orepo/%obranch/altlinux/sisyphus
#for type in binary source ; do
for type in source; do
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
done

#for type in binary source ; do
for type in source ; do
	for flag in flags/$type/* ; do
		install -m755 -d $destdir/$flag
		install -m644 $flag/* $destdir/$flag/
	done
done

mkdir -p %buildroot%_bindir
install -m 755 bin/* %buildroot%_bindir/

%files
%_bindir/*
%_datadir/distromap/*

%changelog
* Tue Dec 31 2019 Igor Vlasenko <viy@altlinux.ru> 0.285-alt1
- db update

* Sat Mar 02 2019 Igor Vlasenko <viy@altlinux.ru> 0.284-alt1
- db update

* Sun Jan 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.283-alt1
- db update

* Sat Jan 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.282-alt1
- db update

* Thu Dec 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.281-alt1
- db update

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- db update

* Fri Dec 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- db update

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- db update

* Thu Feb 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- script refactoring

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- new CLI

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- db update

* Fri Oct 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- db update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- db update

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- db update

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- db update

* Sun Feb 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- db update

* Sun Feb 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- db update

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- db update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- db update (CGI.pm is deprecated)

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- db update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- db update

* Fri Jul 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added distromap-filter-translate-altlinux2cpan

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- db update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- db update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- db update

* Tue Jun 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- db update

* Wed Jun 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added cpan distrodb utils

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- db update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- db update

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- db update

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- db update

* Fri Apr 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- db update

* Thu Apr 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- db update
