Name:    netplan
Version: 0.97
Release: alt2

Summary: Backend-agnostic network configuration in YAML
License: GPL-3.0
Group:   System/Configuration/Networking
URL:     https://github.com/CanonicalLtd/netplan

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  %_bindir/pandoc

Requires:       iproute2

%add_python3_path %_datadir/%name

Source:  %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%build
%make_build

%install
%makeinstall_std DOCDIR=%_docdir/%name-%version
mkdir -p %buildroot%_sysconfdir/%name

%files
%_sbindir/%name
/lib/systemd/system-generators/%name
/lib/%name
%_unitdir/%{name}*
%_datadir/bash-completion/completions/%name
%_datadir/%name
%dir %_sysconfdir/%name
%doc *.md
%_man5dir/%{name}*
%_man8dir/%{name}*

%changelog
* Thu Aug 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.97-alt2
- Remove Requires to systemd and systemd-networkd, it could use NetworkManager

* Fri Jul 26 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.97-alt1
- Initial build for Sisyphus
