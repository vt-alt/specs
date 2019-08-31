%define _unpackaged_files_terminate_build 1

Summary:   Package management service
Name:      packagekit
Version:   1.1.12
Release:   alt8
License:   GPLv2+ and LGPLv2+
Group:     Other
URL:       http://www.freedesktop.org/software/PackageKit/

# https://github.com/hughsie/PackageKit.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: libsqlite3-devel
BuildRequires: libpolkit-devel
BuildRequires: libsystemd-devel
BuildRequires: autoconf-archive
BuildRequires: libapt-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: appstream-devel

BuildRequires: vala-tools
BuildRequires: libgtk+2-devel
BuildRequires: libgtk+3-devel

BuildRequires: boost-devel

%description
PackageKit is a D-Bus abstraction layer that allows the session user
to manage packages in a secure way using a cross-distro,
cross-architecture API.

%package -n lib%name-glib
Summary: GLib libraries for accessing PackageKit
Group: Other
Requires: %name = %EVR

%description -n lib%name-glib
GLib libraries for accessing PackageKit.
Group: Other

%package cron
Summary: Cron job and related utilities for PackageKit
Group: Other
Requires: %name = %EVR

%description cron
Crontab and utilities for running PackageKit as a cron job.

%package -n lib%name-glib-devel
Summary: GLib Libraries and headers for PackageKit
Group: Development/Other
Requires: lib%name-glib = %EVR

%description -n lib%name-glib-devel
GLib headers and libraries for PackageKit.

%package gstreamer-plugin
Summary: Install GStreamer codecs using PackageKit
Group: Other
Requires: lib%name-glib = %EVR

%description gstreamer-plugin
The PackageKit GStreamer plugin allows any Gstreamer application to install
codecs from configured repositories using PackageKit.

%package -n lib%name-gtk3-module
Summary: Install fonts automatically using PackageKit
Group: Other
Requires: lib%name-glib = %EVR

%description -n lib%name-gtk3-module
The PackageKit GTK3+ module allows any Pango application to install
fonts from configured repositories using PackageKit.

%package command-not-found
Summary: Ask the user to install command line programs automatically
Group: Other
Requires: lib%name-glib = %EVR

%description command-not-found
A simple helper that offers to install new packages on the command line
using PackageKit.

%package -n python3-module-%name
Summary: Python3 backend for PackageKit
Group: Development/Python3
BuildArch: noarch
Requires: %name = %EVR

%description -n python3-module-%name
Python3 backend for PackageKit.

%prep
%setup
%patch1 -p1

%build
%add_optflags -std=c++14
%add_optflags -D_FILE_OFFSET_BITS=64
%define _configure_script ./autogen.sh
%configure \
	--disable-static \
	--localstatedir=%_var \
	--disable-bash-completion \
	--enable-aptcc \
	--enable-python3 \
	--disable-dummy \
	--disable-daemon-tests

%make_build

%install
%makeinstall_std

find %buildroot -name '*.la' -delete

# Create directories for downloaded appstream data
mkdir -p %buildroot%_cachedir/app-info/{icons,xmls}
touch %buildroot%_cachedir/PackageKit/groups.sqlite

# create a link that GStreamer will recognise
pushd %buildroot%_libexecdir
ln -s pk-gstreamer-install gst-install-plugins-helper
popd

# get rid of test backend
rm -f %buildroot%_libdir/packagekit-backend/libpk_backend_test_*.so
rm -rf %buildroot%_datadir/PackageKit/helpers/test_spawn

# Following scripts seems unused, and it needs to be patched for ALT should it be used
rm -f %buildroot%_datadir/PackageKit/pk-upgrade-distro.sh

touch %buildroot%_localstatedir/PackageKit/upgrade_lock

%find_lang PackageKit

%post
SYSTEMCTL=systemctl
if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
	"$SYSTEMCTL" daemon-reload
	if [ "$RPM_INSTALL_ARG1" -eq 1 ]; then
		"$SYSTEMCTL" -q preset %name
	else
		# only request stop of service, don't restart it
		"$SYSTEMCTL" is-active --quiet %name && %_bindir/pkcon quit ||:
	fi
fi

%preun
%preun_service %name ||:

%triggerin -- librpm7
# only on update of librpm7
if [ $2 -eq 2 ] ; then
	# if librpm7 is updated, prohibit packagekit to start and ask it to quit
	touch %_localstatedir/PackageKit/upgrade_lock
	SYSTEMCTL=systemctl
	sd_booted && $SYSTEMCTL is-active --quiet %name && %_bindir/pkcon quit ||:
fi
:

%triggerpostun -- librpm7
# after librpm7 is updated, allow packagekit to restart on request
# it may be a good idea to move this to librpm7 package's delayed actions
rm -f %_localstatedir/PackageKit/upgrade_lock ||:
:

%files -f PackageKit.lang
%doc COPYING
%doc README AUTHORS NEWS
%dir %_datadir/PackageKit
%dir %_datadir/PackageKit/helpers
%dir %_sysconfdir/PackageKit
%dir %_localstatedir/PackageKit
%dir %_cachedir/app-info
%dir %_cachedir/app-info/icons
%dir %_cachedir/app-info/xmls
%dir %_cachedir/PackageKit
%ghost %verify(not md5 size mtime) %_cachedir/PackageKit/groups.sqlite
%dir %_libdir/packagekit-backend
%config(noreplace) %_sysconfdir/PackageKit/PackageKit.conf
%config(noreplace) %_sysconfdir/PackageKit/Vendor.conf
%config %_sysconfdir/dbus-1/system.d/*
%_man1dir/pkcon.1*
%_man1dir/pkmon.1*
%_datadir/polkit-1/actions/*.policy
%_datadir/polkit-1/rules.d/*
%_libexecdir/packagekitd
%_libexecdir/packagekit-direct
%_bindir/pkmon
%_bindir/pkcon
%exclude %_libdir/libpackagekit*.so.*
%ghost %verify(not md5 size mtime) %_localstatedir/PackageKit/transactions.db
%ghost %_localstatedir/PackageKit/upgrade_lock
%_datadir/dbus-1/system-services/*.service
%_datadir/dbus-1/interfaces/*.xml
%_unitdir/packagekit-offline-update.service
%_unitdir/packagekit.service
%_unitdir/system-update.target.wants/
%_libexecdir/pk-*offline-update
%config %_sysconfdir/apt/apt.conf.d/20packagekit
%_libdir/packagekit-backend/libpk_backend_aptcc.so
%_datadir/PackageKit/helpers/aptcc

%files -n lib%name-glib
%_libdir/*packagekit-glib2.so.*
%_libdir/girepository-1.0/PackageKitGlib-1.0.typelib

%files cron
%config %_sysconfdir/cron.daily/packagekit-background.cron
%config(noreplace) %_sysconfdir/sysconfig/packagekit-background

%files gstreamer-plugin
%_libexecdir/pk-gstreamer-install
%_libexecdir/gst-install-plugins-helper

%files -n lib%name-gtk3-module
%_libdir/gtk-2.0/modules/*.so
%_libdir/gtk-3.0/modules/*.so
%_libdir/gnome-settings-daemon-3.0/gtk-modules/*.desktop

%files command-not-found
%_sysconfdir/profile.d/*
%_libexecdir/pk-command-not-found
%config(noreplace) %_sysconfdir/PackageKit/CommandNotFound.conf

%files -n lib%name-glib-devel
%_libdir/libpackagekit-glib2.so
%_pkgconfigdir/packagekit-glib2.pc
%dir %_includedir/PackageKit
%dir %_includedir/PackageKit/packagekit-glib2
%_includedir/PackageKit/packagekit-glib*/*.h
%_datadir/gir-1.0/PackageKitGlib-1.0.gir
%_datadir/gtk-doc/html/PackageKit
%_datadir/vala/vapi/packagekit-glib2.vapi

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Fri Aug 30 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.12-alt8
- Fixed processing obsoletes during upgrades (Closes: #36342).

* Wed Jun 26 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1.12-alt7
- Fixed support for refreshCache action. (Thx Aleksei Nikiforov darktemplar@)

* Thu Jun 13 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.12-alt6
- Rebuilt with new Apt.

* Wed Feb 06 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.12-alt5
- Fixed crash during showing errors.
- Enabled verbose logging for packagekit service.

* Fri Feb 01 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.12-alt4
- Fixed stopping service without finishing current request.

* Thu Jan 31 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.12-alt3
- Updated build dependencies.

* Mon Jan 28 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.12-alt2
- Forced stopping and blocked restarting of packagekit service during
  upgrade of librpm7, improved locking (Closes: #35987).

* Tue Dec 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.12-alt1
- Initial build for ALT.
