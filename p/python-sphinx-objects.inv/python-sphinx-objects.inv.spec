%define inversion 2
%define pyversion 3.8
%define reldate 20190514

Name: python-sphinx-objects.inv
Version: %inversion.%pyversion.%reldate
Release: alt1
Epoch: 1
Summary: Sphinx inventory version %inversion
License: BSD
Group: Development/Python
Packager: Python Development Team <python@packages.altlinux.org>
Url: https://docs.python.org/dev/objects.inv
Source: %url
BuildArch: noarch

%description
This package contains periodically updated Sphinx inventory version %inversion
for Python %pyversion.

%install
mkdir -p %buildroot%_datadir/python-sphinx
install -pDm644 %SOURCE0 %buildroot%_datadir/python-sphinx/objects.inv

%files
%_datadir/python-sphinx/

%changelog
* Tue May 14 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190514-alt1
- repocop cronbuild 20190514. At your service.

* Mon May 13 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190513-alt1
- repocop cronbuild 20190513. At your service.

* Mon May 13 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190512-alt1
- repocop cronbuild 20190513. At your service.

* Fri May 10 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190510-alt1
- repocop cronbuild 20190510. At your service.

* Fri May 10 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190509-alt1
- repocop cronbuild 20190510. At your service.

* Tue May 07 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190507-alt1
- repocop cronbuild 20190507. At your service.

* Sat May 04 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190504-alt1
- repocop cronbuild 20190504. At your service.

* Wed May 01 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190501-alt1
- repocop cronbuild 20190501. At your service.

* Mon Apr 29 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190429-alt1
- repocop cronbuild 20190429. At your service.

* Fri Apr 26 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190425-alt1
- repocop cronbuild 20190426. At your service.

* Thu Apr 25 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190424-alt1
- repocop cronbuild 20190425. At your service.

* Tue Apr 23 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190423-alt1
- repocop cronbuild 20190423. At your service.

* Sat Apr 20 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190419-alt1
- repocop cronbuild 20190420. At your service.

* Mon Apr 08 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190408-alt1
- repocop cronbuild 20190408. At your service.

* Sun Apr 07 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190407-alt1
- repocop cronbuild 20190407. At your service.

* Tue Apr 02 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190401-alt1
- repocop cronbuild 20190402. At your service.

* Sat Mar 30 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190330-alt1
- repocop cronbuild 20190330. At your service.

* Fri Mar 29 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190327-alt1
- repocop cronbuild 20190329. At your service.

* Sun Mar 24 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190324-alt1
- repocop cronbuild 20190324. At your service.

* Sat Mar 23 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190322-alt1
- repocop cronbuild 20190323. At your service.

* Wed Mar 20 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190319-alt1
- repocop cronbuild 20190320. At your service.

* Sun Mar 17 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190316-alt1
- repocop cronbuild 20190317. At your service.

* Tue Mar 12 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190312-alt1
- repocop cronbuild 20190312. At your service.

* Mon Mar 11 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190310-alt1
- repocop cronbuild 20190311. At your service.

* Fri Mar 08 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190307-alt1
- repocop cronbuild 20190308. At your service.

* Mon Feb 25 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190224-alt1
- repocop cronbuild 20190225. At your service.

* Sun Feb 24 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190223-alt1
- repocop cronbuild 20190224. At your service.

* Thu Feb 21 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190221-alt1
- repocop cronbuild 20190221. At your service.

* Tue Feb 19 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190219-alt1
- repocop cronbuild 20190219. At your service.

* Thu Feb 07 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190207-alt1
- repocop cronbuild 20190207. At your service.

* Thu Jan 31 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190131-alt1
- repocop cronbuild 20190131. At your service.

* Mon Jan 28 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190127-alt1
- repocop cronbuild 20190128. At your service.

* Fri Jan 25 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190125-alt1
- repocop cronbuild 20190125. At your service.

* Tue Jan 22 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190122-alt1
- repocop cronbuild 20190122. At your service.

* Sat Jan 19 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190118-alt1
- repocop cronbuild 20190119. At your service.

