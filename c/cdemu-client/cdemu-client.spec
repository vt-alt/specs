Name: cdemu-client
Version: 3.2.4
Release: alt1

Summary: A simple command-line client to control CDEmu daemon
License: GPLv2+
Group: File tools

URL: http://cdemu.sourceforge.net
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source: http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2

BuildRequires: cmake
BuildRequires: intltool
BuildRequires: rpm-build-gir

Requires: cdemu-daemon >= 3.2.2

%description
This is cdemu-client, a simple command-line client for controlling CDEmu daemon.
It is part of the userspace-cdemu suite, a free, GPL CD/DVD-ROM device emulator 
for linux.

It provides a way to perform the key tasks related to controlling the CDEmu
daemon, such as loading and unloading devices, displaying devices' status and
retrieving/setting devices' debug masks.

%prep
%setup

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
         -DCMAKE_INSTALL_PREFIX:PATH="%prefix" \
         -DCMAKE_BUILD_TYPE:STRING="Release"
         
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%find_lang cdemu

%files -f cdemu.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/cdemu
%_desktopdir/%name.desktop
%_man1dir/cdemu.*
%_pixmapsdir/%name.svg
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/cdemu

%changelog
* Mon Nov 02 2020 Nazarov Denis <nenderus@altlinux.org> 3.2.4-alt1
- Version 3.2.4

* Mon Jun 17 2019 Nazarov Denis <nenderus@altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Sat Jan 26 2019 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt2
- Remove %ubt macro

* Fri Jul 27 2018 Nazarov Denis <nenderus@altlinux.org> 3.2.0-alt1%ubt
- Version 3.2.0

* Wed Aug 02 2017 Nazarov Denis <nenderus@altlinux.org> 3.1.0-alt1%ubt
- Version 3.1.0

* Thu Oct 13 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.4-alt1
- Version 3.0.4

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Sun Jul 20 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt0.M70P.1
- Build for branch p7

* Fri Jul 04 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt0.M70T.1
- Build for branch t7

* Thu Jul 03 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- Version 3.0.0

* Mon Feb 10 2014 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt1.M70P.1
- Build for branch p7

* Sun Feb 09 2014 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt1.M70T.1
- Build for branch t7

* Tue Oct 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt2
- Use find-lang for language files

* Sat Sep 21 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Sun Jun 09 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Tue Dec 25 2012 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Wed Jan 25 2012 Nazarov Denis <nenderus@altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt1.1
- Rebuild with Python-2.7

* Tue Sep 20 2011 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Jan 25 2011 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt3
- Add lang files after install 

* Tue Nov 23 2010 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt2
- Fix build architecture

* Fri Nov 19 2010 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.1
- Rebuilt with python 2.6

* Fri Nov 14 2008 Nick S. Grechukh <gns@altlinux.org> 1.1.0-alt1
- first build for ALT Linux

* Sat Jun 28 2008 Rok Mandeljc <rok.mandeljc@email.si> - 1.1.0-1
- Updated to 1.1.0

* Thu Dec 20 2007 Rok Mandeljc <rok.mandeljc@email.si> - 1.0.0-1
- Initial RPM release.
