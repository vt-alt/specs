# -*- rpm-spec -*-
# $Id: avrdude,v 1.2 2005/02/02 09:35:55 grigory Exp $

%def_enable doc
%def_enable parport

%define udev_rules_file 70-avrdude_usbprog.rules
%set_verify_elf_method unresolved=relaxed

Summary: AVRDUDE is software for programming Atmel AVR Microcontrollers.
Name: avrdude
Version: 6.3
Release: alt5
License: GPL
Group: Development/Other
URL: http://www.nongnu.org/avrdude/
Source0: http://download.savannah.gnu.org/releases/avrdude/%name-%version.tar.gz
Source3: modprobe.avrdude_parport
##############################
## use to convert avrdude-udev-rules(fedora), debian.avrdude.udev
Source2: udevrules2table.pl
# SuSE 6.3-3.4
Source4: avrdude-usbdevices
# fedora 6.3-17
Source5: avrdude-udev-rules
# debian ???
Source6: debian.avrdude.udev
## merge avrdude-usbdevices(suse), converted avrdude-udev-rules & debian.avrdude.udev
## into avrdude-usbdevices.altmerged
Source7: avrdude-usbdevices.altmerged
##############################
Patch: avrdude-install-header.patch


BuildRequires: gnu-config libtinfo-devel libusb-devel libusb-compat-devel makeinfo
BuildRequires: flex libelf-devel libftdi1-devel libncurses-devel libreadline-devel

%if_enabled doc
BuildRequires: texlive-collection-latexrecommended texi2html texi2dvi
%endif

%package docs
Summary: Documentation for AVRDUDE.
Group: Development/Other
BuildArch: noarch

%package devel
Summary: The AVRDUDE static library with API for other tools.
Group: Development/C
Provides: lib%name-devel = %version-%release
Provides: lib%name-static = %version-%release

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%description docs
Documentation for avrdude in html, postscript and pdf formats.

%description devel
AVRDUDE static library provides API integration for programming Atmel AVR Microcontrollers.

%prep
%setup -q
%patch -p2
# useful cleanups based on fedora spec
chmod -x safemode.c doc/TODO
sed -i 's|/usr/local/etc/avrdude.conf|/etc/avrdude.conf|g' doc/avrdude.texi avrdude.1
iconv -f ISO88591 -t UTF8 -o ChangeLog-2003 < ChangeLog-2003
iconv -f ISO88591 -t UTF8 -o NEWS < NEWS

%build
%autoreconf
%configure %{subst_enable doc} %{subst_enable parport} --enable-linuxgpio
%make

%install
%makeinstall
sed -i 's/^#include "ac_cfg\.h"$/#include <libavrdude_cfg.h>/' %buildroot%_includedir/libavrdude.h
install -T ac_cfg.h %buildroot%_includedir/libavrdude_cfg.h
rm -f %buildroot%_libdir/*.so*

%global udevdir %{_prefix}/lib/udev
%global tag uaccess
RULESFILE=%buildroot%_udevrulesdir/%udev_rules_file
mkdir -p ${RULESFILE%/*}
while IFS=" " read major minor comment;do
    echo "# $comment"
    echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="'$major'", ATTRS{idProduct}=="'$minor'", TAG+="%{tag}"'
done <%{SOURCE7} >> $RULESFILE
chmod 644 $RULESFILE


%if_enabled parport
install -D -m 644 %{SOURCE3} %buildroot%_sysconfdir/modprobe.d/50-avrdude_parport.conf
%endif

%if_enabled doc
%post

%preun
%endif

%files
%doc AUTHORS ChangeLog* NEWS README doc/TODO
%config %_sysconfdir/%name.conf
%_bindir/*
%_man1dir/*
%_udevrulesdir/%udev_rules_file
%if_enabled parport
%dir %{_sysconfdir}/modprobe.d
%config %{_sysconfdir}/modprobe.d/50-avrdude_parport.conf
%endif

%if_enabled doc
%_infodir/*

%files docs
%doc doc/avrdude-html/*.html doc/avrdude.ps doc/avrdude.pdf
%endif

%files devel
%_includedir/*.h
%_libdir/*.a

%changelog
* Thu Aug 29 2019 Igor Vlasenko <viy@altlinux.ru> 6.3-alt5
- added doc fixes from fedora
- added 70-avrdude_usbprog.rules - usb id list merged from SuSE, fedora, debian
- added modprobe ppdev hook on paraport install (from SuSE)

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 6.3-alt4.1
- NMU: remove rpm-build-ubt from BR:

* Wed Feb 06 2019 Grigory Ustinov <grenka@altlinux.org> 6.3-alt3.1
- Rebuild with libreadline7.

* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 6.3-alt3
- NMU: fixed BR: for texlive 2017

* Sun Oct 01 2017 Evgeny Sinelnikov <sin@altlinux.ru> 6.3-alt2%ubt
- Rebuild with libusb-compat-devel due needs for stk500v2 (ALT #33937)

* Thu Jul 27 2017 Evgeny Sinelnikov <sin@altlinux.ru> 6.3-alt1%ubt
- Update to last version with nonstandard speeds on port support (ALT #33688)
- Add avrdude-devel with static development library
- Build with universal build tag (aka ubt macros)

* Sat Jan 09 2016 Grigory Milev <week@altlinux.ru> 6.2-alt1
- new version released

* Tue May 19 2015 Grigory Milev <week@altlinux.ru> 6.1-alt1
- New version released
- flip2 patch obsolete

* Tue Dec 24 2013 Grigory Milev <week@altlinux.ru> 6.0.1-alt2
- Added flip2 bootloaders support (DFU Atmel bootloaders)

* Tue Oct 15 2013 Grigory Milev <week@altlinux.ru> 6.0.1-alt1
- new version released

* Mon Dec 05 2011 Grigory Milev <week@altlinux.ru> 5.11.1-alt1
- new vrsion release, see ChangeLog in docs for detales

* Fri Nov 05 2010 Grigory Milev <week@altlinux.ru> 5.10-alt2
- rebuilded with libusb (bug #24347)

* Thu Nov 04 2010 Grigory Milev <week@altlinux.ru> 5.10-alt1
- new version released
- change make_build to make due troubles with building documentation

* Tue Nov 24 2009 Grigory Milev <week@altlinux.ru> 5.8-alt1
- new version released
- fix dependenses
- remove depricated info install/uninstall scripts

* Fri Mar 27 2009 Grigory Milev <week@altlinux.ru> 5.6-alt1
- New version released
- Added support for USB

* Wed Jan 09 2008 Grigory Milev <week@altlinux.ru> 5.5-alt1
- Update for new version

* Sun Jul 01 2007 Evgeny Sinelnikov <sin@altlinux.ru> 5.3.1-alt1
- Update for new version
- Add enable macros for docs

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 4.4.0-alt1.1
- Rebuilt with libreadline.so.5.

* Tue Feb  1 2005 Grigory Milev <week@altlinux.ru> 4.4.0-alt1
- initial build for ALT Linux

* Wed Aug 27 2003 Theodore A. Roth <troth@openavr.org>
  [Thanks to Artur Lipowski <LAL@pro.onet.pl>]
- Do not build debug package.
- Remove files not packaged to quell RH9 rpmbuild complaints.

* Wed Mar 05 2003 Theodore A. Roth <troth@openavr.org>
- Add docs sub-package.
- Add %post and %preun scriptlets for handling info files.

* Wed Feb 26 2003 Theodore A. Roth <troth@openavr.org>
- Initial build.