* Wed Jan 16 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190116-alt1
- repocop cronbuild 20190116. At your service.

* Thu Jan 10 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190110-alt1
- repocop cronbuild 20190110. At your service.

* Tue Jan 08 2019 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20190108-alt1
- repocop cronbuild 20190108. At your service.

* Thu Dec 20 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181220-alt1
- repocop cronbuild 20181220. At your service.

* Thu Dec 20 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181219-alt1
- repocop cronbuild 20181220. At your service.

* Fri Dec 14 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181214-alt1
- repocop cronbuild 20181214. At your service.

* Tue Dec 11 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181211-alt1
- repocop cronbuild 20181211. At your service.

* Sun Dec 02 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181202-alt1
- repocop cronbuild 20181202. At your service.

* Thu Nov 29 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181129-alt1
- repocop cronbuild 20181129. At your service.

* Wed Nov 21 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181121-alt1
- repocop cronbuild 20181121. At your service.

* Wed Nov 14 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181113-alt1
- repocop cronbuild 20181114. At your service.

* Fri Nov 09 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181109-alt1
- repocop cronbuild 20181109. At your service.

* Thu Nov 08 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181107-alt1
- repocop cronbuild 20181108. At your service.

* Wed Nov 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.3.8.20181106-alt1
- replaced Serial with Epoch in spec

* Mon Nov 05 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181105-alt1
- repocop cronbuild 20181105. At your service.

* Sat Nov 03 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181103-alt1
- repocop cronbuild 20181103. At your service.

* Fri Nov 02 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181102-alt1
- repocop cronbuild 20181102. At your service.

* Wed Oct 31 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181031-alt1
- repocop cronbuild 20181031. At your service.

* Thu Oct 25 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181025-alt1
- repocop cronbuild 20181025. At your service.

* Sun Oct 21 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181020-alt1
- repocop cronbuild 20181021. At your service.

* Tue Oct 16 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181016-alt1
- repocop cronbuild 20181016. At your service.

* Fri Oct 12 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181012-alt1
- repocop cronbuild 20181012. At your service.

* Fri Oct 12 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181011-alt1
- repocop cronbuild 20181012. At your service.

* Wed Oct 10 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20181010-alt1
- repocop cronbuild 20181010. At your service.

* Thu Sep 27 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180926-alt1
- repocop cronbuild 20180927. At your service.

* Tue Sep 25 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180925-alt1
- repocop cronbuild 20180925. At your service.

* Mon Sep 24 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180923-alt1
- repocop cronbuild 20180924. At your service.

* Fri Sep 21 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180921-alt1
- repocop cronbuild 20180921. At your service.

* Fri Sep 21 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180920-alt1
- repocop cronbuild 20180921. At your service.

* Tue Sep 18 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180918-alt1
- repocop cronbuild 20180918. At your service.

* Wed Sep 12 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180912-alt1
- repocop cronbuild 20180912. At your service.

* Wed Aug 29 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180828-alt1
- repocop cronbuild 20180829. At your service.

* Fri Aug 10 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180808-alt1
- repocop cronbuild 20180810. At your service.

* Wed Aug 01 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180731-alt1
- repocop cronbuild 20180801. At your service.

* Tue Jul 24 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180724-alt1
- repocop cronbuild 20180724. At your service.

* Tue Jul 17 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180716-alt1
- repocop cronbuild 20180717. At your service.

* Wed Jul 11 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180710-alt1
- repocop cronbuild 20180711. At your service.

* Sun Jul 08 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180708-alt1
- repocop cronbuild 20180708. At your service.

* Sun Jul 08 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180707-alt1
- repocop cronbuild 20180708. At your service.

* Tue Jun 26 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180626-alt1
- repocop cronbuild 20180626. At your service.

* Sun Jun 17 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180616-alt1
- repocop cronbuild 20180617. At your service.

* Thu Jun 14 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180613-alt1
- repocop cronbuild 20180614. At your service.

* Fri Jun 08 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180608-alt1
- repocop cronbuild 20180608. At your service.

