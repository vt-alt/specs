Name: mpv-not-acceleration
Version: 0.1
Release: alt1
Summary: Config mpv for system without hardware acceleration
License: GPLv2+
Group: Video
URL: https://altlinux.org
BuildArch: noarch

%description
This config mpv contains settings for system without hardware
acceleration.

%install
mkdir -p %buildroot%_sysconfdir/mpv
cat > %buildroot%_sysconfdir/mpv/mpv.conf <<EOF
# HW acceleration is not supported on this platform yet
vo=x11
sws-scaler=fast-bilinear
EOF

%files
%_sysconfdir/mpv/mpv.conf

%changelog
* Thu Sep 19 2019 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build for ALT
