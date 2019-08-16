Name: kmscon
Version: 8
Release: alt4.40.g01dd0a2
Summary: KMS/DRM based System Console
Group: Terminals

License: MIT and LGPLv2+
Url: http://www.freedesktop.org/wiki/Software/kmscon/
Source: %name-%version.tar
Patch1: %name-%version.patch

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libtsm) >= 4.0.0
BuildRequires: pkgconfig(libudev) >= 172
BuildRequires: pkgconfig(libdrm)
BuildRequires: libsystemd-devel pkgconfig(libsystemd)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(pango) pkgconfig(pangoft2)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: xsltproc docbook-style-xsl docbook-dtds

%description
Kmscon is a simple terminal emulator based on Linux kernel mode setting (KMS).
It is an attempt to replace the in-kernel VT implementation with a user-space
console. See kmscon(1) man-page for usage information.

%prep
%setup
%patch1 -p1

%build
mkdir -p m4
%autoreconf
%configure \
	--disable-static \
	--disable-silent-rules \

%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/%name/mod-*.la

# Install systemd services
mkdir -p %buildroot%_unitdir
install -pm 0644 docs/kmscon.service %buildroot%_unitdir
install -pm 0644 docs/kmsconvt@.service %buildroot%_unitdir

%check
%make check

%files
%doc COPYING NEWS README
%_bindir/%name
%_unitdir/*.service
%dir %_libdir/%name
%_libdir/%name/mod-*.so
%dir %_libexecdir/kmscon
%_libexecdir/kmscon/kmscon
%_man1dir/%name.1*

%changelog
* Thu Aug 15 2019 Alexey Shabalin <shaba@altlinux.org> 8-alt4.40.g01dd0a2
- disable post/preun scripts

* Thu Aug 01 2019 Alexey Shabalin <shaba@altlinux.org> 8-alt3.40.g01dd0a2
- Update to git snapshot 01dd0a2

* Tue Jan 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8-alt2
- Fixed build with new systemd and glibc.

* Tue Jun 17 2014 Alexey Shabalin <shaba@altlinux.ru> 8-alt1
- initial build
