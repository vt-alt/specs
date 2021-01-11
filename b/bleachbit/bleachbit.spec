Name:     bleachbit
Version:  4.2.0
Release:  alt1

Summary:  Remove unnecessary files, free space, and maintain privacy
License:  GPL-3.0+
Group:    Archiving/Other
URL:      http://www.bleachbit.org/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source0:  %name-%version.tar
Patch1:   %name-apt-rpm-specific.patch
Patch2:   %name-alt-reasonable-config.patch

BuildArch:      noarch

BuildRequires(pre): rpm-build-gnome python3-devel

%add_python3_req_skip win32api win32con win32file winioctlcon
%add_python3_path %_datadir/%name
%filter_from_provides /^python3(/d

%description
BleachBit deletes unnecessary files to free valuable disk space,
maintain privacy, and remove junk. Rid your system of old clutter
including cache, cookies, Internet history, localizations, logs,
temporary files, and broken shortcuts. It wipes clean the cache
and history list of many common programs.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
make -C po local 
%python3_build

%install
%makeinstall_std prefix=%_prefix

sed -i -e '/^#!\//, 1d' %buildroot%_datadir/bleachbit/CLI.py
sed -i -e '/^#!\//, 1d' %buildroot%_datadir/bleachbit/GUI.py
rm -f %buildroot%_datadir/%name/Windows.py*

%find_lang %name

%files -f %name.lang
%doc COPYING README.md
%_bindir/%name
%_desktopdir/*.desktop
%_datadir/%name/
%_pixmapsdir/%name.png
%_datadir/metainfo/*.metainfo.xml
%_datadir/polkit-1/actions/*.policy

%changelog
* Sun Jan 03 2021 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version.

* Thu Sep 03 2020 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- New version.

* Mon May 04 2020 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.
- Fix License tag according SPDX.
- Build with python3.
- Do not check updates and use dark theme by default.

* Wed Feb 05 2020 Stanislav Levin <slev@altlinux.org> 2.2-alt2
- Fixed FTBS.

* Thu Apr 11 2019 Andrey Cherepanov <cas@altlinux.org> 2.2-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- New version.

* Fri Jul 08 2016 Andrey Cherepanov <cas@altlinux.org> 1.12-alt1
- new version 1.12

* Thu Jan 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.10-alt1
- New version

* Sun Jun 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.8-alt1
- New version

* Sat Feb 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.6-alt3
- Fix apt cleaner for apt-rpm support (ALT #30736)

* Mon Jan 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.6-alt2
- Package watch file to check for new version

* Wed Jan 07 2015 Andrey Cherepanov <cas@altlinux.org> 1.6-alt1
- New version

* Tue Sep 23 2014 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- New version

* Wed Jul 09 2014 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- New version

* Thu Dec 05 2013 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- New version

* Mon Nov 11 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version

* Tue Feb 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.9.5-alt1
- New version 0.9.5

* Fri Sep 07 2012 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- Initial build in Sisyphus (ALT #23106)