* Tue Jun 05 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180605-alt1
- repocop cronbuild 20180605. At your service.

* Wed May 30 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180530-alt1
- repocop cronbuild 20180530. At your service.

* Wed May 30 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180529-alt1
- repocop cronbuild 20180530. At your service.

* Sun May 27 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180526-alt1
- repocop cronbuild 20180527. At your service.

* Fri May 25 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180525-alt1
- repocop cronbuild 20180525. At your service.

* Thu May 24 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180523-alt1
- repocop cronbuild 20180524. At your service.

* Tue May 22 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180522-alt1
- repocop cronbuild 20180522. At your service.

* Mon May 21 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180520-alt1
- repocop cronbuild 20180521. At your service.

* Fri May 18 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180517-alt1
- repocop cronbuild 20180518. At your service.

* Wed May 16 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180516-alt1
- repocop cronbuild 20180516. At your service.

* Tue May 15 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180515-alt1
- repocop cronbuild 20180515. At your service.

* Tue May 15 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180514-alt1
- repocop cronbuild 20180515. At your service.

* Wed May 09 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180508-alt1
- repocop cronbuild 20180509. At your service.

* Fri May 04 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180504-alt1
- repocop cronbuild 20180504. At your service.

* Sun Apr 15 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180415-alt1
- repocop cronbuild 20180415. At your service.

* Sun Apr 15 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180414-alt1
- repocop cronbuild 20180415. At your service.

* Sat Apr 07 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180407-alt1
- repocop cronbuild 20180407. At your service.

* Sun Apr 01 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180401-alt1
- repocop cronbuild 20180401. At your service.

* Wed Mar 28 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180328-alt1
- repocop cronbuild 20180328. At your service.

* Mon Mar 26 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180326-alt1
- repocop cronbuild 20180326. At your service.

* Sun Mar 25 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180325-alt1
- repocop cronbuild 20180325. At your service.

* Fri Mar 23 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180323-alt1
- repocop cronbuild 20180323. At your service.

* Thu Mar 22 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180320-alt1
- repocop cronbuild 20180322. At your service.

* Tue Mar 13 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180312-alt1
- repocop cronbuild 20180313. At your service.

* Sun Mar 11 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180310-alt1
- repocop cronbuild 20180311. At your service.

* Thu Mar 08 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180308-alt1
- repocop cronbuild 20180308. At your service.

* Sun Mar 04 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180302-alt1
- repocop cronbuild 20180304. At your service.

* Tue Feb 13 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180211-alt1
- repocop cronbuild 20180213. At your service.

* Thu Feb 01 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.8.20180201-alt1
- repocop cronbuild 20180201. At your service.

* Tue Jan 30 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180130-alt1
- repocop cronbuild 20180130. At your service.

* Mon Jan 29 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180129-alt1
- repocop cronbuild 20180129. At your service.

* Mon Jan 29 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180128-alt1
- repocop cronbuild 20180129. At your service.

* Sat Jan 27 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180127-alt1
- repocop cronbuild 20180127. At your service.

* Fri Jan 26 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180125-alt1
- repocop cronbuild 20180126. At your service.

* Sun Jan 21 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180121-alt1
- repocop cronbuild 20180121. At your service.

* Sat Jan 20 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180119-alt1
- repocop cronbuild 20180120. At your service.

* Wed Jan 17 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180116-alt1
- repocop cronbuild 20180117. At your service.

* Fri Jan 12 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180112-alt1
- repocop cronbuild 20180112. At your service.

* Thu Jan 11 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180111-alt1
- repocop cronbuild 20180111. At your service.

* Mon Jan 08 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180108-alt1
- repocop cronbuild 20180108. At your service.

* Sat Jan 06 2018 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20180106-alt1
- repocop cronbuild 20180106. At your service.

* Sat Dec 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171230-alt1
- repocop cronbuild 20171230. At your service.

* Sun Dec 24 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171223-alt1
- repocop cronbuild 20171224. At your service.

* Thu Dec 21 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171221-alt1
- repocop cronbuild 20171221. At your service.

