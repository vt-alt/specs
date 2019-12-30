%define _unpackaged_files_terminate_build 1
%def_enable cupstifffilter
%def_enable sane_backend
%def_enable autostart
%def_enable PPDs
%def_enable python_code
%def_with python3
%def_disable foomatic_rip
%def_disable qt3
%def_disable qt4
%def_enable qt5
%def_enable policykit
# udev >= 145
# note: flag dropped upstream
%def_enable udevacl
%def_disable halacl
%def_without ernie
%def_without l10n
%if_with backport
%define cups_filters foomatic-filters
%else
%define cups_filters cups-filters >= 1.0.46-alt1
%endif
%if_with python3
%define pysuffix 3
%else
%define pysuffix %nil
%endif

Name:    hplip
Version: 3.19.12
Release: alt1
Epoch:   1

Summary: Solution for printing, scanning, and faxing with Hewlett-Packard inkjet and laser printers.

%if_without ernie
License: GPL-2.0+ and MIT and BSD-3-Clause
%else
License: GPL-2.0+ and MIT and BSD-3-Clause and IJG and ALT-Public-Domain and GPL-2.0+ with exceptions and ISCL
%endif
Group: Publishing
#URL: http://hplip.sourceforge.net -- old
#URL: http://hplipopensource.com/ -- old
URL: https://developers.hp.com/hp-linux-imaging-and-printing
Packager: Andrey Cherepanov <cas@altlinux.org>

# Remove self-satisfied requires
%if_with python3
%filter_from_requires /^python3(\(base.*\|installer.*\|prnt\|scan\|copier\))/d
%endif

%define hpijsname hpijs

Conflicts: ghostscript <= 7.05-alt15
Obsoletes: hpoj <= 0.91
Provides: cups-backend-ptal
Obsoletes: cups-backend-ptal
Conflicts: cups < 1.1.18-alt7

PreReq:	cups
Requires: %name-common = %{?epoch:%epoch:}%version-%release

# TODO: split hplip and hplip-utils
# and remove this Req:
Requires: %name-hpcups = %{?epoch:%epoch:}%version-%release

# Main package requires wget to avoid
# misleading errors about network connectivity (fc bug #705843).
Requires: wget

# for hplip/base/validation.py (fc bug #1118724).
#Requires: gnupg
# set require directly to /usr/bin/gpg, because gnupg2 and gnupg ships it,
# but gnupg will be deprecated in the future
Requires: %{_bindir}/gpg

%if_enabled python_code
###Requires: python
%if_with python3
BuildRequires(pre): rpm-build-python3
%add_python3_lib_path %_datadir/%name
%else
%add_python_lib_path %_datadir/%name
%endif
# Andy Kuleshov report
Requires: python%{pysuffix}-module-dbus
%if_without python3
Requires: python-modules-ctypes
%endif
%endif

Requires: service => 0.5.9-alt1

BuildPreReq: libsane-devel
# Automatically added by buildreq on Thu Sep 22 2005
BuildRequires: gcc-c++ libcups-devel libjpeg-devel libnet-snmp-devel libssl-devel libstdc++-devel libusb-devel libusb-compat-devel libdbus-devel zlib-devel

%if_enabled python_code
%if_enabled qt3
BuildRequires: python%{pysuffix}-module-qt-devel
%endif
%if_enabled qt4
BuildRequires: python%{pysuffix}-module-PyQt4-devel
%endif
%if_enabled qt5
BuildRequires: python%{pysuffix}-module-PyQt5-devel
%endif
#RemovedBuildRequires: python-base python-dev python-modules-compiler python-modules-encodings
BuildRequires: python%{pysuffix}-devel
%endif

%if_enabled PPDs
#cups-common and foomatic-filters is for cupstestppd
BuildPreReq: perl cups-common %{cups_filters}
%endif

%if_enabled policykit
BuildRequires: polkit libpolkit-devel
%endif

Source: http://dl.sourceforge.net/hplip/%name-%version.tar
Source2: %name.init
Source3: %{name}.appdata.xml
Source4: 80-hpmud.perms
Source5: %name.png
Source6: %name-icons.tar
Source7: %name-fixppd.sh
Source8: %name.watch
Source9: upstream-signing-key.asc

#TODO: see what fdi is better:
# https://bugzilla.redhat.com/show_bug.cgi?id=478495
# https://bugzilla.redhat.com/show_bug.cgi?id=479648
# fedora fdi acl policy
Source100: hplip.fdi
# cvs update: hplip.fdi is no longer in the repository (due to udev-acl)
Source101: hpcups-update-ppds.sh
Source102: copy-deviceids-py2.py
Source103: copy-deviceids.py

# OpenSuSE based sources
# deprecated; 2.7.7 shows 'can't connect to device'
Source201: hp-toolbox.wrapper
Source202: hpijs.1

Patch1: hplip-3.12.9-alt-urlhandler.patch
# dead patch 2
Patch2: hplip-3.9.12-alt-fix-udev-rules-ppdev.patch
Patch4: hplip-alt-hplip-desktop.patch
Patch5: hplip-3.17.11-alt-link-libhpipp.patch
Patch6: hplip-3.15.9-alt-systemd.patch
Patch7: hplip-3.16.7-alt-link-python2.patch
Patch8: hplip-3.16.7-alt-link-python3.patch
Patch9: hplip-3.18.6-alt-auth.patch

Patch10: http://www.linuxprinting.org/download/printing/hpijs/hpijs-1.4.1-rss.1.patch
# it is patch 10 rediffed
Patch12: hplip-3.16.11-alt-fax-setup.patch
Patch13: hplip-alt-fix-PPD-file-choose-in-qt5.patch
# Localization files made for old qt3 forms
Patch14: hplip-alt-use-l10n.patch

# fedora patches
Patch101: hplip-pstotiff-is-rubbish.patch
Patch102: hplip-strstr-const.patch
Patch103: hplip-ui-optional.patch
Patch104: hplip-no-asm.patch
Patch105: hplip-deviceIDs-drv.patch
Patch106: hplip-udev-rules.patch
Patch107: hplip-retry-open.patch
Patch108: hplip-snmp-quirks.patch
Patch109: hplip-hpijs-marker-supply.patch
Patch110: hplip-clear-old-state-reasons.patch
Patch111: hplip-hpcups-sigpipe.patch
Patch112: hplip-logdir.patch
Patch113: hplip-bad-low-ink-warning.patch
Patch114: hplip-deviceIDs-ppd.patch
Patch115: hplip-ppd-ImageableArea.patch
Patch116: hplip-scan-tmp.patch
Patch117: hplip-log-stderr.patch
Patch118: hplip-avahi-parsing.patch
Patch120: hplip-dj990c-margin.patch
Patch121: hplip-strncpy.patch
Patch122: hplip-no-write-bytecode.patch
Patch123: hplip-silence-ioerror.patch
Patch124: hplip-3165-sourceoption.patch
%if_without ernie
Patch125: hplip-noernie.patch
%endif
Patch126: hplip-appdata.patch
Patch127: hplip-check-cups.patch
Patch130: hplip-typo.patch
# python3 - recent HP release removed encoding/decoding to utf-8 in fax/pmlfax.py -
# that results in text string going into translate function in base/utils.py, which
# expects binary string because of parameters. Remove this patch if base/utils.py
# code gets fixed.
Patch131: hplip-use-binary-str.patch
# m278-m281 doesn't work correctly again
Patch132: hplip-colorlaserjet-mfp-m278-m281.patch
Patch133: hplip-error-print.patch
Patch134: hplip-hpfax-importerror-print.patch
Patch135: hplip-wifisetup.patch
Patch137: hplip-keyserver.patch
Patch142: hplip-add-ppd-crash.patch
Patch143: hplip-missing-links.patch
Patch144: hplip-hplj-3052.patch
Patch145: hplip-hpmud-string-parse.patch
Patch146: hplip-m278-m281-needs-plugin.patch
Patch147: hplip-hpcups-crash.patch
Patch148: hplip-covscan.patch
Patch149: hplip-logging-segfault.patch
Patch150: hplip-systray-blockerror.patch
Patch152: hplip-missing-drivers.patch
# end fedora patches

