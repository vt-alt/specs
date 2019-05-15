%add_findreq_skiplist %_datadir/openstack-dashboard/openstack_dashboard/management/commands/horizon.wsgi.template
%define oname horizon
%def_with compression

Name: python-module-django-%oname
Version: 14.0.3
Release: alt1
Epoch: 1
Summary: Django application for talking to Openstack

Group: System/Servers
# Code in horizon/horizon/utils taken from django which is BSD
License: ASL 2.0 and BSD
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: openstack-dashboard-httpd.conf
Source11: openstack-dashboard-httpd-ssl.conf

# systemd snippet to collect static files and compress on httpd restart
Source3:    python-django-horizon-systemd.conf

# demo config for separate logging
Source4: openstack-dashboard-httpd-logging.conf

# logrotate config
Source5:    python-django-horizon-logrotate.conf

BuildArch: noarch

%py_provides openstack_dashboard
Requires: python-module-django

BuildRequires(pre): webserver-common rpm-build-webserver-common rpm-macros-apache2
BuildRequires: gettext-tools
BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-django >= 1.11
BuildRequires: python-module-django-tests
# BuildRequires: python-module-django-babel >= 0.5.1
BuildRequires: python-module-django-compressor >= 2.0
BuildRequires: python-module-django-pyscss >= 2.0.2
BuildRequires: python-module-futurist >= 1.2.0
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-netaddr >= 0.7.18
BuildRequires: python-module-oslo.concurrency >= 3.26.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.policy >= 1.30.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-osprofiler >= 2.3.0
BuildRequires: python-module-pint >= 0.5
BuildRequires: python-module-pymongo >= 3.0.2
BuildRequires: python-module-pyScss >= 1.3.4
BuildRequires: python-module-cinderclient >= 3.3.0
BuildRequires: python-module-glanceclient >= 2.8.0
BuildRequires: python-module-keystoneclient >= 3.15.0
BuildRequires: python-module-neutronclient >= 6.7.0
BuildRequires: python-module-novaclient >= 9.1.0
BuildRequires: python-module-swiftclient >= 3.2.0
BuildRequires: python-module-pytz
BuildRequires: python-module-yaml >= 3.12
BuildRequires: python-module-semantic_version >= 2.3.1

BuildRequires: python-module-xstatic >= 1.0.0
BuildRequires: python-module-xstatic-angular >= 1.5.8.0
BuildRequires: python-module-xstatic-angular-bootstrap >= 2.2.0.0
BuildRequires: python-module-xstatic-angular-fileupload >= 12.0.4.0
BuildRequires: python-module-xstatic-angular-gettext >= 2.3.8.0
BuildRequires: python-module-xstatic-angular-lrdragndrop >= 1.0.2.2
BuildRequires: python-module-xstatic-angular-schema-form >= 0.8.13.0
BuildRequires: python-module-xstatic-bootstrap-datepicker >= 1.3.1.0
BuildRequires: python-module-xstatic-bootstrap-scss >= 3.3.7.1
BuildRequires: python-module-xstatic-bootswatch >= 3.3.7.0
BuildRequires: python-module-xstatic-d3 >= 3.5.17.0
BuildRequires: python-module-xstatic-hogan >= 2.0.0.2
BuildRequires: python-module-xstatic-font-awesome >= 4.7.0
BuildRequires: python-module-xstatic-jasmine >= 2.4.1.1
BuildRequires: python-module-xstatic-jquery >= 1.8.2.1
BuildRequires: python-module-xstatic-jquery-migrate >= 1.2.1.1
BuildRequires: python-module-xstatic-jquery.quicksearch >= 2.0.3.1
BuildRequires: python-module-xstatic-jquery.tablesorter >= 2.14.5.1
BuildRequires: python-module-xstatic-jquery-ui >= 1.10.4.1
BuildRequires: python-module-xstatic-jsencrypt >= 2.3.1.1
BuildRequires: python-module-xstatic-mdi >= 1.4.57.0
BuildRequires: python-module-xstatic-objectpath >= 1.2.1.0
BuildRequires: python-module-xstatic-rickshaw >= 1.5.0.0
BuildRequires: python-module-xstatic-roboto-fontface >= 0.5.0.0
BuildRequires: python-module-xstatic-smart-table >= 1.4.13.2
BuildRequires: python-module-xstatic-spin >= 1.2.5.2
BuildRequires: python-module-xstatic-term.js >= 0.0.7.0
BuildRequires: python-module-xstatic-tv4 >= 1.2.7.0