* Tue Dec 19 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171219-alt1
- repocop cronbuild 20171219. At your service.

* Mon Dec 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171218-alt1
- repocop cronbuild 20171218. At your service.

* Sat Dec 16 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171216-alt1
- repocop cronbuild 20171216. At your service.

* Fri Dec 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171215-alt1
- repocop cronbuild 20171215. At your service.

* Fri Dec 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171214-alt1
- repocop cronbuild 20171215. At your service.

* Wed Dec 13 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171213-alt1
- repocop cronbuild 20171213. At your service.

* Tue Dec 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171211-alt1
- repocop cronbuild 20171212. At your service.

* Sat Dec 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171209-alt1
- repocop cronbuild 20171209. At your service.

* Thu Nov 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171130-alt1
- repocop cronbuild 20171130. At your service.

* Thu Nov 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171129-alt1
- repocop cronbuild 20171130. At your service.

* Mon Nov 27 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171125-alt1
- repocop cronbuild 20171127. At your service.

* Fri Nov 24 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171123-alt1
- repocop cronbuild 20171124. At your service.

* Wed Nov 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171115-alt1
- repocop cronbuild 20171115. At your service.

* Thu Nov 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171108-alt1
- repocop cronbuild 20171109. At your service.

* Tue Nov 07 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171107-alt1
- repocop cronbuild 20171107. At your service.

* Sat Nov 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171104-alt1
- repocop cronbuild 20171104. At your service.

* Fri Nov 03 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171102-alt1
- repocop cronbuild 20171103. At your service.

* Tue Oct 31 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171031-alt1
- repocop cronbuild 20171031. At your service.

* Wed Oct 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171024-alt1
- repocop cronbuild 20171025. At your service.

* Wed Oct 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171017-alt1
- repocop cronbuild 20171018. At your service.

* Tue Oct 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171016-alt1
- repocop cronbuild 20171017. At your service.

* Thu Oct 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171011-alt1
- repocop cronbuild 20171012. At your service.

* Tue Oct 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171009-alt1
- repocop cronbuild 20171010. At your service.

* Fri Oct 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171006-alt1
- repocop cronbuild 20171006. At your service.

* Wed Oct 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20171004-alt1
- repocop cronbuild 20171004. At your service.

* Sat Sep 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170930-alt1
- repocop cronbuild 20170930. At your service.

* Sat Sep 16 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170915-alt1
- repocop cronbuild 20170916. At your service.

* Fri Sep 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170914-alt1
- repocop cronbuild 20170915. At your service.

* Sun Sep 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170910-alt1
- repocop cronbuild 20170910. At your service.

* Sat Sep 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170908-alt1
- repocop cronbuild 20170909. At your service.

* Thu Sep 07 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170907-alt1
- repocop cronbuild 20170907. At your service.

* Thu Sep 07 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170906-alt1
- repocop cronbuild 20170907. At your service.

* Wed Sep 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170905-alt1
- repocop cronbuild 20170906. At your service.

* Tue Sep 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170904-alt1
- repocop cronbuild 20170905. At your service.

* Tue Aug 29 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170828-alt1
- repocop cronbuild 20170829. At your service.

* Fri Aug 11 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170810-alt1
- repocop cronbuild 20170811. At your service.

* Thu Aug 10 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170809-alt1
- repocop cronbuild 20170810. At your service.

* Tue Aug 08 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170807-alt1
- repocop cronbuild 20170808. At your service.

* Wed Aug 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170802-alt1
- repocop cronbuild 20170802. At your service.

* Sun Jul 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170730-alt1
- repocop cronbuild 20170730. At your service.

* Tue Jul 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170718-alt1
- repocop cronbuild 20170718. At your service.

* Wed Jul 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170704-alt1
- repocop cronbuild 20170705. At your service.

* Sat Jun 24 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170624-alt1
- repocop cronbuild 20170624. At your service.

* Wed Jun 21 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170620-alt1
- repocop cronbuild 20170621. At your service.

* Mon Jun 12 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170611-alt1
- repocop cronbuild 20170612. At your service.

