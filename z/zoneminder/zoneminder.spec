%define zmuid_final apache2
%define zmgid_final _webserver

Name: zoneminder
Version: 1.34.1
Release: alt1
Summary: A camera monitoring and analysis tool
Group: System/Servers 
License: GPLv2
Url: http://www.zoneminder.com
Source: %name-%version-alt.tar
Source1: Crud-%version.tar
Source2: CakePHP-Enum-Behavior-%version.tar
Source3: zoneminder.conf
Source4: README.alt
Source5: README-nginx-ru.alt
Source6: nginx-zoneminder.conf.sample
Source7: zm-fcgi.inc
Patch1: zoneminder-1.32.3-alt-mysql8-transition.patch

Conflicts: zm <= 1.22.3
Requires: libgnutls libgnutls-openssl zlib perl-Class-Date perl-DateTime perl-Date-Manip perl-libwww ffmpeg perl-X10 perl-Sys-Mmap perl-DBD-mysql perl-Storable php7-pdo_mysql php7-openssl su perl-Data-Entropy perl-Crypt-Eksblowfish perl-Sys-Mmap webserver perl-Pod-Usage perl-Sys-MemInfo perl-Number-Bytes-Human perl-JSON-MaybeXS perl-Sys-CPU
Requires: perl-SOAP-WSDL perl-Class-Std-Fast perl-Data-UUID perl-IO-Socket-Multicast
AutoReq: noperl
BuildRequires: bzlib-devel ffmpeg gcc-c++ libavresample-devel libswresample-devel libavdevice-devel libavformat-devel libgcrypt-devel libgnutls-openssl-devel libjpeg-devel libmysqlclient-devel libpcre-devel libswscale-devel netpbm perl-Archive-Tar perl-Archive-Zip perl-DBD-mysql perl-Date-Manip perl-MIME-Lite perl-MIME-tools perl-Module-Load perl-Sys-Mmap perl-X10 perl-devel perl-libwww zlib-devel libpolkit-devel cmake libv4l-devel rpm-macros-cmake libvlc-devel libcurl-devel libssl-devel libsystemd-devel libffi-devel libx264-devel libmount-devel libuuid-devel libselinux-devel libblkid-devel libmp4v2

%description
ZoneMinder is a set of applications which is intended to provide a complete
solution allowing you to capture, analyse, record and monitor any cameras you
have attached to a Linux based machine. It is designed to run on kernels which
support the Video For Linux (V4L) interface and has been tested with cameras
attached to BTTV cards, various USB cameras and IP network cameras. It is
designed to support as many cameras as you can attach to your computer without
too much degradation of performance. This package includes cambozola.jar.

%package api
Summary: Zoneminder Web API
Group: Networking/WWW
Requires: zoneminder
BuildArch: noarch

%description api
The API is built in CakePHP and lives under the /api directory. It provides a RESTful service 
and supports CRUD (create, retrieve, update, delete) functions for Monitors, Events, Frames, 
Zones and Config.

%package nginx
Summary: Zoneminder configuration file and requires for nginx
Group: Networking/WWW
Requires: php7-fpm-fcgi fcgiwrap nginx
BuildArch: noarch
%description nginx
Zoneminder configuration file and requires for nginx

%prep
%setup -n %name-%version-alt
%patch1 -p1
tar xvf %SOURCE1 --strip 1 -C web/api/app/Plugin/Crud
tar xvf %SOURCE2 --strip 1 -C web/api/app/Plugin/CakePHP-Enum-Behavior
cp %SOURCE4 README.alt
cp %SOURCE5 README-nginx-ru.alt

cat <<EOF >> db/zm_create.sql.in
use mysql;
grant select,insert,update,delete on zm.* to 'zmuser'@localhost identified by 'zmpass';
EOF

./utils/zmeditconfigdata.sh ZM_OPT_CAMBOZOLA yes
./utils/zmeditconfigdata.sh ZM_UPLOAD_FTP_LOC_DIR /var/spool/zoneminder-upload
./utils/zmeditconfigdata.sh ZM_OPT_CONTROL yes
./utils/zmeditconfigdata.sh ZM_CHECK_FOR_UPDATES no
./utils/zmeditconfigdata.sh ZM_DYN_SHOW_DONATE_REMINDER no
./utils/zmeditconfigdata.sh ZM_OPT_FAST_DELETE no

%build
%cmake -DZM_TARGET_DISTRO="alt" -DPCRE_INCLUDE_DIR=/usr/include/pcre -DZM_SYSTEMD=ON -DZM_WEB_USER=%{zmuid_final} -DZM_WEB_GROUP=%{zmgid_final}

make %{?_smp_mflags} -C BUILD

%install
install -d %buildroot%_var/run
%make_install -C BUILD install DESTDIR=%buildroot
rm -rf %buildroot%prefix/%_lib/perl5/vendor_perl/*.*/*-*
rm -rf %buildroot%prefix/%_lib/perl5/*.*/*-*

install -m 755 -d %buildroot%_var/log/zoneminder
for dir in events images temp
do
	install -m 755 -d %buildroot%_localstatedir/zoneminder/$dir
