#
# spec file for package libevt
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: libevt
Version: 20140411
Release: alt2

Summary: Library and tools to access the Windows Event Log (EVT) format
License: LGPLv3+ and GFDLv1.3+
Group: File tools

Url: http://code.google.com/p/libevt/
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSYm01VnUtLXNUZ2M/libevt-alpha-20131013.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>
Source: %name-alpha-%version.tar.gz
Source1: Windows_Event_Log_(EVT).pdf
Source2: %name.watch

Patch1: upstream-CVE-2018-8754.patch

# Some dependencies are missing on excluded architectures
ExcludeArch: %arm aarch64

BuildRequires: pkg-config
BuildRequires: python-dev
BuildRequires: pkgconfig(libbfio) >= 20120426
BuildRequires: pkgconfig(libcdata) >= 20120425
BuildRequires: pkgconfig(libcfile) >= 20120526
BuildRequires: pkgconfig(libclocale) >= 20120425
BuildRequires: pkgconfig(libcnotify) >= 20120425
BuildRequires: pkgconfig(libcpath) >= 20120701
BuildRequires: pkgconfig(libcsplit) >= 20120701
BuildRequires: pkgconfig(libcthreads) >= 20130723
BuildRequires: pkgconfig(libfdatetime) >= 20120522
BuildRequires: pkgconfig(libfguid) >= 20120426
BuildRequires: pkgconfig(libregf) >= 20120405
BuildRequires: pkgconfig(libuna) >= 20120425
BuildRequires: pkgconfig(libwrc) >= 20120405
# build fails with version in factory, use internal version
#verified 10/13/2013
#BuildRequires:  pkgconfig(libcerror) >= 20130904
# not released as a package by upstream
#BuildRequires:  pkgconfig(libcstring) >= 20120425
#BuildRequires:  pkgconfig(libcsystem) >= 20120425
#BuildRequires:  pkgconfig(libcdirectory) >= 20120423
#BuildRequires:  pkgconfig(libfwnt) >= 20120426
#BuildRequires:  pkgconfig(libfwevt) >= 20120426
#BuildRequires:  pkgconfig(libfvalue) >= 20120428
#BuildRequires:  pkgconfig(libfdata) >= 20120405
#BuildRequires:  pkgconfig(libfcache) >= 20120405
#BuildRequires:  pkgconfig(libexe) >= 20120405

%description
libevt is a library and tools to access the Windows Event Log
(EVT) format.

For the Windows XML Event Log (EVTX) format, see libevtx.

%package tools
Summary: Utilities to export events from Windows Event Log files
License: LGPLv3+
Group: File tools

%description tools
Tools for reading Windows Event Log (EVT) files. These include
evtinfo and evtexport. See evtxtools for Windows XML Event Log (EVTX)
programs.

%package devel
Summary: Development files for libevt, a Windows event file parser
License: LGPLv3+ and GFDLv1.3+
Group: Development/C
Requires: %name = %version

%description devel
libevt is a library to access the Windows Event Log (EVT) format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-module-%name
Summary: Python bindings for libevt, a Windows event file parser
License: LGPLv3+
Group: Development/Python

%description -n python-module-%name
Python bindings for libevt, which can read Windows event files.

%prep
%setup
%patch1 -p1
cp -a "%SOURCE1" .

%build
%configure \
	--disable-static \
	--enable-wide-character-type \
	--enable-python
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README
%_libdir/libevt.so.*

%files tools
%_bindir/evt*
%_man1dir/evt*.1*

%files devel
%doc AUTHORS ChangeLog README Windows_Event_Log*.pdf
%_includedir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files -n python-module-%name
%doc AUTHORS ChangeLog README
%python_sitelibdir/pyevt.so

%changelog
* Thu Jan 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 20140411-alt2
- Applied security fix from upstream (Fixes CVE-2018-8754).

* Sun May 11 2014 Michael Shigorin <mike@altlinux.org> 20140411-alt1
- new version (watch file uupdate)

* Sun May 11 2014 Michael Shigorin <mike@altlinux.org> 20131013-alt1
- initial build for ALT Linux Sisyphus

* Thu Nov 14 2013 Greg.Freemyer@gmail.com
- update to 20131013
  * worked on setup.py, largely for MSI builds
  * updated dependencies
  * worked on libcthreads build support
- use libcthreads and libcfile from factory
* Wed Jul 31 2013 Greg.Freemyer@gmail.com
- update to 20130727
  * updated dependencies
  * pyevt
  - changed event identifier to an unsigned long
  - fixes fro >2G file objects in BFIO glue code
  * worked on tests
  * bug fix for wrapped event record
  * fixed codepage 1255 restriction
  * updates and bug fixes in pyevt
  * implemented libfdata support to improve handling of large EVT files
  * remove item flags
  * added support for truncated event record corruption scenario
  * fixed codepage 949 and 950 restriction
- change to gz compression to simplyfy download/convert
- use libyal factory packages if possible
* Wed Apr  3 2013 jengelh@inai.de
- Cleanups: Set RPM group, license, summary and description
  metadata; remove unused %%py_requires; do not bloat shlib package
  with documentation
- Use system libraries instead of bundled ones where possible
- Name the tools package according to upstream's recommendation
- Drop unnecessary -fno-strict-aliasing
* Wed Mar 27 2013 Greg.Freemyer@gmail.com
- initial package (version 20130319) for build.opensuse.org
