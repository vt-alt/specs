Name: estrlist
Version: 0.2
Release: alt1

Summary: estrlist - string operation utility

License: Public domain
Group: Development/Other
Url: http://www.altlinux.org/Etersoft-build-utils

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: http://git.altlinux.org/people/lav/packages/estrlist.git
Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

Conflicts: etersoft-build-utils < 3.0.0

%description
String operation utility.

%prep
%setup

%install
install -D bin/%name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- estrlist: fix exclude, fix exclude tests

* Wed Oct 07 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus (separated from etersoft-build-utils)
