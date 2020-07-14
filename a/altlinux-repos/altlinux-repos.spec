Name: altlinux-repos
Version: 0.9
Release: alt7

Summary: A set of ALT repos desktop files
License: GPL
Group: System/Configuration/Packaging
BuildArch: noarch

Source: %name-%version.tar

Conflicts: apt-conf-branch < 7.0.0-alt3
Conflicts: apt-conf-sisyphus < 7.0-alt2

%description
A set of desktop files describing ALTLinux repositories and mirrors

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/apt
cp -a mirrors repositories %buildroot%_sysconfdir/apt/

%files
%_sysconfdir/apt/mirrors
%_sysconfdir/apt/repositories

%changelog
* Wed Jul 08 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9-alt7
- Dropped desktop file for armh port of p9.

* Thu Jun 18 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9-alt6
- Added p9 repo for dcdy and msu mirrors.
- Dropped desktop file for armh port of sisyphus.

* Thu Apr 09 2020 Andrey Cherepanov <cas@altlinux.org> 0.9-alt5
- Use altlinux-repos/repositories/cert8.desktop from c8 for c8.

* Thu Apr 09 2020 Andrey Cherepanov <cas@altlinux.org> 0.9-alt4
- Add c8 branch (ALT #38334).

* Mon Jun 03 2019 Ivan A. Melnikov <iv@altlinux.org> 0.9-alt3
- Add noarch for p9_mipsel.

* Mon May 27 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9-alt2
- arei@: added armh, mipsel and riscv64 ports information.

* Tue May 14 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9-alt1
- Added p9 branch.

* Fri Aug 25 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8-alt1
- Added mirror.cs.msu.ru mirror (ALT#33802).

* Mon Dec 05 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.1-alt1
- Removed accidentally added vendors.list.d/alt.list file.

* Mon Dec 05 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7-alt1
- Added mirror.datacenter.by mirror.

* Wed Jun 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6-alt1
- Dropped ibiblio.org mirror.
- Moved vendors.list.d/alt.list from apt-conf-{branch,sisyphus}.

* Thu Apr 14 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5-alt1
- Add p8 branch.

* Wed Dec 24 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4-alt1
- Dropped ftp.linux.kiev.ua mirror (ALT#30104, #30598).

* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1
- Informika mirror is dead, remove it

* Wed Sep 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2-alt1
- Sisyphus has arepo.
- Add t6 and t7 branches.

* Mon Jun 10 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Create separate package for altlinux repos desktop files
