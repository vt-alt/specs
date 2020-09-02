Name:           puzzle-jigsaw
Version:        1.0.2
Release:        alt1
Summary:        Tiling puzzle that requires the assembly mosaiced pieces
Group:          Games/Puzzles
License:        GPLv3+
Url:            https://bitbucket.org/admsasha/puzzle-jigsaw
Source0:        %{name}-%{version}.tar

BuildRequires:  qt5-tools
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Multimedia)

%description
puzzle-jigsaw  is a tiling puzzle that requires the assembly 
of often oddly shaped interlocking and mosaiced pieces.

%prep
%setup -q

%build
lrelease-qt5 %{name}.pro
%qmake_qt5
%make_build

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%doc README* CONTRIBUTORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_iconsdir}/hicolor/*/apps/%{name}.png

%changelog
* Thu Aug 27 2020 Alexander Danilov  <admsasha@altlinux.org> 1.0.2-alt1
- adding a suffix if it is empty
- fixed loading of the puzzle
- set translator for default widget's text

* Wed Aug 26 2020 Alexander Danilov  <admsasha@altlinux.org> 1.0.1-alt1
- release 1.0.1

* Tue Aug 18 2020 Alexander Danilov  <admsasha@altlinux.org> 1.0.0-alt1
- release 1.0.0
