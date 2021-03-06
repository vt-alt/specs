Name:    ibus-m17n
Version: 1.4.5
Release: alt1
Group:   System/Libraries
Summary: The M17N engine for IBus platform
License: GPL-2.0+
URL: https://github.com/ibus/ibus-m17n

Source0: %name-%version.tar

# Fedora specific patches:
# Enable lv3:ralt_switch option for some Indic engines in default.xml.
Patch100: ibus-m17n-xkb-options.patch
# Don't make the status button clickable (maybe obsolete).
Patch101: ibus-m17n-hide-title-status.patch
# Use ar-kbd as default keymap for Arabic
# https://bugzilla.redhat.com/show_bug.cgi?id=1076945
Patch103: ibus-m17n-enable-ar-kbd.patch

BuildRequires: gettext-tools libasprintf-devel
BuildRequires: gcc-c++
BuildRequires: gnome-common
BuildRequires: libm17n-devel
BuildRequires: gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel
BuildRequires: libibus-devel libibus-gir-devel

Requires: ibus python3-module-ibus-overrides
Requires: libm17n m17n-utils

%description
M17N engine for IBus input platform. It allows input of many languages using
the input table maps from m17n-db.

%prep
%setup
%patch100 -p1
%patch101 -p1
%patch103 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static --with-gtk=3.0
# make -C po update-gmo
%make_build

%install
%makeinstall_std
%find_lang %name

%check
make check

%files -f %name.lang
%doc AUTHORS README
%_libexecdir/ibus-engine-m17n
%_libexecdir/ibus-setup-m17n
%_datadir/ibus-m17n
%_datadir/ibus/component/*
%_datadir/metainfo/m17n.appdata.xml
%_desktopdir/ibus-setup-m17n.desktop
%_datadir/glib-2.0/schemas/org.freedesktop.ibus.engine.m17n.gschema.xml

%changelog
* Fri Apr 09 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.5-alt1
- New version.

* Sat Jan 30 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- New version.

* Wed Jun 24 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt1
- New version.
- Build from upstream tag.

* Mon Mar 23 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt2
- Initial import to Sisyphus from Fedora.

