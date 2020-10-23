%define _localstatedir %{_var}

Name: fprintd
Version: 1.90.1
Release: alt1
Summary: D-Bus service for Fingerprint reader access
Group: System/Servers
Url: https://www.freedesktop.org/wiki/Software/fprint/fprintd
License: GPLv2+

Source: %name-%version.tar
Source1: system-auth-fprintd
Patch: %name-%version.patch
Patch1: %name-0.4.1-alt-build.patch
Patch3: %name-0.4.1-alt-pam_docs.patch

BuildRequires(pre): meson
BuildRequires: libdbus-glib-devel
BuildRequires: pkgconfig(libfprint-2) > 0.1.0
BuildRequires: pkgconfig(glib-2.0) pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gmodule-2.0) pkgconfig(polkit-gobject-1) >= 0.91 pkgconfig(gio-2.0) >= 2.26
BuildRequires: libpam0-devel
BuildRequires: gtk-doc intltool
BuildRequires: /usr/bin/pod2man /usr/bin/xmllint /usr/bin/xsltproc docbook-dtds
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libpamtest)
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-dbus
BuildRequires: python3-module-dbusmock
BuildRequires: python3-module-libpamtest
BuildRequires: python3(gi)

%description
D-Bus service to access fingerprint readers.

%package -n pam_fprintd
Summary: PAM module for fingerprint authentication
Provides: pam_fprint
Obsoletes: pam_fprint <= 0.2
Group: System/Base

%description -n pam_fprintd
PAM module that uses the fprintd D-Bus service for fingerprint
authentication.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/Other
BuildArch: noarch

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%prep
%setup -q
%patch -p1
#patch1 -p1
#patch3 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%doc README COPYING AUTHORS TODO
%config(noreplace) %_sysconfdir/fprintd.conf
#_sysconfdir/pam.d/system-auth-fprintd
%_datadir/dbus-1/system.d/net.reactivated.Fprint.conf
%_bindir/fprintd-*
%_prefix/lib/fprintd
%_unitdir/fprintd.service
%_datadir/dbus-1/system-services/net.reactivated.Fprint.service
%_datadir/polkit-1/actions/net.reactivated.fprint.device.policy
#dir %_localstatedir/lib/fprint
%_man1dir/fprintd.1*

%files -n pam_fprintd
%doc pam/README
/%_lib/security/pam_fprintd.so
%_man8dir/pam_fprintd.8*

%files devel
#_datadir/gtk-doc/html/fprintd
%_datadir/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%_datadir/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
* Thu Aug 13 2020 Anton Farygin <rider@altlinux.ru> 1.90.1-alt1
- 1.90.1

* Sat Mar 17 2018 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1.1
- NMU: added URL

* Fri Oct 26 2012 Ivan Ovcherenko <asdus@altlinux.org> 0.4.1-alt1
- 0.4.1 with git updates (closes: #27851)

* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt3
- ported to PolicyKit 1

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt2
- pam_fprintd: fixed obsoletes

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release