done
install -D -m 755 BUILD/scripts/zm %buildroot%_initdir/zoneminder
install -D -m 644 BUILD/misc/zoneminder.service %buildroot/%_unitdir/%name.service
install -D -m 644 BUILD/misc/zoneminder-tmpfiles.conf %buildroot/%_tmpfilesdir/zoneminder.conf
install -D -m 644 %SOURCE3 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/zoneminder.conf
install -D -m 644 %SOURCE6 %buildroot%_sysconfdir/nginx/sites-enabled.d/nginx-zoneminder.conf.sample
install -D -m 644 %SOURCE7 %buildroot%_sysconfdir/nginx/sites-enabled.d/zm-fcgi.inc
mkdir -p %buildroot/%_cachedir/%name

cp -aR web/api %buildroot%_datadir/%name/www/api
ln -s %_cachedir/%name %buildroot%_datadir/%name/www/cache


rm -f %buildroot%perl_vendor_archlib/perllocal.pod
mkdir -p %buildroot%_datadir/%name/db
cp db/*.sql %buildroot%_datadir/%name/db


%post
%post_service zoneminder

%preun
%preun_service zoneminder

%files
%doc COPYING README.md README.alt
%config(noreplace) %_sysconfdir/zm/zm.conf
%config(noreplace) %_sysconfdir/zm/conf.d/*.conf
%ghost %_cachedir/%name
%_sysconfdir/zm/conf.d/README
%_tmpfilesdir/zoneminder.conf
%_unitdir/%name.service
%_initdir/zoneminder
%_bindir/*
%_datadir/%name
%_man8dir/zoneminder*
%perl_vendorlib/ZoneMinder*
%perl_vendorlib/ONVIF*
%perl_vendorlib/WSDiscovery*
%perl_vendorlib/WSSecurity*
%perl_vendorlib/WSNotification*

%_libexecdir/%name
%dir %attr(755,%zmuid_final,%zmgid_final) %_var/log/zoneminder
%dir %attr(755,%zmuid_final,%zmgid_final) %_localstatedir/zoneminder
%dir %attr(755,%zmuid_final,%zmgid_final) %_localstatedir/zoneminder/events
%dir %attr(755,%zmuid_final,%zmgid_final) %_localstatedir/zoneminder/images
%dir %attr(755,%zmuid_final,%zmgid_final) %_localstatedir/zoneminder/temp
%_datadir/polkit-1/*/*
%exclude %_datadir/%name/www/api