* Fri Jun 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170609-alt1
- repocop cronbuild 20170609. At your service.

* Tue Jun 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170606-alt1
- repocop cronbuild 20170606. At your service.

* Sat Jun 03 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170603-alt1
- repocop cronbuild 20170603. At your service.

* Sat Jun 03 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170602-alt1
- repocop cronbuild 20170603. At your service.

* Wed May 31 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170531-alt1
- repocop cronbuild 20170531. At your service.

* Sun May 28 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170527-alt1
- repocop cronbuild 20170528. At your service.

* Thu May 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170524-alt1
- repocop cronbuild 20170525. At your service.

* Sun May 21 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170520-alt1
- repocop cronbuild 20170521. At your service.

* Fri May 19 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170519-alt1
- repocop cronbuild 20170519. At your service.

* Wed May 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170516-alt1
- repocop cronbuild 20170517. At your service.

* Sat May 13 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170512-alt1
- repocop cronbuild 20170513. At your service.

* Tue May 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170508-alt1
- repocop cronbuild 20170509. At your service.

* Sat May 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170505-alt1
- repocop cronbuild 20170506. At your service.

* Tue May 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170501-alt1
- repocop cronbuild 20170502. At your service.

* Thu Apr 27 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170426-alt1
- repocop cronbuild 20170427. At your service.

* Tue Apr 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170425-alt1
- repocop cronbuild 20170425. At your service.

* Sun Apr 23 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170422-alt1
- repocop cronbuild 20170423. At your service.

* Sat Apr 15 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170415-alt1
- repocop cronbuild 20170415. At your service.

* Fri Apr 14 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170413-alt1
- repocop cronbuild 20170414. At your service.

* Sun Apr 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170408-alt1
- repocop cronbuild 20170409. At your service.

* Thu Apr 06 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170405-alt1
- repocop cronbuild 20170406. At your service.

* Wed Apr 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170404-alt1
- repocop cronbuild 20170405. At your service.

* Fri Mar 31 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170330-alt1
- repocop cronbuild 20170331. At your service.

* Thu Mar 30 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170329-alt1
- repocop cronbuild 20170330. At your service.

* Wed Mar 29 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170328-alt1
- repocop cronbuild 20170329. At your service.

* Sun Mar 26 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170325-alt1
- repocop cronbuild 20170326. At your service.

* Thu Mar 23 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170322-alt1
- repocop cronbuild 20170323. At your service.

* Sat Mar 11 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170310-alt1
- repocop cronbuild 20170311. At your service.

* Thu Mar 09 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170308-alt1
- repocop cronbuild 20170309. At your service.

* Sat Mar 04 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170303-alt1
- repocop cronbuild 20170304. At your service.

* Thu Mar 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170301-alt1
- repocop cronbuild 20170302. At your service.

* Sat Feb 25 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170224-alt1
- repocop cronbuild 20170225. At your service.

* Sun Feb 19 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170219-alt1
- repocop cronbuild 20170219. At your service.

* Fri Feb 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170216-alt1
- repocop cronbuild 20170217. At your service.

* Sat Feb 11 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170211-alt1
- repocop cronbuild 20170211. At your service.

* Sun Feb 05 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170205-alt1
- repocop cronbuild 20170205. At your service.

* Thu Feb 02 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170202-alt1
- repocop cronbuild 20170202. At your service.

* Thu Jan 26 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170125-alt1
- repocop cronbuild 20170126. At your service.

* Wed Jan 18 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170117-alt1
- repocop cronbuild 20170118. At your service.

* Tue Jan 17 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170116-alt1
- repocop cronbuild 20170117. At your service.

* Sat Jan 14 2017 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20170113-alt1
- repocop cronbuild 20170114. At your service.

* Thu Dec 29 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20161228-alt1
- repocop cronbuild 20161229. At your service.

* Wed Dec 28 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20161227-alt1
- repocop cronbuild 20161228. At your service.

* Sun Dec 25 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20161224-alt1
- repocop cronbuild 20161225. At your service.

