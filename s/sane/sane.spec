%def_disable static
%define oname %name-backends

Name: sane
Version: 1.0.28
Release: alt1

Summary: This package contains the SANE docs and utils
Summary(ru_RU.UTF-8): Документация и утилиты для SANE

License: GPL
Group: Graphics
Url: http://www.sane-project.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://gitlab.com/sane-project/backends/uploads/9e718daff347826f4cfe21126c8d5091/sane-backends-%version.tar
#Source1: %name-%version.ru.po
Source2: %name.xinetd

Patch3: sane-1.0.19-hp-psc.patch
Patch4: sane-backends-1.0.18-epson-1270.patch
#Patch5: 0001-Revert-use-rewind-instead-of-slow_back_home.patch

# Fedora patches
#Patch109: sane-backends-1.0.18-glibc-2.7.patch
#Patch110: sane-backends-revert-samsung-patch.patch

# Mandriva patches
Patch201: sane-backends-1.0.18-plustek-s12.patch

# FIXME: check module linking without provides
#add_findprov_lib_path %_libdir/%name

BuildRequires: autoconf-archive

Requires: lib%name = %version-%release
Requires: udev
Provides: %oname-drivers-scanners = %version-%release

BuildRequires: rpm-build-intro

# manually removed: libsane-devel
# Automatically added by buildreq on Sat Oct 12 2019
# optimized out: ghostscript-classic glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config gnustep-base-devel libdb4-devel libgpg-error libgphoto2-6 libgphoto2_port-12 libnet-snmp35 libnl-devel libpng-devel libssl-devel libstdc++-devel net-snmp-config netpbm pkg-config python-base python-modules python3 python3-base python3-dev python3-module-mpl_toolkits python3-module-paste python3-module-zope ruby ruby-stdlibs sh4 sssd-client
BuildRequires: libavahi-devel libgphoto2-devel libieee1284-devel libjpeg-devel libnet-snmp-devel libsystemd-devel libtiff-devel libusb-devel libv4l-devel


%package -n %name-server
Summary: SANE as network server
Group: System/Libraries
License: LGPL
Requires: lib%name = %version-%release

%package -n lib%name
Summary: SANE shared libraries
Group: System/Libraries
License: LGPL
Provides: %oname = %version-%release
Provides: %oname-libs = %version-%release

%package -n lib%name-gphoto2
Summary: SANE libraries for gphoto2
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: %oname-drivers-cameras = %version-%release

%description -n lib%name-gphoto2
This package contains the SANE libraries which are needed by applications that
want to access digital cameras via GPhoto2.

%package -n lib%name-devel
Summary: Development environment for SANE
Group: Development/C
License: LGPL
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel
Provides: %oname-devel = %version-%release

%package -n lib%name-devel-static
Summary: SANE static libraries
Group: Development/C
License: LGPL
Requires: lib%name-devel = %version-%release

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras. SANE currently includes modules for
accessing:

Scanners: Abaton, Agfa, Apple, Artec, Avision, Bell+Howell, Canon,
Epson, Fujitsu, HP, LEO, Microtek, Mustek, NEC, Nikon, Panasonic, PIE,
Plustek, Ricoh, Sceptre, Sharp, Siemens, Tamarack, Teco, UMAX
HP Scanjet 3900 series scanners (hp3970,
hp4070, hp4370 and those which use RTS8822 chipset).

Digital cameras: Kodak, Polaroid, Connectix QuickCam
and other SANE devices via network (see sane-server package
and read the saned(1) manpage).

%description -l ru_RU.UTF-8
SANE (Scanner Access Now Easy) -- это достаточно разумный
и в то же время простой интерфейс для локальных и сетевых
сканеров и других устройств оцифровки изображений, таких как
цифровые фотоаппараты и видеокамеры. В настоящее время SANE
включает модули для использования широкого круга сканеров,
включая модели

Сканеров: Abaton, Agfa, Apple, Artec, Avision, Bell+Howell, Canon,
Epson, Fujitsu, HP, LEO, Microtek, Mustek, NEC, Nikon, Panasonic, PIE,
Plustek, Ricoh, Sceptre, Sharp, Siemens, Tamarack, Teco, UMAX

Цифровых фотоаппаратов: Kodak, Polaroid, Connectix QuickCam
и других SANE-устройств по сети (установите пакет sane-server и
прочитайте страницу руководства man saned(1)).

