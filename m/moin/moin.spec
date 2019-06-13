Summary: MoinMoin is a Python clone of WikiWiki
Name: moin
Version: 1.9.10
Release: alt1
License: GPL
Group: Networking/Other
Url: http://moinmo.in/
Source0: http://static.moinmo.in/files/%name-%version.tar.gz
Source1: moin-instance-setup.in
Packager: Fr. Br. George <george@altlinux.ru>
BuildArch: noarch

BuildRequires: python-devel

%define htdocs %_datadir/%name/htdocs

%add_findreq_skiplist %htdocs/applets/FCKeditor/*
%add_findreq_skiplist %_datadir/%name/server/*wsgi*.py
%add_python_req_skip _conv160b_wiki
%add_python_req_skip gdchart
%add_python_req_skip twisted
%add_python_req_skip xapian
%add_python_req_skip py
%add_python_req_skip MySQLdb
%add_python_req_skip win32service
%add_python_req_skip win32serviceutil

Requires: python-module-MoinMoin = %version python-module-moin-jabberbot = %version
Provides: MoinMoin

# TODO suggested modules

#/*G*/BuildRequires: hd2u

%description
A WikiWikiWeb is a collaborative hypertext environment, with an emphasis on
easy access to and modification of information. MoinMoin is a Python
WikiClone that allows you to easily set up your own wiki, only requiring a
Web server and a Python installation.

%package -n python-module-moin-jabberbot
Summary: Jabber robot used for MoinMoin notification
Group: Networking/Other

%description -n python-module-moin-jabberbot
Jabber robot used for MoinMoin notification

%package -n python-module-MoinMoin
Summary: Pyton modules for MoinMoin WikiWikiWeb engine
Group: Development/Python
Obsoletes: python-modules-MoinMoin

%description -n python-module-MoinMoin
Pyton module for MoinMoin WikiWikiWeb engine

%package instance-setup
Summary: Shellscript for deploing moin under Apache2
Group: Networking/Other
%description instance-setup
Shellscript for deploing moin under Apache2

%prep
%setup
sed -i 's@^STATIC_FILES_PATH = .*@STATIC_FILES_PATH = "%htdocs"@' MoinMoin/web/static/__init__.py

%build
sed 's|@HTDOCS@|%htdocs|' < %SOURCE1 > moin-instance-setup
python setup.py build

%install
mkdir -p %buildroot%_datadir/%name
python setup.py install --root=%buildroot
mkdir -p %buildroot/%_sbindir/
install -m755  moin-instance-setup %buildroot/%_sbindir/
rm -rf %buildroot%htdocs
cp -a MoinMoin/web/static/htdocs %buildroot%htdocs
ln -s config/wikiconfig.py %buildroot%_datadir/%name/wikiconfig.py
install wikiserver.py %buildroot%_datadir/%name/

