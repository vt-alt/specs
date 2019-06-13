Name: fonts-ttf-unifont
Version: 12.1.01
Release: alt1

Summary: GNU Unifont, with glyphs for every printable code point in the Unicode 8.0
License: GPLv2
Group: System/Fonts/True type
Url: http://unifoundry.com/unifont.html
Source: unifont-12.1.01.ttf

BuildArch: noarch
Requires(pre): fontconfig

BuildRequires: rpm-build-fonts

%description
GNU Unifont, with glyphs for every printable code point in the Unicode
Basic Multilingual Plane (BMP). The BMP occupies the first 65,536
code points of the Unicode space, denoted as U+0000..U+FFFF.

%prep
cp %SOURCE0 .

%build
%install
%ttf_fonts_install unifont

%files -f unifont.files
%changelog
* Tue May 28 2019 Fr. Br. George <george@altlinux.ru> 12.1.01-alt1
- Autobuild version bump to 12.1.01

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 10.0.07-alt1
- Autobuild version bump to 10.0.07

* Mon Sep 18 2017 Fr. Br. George <george@altlinux.ru> 10.0.06-alt1
- Autobuild version bump to 10.0.06

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 10.0.05-alt1
- Autobuild version bump to 10.0.05

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 9.0.06-alt1
- Autobuild version bump to 9.0.06

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 9.0.04-alt1
- Autobuild version bump to 9.0.04

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 9.0.01-alt1
- Autobuild version bump to 9.0.01

* Mon Aug 31 2015 Fr. Br. George <george@altlinux.ru> 8.0.01-alt1
- Autobuild version bump to 8.0.01

* Sun Aug 30 2015 Fr. Br. George <george@altlinux.ru> 0.0.01-alt1
- Initial empty build

