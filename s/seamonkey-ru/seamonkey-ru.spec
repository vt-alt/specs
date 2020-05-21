%define cid	langpack-ru@seamonkey.mozilla.org
%define ciddir	%sm_prefix/extensions/%cid

Name:		seamonkey-ru
Version:	2.53.2
Release:	alt1
Summary:	Russian (RU) Language Pack for Seamonkey

License:	MPL/NPL
Group:		Networking/WWW
URL:		http://mozilla-russia.org/products/seamonkey/
Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	seamonkey-%{version}.ru.langpack.xpi
Source1:	%name.watch

ExclusiveArch: %ix86 x86_64

Requires:	hunspell-ru
Requires:	seamonkey >= %version

BuildRequires(pre):	rpm-build-seamonkey
BuildRequires:		unzip

%description
The Mozilla Seamonkey Russian translation.

%prep
%setup -c -n %name-%version/%cid

%install
cd ..

mkdir -p %buildroot/%ciddir/dictionaries

cp -r %cid/* %buildroot/%ciddir
ln -s %_datadir/myspell/ru_RU.aff %buildroot/%ciddir/dictionaries/ru.aff
ln -s %_datadir/myspell/ru_RU.dic %buildroot/%ciddir/dictionaries/ru.dic

%files
%dir %sm_prefix
%dir %sm_prefix/extensions
%ciddir

%changelog
* Tue May 19 2020 Andrey Cherepanov <cas@altlinux.org> 2.53.2-alt1
- New version.

* Thu Apr 30 2020 Andrey Cherepanov <cas@altlinux.org> 2.53.2-alt0.1.b1
- New version (beta1).

* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 2.53.1-alt1
- New version.

* Mon Jul 30 2018 Michael Shigorin <mike@altlinux.org> 2.49.4-alt1
- New version

* Fri May 04 2018 Michael Shigorin <mike@altlinux.org> 2.49.3-alt1
- New version

* Wed Feb 21 2018 Michael Shigorin <mike@altlinux.org> 2.49.2-alt1
- New version

* Sun Nov 05 2017 Michael Shigorin <mike@altlinux.org> 2.49.1-alt1
- New version

* Mon Jul 31 2017 Michael Shigorin <mike@altlinux.org> 2.48-alt1
- New version

* Wed Dec 28 2016 Michael Shigorin <mike@altlinux.org> 2.46-alt1
- New version

* Sun Mar 20 2016 Michael Shigorin <mike@altlinux.org> 2.40-alt2
- Official release

* Sat Mar 05 2016 Michael Shigorin <mike@altlinux.org> 2.40-alt1
- New version

* Tue Nov 10 2015 Andrey Cherepanov <cas@altlinux.org> 2.39-alt1
- New version

* Wed Sep 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.38-alt1
- New version

* Fri Sep 04 2015 Andrey Cherepanov <cas@altlinux.org> 2.35-alt1
- New version

* Wed Mar 18 2015 Andrey Cherepanov <cas@altlinux.org> 2.33-alt1
- New version

* Sat Jan 24 2015 Andrey Cherepanov <cas@altlinux.org> 2.32-alt1
- New version

* Sun Dec 14 2014 Andrey Cherepanov <cas@altlinux.org> 2.31-alt1
- New version

* Thu Oct 23 2014 Andrey Cherepanov <cas@altlinux.org> 2.30-alt1
- New version

* Fri Sep 26 2014 Andrey Cherepanov <cas@altlinux.org> 2.29.1-alt1
- New version

* Wed Sep 10 2014 Andrey Cherepanov <cas@altlinux.org> 2.29-alt1
- New version

* Wed Jul 09 2014 Andrey Cherepanov <cas@altlinux.org> 2.26.1-alt1
- New version

* Thu May 22 2014 Andrey Cherepanov <cas@altlinux.org> 2.26-alt1
- New version

* Sun Mar 30 2014 Andrey Cherepanov <cas@altlinux.org> 2.25-alt1
- New version

* Thu Mar 06 2014 Andrey Cherepanov <cas@altlinux.org> 2.24-alt1
- New version

* Tue Feb 18 2014 Andrey Cherepanov <cas@altlinux.org> 2.23-alt1
- New version

* Wed Sep 25 2013 Andrey Cherepanov <cas@altlinux.org> 2.21-alt1
- Localization for version 2.21 of Seamonkey

* Thu Aug 08 2013 Andrey Cherepanov <cas@altlinux.org> 2.20-alt1
- Localization for version 2.20 of Seamonkey

* Thu Jul 11 2013 Andrey Cherepanov <cas@altlinux.org> 2.19-alt1
- Localization for new version 2.19 of Seamonkey

* Thu May 30 2013 Andrey Cherepanov <cas@altlinux.org> 2.17.1-alt1
- Localization for new version 2.17.1 of Seamonkey

* Tue Mar 05 2013 Andrey Cherepanov <cas@altlinux.org> 2.15.2-alt1
- Localization for new version 2.15.2 of Seamonkey

* Thu Feb 28 2013 Andrey Cherepanov <cas@altlinux.org> 2.15.2-alt0.M60P.1
- New version 2.15.2

* Tue Nov 13 2012 Radik Usupov <radik@altlinux.org> 2.13.2-alt0.M60P.1
- Backport to p6

* Wed Oct 31 2012 Radik Usupov <radik@altlinux.org> 2.13.2-alt1
- New version (2.13.2)

* Sun Feb 19 2012 Radik Usupov <radik@altlinux.org> 2.8-alt1
- New version (2.8b3)

* Thu Feb 09 2012 Radik Usupov <radik@altlinux.org> 2.7-alt1
- New version (2.7)

* Thu Nov 24 2011 Radik Usupov <radik@altlinux.org> 2.5-alt1
- New version (2.5)

* Sun Oct 02 2011 Radik Usupov <radik@altlinux.org> 2.4.1-alt1
- New version (2.4.1)

* Wed Sep 07 2011 Radik Usupov <radik@altlinux.org> 2.3.3-alt1
- New version (2.3.3)

* Fri Sep 02 2011 Radik Usupov <radik@altlinux.org> 2.3.2-alt1
- Rebuild from new version sm

* Mon Aug 29 2011 Radik Usupov <radik@altlinux.org> 2.3.1-alt1
- New version (2.3.1)

* Wed Aug 17 2011 Radik Usupov <radik@altlinux.org> 2.3-alt1
- New version (2.3)

* Wed Aug 03 2011 Radik Usupov <radik@altlinux.org> 2.2-alt1
- New version (2.2)

* Tue May 10 2011 Radik Usupov <radik@altlinux.org> 2.0.14-alt1
- New version (2.0.14)
- New packager

* Thu Jan 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.1-alt1
- Updated translation to 1.1
