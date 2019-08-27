#define git_date .git20120414
%define git_date %nil

Name: xfce4-screenshooter
Version: 1.9.6
Release: alt1%git_date

Summary: Screenshot Xfce4 panel plugin
Summary (ru_RU.UTF-8): Дополнение для панели Xfce позволяющее делать снимки экрана
License: %gpl2plus
Group: Graphical desktop/XFce
Url: https://goodies.xfce.org/projects/applications/xfce4-screenshooter
Packager: Xfce Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/apps/xfce4-screenshooter
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libxfce4panel-gtk3-devel libxfce4ui-gtk3-devel libxfce4util-devel libexo-gtk3-devel
BuildPreReq: libxml2-devel libXi-devel
BuildRequires: intltool libsoup-devel libXext-devel libICE-devel libXfixes-devel libSM-devel
# Seems GTK-based programs needed X server even to display a version.
# So don't install help2man and use pre-generated man page from upstream
# instead.
#BuildRequires: help2man

Provides:  xfce4-screenshooter-plugin = %version-%release
Obsoletes: xfce4-screenshooter-plugin < %version-%release

%define _unpackaged_files_terminate_build 1

%description
This application allows you to capture the entire screen, the active
window or a selected region.
You can set the delay that elapses before the screenshot is taken
and the action that will be done with the screenshot: save it to a PNG
file, copy it to the clipboard, or open it using another application.

A plugin for the Xfce panel is also available.

%description -l ru_RU.UTF-8
Стандартное приложение Xfce позволяющее делать снимки экрана. Программа
основана на gnome-screenshot и имеет схожие функции. Имеется возможность
управления как мышкой так и с помощью "горячих" клавишь.

Дополнение для панели Xfce так же включено.

%prep
%setup
%patch -p1
# Don't use git tag in version.
#sed -i 's/m4_define(\[xfce4_screenshooter_version_tag\], \[git\])/m4_define(\[xfce4_screenshooter_version_tag\], \[\])/' configure.ac.in
mkdir m4/

%build
%xfce4reconf
%configure \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS
%_libdir/xfce4/panel/plugins/*.so
%_datadir/xfce4/panel/plugins/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/applications/*.desktop
%_datadir/metainfo/*.xml
%_bindir/xfce4-screenshoot*
%_mandir/man1/xfce4-screenshooter*

%exclude %_libdir/xfce4/panel/plugins/*.la

%changelog
* Mon Aug 26 2019 Mikhail Efremov <sem@altlinux.org> 1.9.6-alt1
- Updated to 1.9.6.

* Mon Apr 01 2019 Mikhail Efremov <sem@altlinux.org> 1.9.5-alt1
- Updated to 1.9.5.

* Tue Mar 12 2019 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt2
- Fix man page.

* Mon Mar 11 2019 Mikhail Efremov <sem@altlinux.org> 1.9.4-alt1
- Added help2man to BR.
- Updated to 1.9.4.

* Wed Aug 22 2018 Mikhail Efremov <sem@altlinux.org> 1.9.3-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Updated to 1.9.3.

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.8.2-alt2
- Rebuild with libxfce4util-4.12.

* Mon Jan 26 2015 Mikhail Efremov <sem@altlinux.org> 1.8.2-alt1
- Revert "Don't use xfhelp4.".
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 1.8.2.

* Tue May 22 2012 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt2
- Updated translations from upstream git.
- Fix BR.

* Thu May 03 2012 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1
- Don't use xfhelp4.
- Fix pligin linking.
- Updated to 1.8.1.

* Mon Apr 16 2012 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt3.git20120414
- Drop additional-category.patch.
- Upstream git snapshot.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt2
- Rebuild with xfce4-panel-4.9.

* Tue Aug 16 2011 Mikhail Efremov <sem@altlinux.org> 1.8.0-alt1
- Enable XFIXES extension support.
- Updated to 1.8.0.

* Tue May 03 2011 Mikhail Efremov <sem@altlinux.org> 1.7.9-alt2.git20110429
- Upstream git snapshot.

* Tue Mar 08 2011 Mikhail Efremov <sem@altlinux.org> 1.7.9-alt2.git20110227
- Upstream git snapshot.

* Thu Jan 27 2011 Mikhail Efremov <sem@altlinux.org> 1.7.9-alt1
- Fix desktop file path for xfce4-panel >= 4.8.
- Spec cleanup & update.
- Fix License.
- Fix Url.
- tar.bz2 -> tar
- Updated to 1.7.9.

* Tue Dec 15 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.6.0-alt3
- Some repocop warnings is taken into account.

* Thu Jul 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.6.0-alt2
- Fix localization errors in screenshot file names.

* Wed Jun 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.6.0-alt1
- Version update to 1.6.0

* Sat Jun 06 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.99-alt1
- Beta version of Xfce4-screenshooter 1.6

* Sun Apr 26 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.1-alt0.M50.1
- Backport to Desktop 5.0

* Fri Apr 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.1-alt1
Update to version 1.5.1. Name changed to xfce4-screenshooter

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.4.0-alt1
- new version

* Sun Oct 29 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.0.0-alt1
- First version of RPM package for Sisyphus.
