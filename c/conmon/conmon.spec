Name: conmon
Version: 2.1
Release: alt1

Summary: OCI container runtime monitor
License: Apache-2.0
Group:    System/Configuration/Other
Url: https://github.com/containers/conmon

Source: %name-%version.tar

BuildRequires: glib2-devel glibc-devel

%description
%summary.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=/usr

%files
%doc README.md
%_bindir/conmon

%changelog
* Fri Sep 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.1-alt1
- Update to 2.1

* Tue Jan 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0-alt1.8fba2062.1
- Initial build for Sisyphus
