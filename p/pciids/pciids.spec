Name: pciids
Version: 20191007
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Repository of PCI IDs (pci.ids database)
License: GPLv2+ or BSD
Group: System/Libraries

Url: http://pciids.sourceforge.net
Source: %url/pci.ids
Patch: hwdatabase.ti24.patch

BuildArch: noarch

%description
This package contains a public list of all known IDs used in PCI devices: ID's
of vendors, devices, subsystems and device classes. It is used in various
programs to display full human-readable names instead of cryptic numeric codes.

%prep
%setup -c -T
cp %SOURCE0 .
%patch -p1

%build


%install
install -pD -m644 pci.ids %buildroot%_datadir/misc/pci.ids

%files
%_datadir/misc/pci.ids

%changelog
* Mon Oct 07 2019 Cronbuild Service <cronbuild@altlinux.org> 20191007-alt1
- repocop cronbuild 20191007. At your service.

* Mon Sep 30 2019 Cronbuild Service <cronbuild@altlinux.org> 20190930-alt1
- repocop cronbuild 20190930. At your service.

* Mon Sep 23 2019 Cronbuild Service <cronbuild@altlinux.org> 20190923-alt1
- repocop cronbuild 20190923. At your service.

* Mon Sep 16 2019 Cronbuild Service <cronbuild@altlinux.org> 20190916-alt1
- repocop cronbuild 20190916. At your service.

* Mon Sep 09 2019 Cronbuild Service <cronbuild@altlinux.org> 20190909-alt1
- repocop cronbuild 20190909. At your service.

* Mon Sep 02 2019 Cronbuild Service <cronbuild@altlinux.org> 20190902-alt1
- repocop cronbuild 20190902. At your service.

* Mon Aug 26 2019 Cronbuild Service <cronbuild@altlinux.org> 20190826-alt1
- repocop cronbuild 20190826. At your service.

* Mon Aug 12 2019 Cronbuild Service <cronbuild@altlinux.org> 20190812-alt1
- repocop cronbuild 20190812. At your service.

* Mon Aug 05 2019 Cronbuild Service <cronbuild@altlinux.org> 20190805-alt1
- repocop cronbuild 20190805. At your service.

* Mon Jul 29 2019 Cronbuild Service <cronbuild@altlinux.org> 20190729-alt1
- repocop cronbuild 20190729. At your service.

* Mon Jul 01 2019 Cronbuild Service <cronbuild@altlinux.org> 20190701-alt1
- repocop cronbuild 20190701. At your service.

* Mon Jun 24 2019 Cronbuild Service <cronbuild@altlinux.org> 20190624-alt1
- repocop cronbuild 20190624. At your service.

* Mon Jun 17 2019 Cronbuild Service <cronbuild@altlinux.org> 20190617-alt1
- repocop cronbuild 20190617. At your service.

* Mon Jun 10 2019 Cronbuild Service <cronbuild@altlinux.org> 20190610-alt1
- repocop cronbuild 20190610. At your service.

* Mon May 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190520-alt1
- repocop cronbuild 20190520. At your service.

* Mon May 06 2019 Cronbuild Service <cronbuild@altlinux.org> 20190506-alt1
- repocop cronbuild 20190506. At your service.

* Mon Apr 29 2019 Cronbuild Service <cronbuild@altlinux.org> 20190429-alt1
- repocop cronbuild 20190429. At your service.

* Mon Apr 22 2019 Cronbuild Service <cronbuild@altlinux.org> 20190422-alt1
- repocop cronbuild 20190422. At your service.

* Mon Apr 15 2019 Cronbuild Service <cronbuild@altlinux.org> 20190415-alt1
- repocop cronbuild 20190415. At your service.

* Mon Apr 08 2019 Cronbuild Service <cronbuild@altlinux.org> 20190408-alt1
- repocop cronbuild 20190408. At your service.

* Mon Apr 01 2019 Cronbuild Service <cronbuild@altlinux.org> 20190401-alt1
- repocop cronbuild 20190401. At your service.

* Mon Mar 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20190325-alt1
- repocop cronbuild 20190325. At your service.

* Mon Mar 18 2019 Cronbuild Service <cronbuild@altlinux.org> 20190318-alt1
- repocop cronbuild 20190318. At your service.

* Mon Mar 11 2019 Cronbuild Service <cronbuild@altlinux.org> 20190311-alt1
- repocop cronbuild 20190311. At your service.

* Mon Feb 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20190225-alt1
- repocop cronbuild 20190225. At your service.

* Mon Feb 18 2019 Cronbuild Service <cronbuild@altlinux.org> 20190218-alt1
- repocop cronbuild 20190218. At your service.

* Mon Feb 11 2019 Cronbuild Service <cronbuild@altlinux.org> 20190211-alt1
- repocop cronbuild 20190211. At your service.

* Mon Feb 04 2019 Cronbuild Service <cronbuild@altlinux.org> 20190204-alt1
- repocop cronbuild 20190204. At your service.

* Mon Jan 21 2019 Cronbuild Service <cronbuild@altlinux.org> 20190121-alt1
- repocop cronbuild 20190121. At your service.

* Mon Jan 14 2019 Cronbuild Service <cronbuild@altlinux.org> 20190114-alt1
- repocop cronbuild 20190114. At your service.

* Mon Jan 07 2019 Cronbuild Service <cronbuild@altlinux.org> 20190107-alt1
- repocop cronbuild 20190107. At your service.

* Mon Dec 31 2018 Cronbuild Service <cronbuild@altlinux.org> 20181231-alt1
- repocop cronbuild 20181231. At your service.

* Mon Dec 24 2018 Cronbuild Service <cronbuild@altlinux.org> 20181224-alt1
- repocop cronbuild 20181224. At your service.

* Mon Dec 17 2018 Cronbuild Service <cronbuild@altlinux.org> 20181217-alt1
- repocop cronbuild 20181217. At your service.

* Mon Dec 03 2018 Cronbuild Service <cronbuild@altlinux.org> 20181203-alt1
- repocop cronbuild 20181203. At your service.

* Mon Nov 26 2018 Cronbuild Service <cronbuild@altlinux.org> 20181126-alt1
- repocop cronbuild 20181126. At your service.

