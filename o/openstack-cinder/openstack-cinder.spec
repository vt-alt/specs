%def_disable doc
%define oname cinder
%add_python_req_skip hp3parclient

Name: openstack-%oname
Version: 13.0.5
Release: alt1
Epoch: 1
Summary: OpenStack Volume service

Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: cinder-dist.conf
Source2: cinder.logrotate
Source3: cinder-tgt.conf
Source4: %name.tmpfiles
Source5: %name.conf
Source10: openstack-cinder-api.service
Source11: openstack-cinder-scheduler.service
Source12: openstack-cinder-volume.service
Source13: openstack-cinder-backup.service

Source110: openstack-cinder-api.init
Source111: openstack-cinder-scheduler.init
Source112: openstack-cinder-volume.init
Source113: openstack-cinder-backup.init

Source20: cinder-sudoers

Patch: cinder-13.0.2-system-urllib3.patch

BuildArch: noarch
BuildRequires: /proc
BuildRequires: webserver-common rpm-build-webserver-common rpm-macros-apache2
BuildRequires: git-core
BuildRequires: crudini
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-setuptools
BuildRequires: graphviz
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-decorator >= 3.4.0
BuildRequires: python-module-defusedxml >= 0.5.0
BuildRequires: python-module-enum34
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-greenlet >= 0.4.10
BuildRequires: python-module-httplib2 >= 0.9.1
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-jsonschema >= 2.6.0
BuildRequires: python-module-ipaddress >= 1.0.17
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-keystonemiddleware >= 4.17.0
BuildRequires: python-module-lxml >= 3.4.1
BuildRequires: python-module-oauth2client >= 1.5.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.concurrency >= 3.26.0
BuildRequires: python-module-oslo.context >= 2.19.2
BuildRequires: python-module-oslo.db >= 4.27.0
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.messaging >= 5.29.0
BuildRequires: python-module-oslo.middleware >= 3.31.0
BuildRequires: python-module-oslo.policy >= 1.30.0
BuildRequires: python-module-oslo.privsep >= 1.23.0
BuildRequires: python-module-oslo.reports >= 1.18.0
BuildRequires: python-module-oslo.rootwrap >= 5.8.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.service >= 1.24.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python-module-osprofiler >= 1.4.0
BuildRequires: python-module-paramiko >= 2.0.0
BuildRequires: python-module-paste >= 2.0.2
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-psutil >= 3.2.2
BuildRequires: python-module-pyparsing >= 2.1.0
BuildRequires: python-module-barbicanclient >= 4.5.2
BuildRequires: python-module-glanceclient >= 2.8.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-novaclient >= 9.1.0
BuildRequires: python-module-swiftclient >= 3.2.0
BuildRequires: python-module-pytz >= 2013.6
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-urllib3
BuildRequires: python-module-retrying >= 1.2.3
BuildRequires: python-module-routes >= 2.3.1
BuildRequires: python-module-taskflow >= 2.16.0
BuildRequires: python-module-rtslib >= 2.1.65
BuildRequires: python-module-simplejson >= 3.5.1
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-migrate >= 0.11.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-suds-jurko >= 0.6
BuildRequires: python-module-webob >= 1.7.1
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.vmware >= 2.17.0
BuildRequires: python-module-os-brick >= 2.2.0
BuildRequires: python-module-os-win >= 3.0.0
BuildRequires: python-module-tooz >= 1.58.0
BuildRequires: python-module-google-api-client >= 1.4.2
BuildRequires: python-module-castellan >= 0.16.0
BuildRequires: python-module-cryptography >= 2.1
BuildRequires: python-module-cursive >= 0.2.1

