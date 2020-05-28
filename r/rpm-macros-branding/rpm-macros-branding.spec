Name: rpm-macros-branding
Version: 1.0.5
Release: alt1
Summary: RPM helper macros to build branding packages
License: %gpl2plus
Group: Development/Other
Source0: branding.rpm.macros
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

%description
%summary.

%build
cp %SOURCE0 branding.rpm.macros

VARIANTS="\
Platform6-server-light \
alt-desktop \
alt-education \
alt-server \
alt-server-v \
alt-spserver \
alt-spworkstation \
alt-starterkit \
alt-workstation \
alt-tonk \
altlinux-backup-server \
altlinux-centaurus \
altlinux-desktop \
altlinux-gnome-desktop \
altlinux-kdesktop \
altlinux-lite \
altlinux-lxdesktop \
altlinux-office-desktop \
altlinux-office-server \
altlinux-p7 \
altlinux-school-server \
altlinux-sisyphus \
altlinux-spt \
altlinux-starterkit \
altlinux-tablet \
altlinux-workbench \
basealt-server \
basealt-starterkit \
basealt-workstation \
informika-schoolmaster \
ivk-chainmail \
lxde-desktop \
lxde-school-lite \
school-junior \
school-lite \
school-master \
school-server \
school-teacher \
school-terminal \
simply-linux \
sisyphus-server-light \
xalt-kworkstation \
"
sed -e "s/@BRANDING_VARIANTS@/$VARIANTS/" -i branding.rpm.macros

%install
install -d -m 0755 %buildroot%_rpmmacrosdir
install -m 0644 branding.rpm.macros %buildroot%_rpmmacrosdir/branding

%files
%_rpmmacrosdir/*

%changelog
* Wed May 13 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.5-alt1
- Added alt-spserver and alt-spworkstation

* Mon Dec 02 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.4-alt1
- Added server-v.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Add alt-tonk

* Wed Aug 31 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2-alt1
- Added 10 more brandings.

* Tue Aug 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1-alt1
- Added xalt-kworkstation.

* Tue Aug 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1
- Initial build.
