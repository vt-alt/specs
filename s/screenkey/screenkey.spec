Name: screenkey
Version: 0.3
Release: alt3

Summary: A screen-cast tool to show your keys and based on key-mon project
License: GPLv3+
Group: Video

Url: https://launchpad.net/screenkey
Source0: %name-%version.tar
Source1: screenkey-stop.desktop
Packager: Denis Smirnov <mithraen@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-build-python

BuildRequires: python-base python-devel python-modules python-modules-compiler python-modules-email

%description
A screen-cast tool to show your keys inspired by Screenflick and based on
the key-mon project.

%prep
%setup
sed -i '/^Version=/d;s/^Categories=.*/Categories=AudioVideo;Video;Recorder;/' \
	data/screenkey.desktop

%build
%python_build

%install
mkdir -p %buildroot%_docdir/%name-%version
find build/lib* -name '*.py' -exec sed -i "1{/^#!/d}" {} \; && \
%python_install
install -pDm644 %SOURCE1 %buildroot%_desktopdir/screenkey-stop.desktop

%files
%doc
%_bindir/screenkey
%_desktopdir/screenkey*.desktop
%python_sitelibdir_noarch/Screenkey
%exclude %python_sitelibdir_noarch/*.egg-info

%changelog
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
