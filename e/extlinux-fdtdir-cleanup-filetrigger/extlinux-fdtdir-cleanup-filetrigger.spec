%define ftrigger extlinux-fdtdir-cleanup.filetrigger

Name: extlinux-fdtdir-cleanup-filetrigger
Version: 0.1
Release: alt1
Summary: Clear lines containing the word ftdir in /boot/extlinux/extlinux.conf
License: GPL-3.0-or-later
Group: System/Configuration/Boot and Init
Url: https://altlinux.org
BuildArch: noarch

%description
%summary

%install
mkdir -p %buildroot%_rpmlibdir
cat>%buildroot%_rpmlibdir/%ftrigger<<END
#!/bin/sh
LC_ALL=C egrep -qs "^/boot/vmlinuz" || exit 0
[ -f /boot/extlinux/extlinux.conf ] || exit 0

sed -i '/fdtdir/d' /boot/extlinux/extlinux.conf 2>/dev/null
END
chmod +x %buildroot%_rpmlibdir/%ftrigger

%files
%_rpmlibdir/%ftrigger

%changelog
* Mon Jul 13 2020 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
