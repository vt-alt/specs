%global _unpackaged_files_terminate_build 1
%define _localstatedir %_var

Name: connman
Version: 1.37
Release: alt1

Summary: ConnMan is a daemon for managing internet connections.
License: %gpl2only
Group: Networking/Other
Url: http://connman.net/

Packager: Alexey Gladkov <legion@altlinux.ru>

Source: %name-%version.tar
Source1: connmand.init
Source4: connman-openresolv.path
Source5: connman-openresolv.service

Patch0: add-options-file.patch
Patch1: connman-add-libs.patch
Patch2: connman-main-conf.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ glib2-devel iptables iptables-devel libdbus-devel wpa_supplicant
BuildRequires: gtk-doc libgnutls-devel libreadline-devel
BuildRequires: openconnect openvpn vpnc xl2tpd
BuildRequires: ppp-devel
BuildRequires: libpolkit-devel libselinux-devel
BuildRequires: systemd-devel libsystemd-devel

Provides: network-config-subsystem

%description
The Connection Manager (ConnMan) project provides a daemon for
managing internet connections within embedded devices running
the Linux operating system. ConnMan is designed to be slim
and to use as few resources as possible, so it can be easily integrated.
It is a fully modular system that can be extended, through plug-ins,
to support all kinds of wired or wireless technologies.
The plug-in approach allows for easy adaption and modification
for various use cases.

%package -n %name-docs
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description -n %name-docs
This package contains documentation files for %name

%package -n %name-devel
Summary: Include files for development with ConnMan Library
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
The Connection Manager (ConnMan) project provides a daemon for managing
internet connections within embedded devices running the Linux operating system.

This package contains include files required for development %name-based software.

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
%autoreconf
%configure \
	--enable-pie \
	--with-systemdunitdir=%_unitdir \
	--with-tmpfilesdir=%_tmpfilesdir \
	--enable-datafiles \
	--enable-client \
	--enable-nmcompat \
	--enable-polkit \
	--enable-selinux \
	--enable-openconnect \
	--enable-openvpn \
	--enable-vpnc \
	--enable-l2tp \
	--enable-pptp \
    --with-dns-backend=internal \
#
%make_build runstatedir=/run

%install
%makeinstall_std

mkdir -p -- \
	%buildroot%_initdir \
	%buildroot%_sysconfdir/sysconfig \
	%buildroot%_localstatedir/lib/%name \
	%buildroot%_localstatedir/lib/%name-vpn \
#

echo 'CONNMAND_OPTS="-r"' > %buildroot%_sysconfdir/sysconfig/connman

install -pm0755 -D %SOURCE1          %buildroot%_initdir/connmand
install -pm0644 -D src/main.conf     %buildroot%_sysconfdir/connman/main.conf

ln -s connman.service %buildroot%_unitdir/connmand.service

find %buildroot%_libdir/%name -name '*.la' -delete

mkdir -p %buildroot%_unitdir/multi-user.target.wants
install -m644 %SOURCE4 %buildroot%_unitdir/connman-openresolv.path
install -m644 %SOURCE5 %buildroot%_unitdir/connman-openresolv.service
ln -s ../connman-openresolv.path %buildroot%_unitdir/multi-user.target.wants

%post
%post_service connmand

%preun
%preun_service connmand

%files
%_sbindir/*
%_bindir/*

%dir %_sysconfdir/connman
%config(noreplace) %_sysconfdir/connman/main.conf
%config(noreplace) %_sysconfdir/sysconfig/connman

%_datadir/dbus-1/system.d/*.conf
%_datadir/dbus-1/system-services/*.service

%_initdir/*
%_unitdir/*
%_tmpfilesdir/*

%dir %_libdir/%name
%dir %_libdir/%name/plugins*
%_libdir/%name/plugins*/*.so

