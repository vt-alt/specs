%define _unpackaged_files_terminate_build 1

Name: sane-airscan
Version: 0.99.8
Release: alt1.20200709.git8bba080

Summary: This package contains SANE backend for AirScan (eSCL) and WSD document scanners

License: GPLv2
Group: Graphics
Url: https://github.com/alexpevzner/sane-airscan
#Git: https://github.com/alexpevzner/sane-airscan.git

Source: %name-%version.tar

Patch0: %name-%version-%release.patch

BuildRequires: meson
BuildRequires: libavahi-glib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libsane-devel
BuildRequires: libsoup-devel >= 2.4
BuildRequires: libxml2-devel

%description
Similar to how most modern network printers support "driverless" printing, using
the universal vendor-neutral printing protocol, many modern network scanners and
MFPs support "driverless" scanning.

Driverless scanning comes in two flavors:

    Apple AirScan or AirPrint scanning (official protocol name is eSCL)
    Microsoft WSD, or WS-Scan (term WSD means "Web Services for Devices)

This backend implements both protocols, choosing automatically between them. It
was successfully tested with many devices from Brother, Canon, Kyocera, Lexmark,
Epson, HP, Ricoh, Samsung and Xerox both in WSD and eSCL modes.

For eSCL devices, Apple maintains a comprehensive list of compatible devices,
but please note, this list contains not only scanners and MFP, but pure printers
as well.

This backend doesn't require to install and doesn't conflict with
vendor-provided proprietary software like ScanGear from Canon, HPLIP from HP and
so on.

%prep
%setup
%patch0 -p1

%build
mkdir -p ./BUILD
meson ./BUILD
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%config(noreplace) %_sysconfdir/sane.d/*.conf
%config(noreplace) %_sysconfdir/sane.d/dll.d/*
%_libdir/sane/libsane-airscan.so.*
%_man1dir/*.1.xz
%_man5dir/*.5.xz

%changelog
* Fri Jul 10 2020 Nikolai Kostrigin <nickel@altlinux.org> 0.99.8-alt1.20200709.git8bba080
- initial build for Sisyphus

