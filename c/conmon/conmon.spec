Name: conmon
# because typo in version :(
Epoch: 1
Version: 2.0.18
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
* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1:2.0.18-alt1
- new version 2.0.18

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 1:2.0.16-alt1
- new version 2.0.16

* Tue Apr 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1:2.0.15-alt1
- Update to 2.0.15

* Fri Sep 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.1-alt1
- Update to 2.1

* Tue Jan 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0-alt1.8fba2062.1
- Initial build for Sisyphus
