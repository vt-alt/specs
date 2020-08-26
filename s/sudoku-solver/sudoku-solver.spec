Name:		sudoku-solver
Version:	1.0.1
Release:	alt1
Summary:	Sudoku solver
Group:		Games/Other
License:	GPLv3+
URL:		http://dansoft.krasnokamensk.ru/more.html?id=1032
Source0:	%{name}-%{version}.tar

BuildRequires:	qt5-tools
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)


%description
Solver sudoku puzzles.

%prep
%setup -q

%build
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
* Mon Aug 24 2020 Alexander Danilov  <admsasha@altlinux.org> 1.0.1-alt1
- release 1.0.1

* Mon Jul 27 2020 Alexander Danilov  <admsasha@altlinux.org> 1.0.0-alt1
- release 1.0.0
