Name:           ds2048
Version:        1.0.1
Release:        alt1
Summary:        The 2048 number game implemented in Qt
Group:          Games/Puzzles
License:        GPLv3+
Url:            https://bitbucket.org/admsasha/ds2048
Source0:        %{name}-%{version}.tar

BuildRequires:	qt5-tools
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
2048 is a mathematics-based puzzle game where you have to slide tiles
on a grid to combine them and create a tile with the number 2048.
You have to merge the similar number tiles by moving the arrow keys
in four different directions. When two tiles with the same number touch,
they will merge into one.

%prep
%setup -q

%build
lrelease-qt5 %{name}.pro
%qmake_qt5
%make_build

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%changelog
* Wed Aug 21 2019 Alexander Danilov  <admsasha@altlinux.org> 1.0.1-alt1
- release 1.0.1