BuildRequires: python-module-rjsmin

BuildRequires: python-module-greenlet
BuildRequires: python-module-django-dbbackend-sqlite3
BuildRequires: python-module-django-appconf

BuildRequires: python-module-coverage
BuildRequires: python-module-mox python-module-mox3
BuildRequires: python-module-nose-exclude
BuildRequires: python-module-nose
BuildRequires: python-module-selenium

BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 1.6.2


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-django >= 1.11
BuildRequires: python3-module-django-tests
# BuildRequires: python3-module-django-babel >= 0.5.1
BuildRequires: python3-module-django-compressor >= 2.0
BuildRequires: python3-module-django-pyscss >= 2.0.2
BuildRequires: python3-module-futurist >= 1.2.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.policy >= 1.30.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-osprofiler >= 2.3.0
BuildRequires: python3-module-pint >= 0.5
BuildRequires: python3-module-pymongo >= 3.0.2
BuildRequires: python3-module-pyScss >= 1.3.4
BuildRequires: python3-module-cinderclient >= 3.3.0
BuildRequires: python3-module-glanceclient >= 2.8.0
BuildRequires: python3-module-keystoneclient >= 3.15.0
BuildRequires: python3-module-neutronclient >= 6.7.0
BuildRequires: python3-module-novaclient >= 9.1.0
BuildRequires: python3-module-swiftclient >= 3.2.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-semantic_version >= 2.3.1

BuildRequires: python3-module-xstatic >= 1.0.0
BuildRequires: python3-module-xstatic-angular >= 1.5.8.0
BuildRequires: python3-module-xstatic-angular-bootstrap >= 2.2.0.0
BuildRequires: python3-module-xstatic-angular-fileupload >= 12.0.4.0
BuildRequires: python3-module-xstatic-angular-gettext >= 2.3.8.0
BuildRequires: python3-module-xstatic-angular-lrdragndrop >= 1.0.2.2
BuildRequires: python3-module-xstatic-angular-schema-form >= 0.8.13.0
BuildRequires: python3-module-xstatic-bootstrap-datepicker >= 1.3.1.0
BuildRequires: python3-module-xstatic-bootstrap-scss >= 3.3.7.1
BuildRequires: python3-module-xstatic-bootswatch >= 3.3.7.0
BuildRequires: python3-module-xstatic-d3 >= 3.5.17.0
BuildRequires: python3-module-xstatic-hogan >= 2.0.0.2
BuildRequires: python3-module-xstatic-font-awesome >= 4.7.0
BuildRequires: python3-module-xstatic-jasmine >= 2.4.1.1
BuildRequires: python3-module-xstatic-jquery >= 1.8.2.1
BuildRequires: python3-module-xstatic-jquery-migrate >= 1.2.1.1
BuildRequires: python3-module-xstatic-jquery.quicksearch >= 2.0.3.1
BuildRequires: python3-module-xstatic-jquery.tablesorter >= 2.14.5.1
BuildRequires: python3-module-xstatic-jquery-ui >= 1.10.4.1
BuildRequires: python3-module-xstatic-jsencrypt >= 2.3.1.1
BuildRequires: python3-module-xstatic-mdi >= 1.4.57.0
BuildRequires: python3-module-xstatic-objectpath >= 1.2.1.0
BuildRequires: python3-module-xstatic-rickshaw >= 1.5.0.0
BuildRequires: python3-module-xstatic-roboto-fontface >= 0.5.0.0
BuildRequires: python3-module-xstatic-smart-table >= 1.4.13.2
BuildRequires: python3-module-xstatic-spin >= 1.2.5.2
BuildRequires: python3-module-xstatic-term.js >= 0.0.7.0
BuildRequires: python3-module-xstatic-tv4 >= 1.2.7.0

BuildRequires: python3-module-rjsmin

BuildRequires: python3-module-greenlet
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-django-appconf

BuildRequires: python3-module-coverage
BuildRequires: python3-module-mox python-module-mox3
BuildRequires: python3-module-nose-exclude
BuildRequires: python3-module-nose
BuildRequires: python3-module-selenium

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 1.6.2

