%define testname lintian
%define lintianver 1.23.48

Name: repocop-unittest-lintian-noncollectors
Version: 0.16.%lintianver
Release: alt8
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>

Summary: port of lintian integration tests for repocop test platform.
Group: Development/Other
License: GPLv2+
Url: http://repocop.altlinux.org
Requires: repocop > 0.55

Source: %name-%version.tar

%description
Lintian is Debian package checker.
Lintian dissects Debian packages and reports bugs and policy violations. It contains automated checks for many aspects of Debian policy as well as some checks for common errors.

This package contains ports to repocop of the following lintian tests:
aspell-package-not-arch-all
backup-file-in-package
bad-permissions-for-ali-file
desktop-file-in-wrong-dir
executable-manpage
macos-ds-store-file-in-package
macos-resource-fork-file-in-package
old-app-defaults-directory
package-installs-file-to-usr-x11r6
subdir-in-usr-bin
symkink-extra-slash
windows-thumbnail-database-in-package

and also adds distro-undependent tests such as
files-in-usr-src-tmp

%prep
%setup

%build

%install

for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

for i in *.pl; do
    install -pD -m 644 $i %buildroot%_datadir/repocop/fixscripts/$i
done

%files
%_datadir/repocop/pkgtests/*
%_datadir/repocop/fixscripts/*

%changelog
* Fri Sep 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.16.1.23.48-alt8
- bugfix release

* Thu Sep 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.16.1.23.48-alt7
- removed known false positives in aspell-package-not-arch-all
- (closes: #38840)

* Tue Apr 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.1.23.48-alt6
- extended arch-dep-package-consists-of-usr-share.pl range

* Thu Jan 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.1.23.48-alt5
- bugfix release

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.1.23.48-alt4
- bugfix release

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.1.23.48-alt3
- added fixscript for arch-dep-package-consists-of-usr-share

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.1.23.48-alt2
- fix in file-in-usr-marked-as-private.posttest

* Thu Nov 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.16.1.23.48-alt1
- adapted for new fixscript syntax

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.15.1.23.48-alt6
- added file-in-usr-marked-as-private.posttest

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.15.1.23.48-alt5
- fixed vim swap file detection thanks to Vladimir Lettiev & Kirill Maslinsky

* Thu Dec 17 2009 Igor Vlasenko <viy@altlinux.ru> 0.15.1.23.48-alt4
- increased level in arch-dep-package-has-big-usr-share
  * added arch-dep-package-consists-of-usr-share

* Wed Dec 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.15.1.23.48-alt3
- renamed: symkink-extra-slash.posttest -> symlink-extra-slash.posttest
	(closes: #22553)
  fixed: backup-file-in-package.pl
  fixed: macos-resource-fork-file-in-package.pl

* Sat Nov 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.15.1.23.48-alt2
- improved pkg-contains-cvs-or-svn-control-dir.pl

* Fri Oct 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.15.1.23.48-alt1
- fixed #21944

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.14.1.23.48-alt3
- posttests migration

* Tue Sep 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.14.1.23.48-alt2
- added exception for GeoIP-Lite-*

* Mon Sep 14 2009 Igor Vlasenko <viy@altlinux.ru> 0.14.1.23.48-alt1
- added subdir-in-var-run test

* Mon May 18 2009 Igor Vlasenko <viy@altlinux.ru> 0.13.1.23.48-alt1
- rm deprecated install-info-not-called && uninstall-info-not-called

* Thu May 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.12.1.23.48-alt3
- bugfix

* Wed May 06 2009 Igor Vlasenko <viy@altlinux.ru> 0.12.1.23.48-alt2
- added Url; added known exeptions to file-in-usr-marked-as-conffile.

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0.12.1.23.48-alt1
- added files-in-usr-src-tmp

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0.11.1.23.48-alt3
- repocop 0.10 adaptation

* Sun Nov 23 2008 Igor Vlasenko <viy@altlinux.ru> 0.11.1.23.48-alt2
- removed bad-permissions-for-ali-file

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.11.1.23.48-alt1
- quiet patch generators

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt9
- added macos-resource-fork-file-in-package patch generator 

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt8
- removed duplicate finds in diffs

* Mon Nov 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt7
- added patch generator for pkg-contains-cvs-or-svn-control-dir

* Mon Nov 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt6
- fixed patch generators

* Sun Nov 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt5
- added patch generators for bugs present in current Sisyphus

* Sun Aug 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt4.1
- bugfix

* Fri Aug 01 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt4
- arch-dep-package-has-big-usr-share also reports completely noarch
  packages (at@' suggest)

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt3
- enabled arch-dep-package-has-big-usr-share.done 
  (for at@' noarch, experimental level)
- fixed bug in macos-ds-store-file-in-package

* Sat Jun 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt2
- new tests:
  + file-in-usr-marked-as-conffile
  + install-info-not-called
  + uninstall-info-not-called
  modified: macos-ds-store-file-in-package

* Tue May 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.10.1.23.48-alt1
- added more tests

* Mon May 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.01.1.23.48-alt1
- initial version
