Name:     touchegg
Version:  2.0.5
Release:  alt0.1.p9

Summary:  Linux multi-touch gesture recognizer
License:  GPL-3.0
Group:    Other
Url:      https://github.com/JoseExposito/touchegg

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch1:   touchegg-alt-remove-static.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libudev-devel
BuildRequires: libinput-devel
BuildRequires: libpugixml-devel
BuildRequires: libcairo-devel
BuildRequires: libXtst-devel
BuildRequires: libXrandr-devel
BuildRequires: libgtk+3-devel
BuildRequires: libpcre-devel
BuildRequires: libstdc++-devel-static

%description
Touchegg is an app that runs in the background and transform the gestures you
make on your touchpad into visible actions in your desktop.

%prep
%setup
#patch1 -p1

%build
%add_optflags -std=c++17
%cmake -GNinja \
       -Wno-dev
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%preun
%preun_service %name

%post
%post_service %name

%files
%doc *.md
%_bindir/%name
%_sysconfdir/xdg/autostart/%name.desktop
%_datadir/%name
%_unitdir/%name.service

%changelog
* Thu Jan 07 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt0.1.p9
- Backport to p9 branch.

* Thu Jan 07 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version.

* Sun Jan 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
