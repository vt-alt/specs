Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-alternatives
BuildRequires: /usr/bin/desktop-file-validate /usr/bin/gtkdocize gcc-c++ glib2-devel pkgconfig(check) pkgconfig(gconf-2.0) pkgconfig(gdk-2.0) pkgconfig(gio-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
%add_findreq_skiplist %_libexecdir/xinputinfo.sh
%add_findreq_skiplist /etc/X11/xinit/xinitrc.d/50-xinput.sh
BuildRequires: libdbus-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		imsettings
Version:	1.8.1
Release:	alt2_1
License:	LGPLv2+
URL:		https://tagoh.bitbucket.org/%{name}/
BuildRequires:	desktop-file-utils
BuildRequires:	gettext gettext-tools
BuildRequires:	libtool automake autoconf
BuildRequires:	libgio >= 2.32.0, gobject-introspection-devel gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires:	libnotify-devel libnotify-gir-devel
BuildRequires:	libX11-devel, libgxim-devel >= 0.5.0
%if !0%{?rhel}
BuildRequires:	libxfconf-devel
%endif
Source0:	https://bitbucket.org/tagoh/%{name}/downloads/%{name}-%{version}.tar.bz2
## Fedora specific: run IM for certain languages only
Patch0:		%{name}-constraint-of-language.patch
## Fedora specific: Disable XIM support
Patch1:		%{name}-disable-xim.patch
## Fedora specific: Enable xcompose for certain languages
Patch2:		%{name}-xinput-xcompose.patch
## Fedora specific: Force enable the IM management on imsettings for Cinnamon
Patch3:		%{name}-force-enable-for-cinnamon.patch

Summary:	Delivery framework for general Input Method configuration
Requires:	xinit >= 1.0.2
Requires:	%{name}-libs = %{version}-%{release}
Requires:	%{name}-desktop-module = %{version}-%{release}
Requires:	%{name}-gsettings
Source44: import.info

%description
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the core DBus services and some utilities.

%package	libs
Group: Development/Other
Summary:	Libraries for imsettings

%description	libs
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the shared library for imsettings.

%package	devel
Group: Development/Other
Summary:	Development files for imsettings
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pkgconfig
Requires:	libgio

%description	devel
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the development files to make any
applications with imsettings.

%package	xim
Group: System/Base
Summary:	XIM support on imsettings
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser

%description	xim
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working with XIM.

%package	gsettings
Group: System/Base
Summary:	GSettings support on imsettings
Requires:	%{name} = %{version}-%{release}
Requires:	dconf libdconf
Provides:	imsettings-desktop-module = %{version}-%{release}
Provides:	%{name}-gnome = %{version}-%{release}
Obsoletes:	%{name}-gnome < 1.5.1-3

%description	gsettings
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on
GNOME and Cinnamon which requires GSettings in their
own XSETTINGS daemons.

%package	qt
Group: System/Base
Summary:	Qt support on imsettings
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser
Provides:	imsettings-desktop-module = %{version}-%{release}

%description	qt
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Qt
applications.

%if !0%{?rhel}
%package	xfce
Group: System/Base
Summary:	Xfce support on imsettings
Requires:	%{name} = %{version}-%{release}
Requires:	im-chooser-xfce
Requires:	xfce4-settings >= 4.5.99.1
Provides:	imsettings-desktop-module = %{version}-%{release}

%description	xfce
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Xfce.  

%package	lxde
Group: System/Base
Summary:	LXDE support on imsettings
Requires:	%{name} = %{version}-%{release}
Requires:	lxde-settings-daemon
# Hack for upgrades: see https://bugzilla.redhat.com/show_bug.cgi?id=693809
Requires:	lxde-lxsession
Requires:	/usr/bin/lxsession
Requires:	im-chooser
Provides:	imsettings-desktop-module = %{version}-%{release}

%description	lxde
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on LXDE.

%package	mate
Group: System/Base
Summary:	MATE support on imsettings
Requires:	%{name} = %{version}-%{release}
# need to keep more deps for similar reason to https://bugzilla.redhat.com/show_bug.cgi?id=693809
Requires:	mate-settings-daemon >= 1.5.0
Requires:	mate-session
Requires:	im-chooser
Provides:	imsettings-desktop-module = %{version}-%{release}

%description	mate
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on MATE.

%package	cinnamon
Group: System/Base
Summary:	Cinnamon support on imsettings
Requires:	%{name} = %{version}-%{release}
# need to keep more deps for similar reason to https://bugzilla.redhat.com/show_bug.cgi?id=693809
Requires:	cinnamon cinnamon-data
Requires:	cinnamon-session
Requires:	im-chooser
Provides:	imsettings-desktop-module = %{version}-%{release}

%description	cinnamon
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Cinnamon.
%endif

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -f
%configure	\
	--with-xinputsh=50-xinput.sh \
	--disable-static \
	--disable-schemas-install

%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

# change the file attributes
chmod 0755 $RPM_BUILD_ROOT%{_libexecdir}/imsettings-target-checker.sh
chmod 0755 $RPM_BUILD_ROOT%{_libexecdir}/xinputinfo.sh
chmod 0755 $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh

# clean up the unnecessary files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/libimsettings-{gconf,mateconf}.so
%if 0%{?rhel}
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/libimsettings-{lxde,xfce,mate-gsettings}.so
%endif

desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/imsettings-start.desktop

%find_lang %{name}
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_imsettings<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_sysconfdir}/X11/xinit/xinput.d/none.conf	10
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_imsettings<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_sysconfdir}/X11/xinit/xinput.d/xcompose.conf	20
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/xinputrc_imsettings<<EOF
%{_sysconfdir}/X11/xinit/xinputrc	%{_sysconfdir}/X11/xinit/xinput.d/xim.conf	30
EOF