%dir %_libdir/%name/scripts
%_libdir/%name/scripts/*.so
%_libdir/%name/scripts/*-script

%_datadir/polkit-1/actions/*

%_localstatedir/lib/%name
%_localstatedir/lib/%name-vpn

%_man1dir/*
%_man5dir/*
%_man8dir/*

%files -n %name-docs
%doc AUTHORS README TODO README ChangeLog doc/*.txt

%files -n %name-devel
%_pkgconfigdir/*.pc
%_includedir/*

%changelog
* Tue Sep 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.37-alt1
- 1.37

* Wed Nov 28 2018 Alexey Shabalin <shaba@altlinux.org> 1.36-alt1
- 1.36

* Fri Feb 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.35-alt3%ubt
- Fixed build with new kernel headers.

* Mon Sep 11 2017 Paul Wolneykien <manowar@altlinux.org> 1.35-alt2%ubt
- Fix: Explicitly set runstatedir=/run (closes: #33848).

* Wed Aug 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.35-alt1%ubt
- 1.35

* Wed Feb 15 2017 Alexey Shabalin <shaba@altlinux.ru> 1.33-alt1
- 1.33
- add systemd unit for update resolv.conf with openresolv

* Mon Apr 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.32-alt1
- 1.32

* Thu Aug 28 2014 Michael Shigorin <mike@altlinux.org> 1.20-alt4
- Provides: network-config-subsystem (closes: #30263)

* Tue Jul 01 2014 Michael Shigorin <mike@altlinux.org> 1.20-alt3
- symlink connman.service as connmand.service (closes: #30147)

* Tue Dec 10 2013 Alexey Gladkov <legion@altlinux.ru> 1.20-alt2
- Rebuilt with new version.

* Thu Dec 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1.20-alt1
- Fresh up to v1.20 with the help of cronbuild and update-source-functions.

* Tue Oct 29 2013 Alexey Gladkov <legion@altlinux.ru> 1.19-alt2
- Add missing directories, manpages and config file.
- Add connmanctl utility.
- Fix sysvinit startup script.

* Tue Oct 15 2013 Cronbuild Service <cronbuild@altlinux.org> 1.19-alt1
- Fresh up to v1.19 with the help of cronbuild and update-source-functions.

* Tue Sep 03 2013 Cronbuild Service <cronbuild@altlinux.org> 1.18-alt1
- Fresh up to v1.18 with the help of cronbuild and update-source-functions.

* Mon Aug 19 2013 Cronbuild Service <cronbuild@altlinux.org> 1.17-alt1
- Fresh up to v1.17 with the help of cronbuild and update-source-functions.

* Wed Jul 17 2013 Cronbuild Service <cronbuild@altlinux.org> 1.16-alt1
- Fresh up to v1.16 with the help of cronbuild and update-source-functions.

* Sun Jun 02 2013 Cronbuild Service <cronbuild@altlinux.org> 1.15-alt1
- Fresh up to v1.15 with the help of cronbuild and update-source-functions.

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 1.14-alt1
- Fresh up to v1.14 with the help of cronbuild and update-source-functions.

* Fri Apr 12 2013 Paul Wolneykien <manowar@altlinux.org> 1.13-alt1
- Remove the already applied ip6_addr patch.
- Fresh up to v1.13 with the help of cronbuild and update-source-functions.

* Mon Apr 08 2013 Aleksey Avdeev <solo@altlinux.ru> 1.12-alt1
- New version 1.1

* Wed Mar 06 2013 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt2.1
- Rebuilt with libxtables.so.10.

* Mon Feb 04 2013 Paul Wolneykien <manowar@altlinux.ru> 1.11-alt2
- Disable DNS proxy by default.
- Make use of /etc/sysconfig/connman.

* Sat Feb 02 2013 Cronbuild Service <cronbuild@altlinux.org> 1.11-alt1
- repocop cronbuild 20130202. At your service.

* Tue Jan 22 2013 Paul Wolneykien <manowar@altlinux.ru> 1.10-alt2
- Fix the storagedir location.

* Fri Jan 18 2013 Paul Wolneykien <manowar@altlinux.ru> 1.10-alt1
- Build with additional features/plugins.
- New version 1.10.
- Add cronbuild scripts.

* Thu Jan 17 2013 Paul Wolneykien <manowar@altlinux.ru> 0.77-alt6
- Initial build for ALT Linux Sisyphus.
