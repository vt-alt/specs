Name:    usb-modeswitch-data
Version: 20191128
Release: alt1

Summary: Data and udev-rules for usb-modeswitch
License: GPL-2.0-or-later

%define _udevdir 	/lib/udev
%define bname 		usb-modeswitch

Group:   System/Configuration/Hardware
Url:     http://www.draisberghof.de/usb_modeswitch/

Source: %name-%version.tar

BuildArch: noarch
Requires: usb-modeswitch >= 2.4.0
Epoch: 1

%description
Data and udev-rules for usb-modeswitch

%define modeswitch_rulesdir %_datadir/usb_modeswitch

%prep
%setup -n %name-%version

%install
%makeinstall_std

%files
%doc ChangeLog README
%modeswitch_rulesdir
%_udevdir/rules.d/40-usb_modeswitch.rules


%changelog
* Mon Feb 10 2020 Sergey Y. Afonin <asy@altlinux.org> 1:20191128-alt1
- New version (ALT #33492)
- used date as %%version again
- updated License tag to SPDX syntax

* Wed May 04 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1:2.3.0-alt1
- Version 20160112

* Thu Nov 05 2015 Andrey Cherepanov <cas@altlinux.org> 20151101-alt1
- New version (ALT #30058)

* Wed Jan 14 2015 Andrey Cherepanov <cas@altlinux.org> 20140529-alt2
- Add support of Huawei 3272

* Wed Nov 05 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20140529-alt1
- 20140529

* Wed Jan 15 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20131113-alt1
- 20131113

* Fri Nov 16 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20121109-alt1
- 20121109
- huawei-E171 patch removed (merged in upstream)

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 20120815-alt1
- 20120815

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 20120531-alt3
- huawei-E171 added

* Mon Oct 22 2012 Lenar Shakirov <snejok@altlinux.ru> 20120531-alt2
- minimum required version changed to 1.2.2 by upstream

* Thu Aug 09 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20120531-alt1
- 2012-05-31

* Tue Jul 12 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110619-alt2
- added "change" event processing (manowar@)

* Fri Jul 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110619-alt1
- Upstream 2011-06-19 by manowar@

* Mon Feb 21 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101222-alt1
- updated from upstream

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101202-alt1
- updated from upstream
- versioned requires

* Fri Sep 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100826-alt1
- first build