%description -n %name-server
This package contains SANE network server components.

%description -n lib%name
This package contains SANE shared libraries
and scanner backend modules.
Install this package for scan programs.

%description -n lib%name -l ru_RU.UTF-8
Этот пакет содержит разделяемые библиотеки SANE
и модули поддержки различных сканеров.
Именно этот пакет требуется программам сканирования.

%description -n lib%name-devel
This package contains development environment for SANE.

%description -n lib%name-devel -l ru_RU.UTF-8
Этот пакет содержит файлы для разработки программ с использованием SANE.

%description -n lib%name-devel-static
This package contains SANE static libraries.

%description -n lib%name-devel-static -l ru_RU.UTF-8
Этот пакет содержит статические библиотеки SANE.

%prep
%setup -n %oname-%version
%patch3
%patch4
#patch5 -p1

# Fedora patches
#patch109 -p1 -b .glibc-2.7
#patch110 -p1 -b .samsung

# Mandriva patches
%patch201 -p1 -b .plusteks12

# Disable v4l backend by default
%__subst 's/^\(v4l\)/#\1/g' backend/dll.conf.in

# Remove the backend/dll.conf file generated by the patches, it prevents
# the Makefile from generating  the real dll.conf file
rm -f backend/dll.conf

#-%version
#cp -f %%SOURCE1 po/%oname.ru.po

%build
%__subst "s|m4_esyscmd_s(\[git describe --dirty\])|%version|" configure.ac
%autoreconf
%configure --enable-translations --with-gphoto2 \
	--with-usb \
	--with-systemd \
	--with-gphoto2 \
	--with-v4l \
	--with-snmp \
	--enable-avahi \
	--enable-locking \
	--disable-rpath \
	--with-lockdir=%_lockdir/%name \
	--enable-static
%make_build
#%make -C doc sane.ps.gz

%install
%makeinstall_std

# fix default path to firmware
%__subst "s|/path/to/your/firmware|%_libdir/hotplug/firmware|" %buildroot%_sysconfdir/sane.d/*.conf

# install udev rules
install -D -m0644 tools/udev/libsane.rules %buildroot%_udevrulesdir/25-libsane.rules
# follow fix drops GROUP! (alt bug #29425)
#remove ownership setup (was conflict with other services) see altbug #21808
#sed 's/,[[:space:]]\+GROUP=\"[^"]\+\"[[:space:]]*//' -i %buildroot%_udevrulesdir/25-libsane.rules

install -D %SOURCE2 -m0644 %buildroot%_sysconfdir/xinetd.d/%name
mkdir -p %buildroot%_lockdir/%name/

