Name: lxqt
Version: 0.15
Release: alt1
Summary: Meta package for install LxQt
Group: Graphical desktop/Other
License: GPL
Url: https://lxqt.org
BuildArch: noarch

%description
%summary

%package mini
Summary: Meta package for install LxQt
Group: Graphical desktop/Other
BuildArch: noarch

# core componenets
Requires: lxmenu-data
Requires: lxqt-about >= %version
Requires: lxqt-themes >= %version
Requires: lxqt-globalkeys >= %version
Requires: lxqt-notificationd >= %version
Requires: lxqt-panel >= %version
Requires: lxqt-powermanagement >= %version
Requires: lxqt-qtplugin >= %version
Requires: lxqt-runner >= %version
Requires: lxqt-session >= %version
Requires: pcmanfm-qt >= %version
Requires: lxqt-config >= %version
Requires: qterminal >= %version
Requires: lxqt-policykit >= %version
# system configuration tools
Requires: lxqt-config >= %version
Requires: obconf-qt >= %version
# themes
Requires: icon-theme-oxygen
# system components
Requires: openbox-base openbox-autostart

Obsoletes: lxqt < 0.14
Obsoletes: lxqt-l10n < 0.14
Obsoletes: compton-conf-l10n < 0.14
Obsoletes: libfm-qt-l10n < 0.14
Obsoletes: lximage-qt-l10n < 0.14
Obsoletes: obconf-qt-l10n < 0.14
Obsoletes: pavucontrol-qt-l10n < 0.14
Obsoletes: pcmanfm-qt-l10n < 0.14
Obsoletes: qterminal-l10n < 0.14
Obsoletes: qtermwidget-l10n < 0.14

%description mini
%summary

%package regular
Summary: Meta package for install regular-lxqt
Group: Graphical desktop/Other
BuildArch: noarch

Requires: lxqt-mini
# sound mixer
Requires: pavucontrol-qt >= %version
# for pavucontrol-qt
Requires: pulseaudio-daemon pulseaudio-utils alsa-plugins-pulse
# optional components
Requires: lxqt-openssh-askpass >= %version
Requires: lxqt-admin >= %version
# archiver
Requires: lxqt-archiver
# task-manager
Requires: qps
# clipboard history applet
Requires: qlipper
# fonts
Requires: fonts-ttf-core
# pdf-viewer
Requires: qpdfview
# image-viewer
Requires: lximage-qt
# themes for window manager
Requires: openbox-themes
# Graphical wrapper for su
Requires: lxqt-sudo

%description regular
%summary

%files mini
%files regular

%changelog
* Sun Apr 26 2020 Anton Midyukov <antohami@altlinux.org> 0.15-alt1
- lxqt-regular: requires lxqt-sudo
- lxqt-regular: requires lxqt-archiver instead file-roller

* Sat Nov 30 2019 Anton Midyukov <antohami@altlinux.org> 0.14-alt4
- lxqt-regular: requires fonts-ttf-core (Closes: 37511)

* Wed Jun 26 2019 Anton Midyukov <antohami@altlinux.org> 0.14-alt3
- lxqt requires openbox-themes

* Mon Jun 24 2019 Anton Midyukov <antohami@altlinux.org> 0.14-alt2
- Requires openbox-base, openbox-autostart instead openbox

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14-alt1
- new version 0.14
- new package lxqt-regular
- replaced lxqt to lxqt-mini

* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13-alt1
- new version 0.13

* Mon Mar 26 2018 Anton Midyukov <antohami@altlinux.org> 0.12-alt2
- Added Url

* Fri Mar 23 2018 Anton Midyukov <antohami@altlinux.org> 0.12-alt1
- Initial build for ALT
