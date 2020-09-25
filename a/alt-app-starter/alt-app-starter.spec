%define _unpackaged_files_terminate_build 1

Name: alt-app-starter
Version: 1.3.0
Release: alt1
Group: Graphical desktop/KDE
Summary: The tool to run programs as another user
License: GPLv2
URL: http://git.altlinux.org/gears/a/alt-app-starter.git

%K5init altplace

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-kdesu-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-kpty-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: boost-devel-headers
Requires: /usr/bin/xvt

%description
Alt-App-Starter is the tool to quickly run programs as another user.
This tool was designed to work with KDE.

%prep
%setup

%build
%K5build

%install
%K5install

%find_lang --with-qt --all-name %name

%files -f %name.lang
%doc COPYING*
%_K5bin/*
%_K5xdgapp/*.desktop

%changelog
* Wed Sep 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt1
- Code cleanup and minor bugfixes.

* Wed Jul 15 2020 Pavel Moseev <mars@altlinux.org>  1.2.9-alt1
- cleanup and optimize code

* Mon Jul 13 2020 Pavel Moseev <mars@altlinux.org>  1.2.8-alt1
- fix priority setting from current user
- update translation
- cleanup and optimize code

* Thu Jul 09 2020 Pavel Moseev <mars@altlinux.org>  1.2.7-alt1
- fix priority setting from current user

* Mon Jul 06 2020 Pavel Moseev <mars@altlinux.org>  1.2.6-alt1
- clean code

* Mon Jun 29 2020 Pavel Moseev <mars@altlinux.org>  1.2.5-alt1
- add checkbox to close terminal application after command execution

* Tue Jun 23 2020 Pavel Moseev <mars@altlinux.org>  1.2.4-alt1
- add choosing application from list and folder

* Fri Jun 19 2020 Pavel Moseev <mars@altlinux.org>  1.2.3-alt1
- clean code

* Fri Jun 19 2020 Pavel Moseev <mars@altlinux.org>  1.2.2-alt1
- add saving history of entered commands

* Mon Jun 08 2020 Pavel Moseev <mars@altlinux.org>  1.2.1-alt1
- clean code

* Thu Jun 04 2020 Pavel Moseev <mars@altlinux.org>  1.2.0-alt1
- new version

* Mon Jun 01 2020 Pavel Moseev <mars@altlinux.org>  1.1.9-alt1
- clean code

* Tue Apr 28 2020 Pavel Moseev <mars@altlinux.org>  1.1.8-alt1
- fix process priority change

* Mon Apr 27 2020 Pavel Moseev <mars@altlinux.org>  1.1.7-alt1
- fix process priority change

* Fri Apr 24 2020 Pavel Moseev <mars@altlinux.org>  1.1.6-alt1
- update translation
- add process priority change

* Fri Feb 14 2020 Pavel Moseev <mars@altlinux.org>  1.1.5-alt1
- update translation
- update user interface
- fix launch applications

* Wed Feb 12 2020 Pavel Moseev <mars@altlinux.org>  1.1.4-alt1
- fix launch of console applications (closes: #37872)
- add tooltip for launching console applications (closes: #37979)
- fix program behavior when entering an invalid password (closes: #38053)
- fix some user interface elements
- update translation

* Thu Feb 06 2020 Pavel Moseev <mars@altlinux.org>  1.1.3-alt1
- fix launch of console applications (closes: #37872)
- upgrade the utility description in the spec file (closes: #37978)
- fix behavior of utility after successful application launch (closes: #37979)
- fix some user interface elements (closes: #37980)
- preferred terminal emulator is read from system settings

* Fri Jan 24 2020 Pavel Moseev <mars@altlinux.org>  1.1.2-alt1
- fix user interface translation

* Thu Jan 23 2020 Pavel Moseev <mars@altlinux.org>  1.1.1-alt1
- fix application title icon (#37870)
- fix behavior of alt-app-starter utility after starting selected app. (#37871)
- removed unused interface elements (#37873)

* Mon Jan 13 2020 Pavel Moseev <mars@altlinux.org>  1.1.0-alt1
- First version. Initial build

