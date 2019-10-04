Name: menulibre
Version: 2.2.1
Release: alt1

Summary: Advanced menu editor with quicklist support
License: %gpl3only
Group: Graphical desktop/Other
BuildArch: noarch
Epoch: 1

URL: https://launchpad.net/menulibre
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses intltool
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
#BuildRequires: python-devel python-module-distutils-extra python-module-pygtk
#BuildRequires: python-module-pyxdg python-module-pygobject3 libgtk+3-gir-devel libgtksourceview3-gir-devel
#libgnome-menus-gir-devel
BuildRequires: python3-module-distutils-extra
BuildRequires: python3-module-pyxdg python3-module-pygobject3 libgtk+3-gir-devel libgtksourceview3-gir-devel libgnome-menus-gir-devel

Requires: libgtk+3-gir libgtksourceview3-gir libgnome-menus-gir

%define _unpackaged_files_terminate_build 1

%description
An advanced menu editor that provides modern features in a clean,
easy-to-use interface. All without GNOME dependencies, so even
lightweight systems can benefit from the sanity that MenuLibre offers.
MenuLibre is your one-stop shop for menus in Linux, whether you use
Gnome, LXDE, Xfce, or Unity.

%prep
%setup
%patch0 -p1

%build
export XDG_RUNTIME_DIR="$TMPDIR"
%python3_build

%install
install -Dm0644 build/share/applications/menulibre.desktop %buildroot%_desktopdir/%name.desktop
export LANG=C.UTF-8
export XDG_RUNTIME_DIR="$TMPDIR"
%python3_install

# Install localizations
mkdir -p %buildroot%_datadir/locale
cp -a build/mo/* %buildroot%_datadir/locale/

%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name
%_bindir/%{name}*
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.*
%_pixmapsdir/*.*
%_man1dir/%{name}*.*
%python3_sitelibdir_noarch/%{name}*

%changelog
* Wed Oct 02 2019 Mikhail Efremov <sem@altlinux.org> 1:2.2.1-alt1
- Updated to 2.2.1.

* Wed Jun 18 2014 Mikhail Efremov <sem@altlinux.org> 1:2.0.4-alt1
- Updated to 2.0.4.

* Tue Mar 11 2014 Mikhail Efremov <sem@altlinux.org> 1:2.0.3-alt1
- Fix Xfce name (XFCE -> Xfce).
- Updated to 2.0.3.

* Mon Jul 08 2013 Mikhail Efremov <sem@altlinux.org> 13.04.17-alt1
- Updated to 13.04.17.

* Wed Apr 24 2013 Mikhail Efremov <sem@altlinux.org> 13.04.12-alt1
- Fix directory creation.
- Initial build.

