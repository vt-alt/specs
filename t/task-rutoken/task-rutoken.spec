Name: task-rutoken
Version: 1.0
Release: alt4

Summary: Metapackage to install all software for Rutoken support
License: GPL
Group: System/Configuration/Hardware

Url: http;//www.rutoken.ru
ExclusiveArch: i586 x86_64 armh aarch64 mipsel mips64el e2k e2kv4

Requires: librtpkcs11ecp
%ifarch i586 x86_64
Requires: rtadmin
Requires: openssl-engines-rutoken
Requires: rutoken-plugin
%endif
Requires: pcsc-lite-ccid

%description
Metapackage to install all software for Rutoken support

%files
%changelog
* Wed Oct 16 2019 Michael Shigorin <mike@altlinux.org> 1.0-alt4
- Sync ExclusiveArch: list with librtpkcs11ecp 1.9.12.0-alt1
- Restrict x86-only dependencies yet

* Thu Oct 03 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt3
- Added ExclusiveArch tag to limit architectures to %%ix86 and x86_64.

* Mon Aug 14 2017 Paul Wolneykien <manowar@altlinux.org> 1.0-alt2
- Fix: Require pcsc-lite-ccid for RuToken.

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus
