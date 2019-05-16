%define nm_version 1.1.90
%define nm_applet_version 1.1.90
%define nm_applet_name NetworkManager-applet-gtk
%define git_date %nil
#define git_date .git20151024

%def_without libnm_glib

%define _unpackaged_files_terminate_build 1

Name: NetworkManager-ssh
Version: 1.2.10
Release: alt1%git_date
License: %gpl2plus
Group: System/Configuration/Networking
Summary: NetworkManager VPN plugin for SSH
Url: https://github.com/danfruehauf/NetworkManager-ssh
# git:git://github.com/danfruehauf/NetworkManager-ssh.git
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: intltool
BuildRequires: libnm-devel >= %nm_version
BuildRequires: libnma-devel >= %nm_applet_version
%if_with libnm_glib
BuildRequires: NetworkManager-devel >= %nm_version
BuildRequires: libnm-glib-vpn-devel >= %nm_version
BuildRequires: libnm-gtk-devel >= %nm_applet_version
%endif
BuildRequires: libgtk+3-devel
BuildRequires: libsecret-devel

Requires: NetworkManager-daemon   >= %nm_version
Requires: openssh

%description
This package contains software for integrating VPN capabilities with
the OpenSSH server with NetworkManager.

%package gtk
License: %gpl2plus
Summary: Applications for use %name with %nm_applet_name
Group: Graphical desktop/GNOME
Requires: %nm_applet_name >= %nm_applet_version
Requires: %name = %version-%release

Obsoletes: %name-gnome < 0.9.1-alt2
Provides: %name-gnome = %version-%release

%description gtk
This package contains applications for use with
NetworkManager panel applet.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--libexecdir=%_libexecdir/NetworkManager \
	--localstatedir=%_var \
%if_without libnm_glib
	--without-libnm-glib \
%endif
	--disable-silent-rules \
	--enable-more-warnings=error
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%files
%doc AUTHORS README README.md
%_libexecdir/NetworkManager/nm-ssh-service
%config %_sysconfdir/dbus-1/system.d/nm-ssh-service.conf
%if_with libnm_glib
%config %_sysconfdir/NetworkManager/VPN/nm-ssh-service.name
%endif
%config %_libexecdir/NetworkManager/VPN/nm-ssh-service.name

%files gtk -f %name.lang
%if_with libnm_glib
%_libdir/NetworkManager/libnm-ssh-properties.so
%endif
%_libexecdir/NetworkManager/nm-ssh-auth-dialog
%_datadir/gnome-vpn-properties/*
%_libdir/NetworkManager/libnm-vpn-plugin-ssh.so
%_datadir/appdata/*.xml

%exclude %_libdir/NetworkManager/*.la

%changelog
* Wed May 15 2019 Mikhail Efremov <sem@altlinux.org> 1.2.10-alt1
- Updated to 1.2.10.

* Tue Mar 19 2019 Mikhail Efremov <sem@altlinux.org> 1.2.9-alt1
- Updated to 1.2.9.

* Fri Nov 09 2018 Mikhail Efremov <sem@altlinux.org> 1.2.8-alt1
- Updated to 1.2.8.

* Tue Sep 18 2018 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt3
- Temporary don't treat warnings as errors.

* Wed Aug 01 2018 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt2
- Disable libnm-glib-* support.
- Fix build without libnm-glib-*.

* Tue Dec 19 2017 Mikhail Efremov <sem@altlinux.org> 1.2.7-alt1
- Updated to 1.2.7.

* Tue Jul 11 2017 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1
- Disable silent rules.
- Fix from upstream:
  + Update README.md.
- Updated to 1.2.6.

* Wed Oct 05 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1
- Updated to 1.2.1.

* Thu Apr 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Thu Jan 21 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.git20151024
- Upstream git snapshot (master branch).

* Fri Jul 17 2015 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1
- Updated BR.
- Updated to 0.9.4.

* Tue Jun 24 2014 Mikhail Efremov <sem@altlinux.org> 0.9.3-alt1
- Update requires: NetworkManager -> NetworkManager-daemon.
- Update BR: Use libnm-glib-vpn-devel.
- Updated to 0.9.3.

* Wed Apr 02 2014 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt4
- Temporary don't treat warrnings as errors.
- Rebuild with NetworkManager-applet-gtk-0.9.9.

* Thu Oct 03 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt3
- Fix build: Avoid deprecation warnings.

* Mon Sep 16 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt2
- Don't reload DBUS configuration during install.
- Rename 'gnome' subpackage to 'gtk'.

* Mon Jul 22 2013 Mikhail Efremov <sem@altlinux.org> 0.9.1-alt1
- Updated from upstream git (e5e66fd96141).
- Updated to 0.9.1.

* Tue Apr 16 2013 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1.git20130405
- Initial build.

