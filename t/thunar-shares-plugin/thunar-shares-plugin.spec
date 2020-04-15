#define git_date .git20111111
%define git_date %nil

Name: thunar-shares-plugin
Version: 0.3.1
Release: alt1%git_date
Epoch: 1
Summary: Thunar file manager extension to share files using Samba
Summary(ru_RU.UTF8): Расширение файлового менеджера Thunar для предоставления доступа к папкам по сети.

Group:     Graphical desktop/XFce
License:   GPLv2+
URL:      https://docs.xfce.org/xfce/thunar/thunar-shares-plugin
Vcs:      git://git.xfce.org/thunar-plugins/thunar-shares-plugin
Source:   %name-%version.tar
Patch:    %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libthunar-devel
BuildRequires: intltool

# Can be used by shareman too.
#Requires: Thunar

Requires: samba

%define _unpackaged_files_terminate_build 1

%description
A Thunar file manager extension to share files using Samba. The backend
is based on nautilus-share.

%description -l (ru_RU.UTF8)
Плагин для файлового менеджера Thunar позволяющий предоставлять общий
доступ к папкам по сети используя Samba. Основан плагине nautilus-share.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
    --disable-static \
    --enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS README
%_libdir/thunarx-*/%name.so
%exclude %_libdir/thunarx-*/*.la

%changelog
* Mon Apr 06 2020 Mikhail Efremov <sem@altlinux.org> 1:0.3.1-alt1
- Updated url.
- Added Vcs tag.
- Don't use rpm-build-licenses.
- Updated to 0.3.1.

* Tue Aug 21 2018 Mikhail Efremov <sem@altlinux.org> 1:0.3.0-alt1
- Update url.
- Enable debug (minimum level).
- Use _unpackaged_files_terminate_build.
- Fix Xfce name (XFCE -> Xfce).
- Updated to 0.3.0.

* Fri Nov 25 2011 Mikhail Efremov <sem@altlinux.org> 1:0.2.1-alt2.git20111111
- Fix usershare_acl parsing.
- Updated translations.

* Wed Sep 07 2011 Mikhail Efremov <sem@altlinux.org> 1:0.2.1-alt1.git20110809
- Drop Thunar from requires (can be used by shareman too).
- Updated translations.

* Mon Apr 11 2011 Mikhail Efremov <sem@altlinux.org> 1:0.2.1-alt1.git20110411
- Fix versioning, add epoch.
- Drop tsp-l10n-fix.patch.
- Spec updated, tar.gz -> tar.
- Updated from upstream git (merged master and thunarx-2 branches).

* Fri Oct 02 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.20-alt2
- Fix localization problem.

* Thu Oct 01 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.20-alt1
- Version update.

* Thu Oct 01 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.16-alt2
- Spec cleanup and dependency refresh.

* Thu Feb 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.16-alt1
- First build.
