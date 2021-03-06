Summary: Translations for kicad
Name: kicad-i18n
Version: 5.1.9
Release: alt1.1
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
License: GPLv2+
Group: Engineering
Url: https://gitlab.com/kicad/code/kicad-i18n
BuildArch: noarch
BuildRequires(pre): cmake rpm-macros-cmake

%description
Translations for kicad

%prep
%setup -n %name-%version

%build
%cmake -DKICAD_I18N_UNIX_STRICT_PATH=ON ..
%cmake_build

%install
%cmakeinstall_std
%find_lang kicad

%files -f kicad.lang

%changelog
* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 5.1.9-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sat Feb 13 2021 Anton Midyukov <antohami@altlinux.org> 5.1.9-alt1
- new version 5.1.9
- Update URL tag

* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 5.1.4-alt1
- new version 5.1.4

* Thu Apr 25 2019 Anton Midyukov <antohami@altlinux.org> 5.1.2-alt1
- new version 5.1.2

* Fri Mar 15 2019 Anton Midyukov <antohami@altlinux.org> 5.1.0-alt1
- new version 5.1.0

* Thu Jan 03 2019 Anton Midyukov <antohami@altlinux.org> 5.0.2-alt1
- new version 5.0.2

* Sun Nov 18 2018 Anton Midyukov <antohami@altlinux.org> 5.0.1-alt1
- new version 5.0.1

* Thu Jul 19 2018 Anton Midyukov <antohami@altlinux.org> 5.0.0-alt1.rc3
- release candidate 5.0.0-rc3

* Wed Aug 30 2017 Anton Midyukov <antohami@altlinux.org> 4.0.7-alt1
- new version 4.0.7

* Wed Mar 01 2017 Anton Midyukov <antohami@altlinux.org> 4.0.6-alt1
- new version 4.0.6

* Wed Feb 22 2017 Anton Midyukov <antohami@altlinux.org> 4.0.5-alt1
- new version 4.0.5

* Wed Aug 31 2016 Anton Midyukov <antohami@altlinux.org> 4.0.4-alt1
- New version 4.0.4

* Thu Jul 21 2016 Anton Midyukov <antohami@altlinux.org> 4.0.2-alt1
- First build for ALT Linux Sisyphus.
