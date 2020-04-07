Group: Graphical desktop/Other
%define oldname dmz-cursor-themes
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# FIXME: Before package was based on openSUSE package. Now it uses Debian package. Also there is git repo
# https://github.com/ganwell/dmz-cursors with high-resolution sizes. May be this is the best option?

Name:           x-cursor-themes-dmz
Version:        0.4.5
Release:        alt1_3
Summary:        Style neutral cursors themes
License:        CC-BY-SA
URL:            https://packages.debian.org/sid/gnome/dmz-cursor-theme
Source0:        http://ftp.debian.org/debian/pool/main/d/dmz-cursor-theme/dmz-cursor-theme_%{version}.tar.xz
Patch0:         dmz-cursor-themes-symbolic-links.patch
BuildArch:      noarch
BuildRequires:  xcursorgen
Source44: import.info

%description
Scalable, style-neutral cursor themes based on the Industrial cursors designed
by Jakub Steiner for the Ximian GNOME Desktop.

%prep
%setup -q -n dmz-cursor-theme-%{version}
%patch0 -p1


%build
for color in White Black; do
    cd %{_builddir}/dmz-cursor-theme-%{version}/DMZ-$color/pngs
    ./make.sh
done

%install
for color in White Black; do
    install -d %{buildroot}%{_datadir}/icons/DMZ-$color/cursors
    install -m644 DMZ-$color/cursor.theme %{buildroot}%{_datadir}/icons/DMZ-$color/
    install -m644 DMZ-$color/index.theme %{buildroot}%{_datadir}/icons/DMZ-$color/
    install -m644 DMZ-$color/xcursors/* -t %{buildroot}%{_datadir}/icons/DMZ-$color/cursors/
done

%files
%doc debian/copyright
%{_datadir}/icons/DMZ-White/
%{_datadir}/icons/DMZ-Black/

%changelog
* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_3
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1_1
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_13
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_9
- update to new release by fcimport

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_8
- moved to Sisyphus for mate-themes-extras

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_8
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_7
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_6
- fc import

