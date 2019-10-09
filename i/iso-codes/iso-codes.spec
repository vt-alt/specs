%def_enable check

Name: iso-codes
Version: 4.4
Release: alt1

Group: System/Internationalization
Summary: ISO code lists and translations
License: LGPL 2.1
Url: https://salsa.debian.org/iso-codes-team/iso-codes

# Cloned from https://salsa.debian.org/iso-codes-team/iso-codes.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: common-licenses python3-base

%description
This package provides several ISO standards:
 * ISO-639   language code list,
 * ISO-3166  territory code list, and ISO-3166-2 sub-territory lists,
 * ISO-4217  currency names and code elements,
 * ISO-15924 codes for the representation of names of scripts
and all their translations in gettext .po form.

%package devel
Summary: Files for development using %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package contains the pkg-config files for development
when building programs that use %name

%prep
%setup
ln -sf %_licensedir/LGPL-2.1 LICENSE

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang --all-name iso --output=%name.lang

%check
%make check

%files -f %name.lang
%doc ChangeLog.md README.md TODO
%doc --no-dereference LICENSE
%_datadir/xml/%name/
%_datadir/%name/json/

%files devel
%_datadir/pkgconfig/iso-codes.pc

%changelog
* Fri Oct 04 2019 Yuri N. Sedunov <aris@altlinux.org> 4.4-alt1
- 4.4

* Fri Jul 12 2019 Yuri N. Sedunov <aris@altlinux.org> 4.3-alt1
- 4.3

* Sat Jan 26 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- 4.1

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- 4.0

* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.79-alt1
- 3.79 (new urls)

* Fri Dec 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.77-alt1
- 3.77

* Fri Sep 22 2017 Yuri N. Sedunov <aris@altlinux.org> 3.76-alt1
- 3.76

* Fri Jun 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.75-alt1
- 3.75

* Sun Jan 22 2017 Yuri N. Sedunov <aris@altlinux.org> 3.74-alt1
- 3.74

* Wed Dec 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.72-alt1
- 3.72

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.71-alt1
- 3.71

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.69-alt1
- 3.69

* Sun Jun 05 2016 Yuri N. Sedunov <aris@altlinux.org> 3.68-alt1
- 3.68 (updated buildreqs, %files section)

* Sun Feb 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.65-alt1
- 3.65

* Wed Oct 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.62-alt1
- 3.62

* Thu Aug 06 2015 Yuri N. Sedunov <aris@altlinux.org> 3.60-alt1
- 3.60

* Sun Apr 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.57-alt1
- 3.57

* Wed Dec 11 2013 Vladimir Lettiev <crux@altlinux.ru> 3.49-alt1
- New version 3.49

* Tue Apr 09 2013 Vladimir Lettiev <crux@altlinux.ru> 3.41-alt1
- New version 3.41

* Wed Nov 07 2012 Vladimir Lettiev <crux@altlinux.ru> 3.40-alt1
- New version 3.40

* Mon Nov 28 2011 Vladimir Lettiev <crux@altlinux.ru> 3.30-alt1
- New version 3.30

* Thu Oct 20 2011 Vladimir Lettiev <crux@altlinux.ru> 3.29-alt1
- New version 3.29

* Sat Mar 05 2011 Vladimir Lettiev <crux@altlinux.ru> 3.24.2-alt1
- New version 3.24.2

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 3.23-alt1
- New version 3.23

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 3.22-alt1
- New version 3.22

* Fri Oct 01 2010 Vladimir Lettiev <crux@altlinux.ru> 3.21-alt1
- New version 3.21

* Sun Sep 05 2010 Vladimir Lettiev <crux@altlinux.ru> 3.20-alt1
- New version 3.20

* Mon Aug 02 2010 Vladimir Lettiev <crux@altlinux.ru> 3.19-alt1
- New version 3.19

* Tue Jun 29 2010 Vladimir Lettiev <crux@altlinux.ru> 3.17-alt1
- New version 3.17

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 3.16-alt1
- New version 3.16

* Sat Apr 17 2010 Vladimir Lettiev <crux@altlinux.ru> 3.15-alt1
- New version 3.15

* Thu Mar 04 2010 Vladimir Lettiev <crux@altlinux.ru> 3.14-alt1
- New version 3.14

* Fri Jan 22 2010 Vladimir Lettiev <crux@altlinux.ru> 3.12.1-alt1
- New version 3.12.1

* Tue Nov 03 2009 Vladimir Lettiev <crux@altlinux.ru> 3.11.1-alt1
- new version

* Tue Oct 27 2009 Vladimir Lettiev <crux@altlinux.ru> 3.11-alt1
- new version

* Mon Sep 07 2009 Vladimir Lettiev <crux@altlinux.ru> 3.10.3-alt1
- new version (closes: 20800)

* Wed Jun 17 2009 Vladimir Lettiev <crux@altlinux.ru> 3.10-alt1
- new version (closes: 16771)

* Sat May 02 2009 Vladimir Lettiev <crux@altlinux.ru> 3.9-alt1
- new version

* Sun Apr 12 2009 Vladimir Lettiev <crux@altlinux.ru> 3.8-alt1
- new version

* Fri Mar 07 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.9-alt1
- New version

* Sun Nov 12 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.58-alt1
- Update to Debian release 0.58-1
- Remove outdated russian translation, use original

* Sat Jun 24 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.51-alt1
- Updated to Debian release 0.51-1.1
- Patch0 is obsolete
- Patch1: updated Russian translation

* Mon Apr 17 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.49-alt2
- Patch0: set package version to 0.49 in configure.ac

* Mon Nov 21 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.49-alt1
- Updated to 0.49

* Sat Sep 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.47-alt1
- Ported to Sisyphus
- Spec cleanup
- Corrected license information

* Fri Aug 26 2005 Christopher Aillon <caillon@redhat.com> 0.47-1
- Update to 0.47

* Fri Jun 10 2005 Christopher Aillon <caillon@redhat.com> 0.46-2
- The .pc file should be installed in %%{_datadir} instead of %%{_libdir}
  since this is a noarch package.  64bit platforms will otherwise look in
  the 64bit version of the %%{_libdir} and not find the .pc file and
  cause them to not find iso-codes

* Fri Jun 10 2005 Christopher Aillon <caillon@redhat.com> 0.46-1
- Initial RPM
