Name: zorin-icon-themes
Version: 2.8.5
Release: alt1
Summary: Zorin icon themes

License: CC-BY-SA-4.0
Group: Graphical desktop/GNOME
URL: https://github.com/ZorinOS/zorin-icon-themes

Source: %name-%version.tar

BuildArch: noarch
AutoReqProv: no

%description
The Zorin icon theme provided in a variety of color combinations.

%define themes Zorin ZorinBlue-Dark ZorinBlue-Light ZorinGreen-Dark ZorinGreen-Light ZorinGrey-Dark ZorinGrey-Light ZorinOrange-Dark ZorinOrange-Light ZorinPurple-Dark ZorinPurple-Light ZorinRed-Dark ZorinRed-Light

%{expand:%(\
    for theme in %{themes}; do \
        echo -e "%%package -n icon-theme-$theme";\
        echo -e "Summary: $theme icon theme\nGroup: Graphical desktop/GNOME\n";\
        echo -e "%%description -n icon-theme-$theme\n$theme icon theme.\n";\
        echo -e "%%files -n icon-theme-$theme\n%%_iconsdir/$theme/\n";\
    done\
)}

%prep
%setup
# Remove bad symlinks
find . -name mintwelcome.png -delete

%install
mkdir -p %buildroot%_iconsdir
cp -a Zorin* %buildroot%_iconsdir

%changelog
* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.5-alt1
- New version.

* Sat Jun 19 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.4-alt1
- New version.

* Wed May 05 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.3-alt1
- New version.

* Mon May 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.2-alt1
- New version.

* Thu Apr 29 2021 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- New version.

* Sun Apr 18 2021 Andrey Cherepanov <cas@altlinux.org> 2.7.9-alt1
- New version.

* Mon Apr 13 2020 Andrey Cherepanov <cas@altlinux.org> 2.4.5-alt1
- New version.

* Wed Apr 01 2020 Andrey Cherepanov <cas@altlinux.org> 2.2.10-alt1
- Initial build in Sisyphus.
