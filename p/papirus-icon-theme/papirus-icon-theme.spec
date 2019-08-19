Name:     papirus-icon-theme
Version:  20190817
Release:  alt1

Summary:  All Papirus icon themes
License:  GPLv3
Group:    Other
Url:      https://github.com/PapirusDevelopmentTeam/papirus-icon-theme

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

Requires: icon-theme-Papirus = %EVR
Requires: icon-theme-Papirus-Dark = %EVR
Requires: icon-theme-Papirus-Light = %EVR
Requires: icon-theme-ePapirus = %EVR

%description
Papirus is a free and open source SVG icon theme for Linux, based on
Paper Icon Set with a lot of new icons and a few extras, like
Hardcode-Tray support, KDE colorscheme support, Folder Color support,
and others.

Papirus icon theme is available in six variants:

* Papirus
* Papirus Dark
* Papirus Light
* ePapirus (for elementary OS and Pantheon Desktop)

%package -n icon-theme-Papirus
Summary: Papirus icon theme
Group: Other

%description -n icon-theme-Papirus
%summary.

%package -n icon-theme-Papirus-Dark
Summary: Papirus-Dark icon theme
Group: Other
Requires(pre): icon-theme-Papirus

%description -n icon-theme-Papirus-Dark
%summary.

%package -n icon-theme-Papirus-Light
Summary: Papirus-Light icon theme
Group: Other
Requires(pre): icon-theme-Papirus

%description -n icon-theme-Papirus-Light
%summary.

%package -n icon-theme-ePapirus
Summary: ePapirus icon theme
Group: Other
Requires(pre): icon-theme-Papirus

%description -n icon-theme-ePapirus
%summary.

%prep
%setup
# Make network menu item in ALT looks like upstream Internet menu item
for i in 16 22 24 32 48 64;do
    ln -s internet-web-browser.svg Papirus/${i}x${i}/apps/applications-network.svg
done

%install
mkdir -p %buildroot%_iconsdir
cp -a Papirus Papirus-Dark Papirus-Light ePapirus %buildroot%_iconsdir

%files
%doc AUTHORS LICENSE README.md

%files -n icon-theme-Papirus
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus

%files -n icon-theme-Papirus-Dark
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Dark

%files -n icon-theme-Papirus-Light
%doc AUTHORS LICENSE README.md
%_iconsdir/Papirus-Light

%files -n icon-theme-ePapirus
%doc AUTHORS LICENSE README.md
%_iconsdir/ePapirus

%changelog
* Mon Aug 19 2019 Andrey Cherepanov <cas@altlinux.org> 20190817-alt1
- New version.

* Mon Aug 05 2019 Andrey Cherepanov <cas@altlinux.org> 20190802-alt1
- New version.

* Mon Jul 22 2019 Andrey Cherepanov <cas@altlinux.org> 20190720-alt1
- New version.

* Wed Jul 10 2019 Andrey Cherepanov <cas@altlinux.org> 20190708-alt1
- New version.

* Mon Jul 01 2019 Andrey Cherepanov <cas@altlinux.org> 20190701-alt1
- New version.

* Sun Jun 16 2019 Andrey Cherepanov <cas@altlinux.org> 20190615-alt1
- New version.

* Tue May 28 2019 Andrey Cherepanov <cas@altlinux.org> 20190521-alt2
- Make network menu item in ALT looks like upstream Internet menu item.

* Thu May 23 2019 Andrey Cherepanov <cas@altlinux.org> 20190521-alt1
- New version.
- Make trash icon grayed.

* Thu May 02 2019 Andrey Cherepanov <cas@altlinux.org> 20190501-alt1
- New version.

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 20190331-alt1
- New version.
- Requires icon-theme-Papirus to derivative themes for correct upgrade (ALT #36318). 

* Wed Mar 06 2019 Andrey Cherepanov <cas@altlinux.org> 20190302-alt1
- New version.

* Mon Feb 04 2019 Andrey Cherepanov <cas@altlinux.org> 20190203-alt1
- New version.

* Sun Jan 06 2019 Andrey Cherepanov <cas@altlinux.org> 20190106-alt1
- New version.

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 20181120-alt1
- New version.
- Remove Papirus-Adapta{,-Nokto} icon themes.

* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 20181007-alt1
- New version.

* Fri Aug 17 2018 Andrey Cherepanov <cas@altlinux.org> 20180816-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 20180720-alt1
- New version.

* Mon Jul 16 2018 Andrey Cherepanov <cas@altlinux.org> 20180601-alt1
- Initial build for Sisyphus
