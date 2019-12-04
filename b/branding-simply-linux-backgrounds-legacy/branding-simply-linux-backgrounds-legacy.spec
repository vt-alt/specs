Name: branding-simply-linux-backgrounds-legacy
Version: 9.0
Release: alt1
BuildArch: noarch

BuildRequires(pre): rpm-macros-branding

Source: backgrounds-%version.tar

Group: Graphics
Summary: Legacy SL backgrounds
License: CC-BY-NC-SA-3.0+
%branding_add_conflicts simply-linux backgrounds-legacy

Conflicts: branding-simply-linux-xfce-settings < 7.98.1-alt1

%define _unpackaged_files_terminate_build 1

%description
This package contains legacy backgrounds from
Simply Linux versions 5, 6, 7.

%package -n branding-simply-linux-backgrounds-vladstudio
Summary: Backgrounds from vladstudio.com
License: CC-BY-NC-SA-3.0+
Group: Graphics
%branding_add_conflicts simply-linux backgrounds-vladstudio
Conflicts: branding-simply-linux-xfce-settings < 7.98.1-alt1

%description -n branding-simply-linux-backgrounds-vladstudio
This package contains backgrounds from vladstudio.com.

%package -n branding-simply-linux-backgrounds8
Group: Graphics
Summary: Backgrounds for SL-8
License: CC-BY-NC-SA-3.0+
BuildArch: noarch
%branding_add_conflicts simply-linux backgrounds8

%description -n branding-simply-linux-backgrounds8
This package contains backgrounds for Simply Linux 8.

%prep
%setup -n backgrounds-%version

%install
mkdir -p %buildroot%_datadir/backgrounds/xfce/
cp -a vladstudio* %buildroot%_datadir/backgrounds/xfce/
install -m 644 slinux_*.{jpg,png} %buildroot%_datadir/backgrounds/xfce/

%files
%_datadir/backgrounds/xfce/slinux_march_2013_*
%_datadir/backgrounds/xfce/slinux_new_year2011_*
%_datadir/backgrounds/xfce/slinux_spring_*

%files -n branding-simply-linux-backgrounds-vladstudio
%_datadir/backgrounds/xfce/vladstudio*

%files -n branding-simply-linux-backgrounds8
%_datadir/backgrounds/xfce/slinux_june_2017_*

%changelog
* Mon Dec 02 2019 Mikhail Efremov <sem@altlinux.org> 9.0-alt1
- Add backgrounds for Simply Linux 8.

* Fri Jun 16 2017 Mikhail Efremov <sem@altlinux.org> 8.0-alt1
- Separated from branding-simply-linux-xfce-settings.