* Mon Nov 19 2018 Cronbuild Service <cronbuild@altlinux.org> 20181119-alt1
- repocop cronbuild 20181119. At your service.

* Mon Nov 12 2018 Cronbuild Service <cronbuild@altlinux.org> 20181112-alt1
- repocop cronbuild 20181112. At your service.

* Mon Nov 05 2018 Cronbuild Service <cronbuild@altlinux.org> 20181105-alt1
- repocop cronbuild 20181105. At your service.

* Mon Oct 29 2018 Cronbuild Service <cronbuild@altlinux.org> 20181029-alt1
- repocop cronbuild 20181029. At your service.

* Mon Oct 22 2018 Cronbuild Service <cronbuild@altlinux.org> 20181022-alt1
- repocop cronbuild 20181022. At your service.

* Mon Oct 15 2018 Cronbuild Service <cronbuild@altlinux.org> 20181015-alt1
- repocop cronbuild 20181015. At your service.

* Mon Oct 08 2018 Cronbuild Service <cronbuild@altlinux.org> 20181008-alt1
- repocop cronbuild 20181008. At your service.

* Mon Oct 01 2018 Cronbuild Service <cronbuild@altlinux.org> 20181001-alt1
- repocop cronbuild 20181001. At your service.

* Mon Sep 24 2018 Cronbuild Service <cronbuild@altlinux.org> 20180924-alt1
- repocop cronbuild 20180924. At your service.

* Mon Sep 17 2018 Cronbuild Service <cronbuild@altlinux.org> 20180917-alt1
- repocop cronbuild 20180917. At your service.

* Mon Sep 10 2018 Cronbuild Service <cronbuild@altlinux.org> 20180910-alt1
- repocop cronbuild 20180910. At your service.

* Mon Sep 03 2018 Cronbuild Service <cronbuild@altlinux.org> 20180903-alt1
- repocop cronbuild 20180903. At your service.

* Mon Aug 20 2018 Cronbuild Service <cronbuild@altlinux.org> 20180820-alt1
- repocop cronbuild 20180820. At your service.

* Mon Aug 13 2018 Cronbuild Service <cronbuild@altlinux.org> 20180813-alt1
- repocop cronbuild 20180813. At your service.

* Mon Jul 23 2018 Cronbuild Service <cronbuild@altlinux.org> 20180723-alt1
- repocop cronbuild 20180723. At your service.

* Sun Jul 01 2018 Cronbuild Service <cronbuild@altlinux.org> 20180701-alt1
- repocop cronbuild 20180701. At your service.

* Sun Jun 24 2018 Cronbuild Service <cronbuild@altlinux.org> 20180624-alt1
- repocop cronbuild 20180624. At your service.

* Sun Jun 17 2018 Cronbuild Service <cronbuild@altlinux.org> 20180617-alt1
- repocop cronbuild 20180617. At your service.

* Sun Jun 10 2018 Cronbuild Service <cronbuild@altlinux.org> 20180610-alt1
- repocop cronbuild 20180610. At your service.

* Sun May 27 2018 Cronbuild Service <cronbuild@altlinux.org> 20180527-alt1
- repocop cronbuild 20180527. At your service.

* Sun May 20 2018 Cronbuild Service <cronbuild@altlinux.org> 20180520-alt1
- repocop cronbuild 20180520. At your service.

* Sun Apr 29 2018 Cronbuild Service <cronbuild@altlinux.org> 20180429-alt1
- repocop cronbuild 20180429. At your service.

* Sun Apr 08 2018 Cronbuild Service <cronbuild@altlinux.org> 20180408-alt1
- repocop cronbuild 20180408. At your service.

* Sun Apr 01 2018 Cronbuild Service <cronbuild@altlinux.org> 20180401-alt1
- repocop cronbuild 20180401. At your service.

* Sun Mar 25 2018 Cronbuild Service <cronbuild@altlinux.org> 20180325-alt1
- repocop cronbuild 20180325. At your service.

* Sun Mar 18 2018 Cronbuild Service <cronbuild@altlinux.org> 20180318-alt1
- repocop cronbuild 20180318. At your service.

* Sun Mar 11 2018 Cronbuild Service <cronbuild@altlinux.org> 20180311-alt1
- repocop cronbuild 20180311. At your service.

* Sun Mar 04 2018 Cronbuild Service <cronbuild@altlinux.org> 20180304-alt1
- repocop cronbuild 20180304. At your service.

* Mon Feb 12 2018 Cronbuild Service <cronbuild@altlinux.org> 20180212-alt1
- repocop cronbuild 20180212. At your service.

* Thu Jan 18 2018 Cronbuild Service <cronbuild@altlinux.org> 20180118-alt1
- repocop cronbuild 20180118. At your service.

* Thu Jan 11 2018 Cronbuild Service <cronbuild@altlinux.org> 20180111-alt1
- repocop cronbuild 20180111. At your service.

* Thu Dec 21 2017 Cronbuild Service <cronbuild@altlinux.org> 20171221-alt1
- repocop cronbuild 20171221. At your service.

* Thu Dec 07 2017 Cronbuild Service <cronbuild@altlinux.org> 20171207-alt1
- repocop cronbuild 20171207. At your service.

* Tue Oct 24 2017 Cronbuild Service <cronbuild@altlinux.org> 20171024-alt1
- repocop cronbuild 20171024. At your service.

* Sat Oct 14 2017 Cronbuild Service <cronbuild@altlinux.org> 20171014-alt1
- repocop cronbuild 20171014. At your service.

* Sat Oct 07 2017 Cronbuild Service <cronbuild@altlinux.org> 20171007-alt1
- repocop cronbuild 20171007. At your service.

* Sat Sep 30 2017 Cronbuild Service <cronbuild@altlinux.org> 20170930-alt1
- repocop cronbuild 20170930. At your service.

* Sat Sep 23 2017 Cronbuild Service <cronbuild@altlinux.org> 20170923-alt1
- repocop cronbuild 20170923. At your service.

* Sat Sep 16 2017 Cronbuild Service <cronbuild@altlinux.org> 20170916-alt1
- repocop cronbuild 20170916. At your service.

* Sat Sep 02 2017 Cronbuild Service <cronbuild@altlinux.org> 20170902-alt1
- repocop cronbuild 20170902. At your service.

