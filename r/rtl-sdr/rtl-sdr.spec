Name: rtl-sdr
Url: http://sdr.osmocom.org/trac/wiki/rtl-sdr
Version: 0.6.0
Release: alt2
License: GPLv2+
Group: Communications
Summary: SDR utilities for Realtek RTL2832 based DVB-T dongles
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

Requires(pre): shadow-utils
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake libusb-devel

%description
This package can turn your RTL2832 based DVB-T dongle into a SDR receiver.

%package devel
Summary: Development files for rtl-sdr
Group: Communications
Requires: %name = %version-%release

%description devel
Development files for rtl-sdr.

%prep
%setup
rm -f src/getopt/*
rmdir src/getopt

%build
%cmake -DDETACH_KERNEL_DRIVER=ON
%cmake_build

%install
%cmakeinstall_std

# remove static libs
rm -f %buildroot%_libdir/*.a

# Fix udev rules and allow access only to users in rtlsdr group
%__subst 's/MODE:="0666"/GROUP:="rtlsdr", MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' rtl-sdr.rules
install -Dpm 644 rtl-sdr.rules %buildroot%_udevrulesdir/10-rtl-sdr.rules

%pre
getent group rtlsdr >/dev/null || \
%_sbindir/groupadd -r rtlsdr >/dev/null 2>&1
exit 0

%files
%doc AUTHORS COPYING
%_bindir/*
%_libdir/*.so.*
%_udevrulesdir/10-rtl-sdr.rules

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Nov 23 2020 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt2
- Fix Requires (Closes: 39334)

* Tue Dec 25 2018 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- New version 0.6.0

* Mon Oct 30 2017 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt2.20170920.1
- Replace 10-rtl-sdr.rules to _udevrulesdir

* Wed Oct 18 2017 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt1.20170920.1
- Initial build for ALT Sisyphus.
