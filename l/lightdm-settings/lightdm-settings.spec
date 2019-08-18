Name: lightdm-settings
Version: 1.2.8
Release: alt1
Summary: Configuration tool for the LightDM display manager
Group: Graphical desktop/Other
License: GPLv3+
Url: https://github.com/linuxmint/lightdm-settings
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildArch: noarch

Requires: slick-greeter
Requires: python3(xapp)
Requires: python3(setproctitle)
Requires: python3-module-pygobject3

%description
This tool currently lets users configure slick-greeter.

%prep
%setup
%patch0 -p1

%build
%make_build

%install
# No install target in Makefile
install -m755 -pd %{buildroot}
cp -pr .%{_prefix} %{buildroot}

# Set exec permissions for bin/* files.
chmod -c 0755 %{buildroot}%{_bindir}/%{name}			\
	 %{buildroot}%{_prefix}/lib/%{name}/%{name}

%find_lang %{name}


%files -f %name.lang
%doc debian/changelog README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/polkit-1/actions/org.x.%{name}.policy

%changelog
* Thu Aug 1 2019 Vladimir Didenko <cow@altlinux.org> 1.2.8-alt1
- 1.2.8

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 1.2.7-alt1
- 1.2.7

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 1.2.6-alt1
- 1.2.6

* Wed Dec 26 2018 Vladimir Didenko <cow@altlinux.org> 1.2.5-alt1
- 1.2.5

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 1.2.4-alt1
- 1.2.4

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Jun 14 2018 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- 1.2.1

* Fri May 18 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.1.4-alt1
- 1.1.4

* Mon Oct 30 2017 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Sep 4 2017 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
