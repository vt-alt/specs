Name: rpm-build-kernel-perms
Version: 1.3
Release: alt1

Summary: RPM helper to fix permissions for kernel and modules
License: GPL-2.0-only
Group: Development/Other

Source: %name-%version.tar

Requires: mount
BuildArch: noarch

%description
RPM helper to make kernel and modules readable by user.

%prep
%setup

%install
install -D -p -m 0755 filetrigger %buildroot%_rpmlibdir/%name.filetrigger

%files
%_rpmlibdir/%name.filetrigger

%pre
# Only allow to install inside of hasher.
[ -d /.host -a -d /.in -a -d /.out ] || {
	echo >&2 '%name is not allowed outside hasher environments'
	exit 1
}

%post
# Fix permissions to boot the installed kernel
find /boot /lib/modules -type f,d \! -perm -444 -print0 | xargs -0r chmod a+rX
chmod a+rwx /lib/modules/*/
control mount unprivileged

%changelog
* Mon Mar 15 2021 Vitaly Chikunov <vt@altlinux.org> 1.3-alt1
- Fix mount and extra/ permissions.

* Mon Mar 15 2021 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- Use filetrigger to fix kernel permissions.

* Mon Oct 15 2018 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- Requires mount

* Tue Jun 05 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0-alt1
- First version.
