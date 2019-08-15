Name:           gigolo
Version:        0.5.0
Release:        alt1
Summary:        frontend to manage connections to remote filesystems using GIO/GVfs
Group:          File tools
License:        %gpl2only
URL:            https://www.uvena.de/gigolo/
Packager: Xfce Team <xfce@packages.altlinux.org>
Source:     %name-%version.tar
Patch:		%name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: libgtk+3-devel libgio-devel libX11-devel
BuildRequires: exo-csource

%define _unpackaged_files_terminate_build 1

%description
Gigolo is a frontend to easily manage connections to remote filesystems
using GIO/GVfs. It allows you to quickly connect/mount a remote
filesystem and manage bookmarks of such.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--enable-maintainer-mode \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name
%_bindir/%name
%_datadir/applications/gigolo.desktop
%_man1dir/%name.*

%changelog
* Tue Aug 13 2019 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- Updated to 0.5.0.

* Fri Mar 01 2019 Mikhail Efremov <sem@altlinux.org> 0.4.91-alt1
- Updated to 0.4.91.

* Mon Oct 29 2018 Mikhail Efremov <sem@altlinux.org> 0.4.90-alt1
- Explicitly enable debug (minimum level).
- Updated url.
- Updated to 0.4.90.

* Tue Nov 01 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- Fix icon.
- Spec updated.
- Updated to 0.4.2 (closes: #25308).

* Thu Jun 02 2011 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt1
- new version

* Wed Oct 21 2009 Mykola Grechukh <gns@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux
