Name: rpmrebuild-pesign
Version: 0.2.4
Release: alt1

Summary: Signer for packages containing PE format files
License: GPL-2.0-or-later
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: rpmrebuild
Requires: pesign

%description
%{summary}.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/rpmrebuild/plugins/
install -pm644 pesign.plug \
	%buildroot%_libexecdir/rpmrebuild/plugins/
install -pm755 pesign-change-{files,spec}.sh \
	%buildroot%_libexecdir/rpmrebuild/plugins/

%files
%_libexecdir/rpmrebuild/plugins/pesign*

%changelog
* Tue Oct 27 2020 Alexey Shabalin <shaba@altlinux.org> 0.2.4-alt1
- Add systemd-boot sign support

* Mon Mar 18 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.2.3-alt1
- Prevent second signing of shim<efi_arch>.efi binaries signed by Microsoft

* Fri Mar 15 2019 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt1
- Sign files in pei-i386 format as well.

* Thu Dec 19 2013 Dmitry V. Levin <ldv@altlinux.org> 0.2.1-alt1
- Fixed a typo in the latest fix.

* Wed Dec 18 2013 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Fixed %%sourcerpm tag clobbering problem.

* Wed Dec 11 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1.1-alt1
- Fixed work with pesign-client.

* Thu Dec 05 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.1-alt1
- Initial build.
