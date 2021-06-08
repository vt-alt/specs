%define _unpackaged_files_terminate_build 1

%define shortname qalculate

Name: qalculate-gtk
Version: 3.19.0
Release: alt1
Summary: A very versatile desktop calculator - GTK+ version.
Group: Office
License: GPL-2.0+
Url: https://qalculate.github.io/

# https://github.com/Qalculate/qalculate-gtk.git
Source: %name-%version.tar

# https://github.com/Qalculate/qalculate-gtk/issues/246
Patch1: fix_autogen.patch

BuildRequires: gcc-c++ libcln-devel libdbus-glib libglade-devel libgmp-devel libgnome-devel
BuildRequires: libqalculate-devel >= %version
BuildRequires: perl-XML-Parser scrollkeeper yelp intltool
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(libxml-2.0) pkgconfig(gtk+-3.0)

%description
A GTK+ graphical interface for Qalculate!

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure --disable-rpath --enable-static=no
%make_build

%install
%makeinstall_std

desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Calculator \
	--add-category=GTK \
	%buildroot%_desktopdir/qalculate-gtk.desktop

%find_lang %name

%files -f %name.lang
%doc COPYING
%doc AUTHORS ChangeLog README README.md
%_bindir/%name
%_libdir/qalculate-search-provider
%_man1dir/*.1*
%_datadir/metainfo/%name.appdata.xml
%_defaultdocdir/%name
%_desktopdir/*
%_iconsdir/hicolor/*x*/apps/%{shortname}.png
%_iconsdir/hicolor/scalable/apps/%{shortname}.svg
%_datadir/dbus-1/services/io.github.Qalculate.SearchProvider.service
%_datadir/gnome-shell/search-providers/io.github.Qalculate.search-provider.ini

%changelog
* Sat May 29 2021 Anton Midyukov <antohami@altlinux.org> 3.19.0-alt1
- Updated to upstream version 3.19.0.

* Tue Mar 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.17.0-alt1
- Updated to upstream version 3.17.0.

* Wed Jan 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.16.0-alt1
- Updated to upstream version 3.16.0.

* Mon Sep 28 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.13.0-alt1
- Updated to upstream version 3.13.0.

* Tue Aug 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.12.1-alt1
- Updated to upstream version 3.12.1.

* Thu Jul 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.0-alt1
- Updated to upstream version 3.11.0.

* Fri Jun 19 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.10.0-alt1
- Updated to upstream version 3.10.0.

* Wed Apr 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.0-alt1.a
- Updated to upstream version 3.8.0a.

* Fri Aug 02 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0.

* Mon Jun 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.0-alt1
- Updated to upstream version 3.2.0.

* Tue Jan 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.2-alt1
- Updated to upstream version 2.8.2.

* Fri Jul 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.1-alt1
- Updated to upstream version 2.6.1.

* Fri May 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1
- Updated to upstream version 2.5.0.

* Mon Sep 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.7-alt3.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qalculate-gtk

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.7-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for qalculate-gtk

* Mon Feb 14 2011 Nick S. Grechukh <gns@altlinux.ru> 0.9.7-alt3
- rebuilt

* Thu Apr 22 2010 Nick S. Grechukh <gns@altlinux.ru> 0.9.7-alt2
- build fixed (intltool)

* Thu Apr 22 2010 Alexey Morsov <swi@altlinux.ru> 0.9.7-alt1
- new version

* Thu Nov 27 2008 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt1.1
- build with cln 1.2.2

* Mon Jun 18 2007 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt1
- version 0.9.6
- clean spec for git

* Wed Dec 20 2006 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1
- initial build for sisyphus


