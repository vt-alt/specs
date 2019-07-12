Name: mintlocale
Version: 1.5.2
Release: alt1

Summary: Language selection tool for Cinnamon
License: GPLv2+
Group: Graphical desktop/GNOME

Url: https://github.com/linuxmint/mintlocale
Source0: %name-%version.tar

BuildArch: noarch

Patch: %name-%version-%release.patch

Requires: iso-flag-png

BuildPreReq: rpm-build-python
BuildPreReq: rpm-build-gir
BuildRequires: gobject-introspection

%description
Language selection tool for Cinnamon

%prep
%setup -n %name-%version
%patch0 -p1

%build

%install
install -m 0755 -d %buildroot%{_prefix}/
cp -Rp usr %buildroot

rm -f %buildroot%_bindir/add-remove-locales \
  %buildroot%_datadir/applications/%{name}-im.desktop \
  %buildroot%_prefix/lib/linuxmint/mintlocale/synaptic-install-packages \
  %buildroot%_prefix/lib/linuxmint/mintlocale/add.py \
  %buildroot%_prefix/lib/linuxmint/mintlocale/install_remove.py

echo 'LANG=$locale' > %{buildroot}%{_datadir}/linuxmint/mintlocale/templates/default_locale.template

%files
%_bindir/mintlocale
%_bindir/mintlocale-im
%_bindir/set-default-locale
%_prefix/lib/linuxmint
%_datadir/applications/%{name}.desktop
%_datadir/icons/hicolor/*/apps/%{name}-im.svg
%_datadir/icons/hicolor/*/apps/%{name}-im.png
%_datadir/linuxmint
%_datadir/polkit-1/actions/com.linuxmint.mintlocale.policy

%doc debian/copyright debian/changelog

%changelog
* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 1.5.2-alt1
- new version

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 1.5.1-alt1
- new version

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 1.5.0-alt1
- new version

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 1.4.9-alt1
- new version

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 1.4.8-alt1
- new version

* Mon Oct 30 2017 Vladimir Didenko <cow@altlinux.org> 1.4.4-alt1
- new version

* Wed May 23 2017 Vladimir Didenko <cow@altlinux.org> 1.4.3-alt1
- new version

* Fri May 30 2014 Vladimir Didenko <cow@altlinux.org> 1.1.6-alt2
- add support for /etc/syconfig/i18n

* Thu May 29 2014 Vladimir Didenko <cow@altlinux.org> 1.1.6-alt1
- initial build