* Sat Dec 24 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.7.20161223-alt1
- repocop cronbuild 20161224. At your service.

* Fri Dec 16 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161216-alt1
- repocop cronbuild 20161216. At your service.

* Thu Dec 08 2016 Dmitry V. Levin <ldv@altlinux.org> 1:2.3.6.20161208-alt1
- 20161206 -> 20161208.
- Serial -> Epoch.

* Tue Dec 06 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161205-alt1
- repocop cronbuild 20161206. At your service.

* Mon Dec 05 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161204-alt1
- repocop cronbuild 20161205. At your service.

* Sun Nov 27 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161126-alt1
- repocop cronbuild 20161127. At your service.

* Fri Nov 25 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161124-alt1
- repocop cronbuild 20161125. At your service.

* Tue Nov 22 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161122-alt1
- repocop cronbuild 20161122. At your service.

* Mon Nov 14 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161114-alt1
- repocop cronbuild 20161114. At your service.

* Sat Nov 12 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161112-alt1
- repocop cronbuild 20161112. At your service.

* Fri Nov 11 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161110-alt1
- repocop cronbuild 20161111. At your service.

* Tue Nov 08 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161107-alt1
- repocop cronbuild 20161108. At your service.

* Mon Nov 07 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161106-alt1
- repocop cronbuild 20161107. At your service.

* Fri Nov 04 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161104-alt1
- repocop cronbuild 20161104. At your service.

* Thu Nov 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161102-alt1
- repocop cronbuild 20161103. At your service.

* Tue Nov 01 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161101-alt1
- repocop cronbuild 20161101. At your service.

* Mon Oct 31 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161030-alt1
- repocop cronbuild 20161031. At your service.

* Wed Oct 26 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161026-alt1
- repocop cronbuild 20161026. At your service.

* Fri Oct 21 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161020-alt1
- repocop cronbuild 20161021. At your service.

* Thu Oct 20 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161019-alt1
- repocop cronbuild 20161020. At your service.

* Mon Oct 10 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161009-alt1
- repocop cronbuild 20161010. At your service.

* Wed Oct 05 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161004-alt1
- repocop cronbuild 20161005. At your service.

* Mon Oct 03 2016 Cronbuild Service <cronbuild@altlinux.org> 1:2.3.6.20161001-alt1
- repocop cronbuild 20161003. At your service.

* Sat Sep 17 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.7.20160916-alt1
- repocop cronbuild 20160917. At your service.

* Tue Sep 13 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.7.20160913-alt1
- repocop cronbuild 20160913. At your service.

* Mon Sep 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160912-alt1
- repocop cronbuild 20160912. At your service.

* Sun Sep 11 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160911-alt1
- repocop cronbuild 20160911. At your service.

* Sat Sep 10 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160910-alt1
- repocop cronbuild 20160910. At your service.

* Thu Sep 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160908-alt1
- repocop cronbuild 20160908. At your service.

* Wed Sep 07 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160907-alt1
- repocop cronbuild 20160907. At your service.

* Tue Sep 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160906-alt1
- repocop cronbuild 20160906. At your service.

* Fri Sep 02 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160902-alt1
- repocop cronbuild 20160902. At your service.

* Tue Aug 30 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160829-alt1
- repocop cronbuild 20160830. At your service.

* Sat Aug 27 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160827-alt1
- repocop cronbuild 20160827. At your service.

* Wed Aug 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160824-alt1
- repocop cronbuild 20160824. At your service.

* Sun Aug 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160820-alt1
- repocop cronbuild 20160821. At your service.

* Sat Aug 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160819-alt1
- repocop cronbuild 20160820. At your service.

* Wed Aug 17 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160816-alt1
- repocop cronbuild 20160817. At your service.

* Mon Aug 15 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160815-alt1
- repocop cronbuild 20160815. At your service.

* Tue Aug 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160808-alt1
- repocop cronbuild 20160809. At your service.

* Sat Aug 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160806-alt1
- repocop cronbuild 20160806. At your service.

* Sat Jul 30 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160730-alt1
- repocop cronbuild 20160730. At your service.