#%%check
## Disable it because it requires DBus session
# make check

%post
systemctl reload dbus.service 2>&1 || :

%postun
if [ "$1" = 0 ]; then
	:
	systemctl reload dbus.service 2>&1 || :
fi



%files	-f %{name}.lang
%_altdir/xinputrc_imsettings
%_altdir/xinputrc_imsettings
%_altdir/xinputrc_imsettings
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/imsettings
%{_bindir}/imsettings-info
%{_bindir}/imsettings-list
%{_bindir}/imsettings-reload
%{_bindir}/imsettings-switch
%{_libexecdir}/imsettings-check
%{_libexecdir}/imsettings-daemon
%{_libexecdir}/xinputinfo.sh
%{_libexecdir}/imsettings-functions
%{_libexecdir}/imsettings-target-checker.sh
%{_datadir}/dbus-1/services/*.service
%{_datadir}/pixmaps/*.png
%{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh
%{_sysconfdir}/X11/xinit/xinput.d
%{_sysconfdir}/xdg/autostart/imsettings-start.desktop
%{_mandir}/man1/imsettings-*.1*

%files	libs
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libimsettings.so.5*

%files	devel
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/imsettings
%{_libdir}/libimsettings.so
%{_libdir}/pkgconfig/imsettings.pc
%{_libdir}/girepository-*/IMSettings-*.typelib
%{_datadir}/gir-*/IMSettings-*.gir
%{_datadir}/gtk-doc/html/imsettings

%files	xim
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/imsettings-xim
%{_libdir}/imsettings/libimsettings-xim.so

%files	gsettings
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-gsettings.so

%files	qt
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-qt.so

%if !0%{?rhel}
%files	xfce
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-xfce.so

%files	lxde
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-lxde.so

%files	mate
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-mate-gsettings.so

# note: done by robot; when cinnamon is supported, not just unifdef me, notify viy@ too
%files cinnamon
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-cinnamon-gsettings.so


%endif
%changelog
* Thu Aug 29 2019 Michael Shigorin <mike@altlinux.org> 1.8.1-alt2_1
- reenable cinnamon subpackage for %%e2k

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1
- update to new release by fcimport

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_7
- merged git fixes to hook, sync with fc

* Mon Aug 20 2018 Mikhail Efremov <sem@altlinux.org> 1.7.3-alt1_2.2
- Fix build: add libdbus-devel to BR.
- Rebuild with libxfconf-0.so.3.

* Thu Mar 01 2018 Grigory Ustinov <grenka@altlinux.org> 1.7.3-alt1_2.1
- NMU: Disable cinnamon section for e2k.

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1_2
- update to new release by fcimport

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.2-alt1_5
- update to new version by fcimport

* Sat Nov 07 2015 Ilya Mashkin <oddity@altlinux.ru> 1.6.8-alt1
- 1.6.8
- update patchset

* Tue Aug 26 2014 Ilya Mashkin <oddity@altlinux.ru> 1.6.7-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1_3
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1_2
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_1
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_3
- update to new release by fcimport

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- update to new release by fcimport

* Tue Feb 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- update to new release by fcimport

* Tue Feb 12 2013 Cronbuild Service <cronbuild@altlinux.org> 1.5.1-alt2_2
- rebuild to get rid of unmets

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_2
- initial fc import

