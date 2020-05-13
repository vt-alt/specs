# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: lxqt-session
Version: 0.15.0
Release: alt1

Summary: Session manager
License: LGPL
Group: Graphical desktop/Other

Url: https://lxqt.org
Source0: %name-%version.tar
Source1: 08lxqt

BuildRequires: gcc-c++ cmake rpm-macros-cmake git-core
BuildRequires: liblxqt-devel qt5-base-devel qt5-tools-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: rpm-build-xdg libqtxdg-devel xdg-utils xdg-user-dirs
BuildRequires: libudev-devel

Requires: lxqt-themes
Requires: xdg-utils

Provides: razorqt-session = %version
Obsoletes: razorqt-session < 0.7.0

Conflicts: lxqt-common <= 0.11.0

%description
%summary

%prep
%setup
# https://bugzilla.altlinux.org/32657
sed -i 's,Exec=,Exec=%_bindir/,' xsession/lxqt.desktop.in

%build
%cmake -DPULL_TRANSLATIONS=OFF \
       -DUPDATE_TRANSLATIONS=OFF \
       -DBUNDLE_XDG_UTILS=No
%cmake_build

%install
%cmakeinstall_std
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/X11/wmsession.d/08lxqt

%files
%_man1dir/*
%_bindir/*
%_xdgconfigdir/*/*
%_desktopdir/*.desktop
%_datadir/xsessions/*.desktop
%_datadir/kdm/sessions/*.desktop
%_datadir/lxqt/*
%_sysconfdir/X11/wmsession.d/08lxqt
%doc AUTHORS CHANGELOG LICENSE README.md

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Fri May 25 2018 Anton Midyukov <antohami@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Sun Oct 22 2017 Michael Shigorin <mike@altlinux.org> 0.12.0-alt1
- 0.12.0
- tweak desktop file (see also #32657)

* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 0.11.0-alt1
- 0.11.0

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 0.10.0-alt1
- 0.10.0

* Sun Feb 08 2015 Michael Shigorin <mike@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Oct 15 2014 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed May 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- replace razorqt-session

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- added wmsession file

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- initial release

