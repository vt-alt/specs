Name:     mod_clamav
Version:  0.14
Release:  alt1.1e555d35

Summary:  Mod_Clamav for ProFTPd
License:  GPL
Group:    System/Servers
Url:      https://github.com/jbenden/mod_clamav

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires: proftpd-devel

Requires: proftpd

%description
%summary

%prep
%setup

%build
prxs -c mod_clamav.c

%install
mkdir -p %buildroot%_libdir/proftpd
install -m 644 .libs/mod_clamav.so %buildroot%_libdir/proftpd

%files
%doc README.md
%_libdir/proftpd/mod_clamav.so

%changelog
* Thu May 28 2020 Anton Midyukov <antohami@altlinux.org> 0.14-alt1.1e555d35
- Initial build
