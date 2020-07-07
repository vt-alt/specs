Name: installer-feature-create-vmbr
Version: 1.1
Release: alt1

Summary: Create empty vmbr0 bridge after PVE install
License: GPLv2
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
BuildArch: noarch

%description
Create empty vmbr0 bridge after PVE installation

%package stage3
Summary: Create empty vmbr0 bridge after PVE installation
License: GPLv2
Group: System/Configuration/Other

%description stage3
Create empty vmbr0 bridge after PVE installation

%prep
%setup -q

%install
%makeinstall

%files stage3
# _datadir/install2/postinstall.d/*
%_datadir/install2/preinstall.d/*

%changelog
* Mon Jul 06 2020 Alexey Shabalin <shaba@altlinux.org> 1.1-alt1
- Cleanup default server etcnet options

* Thu Feb 13 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.0-alt1
- Initial build.

