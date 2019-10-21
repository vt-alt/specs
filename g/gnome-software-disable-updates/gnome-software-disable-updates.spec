Name: gnome-software-disable-updates
Version: 1.0
Release: alt1

Summary: Disable updates for gnome-software
License: GPLv3+
Group: Other
URL: http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: gnome-software
BuildArch: noarch

%description
%{summary}.

%install
mkdir -p %buildroot%_datadir/glib-2.0/schemas
cat > %buildroot%_datadir/glib-2.0/schemas/z-%name.gschema.override << EOF.
[org.gnome.software]
allow-updates = false
EOF.

%files
%_datadir/glib-2.0/schemas/*.gschema.override

%changelog
* Mon Oct 21 2019 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
