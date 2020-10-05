Name: repocop-unittest-altlinux-policy
Version: 0.45
Release: alt1
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>
Url: http://repocop.altlinux.org

Summary: altlinux-policy integration tests for repocop test platform.
Group: Development/Other
License: GPLv2+

Source: %name-%version.tar
Provides: repocop-unittest-altlinux-policy-rpm-macros-packaging = 0.04
Obsoletes: repocop-unittest-altlinux-policy-rpm-macros-packaging
Obsoletes: repocop-unittest-unknown-summary < 0.02

# for pixmap-in-deprecated-location
# Requires: pcregrep
Requires: repocop-collector-specfile
Requires: repocop-collector-description > 0.02
Requires: repocop > 0.79

BuildRequires: perl(RPM/Source/Editor.pm) perl(RPM/Source/SpecConst.pm)


%description
The test warns packages that contain rpm macros, but are not named
appropriately.

%prep
%setup

%build

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    case $testname in
	specfile-*)
	    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/srctests/$testname/posttest
	    ;;
	*)
	    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
    esac
done

for i in *.pl; do
    install -pD -m 644 $i %buildroot%_datadir/repocop/fixscripts/$i
done

for i in repocop-helper-*; do
    testname=`echo $i | sed -e s,^repocop-helper-,,`
    case $testname in
	specfile-*)
	    install -pD -m 755 $i %buildroot%_datadir/repocop/srctests/$testname/repocop-helper-$testname
	    ;;
	*)
	    install -pD -m 755 $i %buildroot%_datadir/repocop/pkgtests/$testname/repocop-helper-$testname
    esac
done

