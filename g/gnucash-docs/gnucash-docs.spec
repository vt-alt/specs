Name:    gnucash-docs
Version: 4.0
Release: alt1

Summary: Documentation for the Gnucash

Packager: Andrey Cherepanov <cas@altlinux.org>

License: GFDL
Group:   Office
Url:     http://www.gnucash.org

BuildArch: noarch

Requires: yelp

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

Source: http://prdownloads.sourceforge.net/gnucash/gnucash-docs/%version/%name-%version.tar

BuildRequires: scrollkeeper xsltproc

%description
GnuCash is a personal finance manager. A check-book like
register GUI allows you to enter and track bank accounts,
stocks, income and even currency trades. The interface is
designed to be simple and easy to use, but is backed with
double-entry accounting principles to ensure balanced books.
This is the documentation module for GnuCash.

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS COPYING-DOCS ChangeLog NEWS README HACKING
%_datadir/gnome/help/gnucash-*/
#%%_datadir/omf/gnucash-*/

%changelog
* Mon Jun 29 2020 Andrey Cherepanov <cas@altlinux.org> 4.0-alt1
- New version.

* Mon Jun 15 2020 Andrey Cherepanov <cas@altlinux.org> 3.905-alt1
- New version.

* Mon Jun 08 2020 Andrey Cherepanov <cas@altlinux.org> 3.904-alt1
- New version.

* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 3.903-alt1
- New version.

* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 3.901-alt1
- New version.

* Sun Apr 12 2020 Andrey Cherepanov <cas@altlinux.org> 3.10-alt1
- New version.

* Tue Apr 07 2020 Andrey Cherepanov <cas@altlinux.org> 3.9-alt1
- New version.

* Thu Mar 05 2020 Andrey Cherepanov <cas@altlinux.org> 3.8-alt1
- New version.

* Tue Sep 10 2019 Andrey Cherepanov <cas@altlinux.org> 3.7-alt1
- New version.

* Mon Jul 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.6-alt1
- New version.

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.5-alt1
- New version.

* Thu Jan 03 2019 Andrey Cherepanov <cas@altlinux.org> 3.4-alt1
- New version.

* Mon Oct 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1
- New version.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 2.6.20-alt1
- New version.

* Tue Dec 19 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.19-alt1
- New version.

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.18-alt1
- New version

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.17-alt1
- New version

* Sun Mar 26 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.16-alt1
- New version

* Wed Dec 21 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.15-alt1
- new version 2.6.15

* Thu Nov 10 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.14-alt1
- new version 2.6.14

* Sun Jul 10 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.13-alt1
- new version 2.6.13

* Sun Jan 17 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.11-alt1
- New version

* Sat Jan 02 2016 Andrey Cherepanov <cas@altlinux.org> 2.6.10-alt1
- New version

* Mon Oct 12 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.9-alt1
- New version

* Wed Sep 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.8-alt1
- New version

* Thu Apr 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.6-alt1
- New version

* Mon Jan 12 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.5-alt1
- New version
- Fix License

* Sat Oct 04 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.4-alt1
- New version

* Fri Apr 11 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.3-alt1
- New version

* Mon Mar 24 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version
- Build from upstream Git repository

* Thu Jan 30 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version

* Thu Jan 09 2014 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- new version

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-scrollkeeper-update for gnucash-docs
  * postclean-05-filetriggers for spec file

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)
- add yelp to requires

* Sat Dec 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt0.1
- new version, rewrote spec

* Sun Dec  4 2005 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt2
- update buildreq

* Thu Dec 16 2004 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- first separate package with gnucash documentation
