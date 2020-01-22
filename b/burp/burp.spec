Name:		burp
Version:	2.3.16
Release:	alt2

Summary:	Burp is a network-based backup and restore program
License:	AGPL-3.0 and BSD and GPLv2+ and LGPLv2+
Group:		Archiving/Backup
Url:		https://burp.grke.org/

# https://github.com/grke/burp.git master
Source:		%{name}-%{version}.tar
Patch:		%{name}-%{version}-%{release}.patch

BuildRequires:  libtool
BuildRequires:  librsync-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  libncurses-devel
BuildRequires:  libacl-devel
BuildRequires:  libuthash-devel
BuildRequires:  libyajl-devel
BuildRequires:  check libcheck-devel
BuildRequires:  libcap-devel
BuildRequires:  openssl

BuildRequires: rpm-macros-intro-conflicts
%filter_from_requires /^\/usr\/local\/bin\/mail\.php$/d

%description
Burp is a network backup and restore program, using client and server.
It uses librsync in order to save network traffic and to save on the
amount of space that is used by each backup.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    --sysconfdir="%_sysconfdir/burp" \
    --disable-static

%make_build

%install
%makeinstall_std install-all
install -D -p -m 0755 .gear/burp.init %{buildroot}%{_initrddir}/burp-server
install -D -p -m 0644 .gear/burp.service %{buildroot}%{_unitdir}/burp-server.service
%__subst "s,password,#password,g" %{buildroot}%_sysconfdir/burp/clientconfdir/testclient

%check
%make_build check
.gear/test-burp.sh

%files
%doc %_docdir/%name/
%{_initrddir}/burp-server
%{_unitdir}/burp-*.*
%dir %_datadir/%name/
%_datadir/%name/scripts/
%_bindir/vss_strip
%_sbindir/*
%_man8dir/*
%defattr(640,root,_burp,3770)
%dir %_sysconfdir/burp/
%dir %_sysconfdir/burp/CA-client/
%dir %_sysconfdir/burp/clientconfdir/
%dir %_sysconfdir/burp/clientconfdir/incexc/
%config(noreplace) %_sysconfdir/burp/*.c*nf
%config(noreplace) %_sysconfdir/burp/clientconfdir/testclient
%config(noreplace) %_sysconfdir/burp/clientconfdir/incexc/example

%pre
/usr/sbin/groupadd -r -f _burp
/usr/sbin/useradd -r -g _burp -d /var/empty -s /dev/null -n -c "BURP BackUp and Restore Program" _burp >/dev/null 2>&1 ||:

%post
%post_service burp-server

%preun
%preun_service burp-server

%changelog
* Fri Dec 06 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.16-alt2
- Adjust chkconfig runlevels so that server isn't enabled by default
- Make _burp:_burp user and configs owned by root:_burp
- Fix setgid if group= is not specified
- Add small functionality test

* Mon Nov 25 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.16-alt1
- New version 2.3.16
- Fix license string
- Fix compatibility with openssl-1.1.1
- Implement support of keeping readall capabilities

* Tue Oct 01 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.14-alt1
- New version 2.3.14

* Wed Apr 03 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.4-alt1
- New version 2.3.4

* Fri Mar 15 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.2-alt1
- new version 2.3.2

* Wed Feb 20 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.0-alt1
- Update to 2.3.0-12-g3d093f25

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.2.4-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jun 06 2018 Vitaly Chikunov <vt@altlinux.org> 2.2.4-alt1
- Update to version 2.2.4

* Thu Apr 19 2018 Vitaly Chikunov <vt@altlinux.org> 2.1.32-alt2
- Fix init script
- Secure permissions for configs that supposed to contain passwords

* Sun Apr 15 2018 Vitaly Chikunov <vt@altlinux.org> 2.1.32-alt1
- Respec for 2.1.32
- Install init scripts

* Tue Dec 05 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.24-alt1
- new version 2.1.24 (with rpmrb script)

* Wed Aug 10 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0.44-alt1
- initial build for ALT Linux Sisyphus

