Name: smartcar
Version: 2.2
Release: alt1
Summary: Frontend to UMKI - Radio Controlled Robotic Construction Set
License: GPL
Group: Education
Conflicts: umki
Provides: umki = %version-%release
Obsoletes: umki
Url: http://umki.vinforika.ru/

Source: %name-%version.tar
Source1: %{name}.desktop
Source2: %{name}.svg
Source3: %{name}-16x16.png
Source4: %{name}-32x32.png
Source5: %{name}-48x48.png

BuildRequires: libqt4-devel libqwt6-devel gcc-c++ desktop-file-utils qt4-serialport-devel

%description
UMKI in Russian stands for Radio Controlled Robotic Construction Set,
Innovative. It helps children to design robots and learn to control
them.

# %package docs
# Summary: Documentation for %name
# Group: Education
# Conflicts: umki-docs
# Provides: umki-docs = %version-%release
# Obsoletes: umki-docs
# BuildArch: noarch

# %description docs
# Documentation for UMKI, which in Russian stands for Radio Controlled
# Robotic Construction Set, Innovative. It helps children to design
# robots and learn to control them.

%prep
%setup -q

%build
qmake-qt4 smartcar.pro
make clean
make

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/applications
mkdir -p %buildroot%_datadir/pixmaps
mkdir -p %buildroot%_miconsdir/
mkdir -p %buildroot%_niconsdir/
mkdir -p %buildroot%_liconsdir/

install -p -m755 %name %buildroot%_bindir/
install -p -m644 smart.ini %buildroot%_sysconfdir/%name
install -p -m644 umki_logo.png %buildroot%_datadir/%name
desktop-file-install --dir=%buildroot%_datadir/applications %SOURCE1
install -p -m644 %SOURCE2 %buildroot%_datadir/pixmaps
install -p -m644 %SOURCE3 %buildroot%_miconsdir/%{name}.png
install -p -m644 %SOURCE4 %buildroot%_niconsdir/%{name}.png
install -p -m644 %SOURCE5 %buildroot%_liconsdir/%{name}.png

%files
%doc readme*
%_bindir/%name
%_sysconfdir/%name
%_datadir/%name
%_datadir/applications/%{name}.desktop
%_datadir/pixmaps/%{name}.svg
%_miconsdir/%{name}.png
%_niconsdir/%{name}.png
%_liconsdir/%{name}.png

# %files docs
%doc umkiguide.pdf

%changelog
* Wed May 26 2021 Dmitry Derjavin <dd@altlinux.org> 2.2-alt1
- Help file display fixed.

* Mon Apr 19 2021 Dmitry Derjavin <dd@altlinux.org> 2.1-alt1
- New version.

* Sat Jun 16 2018 Dmitry Derjavin <dd@altlinux.org> 2.0-alt1
- Replacement for umki package;
- docs subpackage temporarily disabled.
