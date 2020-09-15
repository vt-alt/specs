Name: conmon
Version: 2.0.21
Release: alt1
# due to typo in version :(
Epoch: 1

Summary: OCI container runtime monitor
License: Apache-2.0
Group: System/Configuration/Other

Url: https://github.com/containers/conmon
Source: %name-%version.tar

BuildRequires: glibc-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libsystemd)

%description
%summary.

%prep
%setup

%build
%make_build CFLAGS+="%(getconf LFS_CFLAGS) -Wno-error=deprecated-declarations"

%install
%makeinstall_std PREFIX=%_usr

%files
%doc README.md
%_bindir/conmon

%changelog
* Thu Sep 10 2020 Alexey Shabalin <shaba@altlinux.org> 1:2.0.21-alt1
- new version 2.0.21

* Thu Jul 09 2020 Michael Shigorin <mike@altlinux.org> 1:2.0.18-alt2
- E2K: ftbfs workaround (might be the new glib2)
- i586: LFS fix (thx aris@ either)
- minor spec cleanup

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