# ubuntu patches
Patch201: hp-plugin-download-fix.patch
# end ubuntu patches

# debian patches
Patch302: 01_rss.patch
Patch303: 14_charsign_fixes.patch
Patch304: hp_photosmart_pro_b9100_support.patch
Patch305: pjl-duplex-binding.patch
Patch306: simple-scan-as-default.patch
Patch307: try_libhpmud.so.0.patch
Patch308: add-lidil-two-cartridge-modes.patch
Patch310: hp-systray-make-menu-title-visible-in-sni-qt-indicator.patch
Patch311: hp-systray-make-menu-appear-in-sni-qt-indicator-with-kde.patch
Patch312: hpaio-option-duplex.diff
Patch313: musb-c-do-not-crash-on-usb-failure.patch
Patch314: pcardext-python3-workaround-upstream.patch
Patch315: hpscan-deskjet-3520-aio-allow-non-jpeg-scanning.patch
Patch317: order-page-sizes-consistently.patch
Patch318: install-check-plugin.diff
Patch319: HP-LaserJet_4000-PostScript-PPD.patch
Patch320: ui-patch-upstream-like.patch
Patch321: 0021-Add-include-cups-ppd.h-in-various-places-as-CUPS-2.2.patch
Patch322: 0022-Fix-list-wrapping-in-scan.py-to-fix-generated-manpag.patch
Patch323: 0023-Fix-handling-of-unicode-filenames-in-sixext.py.patch
Patch324: 0024-Make-dat2drv-and-locateppd-build-dependent-of-class-.patch
Patch325: 0025-Remove-all-ImageProcessor-functionality-which-is-clo.patch
Patch326: 0026-Call-QMessageBox-constructors-of-PyQT5-with-the-corr.patch
Patch327: 0027-Fixed-incomplete-removal-of-hp-toolbox-features-whic.patch
Patch328: 0028-hp-check-Fix-core.distro-vs.-core.distro_name-mixups.patch
Patch329: 0029-Make-base.g.xint-more-generous-in-what-it-can-take.patch
# end debian patches

%description
This is the HP driver package to supply Linux support for most
Hewlett-Packard DeskJet, LaserJet, PSC, OfficeJet, and PhotoSmart
printers and all-in-one peripherals (also known as Multi-Function
Peripherals or MFPs), which can print, scan, copy, fax, and/or access
flash memory cards.

This package contains various tools for memory card access,
ink/toner/battery/consumable level checking, and inkjet printer
maintenance, along with python cups backends.

%package hpcups
Summary: Hpcups printer driver for Hewlett-Packard Co. Inkjet Printers and MFPs
License: BSD-3-Clause
Group: Publishing
Requires: %name-common = %{?epoch:%epoch:}%version-%release
Conflicts: %name-common < 3.13

%description hpcups
Hpcups driver is a raster driver that produces printer-ready-bits.
The hpcups driver only works CUPS. Hpcups does not use the APDK, but
is based on re-purposed APDK code.

%if_enabled python_code
%package gui
Summary: HPLIP graphical tools for Hewlett-Packard Co. Inkjet Printers and MFPs
License: GPL-2.0+
Group: Publishing
Obsoletes: xojpanel <= 0.91
Obsoletes: hpoj-xojpanel <= 0.91
Obsoletes: hplip-tools < 2.0
Provides: hplip-tools = 2.0
BuildArch: noarch

%if_enabled qt3
Requires: python%{pysuffix}-module-qt >= 3.16
%endif
%if_enabled qt4
Requires: python%{pysuffix}-module-PyQt4
%else
Requires: python%{pysuffix}-module-PyQt5
%endif

# some utils do require dbus user session
Requires: dbus-tools-gui 
# for python-notify
# Requires: notification-daemon
# for hp-scan -n
Requires: python%{pysuffix}-module-Pillow
# from fedora 3.10.9-9 patch 33 (= 133)
# Enable D-Bus threading (and require pygobject2) (bug #600932).
# patch33 -p1 -b .dbus-threads
Requires: python%{pysuffix}-module-pygobject

Requires: %name = %{?epoch:%epoch:}%version-%release

%description gui
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),
Business Inkjet, LaserJet, and LaserJet MFP.

This package contains the gui toolbox application for HPLIP,
with which several tasks such as memory card access,
ink/toner/battery/consumable level checking, and inkjet printer
maintenance can be done.

%if_enabled autostart
%package gui-autostart
Summary: GNOME/KDE/other XDGE autostart file for HPLIP graphical tools
License: GPL-2.0+
Group: Publishing
Requires: %name-gui = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description gui-autostart
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),
Business Inkjet, LaserJet, and LaserJet MFP.

This package contains the HPLIP gui toolbox application autostart file
for GNOME, KDE and other freedesktop compatible desktop environments.
%endif
%endif

%package recommends
Summary: recommended packages for hplip
License: GPL-2.0+
Group: Publishing
Requires: %name = %{?epoch:%epoch:}%version-%release
Requires: %name-hpcups = %{?epoch:%epoch:}%version-%release
Requires: %name-sane = %{?epoch:%epoch:}%version-%release
Requires: %name-gui = %{?epoch:%epoch:}%version-%release
Requires: notification-daemon
BuildArch: noarch

%description recommends
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package is a virtual package that installs packages
recommended for use with hplip.

%package common
Summary: Hewlett-Packard Co. Inkjet Driver Project
License: GPL-2.0+
Group: Publishing
Conflicts: udev-extras < 0.20090516-alt4

%description common
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains common libraries for
The Hewlett-Packard  Inkjet  Driver  Project.

%if_enabled PPDs
%package PPDs
Summary: PPDs for Hewlett-Packard Co. Inkjet Printers and MFPs (Deprecated)
License: MIT
Group: Publishing
Requires: %name-ps-PPDs = %{?epoch:%epoch:}%version-%release
Requires: %name-hpcups-PPDs = %{?epoch:%epoch:}%version-%release
Requires: %name-hpijs-PPDs = %{?epoch:%epoch:}%version-%release
# TODO: it seems it is not needed 
#Requires: foomatic-db >= 3.0.2-alt7
%if_enabled foomatic_rip
Requires: %{cups_filters}
%endif
BuildArch: noarch

%description PPDs
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

WARNING! foomatic static and dynamic ppd install is deprecated.
Feature can be used as is. Fixes or updates will not be provided.

%package ps-PPDs
Summary: PPDs for Hewlett-Packard Co. Inkjet Printers and MFPs for postscript HP printers
License: MIT
Group: Publishing
%if_enabled foomatic_rip
Requires: %{cups_filters}
%endif
Conflicts: %name-PPDs < %version
BuildArch: noarch

%description ps-PPDs
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains postscript printer definition files (PPDs) for postscript HP printers.

%package hpcups-PPDs
Summary: PPDs for HP Inkjet Printers and MFPs for hpcups cups driver (Deprecated)
License: MIT
Group: Publishing
%if_enabled foomatic_rip
Requires: %{cups_filters}
%endif
Requires: %name-hpcups = %{?epoch:%epoch:}%version-%release
Conflicts: %name-PPDs < %version
BuildArch: noarch

%description hpcups-PPDs
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains postscript printer definition files (PPDs) for hpcups cups driver.

%package hpijs-PPDs
Summary: PPDs for HP Inkjet Printers and MFPs for hpijs cups driver (Deprecated)
License: MIT
Group: Publishing
%if_enabled foomatic_rip
Requires: %{cups_filters}
%endif
Requires: %name-hpijs = %{?epoch:%epoch:}%version-%release
Conflicts: %name-PPDs < %version
BuildArch: noarch

%description hpijs-PPDs
HPLIP is an HP developed solution for printing, scanning, and faxing
with HP inkjet and laser based printers in Linux.

The HPLIP project provides printing support for nearly 1000 printer
models, including Deskjet, Officejet, Photosmart, PSC (Print Scan Copy),

