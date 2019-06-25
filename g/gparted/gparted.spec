%define Name GParted

%def_with pic
%def_disable usermode
%def_enable xhost_root

Name: gparted
Version: 1.0.0
Release: alt1

Summary: %Name Partition Editor
Summary(ru_RU.UTF-8): Редактор разделов %Name
Summary(uk_UA.UTF-8): Редактор розділів %Name
Group: System/Configuration/Hardware
License: %gpl2plus
Url: http://%name.sourceforge.net/

#Source: %name-%version.tar
Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
Source1: %name-pam
Source2: %name-security

AutoReq: yes, noshell

%define polkit_ver 0.112

Requires: yelp
Requires: polkit >= %polkit_ver
%{?_enable_usermode:Requires: consolehelper}
Requires: hdparm
Requires: dosfstools ntfs-3g btrfs-progs >= 4.1
Requires: cryptsetup
# for raid support
Requires: mdadm dmraid dmsetup lvm2
# for UDF filesystems support
Requires: udftools >= 2.0

BuildRequires(pre): rpm-build-licenses
BuildRequires: libparted-devel >= 3.2
BuildRequires: libglibmm-devel >= 2.32 libgtkmm3-devel >= 3.4.0
BuildRequires: gcc-c++ libprogsreiserfs-devel libuuid-devel
BuildRequires: intltool yelp-tools
BuildRequires: polkit >= %polkit_ver

%description
%Name stands for %Name Partition Editor. It uses libparted to detect
and manipulate devices and partitiontables while several (optional)
filesystemtools provide support for filesystems not included in
libparted. These optional packages will be detected at runtime and
don't require a rebuild of %Name.
%Name is written in C++ and uses gtkmm as Graphical Toolkit. The
general approach is to keep the GUI as simple as possible.

%description -l ru_RU.UTF-8
%Name - %Name Partition Editor. Он использует libparted для
обнаружения и манипуляций с устройствами и таблицами разделов, а также
некоторые (необязательные) инструменты (не включенные в libparted),
обеспечивающие поддержку файловых систем. Эти необязательные пакеты
обнаруживаются во время выполнения и не требуют пересборки %Name.
%Name написан на C++ с использованием gtkmm в качестве графического
инструментария. Главная задача - оставить GUI максимально простым.

