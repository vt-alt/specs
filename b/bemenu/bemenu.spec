Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/doxygen gcc-c++ libncurses-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       bemenu
Version:    0.3.0
Release:    alt1_3
Summary:    Dynamic menu library and client program inspired by dmenu

# Library and bindings are LGPLv3+, other files are GPLv3+
License:    GPLv3+ and LGPLv3+
URL:        https://github.com/Cloudef/bemenu
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
# Created with: gpg --export-options export-minimal --armor --export 0CBD2CD395613887
Source2:    pgpkey-0CBD2CD395613887.asc

Patch:      0001-Mark-global-wayland-constant-extern.patch

BuildRequires:  gnupg gnupg2
BuildRequires:  ctest cmake gcc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
Source44: import.info

%description
%{summary}.

%package devel
Group: Other
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
Development files for extending %{name}.

%prep
%setup -q
%patch0 -p1


%build
%{fedora_cmake} \
    -DCURSES_NEED_WIDE=ON \
    -DBEMENU_WAYLAND_RENDERER=ON \
    "$PWD"
%make_build

%install
%makeinstall_std

%files
%doc README.md
%doc --no-dereference LICENSE-CLIENT LICENSE-LIB
%{_bindir}/%{name}
%{_bindir}/%{name}-run
%{_mandir}/man1/%{name}*.1*
# Long live escaping! %%%% resolves to %%; $v%%.* strips everything after first dot
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.%{version}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}-renderer-curses.so
%{_libdir}/%{name}/%{name}-renderer-wayland.so
%{_libdir}/%{name}/%{name}-renderer-x11.so

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so


%changelog
* Sun Mar 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3
- new version

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_3.20190819git442d283
- new version

