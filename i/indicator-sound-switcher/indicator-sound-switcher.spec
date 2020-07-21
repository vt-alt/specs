%define modulename indicator_sound_switcher

Name:    indicator-sound-switcher
Version: 2.3.4
Release: alt1

Summary: Sound input/output selector indicator for Linux
License: GPL-3.0
Group:   Development/Python3
URL:     https://github.com/yktoo/indicator-sound-switcher

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-dev python3-module-setuptools
%add_typelib_req_skiplist typelib(AyatanaAppIndicator3)

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

%find_lang %name

%files -f %name.lang
%doc *.md
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.svg
%_man1dir/*
%python3_sitelibdir/%modulename
%python3_sitelibdir/*.egg-info
%_sysconfdir/xdg/autostart/%name.desktop

%changelog
* Tue Jul 21 2020 Anton Midyukov <antohami@altlinux.org> 2.3.4-alt1
- Initial build for Sisyphus