This package contains postscript printer definition files (PPDs) for hpijs cups driver.
%endif

%package hpijs
Summary: Hewlett-Packard Co. Inkjet Driver Project (Deprecated)
License: BSD-3-Clause
Group: Publishing
Obsoletes: hpijs < 2.7
Provides: %hpijsname = %version
Requires: %name-common = %{?epoch:%epoch:}%version-%release
Requires: ghostscript

%description hpijs
hpijs is a collection of optimized drivers for HP printers.
hpijs supports the DeskJet 350C, 600C, 600C Photo, 630C, Apollo 2000,
Apollo 2100, Apollo 2560, DeskJet 800C, DeskJet 825, DeskJet 900,
PhotoSmart, DeskJet 990C, and PhotoSmart 100 series.

The  Hewlett-Packard  Inkjet  Driver  Project  is  a add-on to the GNU
Ghostscript  application. This driver is open source software based on
the  Hewlett  Packard  Appliance  Printing Development Kit APDK for
deskjet printers.

WARNING! HPIJS is deprecated. Feature can be used as is.
Fixes or updates will not be provided.

%if_enabled sane_backend
%package sane
Summary: SANE driver for scanners in HP's multi-function devices (from HPLIP)
License: GPL-2.0+
Group: Publishing
Requires: libsane
Requires: %name-common = %{?epoch:%epoch:}%version-%release
Obsoletes: libsane-hpoj <= 0.91

%description sane
SANE driver for scanners in HP's multi-function devices (from HPLIP)
%endif # sane_backend

%prep
%setup -q
# Remove proprietary binary blobs
rm -f prnt/hpcups/libImageProcessor-*.so

# For some patch we need to gunzip ppds
find . -name *.ppd.gz -exec gunzip '{}' ';'

%patch1 -p2
# let keep it as is.
#patch2 -p2

# # Fix desktop file.
%patch4 -p2 -b .desktop
%patch5 -p1
%patch6 -p1
%if_with python3
#patch8 -p2
%else
#patch7 -p2
%endif
%patch9 -p2

%patch101 -p1 -b .pstotiff-is-rubbish
%patch102 -p1 -b .strstr-const
%patch103 -p1 -b .ui-optional
%patch104 -p1 -b .no-asm
%patch105 -p1 -b .deviceIDs-drv
chmod +x %{SOURCE102} %{SOURCE103}
mv prnt/drv/hpijs.drv.in{,.deviceIDs-drv-hpijs}
%if_with python3
%{SOURCE103} \
%else
%{SOURCE102} \
%endif
       prnt/drv/hpcups.drv.in \
       prnt/drv/hpijs.drv.in.deviceIDs-drv-hpijs \
       > prnt/drv/hpijs.drv.in

%patch106 -p1 -b .udev-rules
%patch107 -p1 -b .retry-open
%patch108 -p1 -b .snmp-quirks
%patch109 -p1 -b .hpijs-marker-supply
%patch110 -p1 -b .clear-old-state-reasons
%patch111 -p1 -b .hpcups-sigpipe
%patch113 -p1 -b .bad-low-ink-warning
%patch114 -p1 -b .deviceIDs-ppd
%patch115 -p1 -b .ImageableArea
%patch116 -p1 -b .scan-tmp
%patch117 -p1 -b .log-stderr
%patch118 -p1 -b .parsing
%patch120 -p1 -b .dj990c-margin
%patch121 -p1 -b .strncpy
%patch122 -p1 -b .no-write-bytecode
%patch123 -p1 -b .silence-ioerror
%patch124 -p1 -b .sourceoption
%if_without ernie
%patch125 -p1 -b .no-ernie
rm prnt/hpcups/ErnieFilter.{cpp,h} prnt/hpijs/ernieplatform.h
%endif
#patch126 -p1 -b .appdata
%patch127 -p1 -b .check-cups
%patch130 -p1 -b .typo
%patch131 -p1 -b .use-binary-str
%patch132 -p1 -b .colorlaserjet-mfp-m278-m281
%patch133 -p1 -b .error-print-fix
%patch134 -p1 -b .hpfax-import-error-print
%patch135 -p1 -b .wifisetup-bad-call-fix
%patch137 -p1 -b .keyserver
%patch142 -p1 -b .add-ppd-crash
%patch143 -p1 -b .missing-links
%patch144 -p1 -b .hp-laserjet-3052-broken-scanning
%patch145 -p1 -b .hpmud-string-parse
%patch146 -p1 -b .m278-m281-needs-plugin
%patch147 -p1 -b .hpcups-crash
%patch148 -p1 -b .covscan
%patch149 -p1 -b .logging-segfault
%patch150 -p1 -b .systray-blockerror
%patch152 -p1 -b .missing-drivers

# from fedora 3.9.12-3/3.10.9-9
sed -i.duplex-constraints \
    -e 's,\(UIConstraints.* \*Duplex\),//\1,' \
    prnt/drv/hpcups.drv.in

%patch201 -p1 -b .download-plugin

# debian patches
%patch302 -p1
%patch303 -p1
%patch304 -p1
%patch305 -p1
%patch306 -p1
%patch307 -p1
%patch308 -p1
%patch310 -p1
%patch311 -p1
%patch312 -p1
%patch313 -p1
%patch314 -p1
%patch315 -p1
%patch317 -p1
%patch318 -p1
%patch319 -p1
%patch320 -p1
%patch321 -p1
%patch322 -p1
%patch323 -p1
%patch324 -p1
%patch325 -p1
%patch326 -p1
%patch327 -p1
%patch328 -p1
%patch329 -p1

# Conflicted patches
%patch112 -p1 -b .logdir

tar -xf %SOURCE6

#pushd prnt/hpijs
#%patch10 -p1
#popd
%patch12 -p1
%patch13 -p2
%if_with l10n
%patch14 -p2
%endif

egrep -lZr '#!/usr/bin/python$' . | xargs -r0 sed -i 's,#!/usr/bin/python$,#!/usr/bin/python%{pysuffix},'
fgrep -lZr '#!/usr/bin/env python' . | xargs -r0 sed -i 's,#!/usr/bin/env python,#!/usr/bin/python%{pysuffix},'

# ELF binary, if found
rm -f hpps hpcups dat2drv

%build

