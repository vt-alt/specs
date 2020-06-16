%define git %nil
%define _libexecdir %_prefix/libexec
%def_enable obex
%def_enable btpclient
# since 5.44 the following tools marked as deprecated:
# hciattach hciconfig hcitool hcidump rfcomm sdptool ciptool gatttool
%def_enable deprecated

Name: bluez
Version: 5.54
Release: alt5

Summary: Bluetooth utilities
License: GPL-2.0-or-later
Group: Networking/Other

Url: http://www.bluez.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: L.A. Kostis <lakostis@altlinux.org>

# fc
Patch10: 0001-Allow-using-obexd-without-systemd-in-the-user-sessio.patch
Obsoletes: obex-data-server < 0.4.6-alt3
Conflicts: udev-extras < 169
Requires(post,preun): /bin/systemctl

BuildRequires: glib2-devel libudev-devel libdbus-devel libreadline-devel
BuildRequires: systemd-devel gtk-doc
%{?_enable_obex:BuildRequires: libical-devel libicu-devel}
%{?_enable_btpclient:BuildRequires: libell-devel >= 0.28}
# for check
BuildRequires: /proc

%description
Bluetooth protocol stack for Linux

%package -n lib%name
Summary: Libraries for use in Bluetooth applications
Group: System/Libraries
Obsoletes: lib%{name}4

%description -n lib%name
Libraries for use in Bluetooth applications

%package -n lib%name-devel
Summary: Development libraries for Bluetooth applications
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
lib%name-devel contains development libraries and headers for
use in Bluetooth applications

%package cups
Summary: CUPS printer backend for Bluetooth printers
Group: Networking/Other
Requires: %name = %version-%release

%description cups
This package contains the CUPS backend

%package btpclient
Summary: Tester protocol for Bluetooth stack client
Group: Networking/Other
Requires: %name = %version-%release

%description btpclient
BTP stands for Bluetooth Tester Protocol and aims at automated testing of BT
stack. BTP is binary protocol and is already implemented in Zephyr Project.

https://github.com/zephyrproject-rtos/zephyr/blob/master/tests/bluetooth/tester/btp_spec.txt

%prep
%setup
%patch -p1
%patch10 -p1

%build
%autoreconf
export CFLAGS="$CFLAGS %(getconf LFS_CFLAGS)"
%configure \
	--enable-library \
	--enable-threads \
	--enable-external-ell \
	%{subst_enable obex} \
	%{subst_enable btpclient} \
	--enable-cups \
	--enable-tools \
	--localstatedir=%_var \
	%{subst_enable deprecated}
%make_build

%install
%makeinstall_std
%{?_enable_deprecated:install -m755 attrib/gatttool %buildroot%_bindir/}
%{?_enable_btpclient:install -m755 tools/btpclient %buildroot%_bindir/}
install -m755 tools/bneptest %buildroot%_bindir/
install -pD -m755 scripts/bluetooth.alt.init %buildroot%_initdir/bluetoothd
ln -s bluetooth.service %buildroot%_unitdir/bluetoothd.service
mkdir -p %buildroot%_libdir/bluetooth/plugins %buildroot%_localstatedir/bluetooth
# configdir
mkdir -p %buildroot%_sysconfdir/bluetooth

find %buildroot%_libdir -name \*.la -delete

%check
%make check

%post
if [ $1 = 1 ]; then
%post_service bluetoothd
	chkconfig bluetoothd on
	/bin/systemctl --user --global preset obex.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 = 0 ]; then
%preun_service bluetoothd
	/bin/systemctl --user --global disable obex.service >/dev/null 2>&1 || :
fi

%triggerin -- %name < 5.54-alt5
/bin/systemctl --user --global preset obex.service >/dev/null 2>&1 || :

