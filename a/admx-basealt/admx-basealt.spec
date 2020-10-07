%define _destdir %_datadir/PolicyDefinitions

Name: admx-basealt
Version: 0.1.3
Release: alt1

Summary: BaseALT-specific ADMX policy templates
License: AGPLv3+
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-basealt
BuildArch: noarch

Source0: %name-%version.tar

%description
BaseALT-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q

%install
mkdir -p %buildroot%_destdir
cp -r ru-RU/ en-US/ BaseALT*.admx %buildroot%_destdir/

%files
%dir %_destdir
%_destdir

%changelog
* Sat Sep 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.3-alt1
- Add sshd-allow-groups-list
- Fix authentication method (system-auth) selection and some number of typos

* Wed Sep 09 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.2-alt1
- Add sshd-permit-root-login control
- Fix in basealtcontrol ADML
- Fix tcb_chkpwd_restricted to root
- Fix duplicate naming (Accounts service)
- NTP Applier switch added

* Wed Jul 01 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- Update admx according to gpupdate-0.7.0 release

* Mon May 18 2020 Rustem Bapin <rbapin@altlinux.org> 0.1.0-alt1
- Initial release
