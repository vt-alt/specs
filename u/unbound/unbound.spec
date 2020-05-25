%def_disable static

Name: unbound
Version: 1.10.2
Release: alt1
License: BSD
Url: http://unbound.net/
Source: %name-%version.tar
Summary: Validating, recursive, and caching DNS resolver
Group: System/Servers

%define _chrootdir %_localstatedir/%name
%define with_python 0

Requires(pre): chrooted
Requires(pre): lib%name = %version-%release

Provides: %name-chroot(%_chrootdir)

BuildRequires: /proc flex gcc-c++ libssl-devel libexpat-devel libevent-devel
BuildRequires: pkgconfig(libsystemd)
%if %with_python == 2
BuildRequires: python-devel swig
%endif
%if %with_python == 3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel swig
%endif

%description
Unbound is a validating, recursive, and caching DNS resolver.

The C implementation of Unbound is developed and maintained by NLnet
Labs. It is based on ideas and algorithms taken from a java prototype
developed by Verisign labs, Nominet, Kirei and ep.net.

Unbound is designed as a set of modular components, so that also
DNSSEC (secure DNS) validation and stub-resolvers (that do not run
as a server, but are linked into an application) are easily possible.

%package control
Summary: Unbound remote server control
Group: System/Configuration/Other

%description control
Unbound-control performs remote administration on  the  unbound(8)  DNS
server.   It  reads the configuration file, contacts the unbound server
over SSL sends the command and displays the result.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
This package contains shared libraries used by %name's daemons
and clients.

%package -n lib%name-devel-static
Summary: Static library for %name
Group: System/Libraries
Obsoletes: lib%name-static

%description -n lib%name-devel-static
This package contains static libraries used by %name's daemons
and clients.

%package -n lib%name-devel
Summary: Development package that includes the %name header files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The devel package contains the include files

%if %with_python == 2
%package -n python-module-%name
Summary: Python modules and extensions for unbound
Group: Development/Python

%description -n python-module-%name
Python modules and extensions for unbound
%endif

%if %with_python == 3
%package -n python3-module-%name
Summary: Python3 modules and extensions for unbound
Group: Development/Python3

%description -n python3-module-%name
Python3 modules and extensions for unbound
%endif

%prep
%setup

%build
# configure with /var/unbound/unbound.conf so that all default chroot,
# pidfile and config file are in /var/unbound, ready for chroot jail set up.
#
# This is a build using libldns builtin version, the resulting binaries
# do not require libldns and this package does not have version dependencies.
# Could be smaller using a dependency on libldns (use --with-ldns=).
%autoreconf

%configure \
	    %{subst_enable static} \
	    --enable-pie \
	    --enable-relro-now \
	    --disable-rpath \
	    --with-pthreads \
	    --with-conf-file=%_chrootdir/unbound.conf \
	    --with-pidfile=/run/%name/%name.pid \
	    --with-username=_%name \
	    --enable-systemd \
	    --with-libevent \
	    --with-ssl \
	    --enable-subnet \
	    --enable-tfo-client \
	    --enable-tfo-server \
%if %with_python
	    PYTHON_VERSION=%with_python \
	    --with-pythonmodule --with-pyunbound \
%endif
	    --enable-sha2
%make

subst 's|# auto-trust-anchor-file:|auto-trust-anchor-file:|g' doc/example.conf

%install
%make DESTDIR=%buildroot install
install -d -m 0775 %buildroot%_localstatedir/%name
install -d -m 0755 %buildroot%_initdir
install -d -m 0755 %buildroot%_sysconfdir/cron.d
install -m 0755 %name.init %buildroot%_initdir/unbound
install -p -m 0644 unbound.cron.d  %buildroot%_sysconfdir/cron.d/unbound-anchor
install -p -m 0644 icannbundle.pem %buildroot%_localstatedir/%name/icannbundle.pem
# add symbolic link from /etc/unbound/unbound.conf -> /var/lib/unbound/unbound.conf
ln -s ..%_chrootdir %buildroot%_sysconfdir/%name

#systemd services
install -D -p -m 0644 contrib/unbound.service %buildroot%_unitdir/unbound.service
install -D -p -m 0644 unbound-keygen.service %buildroot%_unitdir/unbound-keygen.service
install -D -p -m 0644 unbound-anchor.service %buildroot%_unitdir/unbound-anchor.service
install -D -p -m 0644 unbound-anchor.timer %buildroot%_unitdir/unbound-anchor.timer

# Install tmpfiles.d config
install -D -m 0644 tmpfiles-unbound.conf %buildroot%_tmpfilesdir/unbound.conf

