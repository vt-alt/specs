%define ver_major 0.1
%define _libexecdir %_prefix/libexec

%def_enable man
%def_enable check

Name: xdg-dbus-proxy
Version: %ver_major.1
Release: alt1

Summary: D-Bus connections proxy
Group: System/Kernel and hardware
License: LGPLv2.1+
Url: https://github.com/flatpak/%name

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# https://salsa.debian.org/debian/xdg-dbus-proxy/tree/debian/master/debian/patches
Patch10: build-Adapt-to-AX_CODE_COVERAGE-API-change.patch
Patch11: build-Forbid-AX_-prefixed-patterns-more-selectively.patch
Patch12: build-Use-CODE_COVERAGE_CPPFLAGS.patch

BuildRequires: autoconf-archive libgio-devel > 2.40
%{?_enable_man:BuildRequires: xsltproc docbook-style-xsl}
%{?_enable_check:BuildRequires: /proc dbus-tools-gui}

%description
%name is a filtering proxy for D-Bus connections. It was originally part
of the flatpak project, but it has been broken out as a standalone module
to facilitate using it in other contexts.

%prep
%setup
%patch -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%autoreconf
%configure %{subst_enable man}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/%name
%{?_enable_man:%_man1dir/%name.1.*}
%doc README.md NEWS


%changelog
* Wed May 29 2019 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus



