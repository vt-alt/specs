Name: rpmrebuild-kmodsign
Version: 0.2
Release: alt2

Summary: Signer for packages containing linux kernel modules
License: GPL
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

Requires: rpmrebuild
Requires: rpmrebuild-pesign
Requires: kmod-sign

%description
%{summary}.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/rpmrebuild/plugins/
install -pm644 kmodsign.plug \
	%buildroot%_libexecdir/rpmrebuild/plugins/
install -pm755 kmodsign-change-files.sh \
	%buildroot%_libexecdir/rpmrebuild/plugins/

%files
%_libexecdir/rpmrebuild/plugins/kmodsign*

%changelog
* Fri Jul 05 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt2
- (sources) cleanup backup files

* Thu Sep 13 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.2-alt1
- compressed modules signing fixed

* Wed Sep 12 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt1
- initial build

