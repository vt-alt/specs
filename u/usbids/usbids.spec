Name: usbids
Version: 20191006
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Repository of USB vendor IDs
License: GPLv2+ or BSD 3-clause
Group: System/Libraries

Url: http://www.linux-usb.org
Source: %url/usb.ids

BuildArch: noarch

%description
This package contains a public list of all known IDs used in USB devices.

%prep
%setup -c -T

%build

%install
install -pD -m644 %SOURCE0 %buildroot%_datadir/misc/usb.ids

%files
%_datadir/misc/usb.ids

%changelog
* Sun Oct 06 2019 Cronbuild Service <cronbuild@altlinux.org> 20191006-alt1
- repocop cronbuild 20191006. At your service.

* Sun Sep 22 2019 Cronbuild Service <cronbuild@altlinux.org> 20190922-alt1
- repocop cronbuild 20190922. At your service.

* Sun Aug 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20190825-alt1
- repocop cronbuild 20190825. At your service.

* Sun Jul 28 2019 Cronbuild Service <cronbuild@altlinux.org> 20190728-alt1
- repocop cronbuild 20190728. At your service.

* Sun May 12 2019 Cronbuild Service <cronbuild@altlinux.org> 20190512-alt1
- repocop cronbuild 20190512. At your service.

* Sun Apr 28 2019 Cronbuild Service <cronbuild@altlinux.org> 20190428-alt1
- repocop cronbuild 20190428. At your service.

* Sun Mar 24 2019 Cronbuild Service <cronbuild@altlinux.org> 20190324-alt1
- repocop cronbuild 20190324. At your service.

* Sun Mar 03 2019 Cronbuild Service <cronbuild@altlinux.org> 20190303-alt1
- repocop cronbuild 20190303. At your service.

* Sun Feb 24 2019 Cronbuild Service <cronbuild@altlinux.org> 20190224-alt1
- repocop cronbuild 20190224. At your service.

* Sun Jan 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190120-alt1
- repocop cronbuild 20190120. At your service.

* Sun Dec 09 2018 Cronbuild Service <cronbuild@altlinux.org> 20181209-alt1
- repocop cronbuild 20181209. At your service.

* Sun Nov 18 2018 Cronbuild Service <cronbuild@altlinux.org> 20181118-alt1
- repocop cronbuild 20181118. At your service.

* Sun Oct 28 2018 Cronbuild Service <cronbuild@altlinux.org> 20181028-alt1
- repocop cronbuild 20181028. At your service.

* Sun Aug 19 2018 Cronbuild Service <cronbuild@altlinux.org> 20180819-alt1
- repocop cronbuild 20180819. At your service.

* Sun Aug 12 2018 Cronbuild Service <cronbuild@altlinux.org> 20180812-alt1
- repocop cronbuild 20180812. At your service.

* Sun Jul 08 2018 Cronbuild Service <cronbuild@altlinux.org> 20180708-alt1
- repocop cronbuild 20180708. At your service.

* Sun May 06 2018 Cronbuild Service <cronbuild@altlinux.org> 20180506-alt1
- repocop cronbuild 20180506. At your service.

* Sun Apr 15 2018 Cronbuild Service <cronbuild@altlinux.org> 20180415-alt1
- repocop cronbuild 20180415. At your service.

* Sun Apr 01 2018 Cronbuild Service <cronbuild@altlinux.org> 20180401-alt1
- repocop cronbuild 20180401. At your service.

* Sun Mar 25 2018 Cronbuild Service <cronbuild@altlinux.org> 20180325-alt1
- repocop cronbuild 20180325. At your service.

* Sun Mar 04 2018 Cronbuild Service <cronbuild@altlinux.org> 20180304-alt1
- repocop cronbuild 20180304. At your service.

* Tue Jan 09 2018 Cronbuild Service <cronbuild@altlinux.org> 20180109-alt1
- repocop cronbuild 20180109. At your service.

* Tue Jan 02 2018 Cronbuild Service <cronbuild@altlinux.org> 20180102-alt1
- repocop cronbuild 20180102. At your service.

