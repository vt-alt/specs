%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-firefox
Version: 2.10
Release: alt1

Summary: Firefox-specific ADMX policy templates
License: MPL-2.0
Group: System/Configuration/Other
Url: https://github.com/mozilla/policy-templates
BuildArch: noarch

Source0: policy-templates.tar

%description
Firefox-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q -n policy-templates

%install
mkdir -p %buildroot%_datadir
cp -a windows/ %buildroot%_destdir

%files
%dir %_destdir
%dir %_destdir/*-*/
%_destdir/*.admx
%_destdir/*/*.adml

%changelog
* Fri May 07 2021 Evgeny Sinelnikov <sin@altlinux.org> 2.10-alt1
- Update to new release with russian translation
- Set right URL of upstream project

* Fri Apr 02 2021 Alenka Glukhovskaya <alenka@altlinux.org> 2.9-alt1
- Initial release 