* Sat Aug 26 2017 Cronbuild Service <cronbuild@altlinux.org> 20170826-alt1
- repocop cronbuild 20170826. At your service.

* Sat Aug 12 2017 Cronbuild Service <cronbuild@altlinux.org> 20170812-alt1
- repocop cronbuild 20170812. At your service.

* Sat Jul 29 2017 Cronbuild Service <cronbuild@altlinux.org> 20170729-alt1
- repocop cronbuild 20170729. At your service.

* Sat Jul 15 2017 Cronbuild Service <cronbuild@altlinux.org> 20170715-alt1
- repocop cronbuild 20170715. At your service.

* Sat Jul 01 2017 Cronbuild Service <cronbuild@altlinux.org> 20170701-alt1
- repocop cronbuild 20170701. At your service.

* Sat Jun 24 2017 Cronbuild Service <cronbuild@altlinux.org> 20170624-alt1
- repocop cronbuild 20170624. At your service.

* Sat May 27 2017 Cronbuild Service <cronbuild@altlinux.org> 20170527-alt1
- repocop cronbuild 20170527. At your service.

* Sat Apr 29 2017 Cronbuild Service <cronbuild@altlinux.org> 20170429-alt1
- repocop cronbuild 20170429. At your service.

* Sat Apr 22 2017 Cronbuild Service <cronbuild@altlinux.org> 20170422-alt1
- repocop cronbuild 20170422. At your service.

* Sat Apr 08 2017 Cronbuild Service <cronbuild@altlinux.org> 20170408-alt1
- repocop cronbuild 20170408. At your service.

* Sat Mar 18 2017 Cronbuild Service <cronbuild@altlinux.org> 20170318-alt1
- repocop cronbuild 20170318. At your service.

* Sat Mar 11 2017 Cronbuild Service <cronbuild@altlinux.org> 20170311-alt1
- repocop cronbuild 20170311. At your service.

* Sat Mar 04 2017 Cronbuild Service <cronbuild@altlinux.org> 20170304-alt1
- repocop cronbuild 20170304. At your service.

* Sat Feb 18 2017 Cronbuild Service <cronbuild@altlinux.org> 20170218-alt1
- repocop cronbuild 20170218. At your service.

* Sat Feb 11 2017 Cronbuild Service <cronbuild@altlinux.org> 20170211-alt1
- repocop cronbuild 20170211. At your service.

* Sat Jan 28 2017 Cronbuild Service <cronbuild@altlinux.org> 20170128-alt1
- repocop cronbuild 20170128. At your service.

* Sat Jan 14 2017 Cronbuild Service <cronbuild@altlinux.org> 20170114-alt1
- repocop cronbuild 20170114. At your service.

* Sat Jan 07 2017 Cronbuild Service <cronbuild@altlinux.org> 20170107-alt1
- repocop cronbuild 20170107. At your service.

* Sat Dec 31 2016 Cronbuild Service <cronbuild@altlinux.org> 20161231-alt1
- repocop cronbuild 20161231. At your service.

* Sat Dec 24 2016 Cronbuild Service <cronbuild@altlinux.org> 20161224-alt1
- repocop cronbuild 20161224. At your service.

* Sat Dec 17 2016 Cronbuild Service <cronbuild@altlinux.org> 20161217-alt1
- repocop cronbuild 20161217. At your service.

* Sat Nov 26 2016 Cronbuild Service <cronbuild@altlinux.org> 20161126-alt1
- repocop cronbuild 20161126. At your service.

* Sat Nov 19 2016 Cronbuild Service <cronbuild@altlinux.org> 20161119-alt1
- repocop cronbuild 20161119. At your service.

* Sat Oct 29 2016 Cronbuild Service <cronbuild@altlinux.org> 20161029-alt1
- repocop cronbuild 20161029. At your service.

* Sat Oct 22 2016 Cronbuild Service <cronbuild@altlinux.org> 20161022-alt1
- repocop cronbuild 20161022. At your service.

* Sat Oct 15 2016 Cronbuild Service <cronbuild@altlinux.org> 20161015-alt1
- repocop cronbuild 20161015. At your service.

* Sat Oct 08 2016 Cronbuild Service <cronbuild@altlinux.org> 20161008-alt1
- repocop cronbuild 20161008. At your service.

* Sat Oct 01 2016 Cronbuild Service <cronbuild@altlinux.org> 20161001-alt1
- repocop cronbuild 20161001. At your service.

* Sat Sep 24 2016 Cronbuild Service <cronbuild@altlinux.org> 20160924-alt1
- repocop cronbuild 20160924. At your service.

* Sat Sep 17 2016 Cronbuild Service <cronbuild@altlinux.org> 20160917-alt1
- repocop cronbuild 20160917. At your service.

* Sat Sep 10 2016 Cronbuild Service <cronbuild@altlinux.org> 20160910-alt1
- repocop cronbuild 20160910. At your service.

* Sat Sep 03 2016 Cronbuild Service <cronbuild@altlinux.org> 20160903-alt1
- repocop cronbuild 20160903. At your service.

* Sat Aug 27 2016 Cronbuild Service <cronbuild@altlinux.org> 20160827-alt1
- repocop cronbuild 20160827. At your service.

* Sat Aug 20 2016 Cronbuild Service <cronbuild@altlinux.org> 20160820-alt1
- repocop cronbuild 20160820. At your service.

* Sat Aug 06 2016 Cronbuild Service <cronbuild@altlinux.org> 20160806-alt1
- repocop cronbuild 20160806. At your service.

* Sat Jul 23 2016 Cronbuild Service <cronbuild@altlinux.org> 20160723-alt1
- repocop cronbuild 20160723. At your service.

* Sat Jul 16 2016 Cronbuild Service <cronbuild@altlinux.org> 20160716-alt1
- repocop cronbuild 20160716. At your service.

* Sat Jul 02 2016 Cronbuild Service <cronbuild@altlinux.org> 20160702-alt1
- repocop cronbuild 20160702. At your service.

* Sat Jun 25 2016 Cronbuild Service <cronbuild@altlinux.org> 20160625-alt1
- repocop cronbuild 20160625. At your service.

* Sat Jun 11 2016 Cronbuild Service <cronbuild@altlinux.org> 20160611-alt1
- repocop cronbuild 20160611. At your service.