%description
Horizon is a Django application for providing Openstack UI components.
It allows performing site administrator (viewing account resource usage,
configuring users, accounts, quotas, flavors, etc.) and end user
operations (start/stop/delete instances, create/restore snapshots, view
instance VNC console, etc.)

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n openstack-dashboard
Summary: Openstack web user interface reference implementation
Group: System/Servers
AutoReq: yes, nopython

Provides: openstack-dashboard-branding-upstream = %EVR
Provides: openstack-dashboard-theme = %EVR
Obsoletes: openstack-dashboard-theme < %EVR

Requires: apache2-base
Requires: apache2-mod_wsgi-py3
Requires: python3-module-django-horizon = %EVR
Requires: python3-module-django-openstack-auth  = %EVR
Requires: python3-module-django >= 1.11
# Requires: python3-module-django-tests
# Requires: python3-module-django-babel >= 0.5.1
Requires: python3-module-django-compressor >= 2.0
Requires: python3-module-django-pyscss >= 2.0.2
Requires: python3-module-futurist >= 1.2.0
Requires: python3-module-iso8601 >= 0.1.11
Requires: python3-module-keystoneauth1 >= 3.4.0
Requires: python3-module-netaddr >= 0.7.18
Requires: python3-module-oslo.concurrency >= 3.26.0
Requires: python3-module-oslo.config >= 5.2.0
Requires: python3-module-oslo.i18n >= 2.1.0
Requires: python3-module-oslo.policy >= 1.30.0
Requires: python3-module-oslo.serialization >= 2.18.0
Requires: python3-module-oslo.utils >= 3.33.0
Requires: python3-module-osprofiler >= 2.3.0
Requires: python3-module-pint >= 0.5
Requires: python3-module-pymongo >= 3.0.2
Requires: python3-module-pyScss >= 1.3.4
Requires: python3-module-cinderclient >= 3.3.0
Requires: python3-module-glanceclient >= 2.8.0
Requires: python3-module-keystoneclient >= 3.15.0
Requires: python3-module-neutronclient >= 6.7.0
Requires: python3-module-novaclient >= 9.1.0
Requires: python3-module-swiftclient >= 3.2.0
Requires: python3-module-pytz
Requires: python3-module-yaml >= 3.12
Requires: python3-module-semantic_version >= 2.3.1

Requires: python3-module-xstatic >= 1.0.0
Requires: python3-module-xstatic-angular >= 1.5.8.0
Requires: python3-module-xstatic-angular-bootstrap >= 2.2.0.0
Requires: python3-module-xstatic-angular-fileupload >= 12.0.4.0
Requires: python3-module-xstatic-angular-gettext >= 2.3.8.0
Requires: python3-module-xstatic-angular-lrdragndrop >= 1.0.2.2
Requires: python3-module-xstatic-angular-schema-form >= 0.8.13.0
Requires: python3-module-xstatic-bootstrap-datepicker >= 1.3.1.0
Requires: python3-module-xstatic-bootstrap-scss >= 3.3.7.1
Requires: python3-module-xstatic-bootswatch >= 3.3.7.0
Requires: python3-module-xstatic-d3 >= 3.5.17.0
Requires: python3-module-xstatic-hogan >= 2.0.0.2
Requires: python3-module-xstatic-font-awesome >= 4.7.0
Requires: python3-module-xstatic-jasmine >= 2.4.1.1
Requires: python3-module-xstatic-jquery >= 1.8.2.1
Requires: python3-module-xstatic-jquery-migrate >= 1.2.1.1
Requires: python3-module-xstatic-jquery.quicksearch >= 2.0.3.1
Requires: python3-module-xstatic-jquery.tablesorter >= 2.14.5.1
Requires: python3-module-xstatic-jquery-ui >= 1.10.4.1
Requires: python3-module-xstatic-jsencrypt >= 2.3.1.1
Requires: python3-module-xstatic-mdi >= 1.4.57.0
Requires: python3-module-xstatic-objectpath >= 1.2.1.0
Requires: python3-module-xstatic-rickshaw >= 1.5.0.0
Requires: python3-module-xstatic-roboto-fontface >= 0.5.0.0
Requires: python3-module-xstatic-smart-table >= 1.4.13.2
Requires: python3-module-xstatic-spin >= 1.2.5.2
Requires: python3-module-xstatic-term.js >= 0.0.7.0
Requires: python3-module-xstatic-tv4 >= 1.2.7.0


Requires: openssl
Requires: logrotate

