Name: livecd-setlocale
Version: 0.3.9
Release: alt1

Summary: Automatically set locale from /proc/cmdline
License: GPLv2+
Group: System/Configuration/Other

Source0: %name.tar
BuildArch: noarch
# NB: alterator-sysconfig's kbd data is required
Requires: service chkconfig alterator-sysconfig

%description
Service to automatically set locale from /proc/cmdline
(when specified as e.g. lang=ru_RU).

%prep
%setup -c

%install
mkdir -p %buildroot%_initdir/
install -pDm755 {livecd-setlocale,%buildroot%_initdir}/livecd-setlocale
install -pDm644 {livecd-setlocale,%buildroot%_unitdir}/livecd-setlocale.service

%preun
# would be an inconvenient %%ghost
rm -f %_sysconfdir/profile.d/00dconf-kbd.sh
%preun_service %name

%files 
%_initdir/livecd-setlocale
%_unitdir/livecd-setlocale.service

%changelog
* Fri Dec 11 2020 Anton Midyukov <antohami@altlinux.org> 0.3.9-alt1
- set ctrl+shift for switch keyboard layout for be_BY, tt_RU, uk_UA locale
- Fix License Tag

* Sun Mar 29 2020 Anton Midyukov <antohami@altlinux.org> 0.3.8-alt1
- set alt+shift for switch keyboard layout

* Thu May 12 2016 Michael Shigorin <mike@altlinux.org> 0.3.7-alt1
- drop generated hook when uninstalling (closes: #32040)

* Wed Jul 02 2014 Michael Shigorin <mike@altlinux.org> 0.3.6-alt1
- tweaked unit file deps (thx shaba@)

* Thu Mar 06 2014 Michael Shigorin <mike@altlinux.org> 0.3.5-alt1
- fix unit file deps (broke with systemd-210)

* Wed Nov 13 2013 Michael Shigorin <mike@altlinux.org> 0.3.4-alt1
- ...cinnamon 1.x too...

* Tue Oct 01 2013 Michael Shigorin <mike@altlinux.org> 0.3.3-alt1
- handle cinnamon too

* Wed Sep 18 2013 Michael Shigorin <mike@altlinux.org> 0.3.2-alt1
- regexp thinko fix

* Wed Sep 18 2013 Michael Shigorin <mike@altlinux.org> 0.3.1-alt2
- (closes: #28991)

* Tue Sep 17 2013 Michael Shigorin <mike@altlinux.org> 0.3.1-alt1
- rough localectl support

* Mon Sep 16 2013 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- fixed service file dependencies
- added rudimentary gnome3 support (lacks XKB variants though)

* Wed Apr 17 2013 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- Use preun_service.

* Fri Dec 21 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2.0-alt1
- service file added

* Wed Apr 18 2012 Michael Shigorin <mike@altlinux.org> 0.1.1-alt1
- don't require indexhtml-common (but use it if available)
- added ru_UA special handling
- start in runlevels 3/4/5
- cleanups

* Sun Feb 19 2012 Radik Usupov <radik@altlinux.org> 0.1-alt9
- Added hook to langmap from tt_RU

* Wed Feb 15 2012 Andrey Cherepanov <cas@altlinux.org> 0.1-alt8
- Set Russian as fallback language for tt_RU (closes: #26931)

* Fri Sep 30 2011 Andrey Cherepanov <cas@altlinux.org> 0.1-alt7
- Set correct language for default indexhtml

* Wed Jan 12 2011 Andrey Cherepanov <cas@altlinux.org> 0.1-alt6
- completely rewrite startup script without alterator-cmdline call

* Mon May 25 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt5
- Don't anything at runlevel change

* Mon Feb 23 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt4
- change syntax to call new alterator backends

* Wed Nov 07 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- alterator-syskbd changed to alterator-sysconfig

* Fri Jun 29 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- added keyboard setting

* Thu May 31 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build
