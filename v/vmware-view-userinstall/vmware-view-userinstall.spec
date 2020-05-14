Name: vmware-view-userinstall
Version: 5.4.1
Release: alt2

Summary: VMware Horizon Client pre-installation scripts
License: Public domain
Group: System/Configuration/Other

Url: http://altlinux.org/vmware-view
Source: %name-%version.tar

ExclusiveArch: %ix86 x86_64

Requires: vmware-view-preinstall >= 5.4.1
Requires: userinstall-helper >= 0.2
Requires: python-modules-sqlite3

BuildArch: noarch

%define uinstdir %_cachedir/userinstall

%description
Install this package if you need a script to help install
VMware-Horizon-Client-%version bundle on this system.

%prep
%setup

%install
install -pDm644 vmware-view.desktop \
	%buildroot%_desktopdir/vmware-view.desktop
install -pDm644 vmware-view.png \
	%buildroot%_pixmapsdir/vmware-view.png
install -pDm755 vmware-view.sh %buildroot%_bindir/vmware-view

mkdir -p %buildroot%uinstdir
cp -a checksums %buildroot%uinstdir/goodsums

%files
# this one will clobber itself during real vmware-view deployment
# that shouldn't get clobbered again by this package upgrade
%config(noreplace) %_bindir/vmware-view
%_desktopdir/vmware-view.desktop
%_pixmapsdir/vmware-view.png
%uinstdir/goodsums/*

%changelog
* Sun May 10 2020 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt2
- Requires for new version of vmware-view-preinstall.

* Tue May 05 2020 Andrey Cherepanov <cas@altlinux.org> 5.4.1-alt1
- New version.

* Fri Jan 24 2020 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version.

* Sun Jan 12 2020 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version (VMware-Horizon-Client-5.2.0-14604769).

* Wed Jul 24 2019 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version (VMware-Horizon-Client-5.1.0-13956721).

* Mon Mar 18 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt4
- Make package noarch.

* Thu Mar 14 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt3
- Fix URL for Zenity dialog.
- Use latest desktop file and icon from VMware Horizon Client 4.10.0.

* Tue Mar 12 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt2
- Support both clients for i586 and x86_64.
- Add python-modules-sqlite3 to requirements.

* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- support for VMware-Horizon-Client-4.10.0-11053294.x86.bundle

* Tue Apr 04 2017 Michael Shigorin <mike@altlinux.org> 3.4.0-alt4
- sync ExclusiveArch: to vmware-view-preinstall 3.4.0-alt4
  to avoid an unmet dependency

* Wed Oct 28 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt2
- rewrote to use userinstall-sh-functions too

* Fri Sep 25 2015 Michael Shigorin <mike@altlinux.org> 3.4.0-alt1
- split off vmware-view-preinstall 3.4.0-alt2
- rewrote to rely upon userinstall-helper