%files
%_datadir/repocop/pkgtests/*
%_datadir/repocop/srctests/*
%_datadir/repocop/fixscripts/*

%changelog
* Thu Sep 17 2020 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- specfile-useradd-n tuned

* Wed Sep 16 2020 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- added specfile-useradd-n test

* Fri Jun 14 2019 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- added specfile-macros-ubt-is-deprecated

* Mon Aug 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- added:
  %%__autoreconf fixscript
  specfile-macros-post_fonts-is-deprecated
  specfile-macros-post_ldconfig-is-deprecated
  specfile-macros-__autoreconf-is-obsolete
  specfile-macros-update_menus-is-deprecated
  specfile-macros-update_vimhelp-is-deprecated

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- altlinux-policy-description-too-much-space lowered to info

* Tue Jul 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- added:
  altlinux-policy-description-has-tags.posttest
  altlinux-policy-description-too-much-space.posttest

* Tue Jul 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- updated list of exceptions

* Wed Jun 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- bugfix in altlinux-policy-policykit-bad-location.posttest
- added altlinux-policy-unknown-summary.posttest

* Sun Oct 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- added altlinux-policy-policykit-bad-location.posttest

* Sat Oct 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- do not clean %%__python in postclean pl

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- added exception for hpmud.so

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- added exception for libgdiplus.so

* Thu Jul 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- perl 5.22 quoting in pl fixscripts

* Tue Apr 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- skip *.env in macros.d

* Thu Sep 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- added dbus-xml-not-in-devel

* Mon Apr 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt4
- bugfix release

* Sun Apr 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt3
- bugfix release

* Thu Jan 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2
- bugfix release

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- bugfix release

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt11
- bugfix release

* Tue Nov 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt10
- added requires-ImageMagick.posttest

* Thu Oct 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt9
- added altlinux-policy-rpm-group-should-be-ttf

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt8
- added tests:
  + altlinux-policy-obsolete-httpd2-reload
  + altlinux-policy-rpm-group-should-be-text-tools

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt7
- custom names for rpm-macros-* subpoackages

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt6
- bugfix in altlinux-policy-rpm-macros-packaging*

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt5
- restored specfile-macros-get_dep-is-deprecated.posttest
  as experimental w/o patch generator.

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt4
- removed specfile-macros-get_dep-is-deprecated

* Tue Aug 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt3
- added rpm built-ins to altlinux-policy-rpm-macros-packaging-rpm4

* Tue Aug 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt2
- bugfix in altlinux-policy-rpm-macros-packaging-rpm4

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- added altlinux-policy-rpm-macros-packaging-rpm4

* Thu Nov 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- adapted for new fixscript syntax

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- fixscripts adopted for new R::S::E

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- added files-in-deprecated-iconsdir-mini-large.posttest

* Tue Jun 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- bugfix release

* Wed May 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- altlinux-policy-obsolete-buildreq

* Tue May 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- added postclean for private rpm macros

* Sat Apr 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt4
- altlinux-policy-debian-menu-is-deprecated.posttest:
  * exception for wm-specific menus (todo: debian menu test)

* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt3
- altlinux-policy-debian-menu-is-deprecated.posttest:
  * exception for sessions

* Sun Mar 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2
- altlinux-policy-debian-menu-is-deprecated.posttest:
   exception for wm*

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- added altlinux-policy-debian-menu-is-deprecated.posttest

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt3
- fixed check for get_version

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt2
- bugfixes in patch generator

* Sun Jan 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- added check for get_version

* Fri Jan 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- added specfile-macros-get_dep-is-deprecated
- removed deprecated pixmap-in-deprecated-location

* Fri Aug 20 2010 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- added deprecated-packages-info-i18n-common.posttest

* Fri Feb 19 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt8
- pixmap-in-deprecated-location: use explicit list.

* Sat Feb 06 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt7
- added exception for rpm-macros-packaging/prelink

* Fri Jan 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt6
- pixmap-in-deprecated-location: added exception

* Tue Jan 12 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt5
- added exception for rawstudio & warzone2100 (thanks to force@)

* Sat Jan 09 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt4
- added exception for control (thanks to ldv@).

* Sun Jan 03 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt3
- added noarch support for -macros-*

* Wed Nov 18 2009 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2
- pixmap-in-deprecated-location: added exception

* Fri Nov 13 2009 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- tex policy br: rpm-build-texmf test: warning level

* Thu Nov 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- tex policy br: rpm-build-texmf test

* Mon Nov 09 2009 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4
- fixed pixmap-in-deprecated-location thanks to wrar@.

* Sat Nov 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3
- fixed pixmap-in-deprecated-location thanks to Artem Zolochevskiy.

* Fri Oct 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- fixes in *-tex-obsolete-util-calls-in-post patchgen.

* Fri Oct 23 2009 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added 
  altlinux-policy-tex-obsolete-tetex-prefix.posttest
  altlinux-policy-tex-obsolete-util-calls-in-post.posttest

* Tue Sep 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- use posttests

* Thu Sep 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- added altlinux-policy-tex-buildreq-tetex.posttest

* Tue Sep 22 2009 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- added altlinux-policy-tex-obsolete-tetex.posttest

* Tue Apr 14 2009 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- added missing requires: repocop-collector-specfile

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- pixmap-in-deprecated-location fixscript tuning

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added pixmap-in-deprecated-location test

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added exception for known plugins in libdir.

* Thu Dec 25 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added tests for R:/BR: microsoft-fonts-ttf

* Tue Dec 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- fix in test altlinux-policy-shared-lib-contains-devel-so:
  added test that sonamed lib is a real file.
  (thanks to mithraen@ for report)

* Sat Dec 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added test altlinux-policy-shared-lib-contains-devel-so

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fixes in test pseudouser-added-as-real-user

* Sun Nov 30 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added test pseudouser-added-as-real-user 

* Sun Nov 23 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- _rpmmacrosdir support added

* Fri Nov 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- renamed to repocop-unittest-altlinux-policy
- added check and fixscript for %%perl_vendor_archlib packaging

* Mon Sep 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- refs to wiki.altlinux.org (#16724)

* Thu Jul 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- more verbose description in generated patch

* Thu Jul 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial version; note: added patch generator
