Name: gnome-desktop-testing
Version: 2018.1
Release: alt1

Summary: GNOME test runner for installed tests
Group: Development/GNOME and GTK+
License: LGPLv2+
Url: https://wiki.gnome.org/Initiatives/GnomeGoals/InstalledTests

#VCS: https://gitlab.gnome.org/GNOME/gnome-desktop-testing.git
Source: %name-%version.tar

BuildRequires: pkgconfig(gio-unix-2.0) >= 2.34
BuildRequires: pkgconfig(libsystemd)

%description
gnome-desktop-testing-runner is a basic runner for tests that are
installed in /usr/share/installed-tests.  For more information, see %url

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/gnome-desktop-testing-runner
%_bindir/ginsttest-runner
%doc COPYING README

%changelog
* Wed Jun 26 2019 Yuri N. Sedunov <aris@altlinux.org> 2018.1-alt1
- first build for Sisyphus (v2018.1-7-g355287f)

