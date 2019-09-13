%define _libexecdir %_prefix/libexec

%define xdg_name org.gnome.FileRoller
%define xdg_name1 org.gnome.ArchiveManager
%define ver_major 3.32
%def_disable packagekit
%def_disable magic
%def_enable libarchive
%def_enable nautilus_actions
%define nau_api_ver 3.0

Name: file-roller
Version: %ver_major.2
Release: alt1

Summary: An archive manager for GNOME
Summary (ru_RU.UTF-8): Архиватор для GNOME
Group: File tools
License: %gpl2plus
Url: http://fileroller.sourceforge.net

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Patch1: %name-3.3.90-alt-zip_command.patch
# find ./ -type f -print0| xargs -r0 subst "s/x-lzop-compressed-tar/x-tzo/" --
Patch2: %name-3.31.92-alt-tar.lzo_mime_type.patch

# From configure.in
%define glib_ver 2.36.0
%define gtk_ver 3.12.0
%define libarchive_ver 3.0.0
%define desktop_file_utils_ver 0.8

Requires: tar gzip bzip2 ncompress lzop binutils arj lha unrar zip unzip p7zip lzma-utils xz
# Requires: cdrecord # for .iso support
Requires: dconf gnome-icon-theme

BuildRequires(pre): meson
BuildRequires: rpm-build-gnome rpm-build-licenses yelp-tools
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: intltool >= 0.35.0
BuildPreReq: desktop-file-utils >= %desktop_file_utils_ver
BuildRequires: libjson-glib-devel libnotify-devel
%{?_enable_libarchive:BuildRequires: libarchive-devel >= %libarchive_ver}
%{?_enable_magic:BuildRequires: libmagic-devel}
%{?_enable_nautilus_actions:BuildRequires: libnautilus-devel}

%description
File Roller is an archive manager for the GNOME environment.  This means that
you can : create and modify archives; view the content of an archive; view a
file contained in the archive; extract files from the archive.
File Roller is only a front-end (a graphical interface) to archiving programs
like tar and zip. The supported file types are :
    * Tar archives uncompressed (.tar) or compressed with
          * gzip (.tar.gz, .tgz)
          * bzip (.tar.bz, .tbz)
          * bzip2 (.tar.bz2, .tbz2)
          * compress (.tar.Z, .taz)
          * lzop (.tar.lzo, .tzo)
    * Ar archives (.ar)
    * Arj archives (.arj)
    * Jar archives (.jar, .ear, .war)
    * Lha archives (.lzh)
    * Rar archives (.rar)
    * Zip archives (.zip)
    * 7-Zip archives (.7z)
    * Single files compressed with gzip, bzip, bzip2, compress, lzop

%description -l ru_RU.UTF-8
File Roller - архиватор для рабочего стола GNOME. С его помощью можно:
создавать архивы и изменять их содержимое, читать оглавление архивов,
просматривать и распаковывать заключенные в архив файлы.
File Roller является графической оболочкой к различным средствам сжатия
данных. В число поддерживаемых программой типов архивов входят:
    * Архивы Tar как несжатые (.tar), так и сжатые посредством
          * gzip (.tar.gz, .tgz)
          * bzip (.tar.bz, .tbz)
          * bzip2 (.tar.bz2, .tbz2)
          * compress (.tar.Z, .taz)
          * lzop (.tar.lzo, .tzo)
    * Ar архивы (.ar)
    * Arj архивы (.arj)
    * Jar архивы (.jar, .ear, .war)
    * Lha архивы (.lzh)
    * Rar архивы (.rar)
    * Zip архивы (.zip)
    * 7-Zip архивы (.7z)
    * Отдельные файлы сжатые при помощи gzip, bzip, bzip2, compress, lzop.

%prep
%setup
%patch1
%patch2 -p1 -b .tzo

rm -f data/%xdg_name.desktop{,.in}

%build
%meson \
    %{?_disable_magic:-Dmagic=false} \
    %{?_enable_packagekit:-Dpackagekit=true} \
    %{?_enable_libarchive:-Dlibarchive=true} \
    %{?_disable_nautilus_actions:-Dnautilus-actions=false} \
    -Dnotification=true \
    -Dcpio='/bin/cpio'
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%dir %_libexecdir/%name
%_libexecdir/%name/*.sh
%_libexecdir/%name/rpm2cpio
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/services/%xdg_name.ArchiveManager1.service
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name1}*.*
%config %_datadir/glib-2.0/schemas/*
%_datadir/metainfo/%xdg_name.appdata.xml

%if_enabled nautilus_actions
%_libdir/nautilus/extensions-%nau_api_ver/*.so
%endif

%doc AUTHORS NEWS README


%changelog
* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Jul 17 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.91-alt1
- 3.25.91

* Thu Apr 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Sep 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.91-alt1
- 3.21.91

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Sep 01 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.4-alt1
- 3.16.4

* Tue Jun 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Mar 03 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.91-alt1
- 3.15.91

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2.1-alt1
- 3.10.2.1

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Aug 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Tue Jul 02 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Mar 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt3
- subst'ituted recursively sx-lzop-compressed-tar/x-tzo
  according to shared-mime-info database (ALT #28668)

* Mon Mar 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt2
- disabled libmagic support
- enabled libarchive support

* Wed Nov 28 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1.1-alt1
- 3.6.1.1

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.92-alt1
- 3.5.92

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Thu Mar 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt2
- fixed command line for zip (ALT #27011)

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Tue Apr 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Sun Jan 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt2
- don't allow to use 7z for read/write zip archives (closes #21150)

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Tue Dec 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Tue Dec 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Sat Mar 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sun Sep 28 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)

* Sat May 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)
- add Packager

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for file-roller

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Sun Mar 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Wed Oct 17 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt1
- new version (2.20.1)
- added intltoolize invocation to fix building with new intltool.

* Mon Jul 23 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.4-alt2
- fixed packaging on x86_64.

* Thu Jul 19 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.4-alt1
- new version (2.18.4)
- use macros from rpm-build-gnome; replaced %%__autoreconf macro with a plain
  autoreconf call
- updated files list

* Tue Feb 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version (2.16.3)
- dropped zoo support, as zoo is no more in Sisyphus

* Sat Oct 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- updated dependencies

* Sun Jun 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.3-alt1
- new version (2.14.3)

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version (2.14.1)
- spec cleanup

* Tue Feb 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.92-alt1
- new version (2.13.92)
- updated dependencies, cleaned up the spec.
- removed Debian menu support

* Fri Sep 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Sat Apr 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.3-alt1
- 2.10.3

* Wed Apr 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Thu Mar 31 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Dec 08 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.9.0-alt3
- requires GConf2, scrollkeeper, desktop-file-utils
- run %%{update,clean}_desktopdb in %%post{un,}
  desktop-file-utils >= 0.8 required for build.

* Sun Dec 05 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.9.0-alt2
- removed broken *desktopdb macros

* Wed Nov 24 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.9.0-alt1
- 2.9.0
- requires all backends

* Sat Nov 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.3-alt1
- Updated to 2.8.3
- Spec cleanup

* Thu Jun 24 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.6.2-alt1
- new version

* Sat May 15 2004 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.6.1-alt2
- new version

* Fri Oct 17 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.4.0.1-alt1
- new version

* Sat Nov 02 2002 Vyacheslav Dikonov <slava@altlinux.ru> 2.0.3-alt2
- translation update, missing docs fixed

* Mon Oct 14 2002 AEN <aen@altlinux.ru> 2.0.3-alt1
- new version

* Wed Oct 09 2002 AEN <aen@altlinux.ru> 2.0.2-alt1
- first build for Sisyphus