* Sat Jun 04 2016 Cronbuild Service <cronbuild@altlinux.org> 20160604-alt1
- repocop cronbuild 20160604. At your service.

* Sat May 28 2016 Cronbuild Service <cronbuild@altlinux.org> 20160528-alt1
- repocop cronbuild 20160528. At your service.

* Wed May 11 2016 Cronbuild Service <cronbuild@altlinux.org> 20160511-alt1
- repocop cronbuild 20160511. At your service.

* Wed May 04 2016 Cronbuild Service <cronbuild@altlinux.org> 20160504-alt1
- repocop cronbuild 20160504. At your service.

* Wed Apr 27 2016 Cronbuild Service <cronbuild@altlinux.org> 20160427-alt1
- repocop cronbuild 20160427. At your service.

* Wed Apr 20 2016 Cronbuild Service <cronbuild@altlinux.org> 20160420-alt1
- repocop cronbuild 20160420. At your service.

* Wed Apr 13 2016 Cronbuild Service <cronbuild@altlinux.org> 20160413-alt1
- repocop cronbuild 20160413. At your service.

* Wed Apr 06 2016 Cronbuild Service <cronbuild@altlinux.org> 20160406-alt1
- repocop cronbuild 20160406. At your service.

* Wed Mar 30 2016 Cronbuild Service <cronbuild@altlinux.org> 20160330-alt1
- repocop cronbuild 20160330. At your service.

* Mon Feb 29 2016 Cronbuild Service <cronbuild@altlinux.org> 20160229-alt1
- repocop cronbuild 20160229. At your service.

* Mon Feb 22 2016 Cronbuild Service <cronbuild@altlinux.org> 20160222-alt1
- repocop cronbuild 20160222. At your service.

* Mon Feb 15 2016 Cronbuild Service <cronbuild@altlinux.org> 20160215-alt1
- repocop cronbuild 20160215. At your service.

* Sat Feb 06 2016 Cronbuild Service <cronbuild@altlinux.org> 20160206-alt1
- repocop cronbuild 20160206. At your service.

* Sat Jan 30 2016 Cronbuild Service <cronbuild@altlinux.org> 20160130-alt1
- repocop cronbuild 20160130. At your service.

* Sat Jan 23 2016 Cronbuild Service <cronbuild@altlinux.org> 20160123-alt1
- repocop cronbuild 20160123. At your service.

* Mon Jan 11 2016 Cronbuild Service <cronbuild@altlinux.org> 20160111-alt1
- repocop cronbuild 20160111. At your service.

* Mon Jan 04 2016 Cronbuild Service <cronbuild@altlinux.org> 20160104-alt1
- repocop cronbuild 20160104. At your service.

* Thu Dec 24 2015 Cronbuild Service <cronbuild@altlinux.org> 20151224-alt1
- repocop cronbuild 20151224. At your service.

* Sat Dec 12 2015 Cronbuild Service <cronbuild@altlinux.org> 20151212-alt1
- repocop cronbuild 20151212. At your service.

* Sat Dec 05 2015 Cronbuild Service <cronbuild@altlinux.org> 20151205-alt1
- repocop cronbuild 20151205. At your service.

* Sat Nov 28 2015 Cronbuild Service <cronbuild@altlinux.org> 20151128-alt1
- repocop cronbuild 20151128. At your service.

* Sat Nov 21 2015 Cronbuild Service <cronbuild@altlinux.org> 20151121-alt1
- repocop cronbuild 20151121. At your service.

* Sat Nov 14 2015 Cronbuild Service <cronbuild@altlinux.org> 20151114-alt1
- repocop cronbuild 20151114. At your service.

* Sat Nov 07 2015 Cronbuild Service <cronbuild@altlinux.org> 20151107-alt1
- repocop cronbuild 20151107. At your service.

* Sat Oct 31 2015 Cronbuild Service <cronbuild@altlinux.org> 20151031-alt1
- repocop cronbuild 20151031. At your service.

* Sat Oct 24 2015 Cronbuild Service <cronbuild@altlinux.org> 20151024-alt1
- repocop cronbuild 20151024. At your service.

* Sat Oct 17 2015 Cronbuild Service <cronbuild@altlinux.org> 20151017-alt1
- repocop cronbuild 20151017. At your service.

* Sat Oct 10 2015 Cronbuild Service <cronbuild@altlinux.org> 20151010-alt1
- repocop cronbuild 20151010. At your service.

* Sat Oct 03 2015 Cronbuild Service <cronbuild@altlinux.org> 20151003-alt1
- repocop cronbuild 20151003. At your service.

* Sat Sep 26 2015 Cronbuild Service <cronbuild@altlinux.org> 20150926-alt1
- repocop cronbuild 20150926. At your service.

* Sat Sep 19 2015 Cronbuild Service <cronbuild@altlinux.org> 20150919-alt1
- repocop cronbuild 20150919. At your service.

* Sat Sep 12 2015 Cronbuild Service <cronbuild@altlinux.org> 20150912-alt1
- repocop cronbuild 20150912. At your service.

* Sat Sep 05 2015 Cronbuild Service <cronbuild@altlinux.org> 20150905-alt1
- repocop cronbuild 20150905. At your service.

* Sat Aug 29 2015 Cronbuild Service <cronbuild@altlinux.org> 20150829-alt1
- repocop cronbuild 20150829. At your service.

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 20150823-alt1
- repocop cronbuild 20150823. At your service.

* Wed Jul 29 2015 Cronbuild Service <cronbuild@altlinux.org> 20150729-alt1
- repocop cronbuild 20150729. At your service.

* Wed Jul 15 2015 Cronbuild Service <cronbuild@altlinux.org> 20150715-alt1
- repocop cronbuild 20150715. At your service.

* Wed Jul 08 2015 Cronbuild Service <cronbuild@altlinux.org> 20150708-alt1
- repocop cronbuild 20150708. At your service.

* Wed Jul 01 2015 Cronbuild Service <cronbuild@altlinux.org> 20150701-alt1
- repocop cronbuild 20150701. At your service.

* Wed Jun 24 2015 Cronbuild Service <cronbuild@altlinux.org> 20150624-alt1
- repocop cronbuild 20150624. At your service.

* Wed Jun 17 2015 Cronbuild Service <cronbuild@altlinux.org> 20150617-alt1
- repocop cronbuild 20150617. At your service.

