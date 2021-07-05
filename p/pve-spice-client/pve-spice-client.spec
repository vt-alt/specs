Name: pve-spice-client
Version: 2.0.0
Release: alt3

Summary: PVE Spice Client
License: GPLv3
Group: Networking/Remote access

Url: https://github.com/mxmvoronov/pve-spice-client.git 
Source: %name-%version.tar

Requires: virt-viewer
Provides: spice-ec = %EVR
Obsoletes: spice-ec < %EVR

BuildRequires(pre): rpm-macros-cmake cmake
BuildRequires: qt5-base-devel libqtkeychain-qt5-devel

%description
Spice remote viewer launcher

%prep
%setup

%build
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README.md
%_bindir/*
%_desktopdir/*

%changelog
* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2
- NMU: remove %ubt from release

* Thu Jun 21 2018 Maxim Voronov <mvoronov@altlinux.org> 2.0.0-alt1%ubt
- Totally changed GUI.
- Added possibility to run remote viewer from command line.

* Sat Jun 09 2018 Maxim Voronov <mvoronov@altlinux.org> 1.2.1-alt1%ubt
- fixed segmentation fault on quit with new server

* Fri Mar 30 2018 Maxim Voronov <mvoronov@altlinux.org> 1.2.0-alt1%ubt
- new version

* Wed Mar 21 2018 Maxim Voronov <mvoronov@altlinux.org> 1.1.1-alt1%ubt
- new version

* Mon Mar 19 2018 Maxim Voronov <mvoronov@altlinux.org> 1.1.0-alt1%ubt
- new version

* Thu Mar 15 2018 Maxim Voronov <mvoronov@altlinux.org> 1.0.1-alt1%ubt
- new version

* Mon Mar 12 2018 Maxim Voronov <mvoronov@altlinux.org> 1.0.0-alt1%ubt
- initial build

