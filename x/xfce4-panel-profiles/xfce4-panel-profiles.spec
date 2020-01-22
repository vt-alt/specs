Name: xfce4-panel-profiles
Version: 1.0.10
Release: alt1

Summary: A simple application to manage Xfce panel layouts
License: GPL-3.0+
Group: Graphical desktop/XFce
Url: https://git.xfce.org/apps/xfce4-panel-profiles/about/

Vcs: https://git.xfce.org/apps/xfce4-panel-profiles/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>
BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: intltool
%add_python3_path %_datadir/%name

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
Xfce4 Panel Profiles (xfce4-panel-profiles, formerly known as xfpanel-switch)
is a simple application to manage Xfce panel layouts.
With the modular Xfce Panel, a multitude of panel layouts can be
created. This tool makes it possible to backup, restore, import, and
export these panel layouts.

%prep
%setup
%patch -p1

%build
# It is not autotools configure
./configure \
	--prefix=%_prefix \
	--python=python3
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name
%_bindir/%name
%_datadir/%name/
%_desktopdir/*.desktop
%_datadir/metainfo/*.appdata.xml
%_man1dir/%name.*

%changelog
* Wed Jan 15 2020 Mikhail Efremov <sem@altlinux.org> 1.0.10-alt1
- Added Vcs tag.
- Added Simply Linux 9 profile.
- Updated to 1.0.10.

* Tue Dec 03 2019 Mikhail Efremov <sem@altlinux.org> 1.0.9-alt2
- Don't use rpm-build-licenses.
- Fix requires: use rpm-build-gir.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 1.0.9-alt1
- Updated to 1.0.9.

* Mon Jun 24 2019 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt2
- Fix python3 requires (closes: #36942).

* Mon Aug 27 2018 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt1
- Initial build.