%files
%doc README* docs/CHANGES* docs/INSTALL.html docs/README.migration
%doc docs/licenses/
%_bindir/*
%_datadir/%name/
%exclude %htdocs/*

%files -n python-module-moin-jabberbot
%python_sitelibdir/jabberbot

%files -n python-module-MoinMoin
%exclude %python_sitelibdir/MoinMoin/web/static/htdocs
%htdocs/*
%python_sitelibdir/MoinMoin
%python_sitelibdir/*.egg-info

%files instance-setup
%_sbindir/*

%changelog
* Wed May 22 2019 Fr. Br. George <george@altlinux.ru> 1.9.10-alt1
- Autobuild version bump to 1.9.10
- Separate Apache2 dependency

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.9.9-alt1.qa1
- NMU: applied repocop patch

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 1.9.9-alt1
- Autobuild version bump to 1.9.9

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 1.9.8-alt1
- Autobuild version bump to 1.9.8

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 1.9.7-alt1
- Autobuild version bump to 1.9.7

* Sun Dec 30 2012 Fr. Br. George <george@altlinux.ru> 1.9.6-alt1
- Autobuild version bump to 1.9.6

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 1.9.5-alt1
- Autobuild version bump to 1.9.5

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 1.9.4-alt1
- Autobuild version bump to 1.9.4

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.3-alt1.1
- Rebuild with Python-2.7

* Thu Sep 09 2010 Fr. Br. George <george@altlinux.ru> 1.9.3-alt1
- Version up

* Sat Mar 20 2010 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Version up
- HTDOCS moved to more reasonable location

* Mon Feb 08 2010 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Version up

* Mon Jan 04 2010 Fr. Br. George <george@altlinux.ru> 1.9.0-alt2
- Install script fixed
- htdocs moved from module path

* Sat Dec 19 2009 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Version up
Rebuild with python 2.6

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5-alt1.1
- Rebuilt with python 2.6

* Mon Sep 14 2009 Fr. Br. George <george@altlinux.ru> 1.8.5-alt1
- Version up

* Thu Jul 02 2009 Fr. Br. George <george@altlinux.ru> 1.8.4-alt1
- Version up (closes: #20411).

* Mon May 18 2009 Fr. Br. George <george@altlinux.ru> 1.8.3-alt1
- Version up
- Fixed: #19942

* Tue Feb 24 2009 Fr. Br. George <george@altlinux.ru> 1.8.2-alt1
- Version up
- Package naming improved

* Mon Nov 03 2008 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Version up

* Mon Sep 29 2008 Fr. Br. George <george@altlinux.ru> 1.7.2-alt2
- Unmets eliminated

* Thu Sep 25 2008 Fr. Br. George <george@altlinux.ru> 1.7.2-alt1
- Version up
- #12476 fixed
- #15214 fixed :)

* Sun Aug 03 2008 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Version up
- Switch back to CGI instead of mod_python

* Wed Jun 25 2008 Fr. Br. George <george@altlinux.ru> 1.7.0-alt1
- Version up
- New (simple, but usable) moin-instance-setup
- Patches removed
- Module files splitted

* Mon Nov 12 2007 Fr. Br. George <george@altlinux.ru> 1.6.0beta1-alt1
- Beta 1.6 version up

* Wed Jun 20 2007 Fr. Br. George <george@altlinux.ru> 1.5.8-alt2
- moin-instance-setup adapted for apache2
- dependency fixed

* Sun Jun 03 2007 Fr. Br. George <george@altlinux.ru> 1.5.8-alt1
- Fix CVE-2007-2423
- Version up

* Mon Mar 12 2007 Fr. Br. George <george@altlinux.ru> 1.5.7-alt1
- Version up (bugfixes)

* Thu Nov 02 2006 Fr. Br. George <george@altlinux.ru> 1.5.6-alt1
- Version up

* Wed Aug 30 2006 Fr. Br. George <george@altlinux.ru> 1.5.4-alt2
- moin-instance-setup adapted

* Sat Aug 26 2006 Fr. Br. George <george@altlinux.ru> 1.5.4-alt1
- Version up
- Provide moin-instance-setup for instance creation instead of just README
- Gear repository spec tuning (Packager: field etc.)

* Wed Jun 14 2006 Fr. Br. George <george@altlinux.ru> 1.5.3-alt1
- Version up

* Wed Mar 15 2006 Fr. Br. George <george@altlinux.ru> 1.5.2-alt1
- Initial ALT build

* Mon Feb  6 2006 Matthias Saou <http://freshrpms.net/> 1.5.2-1
- Update to 1.5.2.
- Update config patch.
- Update %%doc files.

* Sun Dec 18 2005 Tommy Reynolds <Tommy.Reynolds@MegaCoder.com> 1.3.5-3
- Remove extraneous '\' from XML output, so that <screen>..</screen>
  does not generate '\' 'n' outside of any markup.

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 1.3.5-2
- Fix python modules path from _libdir to _prefix/lib so that build works on
  64bit systems too.

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 1.3.5-1
- Update to 1.3.5.
- Update the config patch.
- Update %%doc section (many moved to docs/).

* Wed Jun 15 2005 Matthias Saou <http://freshrpms.net/> 1.3.4-1
- Update to 1.3.4.
- Update the config patch.
- Move the README.redhat file out from the patch and rename it to README-rpm.

* Tue Apr 19 2005 Matthias Saou <http://freshrpms.net/> 1.3.3-2
- Adapted for inclusion into Extras.
- Merge relevant bits from Jeff's pyvault version.

* Wed Dec 22 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.3.1

* Thu Dec 09 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.3.0

* Sun Nov 07 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- 1.3beta4

* Fri Aug 06 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.2.3

* Wed May 19 2004 - Kai.Puolamaki@iki.fi
- Fix also directory permissions...

* Mon May 17 2004 - Kai.Puolamaki@iki.fi
- Fix file permissions

* Fri May 14 2004 - Kai.Puolamaki@iki.fi
- 1.2.1
- Home build

