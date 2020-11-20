Name: luckybackup
Version: 0.5.0
Release: alt3
Summary: A powerful, fast and reliable backup and sync tool

Group: File tools
License: GPL-3.0+
URL: http://luckybackup.sourceforge.net/index.html
Source0: http://downloads.sourceforge.net/project/%{name}/%{version}/source/%{name}-%{version}.tar.gz
Source1: luckybackup_ru.ts
Patch1: luckybackup-remove-missing-translations.patch
Patch2: luckybackup-use-locale.patch

BuildRequires(pre): gcc-c++ qt5-base-devel
BuildRequires: qt5-tools
#BuildRequires: desktop-file-utils
Requires: polkit

%define _pkgdocdir %{_docdir}/%{name}-%{version}

%description
luckyBackup is an application that backs-up and/or synchronizes any 
directories with the power of rsync.

It is simple to use, fast (transfers over only changes made and not all data), 
safe (keeps your data safe by checking all declared directories before 
proceeding in any data manipulation ), reliable and fully customizable.

%prep
%setup -q
%patch1 -p2
%patch2 -p2
sed -i 's,/usr/share/doc/luckybackup,%{_pkgdocdir},' luckybackup.pro
sed -i 's,/usr/share/doc/luckybackup/license/gpl.html,%{_pkgdocdir}/license/gpl.html,' src/global.h
sed -i 's,/usr/share/doc/luckybackup/manual/index.html,%{_pkgdocdir}/manual/index.html,' src/global.h
cp -a %SOURCE1 translations/luckybackup_ru.ts
# Remove generated language files
rm -f translations/*.qm

%build
lrelease-qt5 *.pro
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

# Install manual
subst 's,data/,/usr/share/doc/luckybackup/manual/data/,g' manual/index.html
mkdir -p %buildroot%_defaultdocdir/%name
cp -a manual %buildroot%_defaultdocdir/%name

# Remove source translation files
rm -f %buildroot%_datadir/%name/translations/*.ts

%files
%doc readme/README readme/changelog
%_bindir/%name
%_bindir/%name-pkexec
%_datadir/polkit-1/actions/net.luckybackup.su.policy
%_desktopdir/%{name}*
%_datadir/%name
%_man8dir/*.8.*
%_pixmapsdir/%{name}*
%doc %_defaultdocdir/%name

%changelog
* Thu Nov 19 2020 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt3
- Rebuild language files.
- Requires polkit instead of beesu (ALT #39315).
- Use current locale as default language.

* Mon Aug 19 2019 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt2
- Complete Russian translation (thanks Dmitry Astankov).

* Tue Dec 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- New version.
- Package manual.

* Thu Nov 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- New version.
- Build with Qt5.

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt2
- Initial build in Sisyphus from Fedora Autoimport

