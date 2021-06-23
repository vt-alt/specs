%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-chromium
Version: 90.0
Release: alt1

Summary: Chromium-specific ADMX policy templates
License: CC-BY-2.5
Group: System/Configuration/Other
Url: https://www.chromium.org/administrators/policy-templates
BuildArch: noarch

Source0: policy_templates.tar

%description
Chromium-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q -n policy_templates

%install
mkdir -p %buildroot%_datadir
cp -a windows/admx/ %buildroot%_destdir

%files
%dir %_destdir
%dir %_destdir/*-*/
%_destdir/*.admx
%_destdir/*/*.adml

%changelog
* Fri May 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 90.0-alt1
- Update to latest release
- Fix installation to /usr/share/PolicyDefinitions
- Set right License and URL of upstream project

* Fri Apr 02 2021 Alenka Glukhovskaya <alenka@altlinux.org> 89.0-alt1
- Initial release

