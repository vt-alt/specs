Name:           ulcc
Version:        1.0.1
Release:        alt1
Summary:        Teaching children by pictures
Group:          Education
License:        GPLv3+
Url:            https://bitbucket.org/admsasha/ulcc
Source0:        %{name}-%{version}.tar

BuildRequires:	qt5-tools
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Multimedia)

%description
Teaching children by pictures is admirable facilities
to imparting knowledges.

%prep
%setup -q

%build
%qmake_qt5
%make_build

%install
%makeinstall INSTALL_ROOT=%{buildroot}

%files
%doc README* CONTRIBUTORS
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jul 30 2019 Alexander Danilov <admsasha@altlinux.org> 1.0.1-alt1
- release 1.0.1
