#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: nginx
Summary: Fast HTTP server
Version: 1.16.1
Release: alt1
License: BSD
Group: System/Servers
BuildRequires: libpcre-devel libssl-devel perl-devel zlib-devel libkrb5-devel
BuildRequires: libGeoIP-devel
BuildRequires: libgd2-devel
BuildRequires: libpam-devel
BuildRequires: libxml2-devel libxslt-devel
%define pcre_version 4.5
%def_with perl
%def_with aio
%def_with aio
%def_with ipv6
%def_without syslog
%def_with image_filter
%def_with xslt
%def_without debug
%def_with geoip
%def_with spnego
%def_enable cache_purge
%def_enable rtmp
%define modpath %_libdir/%name
Url: http://sysoev.ru/nginx
Source: %url/%name-%version.tar
Source1: %name.conf.in
Source2: %name.init
Source3: %name.logrotate.in
Source5: %name.sysconfig
Source6: default.conf
Source7: cache_purge.tar
Source9: %name.service
Source10: nginx-rtmp-module.tar
Source11: mime.types
Source12: nginx.filetrigger
Source13: ngx_http_auth_pam_module.tar
Source14: spnego-http-auth-nginx-module.tar
Source100: %name.watch
Patch1: nginx-0.8-syslog.patch
Packager: Denis Smirnov <mithraen@altlinux.ru>
Requires(pre): shadow-utils
Requires(post): sed
Provides: webserver
%define nginx_user _nginx
%define nginx_group _nginx
%define nginx_etc %_sysconfdir/%name
%define nginx_spool %_spooldir/%name
%define nginx_log %_logdir/%name
%define configs %buildroot{%_unitdir/%name.service,%_sysconfdir/logrotate.d/%name,%nginx_etc/{%name.conf,sites-available.d/default.conf}}

%package geoip
Summary: GeoIP module for nginx
Group: System/Servers
%def_with geoip
Requires: GeoIP-Lite-City GeoIP-Lite-Country
Requires: %name = %EVR

%description geoip
GeoIP module for nginx

%if_with image_filter
%package image_filter
Summary: image_filter module for nginx
Group: System/Servers
Requires: %name = %EVR

%description image_filter
image_filter module for nginx
%endif

%package pam
Summary: auth_pam module for nginx.
Group: System/Servers
%def_with auth_pam
Requires: %name = %EVR

%description pam
auth_pam module for nginx.

%if_with perl
%package perl
Summary: Perl for nginx
Group: System/Servers
Requires: %name = %EVR

%description perl
Perl for nginx
%endif

%package spnego
Summary: Simple and Protected GSSAPI Negotiation Mechanism for nginx
Group: System/Servers
%def_with spnego
Requires: %name = %EVR

%description spnego
Simple and Protected GSSAPI Negotiation Mechanism for nginx

%package xslt
Summary: XSLT module for nginx
Group: System/Servers
%def_with xslt
Requires: %name = %EVR

%description xslt
XSLT module for nginx

%description
Fast HTTP server, extremely useful as an Apache frontend


%prep
%setup -a 7 -a 10 -a 13 -a 14
%if_with syslog
%patch1 -p2
%endif
sed -i 's/INSTALLSITEMAN3DIR=.*/INSTALLDIRS=vendor/' auto/lib/perl/make
cp -f %SOURCE11 conf/mime.types

%build
%ifarch i686
	CPU="-mtune=pentiumpro" \
%else # pentium4 athlon
	CPU="-mtune=%_arch" \
%endif
%ifarch i586
	CPU="" \
%endif
%ifnarch %ix86
	CPU="" \
%endif # for x86_64 TODO for amd64/nocona
CFLAGS="%optflags $CPU" ./configure \
	--prefix=/ \
	--conf-path=%nginx_etc/nginx.conf \
	--sbin-path=%_sbindir \
        --modules-path=%modpath \
	--error-log-path=%nginx_log/nginx.error.log \
	--http-log-path=%nginx_log/nginx.log \
	--http-client-body-temp-path=%nginx_spool/tmp/client \
	--http-proxy-temp-path=%nginx_spool/tmp/proxy \
	--http-fastcgi-temp-path=%nginx_spool/tmp/fastcgi \
	--http-uwsgi-temp-path=%nginx_spool/tmp/uwsgi \
	--http-scgi-temp-path=%nginx_spool/tmp/scgi \
	--pid-path=%_var/run/nginx.pid \
	--user=%nginx_user \
	--group=%nginx_group \
        --with-cc-opt="-I %_includedir/pcre/" \
	--with-http_ssl_module \
	--with-select_module    \
	--with-poll_module      \
        --with-threads \
%if_with aio
	--with-file-aio		\
%endif
%if_with ipv6
        --with-ipv6 \
%endif
	--with-http_ssl_module  \
	--with-http_v2_module  \
	--with-http_realip_module \
	--with-http_addition_module \
%if_with xslt
	--with-http_xslt_module=dynamic \
%endif
%if_with image_filter
	--with-http_image_filter_module=dynamic \
%endif
%if_with geoip
	--with-http_geoip_module=dynamic \
%endif
%if_with spnego
	--add-dynamic-module=spnego-http-auth-nginx-module \
%endif
%if_with auth_pam
	--add-dynamic-module=ngx_http_auth_pam_module \
%endif
	--with-http_sub_module \
	--with-http_dav_module \
	--with-http_flv_module \
	--with-http_mp4_module \
	--with-http_gunzip_module \
	--with-http_gzip_static_module \
	--with-http_auth_request_module \
        --with-http_random_index_module \
	--with-http_secure_link_module \
	--with-http_degradation_module \
	--with-http_slice_module \
	--with-http_stub_status_module \
