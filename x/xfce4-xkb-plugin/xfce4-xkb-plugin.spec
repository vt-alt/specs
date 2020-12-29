Name: xfce4-xkb-plugin
Version: 0.8.2
Release: alt1

Summary: XKB layout switch plugin for the Xfce panel
Summary(ru_RU.UTF-8): Дополнение для панели Xfce для работы с раскладками клавиатуры
License: BSD-2-Clause
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/panel-plugins/xfce4-xkb-plugin
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/panel-plugins/xfce4-xkb-plugin.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libgarcon-devel
BuildRequires: libSM-devel librsvg-devel libwnck3-devel libxklavier-devel xorg-cf-files

Requires: xfce4-panel

%define _unpackaged_files_terminate_build 1

%description
%name is the indicator and switcher of keyboard layout for XKB on the
XFce panel.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе дополнение для панели Xfce позволяющее
работать с раскладками клавиатуры.
Возможности:
* выбор вариантов отображения текущей раскладки (флаг/буквенный вариант)
* гибкая настройка управления раскладкой (глобально, для каждого
  приложения или для каждого окна).


%prep
%setup
%patch -p1

%build
# Don't use git tag in version.
%xfce4_drop_gitvtag xkb_version_tag configure.ac.in
%xfce4reconf
%configure \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS COPYING
%_libdir/xfce4/panel/plugins/*.so
%dir %_datadir/xfce4/xkb
%dir %_datadir/xfce4/xkb/flags
%_datadir/xfce4/xkb/flags/*
%_datadir/xfce4/panel/plugins/*.desktop

%exclude %_libdir/xfce4/panel/plugins/*.la
# Seems glibc doesn't support uz@Latn
%exclude %_datadir/locale/uz@Latn/LC_MESSAGES/xfce4-xkb-plugin.mo

%changelog
* Thu Dec 24 2020 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2.

* Sun Sep 13 2020 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt3.g6026349
- Fixed BR.
- Updated Vcs tag.
- Upstream git snapshot.

* Wed Mar 25 2020 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt2
- Add Vcs tag.
- Update Url.
- Package COPYING file.
- Fix license.

* Thu Aug 23 2018 Mikhail Efremov <sem@altlinux.org> 0.8.1-alt1
- Don't package uz@Latn translation.
- Fix license.
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 0.8.1.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 0.7.1.

* Wed Oct 16 2013 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt2.git20131012
- Upstream git snapshot.

* Tue May 21 2013 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Tue May 14 2013 Mikhail Efremov <sem@altlinux.org> 0.5.5-alt1.git20130427
- Bump version
  (this snapshot is newer then xfce4-xkb-plugin-0.5.5 release).
- Drop remains of old ALT-specific patches.
- Upstream git snapshot.

* Mon Apr 29 2013 Mikhail Efremov <sem@altlinux.org> 0.5.4.3-alt4.git20130403
- Drop obsoleted patches.
- Upstream git snapshot.

* Thu Jun 14 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.3-alt3
- Fix group name validation.
- Fix reading xkb settings from xfconf.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.3-alt2
- Rebuild against libxfce4util.so.6 (libxfce4util-4.9).
- Updated translations from upstream git.

* Fri Feb 03 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.3-alt1
- Updated to 0.5.4.3.

* Fri Jan 20 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.2-alt4
- Never modify xkb configuration if system settings are used.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 0.5.4.2-alt3
- Rebuild with xfce4-panel-4.9.

* Thu Dec 01 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.2-alt2
- Check keyboard-layout settings in the xfconf.
- Disable layout's list if never_modify_config=true.
- Write settings to xfconf too.

* Mon Oct 17 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.2-alt1
- Updated to 0.5.4.2.

* Mon Oct 10 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.1-alt2
- Fix crash with incomplete configuration.

* Tue May 24 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.1-alt1
- Fix build: create m4 directory.
- Updated to 0.5.4.1.

* Fri Apr 29 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.0-alt2
- Fixes from upstream git (mostly memory leaks).

* Thu Apr 21 2011 Mikhail Efremov <sem@altlinux.org> 0.5.4.0-alt1
- Fix memory leaks.
- Drop obsoleted patches.
- Updated to 0.5.4.0.

* Thu Mar 24 2011 Sergey Kurakin <kurakin@altlinux.org> 0.5.3.3-alt7
- Fix segfault after configuration with empty keyboard model combobox
  (Closes: #25276)

* Thu Jan 27 2011 Mikhail Efremov <sem@altlinux.org> 0.5.3.3-alt6
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec cleanup.
- tar.gz -> tar.
- Fix License.
- Fix Url.
- Renew patches for libxklavier (from Debian).
- Add fix-various-segfaults.patch (from Debian).
- Drop watch file.

* Mon Jun 14 2010 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt5
- Rebuild with new xclavier.

* Tue Nov 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt4
- Added xkb-config.patch.

* Sun Sep 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt3
 -Russion translation updated.

* Fri Sep 04 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt2
- Added first-run.patch from boyarsh

* Mon Apr 27 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.5.3.3-alt1
- Version update

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.2-alt1
- new version

* Thu Jan 03 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.4.3-alt2
- add watch file

* Thu May 03 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.4.3-alt1
- new version

* Fri Oct 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.4.1-alt1
- new version for xfce 4.4rc1

* Sat Jan 01 2005 Andrey Astafiev <andrei@altlinux.ru> 0.3.2-alt2
- Rebuilt with new xfce4-panel.

* Sat Aug 14 2004 Andrey Astafiev <andrei@altlinux.ru> 0.3.2-alt1
- First version of RPM package for Sisyphus.
