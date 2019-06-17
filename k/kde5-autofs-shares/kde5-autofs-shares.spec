Name: kde5-autofs-shares
Version: 0.2.2
Release: alt1
%K5init

Summary: Samba shares plugin for Dolphin

License: GPL
Group: Graphical desktop/KDE
BuildArch: noarch

Requires: kf5-filesystem kde5-kdialog autofs

Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf5

%description
This plugin allows mounting samba shares from Dolphin

%prep
%setup

%install
install -D -m 0644 autofs-shares-manage.desktop %buildroot/%_K5srv/ServiceMenus/autofs-shares-manage.desktop
install -D -m 0755 autofs-shares-mount.desktop %buildroot/%_K5start/autofs-shares-mount.desktop
install -D -m 0755 bin/kde5-autofs-shares-manage %buildroot/%_bindir/kde5-autofs-shares-manage
install -D -m 0755 bin/kde5-autofs-shares-mount %buildroot/%_bindir/kde5-autofs-shares-mount
# translations
find po/* -type d | \
while read d
do
    lang=`basename $d`
    mkdir -p %buildroot/%_datadir/locale/$lang/LC_MESSAGES
    msgfmt -o %buildroot/%_datadir/locale/$lang/LC_MESSAGES/%name.mo $d/%name.po
done

%find_lang %name

%files -f %name.lang
%_K5start/autofs-shares-mount.desktop
%_K5srv/ServiceMenus/autofs-shares-manage.desktop
%_bindir/kde5-autofs-shares-*

%changelog
* Wed Mar 20 2019 Sergey V Turchin <zerg@altlinux.org> 0.2.2-alt1
- check ~/.autofs.shares available on mount

* Mon May 15 2017 Sergey V Turchin <zerg@altlinux.org> 0.2.1-alt1
- fix autostart

* Fri May 12 2017 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- using autofs

* Thu May 04 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.2-alt1
- Add: i18n

* Thu May 04 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt4
- Replaced $1 with $SHARE

* Wed May 03 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt3
- Fixed behavior on mounting shares with whitespaces

* Wed May 03 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt2
- Minor fixes

* Tue May 02 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.1-alt1
- Added bash-script for mounting shares

* Mon May 01 2017 Oleg Solovyov <mcpain@altlinux.org> 0.1.0-alt1
- Initial build