%if_enabled doc
BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-doc8 >= 0.6.0
BuildRequires: python-module-os-api-ref >= 1.4.0
BuildRequires: python-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python-module-sphinx-feature-classification >= 0.1.0
%endif
BuildRequires: python-module-testtools
BuildRequires: python-module-subunit-tests


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-decorator >= 3.4.0
BuildRequires: python3-module-defusedxml >= 0.5.0
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-greenlet >= 0.4.10
BuildRequires: python3-module-httplib2 >= 0.9.1
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-ipaddress >= 1.0.17
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-keystonemiddleware >= 4.17.0
BuildRequires: python3-module-lxml >= 3.4.1
BuildRequires: python3-module-oauth2client >= 1.5.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.db >= 4.27.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.middleware >= 3.31.0
BuildRequires: python3-module-oslo.policy >= 1.30.0
BuildRequires: python3-module-oslo.privsep >= 1.23.0
BuildRequires: python3-module-oslo.reports >= 1.18.0
BuildRequires: python3-module-oslo.rootwrap >= 5.8.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-paramiko >= 2.0.0
BuildRequires: python3-module-paste >= 2.0.2
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-psutil >= 3.2.2
BuildRequires: python3-module-pyparsing >= 2.1.0
BuildRequires: python3-module-barbicanclient >= 4.5.2
BuildRequires: python3-module-glanceclient >= 2.8.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-novaclient >= 9.1.0
BuildRequires: python3-module-swiftclient >= 3.2.0
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-retrying >= 1.2.3
BuildRequires: python3-module-routes >= 2.3.1
BuildRequires: python3-module-taskflow >= 2.16.0
BuildRequires: python3-module-rtslib >= 2.1.65
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-migrate >= 0.11.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-suds-jurko >= 0.6
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.vmware >= 2.17.0
BuildRequires: python3-module-os-brick >= 2.2.0
BuildRequires: python3-module-os-win >= 3.0.0
BuildRequires: python3-module-tooz >= 1.58.0
BuildRequires: python3-module-google-api-client >= 1.4.2
BuildRequires: python3-module-castellan >= 0.16.0
BuildRequires: python3-module-cryptography >= 2.1
BuildRequires: python3-module-cursive >= 0.2.1

%if_enabled doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-doc8 >= 0.6.0
BuildRequires: python3-module-os-api-ref >= 1.4.0
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python3-module-sphinx-feature-classification >= 0.1.0
%endif
BuildRequires: python3-module-testtools
BuildRequires: python3-module-subunit-tests


Requires: python3-module-cinder = %EVR
Requires: python3-module-PasteDeploy
Requires: python3-module-osprofiler >= 1.4.0
Requires: python3-module-keystonemiddleware

Requires(pre): shadow-utils

Requires: lvm2
# Requires: scsitarget-utils
Requires: targetcli
Requires: python3-module-rtslib
Requires: sysfsutils
Requires: sudo
Requires: qemu-img

%description
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

%package -n python-module-%oname
Summary: OpenStack Volume Python libraries
Group: Development/Python

%description -n python-module-%oname
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains the cinder Python library.

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python

%description -n python-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack Volume Python libraries
Group: Development/Python3

%description -n python3-module-%oname
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains the cinder Python library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Volume
Group: Development/Documentation

%description doc
OpenStack Volume (codename Cinder) provides services to manage and
access block storage volumes for use by Virtual Machine instances.

This package contains documentation files for cinder.

%prep
%setup -n %oname-%version
%patch -p1

find . \( -name .gitignore -o -name .placeholder \) -delete

find cinder -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

rm -rf ../python3
cp -a . ../python3

%build

%python_build

pushd ../python3
%python3_build
# Generate config file
oslo-config-generator --config-file=tools/config/cinder-config-generator.conf
oslopolicy-sample-generator --config-file=tools/config/cinder-policy-generator.conf

%if_enabled doc
PYTHONPATH=. python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr build/sphinx/html/.buildinfo
%endif
popd

%install
# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/cinder
install -d -m 755 %buildroot%_cachedir/cinder
install -d -m 775 %buildroot%_logdir/cinder

# Install config files
install -d -m 755 %buildroot%_sysconfdir/cinder
install -d -m 755 %buildroot%_sysconfdir/cinder/cinder.conf.d
install -d -m 755 %buildroot%_sysconfdir/cinder/cinder-volume.conf.d
install -d -m 755 %buildroot%_sysconfdir/cinder/volumes
install -d -m 755 %buildroot%_sysconfdir/cinder/rootwrap.d

