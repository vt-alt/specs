Name: inxi
Version: 3.1.00
Release: alt1

Summary: A full featured system information script
Summary(ru): Скрипт вывода полной информации об оборудовании и системе

License: GPL-3.0-or-later
Group: Monitoring
URL: https://smxi.org
# Source-url: https://github.com/smxi/inxi/archive/%version-1.tar.gz
Source: %name-%version.tar.gz

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Requires: net-tools
Requires: pciutils
Requires: procps
Requires: lm_sensors
Requires: usbutils
Requires: hddtemp

AutoReq: no

%description
Inxi offers a wide range of built-in options, as well as a good number
of extra features which require having the script recommends installed
on the system.

%description -l ru
Inxi позволяет выводить различную информацию об используемом
оборудовании и о работе системы.

%prep
%setup -q
chmod -x %name.changelog
#Disable update option
sed -i "s/B_ALLOW_UPDATE='true'/B_ALLOW_UPDATE='false'/" inxi

%build

%install
install -p -D -m 755 %name %buildroot/%_bindir/%name
install -p -D -m 644 %name.1 %buildroot/%_man1dir/%name.1

%files
%doc %name.changelog
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat May 09 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.00-alt1
- New version (3.1.00)

* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 3.0.38-alt1
- New version (3.0.38)

* Wed Nov 20 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.37-alt1
- New version (3.0.37)

* Thu Aug 15 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.36-alt1
- New version (3.0.36)

* Tue Jul 16 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.35-alt1
- New version (3.0.35)

* Mon May 06 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.34-alt1
- New version (3.0.34)

* Mon Apr 01 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.33-alt1
- New version (3.0.33)

* Tue Feb 12 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.32-alt1
- New version (3.0.32)

* Thu Feb 07 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.31-alt1
- New version (3.0.31)

* Wed Jan 09 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.30-alt1
- New version

* Tue Dec 18 2018 Leontiy Volodin <lvol@altlinux.org> 3.0.29-alt1
- New version

* Fri Dec 07 2018 Leontiy Volodin <lvol@altlinux.org> 3.0.28-alt1
- New version

* Mon Oct 29 2018 Leontiy Volodin <lvol@altlinux.org> 3.0.27-alt1
- New version
- Change project URL

* Wed Oct 03 2018 Leontiy Volodin <lvol@altlinux.org> 3.0.26-alt1
- New version

* Tue Dec 13 2016 Mikhail Kolchin <mvk@altlinux.org> 2.3.5-alt1
- New version

* Fri Sep 16 2016 Mikhail Kolchin <mvk@altlinux.org> 2.3.1-alt1
- New version

* Wed Apr 27 2016 Mikhail Kolchin <mvk@altlinux.org> 2.3.0-alt1
- New version

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.33-alt1
- New version

* Sun Jan 17 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.32-alt1
- New version

* Tue Nov 24 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.31-alt1
- New version

* Sun Aug 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.28-alt1
- New version
- Build from upstream Git repository
- Change project URL

* Thu Jun 25 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.25-alt1.r2604
- New version

* Sat May 23 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.21-alt2
- New version

* Mon Apr 27 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.19-alt2
- Disable autoreq to prevent excess requirements

* Sun Apr 26 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.19-alt1
- Initial build for Sisyphus (thanks Fedora team for the spec)
