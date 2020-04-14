Name: xdg-user-dirs-gtk
Version: 0.10
Release: alt2
Summary: Gnome integration of special directories
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later
URL: https://git.gnome.org/browse/xdg-user-dirs-gtk

Requires: xdg-user-dirs

Source: %name-%version.tar
Patch0: user-dirs-update-gtk.desktop.in-run-in-lxqt-xfce.patch

BuildRequires: intltool pkgconfig(gtk+-3.0) xdg-user-dirs

%description
Contains some integration of xdg-user-dirs with the gnome
desktop, including creating default bookmarks and detecting
locale changes.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
export CFLAGS='-Wno-error=deprecated-declarations'
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc NEWS AUTHORS README ChangeLog COPYING
%_sysconfdir/xdg/autostart/user-dirs-update-gtk.desktop
%_bindir/*

%changelog
* Thu Apr 09 2020 Anton Midyukov <antohami@altlinux.org> 0.10-alt2
- Added autostart to lxqt and xfce

* Mon Mar 23 2020 Anton Midyukov <antohami@altlinux.org> 0.10-alt1
- New version 0.10 (Closes: 27155)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Aug 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt1
- initial release
