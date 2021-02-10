Name:    lightdm-gtk-greeter-settings
Version: 1.2.2
Release: alt1

Summary: A small dialog to make it easier for users to modify the settings of lightdm-gtk-greeter.
License: GPL-3.0
Group:   Development/Python3
URL:     https://github.com/Xubuntu/lightdm-gtk-greeter-settings

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-distutils-extra
BuildRequires: python3-module-pygobject3
BuildRequires: intltool

BuildArch: noarch

Source:  %name-%version.tar

%filter_from_requires /python3[(]gi.repository.GObject[)]/d

%description
LightDM GTK+ Greeter Settings is a configuration tool for the LightDM GTK+
Greeter.

%prep
%setup

%build
%python3_build

%install
%python3_install
mkdir -p %buildroot%_datadir/locale
cp -av build/mo/* %buildroot%_datadir/locale
cp -av build/share/* %buildroot%_datadir
rm -f %buildroot%_defaultdocdir/%name/*
%find_lang %name

%files -f %name.lang
%doc README NEWS
%_bindir/%{name}*
%_desktopdir/%name.desktop
%python3_sitelibdir/lightdm_gtk_greeter_settings
%python3_sitelibdir/*.egg-info
%_datadir/%name
%_datadir/polkit-1/actions/com.ubuntu.pkexec.lightdm-gtk-greeter-settings.policy

%changelog
* Wed Feb 03 2021 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus
