%define oname tslib
%define plugindir %_libdir/libts-1.0
%define sover 0
%define libts libts_0.0_%sover

Name: libts-compat
Version: 1.0
Release: alt2

Summary: tslib - touchscreen access library

Url: http://developer.berlios.de/projects/tslib/
License: GPL
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://download.berlios.de/tslib/%oname-%version.tar
Patch: tslib-glibc2.8.patch

# Automatically added by buildreq on Sun Jan 10 2010
BuildRequires: gcc-c++ glibc-devel

%description
Hardware independent touchscreen access library.

%package -n %libts
Group: System/Libraries
Summary: %name library
%description -n %libts
Hardware independent touchscreen access library.

%package devel
Summary: Development library and headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files (headers etc.) for %name.

%prep
%setup -n %oname-%version
%__subst 's,^# module_raw input$,module_raw input,' etc/ts.conf
# For quick verification during building:
grep "module_raw input" etc/ts.conf
%patch0 -p1

%build
./autogen.sh
%configure --with-plugindir=%plugindir
%make_build

%install
%makeinstall_std
rm -f %buildroot%plugindir/*.la

%files -n %libts
%doc README AUTHORS ChangeLog
%_libdir/libts-0.0.so.%sover
%_libdir/libts-0.0.so.*

%changelog
* Tue Oct 06 2020 Sergey V Turchin <zerg@altlinux.org> 1.0-alt2
- package only compat library

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jan 10 2010 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva)

* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-5mdv2010.0
+ Revision: 445562
- rebuild

* Sat Feb 28 2009 Anssi Hannula <anssi@mandriva.org> 1.0-4mdv2009.1
+ Revision: 346002
- fix build with glibc 2.8 (patch from debian)
- spec file cleaning

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 16 2007 Anssi Hannula <anssi@mandriva.org> 1.0-1mdv2008.0
+ Revision: 52350
- initial Mandriva Linux release based on .spec from Gary Greene
  <greeneg@tolharadys.net>

