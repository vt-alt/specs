%define ver_major 3.32

Name: gnome-user-docs
Version: %ver_major.3
Release: alt1

Summary: General GNOME User Documentation
License: %fdl
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

Obsoletes: gnome-users-guide
Provides: gnome-users-guide
Obsoletes: gnome2-user-docs
Provides: gnome2-user-docs

%define yelp_ver 3.18.0

BuildRequires: rpm-build-gnome rpm-build-licenses
BuildRequires: intltool yelp-tools >= %yelp_ver itstool xml-utils xsltproc xmllint

%description
This package contains general GNOME user documentation which is not
directly associated with any particular GNOME application or package.

%prep
%setup

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang gnome-help system-admin-guide

%files -f %name.lang
%doc README NEWS

%changelog
* Thu Jul 18 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.3-alt1
- 3.32.3

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Oct 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun May 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Dec 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2.1-alt1
- 3.26.2.1

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Wed Oct 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1.1-alt1
- 3.26.1.1

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Thu Sep 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0.1-alt1
- 3.26.0.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Fri Mar 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Feb 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.90-alt1
- 3.15.90

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Jun 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Fri Feb 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Jun 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu May 31 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0.1-alt1
- 3.2.0.1

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Mon Apr 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sat Apr 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Wed Dec 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Fri Nov 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Sat Mar 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sat Jan 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Mon Dec 15 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- removed obsolete %%{update,clean}_scrollkeeper

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Mon Apr 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Sat Nov 17 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt1
- new version (2.20.1)
- use a macro from rpm-build-licenses

* Sun Jul 15 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt1
- new version (2.18.2)
- spec cleanup

* Sat Oct 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version (2.16.1)

* Sun Sep 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.1-alt1
- new version (2.15.1)

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Mon Feb 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1.1-alt1
- new version (2.13.1.1)

* Fri Sep 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Thu Feb 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Mon Oct 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Mon Jan 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Wed Jan 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Wed Sep 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- First build for Sisyphus.
