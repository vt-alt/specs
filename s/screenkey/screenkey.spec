Name: screenkey
Version: 1.1
Release: alt2

Summary: A screen-cast tool to show your keys and based on key-mon project
License: GPLv3+
Group: Video

Url: https://gitlab.com/screenkey/screenkey
Source: %name-%version.tar
Source1: screenkey-stop.desktop
Packager: Artyom Bystrov <arbars@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3  python3-module-distutils-extra intltool
Requires: slop
%description
A screen-cast tool to show your keys inspired by Screenflick and based on
the key-mon project.

%prep
%setup
%__subst '/^Version=/d;s/^Categories=.*/Categories=AudioVideo;Video;Recorder;/' \
	data/screenkey.desktop

%build
%python3_build

%install
mkdir -p %buildroot%_docdir/%name-%version
find build/lib* -name '*.py' -exec sed -i "1{/^#!/d}" {} \; && \
%python3_install
install -pDm644 %SOURCE1 %buildroot%_desktopdir/screenkey-stop.desktop

%files
%doc NEWS.rst README.rst
%_bindir/screenkey
%_desktopdir/screenkey*.desktop
%python3_sitelibdir/Screenkey
%exclude %python3_sitelibdir/*.egg-info

%changelog
* Sat Jul 25 2020 Artyom Bystrov <arbars@altlinux.org> 1.1-alt2
- Restoring changelog history of old versions

* Mon Jul 20 2020 Artyom Bystrov <arbars@altlinux.org> 1.1-alt1
- update version to 1.1
- changed URL of sources
- added translation to russian

* Mon Dec 02 2019 Artyom Bystrov <arbars@altlinux.org> 0.10-alt1
- Total update to version 0.10

* Fri Nov 29 2019 Michael Shigorin <mike@altlinux.org> 0.3-alt3
- screenkey-stop.desktop: consider rm#9540 notes

* Thu Nov 28 2019 Michael Shigorin <mike@altlinux.org> 0.3-alt2
- it's noarch
- added screenkey-stop.desktop
- fixed License: tag
- minor spec cleanup

* Thu Sep 05 2013 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- %name.desktop fixes

* Wed Sep 04 2013 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