* Tue Nov 28 2017 Cronbuild Service <cronbuild@altlinux.org> 20171128-alt1
- repocop cronbuild 20171128. At your service.

* Wed Sep 13 2017 Cronbuild Service <cronbuild@altlinux.org> 20170913-alt1
- repocop cronbuild 20170913. At your service.

* Wed Aug 02 2017 Cronbuild Service <cronbuild@altlinux.org> 20170802-alt1
- repocop cronbuild 20170802. At your service.

* Wed Jun 28 2017 Cronbuild Service <cronbuild@altlinux.org> 20170628-alt1
- repocop cronbuild 20170628. At your service.

* Wed Feb 15 2017 Cronbuild Service <cronbuild@altlinux.org> 20170215-alt1
- repocop cronbuild 20170215. At your service.

* Wed Dec 07 2016 Cronbuild Service <cronbuild@altlinux.org> 20161207-alt1
- repocop cronbuild 20161207. At your service.

* Wed Nov 16 2016 Cronbuild Service <cronbuild@altlinux.org> 20161116-alt1
- repocop cronbuild 20161116. At your service.

* Wed Nov 09 2016 Cronbuild Service <cronbuild@altlinux.org> 20161109-alt1
- repocop cronbuild 20161109. At your service.

* Wed Oct 19 2016 Cronbuild Service <cronbuild@altlinux.org> 20161019-alt1
- repocop cronbuild 20161019. At your service.

* Wed Oct 05 2016 Cronbuild Service <cronbuild@altlinux.org> 20161005-alt1
- repocop cronbuild 20161005. At your service.

* Wed Sep 28 2016 Cronbuild Service <cronbuild@altlinux.org> 20160928-alt1
- repocop cronbuild 20160928. At your service.

* Wed Sep 07 2016 Cronbuild Service <cronbuild@altlinux.org> 20160907-alt1
- repocop cronbuild 20160907. At your service.

* Wed Aug 17 2016 Cronbuild Service <cronbuild@altlinux.org> 20160817-alt1
- repocop cronbuild 20160817. At your service.

* Wed Jul 27 2016 Cronbuild Service <cronbuild@altlinux.org> 20160727-alt1
- repocop cronbuild 20160727. At your service.

* Wed Jul 13 2016 Cronbuild Service <cronbuild@altlinux.org> 20160713-alt1
- repocop cronbuild 20160713. At your service.

* Wed Jun 29 2016 Cronbuild Service <cronbuild@altlinux.org> 20160629-alt1
- repocop cronbuild 20160629. At your service.

* Tue Mar 08 2016 Cronbuild Service <cronbuild@altlinux.org> 20160308-alt1
- repocop cronbuild 20160308. At your service.

* Thu Dec 24 2015 Cronbuild Service <cronbuild@altlinux.org> 20151224-alt1
- repocop cronbuild 20151224. At your service.

* Sat Oct 03 2015 Cronbuild Service <cronbuild@altlinux.org> 20151003-alt1
- repocop cronbuild 20151003. At your service.

* Sat Sep 19 2015 Cronbuild Service <cronbuild@altlinux.org> 20150919-alt1
- repocop cronbuild 20150919. At your service.

* Sat Sep 05 2015 Cronbuild Service <cronbuild@altlinux.org> 20150905-alt1
- repocop cronbuild 20150905. At your service.

* Sun Aug 23 2015 Cronbuild Service <cronbuild@altlinux.org> 20150823-alt1
- repocop cronbuild 20150823. At your service.

* Wed Jun 24 2015 Cronbuild Service <cronbuild@altlinux.org> 20150624-alt1
- repocop cronbuild 20150624. At your service.

* Wed Jun 10 2015 Cronbuild Service <cronbuild@altlinux.org> 20150610-alt1
- repocop cronbuild 20150610. At your service.

* Thu May 07 2015 Cronbuild Service <cronbuild@altlinux.org> 20150507-alt1
- repocop cronbuild 20150507. At your service.

* Thu Apr 30 2015 Cronbuild Service <cronbuild@altlinux.org> 20150430-alt1
- repocop cronbuild 20150430. At your service.