* Wed Jun 10 2015 Cronbuild Service <cronbuild@altlinux.org> 20150610-alt1
- repocop cronbuild 20150610. At your service.

* Wed Jun 03 2015 Cronbuild Service <cronbuild@altlinux.org> 20150603-alt1
- repocop cronbuild 20150603. At your service.

* Thu May 21 2015 Cronbuild Service <cronbuild@altlinux.org> 20150521-alt1
- repocop cronbuild 20150521. At your service.

* Thu May 14 2015 Cronbuild Service <cronbuild@altlinux.org> 20150514-alt1
- repocop cronbuild 20150514. At your service.

* Thu May 07 2015 Cronbuild Service <cronbuild@altlinux.org> 20150507-alt1
- repocop cronbuild 20150507. At your service.

* Thu Apr 30 2015 Cronbuild Service <cronbuild@altlinux.org> 20150430-alt1
- repocop cronbuild 20150430. At your service.

* Thu Apr 23 2015 Cronbuild Service <cronbuild@altlinux.org> 20150423-alt1
- repocop cronbuild 20150423. At your service.

* Thu Apr 16 2015 Cronbuild Service <cronbuild@altlinux.org> 20150416-alt1
- repocop cronbuild 20150416. At your service.

* Thu Apr 09 2015 Cronbuild Service <cronbuild@altlinux.org> 20150409-alt1
- repocop cronbuild 20150409. At your service.

* Thu Apr 02 2015 Cronbuild Service <cronbuild@altlinux.org> 20150402-alt1
- repocop cronbuild 20150402. At your service.

* Thu Mar 26 2015 Cronbuild Service <cronbuild@altlinux.org> 20150326-alt1
- repocop cronbuild 20150326. At your service.

* Thu Mar 19 2015 Cronbuild Service <cronbuild@altlinux.org> 20150319-alt1
- repocop cronbuild 20150319. At your service.

* Thu Mar 12 2015 Cronbuild Service <cronbuild@altlinux.org> 20150312-alt1
- repocop cronbuild 20150312. At your service.

* Thu Mar 05 2015 Cronbuild Service <cronbuild@altlinux.org> 20150305-alt1
- repocop cronbuild 20150305. At your service.

* Thu Feb 26 2015 Cronbuild Service <cronbuild@altlinux.org> 20150226-alt1
- repocop cronbuild 20150226. At your service.

* Thu Feb 19 2015 Cronbuild Service <cronbuild@altlinux.org> 20150219-alt1
- repocop cronbuild 20150219. At your service.

* Thu Feb 12 2015 Cronbuild Service <cronbuild@altlinux.org> 20150212-alt1
- repocop cronbuild 20150212. At your service.

* Thu Feb 05 2015 Cronbuild Service <cronbuild@altlinux.org> 20150205-alt1
- repocop cronbuild 20150205. At your service.

* Thu Jan 29 2015 Cronbuild Service <cronbuild@altlinux.org> 20150129-alt1
- repocop cronbuild 20150129. At your service.

* Thu Jan 22 2015 Cronbuild Service <cronbuild@altlinux.org> 20150122-alt1
- repocop cronbuild 20150122. At your service.

* Thu Jan 08 2015 Cronbuild Service <cronbuild@altlinux.org> 20150108-alt1
- repocop cronbuild 20150108. At your service.

* Thu Jan 01 2015 Cronbuild Service <cronbuild@altlinux.org> 20150101-alt1
- repocop cronbuild 20150101. At your service.

* Thu Dec 25 2014 Cronbuild Service <cronbuild@altlinux.org> 20141225-alt1
- repocop cronbuild 20141225. At your service.

* Thu Dec 18 2014 Cronbuild Service <cronbuild@altlinux.org> 20141218-alt1
- repocop cronbuild 20141218. At your service.

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 20141211-alt1
- repocop cronbuild 20141211. At your service.

* Thu Nov 27 2014 Cronbuild Service <cronbuild@altlinux.org> 20141127-alt1
- repocop cronbuild 20141127. At your service.

* Thu Nov 20 2014 Cronbuild Service <cronbuild@altlinux.org> 20141120-alt1
- repocop cronbuild 20141120. At your service.

* Thu Nov 13 2014 Cronbuild Service <cronbuild@altlinux.org> 20141113-alt1
- repocop cronbuild 20141113. At your service.

* Thu Nov 06 2014 Cronbuild Service <cronbuild@altlinux.org> 20141106-alt1
- repocop cronbuild 20141106. At your service.

* Thu Oct 30 2014 Cronbuild Service <cronbuild@altlinux.org> 20141030-alt1
- repocop cronbuild 20141030. At your service.

* Thu Oct 23 2014 Cronbuild Service <cronbuild@altlinux.org> 20141023-alt1
- repocop cronbuild 20141023. At your service.

* Thu Oct 16 2014 Cronbuild Service <cronbuild@altlinux.org> 20141016-alt1
- repocop cronbuild 20141016. At your service.

* Thu Oct 09 2014 Cronbuild Service <cronbuild@altlinux.org> 20141009-alt1
- repocop cronbuild 20141009. At your service.

* Thu Oct 02 2014 Cronbuild Service <cronbuild@altlinux.org> 20141002-alt1
- repocop cronbuild 20141002. At your service.

* Thu Sep 25 2014 Cronbuild Service <cronbuild@altlinux.org> 20140925-alt1
- repocop cronbuild 20140925. At your service.

* Thu Sep 18 2014 Cronbuild Service <cronbuild@altlinux.org> 20140918-alt1
- repocop cronbuild 20140918. At your service.

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 20140911-alt1
- repocop cronbuild 20140911. At your service.

* Thu Jul 03 2014 Cronbuild Service <cronbuild@altlinux.org> 20140703-alt1
- repocop cronbuild 20140703. At your service.

* Thu Jun 26 2014 Cronbuild Service <cronbuild@altlinux.org> 20140626-alt1
- repocop cronbuild 20140626. At your service.

* Thu Jun 19 2014 Cronbuild Service <cronbuild@altlinux.org> 20140619-alt1
- repocop cronbuild 20140619. At your service.

* Thu Jun 12 2014 Cronbuild Service <cronbuild@altlinux.org> 20140612-alt1
- repocop cronbuild 20140612. At your service.