%description -n openstack-dashboard
Openstack Dashboard is a web user interface for Openstack. The package
provides a reference implementation using the Django Horizon project,
mostly consisting of JavaScript and CSS to tie it altogether as a standalone
site.

%package -n python3-module-django-%oname
Summary: Django application for talking to Openstack
Group: Development/Python3

%py3_provides openstack_dashboard
%py3_provides openstack_dashboard.utils

%description -n python3-module-django-%oname
Horizon is a Django application for providing Openstack UI components.
It allows performing site administrator (viewing account resource usage,
configuring users, accounts, quotas, flavors, etc.) and end user
operations (start/stop/delete instances, create/restore snapshots, view
instance VNC console, etc.)

%package -n python3-module-django-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
AutoReq: yes, nopython

%description -n python3-module-django-%oname-tests
This package contains tests for %oname.


%package -n python-module-django-openstack-auth
Summary: Django authentication backend for OpenStack Keystone
Group: Development/Python

%description -n python-module-django-openstack-auth
Django OpenStack Auth is a pluggable Django authentication backend that
works with Django's contrib.auth framework to authenticate a user against
OpenStack's Keystone Identity API.

The current version is designed to work with the Keystone v2.0 and v3 API.

%package -n python-module-django-openstack-auth-tests
Summary: Tests for %oname
Group: Development/Python
Requires: python-module-django-openstack-auth = %EVR

%description -n python-module-django-openstack-auth-tests
This package contains tests for %oname.

%package -n python3-module-django-openstack-auth
Summary: Django authentication backend for OpenStack Keystone
Group: Development/Python3

%description -n python3-module-django-openstack-auth
Django OpenStack Auth is a pluggable Django authentication backend that
works with Django's contrib.auth framework to authenticate a user against
OpenStack's Keystone Identity API.

The current version is designed to work with the Keystone v2.0 and v3 API.

%package -n python3-module-django-openstack-auth-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-django-openstack-auth = %EVR

%description -n python3-module-django-openstack-auth-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Django Horizon
Group: Development/Documentation

%description doc
Documentation for the Django Horizon application for talking with Openstack

%prep
%setup -n %oname-%version

# remove precompiled egg-info
# rm -rf horizon.egg-info

# remove unnecessary .mo files
# they will be generated later during package build
find . -name "django*.mo" -exec rm -f '{}' \;


# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

# drop config snippet
cp -p %SOURCE4 .

sed -i "/^DEBUG =.*/c\DEBUG = False" openstack_dashboard/local/local_settings.py.example
sed -i "/^WEBROOT =.*/c\WEBROOT = '/dashboard/'" openstack_dashboard/local/local_settings.py.example
sed -i "/^.*ALLOWED_HOSTS =.*/c\ALLOWED_HOSTS = ['horizon.example.com', 'localhost']" openstack_dashboard/local/local_settings.py.example
sed -i "/^.*LOCAL_PATH =.*/c\LOCAL_PATH = '/tmp'" openstack_dashboard/local/local_settings.py.example
sed -i "/^.*POLICY_FILES_PATH =.*/c\POLICY_FILES_PATH = '/etc/openstack-dashboard'" openstack_dashboard/local/local_settings.py.example

sed -i "/^BIN_DIR = .*/c\BIN_DIR = '/usr/bin'" openstack_dashboard/settings.py
sed -i "/^COMPRESS_PARSER = .*/a COMPRESS_OFFLINE = True" openstack_dashboard/settings.py

%if_with compression
# set COMPRESS_OFFLINE=True
sed -i 's:COMPRESS_OFFLINE.=.False:COMPRESS_OFFLINE = True:' openstack_dashboard/settings.py
%else
# set COMPRESS_OFFLINE=False
sed -i 's:COMPRESS_OFFLINE = True:COMPRESS_OFFLINE = False:' openstack_dashboard/settings.py
%endif

rm -rf ../python3
cp -a . ../python3

%build
# compile message strings
cd horizon && django-admin compilemessages && cd ..
cd openstack_dashboard && django-admin compilemessages && cd ..
%python_build

pushd ../python3
%python3_build

# compress css, js etc.
cp openstack_dashboard/local/local_settings.py.example openstack_dashboard/local/local_settings.py
# get it ready for compressing later in puppet-horizon
%if_with compression
python3 manage.py collectstatic --noinput --clear
python3 manage.py compress --force
%endif

