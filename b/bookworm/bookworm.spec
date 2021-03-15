Name:     bookworm
Version:  1.1.2
Release:  alt2

Summary:  Simple, focused eBook reader

License:  GPLv3
Group: Office
URL:      https://github.com/babluboy/bookworm

# Source-git: https://github.com/babluboy/bookworm.git
Source:  %name-%version.tar

Patch1: %name-%version.patch

BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: libgranite-devel
BuildRequires: libgranite-vala
BuildRequires: libgee0.8-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: libpoppler-glib-devel
BuildRequires: libvala-devel vala
BuildRequires: libwebkit2gtk-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: appstream-devel
BuildRequires: libxml2-devel
BuildRequires: libsqlite3-devel

Requires: icon-theme-hicolor

%description

Read the books you love without having to worry about the different
format complexities like epub, pdf, mobi, cbr, etc. This version
supports EPUB, MOBI, FB2, PDF, FB2 and Comics (CBR and CBZ) formats
with support for more formats to follow soon.

%prep
%setup -q -n %name-%version
%patch1 -p1
# add python3 support fix
sed -i 's|#!.*python2$|#!/usr/bin/python3|' $(grep -Rl '#!.*python2$' *)

%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.babluboy.bookworm
desktop-file-validate %buildroot%_datadir/applications/com.github.babluboy.bookworm.desktop
appstream-util validate-relax --nonet %buildroot%_metainfodir/com.github.babluboy.bookworm.appdata.xml
( cd %buildroot%_bindir
  ln -s com.github.babluboy.bookworm bookworm
)

%files -f com.github.babluboy.bookworm.lang
%_bindir/com.github.babluboy.bookworm
%_bindir/bookworm
%_datadir/com.github.babluboy.bookworm/
%_datadir/applications/com.github.babluboy.bookworm.desktop
%_datadir/glib-2.0/schemas/com.github.babluboy.bookworm.gschema.xml
%_datadir/icons/hicolor/*/apps/com.github.babluboy.bookworm.svg
%_metainfodir/com.github.babluboy.bookworm.appdata.xml

%doc README.md
%doc COPYING

%changelog
* Sun Mar 07 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.1.2-alt2
- change description and make com.github.babluboy.bookworm symlink

* Sat Feb 27 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.1.2-alt1
- Initial build in Sisyphus (thanks Fedora for the spec)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.3.20200414git.c7c3643
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.2.20200414git.c7c3643
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.3-0.1.20200414git.c7c3643
- pre-release of 0.1.3

* Wed Apr 08 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-4
- resolve RHBZ#1822231

* Tue Mar 31 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-3
- changes per RHBZ#1812411

* Wed Mar 11 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-2
- fix Source0

* Sat Feb 22 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.2-1
- Initial version of the package
