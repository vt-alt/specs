Name:		qnetstatview
Version:	1.5.3
Release:	alt1
Summary:	Shows detailed listings of all TCP and UDP endpoints
Group:		Networking/Other
License:	GPLv3+
URL:		http://dansoft.krasnokamensk.ru/more.html?id=1016
Source0:	%{name}-%{version}.tar

BuildRequires:	qt5-tools
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)


%description
Shows detailed listings of all TCP and UDP endpoints.

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
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Aug 15 2019 Alexander Danilov  <admsasha@altlinux.org> 1.5.3-alt1
- release 1.5.3

* Fri Aug  2 2019 Alexander Danilov  <admsasha@altlinux.org> 1.5.2-alt1
- release 1.5.2