* Sat Jul 16 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160716-alt1
- repocop cronbuild 20160716. At your service.

* Wed Jul 13 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160712-alt1
- repocop cronbuild 20160713. At your service.

* Sat Jul 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160708-alt1
- repocop cronbuild 20160709. At your service.

* Mon Jul 04 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160703-alt1
- repocop cronbuild 20160704. At your service.

* Sat Jun 25 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160624-alt1
- repocop cronbuild 20160625. At your service.

* Thu Jun 23 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160622-alt1
- repocop cronbuild 20160623. At your service.

* Wed Jun 22 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160621-alt1
- repocop cronbuild 20160622. At your service.

* Sun Jun 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160618-alt1
- repocop cronbuild 20160619. At your service.

* Sat Jun 18 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160617-alt1
- repocop cronbuild 20160618. At your service.

* Wed Jun 15 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160614-alt1
- repocop cronbuild 20160615. At your service.

* Sun Jun 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160612-alt1
- repocop cronbuild 20160612. At your service.

* Fri Jun 10 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160610-alt1
- repocop cronbuild 20160610. At your service.

* Thu Jun 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160608-alt1
- repocop cronbuild 20160609. At your service.

* Mon Jun 06 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160605-alt1
- repocop cronbuild 20160606. At your service.

* Sat Jun 04 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160604-alt1
- repocop cronbuild 20160604. At your service.

* Fri Jun 03 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160603-alt1
- repocop cronbuild 20160603. At your service.

* Thu Jun 02 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160601-alt1
- repocop cronbuild 20160602. At your service.

* Sat May 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160527-alt1
- repocop cronbuild 20160528. At your service.

* Wed May 25 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160524-alt1
- repocop cronbuild 20160525. At your service.

* Fri May 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160519-alt1
- repocop cronbuild 20160520. At your service.

* Sun May 15 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160515-alt1
- repocop cronbuild 20160515. At your service.

* Wed May 11 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160510-alt1
- repocop cronbuild 20160511. At your service.

* Mon May 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160508-alt1
- repocop cronbuild 20160509. At your service.

* Sun May 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160507-alt1
- repocop cronbuild 20160508. At your service.

* Sat Apr 30 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160429-alt1
- repocop cronbuild 20160430. At your service.

* Sat Apr 23 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160423-alt1
- repocop cronbuild 20160423. At your service.

* Tue Apr 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160416-alt1
- repocop cronbuild 20160419. At your service.

* Wed Apr 13 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160413-alt1
- repocop cronbuild 20160413. At your service.

* Tue Apr 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160411-alt1
- repocop cronbuild 20160412. At your service.

* Sat Apr 09 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160408-alt1
- repocop cronbuild 20160409. At your service.

* Tue Apr 05 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160404-alt1
- repocop cronbuild 20160405. At your service.

* Sat Apr 02 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160402-alt1
- repocop cronbuild 20160402. At your service.

* Fri Apr 01 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160401-alt1
- repocop cronbuild 20160401. At your service.

* Mon Mar 28 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160327-alt1
- repocop cronbuild 20160328. At your service.

* Thu Mar 24 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160323-alt1
- repocop cronbuild 20160324. At your service.

* Tue Mar 22 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160322-alt1
- repocop cronbuild 20160322. At your service.

* Mon Mar 21 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160321-alt1
- repocop cronbuild 20160321. At your service.

* Sun Mar 20 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160319-alt1
- repocop cronbuild 20160320. At your service.

* Sat Mar 19 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160318-alt1
- repocop cronbuild 20160319. At your service.

* Mon Mar 14 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160314-alt1
- repocop cronbuild 20160314. At your service.

* Sat Mar 12 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160311-alt1
- repocop cronbuild 20160312. At your service.

* Tue Mar 08 2016 Cronbuild Service <cronbuild@altlinux.org> 2.3.6.20160307-alt1
- repocop cronbuild 20160308. At your service.

* Fri Feb 26 2016 Dmitry V. Levin <ldv@altlinux.org> 2.3.6.20160226-alt1
- Initial revision.
