Name:           screenfetch
Version:        3.9.0
Release:        alt1
Summary:        A "Bash Screenshot Information Tool"

License:        GPLv3+
Group:		Monitoring
URL:            https://github.com/KittyKatt/screenFetch
Packager:       Andrey Cherepanov <cas@altlinux.org>

Source:		%name-%version.tar
Patch:		%name-%version.patch

Requires:	scrot

%filter_from_requires \,^\(/usr/bin/sw_vers\|/etc/portage/make.conf\)$,d

%description
This handy Bash script can be used to generate one of
those nifty terminal theme information + ASCII distribution
logos you see in everyone's screen-shots nowadays. It will
auto-detect your distribution and display an ASCII version
of that distribution's logo and some valuable information
to the right. There are options to specify no ASCII art,
colors, taking a screen-shot upon displaying info, and even
customizing the screen-shot command! This script is very easy
to add to and can easily be extended.

%prep
%setup -q
%patch -p1

%build

%install
install -Dm 0755 screenfetch-dev %buildroot%_bindir/%name
install -Dm 0644 screenfetch.1 %buildroot%_man1dir/%name.1

%files
%doc CHANGELOG README.mkdn TODO
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Fri Nov 08 2019 Andrey Cherepanov <cas@altlinux.org> 3.9.0-alt1
- New version.

* Tue Mar 14 2017 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version

* Wed Feb 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- Initial build in Sisyphus

