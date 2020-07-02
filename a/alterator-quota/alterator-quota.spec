Name: alterator-quota
Version: 1.5.2
Release: alt1

Packager: Vladislav Zavjalov <slazav@altlinux.org>

Summary: alterator module for managing filesystem quotas
License: GPL
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/Alterator

Source: %name-%version.tar

BuildArch: noarch

Requires: alterator >= 3.9-alt3
Requires: quota

Requires: alterator-sh-functions >= 0.10-alt1
Conflicts: alterator-fbi < 2.10-alt5

BuildPreReq: alterator >= 3.9-alt3

%description
alterator module for managing filesystem quotas

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_backend3dir/*
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/*
%_bindir/*

%changelog
* Tue Jun 30 2020 Sergey V Turchin <zerg@altlinux.org> 1.5.2-alt1
- allow to work with root filesystem

* Thu Jul 03 2014 Mikhail Efremov <sem@altlinux.org> 1.5.1-alt1
- alterator-quota: Show first mountpoint only.

* Sun Feb 28 2010 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt2
- fix error with empty lists in ajax.scm

* Tue Feb 16 2010 Vladislav Zavjalov <slazav@altlinux.org> 1.5-alt1
- HTML UI: show user list when fs list is empty
- QT UI: fix error with empty lists

* Wed Nov 18 2009 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1
- use workflow 'none'

* Fri Sep 11 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt3
- update transtlations in desktop-file (closes: #21536)

* Fri Aug 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt2
- change ru label in desktop (closes: #21146)

* Thu May 07 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.3-alt1
- use getent for list users, use edquota for read quota information

* Wed Apr 15 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.2-alt1
- ajax.scm: fix error on empty lists

* Mon Apr 06 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- fix labels
- fix on-init settings in html UI

* Wed Apr 01 2009 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- first version