* Thu Apr 23 2015 Cronbuild Service <cronbuild@altlinux.org> 20150423-alt1
- repocop cronbuild 20150423. At your service.

* Thu Apr 02 2015 Cronbuild Service <cronbuild@altlinux.org> 20150402-alt1
- repocop cronbuild 20150402. At your service.

* Thu Mar 26 2015 Cronbuild Service <cronbuild@altlinux.org> 20150326-alt1
- repocop cronbuild 20150326. At your service.

* Thu Mar 19 2015 Cronbuild Service <cronbuild@altlinux.org> 20150319-alt1
- repocop cronbuild 20150319. At your service.

* Thu Mar 12 2015 Cronbuild Service <cronbuild@altlinux.org> 20150312-alt1
- repocop cronbuild 20150312. At your service.

* Thu Feb 26 2015 Cronbuild Service <cronbuild@altlinux.org> 20150226-alt1
- repocop cronbuild 20150226. At your service.

* Thu Feb 05 2015 Cronbuild Service <cronbuild@altlinux.org> 20150205-alt1
- repocop cronbuild 20150205. At your service.

* Thu Jan 15 2015 Cronbuild Service <cronbuild@altlinux.org> 20150115-alt1
- repocop cronbuild 20150115. At your service.

* Thu Jan 08 2015 Cronbuild Service <cronbuild@altlinux.org> 20150108-alt1
- repocop cronbuild 20150108. At your service.

* Thu Dec 11 2014 Cronbuild Service <cronbuild@altlinux.org> 20141211-alt1
- repocop cronbuild 20141211. At your service.

* Thu Sep 11 2014 Cronbuild Service <cronbuild@altlinux.org> 20140911-alt1
- repocop cronbuild 20140911. At your service.

* Thu Jun 26 2014 Cronbuild Service <cronbuild@altlinux.org> 20140626-alt1
- repocop cronbuild 20140626. At your service.

* Thu May 08 2014 Cronbuild Service <cronbuild@altlinux.org> 20140508-alt1
- repocop cronbuild 20140508. At your service.

* Thu Feb 06 2014 Cronbuild Service <cronbuild@altlinux.org> 20140206-alt1
- repocop cronbuild 20140206. At your service.

* Thu Jan 09 2014 Cronbuild Service <cronbuild@altlinux.org> 20140109-alt1
- repocop cronbuild 20140109. At your service.

* Thu Dec 26 2013 Cronbuild Service <cronbuild@altlinux.org> 20131226-alt1
- repocop cronbuild 20131226. At your service.

* Thu Dec 19 2013 Cronbuild Service <cronbuild@altlinux.org> 20131219-alt1
- repocop cronbuild 20131219. At your service.

* Thu Oct 24 2013 Cronbuild Service <cronbuild@altlinux.org> 20131024-alt1
- repocop cronbuild 20131024. At your service.

* Thu Aug 22 2013 Cronbuild Service <cronbuild@altlinux.org> 20130822-alt1
- repocop cronbuild 20130822. At your service.

* Wed May 29 2013 Cronbuild Service <cronbuild@altlinux.org> 20130529-alt1
- repocop cronbuild 20130529. At your service.

* Mon Mar 25 2013 Cronbuild Service <cronbuild@altlinux.org> 20130325-alt1
- repocop cronbuild 20130325. At your service.

* Mon Mar 11 2013 Cronbuild Service <cronbuild@altlinux.org> 20130311-alt1
- repocop cronbuild 20130311. At your service.

* Sun Jan 20 2013 Cronbuild Service <cronbuild@altlinux.org> 20130120-alt1
- repocop cronbuild 20130120. At your service.

* Sun Nov 25 2012 Cronbuild Service <cronbuild@altlinux.org> 20121125-alt1
- repocop cronbuild 20121125. At your service.

* Sun Sep 30 2012 Cronbuild Service <cronbuild@altlinux.org> 20120930-alt1
- repocop cronbuild 20120930. At your service.

* Tue Jul 31 2012 Cronbuild Service <cronbuild@altlinux.org> 20120731-alt1
- repocop cronbuild 20120731. At your service.