%files nginx
%doc README-nginx-ru.alt
%config(noreplace) %_sysconfdir/nginx/sites-enabled.d/*

%files api
%_datadir/%name/www/api

%changelog
* Mon Feb 03 2020 Anton Farygin <rider@altlinux.ru> 1.34.1-alt1
- 1.34.1

* Tue Jan 21 2020 Anton Farygin <rider@altlinux.ru> 1.34.0-alt1
- 1.34.0 (fixes: CVE-2019-13072, CVE-2019-6777, CVE-2019-8429, CVE-2019-8428,
	  CVE-2019-8427, CVE-2019-8426, CVE-2019-8425, CVE-2019-8424, CVE-2019-8423,
	  CVE-2019-7352, CVE-2019-7351, CVE-2019-7350, CVE-2019-7349, CVE-2019-7348,
	  CVE-2019-7347, CVE-2019-7346, CVE-2019-7345, CVE-2019-7344, CVE-2019-7343,
	  CVE-2019-7342, CVE-2019-7341, CVE-2019-7340, CVE-2019-7339, CVE-2019-7338,
	  CVE-2019-7337, CVE-2019-7336, CVE-2019-7335, CVE-2019-7334, CVE-2019-7333,
	  CVE-2019-7332, CVE-2019-7331, CVE-2019-7330, CVE-2019-7329, CVE-2019-7328,
	  CVE-2019-7326, CVE-2019-7325, CVE-2019-6992, CVE-2019-6991, CVE-2019-6990)
- switched to apache2 as default user for ZoneMinder
- removed MySQL-client require

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.32.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Mon Jan 14 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.32.3-alt2
- fix FTBFS due to transition to libmysqlclient21

* Fri Dec 14 2018 Anton Farygin <rider@altlinux.ru> 1.32.3-alt1
- 1.32.3

* Wed Oct 17 2018 Anton Farygin <rider@altlinux.ru> 1.32.2-alt1
- 1.32.2

* Thu Oct 11 2018 Anton Farygin <rider@altlinux.ru> 1.32.1-alt1
- 1.32.1

* Tue Sep 25 2018 Anton Farygin <rider@altlinux.ru> 1.32.0-alt1
- 1.32.0

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 1.30.4-alt3
- removed spawn-fcgi requires for nginx
	(it does not need on configuration with systemd)

* Wed Jun 21 2017 Anton Farygin <rider@altlinux.ru> 1.30.4-alt2
- removed apache subpackage

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 1.30.4-alt1
- new version

* Mon Jan 16 2017 Anton Farygin <rider@altlinux.ru> 1.30.0-alt1
- added ubt tag to facilitate the backporting process

* Mon Jan 16 2017 Anton Farygin <rider@altlinux.ru> 1.30.0-alt1
- new version

* Fri Mar 11 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27.0-alt4
- rebuild with recent libav

* Fri Aug 22 2014 Mikhail Efremov <sem@altlinux.org> 1.27.0-alt3
- Rebuild with libgnutls28.

* Mon May 19 2014 Anton Farygin <rider@altlinux.ru> 1.27.0-alt2
- rebuild with new libav

* Wed Apr 16 2014 Anton Farygin <rider@altlinux.ru> 1.27.0-alt1
- new version
- added subpackage with sample nginx configuration for zoneminder web interface

* Tue May 15 2012 Andrey Cherepanov <cas@altlinux.org> 1.24.4-alt2.1.M60P.2
- Rebuild with new version of libav

* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.24.4-alt2.2
- Fixed build with libav 0.8

* Wed Dec 07 2011 Yuri N. Sedunov <aris@altlinux.org> 1.24.4-alt2.1
- rebuilt against libgnutls-openssl.so.27 (gnutls26-2.12.14)

* Tue Aug 09 2011 Alex Negulescu <alecs@altlinux.org> 1.24.4-alt2
- changed buildreq
- reapplied some 1.24.2 patches (cumulative patch)
  - fixed debian bug #608790, already fixed in 1.24.2-alt2
  - mpeg.cpp patch
  - zm_sdp.cpp un-patch (av_alloc_format_context issue)
  - fixed MySQL 4.x compatibility issue
  - fix incomplete image errors in zmf
- added cambozola 0.92
- initscript complies with Alt policy

* Mon Aug 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.24.4-alt1
- 1.24.4

* Tue Jan 18 2011 Alex Negulescu <alecs@altlinux.org> 1.24.2-alt3
- fixed issues reported by Roman Lesnichenko
  - removed apache from requires, added webserver
  - changed path from /var/lib/lib/zoneminder to /var/lib/zoneminder
  - fixed ffmpeg path
  - removed unnecessary /var/lib/run, /var/lib/log
  - added /var/log/zoneminder to files
  - small changes to init script

* Thu Jan 13 2011 Alex Negulescu <alecs@altlinux.org> 1.24.2-alt2
- readded to sisyphus
- spec changes & cumulative patch, fixing following issues:
  - Function ereg is deprecated warning
  - Missing progress bar for certain users
  - Marking a monitor from a restricted user
  - Delete group "undefined index" warning
  - Disabling a monitor from monitor options page
  - Unarchive button in events list page
  - Opera, Safari and iPhone MJPEG streaming capability
  - Gapless and All events replay mode
  - strftime() and strtotime() PHP warnings
  - Changing scale when viewing an event kills the stream
  - Incomplete read of frame image data error
  - "`errno' was not declared in this scope" error
  - "V4L2_PIX_FMT_HM12' was not declared in this scope" error
  - "avformat_alloc_context' was not declared in this scope" error
  - "You have an error in your SQL syntax;... 'where Name = 'Monitors'" MySQL 4.x compatibility issue

* Fri Nov 27 2009 Denis Klimov <zver@altlinux.org> 1.24.2-alt1
- new version
- use install patch as git commit
- remove patch for install sql files
- install sql files in spec

* Tue Apr 29 2008 Denis Medvedev <nbr@altlinux.ru> 1.23.3-alt2
- zm init script condstop added

* Tue Apr 29 2008 Denis Medvedev <nbr@altlinux.ru> 1.23.3-alt1
- http://secunia.com/advisories/29995/ and new version

* Tue Dec 25 2007 Denis Medvedev <nbr@altlinux.ru> 1.22.3-alt4
- fixed stupid bug with wrong param to url_close

* Tue Nov 06 2007 Denis Medvedev <nbr@altlinux.ru> 1.22.3-alt3
- Changed README.alt

* Tue Sep 04 2007 Denis Klimov <zver@altlinux.ru> 1.22.3-alt2
- Add requires: perl-Storable MySQL-client su
- Add subpackage zoneminder-apache
- Add %%config(noreplace) for zm.conf

* Thu Aug 30 2007 Denis Medvedev <nbr@altlinux.ru> 1.22.3-alt1
- Initial build for ALT

* Thu Jul 12 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-7
- Fixes from testing by Jitz including missing dependencies and database creation

* Sat Jun 30 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-6
- Disable crashtrace on ppc

* Sat Jun 30 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-5
- Fix uid for directories in /var/lib/zoneminder

* Tue Jun 26 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-4
- Added perl Archive::Tar dependency
- Disabled web interface due to lack of access control on the event images

* Sun Jun 10 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-3
- Changes recommended in review by Jason Tibbitts

* Mon Apr  2 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-2
- Standardised on package name of zoneminder

* Thu Dec 28 2006 Martin Ebourne <martin@zepler.org> - 1.22.3-1
- First version. Uses some parts from zm-1.20.1 by Corey DeLasaux and Serg Oskin