%files
%doc AUTHORS ChangeLog README
%dir %_sysconfdir/bluetooth
%_initdir/bluetoothd
%config %_sysconfdir/dbus-1/system.d/bluetooth.conf
%_unitdir/*.service
%_prefix/lib/systemd/user/obex.service
/lib/udev/rules.d/*-hid2hci.rules
/lib/udev/hid2hci
%_bindir/bccmd
%_bindir/bluemoon
%_bindir/bluetoothctl
%_bindir/btattach
%_bindir/btmon
%_bindir/hex2hcd
%_bindir/l2ping
%_bindir/l2test
%_bindir/mpris-proxy
%_bindir/rctest
%_bindir/bneptest

%if_enabled deprecated
%_bindir/ciptool
%_bindir/gatttool
%_bindir/hciattach
%_bindir/hciconfig
%_bindir/hcidump
%_bindir/hcitool
%_bindir/rfcomm
%_bindir/sdptool
%endif

%_libdir/bluetooth/
%_libexecdir/bluetooth/
%_datadir/dbus-1/system-services/org.bluez.service
%_datadir/dbus-1/services/org.bluez.obex.service
%_localstatedir/bluetooth
%_man1dir/*.1*
%_man8dir/*.8*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/bluetooth
%_libdir/*.so
%_pkgconfigdir/*.pc

%files cups
%_prefix/lib/cups/backend/bluetooth

%if_enabled btpclient
%files btpclient
%_bindir/btpclient
%endif

%changelog
* Tue Jun 09 2020 Yuri N. Sedunov <aris@altlinux.org> 5.54-alt5
- fixed %%post, %%preun scripts
- used LFS_CFLAGS

* Tue Jun 09 2020 Anton Midyukov <antohami@altlinux.org> 5.54-alt4
- Disable obex.service only when uninstalling package
- Install package bluez after installing systemd-utils
(not avoid systemd-utils dependency)
- Fix License tag

* Mon Apr 20 2020 Michael Shigorin <mike@altlinux.org> 5.54-alt3
- avoid systemd-utils dependency
- minor spec cleanup

* Mon Apr 20 2020 Anton Midyukov <antohami@altlinux.org> 5.54-alt2
- Enable obex.service (closes #38279).

* Sun Mar 15 2020 L.A. Kostis <lakostis@altlinux.ru> 5.54-alt1
- 5.54;
- remove merged patches;
- security fixes:
  + CVE-2020-0556 (closes #38220).

* Wed Sep 18 2019 L.A. Kostis <lakostis@altlinux.ru> 5.50-alt1.2
- Added patch:
  + 0001-policy-Add-logic-to-connect-a-Sink.patch (fixing issue when a2dp wasn't
    selected properly)

* Mon Sep 16 2019 L.A. Kostis <lakostis@altlinux.ru> 5.50-alt1.1
- Remove conflicting obsoletes with bluez-alsa.
- Added patch:
  + 0001-tools-Fix-build-after-y2038-changes-in-glibc.patch

* Fri Jun 22 2018 L.A. Kostis <lakostis@altlinux.ru> 5.50-alt1
- 5.50.

* Sat Mar 31 2018 L.A. Kostis <lakostis@altlinux.ru> 5.49-alt1
- 5.49.
- Enable btpclient (and new dependency to libell).

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 5.48-alt2
- rebuilt against libical.so.3

* Sun Dec 31 2017 L.A. Kostis <lakostis@altlinux.ru> 5.48-alt1
- 5.48.

* Fri Sep 08 2017 L.A. Kostis <lakostis@altlinux.ru> 5.46-alt1.2
- Added bneptest (might be useful to debug BNEP issues).

* Wed Aug 30 2017 L.A. Kostis <lakostis@altlinux.ru> 5.46-alt1.1
- unit tests: disable gatt test (doesn't work in VM).

* Mon Aug 28 2017 L.A. Kostis <lakostis@altlinux.ru> 5.46-alt1
- 5.46.
- Added patches from GIT master:
  + core: Fallback to LE if BR/EDR connection fails with EHOSTDOWN.
  + gatt: Fix crash when cleanup notify_io.
  + plugins: Fix reconnect_interval for cases of improper main.conf.
  + hciattach: fix the delay timer for bcm43xx firmware download.
  + gatt: Don't return to AcquireNotify until it has completed.
  + core/advertisement: Add specifc error if max instance is reached.
  + shared/gatt-db: Fix memory comparison error.

* Fri Jul 07 2017 L.A. Kostis <lakostis@altlinux.ru> 5.46-alt0.c896183.1
- Added patches:
  + device: Fix crashing when connecting ATT over BR/EDR
    (kbo#195221 ALT#33623)

* Thu Jul 06 2017 L.A. Kostis <lakostis@altlinux.ru> 5.46-alt0.c896183
- GIT snapshot c896183.

* Sun Jun 25 2017 Yuri N. Sedunov <aris@altlinux.org> 5.45-alt1.1
- buildreqs /proc for check

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 5.45-alt1
- 5.45

* Fri Mar 03 2017 Yuri N. Sedunov <aris@altlinux.org> 5.44-alt1
- 5.44

* Sun Oct 30 2016 Yuri N. Sedunov <aris@altlinux.org> 5.43-alt1
- 5.43

* Sat Oct 15 2016 Yuri N. Sedunov <aris@altlinux.org> 5.42-alt1
- 5.42

* Sun Jul 24 2016 Yuri N. Sedunov <aris@altlinux.org> 5.41-alt1
- 5.41

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 5.40-alt1
- 5.40

* Wed Apr 06 2016 Yuri N. Sedunov <aris@altlinux.org> 5.39-alt1
- 5.39

* Fri Mar 18 2016 Yuri N. Sedunov <aris@altlinux.org> 5.38-alt1
- 5.38

* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 5.37-alt2
- rebuilt against libical.so.2

* Tue Dec 29 2015 Yuri N. Sedunov <aris@altlinux.org> 5.37-alt1
- 5.37

* Fri Oct 30 2015 Yuri N. Sedunov <aris@altlinux.org> 5.36-alt1
- 5.36
- probably fixed problem with daemon under sysv init (ALT #30562)
- removed bluez-5.35-alt-duplicate_test_case_path.patch (fixed by upstream)

* Thu Oct 01 2015 Yuri N. Sedunov <aris@altlinux.org> 5.35-alt1
- 5.35

* Fri Sep 04 2015 Yuri N. Sedunov <aris@altlinux.org> 5.34-alt1
- 5.34

* Mon Aug 03 2015 Yuri N. Sedunov <aris@altlinux.org> 5.33-alt1
- 5.33

* Sat Jul 11 2015 Yuri N. Sedunov <aris@altlinux.org> 5.32-alt1
- 5.32

* Mon Jun 29 2015 Yuri N. Sedunov <aris@altlinux.org> 5.31-alt2
- removed obsolete /etc/modprobe.d/bluetooth.conf

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 5.31-alt1
- 5.31

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 5.30-alt2
- install gatttool (ALT #30942)

* Wed Apr 01 2015 Yuri N. Sedunov <aris@altlinux.org> 5.30-alt1
- 5.30

* Thu Mar 12 2015 Yuri N. Sedunov <aris@altlinux.org> 5.29-alt1
- 5.29

* Mon Feb 02 2015 Yuri N. Sedunov <aris@altlinux.org> 5.28-alt1
- 5.28

* Sat Dec 27 2014 Yuri N. Sedunov <aris@altlinux.org> 5.27-alt1
- 5.27
- enabled OBEX profile support
- applied fc patch to allow using obexd without systemd in the user session,
  probably fixed and ALT #30565

* Sun Dec 14 2014 Yuri N. Sedunov <aris@altlinux.org> 5.26-alt1
- 5.26

* Fri Dec 05 2014 Yuri N. Sedunov <aris@altlinux.org> 5.25-alt1
- 5.25

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 5.14-alt1
- 5.14

* Tue Nov 26 2013 Valery Inozemtsev <shrek@altlinux.ru> 5.11-alt1
- 5.11

* Thu Feb 14 2013 Valery Inozemtsev <shrek@altlinux.ru> 5.2-alt1
- 5.2

* Tue Dec 25 2012 Valery Inozemtsev <shrek@altlinux.ru> 5.0-alt1
- 5.0

* Wed Jun 27 2012 Valery Inozemtsev <shrek@altlinux.ru> 4.101-alt1
- 4.101

* Fri Jun 15 2012 Valery Inozemtsev <shrek@altlinux.ru> 4.100-alt1
- 4.100

* Wed Mar 07 2012 Valery Inozemtsev <shrek@altlinux.ru> 4.99-alt1
- 4.99

* Mon Jan 16 2012 Valery Inozemtsev <shrek@altlinux.ru> 4.98-alt1
- 4.98

* Sat Dec 24 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.97-alt1
- 4.97

* Mon Aug 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.96-alt1
- 4.96

* Tue Jul 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.95-alt1
- 4.95

* Tue May 31 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.94-alt1
- 4.94

* Thu May 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.93-alt2
- hid2hci: moved from udev-extras package

* Wed May 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.93-alt1
- 4.93
- add systemd service files (closes: #25563)

* Tue Apr 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.92-alt1
- 4.92

* Wed Mar 30 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.91-alt1
- 4.91

* Wed Mar 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.90-alt1
- 4.90

* Wed Feb 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.89-alt1
- 4.89
- libbluez: added obsoletes libbluez4 (closes: #24780)

* Tue Feb 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.88-alt1
- 4.88

* Wed Jan 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.87-alt1
- 4.87

* Sat Jan 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.86-alt1
- 4.86

* Thu Jan 13 2011 Valery Inozemtsev <shrek@altlinux.ru> 4.85-alt1
- 4.85

* Wed Dec 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.84-alt1
- 4.84

* Sun Dec 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.82-alt1
- 4.82

* Wed Dec 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.81-alt1
- 4.81
- disabled gstreamer plugin

* Mon Nov 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.80-alt1
- 4.80

* Mon Nov 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.79-alt1
- 4.79

* Sat Nov 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.78-alt1
- 4.78

* Wed Oct 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.77-alt1
- 4.77

* Fri Oct 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.76-alt1
- 4.76

* Tue Oct 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.75-alt1
- 4.75

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.73-alt1
- 4.73

* Fri Sep 24 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.72-alt1
- 4.72

* Thu Sep 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.71-alt1
- 4.71

* Thu Aug 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.70-alt1
- 4.70

* Sun Jul 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.69-alt1
- 4.69

* Sat Jul 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.67-alt1
- 4.67

* Sun Jun 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.66-alt1
- 4.66

* Sun May 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.65-alt2
- removed HAL plugin

* Thu May 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.65-alt1
- 4.65

* Fri Apr 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.64-alt1
- 4.64

* Sat Mar 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.63-alt1
- 4.63

* Mon Mar 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.62-alt1
- 4.62

* Sat Feb 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.61-alt1
- 4.61

* Sun Jan 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 4.60-alt1
- 4.60

* Sat Dec 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.59-alt1
- 4.59

* Mon Nov 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.58-alt1
- 4.58

* Fri Nov 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.57-alt2
- renamed libbluez4 to libbluez

* Sat Oct 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.57-alt1
- 4.57

* Sun Oct 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.56-alt1
- 4.56

* Sun Oct 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.55-alt1
- 4.55

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.54-alt1
- 4.54

* Sat Sep 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.53-alt2
- 4.53-9cec7f

* Fri Sep 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.53-alt1
- 4.53

* Tue Sep 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.52-alt2
- 4.52-30b4f3

* Fri Sep 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.52-alt1
- 4.52

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.50-alt1
- 4.50

* Mon Aug 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.49-alt1
- 4.49

* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.48-alt1
- 4.48

* Sun Aug 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.47-alt2
- removed hid2hci, requires udev-extras >= 145

* Sun Aug 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.47-alt1
- 4.47

* Sat Aug 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.46-alt2
- used limited discoverable mode only when 0 < discov_timeout <= 60

* Sun Jul 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.46-alt1
- 4.46

* Wed Jul 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.45-alt1
- 4.45

* Tue Jul 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.44-alt1
- 4.44

* Fri Jul 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.43-alt1
- 4.43

* Mon Jun 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.42-alt1
- 4.42

* Sun Jun 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.41-alt1
- 4.41

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.40-alt2
- hid2hci run from udev

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.40-alt1
- 4.40

* Tue May 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.39-alt1
- 4.39

* Mon May 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.38-alt1
- 4.38

* Wed Apr 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.37-alt3
- condrestart does nothing

* Sun Apr 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.37-alt2
- enable service bluetoothd by default (closes: #19771)

* Thu Apr 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.37-alt1
- 4.37

* Sat Apr 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.36-alt3
- bluetoothd start after haldaemon

* Fri Apr 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.36-alt2
- enabled netlink

* Fri Apr 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.36-alt1
- 4.36

* Sun Apr 12 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.35-alt1
- 4.35

* Tue Apr 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.34-alt1
- 4.34

* Mon Mar 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.33-alt1
- 4.33

* Tue Mar 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.32-alt1
- 4.32

* Thu Feb 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.31-alt1
- 4.31

* Fri Feb 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.30-alt1
- 4.30

* Sun Feb 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.29-alt1
- 4.29

* Mon Feb 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.28-alt1
- 4.28

* Sat Jan 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 4.27-alt1
- 4.27
- renamed to bluez

* Sat Jan 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 3.36-alt3
- dropped tests
- dropped .service dbus file
- fixed init scripts
- fixed udev rules
- fixed dbus config

* Tue Oct 14 2008 Alexey Shabalin <shaba@altlinux.ru> 3.36-alt2
- use standart path for alsa library(#17555)
- drop buildrequires on libpulse-devel

* Mon Aug 04 2008 Alexey Shabalin <shaba@altlinux.ru> 3.36-alt1
- 3.36
- fix build with netlink (change buildreq libnetlink-devel to libnl-devel)

* Mon Jul 07 2008 Alexey Shabalin <shaba@altlinux.ru> 3.35-alt2
- install /etc/sysconfig/bluetooth from SOURCE2
- add parameter HID2HCI_UNDO to conf and init
- add a .service dbus file
- build with enabled network, serial, input, audio
- install audio.conf and network.conf
- rename udev rules to 81-bluetooth-pcmcia.rules
- add udev rules 80-bluetooth.rules from udev-rules package
- split packages alsa, gstreamer

* Mon Jul 07 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.35-alt1
- 3.35

* Wed Jun 25 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.34-alt1
- 3.34

* Sat Jun 21 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.33-alt1
- 3.33

* Tue May 27 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.32-alt1
- 3.32

* Fri May 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.31-alt1
- 3.31
- restore setserial support
- link bluetoothctl -> initscript, not vice versa (ldv@)

* Fri Apr 04 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.30-alt1
- 3.30
- disable setserial in /lib/udev/bluetooth_serial

* Sat Mar 22 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.29-alt1
- 3.29
- package dbus docs

* Thu Mar 06 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.28-alt1
- 3.28

* Sun Feb 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.26-alt1
- 3.26

* Sat Feb 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.25-alt1
- 3.25

* Thu Jan 31 2008 Andrey Rahmatullin <wrar@altlinux.ru> 3.24-alt1.1
- rebuild

* Wed Dec 26 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.24-alt1
- 3.24

* Tue Dec 11 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.23-alt1
- 3.23

* Fri Oct 26 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.22-alt1
- 3.22
- update buildreqs
- update License:

* Fri Oct 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.20-alt1
- 3.20

* Sun Sep 16 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.19-alt1
- 3.19

* Sat Sep 08 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.18-alt1
- 3.18

* Thu May 24 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.11-alt1
- 3.11
- remove l2test and rctest from the main package, add Conflicts (#11815)

* Tue May 15 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.10-alt2
- increase dbus find time to 5 min
- do not build sdpd
- fix apitest for new python-modules-dbus (SuSE)

* Fri May 11 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.10-alt1
- 3.10
- spec cleanup
- fix dev files location (shrek, #11567)
- enable Major Service Class: Telephony in default CoD (Guest007)
- disable discoverable mode timeout (#11676)

* Wed Feb 14 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.9-alt2
- enable rfcomm by default (#10825)
- initscript:
  + enable sdpd support in hcid if sdpd daemon is disabled
  + check whether hcid and sdpd are enabled when stopping them
  + remove `killall rfcommd' and `rmmod' calls
  + package as %%_sbindir/bluetoothctl, leaving symlink in %%_initdir
    (#10726)

* Fri Feb 09 2007 Andrey Rahmatullin <wrar@altlinux.ru> 3.9-alt1
- 3.9
- hcid on start now retries to find dbus for 1 minute after start
  (patch from Daniel Gollub, SuSE)
- hcid.conf:
  + change default device class to 104 (Desktop)
  + add comment about device class numbers (from SuSE)
- package test utils separately, add missing obsoletes/provides
  for bluez-hciemu
- remove alsa subpackage
- install cups backend to prefix/lib even on x86_64 (#10762)

* Wed Dec 27 2006 Andrey Rahmatullin <wrar@altlinux.ru> 3.8-alt1
- 3.8
- remove wildcards from %%files
- enable _unpackaged_files_terminate_build
- remove --enable-all, explicitly enable what is needed
- disable FUSE "support"
- enable PIE linking
- sync module aliases with Debian (remove old lines, add hidp)
- add Requires: dbus
- add Requires: libbluez >= %%version

* Tue Nov 07 2006 Andrey Rahmatullin <wrar@altlinux.ru> 3.7-alt1
- 3.7
- spec cleanup
- remove kernel-headers-std26-up from buildreqs
- fix statedir path and package it (#8885)
- set default PIN to "1234" (Debian)
- set default device ident string to "%%h-%%d" (Debian)
- install passkey-agent (#10176)
- add patch from http://kmobiletools.org/node/228 for compatibility
  with old helpers

* Wed Aug 23 2006 Grigory Milev <week@altlinux.ru> 3.3-alt1
- new version released
- removed bluepin
- removed package pcmcia
- added D-Bus support
- added udev support

* Tue Feb 21 2006 Grigory Milev <week@altlinux.ru> 2.25-alt1
- new version released (Read ChangeLog in doc dir)

* Mon Aug 22 2005 Grigory Milev <week@altlinux.ru> 2.19-alt1
- new version released
- added cups and alsa support

* Thu Apr 14 2005 Grigory Milev <week@altlinux.ru> 2.15-alt4
- return unpackage file hcitool

* Thu Mar 17 2005 Grigory Milev <week@altlinux.ru> 2.15-alt3
- move misc tool to separate package

* Tue Mar 15 2005 Grigory Milev <week@altlinux.ru> 2.15-alt2
- Fix build requires

* Mon Mar 14 2005 Grigory Milev <week@altlinux.ru> 2.15-alt1
- new version released

* Mon Mar 14 2005 Grigory Milev <week@altlinux.ru> 2.13-alt3
- remove requires to python

* Wed Jan 12 2005 Grigory Milev <week@altlinux.ru> 2.13-alt2
- fixed build requires

* Tue Jan 11 2005 Grigory Milev <week@altlinux.ru> 2.13-alt1
- new version released
- turn off HIDD_ENABLE on default config

* Tue Nov  2 2004 Grigory Milev <week@altlinux.ru> 2.10-alt2
- Start bluez utils after hotplug

* Thu Sep 23 2004 Grigory Milev <week@altlinux.ru> 2.10-alt1
- new version released

* Wed Jul 14 2004 Grigory Milev <week@altlinux.ru> 2.7-alt3
- fixed startup script for work with chkconfig

* Mon Jun 28 2004 Grigory Milev <week@altlinux.ru> 2.7-alt2
- fix requires

* Mon Jun 21 2004 Grigory Milev <week@altlinux.ru> 2.7-alt1
- fixating init script (not all)
- bluez-sdp orphaned, currently moved to bluez-utils
- new version released

* Thu Jun  3 2004 Grigory Milev <week@altlinux.ru> 2.4-alt2
- rebuild with new python

* Tue Feb 24 2004 Grigory Milev <week@altlinux.ru> 2.4-alt1
- new version released
- move pcmcia scripts to separate package
- fix bluepin script

* Tue Oct 14 2003 Grigory Milev <week@altlinux.ru> 2.3-alt1
- new version released
- fix initscript for start/stop daemon support
- add modutils configuration

* Mon Mar 31 2003 Grigory Milev <week@altlinux.ru> 2.2-alt2
- move /dev/vhci to package MAKEDEV

* Tue Feb 18 2003 Grigory Milev <week@altlinux.ru> 2.2-alt1
- new version released

* Fri Dec 20 2002 Grigory Milev <week@altlinux.ru> 2.1-alt1
- Initial build.