# we use source that is not pristine; in upstream they gzipped it :(
gzip_n_mov_ppd() {
#	mkdir tmp1; cp -a $1/*.ppd tmp1
	gzip -9 $1/*.ppd
#	mv tmp1/*.ppd $1/; rmdir tmp1
}

gzip_n_mov_ppd fax/ppd
gzip_n_mov_ppd prnt/ps
gzip_n_mov_ppd ppd/classppd/hpcups
gzip_n_mov_ppd ppd/classppd/ps
gzip_n_mov_ppd ppd/hpcups

# Work-around Makefile.am imperfections.
sed -i 's|^AM_INIT_AUTOMAKE|AM_INIT_AUTOMAKE([foreign subdir-objects])|g' configure.in
# Upstream uses old libtool, which causes problems (due to libhpmud requiring
# libhpdiscovery) when we try to remove rpath from it.
# Regenerating all autotools files works-around these rpath issues.
autoreconf -fisv

cat > /dev/null <<EOF
  --disable-option-checking  ignore unrecognized --enable/--with options
  --enable-static[=PKGS]  build static libraries [default=no]
  --disable-dependency-tracking  speeds up one-time build
  --enable-dependency-tracking   do not reject slow dependency extractors
  --enable-shared[=PKGS]  build shared libraries [default=yes]
  --enable-fast-install[=PKGS]
                          optimize for fast installation [default=yes]
  --disable-libtool-lock  avoid locking (might break parallel builds)
  --enable-doc-build     enable documentation build (default=yes)
  --enable-hpijs-only-build     enable hpijs only build (default=yes)(Deprecated)
  --enable-lite-build     enable lite build, print & scan only (default=no)
  --enable-hpcups-only-build     enable hpcups only build, print only (default=no)
  --enable-hpijs-install     enable hpijs install (default=no)(Deprecated)
  --enable-hpcups-install     enable hpcups install (default=yes)
  --enable-new-hpcups     enable new hpcups install (default=no)
  --enable-network-build    enable network build (default=yes)
  --enable-pp-build    enable parallel port build (default=no)(Deprecated)
  --enable-scan-build    enable scanner build (default=yes)
  --enable-gui-build    enable gui build (default=yes)
  --enable-fax-build    enable fax build (default=yes)
  --enable-apparmor_build    enable apparmor build (default=no)
  --enable-dbus-build    enable dbus build (default=yes)
  --enable-cups11-build    enable cups 1.1.x build (default=no)
  --enable-udev_sysfs_rules    Use SYSFS attribute instead of ATTR/ATTRS attribute in udev rules(default=no)
  --enable-shadow-build    enable shadow build (default=no)
  --enable-libusb01_build    Use libusb-0.1 instead of libusb-1.0 (default=no. i.e. libusb-1.0)
  --enable-foomatic-ppd-install    enable foomatic static ppd install (default=no)(Deprecated), uses hpppddir
  --enable-foomatic-drv-install    enable foomatic dynamic ppd install (default=no)(Deprecated), uses drvdir and hpppddir
  --enable-cups-drv-install    enable cups dynamic ppd install (default=yes), uses drvdir and hpppddir
  --enable-cups-ppd-install    enable cups static ppd install (default=no), uses hpppddir
  --enable-foomatic-rip-hplip-install    enable foomatic-rip-hplip install (default=no)(Deprecated), uses cupsfilterdir
  --enable-qt5    enable qt5 (default=no)
  --enable-qt4    enable qt4 (default=yes)
  --enable-qt3    enable qt3 (default=no)
  --enable-policykit    enable PolicyKit (default=no)
EOF

#we install foomatic data in separate package
# TODO
%configure \
    --with-mimedir=%{_datadir}/cups/mime \
    --disable-foomatic-rip-hplip-install \
    --enable-pp-build \
%if_enabled PPDs
    --enable-foomatic-ppd-install \
    --enable-foomatic-drv-install \
    --enable-cups-ppd-install \
%else
    --disable-foomatic-ppd-install \
    --disable-cups-ppd-install \
%endif
    --enable-hpijs-install \
%if_enabled python_code
    --enable-gui-build \
    --enable-fax-build \
    --enable-network-build=yes \
    %{subst_enable policykit} \
    %{subst_enable qt3} \
    %{subst_enable qt4} \
    %{subst_enable qt5} \
%if_enabled sane_backend
    --enable-scan-build \
%else
    --disable-scan-build \
%endif
%if_with python3
	 PYTHON=%{__python3}
%endif
%else
    --enable-hpijs-only-build 
%endif

%make

%install
install -d $RPM_BUILD_ROOT/%_datadir/cups/model/
%if_disabled PPDs
# in alt, ppds are stored with cups (not good?)
#mv $RPM_BUILD_ROOT/usr/share/ppd/HP/fax/HP-Fax-hplip.ppd.gz $RPM_BUILD_ROOT/%_datadir/cups/model/
install -m644 fax/ppd/HP-Fax-hplip.ppd $RPM_BUILD_ROOT/%_datadir/cups/model/
%endif

%make DESTDIR=%buildroot install \
%if_with python3
	 PYTHON=%{__python3}
%endif

%if_enabled python_code

%if_disabled udevacl
###
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/security/console.perms.d/
install -m 600 %{SOURCE4} $RPM_BUILD_ROOT%_sysconfdir/security/console.perms.d/80-hpmud.perms
%endif

#mkdir -p $RPM_BUILD_ROOT%_initdir/
#install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%_initdir/%name

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/hp

# Create /var/run/hplip
mkdir -p %buildroot%_runtimedir/hplip
## Create /run/hplip
#mkdir -p %{buildroot}/run/hplip
# Create /var/lib/hp
mkdir -p %{buildroot}%{_sharedstatedir}/hp

# install /usr/lib/tmpfiles.d/hplip.conf (bug #1015831)
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/hplip.conf <<EOF
# See tmpfiles.d(5) for details

d /run/hplip 0775 root lp -
EOF

# # Comment out all "setSizePolicy" calls, this function is incompatible with
# # PyQT/SIP <3.16
# # the code below is correct: it does'nt comments semilines ..., as previous
# # which cause syntax error in 1.6.6a, but is deprecated with PyQT = 3.16
# perl -p -i -e 'if (/^(.*setSizePolicy.*)$/) {$_="#".$_; if (/,\s*$/) {$endcomma=1}} elsif ($endcomma) {$_="#".$_; $endcomma=0}' `grep -l setSizePolicy $RPM_BUILD_ROOT%_datadir/%name/ui/*.py`

mkdir -p %{buildroot}%{_datadir}/appdata
cp %{SOURCE3} %{buildroot}%{_datadir}/appdata/

# Menu Icons
#install -pD -m644 %name.16.png $RPM_BUILD_ROOT%_miconsdir/hplip.png
#install -pD -m644 %name.32.png $RPM_BUILD_ROOT%_niconsdir/hplip.png
install -pD -m644 %name.48.png $RPM_BUILD_ROOT%_liconsdir/hplip.png

# TODO: switch to hp_logo in desktop?
install -pD -m644 %{buildroot}%{_datadir}/hplip/data/images/16x16/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/hplip.png
install -pD -m644 %{buildroot}%{_datadir}/hplip/data/images/32x32/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/hplip.png
install -pD -m644 %{buildroot}%{_datadir}/hplip/data/images/64x64/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/hplip.png

# Remove the installed /etc/sane.d/dll.conf
# because this is provided by the sane package:
rm -f $RPM_BUILD_ROOT%_sysconfdir/sane.d/dll.conf
# Remove other unneeded files
rm -f $RPM_BUILD_ROOT%_datadir/%name/%name
rm -f $RPM_BUILD_ROOT%_datadir/%name/hplip_readme.html
rm -f $RPM_BUILD_ROOT%_datadir/%name/hplip_overview.png

# fedora
rm -f %{buildroot}%{_datadir}/hplip/hplip-install
rm -rf %{buildroot}%{_datadir}/hplip/install.*
rm -f %{buildroot}%{_datadir}/hplip/uninstall.*
rm -f %{buildroot}%{_bindir}/hp-uninstall
rm -f %{buildroot}%{_datadir}/hplip/upgrade.*
rm -f %{buildroot}%{_bindir}/hp-upgrade
#rm -f %{buildroot}%{_bindir}/hp-config_usb_printer
#rm -f %{buildroot}%{_datadir}/hplip/config_usb_printer.*
#rm -f %{buildroot}%{_unitdir}/hplip-printer@.service
%endif # python_code

# Install other files for HPIJS
mkdir -p $RPM_BUILD_ROOT%_docdir/%hpijsname-%version
install -pD -m644 prnt/hpijs/README_LIBJPG  $RPM_BUILD_ROOT%_docdir/%hpijsname-%version/
install -d %{buildroot}%{_man1dir}/
install -p -m644 %{SOURCE202} %{buildroot}%{_man1dir}/

%if_enabled PPDs
#### Remove the installed /usr/bin/foomatic-rip
#### because this is provided by the cups-filters package:
###rm %{buildroot}%{_bindir}/foomatic-rip

### a piece of ancient wisdom of SuSE
# Make some general tests and adjustments for all PPDs (see manufacturer-PPDs.spec):
pushd %{buildroot}%{_datadir}/ppd/HP
#pushd foomatic-db/db/source/PPD/HP
for ppd in *.ppd{,.gz,.bz2}; 
do
       [ -e $ppd ] && sh %{SOURCE7} $ppd
done
popd
# End of the general tests and adjustments for all PPDs.
%endif # PPDs

%if_enabled halacl
# fedora fdi policy
mkdir -p %{buildroot}%{_datadir}/hal/fdi/policy/10osvendor
install -p -m644 %{SOURCE100} %{buildroot}%{_datadir}/hal/fdi/policy/10osvendor/22-hplip.fdi
%endif

# hack to properly compile .py files
python%{pysuffix} -m compileall $RPM_BUILD_ROOT%_datadir/%name


# removing unpackaged files
pushd $RPM_BUILD_ROOT
#rm  usr/share/hplip/hplip-install usr/share/hplip/install.*
popd

# ELF object out of allowed directory tree
rm -rf \
   %{buildroot}%{_datadir}/hplip/locatedriver* \
   %{buildroot}%{_datadir}/hplip/dat2drv*

# Regenerate hpcups PPDs on upgrade if necessary (bug #579355).
install -p -m755 %{SOURCE101} %{buildroot}%{_bindir}/hpcups-update-ppds

mkdir -p %{buildroot}%{_sysconfdir}/sane.d/dll.d
echo hpaio > %{buildroot}%{_sysconfdir}/sane.d/dll.d/hpaio

# Create an empty plugins directory to make sure it gets the right
# SELinux file context (bug #564551).
mkdir -p %{buildroot}%{_datadir}/hplip/prnt/plugins

# traditional place for udev rules
mkdir -p %{buildroot}/lib
mv %{buildroot}/usr/lib/udev %{buildroot}/lib/

# remove hp-uiscan.desktop
rm -f %buildroot%_desktopdir/hp-uiscan.desktop

%pre
# TODO: drop it somewhere after p7 release
# no more services
if [ -f %_initrddir/%name ]; then
    /sbin/service hplip condstop ||:
    /sbin/chkconfig --del hplip ||:
fi

%post
/sbin/service cups condrestart ||:

%preun
if [ "$RPM_INSTALL_ARG1" -eq 0 ]; then
    /sbin/service cups condrestart ||:
fi

#fedora use it in post...
#%post hpijs
#%{_bindir}/hpcups-update-ppds &>/dev/null ||:

%if_enabled sane_backend
%preun sane
# no more /etc/sane.d/dll.conf - using /etc/sane.d/dll.d
# Remove HPLIP driver from /etc/sane.d/dll.conf
if [ "$1" = 0 ]; then
        %__subst 's|^\([[:space:]]*hpaio[[:space:]]*\)$|#\1|' %_sysconfdir/sane.d/dll.conf
fi
%endif #sane_backend

%files
%doc %_defaultdocdir/%name-%version
%if_enabled python_code
%dir %{_sysconfdir}/hp
%config %{_sysconfdir}/hp/hplip.conf
#deprecated
#%_initdir/%name
# C libraries for Python
%_libdir/python*/site-packages/*.so*
%if_disabled udevacl
# logged-in user gave direct access to the printers
%_sysconfdir/security/console.perms.d/80-hpmud.perms
%endif
%exclude %_libdir/python*/site-packages/*.la
# CUPS backend
%_prefix/lib/cups/backend/hp
%_prefix/lib/cups/backend/hpfax
# python
%{_bindir}/hp-align
%{_bindir}/hp-check-plugin
%{_bindir}/hp-clean
%{_bindir}/hp-colorcal
%{_bindir}/hp-config_usb_printer
%{_bindir}/hp-diagnose_plugin
%{_bindir}/hp-diagnose_queues
%{_bindir}/hp-fab
%{_bindir}/hp-firmware
%{_bindir}/hp-info
%{_bindir}/hp-levels
%{_bindir}/hp-makeuri
%if_enabled policykit
%{_bindir}/hp-pkservice
%endif
%{_bindir}/hp-plugin
%{_bindir}/hp-probe
%{_bindir}/hp-query
%{_bindir}/hp-scan
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_bindir}/hp-unload
# Files
%dir %{_datadir}/hplip
%{_datadir}/hplip/align.py*
%{_datadir}/hplip/check-plugin.py*
%{_datadir}/hplip/clean.py*
%{_datadir}/hplip/colorcal.py*
%{_datadir}/hplip/config_usb_printer.py*
%{_datadir}/hplip/diagnose_plugin.py*
%{_datadir}/hplip/diagnose_queues.py*
%{_datadir}/hplip/fab.py*
%{_datadir}/hplip/fax
#exclude %{_datadir}/hplip/fax/pstotiff*
%{_datadir}/hplip/firmware.py*
%{_datadir}/hplip/hpdio.py*
%{_datadir}/hplip/hplip_clean.sh
%{_datadir}/hplip/hpssd*
%{_datadir}/hplip/info.py*
%{_datadir}/hplip/__init__.py*
%{_datadir}/hplip/levels.py*
%{_datadir}/hplip/makeuri.py*
%{_datadir}/hplip/plugin.py*
%{_datadir}/hplip/probe.py*
%{_datadir}/hplip/query.py*
%{_datadir}/hplip/scan.py*
%{_datadir}/hplip/sendfax.py*
%{_datadir}/hplip/setup.py*
%{_datadir}/hplip/testpage.py*
%{_datadir}/hplip/timedate.py*
%{_datadir}/hplip/unload.py*
%if_enabled policykit
%{_datadir}/hplip/pkservice.py*
%{_datadir}/polkit-1/actions/com.hp.hplip.policy
%{_unitdir}/hplip-printer@.service
%endif
%if_with python3
#{_datadir}/hplip/__pycache__/check-plugin.*
%dir %{_datadir}/hplip/__pycache__
%endif
# global dbus service
%{_datadir}/dbus-1/system-services/com.hp.hplip.service
/etc/dbus-1/system.d/com.hp.hplip.conf

# Directories
%{_datadir}/hplip/base
%{_datadir}/hplip/copier
%dir %{_datadir}/hplip/data
#%{_datadir}/hplip/data/firmware
%{_datadir}/hplip/data/ldl
%{_datadir}/hplip/data/localization
%{_datadir}/hplip/data/models
%{_datadir}/hplip/data/pcl
%{_datadir}/hplip/data/ps
%{_datadir}/hplip/installer
%{_datadir}/hplip/pcard
%{_datadir}/hplip/prnt
%{_datadir}/hplip/scan
%dir %_sharedstatedir/hp
#%_sharedstatedir/hp/hplip.state
#%dir %attr(0775,root,lp) %{_var}/log/hp
#%dir %attr(1775,root,lp) %{_var}/log/hp/tmp
%dir %attr(0775,root,lp) %_runtimedir/hplip
#%{_sysconfdir}/cron.daily/hplip_cron
%endif

%files hpcups
# CUPS drv
%dir %{_datadir}/cups/drv/hp
%{_datadir}/cups/drv/hp/hpcups.drv
# CUPS filter
%_prefix/lib/cups/filter/hpcups
%_prefix/lib/cups/filter/hpcupsfax
%{_bindir}/hpcups-update-ppds
# moved from common
%_prefix/lib/cups/filter/hpps
%if_enabled cupstifffilter
/usr/lib/cups/filter/pstotiff
%{_datadir}/cups/mime/pstotiff.convs
%{_datadir}/cups/mime/pstotiff.types
%endif


%if_enabled python_code
%files gui
# xdg autostart instead of init.d (do we need them???)
# The systray applet doesn't work properly (displays icon as a
# window), so don't ship the launcher yet.
#/etc/xdg/autostart/hplip-systray.desktop
#_bindir/hp-*
%{_bindir}/hp-check
%{_bindir}/hp-devicesettings
%{_bindir}/hp-faxsetup
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-makecopies
%{_bindir}/hp-print
%{_bindir}/hp-printsettings
%{_bindir}/hp-systray
#%{_bindir}/hp-toolbox.wrapper
%{_bindir}/hp-toolbox
%{_bindir}/hp-wificonfig
%{_bindir}/hp-uiscan
# Files
%{_datadir}/hplip/check.py*
%{_datadir}/hplip/devicesettings.py*
%{_datadir}/hplip/faxsetup.py*
%{_datadir}/hplip/linefeedcal.py*
%{_datadir}/hplip/makecopies.py*
%{_datadir}/hplip/print.py*
%{_datadir}/hplip/toolbox.py*
%{_datadir}/hplip/systray.py*
%{_datadir}/hplip/printsettings.py*
%{_datadir}/hplip/wificonfig.py*
%{_datadir}/hplip/uiscan.py*
# garbage
%{_bindir}/hp-doctor
%{_bindir}/hp-logcapture
%{_bindir}/hp-pqdiag
%{_datadir}/hplip/doctor.py*
%{_datadir}/hplip/logcapture.py*
%{_datadir}/hplip/pqdiag.py*
# Directories
%{_datadir}/hplip/data/images
# qt3 interface
%if_enabled qt3
%{_datadir}/hplip/plugins
%{_datadir}/hplip/ui
%endif
# qt4 interface
%if_enabled qt4
%{_datadir}/hplip/ui4
%endif
# qt5 interface
%if_enabled qt5
%{_datadir}/hplip/ui5
%endif
# gui data
%{_datadir}/appdata/hplip.appdata.xml
# HPLIP menu files
%_desktopdir/%name.desktop
#_niconsdir/hplip.png
#_liconsdir/hplip.png
#_miconsdir/hplip.png
%_iconsdir/hicolor/*/apps/hplip.png

%if_enabled autostart
%files gui-autostart
/etc/xdg/autostart/hplip-systray.desktop
%endif
%endif

%if_enabled PPDs
%files PPDs
### moved to foomatic
###%_datadir/cups/model/foomatic-ppds
%files hpijs-PPDs
%_datadir/ppd/HP/*-hpijs*.ppd*
%files hpcups-PPDs
%_datadir/ppd/HP/*
%exclude %_datadir/ppd/HP/*-hpijs*.ppd*
%exclude %_datadir/ppd/HP/*-ps.ppd*
%files ps-PPDs
%_datadir/ppd/HP/*-ps.ppd*
%else
%_datadir/cups/model/HP-Fax-hplip.ppd*
%endif

%files recommends

%files common
# HPIP
%{_libdir}/libhpip.so.0
%{_libdir}/libhpip.so.0.0.1
%{_libdir}/libhpipp.so.0
%{_libdir}/libhpipp.so.0.0.1
%{_libdir}/libhpdiscovery.so.0
%{_libdir}/libhpdiscovery.so.0.0.1
%exclude %_libdir/libhpip*so
%exclude %_libdir/libhpdiscovery.so
# The so symlink is required here (see RH bug #489059).
%{_libdir}/libhpmud.so
%{_libdir}/libhpmud.so.0
%{_libdir}/libhpmud.so.0.0.6
%{_udevrulesdir}/56-hpmud.rules
%{_tmpfilesdir}/hplip.conf

%files hpijs
%doc %_docdir/%hpijsname-%version
%_bindir/%hpijsname
%{_man1dir}/%hpijsname.1*
%dir %{_datadir}/cups/drv/hp
%{_datadir}/cups/drv/hp/hpijs.drv

%if_enabled sane_backend
# SANE
%files sane
%config(noreplace) %{_sysconfdir}/sane.d/dll.d/hpaio
%{_datadir}/hal/fdi/preprobe/10osvendor/20-hplip-devices.fdi
%if_enabled halacl
# fedora's hal-based acl
%{_datadir}/hal/fdi/policy/10osvendor/22-hplip.fdi
%endif
%_libdir/sane/libsane-hpaio*.so*
%exclude %_libdir/sane/libsane-hpaio*.la
# is it needed?
#%{_datadir}/hplip/hpaio.desc
%endif

#TODO
#*** SANE Backend ***
#SANE - need test with real devices and SANE software
#SANE - merge SuSE trigger on installing sane

%changelog
* Mon Dec 16 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.12-alt1
- New version.
- Added support for the following new Printers:
  + HP Color LaserJet Pro M155a
  + HP Color LaserJet Pro M155nw
  + HP Color LaserJet Pro M156a
  + HP Color LaserJet Pro M156nw
  + HP Color LaserJet Pro M255dn
  + HP Color LaserJet Pro M255dw
  + HP Color LaserJet Pro M255nw
  + HP Color LaserJet Pro M256dn
  + HP Color LaserJet Pro M256dw
  + HP Color LaserJet Pro M256nw
  + HP Color LaserJet Pro MFP M182n
  + HP Color LaserJet Pro MFP M182nw
  + HP Color LaserJet Pro MFP M183fw
  + HP Color LaserJet Pro MFP M184n
  + HP Color LaserJet Pro MFP M184nw
  + HP Color LaserJet Pro MFP M185fw
  + HP Color LaserJet Pro MFP M282nw
  + HP Color LaserJet Pro MFP M283cdw
  + HP Color LaserJet Pro MFP M283fdn
  + HP Color LaserJet Pro MFP M283fdw
  + HP Color LaserJet Pro MFP M284nw
  + HP Color LaserJet Pro MFP M285cdw
  + HP Color LaserJet Pro MFP M285fdn
  + HP Color LaserJet Pro MFP M285fdw
- Fix select PPD file in Qt5 GUI (ALT #37610).

* Wed Nov 06 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.11-alt1
- New version.
- Added support for the following new Printers:
  + HP Color LaserJet MFP M776dn
  + HP Color LaserJet Flow MFP M776z
  + HP Color LaserJet Flow MFP M776zs
  + HP Color LaserJet M856dn
  + HP Color LaserJet M856x
  + HP Color LaserJet E85055dn

* Thu Oct 31 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.10-alt1
- New version.
- Added support for the following new Printers:
  + HP Color LaserJet MFP M776dn
  + HP Color LaserJet Flow MFP M776z
  + HP Color LaserJet Flow MFP M776zs
  + HP Color LaserJet M856dn
  + HP Color LaserJet M856x
  + HP Color LaserJet E85055dn
- Build with Python3 (ALT #37289).

* Thu Aug 29 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.8-alt1
- New version.
- Added support for new printers:
  + HP DesignJet T1530 Postscript
  + HP DesignJet T2530 Postscript
  + HP DesignJet T930 Postscript
  + HP DesignJet T1600 Postscript Printer
  + HP DesignJet T1600dr Postscript Printer
  + HP DesignJet T2600 Postscript MFP
  + HP LaserJet Pro MFP M329dn
  + HP LaserJet Pro MFP M329dw
  + HP LaserJet Pro M305d
  + HP LaserJet Pro M304a
  + HP LaserJet Pro M305dn
  + HP LaserJet Pro M305dw

* Sat Jun 29 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.6-alt1
- New version.
- Added support for new printers:
  + HP Smart Tank 500 series
  + HP Smart Tank 530 series
  + HP Smart Tank Plus 570 series
  + HP Smart Tank Plus 650
  + HP Smart Tank 610
  + HP Smart Tank Plus 550
  + HP Smart Tank 510
  + HP Neverstop Laser MFP 1200a
  + HP Neverstop Laser MFP 1200w
  + HP Laser NS MFP 1005
  + HP Laser NS MFP 1005w
  + HP Neverstop Laser 1000a
  + HP Neverstop Laser 1000w
  + HP Laser NS 1020
  + HP Laser NS 1020w
  + HP DesignJet T2600dr Postscript MFP
  + HP DesignJet XL 3600 PS MFP
  + HP Color LaserJet Pro M453cdn
  + HP Color LaserJet Pro M454dn
  + HP Color LaserJet Pro M454cdn
  + HP Color LaserJet Pro M453cdw
  + HP Color LaserJet Pro M454nw
  + HP Color LaserJet Pro M454dw
  + HP Color LaserJet Pro M454cdw
  + HP Color LaserJet Pro MFP M479dw
  + HP Color LaserJet Pro MFP M478fcdn
  + HP Color LaserJet Pro MFP M479fdn
  + HP Color LaserJet Pro MFP M479fcdn
  + HP Color LaserJet Pro MFP M478fcdw
  + HP Color LaserJet Pro MFP M479fdw
  + HP Color LaserJet Pro MFP M479fnw
  + HP Color LaserJet Pro MFP M479fcdw
  + HP LaserJet Pro MFP M428dw
  + HP LaserJet Pro MFP M429dw
  + HP LaserJet Pro MFP M428fdn
  + HP LaserJet Pro MFP M428c1
  + HP LaserJet Pro MFP M428c3
  + HP LaserJet Pro MFP M428m
  + HP LaserJet Pro MFP M429fdn
  + HP LaserJet Pro MFP M428fdw
  + HP LaserJet Pro MFP M428c2
  + HP LaserJet Pro MFP M428c4
  + HP LaserJet Pro MFP M429fdw
  + HP LaserJet Pro M404d
  + HP LaserJet Pro M405d
  + HP LaserJet Pro M404n
  + HP LaserJet Pro M405n
  + HP LaserJet Pro M404dn
  + HP LaserJet Pro M404c1
  + HP LaserJet Pro M404c3
  + HP LaserJet Pro M404m
  + HP LaserJet Pro M405dn
  + HP LaserJet Pro M404dw
  + HP LaserJet Pro M404c2
  + HP LaserJet Pro M404c4
  + HP LaserJet Pro M405dw

* Thu May 23 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.5-alt2
- Add Russian localization to desktop file.
- Remove hp-uiscan.desktop.

* Tue May 14 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.5-alt1
- New version.
- Added support for new printers:
  + HP LaserJet Enterprise M507n
  + HP LaserJet Enterprise M507dn
  + HP LaserJet Enterprise M507x
  + HP LaserJet Enterprise M507dng
  + HP LaserJet Managed E50145dn
  + HP LaserJet Managed E50145x
  + HP LaserJet Enterprise MFP M528dn
  + HP LaserJet Enterprise MFP M528f
  + HP LaserJet Enterprise Flow MFP M528c
  + HP LaserJet Enterprise Flow MFP M528z
  + HP LaserJet Managed MFP E52645dn
  + HP LaserJet Managed Flow MFP E52645c
  + HP Color LaserJet Managed E75245dn
  + HP Color LaserJet Enterprise M751n
  + HP Color LaserJet Enterprise M751dn
  + HP PageWide XL 3900PS MFP
  + HP OfficeJet Pro 8030 All-in-One Printer series
  + HP OfficeJet Pro 8020 All-in-One Printer series
  + HP OfficeJet 8020 All-in-One Printer Series
  + HP OfficeJet 8010 All-in-One Printer series

* Thu Mar 28 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.3-alt1
- New version.
- Added support for new printers:
  + HP OfficeJet Pro All-in-One 9010
  + HP OfficeJet Pro All-in-One 9020
  + HP OfficeJet All-in-One 9010
  + HP PageWide XL 4100 Printer
  + HP PageWide XL 4100 MFP
  + HP PageWide XL 4600 Printer
  + HP PageWide XL 4600PS MFP
  + HP Color LaserJet Managed MFP E77422a
  + HP Color LaserJet Managed MFP E77422dv
  + HP Color LaserJet Managed MFP E77422dn
  + HP Color LaserJet Managed MFP E77428dn
  + HP LaserJet MFP E72425a
  + HP LaserJet MFP E72425dv
  + HP LaserJet MFP E72425dn
  + HP LaserJet MFP E72430dn
  + HP LaserJet Managed MFP E62655dn
  + HP LaserJet Managed MFP E62665hs
  + HP LaserJet Managed Flow MFP E62665h
  + HP LaserJet Managed Flow MFP E62675z
  + HP LaserJet Managed Flow MFP E62665z
  + HP LaserJet Managed E60155dn
  + HP LaserJet Managed E60165dn
  + HP LaserJet Managed E60175dn
  + HP Color LaserJet Managed E65150dn
  + HP Color LaserJet Managed E65160dn
  + HP Color LaserJet Managed MFP E67650dh
  + HP Color LaserJet Managed Flow MFP E67660z

* Thu Feb 07 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.1-alt2
- Autodetect auth type for modern ALT distro (ALT #36053).

* Fri Feb 01 2019 Andrey Cherepanov <cas@altlinux.org> 1:3.19.1-alt1
- New version.
- Added support for new printers:
  + HP LaserJet Managed MFP E82540du, E82550du, E82560du;
  + HP Color LaserJet Managed MFP E87640du, E87650du, E87660du.
- Added support for the HP Scanjet Pro 2500 f1.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.18.12-alt1
- New version.

* Mon Nov 12 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.18.10-alt1
- New version.

* Fri Nov 02 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.18.9-alt1
- New version (ALT #35531).
- Build with Qt5 (ALT #35571).

* Fri Jul 27 2018 Pavel Akopov <pak@altlinux.ru> 1:3.18.6-alt2
- added translation patch

* Fri Jul 13 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.18.6-alt1
- new version

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.17.11-alt1
- new version

* Wed Oct 25 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.17.10-alt1
- new version

* Sat Oct 14 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.17.9-alt1
- new version

* Tue Aug 01 2017 Sergey V Turchin <zerg@altlinux.org> 1:3.16.11-alt4
- fix download plugin
- fix fax setup
- fix polkit action placement

* Thu Feb 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.16.11-alt3
- added hplip-3.16.11-alt-auth.patch
- disabled noernie patch
- added license for ErnieFilter code

* Wed Feb 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.16.11-alt2
- Sisyphus release (closes: #33106)
- PPD* subpackages are now optional as they are deprecated
- cups/filter/foomatic-rip dependency disabled by default
- foomatic-db moved out from requires

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.16.11-alt1
- new version

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.16.10-alt2
- 3.16.10 build

* Thu Nov 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.16.7-alt2
- reverted back to 3.16.7 due to problems in 3.16.10

* Wed Nov 09 2016 Igor Vlasenko <viy@altlinux.ru> 3.16.10-alt1
- new version

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 3.16.7-alt1
- new version (closes: #31946)

* Fri Oct 23 2015 Igor Vlasenko <viy@altlinux.ru> 3.15.9-alt1
- new version

* Thu Nov 20 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.10-alt1
- new version

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.6-alt1
- new version (closes: #30203)

* Mon Jun 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.3-alt2
- added watch file
- added upstream-signing-key.asc

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.14.3-alt1
- new version

* Wed Feb 26 2014 Anton Farygin <rider@altlinux.ru> 3.13.9-alt2
- NMU: fixed requires - foomatic-filters now is 
  integraded to cups-filters package.

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 3.13.9-alt1
- new version

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 3.12.11-alt1
- new version

* Thu Nov 22 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.10a-alt0.M60P.1
- backport

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.10a-alt1
- new version 3.12.10a

* Sat Sep 29 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.9-alt2
- build with cups 1.6

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.9-alt1
- new version

* Wed Aug 08 2012 Igor Vlasenko <viy@altlinux.ru> 3.12.6-alt1
- new version

* Tue Dec 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.10-alt1.M60P.1
- backport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.10-alt2
- updated fedora patches

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.11.10-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.10-alt0.M60P.1
- M60P backport

* Thu Oct 20 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.10-alt1
- new version 3.11.10

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt2.M60P.1
- backport

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt3
- updated fedora patches
- use /etc/sane.d/dll.d

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt2
- CVE-2011-2722

* Fri Jul 29 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.7-alt1
- new version

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.5-alt0.M51.1
- M51 backport

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.5-alt1
- new version

* Wed Mar 30 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.3-alt1
- new version

* Sat Feb 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt4
- marked noarch packages

* Fri Feb 18 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt3
- added conflicts (closes: #23348)
- synced fedora patches

* Fri Jan 28 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt2
- restored .desktop patch

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 3.11.1-alt1
- new version

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt4
- added fedora patches as of 3.10.9-9
- added gui-autostart

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt3
- added hpcups driver and PPDs subpackages (closes: 24624)

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt0.M50P.1
- p5 backport

* Sat Nov 20 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt0.M51.1
- backport

* Sat Nov 20 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt2
- added fedora patches as of 3.10.9-6

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.9-alt1
- new version

* Tue Aug 03 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.6-alt0.M51.1
- backport

* Tue Aug 03 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.6-alt1
- new version

* Tue May 11 2010 Igor Vlasenko <viy@altlinux.ru> 3.10.2-alt1
- new version

* Tue Jan 26 2010 Igor Vlasenko <viy@altlinux.ru> 3.9.12-alt0.M51.1
- backport

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 3.9.12-alt1
- new version

* Sat Oct 10 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.8-alt4
- enabled udev acl (via console kit)

* Tue Oct 06 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.8-alt3
- moved hpijs.drv

* Mon Oct 05 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.8-alt2
- PPDs split into hpcups PPDs and hpijs PPDs.
- fixed hplip dependencies (closes #21827)

* Wed Sep 09 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.8-alt1
- new version

* Thu Jul 23 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.4b-alt3
- rebuild,
- does not require qt3, close #20615

* Fri May 15 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.4b-alt2
- fixed requires

* Wed May 13 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.4b-alt1
- new version

* Wed Apr 08 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.2-alt0.2
- experimental build 2

* Mon Apr 06 2009 Igor Vlasenko <viy@altlinux.ru> 3.9.2-alt0.1
- new version
- experimental build

* Sun Dec 07 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.10-alt3
- lenient hplip-fixppd - warns only (todo: report upstream)

* Thu Dec 04 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.10-alt2
- fixed and loosed dependencies
- added recommends subpackage

* Wed Dec 03 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.10-alt1
- new version
- spec cleanup: foomatic stuff is now in foomatic-db

* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.9-alt1
- new version

* Thu Jul 31 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.7-alt1
- new version

* Sat Jul 26 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.6b-alt1
- version 2.6.8b 

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.6-alt1
- new version
- Update hplip.fdi for new kernels: info.bus -> info.subsystem.

* Fri May 30 2008 Igor Vlasenko <viy@altlinux.ru> 2.8.5-alt1
- new version

* Tue Jan 08 2008 Igor Vlasenko <viy@altlinux.ru> 2.7.12-alt1
- new version

* Thu Nov 22 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.10-alt3
- thanks to mithraen@:
  + added provides hplip-tools
  + added Requires: python-module-imaging for hp-scan -n mode

* Wed Nov 07 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.10-alt2
- removed dependency on printer-drivers-utils

* Mon Oct 22 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.10-alt1
- new version

* Sat Sep 29 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.9-alt1
- added security patch (thanks to ldv@)
- new version

* Thu Sep 13 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.7-alt2
- resolved conflict with foomatic-db

* Wed Aug 22 2007 Igor Vlasenko <viy@altlinux.ru> 2.7.7-alt1
- new version
  * Replaced hpiod with the new HP Multi-Point Transport Driver (hpmud).
  * Hpmud is a shared library instead of a daemon.
  * Hpssd is started automatically when needed by HPLIP.
- removed foomatic-db-hpijs snapshots (included upstream)
- removed hp-toolbox.wrapper (hp-toolbox is already fixed)
- removed init script for hpssd 
  (it is is started automatically when needed by HPLIP)
- hplip-tools renamed and rearranged to hplip-gui
- added pam_console support.

* Wed May 16 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.4a-alt1
- new version
- foomatic-db-hpijs snapshot 20070516

* Mon Apr 02 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.3-alt1
- new version
- new foomatic snapshot 20070327 

* Thu Mar 01 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.2-alt1
- new version

* Wed Feb 28 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2
- foomatic-db-hpijs snapshot 20070227

* Thu Jan 25 2007 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1
- new version

* Thu Jan 18 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt5
- foomatic_snapshot updated to 20070117
- fixes for x86_64 (thanks to Dmitriy Khanzhin - dimajin-sandy.ru)

* Tue Jan 02 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt4
- PPDs are moved to separate package
- removed .desktop (menu is used again due to Configuration/Printing)

* Tue Jan 02 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt3
- spec cleanup -- removed manual links as they are already created

* Mon Jan 01 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt0.M30.1
- backport for M30

* Mon Jan 01 2007 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt2
- enabled PPDs by default (some hplip tools do require them)
- hplip initscript merge

* Sat Dec 23 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.12-alt1
- new version
- spec cleanup
- removed menu (now .desktop is used)

* Sat Nov 11 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.10-alt1
- new version
- new foomatic snapshot 20061109

* Sat Sep 23 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.9-alt1
- new version
- new foomatic snapshot 20060922 

* Fri Sep 08 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt2
- new foomatic snapshot 20060906 

* Tue Sep 05 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.7-alt1
- new version

* Fri Aug 25 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt0.M30.4.1
- backport for M30

* Mon Aug 07 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt4
- set default url viewer to url_handler.sh
  (hplip-1.6.6a-alt-urlhandler.patch)

* Thu Aug 03 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt3
- all python code moved to package hplip-tools
- BuildRequires python-devel according to python policy
- added hpfax cups backend
- added build of ppds (disabled)
- OpenSuSE experience partially integrated
- fedora experience partially integrated

* Sun Jul 30 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt2
- libhpip moved to package common --- this eliminates 
  printing system dependency on python.

* Thu Jul 27 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt1
- new fresh versions of hplip, hpijs, foomatic-db-hpijs
- build for Sisyphus

* Fri Jul 21 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt0
- build for Daedalus 

* Wed Jul 12 2006 Igor Vlasenko <viy@altlinux.ru> 1.6.6a-alt0.M30.1
- new fresh versions of hplip, hpijs, foomatic-db-hpijs
- backport for M30

* Fri Dec 02 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.4-alt3.1
- rebuild with libnetsnmp.so.9 .

* Mon Sep 19 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt3
- update initscript (add --displayname)
- Add Requires to package service-0.5.9-alt1
- Fix absolute symlinks (#7984)
- Update Buildreq

* Fri Sep 09 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt2.2
- Correct SANE backend scripts and etc

* Sun Sep 04 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt2.1
- Update foomatic version to new snapshot at 20050903
- Add Provides: foomatic-db-hpijs = %%fooversion-%%foomatic_snapshot
- Add PreReq: cups

* Sun Sep 04 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt2
- FIX (thanks Dmitry Vukolov)
  + mistake in "Provides hplip-hpijs-%%hpijsversion"
  + Provides/Obsoletes in hplip-foomatic
  + PreReq in hplip-foomatic
  + remove automatic requirements to gcc-g77
  + correct descriptions
  + correct mistake in hplip.desktop
  + correct hplip.menu (change title, section and add icons)

* Mon Aug 22 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt1
- Initscript fix hack
- Replace #!/usr/bin/env python  by the #!/usr/bin/python

* Thu Aug 18 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt0.2
- Init script cleanup
- Local hack in initscript for work hpssd.py from it (start, stop, status) 

* Mon Aug 08 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.4-alt0.1
- Update to new version 0.9.4
- Create link %_bindir/hp-* to %_datadir/%name/*

* Tue May 31 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.3-alt0.2
- FIX rpm conflicts with hpijs <= 2.0

* Sun May 29 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.3-alt0.1
- Update to new version 0.9.3
- Add variable %%hplip_minor

* Thu May 19 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.2-alt4
- Correct python builds
- Update BuildRequires and spec cleanup
- Add menu files
- Add correct QTDIR

* Sat May 14 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.2-alt3
- SPEC cleanup
- Add Requires to python-module-PyQt

* Fri May 13 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.2-alt2
- Add initial hplip.init for ALT Linux Sisyphus

* Mon May 09 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.2-alt1
- Update 
  - to new version HPLIP 0.9.2
  - version of hpijs componets to 2.1.2
  - Build Requires
  - spec according spec from Mandrake (Mandriva) linux
- Add conflicts with hpijs < 2.0
- Spec clean up
- Remove all patches
- Correct license
- Devide four packages hplip, hplip-hpijs, hplip-sane, hplip-foomatic

* Mon May 09 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.1-alt2
- Update to new foomatic-db-hpijs snapshot 20050508 (v.1.5)

* Mon Apr 18 2005 Serge A. Volkov <vserge at altlinux.ru> 0.9.1-alt1
- Update to new version 0.9.1
- Disable
  - patch1
  - buils with SANE
- Add patch from MDK package: hplip-0.9.1-HP-DeskJet_450-Battery.patch

* Sun Jan 09 2005 Serge A. Volkov <vserge at altlinux.ru> 0.8.4-alt1
- Add patch from Debian
- Initial release
