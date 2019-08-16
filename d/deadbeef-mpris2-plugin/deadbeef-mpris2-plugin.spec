# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     deadbeef-mpris2-plugin
Version:  1.13
Release:  alt1

Summary:  A rewrite of the seemingly orphaned deadbeef-mpris-plugin originally written by HuangCongyu
License:  GPL-2.0
Group:    Sound
Url:      https://github.com/Serranya/deadbeef-mpris2-plugin

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires: glib2-devel libgio-devel deadbeef-devel
Requires: deadbeef

%description
%summary

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

# remove static library
rm -f %buildroot%_libdir/deadbeef/*.la

%files
%doc README LICENSE
%_libdir/deadbeef/mpris.so

%changelog
* Fri Aug 16 2019 Anton Midyukov <antohami@altlinux.org> 1.13-alt1
- new version 1.13

* Wed May 08 2019 Anton Midyukov <antohami@altlinux.org> 1.12-alt1
- Initial build for Sisyphus
