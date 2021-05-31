%add_python3_lib_path %_datadir/openuds
%allow_python3_import_path %_datadir/openuds
%add_findreq_skiplist %_datadir/openuds/uds/transports/*/scripts/windows/* %_datadir/openuds/uds/transports/*/scripts/macosx/*
%add_python3_req_skip uds.forward
%filter_from_provides /^python3(manage)/d
%filter_from_provides /^python3(server)/d
%filter_from_provides /^python3(server\.settings)/d
%filter_from_provides /^python3(server\.urls)/d
%filter_from_provides /^python3(server\.wsgi)/d

Name: openuds-server
Version: 3.0.0
Release: alt7
Summary: Universal Desktop Services (UDS) Broker
License: BSD-3-Clause and MIT and Apache-2.0
Group: Networking/Remote access
URL: https://github.com/dkmstr/openuds
AutoReqProv: yes, nopython
Source0: %name-%version.tar

Source10: openuds-httpd.conf
Source11: openuds-httpd-ssl.conf
Source12: openuds.logrotate
Source13: openuds-nginx-sites.conf
Source15: openuds-taskmanager.service
Source16: openuds-web.service
Source17: openuds-web.socket

#Patch: %name-%version.patch

Requires: python3-module-django >= 2.2
Requires: python3-module-django-dbbackend-mysql >= 2.2
Requires: python3-module-django-dbbackend-sqlite3 >= 2.2
Requires: openssl
Requires: logrotate

Conflicts: openuds-tunnel openuds-guacamole-tunnel
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): webserver-common rpm-build-webserver-common rpm-macros-apache2

%description
OpenUDS (Universal Desktop Services) is a multiplatform connection broker for:
- VDI: Windows and Linux virtual desktops administration and deployment
- App virtualization
- Desktop services consolidation

This package provides the required components
to allow this machine to work as UDS Broker.


%package apache2
Group: Networking/WWW
BuildArch: noarch
Summary: apache2 configs for %name
Requires: %name = %version-%release
Requires: apache2-httpd-prefork-like
Requires: apache2-base
Requires: apache2-mod_wsgi-py3

%description apache2
%summary

%package nginx
Group: Networking/WWW
BuildArch: noarch
Summary: nginx configs for %name
Requires: %name = %version-%release
Requires: nginx
Requires: python3-module-gunicorn
Requires: cert-sh-functions

%description nginx
%summary

%prep
%setup
#%patch -p1

sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|' \
    $(find . -name '*.py')

%install

mkdir -p %buildroot{%_datadir,%_logdir,%_sysconfdir,%_sharedstatedir}/openuds
cp -r src/* %buildroot%_datadir/openuds/
mv %buildroot%_datadir/openuds/server/settings.py.sample %buildroot%_sysconfdir/openuds/settings.py
ln -r -s %buildroot%_logdir/openuds %buildroot%_datadir/openuds/log
ln -r -s %buildroot%_sysconfdir/openuds/settings.py %buildroot%_datadir/openuds/server/settings.py
# drop httpd-conf snippet
install -p -D -m 644 %SOURCE10 %buildroot%apache2_sites_available/openuds.conf
install -p -D -m 644 %SOURCE11 %buildroot%apache2_sites_available/openuds-ssl.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/openuds.conf
install -p -D -m 644 %SOURCE12 %buildroot%_logrotatedir/openuds-server
install -p -D -m 644 %SOURCE13 %buildroot%_sysconfdir/nginx/sites-available.d/openuds.conf
mkdir -p %buildroot%_sysconfdir/nginx/sites-enabled.d
touch %buildroot%_sysconfdir/nginx/sites-enabled.d/openuds.conf
install -p -D -m 644 %SOURCE15 %buildroot%_unitdir/openuds-taskmanager.service
install -p -D -m 644 %SOURCE16 %buildroot%_unitdir/openuds-web.service
install -p -D -m 644 %SOURCE17 %buildroot%_unitdir/openuds-web.socket

%pre
%_sbindir/groupadd -r -f openuds >/dev/null 2>&1 ||:
%_sbindir/useradd -M -r -g openuds -G _webserver -c 'OpenUDS Brocker Daemon' \
        -s /bin/false  -d %_sharedstatedir/openuds openuds >/dev/null 2>&1 ||:

%post
# ugly hack to set a unique SECRET_KEY
sed -i "/^SECRET_KEY.*$/{N;s/^.*$/SECRET_KEY='`openssl rand -hex 10`'/}" %_sysconfdir/openuds/settings.py

%post_service openuds-taskmanager

%preun
%preun_service openuds-taskmanager

%post nginx
%post_service openuds-web
# Create SSL certificate for HTTPS server
cert-sh generate nginx-openuds ||:

%preun nginx
%preun_service openuds-web

%files
%_datadir/openuds
%dir %attr(0750, root, openuds) %_sysconfdir/openuds
%config(noreplace) %attr(0640, root, openuds) %_sysconfdir/openuds/settings.py
%dir %attr(0770, root, openuds) %_sharedstatedir/openuds
%dir %attr(0770, root, openuds) %_logdir/openuds
%config(noreplace) %_logrotatedir/openuds-server
%_unitdir/openuds-taskmanager.service

%files apache2
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf

%files nginx
%config(noreplace) %_sysconfdir/nginx/sites-available.d/openuds.conf
%ghost %_sysconfdir/nginx/sites-enabled.d/openuds.conf
%_unitdir/openuds-web.service
%_unitdir/openuds-web.socket

%changelog
* Fri Apr 23 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt7
- Fix create home dir for user openuds

* Thu Apr 22 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt6
- Switch to local memory from memcached by default in settings.py.
- Fix openuds-web.service for execute gunicorn.py3 for use python3.
- Add conflicts with openuds-tunnel,openuds-guacamole-tunnel.

* Wed Apr 21 2021 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt5
- Fix typo in nginx config (ALT #39968)

* Wed Apr 14 2021 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.0-alt4
- Remove pages and buttons with downloading clients and actors

* Mon Dec 07 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt3
- merge with upstream v3.0 branch (b1c43850908c5c207afa5812edc6c1ce46d8ca78)
- update nginx config

* Thu Dec 03 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt2
- move apache config to apache2 package
- add package with nginx config and service for start django app over gunicorn

* Thu Nov 05 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0 Release

* Tue Apr 14 2020 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt0.1.git.d7e30d14
- Initial build for ALT