# build docs
#export PYTHONPATH="$( pwd ):$PYTHONPATH"
#sphinx-build-3 -b html doc/source html

# undo hack
cp openstack_dashboard/local/local_settings.py.example openstack_dashboard/local/local_settings.py

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo
popd

%install
%python_install

pushd ../python3
%python3_install
popd


# drop httpd-conf snippet
install -m 0644 -D -p %SOURCE1 %buildroot%apache2_sites_available/openstack-dashboard.conf
install -m 0644 -D -p %SOURCE11 %buildroot%apache2_sites_available/openstack-dashboard-ssl.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/openstack-dashboard.conf
touch %buildroot%apache2_sites_available/openstack-dashboard-ssl.conf

install -d -m 755 %buildroot%_datadir/openstack-dashboard
install -d -m 755 %buildroot%_sharedstatedir/openstack-dashboard
install -d -m 755 %buildroot%_sysconfdir/openstack-dashboard

# create directory for systemd snippet
#mkdir -p %buildroot%_unitdir/httpd.service.d/
#cp %SOURCE3 %buildroot%_unitdir/httpd.service.d/openstack-dashboard.conf

mkdir -p %buildroot%_sysconfdir/systemd/system/httpd2.service.d
cp %SOURCE3 %buildroot%_sysconfdir/systemd/system/httpd2.service.d/openstack-dashboard.conf

# Copy everything to /usr/share
mv %buildroot%python3_sitelibdir/openstack_dashboard \
   %buildroot%_datadir/openstack-dashboard
cp manage.py %buildroot%_datadir/openstack-dashboard
rm -rf %buildroot%python_sitelibdir/openstack_dashboard
rm -rf %buildroot%python3_sitelibdir/openstack_dashboard
#find %buildroot%_datadir/openstack-dashboard -name *.pyc -exec rm '{}' \;

# remove unnecessary .po files
find %buildroot -name django.po -exec rm '{}' \;
find %buildroot -name djangojs.po -exec rm '{}' \;

# Move config to /etc, symlink it back to /usr/share
mv %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/local_settings.py.example %buildroot%_sysconfdir/openstack-dashboard/local_settings
ln -s ../../../../../%_sysconfdir/openstack-dashboard/local_settings %buildroot%_datadir/openstack-dashboard/openstack_dashboard/local/local_settings.py

cp openstack_dashboard/conf/*.json %buildroot%_sysconfdir/openstack-dashboard/

# copy static files to %_datadir/openstack-dashboard/static
mkdir -p %buildroot%_datadir/openstack-dashboard/static
cp -a openstack_dashboard/static/* %buildroot%_datadir/openstack-dashboard/static
cp -a horizon/static/* %buildroot%_datadir/openstack-dashboard/static
#cp -a static/* %buildroot%_datadir/openstack-dashboard/static
cp -a openstack_dashboard/themes %buildroot%_datadir/openstack-dashboard/openstack_dashboard/
# ln -r -s %buildroot%_datadir/openstack-dashboard/static/themes %buildroot%_datadir/openstack-dashboard/openstack_dashboard/static/themes

# create /var/run/openstack-dashboard/ and own it
mkdir -p %buildroot%_runtimedir/openstack-dashboard

%pre -n openstack-dashboard
%_sbindir/groupadd -r -f dashboard 2>/dev/null ||:
%_sbindir/useradd -r -g dashboard -G _webserver -c 'OpenStack Dashboard Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/openstack-dashboard dashboard 2>/dev/null ||:

%post -n openstack-dashboard
# ugly hack to set a unique SECRET_KEY
sed -i "/^from horizon.utils import secret_key$/d" /etc/openstack-dashboard/local_settings
sed -i "/^SECRET_KEY.*$/{N;s/^.*$/SECRET_KEY='`openssl rand -hex 10`'/}" /etc/openstack-dashboard/local_settings

%files
%python_sitelibdir/horizon
%python_sitelibdir/horizon-*.egg-info
#%exclude %python_sitelibdir/horizon/conf/*/static
#%exclude %python_sitelibdir/horizon/conf/*/templates
#%exclude %python_sitelibdir/horizon/test/tests
%exclude %python_sitelibdir/horizon/test

%files tests
#%python_sitelibdir/horizon/test/tests
%python_sitelibdir/horizon/test
#%_datadir/openstack-dashboard/openstack_dashboard/karma.conf.js
#%_datadir/openstack-dashboard/openstack_dashboard/test