%if_with perl
	--with-http_perl_module=dynamic \
%endif
	--with-mail=dynamic \
	--with-mail_ssl_module \
	--with-stream=dynamic \
	--with-stream_ssl_module \
%if_enabled cache_purge
	--add-module=cache_purge \
%endif
%if_enabled rtmp
	--add-dynamic-module=nginx-rtmp-module \
%endif
%if_with debug
	--with-debug \
%endif
%if_with syslog
	--with-syslog \
%endif
	--with-md5=%_libdir \
	--with-sha1=%_libdir
subst s!%buildroot!!g objs/*.h
%make_build DESTDIR=%buildroot

%install
mkdir -p %buildroot{%nginx_etc,%_sysconfdir/logrotate.d,%_sbindir,%nginx_spool/tmp,%nginx_log}
mkdir -p %buildroot%_spooldir/nginx/tmp/{client,proxy,fastcgi,scgi,uwsgi}
mkdir -p %buildroot%_lockdir/%name
mkdir -p %buildroot%nginx_etc/sites-enabled.d
mkdir -p %buildroot%nginx_etc/sites-available.d
mkdir -p %buildroot%nginx_etc/conf-enabled.d
mkdir -p %buildroot%nginx_etc/conf-available.d
%makeinstall DESTDIR=%buildroot
rm -f %buildroot%nginx_etc/%name.conf
install -pD -m644 %SOURCE1 %buildroot%nginx_etc/%name.conf
install -pD -m755 %SOURCE2 %buildroot%_initdir/%name
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/%name
install -pD -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name
install -pD -m644 %SOURCE6 %buildroot%nginx_etc/sites-available.d/default.conf
install -pD -m644 %SOURCE9 %buildroot%_unitdir/%name.service
install -pD -m644 nginx-rtmp-module/stat.xsl %buildroot%nginx_etc/stat.xsl
subst s!@nginx_user@!%nginx_user!g %configs
subst s!@nginx_etc@!%nginx_etc!g %configs
subst s!@nginx_spool@!%nginx_spool!g %configs
subst s!@nginx_log@!%nginx_log!g %configs
mkdir -p %buildroot%_docdir/%name-%version
cp -a CHANGES CHANGES.ru %buildroot%_docdir/%name-%version/
%if_with uwsgi
install -pD -m644 uwsgi/uwsgi_params %buildroot%nginx_etc/
%endif
rm -rf %buildroot/html/
mkdir -p %buildroot%nginx_etc/modules-available.d
mkdir -p %buildroot%nginx_etc/modules-enabled.d
for s in %buildroot/%modpath/*.so; do
    fn=${s##*/}
    module=${fn%%.so}
    module=${module#ngx_}
    module=${module%%_module}
    echo "load_module %modpath/$fn;" >> %buildroot%nginx_etc/modules-available.d/$module.conf
done
echo "# load dynamic nginx modules" > %buildroot%nginx_etc/nginx.conf.tmp
echo -e "include /etc/nginx/modules-enabled.d/*.conf;\n" >> %buildroot%nginx_etc/nginx.conf.tmp
cat %buildroot%nginx_etc/nginx.conf >> %buildroot%nginx_etc/nginx.conf.tmp
mv -f %buildroot%nginx_etc/nginx.conf.tmp %buildroot%nginx_etc/nginx.conf
install -pD -m755 %SOURCE12 %buildroot/usr/lib/rpm/nginx.filetrigger

%preun
%preun_service %name

%pre
%_sbindir/groupadd -r -f %nginx_group ||:
%_sbindir/groupadd -r -f _webserver ||:
%_sbindir/useradd -r -g %nginx_group -G _webserver -d /dev/null -s /dev/null -n %nginx_user \
	2> /dev/null > /dev/null ||:

%post
sed -i 's/\(types_hash_bucket_size[[:space:]]*\)[[:space:]]32[[:space:]]*;[[:space:]]*$/\1 64;/' /etc/nginx/nginx.conf ||:

%files
%_rpmlibdir/nginx.filetrigger
%_initdir/*
%_sbindir/*
%dir %nginx_etc
%dir %nginx_etc/sites-enabled.d
%dir %nginx_etc/sites-available.d
%dir %nginx_etc/modules-enabled.d
%dir %nginx_etc/modules-available.d
%dir %nginx_etc/conf-enabled.d
%dir %nginx_etc/conf-available.d
%config(noreplace) %nginx_etc/modules-available.d/mail.conf
%config(noreplace) %nginx_etc/modules-available.d/stream.conf
%config(noreplace) %nginx_etc/sites-available.d/default.conf
%if_enabled rtmp
%config(noreplace) %nginx_etc/modules-available.d/rtmp.conf
%nginx_etc/stat.xsl
%endif
%dir %attr(0700,root,root) %_lockdir/%name
%dir %attr(1770,root,%nginx_group) %nginx_spool/tmp
%dir %attr(1770,root,%nginx_group) %nginx_spool/tmp/client
%dir %attr(1770,root,%nginx_group) %nginx_spool/tmp/proxy
%dir %attr(1770,root,%nginx_group) %nginx_spool/tmp/fastcgi
%dir %attr(1770,root,%nginx_group) %nginx_spool/tmp/scgi
%dir %attr(1770,root,%nginx_group) %nginx_spool/tmp/uwsgi
%dir %attr(1770,root,%nginx_group) %nginx_spool
%dir %attr(1770,root,%nginx_group) %nginx_log
%config(noreplace) %nginx_etc/mime.types
%config(noreplace) %nginx_etc/nginx.conf
%config(noreplace) %nginx_etc/fastcgi.conf
%config(noreplace) %nginx_etc/scgi_params
%config(noreplace) %nginx_etc/uwsgi_params
%config(noreplace) %nginx_etc/fastcgi_params
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config %_unitdir/%name.service
%nginx_etc/*.default
%nginx_etc/koi-win
%nginx_etc/koi-utf
%nginx_etc/win-utf
%_docdir/%name-%version
%if_with uwsgi
%config(noreplace) %nginx_etc/uwsgi_params
%endif
%dir %modpath
%modpath/ngx_mail_module.so
%modpath/ngx_stream_module.so
%if_enabled rtmp
%modpath/ngx_rtmp_module.so
%endif

%files geoip
%config(noreplace) %nginx_etc/modules-available.d/http_geoip.conf
%modpath/ngx_http_geoip_module.so

%if_with image_filter
%files image_filter
%config(noreplace) %nginx_etc/modules-available.d/http_image_filter.conf
%modpath/ngx_http_image_filter_module.so
%endif

%files pam
%config(noreplace) %nginx_etc/modules-available.d/http_auth_pam.conf
%modpath/ngx_http_auth_pam_module.so

%if_with perl
%files perl
%config(noreplace) %nginx_etc/modules-available.d/http_perl.conf
%perl_vendor_archlib/nginx.pm
%perl_vendor_autolib/nginx
%modpath/ngx_http_perl_module.so
%endif

%files spnego
%config(noreplace) %nginx_etc/modules-available.d/http_auth_spnego.conf
%modpath/ngx_http_auth_spnego_module.so

%files xslt
%config(noreplace) %nginx_etc/modules-available.d/http_xslt_filter.conf
%modpath/ngx_http_xslt_filter_module.so

%changelog
* Sun Sep 01 2019 Anton Farygin <rider@altlinux.ru> 1.16.1-alt1
- 1.16.1

* Wed Dec 05 2018 Anton Farygin <rider@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Mon Nov 12 2018 Anton Farygin <rider@altlinux.ru> 1.14.1-alt2
- restart service only from filetrigger

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 1.14.1-alt1
- 1.14.1 (fixes: CVE-2018-16845, CVE-2018-16843, CVE-2018-16844)

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1.14.0-alt3
- rebuilt with openssl-1.1

* Fri Jul 20 2018 Anton Farygin <rider@altlinux.ru> 1.14.0-alt2
- fixed build with glibc-2.3.2
- spenego module moved to tarball
- updated auth_pam module

* Tue Jun 05 2018 Denis Smirnov <mithraen@altlinux.ru> 1.14.0-alt1.S1
- Updated to 1.14.0
- Updated nginx-rtmp-module

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.12.1-alt2.1
- rebuild with new perl 5.26.1

* Wed Jul 19 2017 Elvira Khabirova <lineprinter@altlinux.org> 1.12.1-alt2
- Added ngx_http_auth_pam_module.
- Fixed dependencies of module packages.

* Tue Jul 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.12.1-alt1
- Updated to 1.12.1 (Fixes CVE-2017-7529).

* Thu May 11 2017 Evgeny Bolshedvorsky <jenya@altlinux.org> 1.12-alt3
- added spnego dynamic module

* Sun Apr 16 2017 Denis Smirnov <mithraen@altlinux.ru> 1.12-alt2
- update rtmp module

* Sat Apr 15 2017 Denis Smirnov <mithraen@altlinux.ru> 1.12-alt1
- 1.12

* Mon Apr 03 2017 Denis Smirnov <mithraen@altlinux.ru> 1.10.3-alt2
- add %

* Tue Mar 28 2017 Denis Smirnov <mithraen@altlinux.ru> 1.10.3-alt1
- 1.10.3

* Wed Jun 01 2016 Denis Smirnov <mithraen@altlinux.ru> 1.10.1-alt1
- 1.10.1
- CVE-2016-4450

* Sun May 01 2016 Denis Smirnov <mithraen@altlinux.ru> 1.10.0-alt3
- remove ctpp module (ALT #32041)
- fix dynamic modules configuration (use %nginx_etc/modules-enabled.d)
- move perl module to nginx-perl subpackege
- move GeoIP module to nginx-geoip subpackege
- move xslt module to nginx-xslt subpackege
- add image_filter module to nginx-image_filter subpackage
- add filetrigger for restart nginx when modules installed/removed

* Sat Apr 30 2016 Denis Smirnov <mithraen@altlinux.ru> 1.10.0-alt2
- update default config with dynamic modules loading sample

* Sat Apr 30 2016 Denis Smirnov <mithraen@altlinux.ru> 1.10.0-alt1
- 1.10.0
- build some modules as dynamic

* Mon Feb 01 2016 Denis Smirnov <mithraen@altlinux.ru> 1.8.1-alt1
- 1.8.1
- CVE-2016-0742
- CVE-2016-0746
- CVE-2016-0747

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1.1
- rebuild with new perl 5.22.0

* Mon Aug 24 2015 Denis Smirnov <mithraen@altlinux.ru> 1.8.0-alt1
- 1.8.0
- update cache-purge patch

* Fri Apr 10 2015 Denis Smirnov <mithraen@altlinux.ru> 1.6.3-alt1
- 1.6.3
- update rtmp module to 1.1.7

* Wed Dec 24 2014 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt2
- update rtmp module to 1.1.6

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1.1
- rebuild with new perl 5.20.1

* Thu Sep 18 2014 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt1
- 1.6.2
- CVE-2014-3616

* Thu Aug 28 2014 Denis Smirnov <mithraen@altlinux.ru> 1.6.1-alt2
- enable geopip module

* Wed Aug 06 2014 Denis Smirnov <mithraen@altlinux.ru> 1.6.1-alt1
- 1.6.1
- CVE-2014-3556

* Tue Apr 29 2014 Denis Smirnov <mithraen@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Wed Apr 23 2014 Denis Smirnov <mithraen@altlinux.ru> 1.4.7-alt3
- fix logrotate script (ALT #30018)

* Sat Mar 29 2014 Denis Smirnov <mithraen@altlinux.ru> 1.4.7-alt2
- add stat.xsl (ALT #29917)

* Wed Mar 19 2014 Denis Smirnov <mithraen@altlinux.ru> 1.4.7-alt1
- 1.4.7
- CVE-2014-0133

* Tue Mar 04 2014 Denis Smirnov <mithraen@altlinux.ru> 1.4.5-alt2
- add nginx_rtmp module

* Wed Feb 19 2014 Denis Smirnov <mithraen@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Mon Nov 25 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4.4-alt2
- use config(noreplace) for sites-available.d/default.conf (closes: #29607)

* Fri Nov 22 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4.4-alt1
- 1.4.4 (ALT #29604)
- CVE-2013-4547

* Mon Oct 14 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4.3-alt3
- add ipv6 support

* Thu Oct 10 2013 Anton Farygin <rider@altlinux.ru> 1.4.3-alt2
- fixed mime-types conflict (closes: #28550)

* Wed Oct 09 2013 Anton Farygin <rider@altlinux.ru> 1.4.3-alt1
- new version

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.4.2-alt2
- built for perl 5.18

* Tue Aug 13 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Tue May 07 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4.1-alt1
- 1.4.1
- CVE-2013-2028

* Fri May 03 2013 Denis Smirnov <mithraen@altlinux.ru> 1.4.0-alt1
- 1.4.0
- enable http_spdy_module

* Wed Apr 17 2013 Anton Farygin <rider@altlinux.ru> 1.2.8-alt1
- new version

* Wed Mar 13 2013 Anton Farygin <rider@altlinux.ru> 1.2.7-alt1
- new version

* Thu Feb 28 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 1.2.4-alt1.1
- add systemd service (ALT #28069)
- logrotate using 'nginx -s reopen' (systemd)

* Fri Oct 26 2012 Anton Farygin <rider@altlinux.ru> 1.2.4-alt1
- new version

* Mon Oct 08 2012 Denis Smirnov <mithraen@altlinux.ru> 1.2.3-alt3
- add ngx_ctpp2 module

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.2.3-alt2
- rebuilt for perl-5.16

* Wed Aug 29 2012 Anton Farygin <rider@altlinux.ru> 1.2.3-alt1
- new version

* Sat Jul 21 2012 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- new version

* Wed Jun 06 2012 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- new version

* Wed May 30 2012 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- new version (closes: #27215)

* Fri Jan 27 2012 Anton Farygin <rider@altlinux.ru> 1.1.13-alt1
- new version
- decreased starting priority in initscript to 98 (closes: #26466)
- removed old Readme.ALT (closes: #26861)
- fixed duplicated ogg in mime-types (closes: #26863)

* Tue Nov 29 2011 Anton Farygin <rider@altlinux.ru> 1.1.9-alt1
- new version

* Wed Oct 26 2011 Anton Farygin <rider@altlinux.ru> 1.1.6-alt1
- new version

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 1.1.5-alt1.1
- rebuilt for perl-5.14

* Sun Oct 09 2011 Anton Farygin <rider@altlinux.ru> 1.1.5-alt1
- new version

* Thu Sep 22 2011 Anton Farygin <rider@altlinux.ru> 1.1.4-alt1
- new version
- enabled http_mp4_module

* Thu Sep 15 2011 Anton Farygin <rider@altlinux.ru> 1.1.3-alt1
- new version

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 1.1.2-alt1
- new version

* Tue Aug 23 2011 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- new version

* Wed Jun 01 2011 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- new version

* Fri May 27 2011 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- new version

* Wed Apr 13 2011 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2
- add cache_purge module

* Tue Apr 12 2011 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Feb 10 2011 Anton Farygin <rider@altlinux.ru> 0.8.54-alt1
- updated to 0.8.54
- add nginx user to _webserver group (closes: #24938)

* Wed Dec 01 2010 Anton Farygin <rider@altlinux.ru> 0.8.53-alt4
- added patch from 0.9.0 with fix for memory violation in auth_basic

* Tue Nov 30 2010 Anton Farygin <rider@altlinux.ru> 0.8.53-alt3
- fixed build with new perl

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.8.53-alt2.1
- rebuilt with perl 5.12

* Tue Nov 02 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.53-alt2
- add http_secure_link_module

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 0.8.53-alt1
- new version

* Mon Oct 04 2010 Anton Farygin <rider@altlinux.ru> 0.8.52-alt1
- new version

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 0.8.51-alt1
- new version

* Sun Sep 05 2010 Anton Farygin <rider@altlinux.ru> 0.8.50-alt1
- new version

* Fri Aug 20 2010 Anton Farygin <rider@altlinux.ru> 0.8.49-alt1
- new version

* Tue Aug 03 2010 Anton Farygin <rider@altlinux.ru> 0.8.48-alt1
- new version

* Thu Jul 01 2010 Anton Farygin <rider@altlinux.ru> 0.8.43-alt1
- new version
- removed external uswgi module (included to mainstream)
- new uswgi and scgi modules

* Wed May 26 2010 Ivan Fedorov <ns@altlinux.org> 0.8.38-alt1
- new version
- add uswgi module

* Wed Apr 07 2010 Anton Farygin <rider@altlinux.ru> 0.8.35-alt1
- new version
- added (disabled by default) syslogd patch

* Wed Mar 10 2010 Anton Farygin <rider@altlinux.ru> 0.8.34-alt1
- new version

* Thu Feb 04 2010 Anton Farygin <rider@altlinux.ru> 0.8.33-alt1
- new version

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 0.8.32-alt1
- new version
- remove unused patches

* Wed Nov 11 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.24-alt1
- Updated to 0.8.24.

* Tue Oct 06 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.19-alt1
- Updated to 0.8.19:
  + Bugfixes in limit_req;
  + SSL module enforcements (-SSLv2).

* Tue Oct 06 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.18-alt1
- Updated to 0.8.18.
- Move mime.types modification to separate patch.

* Wed Sep 23 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.16-alt1
- Updated to 0.8.16:
  + Bugfixes in resolver code, image module and gzip_vary handling.

* Mon Sep 14 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.15-alt1
- Updated to 0.8.15:
   + Security: a segmentation fault might occur in worker process while
     specially crafted request handling (VU#180065);
   + Bugfix: in file AIO.

* Mon Sep 07 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.14-alt1
- Updated to 0.8.14.

* Sun Sep 06 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.13-alt1
- NMU:
  + updated to 0.8.13;
  + add new aio module (and enable file aio);
  + add new geoip module (disabled by default);
  + massive update of mime.types database (sync with Apache);
  + nginx.init: get rid of duplicated conftest calls.

* Tue Jul 28 2009 L.A. Kostis <lakostis@altlinux.ru> 0.7.61-alt1
- NMU:
  + updated to 0.7.61.
  + src/event/openssl: fix memory corruption in $ssl_client_cert
    (thanks to Sergey Zhuravlev)

* Wed May 27 2009 L.A. Kostis <lakostis@altlinux.ru> 0.7.59-alt1
- NMU:
  + updated to 0.7.59.
  + fix optimization for x86.
  + add support of building new modules (disabled by default):
    + image_filter
    + xslt.

* Sat May 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.6.37-alt1.1
- rebuild

* Wed May 20 2009 L.A. Kostis <lakostis@altlinux.ru> 0.6.37-alt1
- NMU:
  + updated to 0.6.37.
  + disable all debug stuff (e.g. perftools support).

* Sat Apr 11 2009 Michael Shigorin <mike@altlinux.org> 0.6.35-alt2
- fixed missing substitution of sites-available.d/default.conf
  (Closes: #19560)

* Sat Feb 07 2009 Denis Smirnov <mithraen@altlinux.ru> 0.6.35-alt1
- Bugfix: in shared memory allocations if nginx was built without debugging.
- Bugfixes in an "Expect" request header line support.
- Bugfix: UTF-8 encoding usage in the ngx_http_autoindex_module.

* Sat Feb 07 2009 Denis Smirnov <mithraen@altlinux.ru> 0.6.34-alt2
- update README.ALT
- move default config to /etc/nginx/sites-available.d

* Sat Nov 29 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.34-alt1
- Change: now the EAGAIN error returned by connect() is not considered as
  temporary error.
- Change: now the "gzip_vary" directive turned on issues a "Vary:
  Accept-Encoding" header line for uncompressed responses too.
- Feature: the "expires" directive supports daily time.
- Feature: the "Expect" request header line support.
- Feature: now the "rewrite" directive does a redirect automatically if the
  "https://" protocol is used.
- Bugfix: the "listen" directive parameters such as "backlog", "rcvbuf", etc.
  were not set, if a default server was not the first one.
- Bugfix: the "log_not_found" directive did not work for index files tests.
- Bugfix: now if FastCGI server sends a "Location" header line without status
  line, then nginx uses 302 status code.  Thanks to Maxim Dounin.
- Bugfix: the ngx_http_flv_module did not support several values in a query
  string.
- Bugfix: when a request to a directory was redirected with the slash added,
  nginx dropped a query string from the original request.
- Feature: now nginx returns the 405 status code for POST method requesting a
  static file only if the file exists.
- Bugfix: the resolver did not understand big DNS responses.  Thanks to Zyb.
- Bugfix: in HTTPS mode requests might fail with the "bad write retry" error.
- Bugfix: the ngx_http_charset_module did not understand quoted charset name
  received from backend.
- Bugfix: if the "max_fails=0" parameter was used in upstream with several
  servers, then a worker process exited on a SIGFPE signal.  Thanks to Maxim
  Dounin.
- Bugfix: the $r->header_in() method did not return value of the "Host",
  "User-Agent", and "Connection" request header lines; the bug had appeared
  in 0.6.32.
- Bugfix: a full response was returned for request method HEAD while
  redirection via an "error_page" directive.
- Bugfix: if a directory has search only rights and the first index file was
  absent, then nginx returned the 500 status code.
- Bugfix: of recursive error_page for 500 status code.

* Mon Oct 27 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.32-alt1
- Change: the "none" parameter in the "ssl_session_cache" directive; now this
  is default parameter.  Thanks to Rob Mueller.
- Change: now the 0x00-0x1F, '"' and '\' characters are escaped as \xXX in an
  access_log.  Thanks to Maxim Dounin.
- Change: now nginx allows several "Host" request header line.
- Feature: the "modified" flag in the "expires" directive.
- Feature: the $uid_got and $uid_set variables may be used at any request
  processing stage.
- Feature: the $hostname variable.  Thanks to Andrei Nigmatulin.
- Feature: DESTDIR support.  Thanks to Todd A. Fisher and Andras Voroskoi.
- Bugfix: if sub_filter and SSI were used together, then responses might were
  transferred incorrectly.
- Bugfix: large SSI inclusions might be truncated.
- Bugfix: the "proxy_pass" directive did not work with the HTTPS protocol; the
  bug had appeared in 0.6.9.
- Bugfix: worker processes might not catch reconfiguration and log rotation
  signals.
- Bugfix: a segmentation fault might occur in worker process on Linux, if
  keepalive was enabled.

* Fri Jul 04 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.31-alt1
- Bugfix: nginx did not process FastCGI response if header was at the end of
  FastCGI record; bug appeared in 0.6.2.  Thanks to Sergey Serov.
- Bugfix: a segmentation fault might occur in worker process if a file was
  deleted and the "open_file_cache_errors" directive was off.

* Thu May 08 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.30-alt1
- Update to 0.6.30
- Change: now if an "include" directive pattern does not match any file, then
  nginx does not issue an error.
- Feature: now the time in directives may be
  specified without spaces, for example, "1h50m".
- Bugfix: memory leaks if the "ssl_verify_client" directive was on.  Thanks to
  Chavelle Vincent.
- Bugfix: the "sub_filter" directive might set text to change into output.
- Bugfix: the "error_page" directive did not take into account arguments in
  redirected URI.

* Mon Mar 31 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.29-alt1
- Update to 0.6.29

* Fri Feb 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.35-alt2
- rebuild

* Mon Jan 28 2008 Michael Shigorin <mike@altlinux.org> 0.5.35-alt1.1
- re-added kludge from 0.5.34-alt1.1: the more insightful fix didn't
  account for the case of i586 (which is our default x86 buildarch)
  while my dirty hack doesnn't account at all, it just has a hammer :)
- so "could not build the types_hash, you should increase types_hash_bucket_size: 32
  error with our default configuration (considerably larger mime.types)
  should go away again

* Sat Jan 26 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.35-alt1
- Change: now the ngx_http_userid_module adds start time microseconds
  to the cookie field contains a pid value.
- Change: now the uname(2) is used on Linux instead of procfs.
  Thanks to Ilya Novikov.
- Feature: the "If-Range" request header line support.
  Thanks to Alexander V. Inyukhin.
- Bugfix: in HTTPS mode requests might fail with the "bad write retry"
  error; bug appeared in 0.5.13.
- Bugfix: the STARTTLS in SMTP mode did not work.
  Thanks to Oleg Motienko.
- Bugfix: large_client_header_buffers did not freed before going to
  keep-alive state.
  Thanks to Olexander Shtepa.
- Bugfix: the "limit_rate" directive did not allow to use full
  throughput, even if limit value was very high.
- Bugfix: the $status variable was equal to 0 if a proxied server
  returned response in HTTP/0.9 version.
- Bugfix: if the "?" character was in a "error_page" directive, then
  it was escaped in a proxied request; bug appeared in 0.5.32.

* Sat Jan 26 2008 Michael Shigorin <mike@altlinux.org> 0.5.34-alt2.2
- replaced ugly kludge introduced by me in 0.5.34-alt1.1
  with an insightful one by Gena Makhomed (#13407)

* Sat Jan 26 2008 Michael Shigorin <mike@altlinux.org> 0.5.34-alt2.1
- added Provides: webserver (#13546)

* Thu Jan 10 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.34-alt2
- rebuild

* Thu Jan 10 2008 Michael Shigorin <mike@altlinux.org> 0.5.34-alt1.1
- got fed up with "could not build the types_hash, you should
  increase types_hash_bucket_size: 32" and did increase the default
  to empirically tested (Linux/i586) value of 64

* Tue Jan 08 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.34-alt1
- Change: now the full request line instead of URI only is written to
  error_log.
- Feature: the "merge_slashes" directive.
- Feature: the "gzip_vary" directive.
- Feature: the "server_tokens" directive.
- Feature: the "access_log" directive may be used inside the "limit_except" block.
- Bugfix: if the $server_protocol was used in FastCGI parameters and a
  request line length was near to the "client_header_buffer_size" directive
  value, then nginx issued an alert "fastcgi: the request record is too big".
- Bugfix: if a plain text HTTP/0.9 version request was made to HTTPS server,
  then nginx returned usual response.
- Bugfix: URL double escaping in a redirect of the "msie_refresh"
  directive; bug appeared in 0.5.28.
- Bugfix: a segmentation fault might occur in worker process if
  subrequests were used.
- Bugfix: the big responses may be transferred truncated if SSL and gzip were
 used.
- Bugfix: compatibility with mget.
- Bugfix: nginx did not unescape URI in the "include" SSI command.
- Bugfix: the segmentation fault was occurred on start or while
  reconfiguration if variable was used in the "charset" or
  "source_charset" directives.
- Bugfix: nginx returned the 400 response on requests like
  "GET http://www.domain.com HTTP/1.0". Thanks to James Oakley.
- Bugfix: a segmentation fault occurred in worker process if
  $date_local and $date_gmt were used outside the
  ngx_http_ssi_filter_module.
- Bugfix: a segmentation fault might occur in worker process if debug
  log was enabled. Thanks to Andrei Nigmatulin.
- Bugfix: ngx_http_memcached_module did not set $upstream_response_time.
  Thanks to Maxim Dounin.
- Bugfix: a worker process may got caught in an endless loop, if the
  memcached was used.

* Sun Jan 06 2008 Michael Shigorin <mike@altlinux.org> 0.5.33-alt2.1
- Fix default nginx.conf:
  + first server_name with wildcards is a fatal error now
  + add two more somewhat unobvious tips on reverse proxying
  + link to http://nginx.net for info/docs

* Sat Dec 01 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.33-alt2
- Auto fix types_hash_bucket_size in config

* Sat Nov 10 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.33-alt1
- Change: now by default the "echo" SSI command uses entity encoding.
- Feature: the "encoding" parameter in the "echo" SSI command.
- Change: mail proxy was split on three modules: pop3, imap and smtp.
- Feature: the "smtp_greeting_delay" and "smtp_client_buffer" directives of the
  ngx_mail_smtp_module.
- Feature: the "server_name" and "valid_referers" directives support regular
  expressions.
- Feature: the "server_name", "map", and "valid_referers" directives support
  the "www.example.*" wildcards.
- Bugfix: sub_filter did not work with empty substitution.
- Bugfix: in sub_filter parsing.
- Bugfix: a worker process may got caught in an endless loop, if the memcached
  was used.
- Bugfix: nginx supported low case only "close" and "keep-alive" values in the
  "Connection" request header line; bug appeared in 0.5.32.
- build --with debug (for more verbose logging)

* Sun Oct 21 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.32-alt1
- Change: now nginx tries to set the "worker_priority", "worker_rlimit_nofile",
  "worker_rlimit_core", and "worker_rlimit_sigpending" without super-user
  privileges.
- Change: now nginx escapes space and "%%" in request to a mail proxy
  authentication server.
- Change: now nginx escapes "%%" in $memcached_key variable.
- Feature: the "add_header Last-Modified ..." directive changes the
  "Last-Modified" response header line.
- Feature: the mail proxy supports AUTHENTICATE in IMAP mode.  Thanks to Maxim
  Dounin.
- Feature: the mail proxy supports STARTTLS in SMTP mode.  Thanks to Maxim
  Dounin.
- Bugfix: nginx did not close directory file on HEAD request if autoindex was
  used.  Thanks to Arkadiusz Patyk.
- Bugfix: the "proxy_hide_header" and "fastcgi_hide_header" directives did not
  hide response header lines whose name was longer than 32 characters.  Thanks
  to Manlio Perillo.
- Bugfix: active connection counter always increased if mail proxy was used.
- Bugfix: if backend returned response header only using non-buffered proxy,
  then nginx closed backend connection on timeout.
- Bugfix: nginx did not support several "Connection" request header lines.
- Bugfix: a charset set by the "charset" directive was not appended to the
  "Content-Type" header set by $r->send_http_header().
- Bugfix: a segmentation fault might occur in worker process if /dev/poll
  method was used.
- Bugfix: a segmentation fault occurred in worker process if invalid address
  was set in the "auth_http" directive.
- Bugfix: now nginx uses default listen backlog value 511 on all platforms
  except FreeBSD.  Thanks to Jiang Hong.
- Bugfix: now Solaris sendfilev() is not used to transfer the client request
  body to FastCGI-server via the unix domain socket.
- Bugfix: if the same host without specified port was used as backend for HTTP
  and HTTPS, then nginx used only one port - 80 or 443.
- Bugfix: the "proxy_ignore_client_abort" and "fastcgi_ignore_client_abort"
  directives did not work; bug appeared in 0.5.13.

* Fri Aug 31 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.31-alt4
- rebuild

* Fri Aug 31 2007 Michael Shigorin <mike@altlinux.org> 0.5.31-alt3.1
- properly fixed #7441 (taking into accound ldv@'s objections)
- properly fixed #12655 (ditto)
- readability improvements to initscript
- added /etc/sysconfig/nginx (flexible ulimit setup)

* Fri Aug 31 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.31-alt3
- rebuild

* Thu Aug 30 2007 Michael Shigorin <mike@altlinux.org> 0.5.31-alt2.1
- fix back my thinko regarding /var/run/nginx/ directory
- rework upgrade() initscript action (and run it only for package upgrades,
  just do a restart for sysadmin's command) -- should fix #12655

* Thu Aug 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.31-alt2
- rebuild

* Thu Aug 30 2007 Michael Shigorin <mike@altlinux.org> 0.5.31-alt1.1
- NMU: moved remnants of directory creation and permissions setup
  from initscript to specfile (seems like was a band-aid which is
  currently unneeded and non-elegant); see also #12647
- fixed #7441 (service nginx stop would leave children running)

* Fri Aug 17 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.31-alt1
- Feature: named locations.
- Feature: the "proxy_store" and "fastcgi_store" directives.
- Feature: the "proxy_store_access" and "fastcgi_store_access" directives.
- Feature: the $args variable can be set with the "set" directive.
- Feature: the $is_args variable.
- Bugfix: if a client has closed connection to mail proxy then nginx might not
  close connection to backend.
- Bugfix: now nginx escapes space in $memcached_key variable.
- Bugfix: a segmentation fault might occur in worker process when the HTTPS
  protocol was used in the "proxy_pass" directive.
- Bugfix: the perl $$ variable value in ngx_http_perl_module was equal to the
  master process identification number.
- Bugfix: fix building on Solaris/amd64 by Sun Studio 11 and early versions;
  bug appeared in 0.5.29.
- Feature: $nginx_version variable.  Thanks to Nick S. Grechukh.
- Bugfix: if the FastCGI header was split in records, then nginx passed garbage
  in the header to a client.
- Bugfix: Sun Studio compatibility on Solaris/amd64 and Solaris/sparc64.
  Thanks to Jiang Hong and Andrei Nigmatulin.
- Bugfix: of minor potential bugs.  Thanks to Coverity's Scan.
- Security: the "msie_refresh" directive allowed XSS.  Thanks to Maxim Boguk.
- Bugfix: a segmentation fault might occur in worker process if the
  "auth_http_header" directive was used.  Thanks to Maxim Dounin.
- Bugfix: a segmentation fault occurred in worker process if the CRAM-MD5
  authentication method was used, but it was not enabled.
- Bugfix: a segmentation fault might occur in worker process if the eventport
  method was used.
- Bugfix: if remote SSI subrequest was used, then posterior local file
  subrequest might transferred to client in wrong order.
- Bugfix: large SSI inclusions buffered in temporary files were truncated.

* Fri Jul 06 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.26-alt2
- More strict requires for perl-base version

* Fri Jun 22 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.26-alt1
- Remove nginx.perl.fix.patch (added to upstream)
- Drop nginx-0.5.14-gns-catchstderr.patch (added to upstream)
- Bugfix: in SSI parsing.
- Bugfix: nginx could not be built with the --without-http_rewrite_module
  parameter; bug appeared in 0.5.24.
- Security: the "ssl_verify_client" directive did not work if request was made
  using HTTP/0.9.
- Bugfix: a part of response body might be passed uncompressed if gzip was
  used; bug appeared in 0.5.23.

* Wed May 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.22-alt1
- update version to 0.5.22
- fix perl module (#11911)

* Mon May 28 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.20-alt3
- update mime.types (get it from Apache)

* Tue May 08 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.20-alt2
- fix x86_64 building

* Mon May 07 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.20-alt1
- update version to 0.5.20
- remove connection_pool_size option from config file (fix crash on x86_64)
- build with perl support (at@)
- Feature: the "sendfile_max_chunk" directive.
- Feature: the "$http_...", "$sent_http_...", and "$upstream_http_..."
  variables may be changed using the "set" directive.
- Bugfix: a segmentation fault might occur in worker process if the SSI command
  'if expr="$var = /"' was used.
- Bugfix: trailing boundary of multipart range response was transferred
  incorrectly.  Thanks to Evan Miller.

* Mon Apr 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.19-alt1
- update version to 0.5.19
- build --with-http_stub_status_module (gns@)
- fix mail proxy building
- Add Symbian sis/sisx files to mime.types (#11459)
- Add hints to config file (#11368)
- Make default config file more useful
- Add README.ALT
- Start more workers in default config (more DoS proof)
- Change: now the $request_time variable has millisecond precision.
- Feature: the $upstream_addr variable.
- Feature: the "proxy_headers_hash_max_size" and
  "proxy_headers_hash_bucket_size" directives.  Thanks to Volodymyr Kostyrko.
- Bugfix: the files more than 2G could not be transferred using sendfile on
  64-bit Linux.
- Feature: the ngx_http_sub_filter_module.
- Feature: the "$upstream_http_..." variables.
- Feature: now the $upstream_status and $upstream_response_time variables keep
  data about all upstreams before X-Accel-Redirect.

* Fri Apr 13 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.17-alt1
- update version to 0.5.17

* Sun Mar 18 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.14-alt1
- update version to 0.5.14

* Thu Dec 07 2006 Denis Smirnov <mithraen@altlinux.ru> 0.5.0-alt1
- update version to 0.5.0

* Fri Oct 27 2006 Denis Smirnov <mithraen@altlinux.ru> 0.4.11-alt1
- version update

* Fri Oct 20 2006 Denis Smirnov <mithraen@altlinux.ru> 0.4.9-alt2
- rebuild with http_browser_module

* Mon Oct 16 2006 Denis Smirnov <mithraen@altlinux.ru> 0.4.9-alt1
- version update

* Sat Aug 12 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.57-alt1
- version update

* Mon May 08 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.45-alt1
- version update
- authorize by client certifications added

* Mon Apr 17 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.38-alt1
- version update

* Sun Mar 12 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.32-alt1
- version update
- with realip

* Thu Mar 09 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.30-alt1
- version update;

* Fri Jan 13 2006 LAKostis <lakostis at altlinux.ru> 0.3.19-alt1
- NMU;
- version update;
- x86_64 fixes;
- default config updated;
- init script improvements;
- add logrotate script;
- update patches.

* Sun Nov 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.3.12-alt1
- version update

* Sun Oct 16 2005 Denis Smirnov <mithraen@altlinux.ru> 0.3.2-alt1
- version update
- create directories for temp files (client requests, fastcgi & proxy replies)

* Sat Sep 17 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.45-alt1
- version update

* Fri Aug 19 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.41-alt2
- added two patches (from lakostis@)
- build with optimization flags (from lakostis@)

* Wed Aug 03 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.41-alt1
- version update

* Sun Jul 24 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.40-alt1
- default_charset removed
- charset set reply codepage, source_charset -- source charset :)
- limit_rate supported with proxy and fastcgi
- X-Accel-Limit-Rate header from backend supported
- added: ssi_types
- added: autoindex_exact_size
- added: log_not_found
- added: break
- removed: post_accept_timeout
- build with imap
- many other fixes

* Thu Jun 09 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.35-alt1
- version update

* Sat May 28 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.34-alt1
- 0.1.34
- spec cleanup / macrification (mike@)
- changed "nginx" user/group to "_nginx" (mike@)

* Wed May 18 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.31-alt1
- version update
- some cleanups

* Sun Apr 17 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.28-alt1
- version update

* Sun Mar 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.26-alt2
- cleanup

* Sat Mar 26 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.26-alt1
- version update
- add ulimit -n 16384 to initscript

* Mon Mar 21 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.25-alt1
- version update
- cleanup
- tmp moved to /var/spool/nagios/tmp

* Thu Mar 17 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.24-alt1
- version update

* Sun Feb 06 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.17-alt1
- version update

* Sat Jan 29 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.16-alt1
- version update
- fastcgi support (upstream)

* Fri Dec 24 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1.13-alt1
- version update
- OpenSSL-support builded
- rewrite and pcre support builded
- startup script
- useful default config-file

* Sat Nov 27 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1.10-alt1
- version update

* Tue Oct 12 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1.1-alt1
- first build

