Name: cdemu-daemon
Version: 3.2.4
Release: alt1

Summary: CDEmu daemon
License: GPLv2+
Group: System/Servers

URL: http://cdemu.sourceforge.net
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://downloads.sourceforge.net/cdemu/%name-%version.tar.bz2 
Source1: vhba.init
Source2: vhba.service

BuildRequires: cmake
BuildRequires: glibc-kernheaders-generic
BuildRequires: intltool
BuildRequires: libao-devel >= 0.8.0
BuildRequires: libmirage-devel >= 3.2.0

%description
This is CDEmu daemon, the userspace daemon part of the userspace-cdemu suite, a 
free, GPL CD/DVD-ROM device emulator for linux.

It receives SCSI commands from kernel module and processes them, passing the 
requested data back to the kernel. Daemon implements the actual virtual device; 
one instance per each device registered by kernel module. It uses libMirage, an 
image access library that is part of userspace-cdemu suite, for the image access 
(e.g. sector reading).

The daemon registers itself on D-BUS' system or session bus (depending on the
options passed to it) where it exposes an interface that can be used by clients
to control it.

%prep
%setup -q

%build
%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
         -DCMAKE_INSTALL_PREFIX:PATH="%prefix" \
         -DCMAKE_INSTALL_LIBEXECDIR:PATH="%_libexecdir/%name" \
         -DCMAKE_C_FLAGS:STRING="%optflags" \
         -DCMAKE_BUILD_TYPE:STRING="Release"
         
popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__install -Dp -m0755 %SOURCE1 %buildroot%_initdir/vhba
%__install -Dp -m0644 %SOURCE2 %buildroot%_unitdir/vhba.service
%find_lang %name

%preun
%preun_service vhba
/sbin/service vhba condstop ||:

%post
%post_service vhba
/sbin/service vhba condrestart ||:

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name-session.sh
%_man8dir/%name.*
%dir %_datadir/dbus-1
%dir %_datadir/dbus-1/services
%_datadir/dbus-1/services/*.service
%_initdir/vhba
%dir /lib/systemd
%dir %_unitdir
%_unitdir/vhba.service

%changelog
* Mon Nov 02 2020 Nazarov Denis <nenderus@altlinux.org> 3.2.4-alt1
- Version 3.2.4

* Mon Jun 17 2019 Nazarov Denis <nenderus@altlinux.org> 3.2.2-alt1
- Version 3.2.2

* Sat Jan 26 2019 Nazarov Denis <nenderus@altlinux.org> 3.2.1-alt2
- Remove %ubt macro

* Fri Jul 27 2018 Nazarov Denis <nenderus@altlinux.org> 3.2.1-alt1%ubt
- Version 3.2.1

* Wed Aug 02 2017 Nazarov Denis <nenderus@altlinux.org> 3.1.0-alt1%ubt
- Version 3.1.0

* Thu Oct 13 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.5-alt1
- Version 3.0.5

* Mon Jan 11 2016 Nazarov Denis <nenderus@altlinux.org> 3.0.4-alt1
- Version 3.0.4

* Fri Oct 10 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.2-alt0.M70T.1
- Build for branch t7

* Tue Oct 07 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.2-alt1
- Version 3.0.2

* Thu Aug 07 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt0.M70T.1
- Build for branch t7

* Wed Aug 06 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.1-alt1
- Version 3.0.1

* Sun Jul 20 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt2.M70P.1
- Build for branch p7

* Sat Jul 19 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt2.M70T.1
- Build for branch t7

* Wed Jul 16 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt3
- Add vhba service file for systemd

* Tue Jul 15 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt2
- Add vhba init script
- Add LSB init header

* Fri Jul 04 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt0.M70T.1
- Build for branch t7

* Thu Jul 03 2014 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- Version 3.0.0

* Mon Feb 10 2014 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt0.M70P.1
- Build for branch p7

* Sun Feb 09 2014 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt0.M70T.1
- Build for branch t7

* Sat Sep 21 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Sun Jun 09 2013 Nazarov Denis <nenderus@altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Tue Dec 25 2012 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt2
- Fix build requires and libexec directory path

* Tue Dec 25 2012 Nazarov Denis <nenderus@altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Wed Jan 25 2012 Nazarov Denis <nenderus@altlinux.org> 1.5.0-alt1
- Version 1.5.0

* Tue Sep 20 2011 Nazarov Denis <nenderus@altlinux.org> 1.4.0-alt1
- Version 1.4.0

* Tue Jan 25 2011 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt2
- Add LSB init headers

* Fri Nov 19 2010 Nazarov Denis <nenderus@altlinux.org> 1.3.0-alt1
- Initial build for ALT Linux

* Sat Sep 18 2010 tuoma_mel@inbox.ru
- Updated to 1.3.0

* Mon Mar 29 2010 tuoma_mel@inbox.ru
- Updated to 1.2.0

* Sat Jun 28 2008 Rok Mandeljc <rok.mandeljc@email.si> - 1.1.0-1
- Updated to 1.1.0

* Thu Dec 20 2007 Rok Mandeljc <rok.mandeljc@email.si> - 1.0.0-1
- Initial RPM release.