%python_install
mv %buildroot%_bindir/cinder-api %buildroot%_bindir/cinder-api.py2
mv %buildroot%_bindir/cinder-backup %buildroot%_bindir/cinder-backup.py2
mv %buildroot%_bindir/cinder-manage %buildroot%_bindir/cinder-manage.py2
mv %buildroot%_bindir/cinder-rootwrap %buildroot%_bindir/cinder-rootwrap.py2
mv %buildroot%_bindir/cinder-rtstool %buildroot%_bindir/cinder-rtstool.py2
mv %buildroot%_bindir/cinder-scheduler %buildroot%_bindir/cinder-scheduler.py2
mv %buildroot%_bindir/cinder-volume %buildroot%_bindir/cinder-volume.py2
mv %buildroot%_bindir/cinder-volume-usage-audit %buildroot%_bindir/cinder-volume-usage-audit.py2
mv %buildroot%_bindir/cinder-wsgi %buildroot%_bindir/cinder-wsgi.py2

pushd ../python3
%python3_install
mkdir -p %buildroot%_man1dir
install -p -D -m 640 etc/cinder/cinder.conf.sample %buildroot%_sysconfdir/cinder/cinder.conf
install -p -D -m 640 etc/cinder/policy.yaml.sample %buildroot%_sysconfdir/cinder/policy.yaml
install -p -D -m 644 etc/cinder/{api-paste.ini,rootwrap.conf} %buildroot%_sysconfdir/cinder/
install -p -D -m 644 etc/cinder/rootwrap.d/* %buildroot%_sysconfdir/cinder/rootwrap.d/
popd

# Install config files

install -p -D -m 644 %SOURCE3 %buildroot%_sysconfdir/tgt/conf.d/cinder.conf


# Symlinks to rootwrap config files
for filter in %_sysconfdir/os-brick/rootwrap.d/*.filters; do
ln -s $filter %buildroot%_sysconfdir/cinder/rootwrap.d/
done

# Install initscripts for services
install -p -D -m 644 %SOURCE10 %buildroot%_unitdir/openstack-cinder-api.service
install -p -D -m 644 %SOURCE11 %buildroot%_unitdir/openstack-cinder-scheduler.service
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/openstack-cinder-volume.service
install -p -D -m 644 %SOURCE13 %buildroot%_unitdir/openstack-cinder-backup.service
install -p -D -m 644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf

install -p -D -m 755 %SOURCE110 %buildroot%_initdir/openstack-cinder-api
install -p -D -m 755 %SOURCE111 %buildroot%_initdir/openstack-cinder-scheduler
install -p -D -m 755 %SOURCE112 %buildroot%_initdir/openstack-cinder-volume
install -p -D -m 755 %SOURCE113 %buildroot%_initdir/openstack-cinder-backup

# Install sudoers
install -p -D -m 400 %SOURCE20 %buildroot%_sysconfdir/sudoers.d/cinder

# Install logrotate
install -p -D -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/openstack-cinder

# Install pid directory
install -d -m 755 %buildroot%_runtimedir/cinder

# Install sample HTTPD integration files
install -p -D -m 644 cinder/wsgi/wsgi.py %buildroot%_datadir/cinder/cinder.wsgi
install -p -D -m 644 etc/cinder/api-httpd.conf  %buildroot%_datadir/cinder/

# apache2 settings
install -m 0644 -D -p %SOURCE5 %buildroot%apache2_sites_available/openstack-cinder-api.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/openstack-cinder-api.conf
mkdir -p %buildroot%webserver_cgibindir
ln -s %_datadir/cinder/cinder.wsgi %buildroot%webserver_cgibindir/cinder-osapi_volume

### set default configuration (mostly applies to package-only setups and quickstart, i.e. not generally crowbar)
%define cinder_conf %buildroot%_sysconfdir/cinder/cinder.conf.d/010-cinder.conf
crudini --set %cinder_conf DEFAULT log_dir /var/log/cinder
crudini --set %cinder_conf DEFAULT state_path /var/lib/cinder
crudini --set %cinder_conf oslo_concurrency lock_path /var/run/cinder

# cleanup
rm -rf %buildroot/usr/etc

%pre
# 165:165 for ceilometer (openstack-cinder)
%_sbindir/groupadd -r -g 165 -f cinder 2>/dev/null ||:
%_sbindir/useradd -r -u 165 -g cinder -G cinder,nobody,wheel  -c 'OpenStack Cinder Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/cinder cinder 2>/dev/null ||:

%post
%post_service %name-volume
%post_service %name-api
%post_service %name-scheduler
%post_service %name-backup

%preun
%preun_service %name-volume
%preun_service %name-api
%preun_service %name-scheduler
%preun_service %name-backup

%files
%doc LICENSE
%dir %_sysconfdir/cinder
%dir %_sysconfdir/cinder/cinder.conf.d
%dir %_sysconfdir/cinder/rootwrap.d
%config(noreplace) %attr(0640, root, cinder) %_sysconfdir/cinder/cinder.conf
%config(noreplace) %attr(0640, root, cinder) %_sysconfdir/cinder/cinder.conf.d/010-cinder.conf
%config %attr(0640, root, cinder) %_sysconfdir/cinder/api-paste.ini
%config %_sysconfdir/cinder/rootwrap.conf
%config %_sysconfdir/cinder/policy.yaml
%config(noreplace) %_sysconfdir/logrotate.d/openstack-cinder
%config(noreplace) %_sysconfdir/sudoers.d/cinder
%config(noreplace) %_sysconfdir/tgt/conf.d/cinder.conf
%config(noreplace) %_sysconfdir/cinder/rootwrap.d/*
%dir %_datadir/cinder
%_datadir/cinder/cinder.wsgi
%_datadir/cinder/*.conf
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf
%webserver_cgibindir/*

%dir %attr(0770, root, cinder) %_logdir/cinder
%dir %attr(0755, root, cinder) %_runtimedir/cinder
%dir %attr(0775, root, cinder) %_sysconfdir/cinder/volumes

%_unitdir/*
%_initdir/*
%_tmpfilesdir/*

%dir %attr(0775, root, cinder) %_sharedstatedir/cinder
%dir %attr(0775, root, cinder) %_cachedir/cinder

%files -n python-module-%oname
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/test.*

%files -n python3-module-%oname
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/test.*

%files -n python-module-%oname-tests
%python_sitelibdir/%oname/tests
%python_sitelibdir/%oname/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/test.*

%if_enabled doc
%files doc
%doc ../python3/build/sphinx/html
%endif

%changelog
* Mon May 13 2019 Alexey Shabalin <shaba@altlinux.org> 1:13.0.5-alt1
- 13.0.5
- disbale build docs

* Mon Apr 22 2019 Alexey Shabalin <shaba@altlinux.org> 1:13.0.4-alt1
- 13.0.4

* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 1:13.0.2-alt1
- 13.0.2 Rocky release
- switch to python3

* Fri Jul 14 2017 Lenar Shakirov <snejok@altlinux.ru> 1:10.0.3-alt2
- Requires added:
  * python-module-osprofile
  * python-module-keystonemiddleware

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.3-alt1
- 10.0.3
- drop signing_dir from default config

* Thu Jun 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1:10.0.2-alt1
- 10.0.2 Ocata release
- add tests package

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1:9.1.3-alt1
- 9.1.3

* Thu Feb 09 2017 Alexey Shabalin <shaba@altlinux.ru> 1:9.1.2-alt1
- 9.1.2

* Fri Jan 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1:9.1.1-alt1
- 9.1.1

* Fri Nov 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.1.0-alt1
- 9.1.0
- fix logrotate

* Wed Nov 09 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt2
- fix dir permitions
- update systemd unites

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:9.0.0-alt1
- 9.0.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.0-alt1
- 8.0.0 Mitaka release

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.1-alt1
- 7.0.1

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.0-alt1
- 7.0.0 Liberty release
- add configs for run api over apache2

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Fri Sep 18 2015 Lenar Shakirov <snejok@altlinux.ru> 2015.1.1-alt2
- .service files fixed

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1
- drop dist config in datadir

* Tue May 19 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0 Kilo Release

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b3.0
- 2015.1.0b3

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0b2

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- 2014.1.1

* Sat Aug 09 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt3
- sysfsutils added to Requires: warning about systool

* Tue Aug 05 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt2
- user cinder added to wheel group, for cinder-rootwrap

* Fri Jul 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1-alt1
- Initial build for Sisyphus (based on Fedora)
- New version - icehouse

