Name: shellinabox
Version: 2.20
Release: alt1

Summary: AJAX based terminal emulator exporting a console to the browser
License: GPLv2
Group: Networking/Remote access

Url: https://github.com/shellinabox/shellinabox
Source0: %name-%version.tar
Source1: shellinabox.conf
Source2: shellinaboxd.init.in
Source3: shellinaboxd.service
Patch1:  shellinabox-ssh-options.patch

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: zlib-devel openssl-devel

%define runas _shellinaboxd

%description
Shell In A Box implements a web server that can export arbitrary command
line tools to a web based terminal emulator. This emulator is accessible
to any JavaScript and CSS enabled web browser and does not require any
additional browser plugins.

All client-server communications are encrypted, if SSL/TLS certificates
have been installed.

More details are available in the manual page; for configuration,
see also /etc/sysconfig/shellinaboxd (localhost only by default).

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure --bindir=%_sbindir \
	   --disable-runtime-loading
%make_build

%install
%makeinstall_std
rm -r %buildroot/usr/share/doc
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/shellinaboxd
install -pDm755 /dev/null %buildroot%_initdir/shellinaboxd
sed 's/%%runas/%runas/' < %SOURCE2 > %buildroot%_initdir/shellinaboxd
install -pDm644 %SOURCE3 %buildroot%_unitdir/shellinaboxd.service
mkdir -p %buildroot%_datadir/%name
cp shellinabox/*.css %buildroot%_datadir/%name
mkdir -p %buildroot%_localstatedir/%name

%pre
/usr/sbin/groupadd -r -f %runas
/usr/sbin/useradd -r -g %runas -d / -s /dev/null \
	-c "Shell in a Box" -n %runas >/dev/null 2>&1 ||:

%post
%post_service shellinaboxd

%preun
%preun_service shellinaboxd

%files
%doc AUTHORS ChangeLog COPYING GPL-2 NEWS README.md
%doc shellinabox/monochrome.css shellinabox/color.css
%doc shellinabox/black-on-white.css shellinabox/white-on-black.css
%doc demo
%_man1dir/shellinaboxd.1*
%_sbindir/shellinaboxd
%_datadir/%name
%config(noreplace) %_sysconfdir/sysconfig/shellinaboxd
%_initdir/shellinaboxd
%_unitdir/shellinaboxd.service
%attr(750,%runas,%runas) %_localstatedir/%name

%changelog
* Wed Jan 01 2020 Andrey Cherepanov <cas@altlinux.org> 2.20-alt1
- New version (ALT #37711).
- Build from upstream git tag.

* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 2.14-alt1
- 2.14

* Mon Feb 14 2011 Michael Shigorin <mike@altlinux.org> 2.10-alt1
- initial build for ALT Linux Sisyphus

* Sun Sep 12 2010 Jochen Wiedmann <jochen.wiedmann@gmail.com> - 2.10-2
- Review by Martin Gieseking, see
  https://bugzilla.redhat.com/show_bug.cgi?id=619228#c1

* Thu Jul 29 2010 Jochen Wiedmann <jochen.wiedmann@gmail.com> - 2.10-1
- Initial build.
