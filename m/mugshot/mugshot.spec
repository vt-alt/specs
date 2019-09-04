Name:    mugshot
Version: 0.4.2
Release: alt1

Summary: Mugshot is a lightweight user configuration utility that allows you to easily update personal user details
License: GPLv3+
Group:   Other
URL:     https://github.com/bluesabre/mugshot

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-distutils-extra
BuildRequires: intltool
BuildRequires: python3-module-dbus
BuildRequires: python3-module-pexpect
BuildRequires: python3-module-pycairo
BuildRequires: python3-module-pygobject3

BuildArch: noarch

Source:  %name-%version.tar

%description
Mugshot is a lightweight user configuration utility that allows you to
easily update personal user details. This includes:
- Linux profile image: ~/.face
- User details stored in /etc/passwd (used by finger)
- Pidgin buddy icon
- LibreOffice user details

%prep
%setup -n %name-%version

%build
%python3_build

%install
install -Dm0644 build/share/applications/mugshot.desktop %buildroot%_desktopdir/%name.desktop
%python3_install --prefix=/usr
rm -rf %buildroot%_datadir/doc/%name \
       %buildroot%_datadir/%name/metainfo

mkdir %buildroot%_datadir/locale
cp -av build/mo/* %buildroot%_datadir/locale

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README.md
%_bindir/%name
%python3_sitelibdir/%{name}*/
%python3_sitelibdir/*.egg-info
%_datadir/%name
%_datadir/glib-2.0/schemas/*.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/metainfo/%name.appdata.xml
%_man1dir/%name.1*

%changelog
* Sun Sep 01 2019 Andrey Cherepanov <cas@altlinux.org> 0.4.2-alt1
- New version.

* Fri Dec 28 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