rm -f %buildroot%_libdir/%name/*.la

%find_lang %oname

%if_disabled static
rm -f %buildroot%_libdir/*.a
rm -f %buildroot%_libdir/%name/*.a
%endif

%pre -n lib%name
%groupadd -f scanner || :

%pre -n %name-server
%useradd -d /var/empty -s /dev/null -G scanner _saned || :

%files
%_docdir/%name-*
%_bindir/sane-find-scanner
%_bindir/scanimage
%_bindir/gamma4scanimage
%_bindir/umax_pp
%_man1dir/*
%exclude %_man8dir/saned*
%exclude %_man1dir/sane-config*
%_man7dir/*

%files -n %name-server
%config(noreplace) %_sysconfdir/xinetd.d/%name
%config(noreplace) %_sysconfdir/sane.d/saned.conf
%_sbindir/saned
%_man8dir/saned*

%files -n lib%name -f %oname.lang
%_libdir/*.so.1
# to check we updated correctly
%_libdir/*.so.%version
%_udevrulesdir/*
%_man5dir/*
%dir %_sysconfdir/sane.d/
%config(noreplace) %_sysconfdir/sane.d/*
%exclude %_sysconfdir/sane.d/saned.conf
%dir %_libdir/%name/
%_libdir/%name/*.so.*
%_libdir/%name/*.so
%exclude %_libdir/sane/*gphoto2.so.*
%exclude %_libdir/sane/*gphoto2.so
# used in sane-frontends, xsane
%dir %_datadir/%name/
%attr(0775,root,scanner) %dir %_lockdir/%name/

%files -n lib%name-gphoto2
%_libdir/sane/*gphoto2.so.*
%_libdir/sane/*gphoto2.so

%files -n lib%name-devel
%_bindir/sane-config
%_man1dir/sane-config*
%_libdir/*.so
%_includedir/sane/
%_pkgconfigdir/%oname.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%_libdir/sane/*.a
%endif

%changelog
* Sat Oct 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.28-alt1
- new version 1.0.28 (with rpmrb script)
- update buildreq (enable build with systemd, avahi)

* Fri May 11 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.27-alt4
- revert Color scanning for Samsung models, which support JPEG Lossy compression (ALT bug 34855)

* Sun Dec 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.27-alt3
- cleanup spec

* Mon Oct 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.27-alt2
- revert bd0b0cd218504868f32962a5558449956c8ce242 (ALT bug 33993)

* Thu May 25 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.27-alt1
- new version 1.0.27 (with rpmrb script)
- disable v4k backend by default

* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.25-alt3
- real build 1.0.25 (ALT bug #32851)

* Tue Apr 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.25-alt2
- move .so plugins from -devel (ALT bug #31920)

* Sat Dec 12 2015 Vitaly Lipatov <lav@altlinux.ru> 1.0.25-alt1
- new version 1.0.25 (with rpmrb script) (ALT bug #31327)
- add libnet-snmp-devel build requires

* Thu Feb 05 2015 Michael Shigorin <mike@altlinux.org> 1.0.24-alt2.3
- rebuilt against recent libgphoto2

* Sun Jan 05 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.24-alt2.2
- Add all provides for sane-backends-* for Red Hat compatibility

* Sat Jan 04 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.24-alt2.1
- Add sane-backends-devel provides for Red Hat compatibility

* Fri Oct 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.24-alt2
- return GROUP=scanner (ALT bug #29425)
- remove obsoleted patches
- add user _saned and run saned under _saned:scanner

* Wed Oct 02 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.24-alt1
- new version 1.0.24 (with rpmrb script) (ALT bug #29418)

* Thu Sep 13 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.23-alt2
- add missed pkgconfig (ALT bug #27727)

* Wed Sep 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.0.23-alt1
- new version 1.0.23 (ALT bug #27677)

* Fri Mar 02 2012 Michael Shigorin <mike@altlinux.org> 1.0.22-alt3
- added Canon MF4410 support patch (ALT bug #27023)

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.22-alt2.1
- Rebuilt with libusb 1.0.9

* Tue Dec 20 2011 Vitaly Lipatov <lav@altlinux.ru> 1.0.22-alt2
- build without RPATH for libsane

* Thu Apr 21 2011 Vitaly Lipatov <lav@altlinux.ru> 1.0.22-alt1
- new version 1.0.22 (with rpmrb script) (ALT bug #25483)

* Thu Jan 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.0.21-alt2
- xinetd: add only_from as example (ALT #24773)

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.21-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat May 29 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0.21-alt1
- new version 1.0.21 (with rpmrb script) (ALT bug #23419)
- drop obsoleted scsi rules (see bug #23381)

* Fri Oct 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.20-alt2
- fix device group (bug #21808)

* Thu Jun 18 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.20-alt1
- new version 1.0.20 (with rpmrb script)
- drop iscan to separate package

* Wed Mar 11 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.19-alt3
- build with new iscan 2.17.0

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.19-alt2
- fix build iscan with gcc 4.3

* Sat Apr 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.19-alt1
- new version (1.0.19), drop patches for hpljm1005, hp3900
- disable epkowa (from IScan) by default
- sync patches with FC9

* Fri Mar 14 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt8
- rebuild with new libgphoto2 (fix bug #14881)
- enable static due internal build liblib.a
- fix libsane-gphoto2 package name

* Wed Jan 30 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt7
- split gphoto2 backend to standalone package
- disable static subpackage
- do not pack hotplug files
- do not use libusbscanner script for set permissions

* Mon Jan 28 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt6
- apply Fedora, Mandriva patches (udev fixes here)
- enable support for Epson CX-5000, Epson Perfection 1270
- enable support Plustek s12
- added the "epkowa" backend from Epson Avasys (Source 13).
- commented out "epson" backend in dll.conf (replaced by "epkowa")
- added "hp_rts88xx" backend to support the HP ScanJet 44x0C scanners
- added "Provides: iscan"
- update buildreqs, add pkgconfig file
- rearranged udev rules (review me!)
- fix group for lockdir/sane

* Fri Oct 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt5
- fix smp build
- add scanner HP PSC 1510 (fix #13221)

* Mon Sep 17 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt4
- link hpljm1005 module with sanei (reclose #12764)

* Thu Sep 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt3
- add requires to libsane in sane-server
- build to Sisyphus (close #12764)
- enable semi-SMP-compatible build

* Thu Sep 13 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 1.0.18-alt2
- add support for HP LaserJet M1005 MFP (#12764).

* Tue Jan 23 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt1
- add patch with hp3900 backend (close bug #10697)

* Mon Sep 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.18-alt0.1
- new version 1.0.18
- drop lock patch applied in mainstream

* Fri Sep 15 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt4
- fix bug #9889 (add udev rules for scsi scanners)
- add requires for udev

* Tue Jul 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt3
- revert accidently removed autoreconf

* Sat Jul 15 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt2
- fix bug (#9638) - add udev rules file (thanks to Artem Zolochevskiy <azol@>)

* Sat Feb 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt1
- fix bug with lockdir (#9107) - rewrote lockdir setting
- remove tetex buildreqs

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.17-alt0.1
- new version

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.16-alt2
- fix bug #7909 (lock dir placement)
- do install via DESTDIR now

* Sun Sep 04 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.16-alt1
- new version
- add provides sane-backends (for iscan package from Epson)

* Mon Mar 21 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.15-alt4.20050320
- cvs snapshot

* Wed Feb 09 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0.15-alt4.20050208
- cvs snapshot from 2005-02-08
- remove dev requires and >/dev/null (bug #5563)
- update summary and description

* Sun Nov 28 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.15-alt2
- add dev requires (bug #5563)

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.15-alt1
- new version
- remove niash patch (in mainstream now)

* Sun Sep 05 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt4
- fix permission on config files
- fix russian translation
- add group scanner during package installation (fix bug #4337)

* Sun Jul 04 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt3
- use a macro for ldconfig
- change URL
- add niash plugin
- update russian translation

* Fri Jun 11 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt2
- split into subpackages improved (#4338)
- move saned to sane-server package
- add hotplug support (#4337)

* Sat May 15 2004 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt1
- new version
- remove COPYING from doc

* Sat Dec 13 2003 Vitaly Lipatov <lav@altlinux.ru> 1.0.13-alt1
- new version
- build without .la files

* Fri Sep 26 2003 Vitaly Lipatov <lav@altlinux.ru> 1.0.12-alt1.1
- remove %make_build

* Wed Sep 24 2003 Vitaly Lipatov <lav@altlinux.ru> 1.0.12-alt1
- new version

* Mon Mar 24 2003 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt1
- release of 1.0.11
- update of russian translation
- security patch applied to the release

* Wed Feb 12 2003 AEN <aen@altlinux.ru> 1.0.9-alt2
- security patch

* Mon Oct 28 2002 Vitaly Lipatov <lav@altlinux.ru> 1.0.9-alt1
- release of 1.0.9
- add russian translation in spec
- enable translation (gettext) for sane modules
- remove kernel24-source from BuildRequires (will use
  /usr/include/scsi/sg.h from glibc-devel)

* Tue Sep 17 2002 AEN <aen@altlinux.ru> 1.0.9-alt0.2
- new sources from cvs

* Mon Sep 09 2002 AEN <aen@altlinux.ru> 1.0.9-alt0.1
- built CVS version for J2.1/HomePC

* Mon Jun 03 2002 AEN <aen@logic.ru> 1.0.8-alt1
- new version
- new avision patch

* Mon Mar 25 2002 AEN <aen@logic.ru> 1.0.7-alt2
- avision patch (with HP5300C experimental support)

* Wed Feb 13 2002 AEN <aen@logic.ru> 1.0.7-alt1
- new version
- removed all patches -- merged upstream

* Mon Jan 21 2002 AEN <aen@logic.ru> 1.0.6-alt2
- umax 1220u added

* Fri Jan 18 2002 AEN <aen@logic.ru> 1.0.6-alt1
- new version
- hp backaend included in upstream

* Thu Dec 06 2001 AEN <aen@logic.ru> 1.0.5-alt3
- rebuilt with new libusb

* Wed Nov 14 2001 AEN <aen@logic.ru> 1.0.5-alt2
- new hp backend, thnx to Alexander Goncharenko

* Fri Aug 10 2001 AEN <aen@logic.ru> 1.0.5-alt1
- new version

* Mon Jun 18 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.4-ipl2mdk
- Libification.
- Specfile cleanup (policy enforcement).

* Mon Jan 08 2001 AEN <aen@logic.ru>
- new version - 1.0.4

* Tue Dec 26 2000 AEN <aen@logic.ru>
- build with gimp-1.2

* Fri Dec 15 2000 AEN <aen@logic.ru>
- patch for new gimp

* Sat Dec 09 2000 AEN <aen@logic.ru>
- rebuild for RE
- glibc22 patch

* Thu Aug 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.3-2mdk
- rebuild for new libgimp
- fix %%config(noreplace)

* Sun Aug 13 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0.3-1mdk
- s|1.0.2|1.0.3|.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.2-5mdk
- automatically added BuildRequires

* Thu Jul 27 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.2-4mdk

- BMacros
- Some spec file changes

* Wed Apr 05 2000 Francis Galiegue <fg@mandrakesoft.com> 1.0.2-3mdk

- Fixed group for sane-devel

* Fri Mar 17 2000 Francis Galiegue <francis@mandrakesoft.com> 1.0.2-2mdk

- Changed group to match 7.1 specs
- Some spec file changes
- Let spec-helper do its job

* Tue Mar 07 2000 Daouda LO	<daouda@mandrakesoft.com>
-1.0.2

* Mon Nov 15 1999 Florin Grad <florin@mandrakesoft.com>

* Tue Sep 21 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Recompile with gimp-1.0.4.

* Thu Aug 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Rebuild with gimp-1.1.8.

* Thu Aug 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fix broken %post %postun broken scripts.

* Tue May 25 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- recompile in a GIMP-friendly environment
- fix some rather stupid spec bugs

* Tue May 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.01.
- Mandrake adaptations.

* Mon Nov 23 1998 Jonathan Miller <jlm@mvhi.com>
 [1.00-1]
- upgraded to 1.00 (and made description less space-consuming)
- included the post 1.00 fixed "configure" script available 22 Nov 1998.

* Sat Aug 08 1998 Arne Coucheron <arneco@online.no>
  [0.74-3]
- added %_sysconfdir/sane.d to %%dir in file list

* Sat Aug 01 1998 Arne Coucheron <arneco@online.no>
  [0.74-2]
- devel Group: reverted back to Development/Other
- some changes to the %%defattr and %%attr usage in file list

* Tue Jul 28 1998 Binaire <binaire@binaire.ml.org>
  [0.74-1]

* Fri May 22 1998 Arne Coucheron <arneco@online.no>
  [0.73-3]
- added use of %%name and %%version macros
- added a %postun for running ldconfig after uninstall
- using BuildRoot properly now
- using %%defattr and %%attr macros in filelist, allows non-root build
  this means that RPM 2.5 is required to build this spec file now!
- devel Group: changed to X11/Libraries
- added using RPM_OPT_FLAGS during make
- added striping of programs and libraries
- added Requires: gtk+ >= 0.99.13 to main package
- added Requires: %%name = %%version to devel package
- added a %clean section for removing the buildroot dir
- simplified the filelist and added %%config for sane-style.rc
- moved lib*.so to %files devel and dropped the *.la files
- added -q parameter to %%setup
- removed some older changelog entries
- removed the "fix ldconfig brokenness..." stuff
- removed the Packager: line; use %_sysconfdir/rpmrc if you want your name in
- if GIMP is installed, make symlink from xscanimage to plug-ins dir
- install the find-scanner program from the tools dir

* Mon May 18 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Version 0.73 was created: May 13 1998
- gimp (original was build against 0.99.29)
- gtk+ (original was build against 1.0.1)
- dlh (original was build against 0.7d)
- X11 development tree including xpm libraries.

* Wed Apr 22 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Binaries are now BuildRoot proof.

* Wed Apr 22 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Binaries are not BuildRoot proof. release 3 is done without BuildRoot!

* Tue Apr 21 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Temp. fix for some documentations problems with BuildRoot.

* Sat Apr 11 1998 Hugo van der Kooij <hvdkooij@caiw.nl>
- Formal 0.72 now made as RPM! (Build against GTK+ 0.99.10 and GIMP 0.99.24)
- Original package was released: Tue Apr 7 1998