* Thu Jun 05 2014 Cronbuild Service <cronbuild@altlinux.org> 20140605-alt1
- repocop cronbuild 20140605. At your service.

* Thu May 29 2014 Cronbuild Service <cronbuild@altlinux.org> 20140529-alt1
- repocop cronbuild 20140529. At your service.

* Thu May 22 2014 Cronbuild Service <cronbuild@altlinux.org> 20140522-alt1
- repocop cronbuild 20140522. At your service.

* Thu May 15 2014 Cronbuild Service <cronbuild@altlinux.org> 20140515-alt1
- repocop cronbuild 20140515. At your service.

* Thu May 08 2014 Cronbuild Service <cronbuild@altlinux.org> 20140508-alt1
- repocop cronbuild 20140508. At your service.

* Thu May 01 2014 Cronbuild Service <cronbuild@altlinux.org> 20140501-alt1
- repocop cronbuild 20140501. At your service.

* Thu Apr 24 2014 Cronbuild Service <cronbuild@altlinux.org> 20140424-alt1
- repocop cronbuild 20140424. At your service.

* Thu Apr 17 2014 Cronbuild Service <cronbuild@altlinux.org> 20140417-alt1
- repocop cronbuild 20140417. At your service.

* Thu Apr 10 2014 Cronbuild Service <cronbuild@altlinux.org> 20140410-alt1
- repocop cronbuild 20140410. At your service.

* Thu Apr 03 2014 Cronbuild Service <cronbuild@altlinux.org> 20140403-alt1
- repocop cronbuild 20140403. At your service.

* Thu Mar 27 2014 Cronbuild Service <cronbuild@altlinux.org> 20140327-alt1
- repocop cronbuild 20140327. At your service.

* Thu Mar 20 2014 Cronbuild Service <cronbuild@altlinux.org> 20140320-alt1
- repocop cronbuild 20140320. At your service.

* Thu Mar 13 2014 Cronbuild Service <cronbuild@altlinux.org> 20140313-alt1
- repocop cronbuild 20140313. At your service.

* Thu Mar 06 2014 Cronbuild Service <cronbuild@altlinux.org> 20140306-alt1
- repocop cronbuild 20140306. At your service.

* Thu Feb 27 2014 Cronbuild Service <cronbuild@altlinux.org> 20140227-alt1
- repocop cronbuild 20140227. At your service.

* Thu Feb 20 2014 Cronbuild Service <cronbuild@altlinux.org> 20140220-alt1
- repocop cronbuild 20140220. At your service.

* Thu Feb 13 2014 Cronbuild Service <cronbuild@altlinux.org> 20140213-alt1
- repocop cronbuild 20140213. At your service.

* Thu Feb 06 2014 Cronbuild Service <cronbuild@altlinux.org> 20140206-alt1
- repocop cronbuild 20140206. At your service.

* Thu Jan 30 2014 Cronbuild Service <cronbuild@altlinux.org> 20140130-alt1
- repocop cronbuild 20140130. At your service.

* Thu Jan 23 2014 Cronbuild Service <cronbuild@altlinux.org> 20140123-alt1
- repocop cronbuild 20140123. At your service.

* Thu Jan 16 2014 Cronbuild Service <cronbuild@altlinux.org> 20140116-alt1
- repocop cronbuild 20140116. At your service.

* Thu Jan 09 2014 Cronbuild Service <cronbuild@altlinux.org> 20140109-alt1
- repocop cronbuild 20140109. At your service.

* Thu Jan 02 2014 Cronbuild Service <cronbuild@altlinux.org> 20140102-alt1
- repocop cronbuild 20140102. At your service.

* Thu Dec 26 2013 Cronbuild Service <cronbuild@altlinux.org> 20131226-alt1
- repocop cronbuild 20131226. At your service.

* Thu Dec 12 2013 Cronbuild Service <cronbuild@altlinux.org> 20131212-alt1
- repocop cronbuild 20131212. At your service.

* Thu Dec 05 2013 Cronbuild Service <cronbuild@altlinux.org> 20131205-alt1
- repocop cronbuild 20131205. At your service.

* Thu Nov 28 2013 Cronbuild Service <cronbuild@altlinux.org> 20131128-alt1
- repocop cronbuild 20131128. At your service.

* Thu Nov 21 2013 Cronbuild Service <cronbuild@altlinux.org> 20131121-alt1
- repocop cronbuild 20131121. At your service.

* Thu Nov 14 2013 Cronbuild Service <cronbuild@altlinux.org> 20131114-alt1
- repocop cronbuild 20131114. At your service.

* Thu Nov 07 2013 Cronbuild Service <cronbuild@altlinux.org> 20131107-alt1
- repocop cronbuild 20131107. At your service.

* Thu Oct 31 2013 Cronbuild Service <cronbuild@altlinux.org> 20131031-alt1
- repocop cronbuild 20131031. At your service.

* Thu Oct 24 2013 Cronbuild Service <cronbuild@altlinux.org> 20131024-alt1
- repocop cronbuild 20131024. At your service.

* Thu Oct 17 2013 Cronbuild Service <cronbuild@altlinux.org> 20131017-alt1
- repocop cronbuild 20131017. At your service.

* Thu Oct 10 2013 Cronbuild Service <cronbuild@altlinux.org> 20131010-alt1
- repocop cronbuild 20131010. At your service.

* Thu Oct 03 2013 Cronbuild Service <cronbuild@altlinux.org> 20131003-alt1
- repocop cronbuild 20131003. At your service.

* Thu Sep 26 2013 Cronbuild Service <cronbuild@altlinux.org> 20130926-alt1
- repocop cronbuild 20130926. At your service.

* Thu Sep 19 2013 Cronbuild Service <cronbuild@altlinux.org> 20130919-alt1
- repocop cronbuild 20130919. At your service.

* Thu Sep 12 2013 Cronbuild Service <cronbuild@altlinux.org> 20130912-alt1
- repocop cronbuild 20130912. At your service.

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 20130905-alt1
- repocop cronbuild 20130905. At your service.

* Wed Aug 28 2013 Cronbuild Service <cronbuild@altlinux.org> 20130828-alt1
- repocop cronbuild 20130828. At your service.

* Wed Aug 21 2013 Cronbuild Service <cronbuild@altlinux.org> 20130821-alt1
- repocop cronbuild 20130821. At your service.