%files -n python-module-django-openstack-auth
%python_sitelibdir/openstack_auth
%exclude %python_sitelibdir/openstack_auth/tests

%files -n python-module-django-openstack-auth-tests
%python_sitelibdir/openstack_auth/tests

%files -n python3-module-django-%oname
%python3_sitelibdir/horizon
%python3_sitelibdir/horizon-*.egg-info
%exclude %python3_sitelibdir/horizon/test

%files -n python3-module-django-%oname-tests
%python3_sitelibdir/horizon/test
%_datadir/openstack-dashboard/openstack_dashboard/karma.conf.js
%_datadir/openstack-dashboard/openstack_dashboard/test

%files -n python3-module-django-openstack-auth
%python3_sitelibdir/openstack_auth
%exclude %python3_sitelibdir/openstack_auth/tests

%files -n python3-module-django-openstack-auth-tests
%python3_sitelibdir/openstack_auth/tests

%files -n openstack-dashboard
%doc LICENSE README.rst openstack-dashboard-httpd-logging.conf
%_datadir/openstack-dashboard
%exclude %_datadir/openstack-dashboard/openstack_dashboard/test
%exclude %_datadir/openstack-dashboard/openstack_dashboard/karma.conf.js

%dir %attr(0750, root, _webserver) %_sysconfdir/openstack-dashboard
%dir %attr(0770, root, _webserver) %_sharedstatedir/openstack-dashboard
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf
%config(noreplace) %attr(0640, root, _webserver) %_sysconfdir/openstack-dashboard/local_settings
%config(noreplace) %attr(0640, root, _webserver) %_sysconfdir/openstack-dashboard/*.json
%config(noreplace) %_sysconfdir/systemd/system/httpd2.service.d/openstack-dashboard.conf

#%files doc
#%doc html

%changelog
* Wed May 15 2019 Alexey Shabalin <shaba@altlinux.org> 1:14.0.3-alt1
- 14.0.3

* Tue Feb 19 2019 Alexey Shabalin <shaba@altlinux.org> 1:14.0.2-alt2
- fixed apache config for run wsgi.py
- fixed collectstatic and compress static files in systemd drop-in config with python3

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 1:14.0.2-alt1
- 14.0.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:11.0.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1:11.0.3-alt1
- 11.0.3

* Thu Jun 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1:11.0.2-alt1
- 11.0.2
- add tests package

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.3-alt1
- 10.0.3

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.2-alt1
- 10.0.2
- return drop-in config for systemd

* Fri Jan 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.1-alt2
- horizon-stable-newton 20161214

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.1-alt1
- 10.0.1
- delete drop-in config for systemd, use compressed files form rpm package

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.0-alt1
- 10.0.0 Newton release

* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt1
- 9.0.0 Mitaka Release

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.1-alt1
- 8.0.1

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.0-alt1
- 8.0.0 Liberty Release

* Mon Oct 26 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt2
- add patch for utf8 error

* Wed Oct 14 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2
- update patches
- drop auto-enable /etc/httpd2/conf/extra-enabled/openstack-dashboard.conf
- update apache config and run wsgi as user dashboard
- install apache config to /etc/httpd2/conf/sites-available/openstack-dashboard.conf
- add /etc/httpd2/conf/sites-available/openstack-dashboard-ssl.conf
- add drop-in config /etc/systemd/system/httpd2.service.d/openstack-dashboard.conf for apache2

* Wed Sep 16 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt2
- Add Requires: python-module-django-tests

* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt1
- 2015.1.1-alt1

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0b3

* Tue Mar 17 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Sun Sep 07 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt2
- Tests disabled temporary
- 0101-Add-ru-locale-horizon.patch updated
- 0102-CVE-2014-3594.patch added
- AutoReq: yes, nopython for theme subpackage

* Mon Aug 25 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.2-alt1
- 2014.1.2

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt3
- 0101-Add-ru-locale-horizon.patch added

* Wed Aug 06 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt2
- openstack-dashboard.conf: allow /usr/share/openstack-dashboard/static

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- New version (based on Fedora 2014.1.1-1.fc20.src)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 2012.2.3-alt2
- cleanup spec, fix groups
- build with django 1.4.x

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 2012.2.3-alt1
- Initial release for Sisyphus (based on Fedora)
