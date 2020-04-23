Name: udev-rules-rfkill-uaccess
Version: 1.0
Release: alt1
Summary: Get access to /dev/rfkill for users
License: GPL-2.0-or-later
Group: System/Configuration/Hardware

BuildArch: noarch

%description
Get access to /dev/rfkill for users
See https://bugzilla.redhat.com/show_bug.cgi?id=514798

Simplified by Kay Sievers
https://bugzilla.redhat.com/show_bug.cgi?id=733326
See also https://bugzilla.gnome.org/show_bug.cgi?id=711373

%install
mkdir -p %buildroot%_udevrulesdir

cat > %buildroot%_udevrulesdir/61-rfkill-uaccess.rules <<EOF
# Get access to /dev/rfkill for users
# See https://bugzilla.redhat.com/show_bug.cgi?id=514798
#
# Simplified by Kay Sievers
# https://bugzilla.redhat.com/show_bug.cgi?id=733326
# See also https://bugzilla.gnome.org/show_bug.cgi?id=711373

KERNEL=="rfkill", SUBSYSTEM=="misc", TAG+="uaccess"
EOF

%files
%_udevrulesdir/61-rfkill-uaccess.rules

%changelog
* Fri Apr 17 2020 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- Initial build