%description -l uk_UA.UTF-8
%Name - %Name Partition Editor. Він використовує libparted для
виявлення та маніпуляцій з пристроями і таблицями разділів, а також
деякі (необов'язкові) інструменти (не включені в libparted), які
забезпечують підтримку файлових систем. Ці необов'язкові пакети
виявляються під час виконання і не потребують перебудови %Name.
%Name написано на C++ з використанням gtkmm в якості графічного
інструментарію. Головне завдання - залишити GUI максимально простим.


%prep
%setup

# get polkit version from pkaction in hasher
subst 's/pkexec --version/pkaction --version/' configure*

%build
#NOCONFIGURE=1 ./autogen.sh
%add_optflags -D_FILE_OFFSET_BITS=64
%configure %{subst_with pic} \
	%{?_enable_usermode:--bindir=%_sbindir} \
	%{?_enable_xhost_root:--enable-xhost-root} \
	--enable-libparted-dmraid \
	--enable-online-resize
%make_build
bzip2 --best --keep --force ChangeLog

%install
%makeinstall_std

%if_enabled usermode
install -pD -m640 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/%name
install -d -m 0755 %buildroot%_bindir
ln -s %_bindir/consolehelper %buildroot%_bindir/%name
sed -i 's|%_sbindir|%_bindir|' %buildroot%_desktopdir/%name.desktop
%endif

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS ChangeLog.* README NEWS
%_bindir/%name
%_sbindir/%{name}bin
%_man8dir/%name.8.*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/%name.desktop
%_datadir/polkit-1/actions/org.gnome.gparted.policy
%_datadir/appdata/%name.appdata.xml

%if_enabled usermode
%_bindir/%name
%_sysconfdir/pam.d/%name
%_sysconfdir/security/console.apps/%name
%endif

%changelog
* Thu May 30 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0 (ported to Gtkmm3)
- removed obsolete dmraid.patch

* Wed Apr 17 2019 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt2
- rebuilt with --enable-xhost-root (ALT #35409)

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt1
- 0.33.0

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.31.0-alt1
- 0.31.0
- updated requires

* Thu Oct 12 2017 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0
- removed consolehelper support in favor of polkit

* Wed Aug 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1
- 0.29.0
- ekorneechev@:
  %%name-0.29.0-alt-dmraid.patch (ALT #32338)

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Thu Oct 27 2016 Yuri N. Sedunov <aris@altlinux.org> 0.27.0-alt1
- 0.27.0

* Tue Jun 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Tue Apr 26 2016 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Wed Jan 20 2016 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Sun Nov 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt2
- improved consolehelper support (ALT #31487)

* Wed Oct 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1.1
- rebuilt with newer *mm libraries

* Tue Aug 04 2015 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.22.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Mar 27 2015 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Mon Jan 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Tue Oct 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.1
- Fixed build

* Thu Feb 17 2011 Mykola Grechukh <gns@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Sat Dec 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Sep 25 2010 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- rebuilt for Sisyphus (fixes: #23807)

* Sun Jul 25 2010 Led <led@altlinux.ru> 0.5.2-tmc2
- fixed ext4 support

* Sun Jul 04 2010 Led <led@altlinux.ru> 0.5.2-tmc1
- 0.5.2

* Sun Mar 21 2010 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- rebuilt for Sisyphus on aris@' request;
  thanks led@ for gear repo

* Wed Mar 03 2010 Led <led@altlinux.ru> 0.5.1-tmc1
- 0.5.1

* Sun Jan 24 2010 Led <led@altlinux.ru> 0.5.0-tmc1
- 0.5.0

* Mon Dec 07 2009 Led <led@altlinux.ru> 0.4.8-alt2
- added nilfs2 support

* Sat Dec 05 2009 Led <led@altlinux.ru> 0.4.8-alt1
- 0.4.8

* Tue Oct 27 2009 Alexey Rusakov <ktirf@altlinux.org> 0.4.6-alt1.1
- thanks to led@ for keeping the package fresh in his git

* Tue Oct 20 2009 Led <led@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Mon Aug 10 2009 Led <led@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Mon May 11 2009 Led <led@altlinux.ru> 0.4.5-alt2
- added common class for FAT 16/32 and EXT 2/3/4
- updated BuildRequires

* Sat May 09 2009 Led <led@altlinux.ru> 0.4.5-alt1
- 0.4.5:
  + Improved crypt-luks detection
  + Improved dmraid device detection
  + Improved UUID detection
  + Enhanced to search for udevadm if udevsettle not found
  + Improved file system detection

* Fri Apr 03 2009 Led <led@altlinux.ru> 0.4.4-alt1
- 0.4.4:
  + enhanced move/resize functionality
  + added detection of LUKS encrypted partitions
  + added detection of btrfs file system
  + added initial support for dmraid devices

* Wed Mar 04 2009 Led <led@altlinux.ru> 0.4.3-alt2
- fixed mistranslation in ru.po (#19047) (thanx lav@)

* Sun Feb 15 2009 Led <led@altlinux.ru> 0.4.3-alt1
- 0.4.3:
  + fixed #18367

* Fri Dec 26 2008 Led <led@altlinux.ru> 0.4.1-alt2
- cleaned up spec
- fixed Exec in %name.desktop
- fixed ru and uk translations
- fixed descriptions and summaries

* Tue Dec 02 2008 Led <led@altlinux.ru> 0.4.1-alt1
- 0.4.1
- cleaned up spec

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.3.9-alt1
- 0.3.9
- fixed %name.desktop

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.3.8-alt2
- fixed %name.desktop

* Sun Jul 20 2008 Led <led@altlinux.ru> 0.3.8-alt1
- 0.3.8

* Mon Mar 31 2008 Led <led@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Sun Mar 02 2008 Led <led@altlinux.ru> 0.3.5-alt2
- added icons

* Sun Feb 10 2008 Led <led@altlinux.ru> 0.3.5-alt1
- 0.3.5
- updated BuildRequires

* Sun Sep 16 2007 Led <led@altlinux.ru> 0.3.3-alt7
- added %name-0.3.3-disable_hal_dirty_hack.patch for disable dirty hack
  for HAL (fixed #12753)

* Wed Aug 15 2007 Led <led@altlinux.ru> 0.3.3-alt6
- rebuild with libparted-1.8.so.8
- fixed License

* Mon May 14 2007 Led <led@altlinux.ru> 0.3.3-alt5
- rebuild with libparted-1.8.so.7

* Sun Mar 25 2007 Led <led@altlinux.ru> 0.3.3-alt4
- rebuild with libparted-1.8.so.6

* Mon Mar 19 2007 Led <led@altlinux.ru> 0.3.3-alt3
- rebuild with libparted-1.8.so.4

* Tue Jan 16 2007 Led <led@altlinux.ru> 0.3.3-alt2
- rebuild with libparted-1.8.so.2

* Fri Dec 08 2006 Led <led@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Dec 04 2006 Led <led@altlinux.ru> 0.3.2-alt1
- 0.3.2:
  + added support for reading volumelabels (ext2/3 now)
- removed %name-0.3.1-configure.patch (fixed in upstream)
- fixed BuildRequires
- cleaned up %%setup due fixes in upstream
- fixed %name.desktop

* Thu Nov 23 2006 Led <led@altlinux.ru> 0.3.1-alt2
- rebuild with new libparted
- added %name-0.3.1-configure.patch
- fixed spec

* Tue Sep 12 2006 Led <led@altlinux.ru> 0.3.1-alt1
- 0.3.1
- fixed configure*

* Thu Sep 07 2006 Led <led@altlinux.ru> 0.3-alt1
- 0.3
- fixed BuildRequires

* Mon Jun 19 2006 Led <led@altlinux.ru> 0.2.5-alt4
- rebuild without changes for fixing unmets

* Tue May 30 2006 Led <led@altlinux.ru> 0.2.5-alt3
- rebuild with libparted-1.7.1

* Mon May 22 2006 Led <led@altlinux.ru> 0.2.5-alt2
- rebuild with libparted-1.7.0

* Mon May 22 2006 Led <led@altlinux.ru> 0.2.5-alt1
- fixed spec

* Mon May 15 2006 Led <led@altlinux.ru> 0.2.5-alt0.1
- 0.2.5
- removed unneedful BuildReq's

* Wed Apr 05 2006 Led <led@altlinux.ru> 0.2.4-alt0.1
- 0.2.4

* Wed Mar 29 2006 Led <led@altlinux.ru> 0.2.3-alt0.1
- 0.2.3

* Fri Feb 24 2006 Led <led@altlinux.ru> 0.2.2-alt0.1
- 0.2.2

* Fri Feb 17 2006 Led <led@altlinux.ru> 0.2.1-alt0.1
- 0.2.1
- removed unneedful BuildReq's

* Mon Jan 30 2006 Led <led@altlinux.ru> 0.2-alt1
- 0.2

* Mon Jan 23 2006 Led <led@altlinux.ru> 0.1-alt1
- 0.1
- removed empty NEWS from docs
- uk and ru Summary and description
- added usermode

* Sun Nov 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.0.9-alt1
- new version
- the binary now lives in bindir instead of sbindir (it's an upstream change actually).

* Mon Sep 12 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.0.8-alt0.1.1
- rebuild with libparted.

* Sat Jan 29 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.0.8-alt0.1
- 0.0.8

* Wed Dec 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.7-alt0.1
- First build for Sisyphus.
