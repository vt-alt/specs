%def_without bootstrap
%define destname gear-uupdate
Name: %destname
Version: 0.28.0
Release: alt1

Summary: Helper utility to be called by uscan for gear repository update
Source: %name-%version.tar

License: GPL2+
Group: Development/Other
URL: http://www.altlinux.org/Gear/gear-uupdate

BuildArch: noarch

BuildRequires: perl-devel perl(Pod/Usage.pm) /usr/bin/pod2man perl-Gear-Rules perl-Source-Bundle perl-RPM-Source-Editor perl-String-ShellQuote
Requires: gear /usr/bin/srpmnmu perl-Gear-Rules > 0.196 perl-RPM-Source-Editor > 0.9228
%if_without bootstrap
Requires: /usr/bin/gear-remotes-fetch
%endif

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -Dm755 gear-uupdate gear-uupdate-* %buildroot%_bindir/

for i in gear-uupdate-prepare gear-uupdate-execute; do
    pod2man  --name $i --center $i --section 1 --release %version $i > $i.1
done
ln -s gear-uupdate-prepare.1 gear-uupdate.1
mkdir -p %buildroot%_man1dir
install -m 644 gear-*.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Aug 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.28.0-alt1
- use --ignore-exclude by default (closes: #37129)

* Thu Jun 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- use new API

* Thu Oct 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- added support for subtree merge

* Fri Oct 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- updated man pages thanks to grenka@

* Fri Feb 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- initial submodules support

* Tue Jan 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2
- cleaned up install garbage (closes: 34475)

* Thu Apr 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- new version

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- new version

* Mon Jan 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- new version

* Fri Sep 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- support for GEAR_UUPDATE_CHANGELOG

* Wed Sep 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- gear-update --exclude option support

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- new version

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- specgen support

* Sun Jul 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- new version

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- new version

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- added --override-spec option

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- bugfix release

* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- new version

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- updated man pages

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- bugfix release

* Sat Aug 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- now works correctly with depth0 archives

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- git merge --no-edit default behavior

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- bugfix release

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fixes for upstream branch with sources in root

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- bugfix

* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added man page

* Fri Jan 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new version

* Thu Oct 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new development version

* Wed Oct 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- new version

* Sat Oct 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First draft

