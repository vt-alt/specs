%define _unpackaged_files_terminate_build 1

%define service_name loolwsd
%define service_user lool
%define default_loroot %_libdir/LibreOffice
%define loolparent %_localstatedir

%ifarch ppc64le
%define __nprocs 32
%endif

Name: libreoffice-online
Version: 6.2.3.2
Release: alt4
Summary: LibreOffice Online WebSocket Daemon
License: MPL-2.0
Group: Office
Url: https://www.libreoffice.org/download/libreoffice-online/

# https://git.libreoffice.org/online
Source0: %name-%version.tar
Source1: node_modules-%version.tar
Source2: %service_name.init
Source3: %name.conf.nginx
Source4: %name.conf.apache2

Patch1: remove-rpath.patch
Patch2: disable-copying-libs.patch
Patch3: fix-conf-dir.patch
Patch4: ru-translation.patch
Patch5: loleaflet-makefile.patch
Patch6: skip-installing-http-configs.patch
Patch7: alt-systemd-service.patch
Patch8: alt-use-hash-directory.patch
Patch9: alt-gcc-compat.patch
Patch10: alt-python2-compat.patch
Patch11: alt-32bit-build.patch
Patch12: alt-fix-build-poco-1.10.1.patch

Requires: LibreOffice python3 fonts-ttf-core

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libtool automake npm libcap-utils fontconfig
BuildRequires: libpoco-devel libpng-devel libcap-devel cppunit-devel
BuildRequires: pam-devel libpcre-devel
BuildRequires: python-module-polib python-module-lxml

%description
This is LibreOffice Online, which provides basic collaborative editing of
documents in a browser by re-using the LibreOffice core.
Rendering fidelity should be excellent,
and interoperability match that of LibreOffice.

%package nginx
Summary: nginx web-server default configuration for %name
Group: Networking/WWW
BuildArch: noarch
Requires: %name = %EVR
Requires: nginx

%description nginx
nginx web-server default configuration for %name.

%package apache2
Summary: Apache 2.x web-server default configuration for %name
Group: Networking/WWW
BuildArch: noarch
Requires: %name = %EVR
Requires: apache2
Requires: apache2-mods
Requires: apache2-mod_ssl

%description apache2
Apache 2.x web-server default configuration for %name.

%prep
%setup -a1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%ifarch ppc64le
# ppc64le misses following definition
%add_optflags -D__linux=1
%endif

%autoreconf
%configure \
	--with-lokit-path=bundled/include \
	--disable-setcap \
	--with-lo-path=%default_loroot \
	--localstatedir=%_var \
%ifnarch x86_64
	--disable-seccomp \
%endif
	%nil

%make_build

%install
%makeinstall_std

install -D -m 644 %service_name.service %buildroot%_unitdir/%service_name.service
install -D -m 755 %SOURCE2 %buildroot%_initdir/%service_name

install -d -m 755 %buildroot%_var/adm/fillup-templates
install -d -m 755 %buildroot%_cachedir/%name
install -d -m 755 %buildroot%loolparent/%service_user/child-roots 
install -d -m 755 %buildroot%loolparent/%service_user/systemplate
install -D -m 644 sysconfig.%service_name %buildroot%_sysconfdir/sysconfig/%service_name

mkdir -p %buildroot%_sysconfdir/cron.d
echo "#Remove old tiles once every 10 days at midnight" > %buildroot%_sysconfdir/cron.d/%service_name.cron
echo "0 0 */1 * * root find %_cachedir/%name -name \"*.png\" -a -atime +10 -exec rm {} \;" >> %buildroot%_sysconfdir/cron.d/%service_name.cron

mkdir -p %buildroot%_sysconfdir/pam.d
echo "auth       required     pam_unix.so" > %buildroot%_sysconfdir/pam.d/%service_name
echo "account    required     pam_unix.so" >>  %buildroot%_sysconfdir/pam.d/%service_name

install -pD -m0644 %SOURCE3 %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf
install -pD -m0644 %SOURCE4 %buildroot%_sysconfdir/httpd2/conf/sites-available/%name.conf

install -pD -m0644 etc/*.pem %buildroot%_sysconfdir/%name/

ln -s dist %buildroot%_datadir/%name/loleaflet/$(echo %version | cut -d . -f 1-3)

cp etc/apache2/loolwsd.conf loolwsd.apache2.conf
cp etc/nginx/loolwsd.conf loolwsd.nginx.conf

mv %buildroot%_defaultdocdir/%name ./%{name}-doc

%pre
getent group %service_user >/dev/null || groupadd -r %service_user
getent passwd %service_user >/dev/null || useradd -g %service_user -r %service_user -d %loolparent/%service_user -s /bin/bash

%post
rm -rf %_cachedir/%name/*
rm -rf %loolparent/%service_user/child-roots/*

%post_service %service_name

%preun
%preun_service %service_name

%post apache2
a2ensite %name
a2enmod ssl
a2enport https
a2enmod rewrite
a2enmod env
a2enmod headers
%_initdir/httpd2 condreload

%postun apache2
%_initdir/httpd2 condreload

%files
%doc COPYING
%doc AUTHORS ChangeLog README NEWS PROBLEMS
%doc %{name}-doc
%_bindir/*
%_datadir/%name
%_man1dir/*
%dir %_sysconfdir/%name/
%config(noreplace) %attr(640, %service_user, root) %_sysconfdir/%name/%service_name.xml
%config(noreplace) %_sysconfdir/%name/loolkitconfig.xcu
%config(noreplace) %attr(640,%service_user, root) %_sysconfdir/%name/*.pem
%config(noreplace) %_sysconfdir/sysconfig/%service_name
%config(noreplace) %_sysconfdir/cron.d/%service_name.cron
%config(noreplace) %_sysconfdir/pam.d/%service_name
%_initdir/%service_name
%_unitdir/%service_name.service
%dir %attr(-,%service_user,%service_user) %loolparent/%service_user
%dir %attr(-,%service_user,%service_user) %loolparent/%service_user/child-roots
%dir %attr(-,%service_user,%service_user) %loolparent/%service_user/systemplate
%dir %attr(-,%service_user,%service_user) %_cachedir/%name

%files nginx
%doc loolwsd.nginx.conf
%config(noreplace) %attr(0644,root,root) %_sysconfdir/nginx/sites-available.d/%name.conf

%files apache2
%doc loolwsd.apache2.conf
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/sites-available/%name.conf

%changelog
* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.3.2-alt4
- Updated build dependencies.

* Thu Mar 05 2020 Alexei Takaseev <taf@altlinux.org> 6.2.3.2-alt3
- Fix build with poco 1.10.1

* Wed Mar 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.3.2-alt2
- Fixed build on p9 for ppc64le.

* Wed Mar 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.3.2-alt1
- Updated to upstream version 6.2.3.2.

* Wed Aug 21 2019 Alexei Takaseev <taf@altlinux.org> 6.0.2.3-alt3.1
- Fix build (race-condition on ppc64le)

* Tue Feb 05 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.2.3-alt3
- NMU: fixed build.

* Thu Sep 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.2.3-alt2
- NMU: rebuilt with openssl 1.1.

* Wed Apr 18 2018 Maxim Voronov <mvoronov@altlinux.org> 6.0.2.3-alt1
- initial build for ALT

