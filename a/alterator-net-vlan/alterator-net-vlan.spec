Name: alterator-net-vlan
Version: 0.1.2
Release: alt1

Source:%name-%version.tar

Summary: alterator module for VLAN interfaces
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.24 libshell >= 0.0.1-alt4
Requires: alterator-l10n
Requires: alterator-sh-functions >= 0.12-alt1
Requires: alterator-net-functions >= 2.0.0
Requires: alterator-net-eth >= 5.0.0
Requires: etcnet

BuildPreReq: alterator >= 4.7-alt3

BuildArch: noarch

BuildRequires: alterator

%description
alterator module for VLAN network interfaces

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_backend3dir/*

%changelog
* Thu Jul 11 2019 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Fix Qt interface.

* Mon Mar 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Fix QT UI.

* Wed Mar 23 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

