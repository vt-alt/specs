Name: kde5-ksplash-disabled
Version: 0.1
Release: alt1
Summary: Disabled KDE5 ksplash
License: GPLv2+
Group: Graphical desktop/KDE
URL: https://altlinux.org
BuildArch: noarch

%description
%summary

%install
mkdir -p %buildroot%_sysconfdir/kf5/xdg
cat > %buildroot%_sysconfdir/kf5/xdg/ksplashrc <<EOF
[KSplash]
Engine=none
EOF

%files
%_sysconfdir/kf5/xdg/ksplashrc

%changelog
* Thu Sep 19 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT

