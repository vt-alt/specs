Name:		ipqalc
Version:	1.5.3
Release:	alt1
Summary:	IP address calculator
Group:		Video
License:	GPLv3+
URL:		https://bitbucket.org/admsasha/ipqalc/
Source0:	https://bitbucket.org/admsasha/ipqalc/downloads/%{name}-%{version}.tar.gz

BuildRequires:	qt5-tools
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
Small utility for IP address calculations including broadcast 
and network addresses as well as Cisco wildcard mask.

%prep
%setup -q

%build
%qmake_qt5
%make_build

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Aug  1 2019 Alexander Danilov  <admsasha@altlinux.org> 1.5.3-alt1
- release 1.5.3

* Tue Jul 30 2019 Alexander Danilov <admsasha@altlinux.org> 1.5.2-alt1
- release 1.5.2