# Install directories for easier config file drop in
mkdir -p %buildroot%_chrootdir/{keys.d,conf.d,local.d}
install -p example.com.key %buildroot%_chrootdir/keys.d/
install -p example.com.conf %buildroot%_chrootdir/conf.d/
install -p block-example.com.conf %buildroot%_chrootdir/local.d/
touch %buildroot%_chrootdir/root.key

%if %with_python
rm -f %buildroot%python_sitelibdir/*.la
rm -f %buildroot%python3_sitelibdir/*.la
%endif

%check
%make check

%pre -n lib%name
/usr/sbin/groupadd -r -f _%name
/usr/sbin/useradd -r -g _%name -d %_chrootdir -s /dev/null -n -c "Domain Name Server" _%name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name
%files
%doc doc/README doc/CREDITS doc/LICENSE doc/FEATURES doc/Changelog
%_initdir/%name
%_unitdir/unbound.service
%_unitdir/unbound-keygen.service
%_tmpfilesdir/*
%config(noreplace) %_chrootdir/unbound.conf
%attr(0755,root,_%name) %dir %_chrootdir/keys.d
%attr(0755,root,_%name) %dir %_chrootdir/conf.d
%attr(0755,root,_%name) %dir %_chrootdir/local.d
%attr(0664,root,_%name) %config(noreplace) %_chrootdir/keys.d/*.key
%attr(0664,root,_%name) %config(noreplace) %_chrootdir/conf.d/*.conf
%attr(0664,root,_%name) %config(noreplace) %_chrootdir/local.d/*.conf
%_sysconfdir/%name
%_sbindir/*
%_man1dir/*
%_man5dir/*
%_man8dir/*


%exclude %_sbindir/unbound-anchor
%exclude %_sbindir/unbound-control
%exclude %_man8dir/unbound-control.8.*
%exclude %_man8dir/unbound-anchor*

%files control
%_sbindir/unbound-control
%_man8dir/unbound-control.8.*

%files -n lib%name
%attr(1775,root,_%name) %dir %_localstatedir/%name
%attr(644,_%name,_%name) %ghost %_chrootdir/root.key
%config(noreplace) %_sysconfdir/cron.d/unbound-anchor
%_unitdir/unbound-anchor.service
%_unitdir/unbound-anchor.timer
%config(noreplace) %_localstatedir/%name/icannbundle.pem
%_libdir/libunbound*so.*
%exclude %_libdir/libunbound.so
%_sbindir/unbound-anchor
%_man8dir/unbound-anchor*
%_man3dir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/libunbound.a
%endif

%files -n lib%name-devel
%_includedir/*
%_libdir/libunbound.so
%_libdir/pkgconfig/*

%if %with_python == 2
%files -n python-module-%name
%python_sitelibdir/*
%doc libunbound/python/examples/*
%doc pythonmod/examples/*
%endif

%if %with_python == 3
%files -n python3-module-%name
%python3_sitelibdir/*
%doc libunbound/python/examples/*
%doc pythonmod/examples/*
%endif

%changelog
* Fri May 22 2020 Alexei Takaseev <taf@altlinux.org> 1.10.2-alt1
- 1.10.2
- (Fixes CVE-2020-12662, CVE-2020-12663)

* Tue Feb 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.9.6-alt3
- update systemd unit for run without pidfile

* Tue Feb 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.9.6-alt2
- build unbound without python
- build with systemd support
- update unbound-anchor cron config
- add unbound-anchor.timer
- disable build static libs
- update configure options:
  + --enable-pie
  + --enable-relro-now
  + --disable-rpath
  + --with-ssl
  + --enable-tfo-client
  + --enable-tfo-server
  + --enable-subnet
- cleanup BR:

* Fri Dec 13 2019 Alexei Takaseev <taf@altlinux.org> 1.9.6-alt1
- 1.9.6 (Fixes CVE-2019-18934)

* Fri Oct 04 2019 Alexei Takaseev <taf@altlinux.org> 1.9.4-alt1
- 1.9.4 (Fixes CVE-2019-16866)

* Thu Aug 29 2019 Alexei Takaseev <taf@altlinux.org> 1.9.3-alt1
- 1.9.3

* Mon Jun 17 2019 Alexei Takaseev <taf@altlinux.org> 1.9.2-alt1
- 1.9.2

* Thu Mar 14 2019 Alexei Takaseev <taf@altlinux.org> 1.9.1-alt1
- 1.9.1

* Thu Feb 07 2019 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt1
- 1.9.0

* Wed Dec 12 2018 Alexei Takaseev <taf@altlinux.org> 1.8.3-alt1
- 1.8.3

* Wed Dec 05 2018 Alexei Takaseev <taf@altlinux.org> 1.8.2-alt1
- 1.8.2

* Fri Nov 02 2018 Andrey Savchenko <bircoph@altlinux.org> 1.8.1-alt2
- Set proper anchor file permissions in the cron job, otherwise
  unbound will on run-time fail because it can't update theanchor
  after a cron job run.

* Tue Oct 09 2018 Alexei Takaseev <taf@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Sep 11 2018 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt1
- 1.8.0

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.7.3-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Jun 22 2018 Alexei Takaseev <taf@altlinux.org> 1.7.3-alt1
- 1.7.3

* Wed Jun 13 2018 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt1
- 1.7.2

* Thu Jun 07 2018 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt2
- Fix permission to /var/lib/unbound/root.key (ALT#35001)
- Move create _unbound user to libunbound subpackage

* Fri May 04 2018 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt1
- 1.7.1

* Fri Mar 23 2018 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt1
- 1.7.0
- New version (closes: #34122)
- Add lost libunbound.so and libunbound.pc to libunbound-devel
- Set libunbound-devel arch-depended
- Move unbound-control-setup.8 from unbound-control to unbound
- Fixed CVE-2017-15105

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.10-alt1
- New version

* Wed Jun 29 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.9-alt1
- New version, see Changelog
- Removed /sbin/restorecon (not real, something old) from unbound-keygen.service

* Tue May 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.8-alt2
- Added Changelog file (ALT 32079)

* Fri May 06 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.8-alt1
- New version, see Changelog

* Mon Feb 29 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.7-alt1
- New version, see Changelog

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.4-alt1
- New version, see Changelog

* Mon Apr 27 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.3-alt1
- New version, see Changelog

* Thu Dec 18 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.1-alt1
- New version, see Changelog

* Tue Nov 04 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.22-alt1
- New version, see Changelog

* Sat Nov 01 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.21-alt2
- Some repocop warning fixed, taked package also

* Mon Oct 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.21-alt1
- 1.4.21

* Mon Aug 05 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.20-alt1
- 1.4.20
- Add support for systemd. Fixed (ALT #26351) in case if started by systemd
- Add addon folders %_chrootdir/{keys.d,conf.d,local.d}
- Move link /etc/unbound.conf to /etc/unbound/unbound.conf

* Sat Feb 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.19-alt1
- 1.4.19
- Move %_sbindir/unbound-anchor to lib%name subpackage
- Add %_sysconfdir/cron.monthly/unbound-anchor
- Add %_localstatedir/%name/icannbundle.pem

* Wed Sep 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.18-alt1
- 1.4.18

* Sun Jul 08 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.17-alt1
- 1.4.17

* Fri Feb 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.16-alt1
- 1.4.16

* Fri Dec 23 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.14-alt1
- 1.4.14
- Fix for VU#209659 CVE-2011-4528

* Thu Sep 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.13-alt1
- 1.4.13
- Add python-module-unbound subpackage

* Fri Jul 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.12-alt1
- 1.4.12

* Sun Jul 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.11-alt1
- 1.4.11

* Wed Jun 01 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.10-alt1
- 1.4.10
- Fix assertion failure when unbound generates an empty error reply
  in response to a query, CVE-2011-1922 VU#531342

* Sat Apr 16 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.9-alt1
- 1.4.9

* Mon Feb 07 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.8-alt4
- Rebuild with new libevent
- Fix init script
- Make devel subpackage noarch

* Thu Feb 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.8-alt3
- Use libevent1.4
- Fix init script

* Thu Feb 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.8-alt2
- Fix init script

* Thu Feb 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.8-alt1
- 1.4.8
- Build with libevent
- Update init for run unbound-anchor
- Enable by default auto-trust-anchor-file for DNSSEC

* Sat Nov 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.7-alt1
- 1.4.7

* Fri Aug 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.6-alt1
- 1.4.6
- Add make test and update BuildRequires

* Tue Jun 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.5-alt1
- 1.4.5

* Fri May 14 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.4-alt1
- 1.4.4

* Sun Apr 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.3-alt1
- 1.4.3

* Sun Jan 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Dec 14 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed Nov 18 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.4-alt1
- 1.3.4

* Sat Aug 15 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Jun 16 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.0-alt1
- 1.3.0

* Thu Mar 26 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.1-alt1
- 1.2.1
- Build without --enable-debug

* Thu Nov 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt2
- Rename subpackage lib%name-static to lib%name-devel-static (http://www.altlinux.org/Drafts/SharedLibs)

* Mon Sep 15 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.2-alt1
- New version

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.1-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Thu Aug 07 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.1-alt1
- This version features bugfixes, a couple of fixes for looking up corner cases
  (badly operated domains), and a cleanup of code for config file reading.

* Fri May 30 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.0-alt2
- Change owner of %_localstatedir/%name to root and add sticky bit
- Change default username to _%name

* Sun May 25 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.0-alt1
- Build for ALT
