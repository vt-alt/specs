Name: livecd-webkiosk
Version: 0.6.1
Release: alt2

Summary: start the browser for a suitable webkiosk environment
License: Public domain
Group: System/X11

Url: http://en.altlinux.org/starterkits
Packager: Michael Shigorin <mike@altlinux.org>

Requires: ratpoison xinit libshell
ExcludeArch: ppc64le armh aarch64

%define skeldir %_sysconfdir/skel
%define ifacedir %_sysconfdir/net/ifaces/eth0
%define xsfile %skeldir/.xsession
%define wrapper %_bindir/webkiosk-browser

%description
%summary
(livecd specific; also employs some ratpoison)

%package seamonkey
Summary: seamonkey webkiosk setup
Group: System/X11
Requires: %name = %version-%release
Requires: seamonkey

%description seamonkey
%summary
(the browser == seamonkey)

%package firefox
Summary: firefox webkiosk setup
Group: System/X11
Requires: %name = %version-%release
Requires: livecd-firefox firefox-r-kiosk

%description firefox
%summary
(the browser == firefox)

#ifarch x86_64
%package chromium
Summary: chromium webkiosk setup
Group: System/X11
Requires: %name = %version-%release
Requires: chromium

%description chromium
%summary
(the browser == chromium)
#endif

%package falkon
Summary: falkon webkiosk setup
Group: System/X11
Requires: %name = %version-%release
Requires: falkon

%description falkon
%summary
(the browser == falkon)

%prep

%build

%install
mkdir -p %buildroot{%skeldir,%ifacedir}

cat > %buildroot%xsfile << _EOF_
#!/bin/sh

ratpoison &

. shell-cmdline

read cmdline < /proc/cmdline
cmdline_get url url
[ -z "\$url" -a -f /image/index.html ] && url=/image/index.html

while :; do
	xset s off; xset -dpms
	webkiosk-browser \$url
done
_EOF_
chmod +x %buildroot%xsfile

cat > %buildroot%skeldir/.ratpoisonrc << _EOF_
startup_message off
set border 0
set padding 0 0 0 0
set barpadding 0 0
escape F25
banish
_EOF_

cat > %buildroot%ifacedir/options << _EOF_
BOOTPROTO=dhcp
_EOF_

%post seamonkey
cat > %wrapper << _EOF_
#!/bin/sh
exec seamonkey -chrome "\$@"
_EOF_
chmod +x %wrapper

%post firefox
cat > %wrapper << _EOF_
#!/bin/sh
exec firefox "\$@"
_EOF_
chmod +x %wrapper

#ifarch x86_64
%post chromium
cat > %wrapper << _EOF_
#!/bin/sh
exec chromium --kiosk --start-maximized --disable-translate --no-first-run "\$@"
_EOF_
chmod +x %wrapper
#endif

%post falkon
cat > %wrapper << _EOF_
#!/bin/sh
exec falkon --fullscreen "\$@"
_EOF_
chmod +x %wrapper

%files
%skeldir/.ratpoisonrc
%ifacedir/options
%xsfile

%files firefox

%ifarch %ix86 x86_64 aarch64
%files seamonkey
#ifarch x86_64
%files chromium
#endif
%files falkon
%endif

%changelog
* Mon Nov 30 2020 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt2
- ExcludeArch: ppc64le armh aarch64 (as for firefox and seamonkey).

* Fri Sep 13 2019 Leonid Krivoshein <klark@altlinux.org> 0.6.1-alt1
- fixed typo in the spec: url from cmdline now realy used

* Wed Sep 12 2018 Michael Shigorin <mike@altlinux.org> 0.6.0-alt1
- replaced qupzilla with falkon following upstream decision
- made all but firefox subpackages x86/aarch64-only

* Wed Jun 22 2016 Michael Shigorin <mike@altlinux.org> 0.5.0-alt1
- added "url" kernel boot parameter support

* Wed Oct 14 2015 Michael Shigorin <mike@altlinux.org> 0.4.3-alt3
- the whole livecd-webkiosk source package should be made noarch

* Wed Oct 14 2015 Michael Shigorin <mike@altlinux.org> 0.4.3-alt2
- reenabled non-x86_64 build for chromium subpackage
  (and actually made it noarch)

* Tue Sep 08 2015 Michael Shigorin <mike@altlinux.org> 0.4.3-alt1
- tweaked chromium options as its kiosk doesn't mute "first run"

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 0.4.2-alt5
- reenabled noarch for non-chromium subpackages

* Mon Sep 07 2015 Michael Shigorin <mike@altlinux.org> 0.4.2-alt4
- s/firefox-fullscreen-kiosk/firefox-r-kiosk/

* Fri Jun 19 2015 Michael Shigorin <mike@altlinux.org> 0.4.2-alt3
- there are 32-bit capable browsers out there still :)

* Thu Jun 18 2015 Andrey Cherepanov <cas@altlinux.org> 0.4.2-alt2
- rebuild without 32-bit support

* Wed Dec 31 2014 Michael Shigorin <mike@altlinux.org> 0.4.2-alt1
- disable DPMS (thanks valintinr@)

* Mon Sep 29 2014 Michael Shigorin <mike@altlinux.org> 0.4.1-alt1
- require qupzilla 1.8.0 or later for --fullscreen

* Sat Sep 27 2014 Michael Shigorin <mike@altlinux.org> 0.4-alt1
- added qupzilla support

* Sat Sep 13 2014 Michael Shigorin <mike@altlinux.org> 0.3-alt1
- added seamonkey support

* Fri Jun 07 2013 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- rebuilt

* Sun Dec 23 2012 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- introduced chromium support (as a separate subpackage)
- NB: firefox support moved to a subpackage as well,
  please pay attention if you're upgrading live images

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- moved firefox prefs.js handling to livecd-firefox package

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- disable firefox' default browser check

* Tue Jan 24 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