* Wed Aug 14 2013 Cronbuild Service <cronbuild@altlinux.org> 20130814-alt1
- repocop cronbuild 20130814. At your service.

* Wed Jul 31 2013 Cronbuild Service <cronbuild@altlinux.org> 20130731-alt1
- repocop cronbuild 20130731. At your service.

* Wed Jul 24 2013 Cronbuild Service <cronbuild@altlinux.org> 20130724-alt1
- repocop cronbuild 20130724. At your service.

* Wed Jul 17 2013 Cronbuild Service <cronbuild@altlinux.org> 20130717-alt1
- repocop cronbuild 20130717. At your service.

* Wed Jul 10 2013 Cronbuild Service <cronbuild@altlinux.org> 20130710-alt1
- repocop cronbuild 20130710. At your service.

* Wed Jul 03 2013 Cronbuild Service <cronbuild@altlinux.org> 20130703-alt1
- repocop cronbuild 20130703. At your service.

* Wed Jun 26 2013 Cronbuild Service <cronbuild@altlinux.org> 20130626-alt1
- repocop cronbuild 20130626. At your service.

* Wed Jun 19 2013 Cronbuild Service <cronbuild@altlinux.org> 20130619-alt1
- repocop cronbuild 20130619. At your service.

* Wed Jun 12 2013 Cronbuild Service <cronbuild@altlinux.org> 20130612-alt1
- repocop cronbuild 20130612. At your service.

* Wed Jun 05 2013 Cronbuild Service <cronbuild@altlinux.org> 20130605-alt1
- repocop cronbuild 20130605. At your service.

* Wed May 29 2013 Cronbuild Service <cronbuild@altlinux.org> 20130529-alt1
- repocop cronbuild 20130529. At your service.

* Wed May 22 2013 Cronbuild Service <cronbuild@altlinux.org> 20130522-alt1
- repocop cronbuild 20130522. At your service.

* Wed May 15 2013 Cronbuild Service <cronbuild@altlinux.org> 20130515-alt1
- repocop cronbuild 20130515. At your service.

* Wed May 08 2013 Cronbuild Service <cronbuild@altlinux.org> 20130508-alt1
- repocop cronbuild 20130508. At your service.

* Mon Apr 08 2013 Cronbuild Service <cronbuild@altlinux.org> 20130408-alt1
- repocop cronbuild 20130408. At your service.

* Mon Apr 01 2013 Cronbuild Service <cronbuild@altlinux.org> 20130401-alt1
- repocop cronbuild 20130401. At your service.

* Mon Mar 25 2013 Cronbuild Service <cronbuild@altlinux.org> 20130325-alt1
- repocop cronbuild 20130325. At your service.

* Mon Mar 18 2013 Cronbuild Service <cronbuild@altlinux.org> 20130318-alt1
- repocop cronbuild 20130318. At your service.

* Mon Mar 11 2013 Cronbuild Service <cronbuild@altlinux.org> 20130311-alt1
- repocop cronbuild 20130311. At your service.

* Mon Mar 04 2013 Cronbuild Service <cronbuild@altlinux.org> 20130304-alt1
- repocop cronbuild 20130304. At your service.

* Mon Feb 25 2013 Cronbuild Service <cronbuild@altlinux.org> 20130225-alt1
- repocop cronbuild 20130225. At your service.

* Mon Feb 18 2013 Cronbuild Service <cronbuild@altlinux.org> 20130218-alt1
- repocop cronbuild 20130218. At your service.

* Mon Feb 11 2013 Cronbuild Service <cronbuild@altlinux.org> 20130211-alt1
- repocop cronbuild 20130211. At your service.

* Mon Feb 04 2013 Cronbuild Service <cronbuild@altlinux.org> 20130204-alt1
- repocop cronbuild 20130204. At your service.

* Mon Jan 28 2013 Cronbuild Service <cronbuild@altlinux.org> 20130128-alt1
- repocop cronbuild 20130128. At your service.

* Mon Jan 21 2013 Cronbuild Service <cronbuild@altlinux.org> 20130121-alt1
- repocop cronbuild 20130121. At your service.

* Mon Jan 14 2013 Cronbuild Service <cronbuild@altlinux.org> 20130114-alt1
- repocop cronbuild 20130114. At your service.

* Mon Jan 07 2013 Cronbuild Service <cronbuild@altlinux.org> 20130107-alt1
- repocop cronbuild 20130107. At your service.

* Mon Dec 31 2012 Cronbuild Service <cronbuild@altlinux.org> 20121231-alt1
- repocop cronbuild 20121231. At your service.

* Mon Dec 24 2012 Cronbuild Service <cronbuild@altlinux.org> 20121224-alt1
- repocop cronbuild 20121224. At your service.

* Mon Dec 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20121217-alt1
- repocop cronbuild 20121217. At your service.

* Mon Dec 10 2012 Cronbuild Service <cronbuild@altlinux.org> 20121210-alt1
- repocop cronbuild 20121210. At your service.

* Sun Dec 02 2012 Cronbuild Service <cronbuild@altlinux.org> 20121202-alt1
- repocop cronbuild 20121202. At your service.

* Sun Nov 25 2012 Cronbuild Service <cronbuild@altlinux.org> 20121125-alt1
- repocop cronbuild 20121125. At your service.

* Sun Nov 18 2012 Cronbuild Service <cronbuild@altlinux.org> 20121118-alt1
- repocop cronbuild 20121118. At your service.

* Sun Nov 11 2012 Cronbuild Service <cronbuild@altlinux.org> 20121111-alt1
- repocop cronbuild 20121111. At your service.

* Sun Nov 04 2012 Cronbuild Service <cronbuild@altlinux.org> 20121104-alt1
- repocop cronbuild 20121104. At your service.

* Sun Oct 28 2012 Cronbuild Service <cronbuild@altlinux.org> 20121028-alt1
- repocop cronbuild 20121028. At your service.

* Sun Oct 21 2012 Cronbuild Service <cronbuild@altlinux.org> 20121021-alt1
- repocop cronbuild 20121021. At your service.

* Sun Oct 14 2012 Cronbuild Service <cronbuild@altlinux.org> 20121014-alt1
- repocop cronbuild 20121014. At your service.