* Tue Jun 12 2012 Cronbuild Service <cronbuild@altlinux.org> 20120612-alt1
- repocop cronbuild 20120612. At your service.

* Tue Apr 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120417-alt1
- repocop cronbuild 20120417. At your service.

* Tue Feb 14 2012 Cronbuild Service <cronbuild@altlinux.org> 20120214-alt1
- repocop cronbuild 20120214. At your service.

* Tue Feb 07 2012 Cronbuild Service <cronbuild@altlinux.org> 20120207-alt1
- repocop cronbuild 20120207. At your service.

* Tue Jan 24 2012 Cronbuild Service <cronbuild@altlinux.org> 20120124-alt1
- repocop cronbuild 20120124. At your service.

* Tue Jan 17 2012 Cronbuild Service <cronbuild@altlinux.org> 20120117-alt1
- repocop cronbuild 20120117. At your service.

* Wed Nov 16 2011 Cronbuild Service <cronbuild@altlinux.org> 20111116-alt1
- repocop cronbuild 20111116. At your service.

* Fri Sep 30 2011 Cronbuild Service <cronbuild@altlinux.org> 20110930-alt1
- repocop cronbuild 20110930. At your service.

* Fri Sep 09 2011 Cronbuild Service <cronbuild@altlinux.org> 20110909-alt1
- repocop cronbuild 20110909. At your service.

* Fri Aug 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20110812-alt1
- repocop cronbuild 20110812. At your service.

* Fri Jun 24 2011 Cronbuild Service <cronbuild@altlinux.org> 20110624-alt1
- repocop cronbuild 20110624. At your service.

* Sat Apr 16 2011 Cronbuild Service <cronbuild@altlinux.org> 20110416-alt1
- repocop cronbuild 20110416. At your service.

* Sat Mar 12 2011 Cronbuild Service <cronbuild@altlinux.org> 20110312-alt1
- repocop cronbuild 20110312. At your service.

* Sat Mar 05 2011 Cronbuild Service <cronbuild@altlinux.org> 20110305-alt1
- repocop cronbuild 20110305. At your service.

* Fri Jan 28 2011 Cronbuild Service <cronbuild@altlinux.org> 20110128-alt1
- repocop cronbuild 20110128. At your service.

* Fri Jan 14 2011 Cronbuild Service <cronbuild@altlinux.org> 20110114-alt1
- repocop cronbuild 20110114. At your service.

* Tue Nov 16 2010 Cronbuild Service <cronbuild@altlinux.org> 20101116-alt1
- repocop cronbuild 20101116. At your service.

* Tue Nov 02 2010 Cronbuild Service <cronbuild@altlinux.org> 20101102-alt1
- repocop cronbuild 20101102. At your service.

* Tue Oct 26 2010 Cronbuild Service <cronbuild@altlinux.org> 20101026-alt1
- repocop cronbuild 20101026. At your service.

* Tue Oct 12 2010 Cronbuild Service <cronbuild@altlinux.org> 20101012-alt1
- repocop cronbuild 20101012. At your service.

* Mon Sep 20 2010 Cronbuild Service <cronbuild@altlinux.org> 20100920-alt1
- repocop cronbuild 20100920. At your service.

* Mon Sep 13 2010 Cronbuild Service <cronbuild@altlinux.org> 20100913-alt1
- repocop cronbuild 20100913. At your service.

* Mon Sep 06 2010 Cronbuild Service <cronbuild@altlinux.org> 20100906-alt1
- repocop cronbuild 20100906. At your service.

* Tue Sep 15 2009 Victor Forsyuk <force@altlinux.org> 20090912-alt1
- 2009-09-12 snapshot.

* Tue Jul 07 2009 Victor Forsyuk <force@altlinux.org> 20090705-alt1
- 2009-07-05 snapshot.

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 20080921-alt1
- 2008-09-21 snapshot.

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 20080327-alt1
- 2008-03-27 snapshot.

* Mon Feb 18 2008 Victor Forsyuk <force@altlinux.org> 20080210-alt1
- 2008-02-10 snapshot.

* Tue Aug 07 2007 Victor Forsyuk <force@altlinux.org> 20070728-alt1
- Initial build.