* Sun Oct 07 2012 Cronbuild Service <cronbuild@altlinux.org> 20121007-alt1
- repocop cronbuild 20121007. At your service.

* Sun Sep 30 2012 Cronbuild Service <cronbuild@altlinux.org> 20120930-alt1
- repocop cronbuild 20120930. At your service.

* Tue Sep 18 2012 Cronbuild Service <cronbuild@altlinux.org> 20120918-alt1
- repocop cronbuild 20120918. At your service.

* Tue Sep 11 2012 Cronbuild Service <cronbuild@altlinux.org> 20120911-alt1
- repocop cronbuild 20120911. At your service.

* Tue Sep 04 2012 Cronbuild Service <cronbuild@altlinux.org> 20120904-alt1
- repocop cronbuild 20120904. At your service.

* Tue Aug 21 2012 Cronbuild Service <cronbuild@altlinux.org> 20120821-alt1
- repocop cronbuild 20120821. At your service.

* Tue Aug 14 2012 Cronbuild Service <cronbuild@altlinux.org> 20120814-alt1
- repocop cronbuild 20120814. At your service.

* Tue Jul 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120717-alt1
- repocop cronbuild 20120717. At your service.

* Tue Jun 26 2012 Cronbuild Service <cronbuild@altlinux.org> 20120626-alt1
- repocop cronbuild 20120626. At your service.

* Tue May 08 2012 Cronbuild Service <cronbuild@altlinux.org> 20120508-alt1
- repocop cronbuild 20120508. At your service.

* Tue Apr 10 2012 Cronbuild Service <cronbuild@altlinux.org> 20120410-alt1
- repocop cronbuild 20120410. At your service.

* Tue Feb 28 2012 Cronbuild Service <cronbuild@altlinux.org> 20120228-alt1
- repocop cronbuild 20120228. At your service.

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 20120124-alt1
- repocop cronbuild 20120124. At your service.

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120117-alt1
- repocop cronbuild 20120117. At your service.

* Tue Jan 10 2012 Cronbuild Service <cronbuild@altlinux.org> 20120110-alt1
- repocop cronbuild 20120110. At your service.

* Tue Dec 27 2011 Cronbuild Service <cronbuild@altlinux.org> 20111227-alt1
- repocop cronbuild 20111227. At your service.

* Tue Dec 20 2011 Cronbuild Service <cronbuild@altlinux.org> 20111220-alt1
- repocop cronbuild 20111220. At your service.

* Wed Nov 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20111109-alt1
- repocop cronbuild 20111109. At your service.

* Sat Sep 10 2011 Cronbuild Service <cronbuild@altlinux.org> 20110910-alt1
- repocop cronbuild 20110910. At your service.

* Sat Jul 16 2011 Cronbuild Service <cronbuild@altlinux.org> 20110716-alt1
- repocop cronbuild 20110716. At your service.

* Sat Jul 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20110709-alt1
- repocop cronbuild 20110709. At your service.

* Sat Jun 25 2011 Cronbuild Service <cronbuild@altlinux.org> 20110625-alt1
- repocop cronbuild 20110625. At your service.

* Sat Jun 18 2011 Cronbuild Service <cronbuild@altlinux.org> 20110618-alt1
- repocop cronbuild 20110618. At your service.

* Sat May 28 2011 Cronbuild Service <cronbuild@altlinux.org> 20110528-alt1
- repocop cronbuild 20110528. At your service.

* Sat May 21 2011 Cronbuild Service <cronbuild@altlinux.org> 20110521-alt1
- repocop cronbuild 20110521. At your service.

* Sat Apr 30 2011 Cronbuild Service <cronbuild@altlinux.org> 20110430-alt1
- repocop cronbuild 20110430. At your service.

* Sat Apr 23 2011 Cronbuild Service <cronbuild@altlinux.org> 20110423-alt1
- repocop cronbuild 20110423. At your service.

* Sat Apr 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20110409-alt1
- repocop cronbuild 20110409. At your service.

* Sat Mar 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20110312-alt1
- repocop cronbuild 20110312. At your service.

* Fri Feb 11 2011 Cronbuild Service <cronbuild@altlinux.org> 20110211-alt1
- repocop cronbuild 20110211. At your service.

* Fri Jan 28 2011 Cronbuild Service <cronbuild@altlinux.org> 20110128-alt1
- repocop cronbuild 20110128. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 20110114-alt1
- repocop cronbuild 20110114. At your service.

* Tue Nov 23 2010 Cronbuild Service <cronbuild@altlinux.org> 20101123-alt1
- repocop cronbuild 20101123. At your service.

* Tue Nov 09 2010 Cronbuild Service <cronbuild@altlinux.org> 20101109-alt1
- repocop cronbuild 20101109. At your service.

* Mon Oct 25 2010 Cronbuild Service <cronbuild@altlinux.org> 20101025-alt1
- repocop cronbuild 20101025. At your service.

* Tue Oct 05 2010 Cronbuild Service <cronbuild@altlinux.org> 20101005-alt1
- repocop cronbuild 20101005. At your service.

* Mon Sep 06 2010 Cronbuild Service <cronbuild@altlinux.org> 20100906-alt1
- repocop cronbuild 20100906. At your service.

* Tue Sep 15 2009 Victor Forsyuk <force@altlinux.org> 20090915-alt1
- 2009-09-15 snapshot.

* Tue Jul 07 2009 Victor Forsyuk <force@altlinux.org> 20090704-alt1
- 2009-07-04 snapshot.

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 20081105-alt1
- 2008-11-05 snapshot.

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 20080331-alt1
- 2008-03-31 snapshot.

* Mon Feb 18 2008 Victor Forsyuk <force@altlinux.org> 20080218-alt1
- 2008-02-18 snapshot.

* Mon Oct 15 2007 Victor Forsyuk <force@altlinux.org> 20071015-alt1
- 2007-10-15 snapshot.

* Tue Sep 04 2007 Victor Forsyuk <force@altlinux.org> 20070904-alt1
- 2007-09-04 snapshot.

* Tue Aug 14 2007 Victor Forsyuk <force@altlinux.org> 20070814-alt1
- 2007-08-14 snapshot.

* Tue Aug 07 2007 Victor Forsyuk <force@altlinux.org> 20070807-alt1
- Initial build.
