%define oname ceilometer
%def_without doc

Name: openstack-%oname
Version: 11.0.1
Release: alt1
Epoch: 1
Summary: OpenStack measurement collection service

Group: System/Servers
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source2: ceilometer.logrotate
Source4: ceilometer-rootwrap-sudoers
Source5: openstack-ceilometer-polkit.rules
Source6: ceilometer.conf

Source11: %name-collector.service
Source12: %name-compute.service
Source13: %name-central.service
Source16: %name-notification.service
Source17: %name-ipmi.service
Source18: %name-polling.service
Source20: %name.tmpfiles

Source111: %name-collector.init
Source112: %name-compute.init
Source113: %name-central.init
Source116: %name-notification.init
Source117: %name-ipmi.init
Source118: %name-polling.init

Provides: %name-common = %EVR
Obsoletes: %name-common < %EVR
# Collector service has been removed but not replaced
Provides: %name-collector = %EVR
Obsoletes: %name-collector < %EVR
# api service has been removed
Obsoletes: %name-api

Requires: python3-module-PasteDeploy
Requires(pre):    shadow-utils
Requires: python3-module-ceilometer  = %EVR
Requires: python3-module-oslo.messaging >= 5.2.0
Requires: python3-module-oslo.serialization >= 1.10.0
Requires: python3-module-oslo.utils >= 3.5.0

BuildRequires: /proc
BuildArch: noarch
BuildRequires: crudini
BuildRequires: webserver-common rpm-build-webserver-common rpm-macros-apache2
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-cachetools >= 1.1.0
BuildRequires: python-module-cotyledon >= 1.3.0
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-futurist >= 0.11.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-jsonpath-rw-ext >= 0.1.9
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-monotonic
BuildRequires: python-module-msgpack >= 0.4.0
BuildRequires: python-module-oslo.concurrency >= 3.5.0
BuildRequires: python-module-oslo.config >= 3.22.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.reports >= 0.6.0
BuildRequires: python-module-oslo.rootwrap >= 2.0.0
BuildRequires: python-module-oslo.service >= 0.7.0
BuildRequires: python-module-oslo.messaging >= 5.12.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-pysnmp4 >= 4.2.3
BuildRequires: python-module-glanceclient >= 2.0.0
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-keystoneauth1 >= 2.1.0
BuildRequires: python-module-neutronclient >= 4.2.0
BuildRequires: python-module-novaclient >= 2.29.0
BuildRequires: python-module-swiftclient >= 2.2.0
BuildRequires: python-module-cinderclient >= 1.6.0
BuildRequires: python-module-yaml >= 3.1.0
BuildRequires: python-module-requests >= 2.8.1
BuildRequires: python-module-stevedore >= 1.9.0
BuildRequires: python-module-tenacity >= 3.2.1
BuildRequires: python-module-tooz >= 1.47.0
BuildRequires: python-module-os-xenapi >= 0.1.1

BuildRequires: python-module-oslo.cache >= 1.5.0
BuildRequires: python-module-gnocchiclient >= 3.1.0

BuildRequires: python-module-openstackdocstheme >= 1.11.0
BuildRequires: python-module-reno >= 1.6.2
BuildRequires: python-module-oslo.vmware >= 1.16.0
BuildRequires: python-module-sphinx >= 1.6.2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-cachetools >= 1.1.0
BuildRequires: python3-module-cotyledon >= 1.3.0
BuildRequires: python3-module-futurist >= 0.11.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-jsonpath-rw-ext >= 0.1.9
BuildRequires: python3-module-lxml >= 2.3
BuildRequires: python3-module-monotonic
BuildRequires: python3-module-msgpack >= 0.4.0
BuildRequires: python3-module-oslo.concurrency >= 3.5.0
BuildRequires: python3-module-oslo.config >= 3.22.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-oslo.reports >= 0.6.0
BuildRequires: python3-module-oslo.rootwrap >= 2.0.0
BuildRequires: python3-module-oslo.service >= 0.7.0
BuildRequires: python3-module-oslo.messaging >= 5.12.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-pysnmp4 >= 4.2.3
BuildRequires: python3-module-glanceclient >= 2.0.0
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-keystoneauth1 >= 2.1.0
BuildRequires: python3-module-neutronclient >= 4.2.0
BuildRequires: python3-module-novaclient >= 2.29.0
BuildRequires: python3-module-swiftclient >= 2.2.0
BuildRequires: python3-module-cinderclient >= 1.6.0
BuildRequires: python3-module-yaml >= 3.1.0
BuildRequires: python3-module-requests >= 2.8.1
BuildRequires: python3-module-stevedore >= 1.9.0
BuildRequires: python3-module-tenacity >= 3.2.1
BuildRequires: python3-module-tooz >= 1.47.0
BuildRequires: python3-module-os-xenapi >= 0.1.13

BuildRequires: python3-module-oslo.cache >= 1.5.0
BuildRequires: python3-module-gnocchiclient >= 3.1.0

BuildRequires: python3-module-openstackdocstheme >= 1.11.0
BuildRequires: python3-module-reno >= 1.6.2
BuildRequires: python3-module-oslo.vmware >= 1.16.0
BuildRequires: python3-module-sphinx >= 1.6.2

%description
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

%package -n python-module-%oname
Summary: OpenStack ceilometer python libraries
Group: Development/Python
Requires: python-module-PasteDeploy
Requires: python-module-ceilometerclient
Requires: python-module-keystoneclient
Requires: python-module-keystonemiddleware

%description -n python-module-%oname
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer python library.

%package -n python-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description -n python-module-%oname-tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack ceilometer python3 libraries
Group: Development/Python3
Requires: python3-module-PasteDeploy
Requires: python3-module-ceilometerclient
Requires: python3-module-keystoneclient
Requires: python3-module-keystonemiddleware

%description -n python3-module-%oname
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer python3 library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package compute
Summary: OpenStack ceilometer compute agent
Group: System/Servers
Requires: %name = %EVR
Requires: %name-polling = %EVR
Requires: python3-module-libvirt

%description compute
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer agent for
running on OpenStack compute nodes.

%package central
Summary: OpenStack ceilometer central agent
Group: System/Servers
Requires: %name = %EVR
Requires: %name-polling = %EVR
Requires: python3-module-glanceclient >= 2.0.0
Requires: python3-module-keystoneclient >= 1.6.0
Requires: python3-module-neutronclient >= 4.2.0
Requires: python3-module-novaclient >= 2.29.0
Requires: python3-module-swiftclient >= 2.2.0

%description central
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the central ceilometer agent.

%package notification
Summary: OpenStack ceilometer notification agent
Group: System/Servers
Requires: %name = %EVR

%description notification
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ceilometer notification agent
which pushes metrics to the collector service from the
various OpenStack services.

%package ipmi
Summary: OpenStack ceilometer ipmi agent
Group: System/Servers
Requires: %name = %EVR
Requires: %name-polling = %EVR
Requires: python3-module-keystoneclient >= 1.6.0
Requires: python3-module-neutronclient >= 4.2.0
Requires: python3-module-novaclient >= 2.29.0
Requires: python3-module-oslo.rootwrap >= 2.0.0
Requires: python3-module-tooz >= 1.28.0
Requires: ipmitool

%description ipmi
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains the ipmi agent to be run on OpenStack
nodes from which IPMI sensor data is to be collected directly,
by-passing Ironic's management of baremetal.

%package polling
Summary: OpenStack ceilometer polling agent
Group: System/Servers
Requires: %name = %EVR
Requires: python3-module-glanceclient >= 2.0.0
Requires: python3-module-keystoneclient >= 1.6.0
Requires: python3-module-novaclient >= 2.29.0
Requires: python3-module-swiftclient >= 2.2.0
Requires: python3-module-libvirt

%description polling
Ceilometer aims to deliver a unique point of contact for billing systems to
aquire all counters they need to establish customer billing, across all
current and future OpenStack components. The delivery of counters must
be tracable and auditable, the counters must be easily extensible to support
new projects, and agents doing data collections should be
independent of the overall system.

This package contains the polling service.


%package doc
Summary: Documentation for OpenStack ceilometer
Group: Development/Documentation

%description doc
OpenStack ceilometer provides services to measure and
collect metrics from OpenStack components.

This package contains documentation files for ceilometer.

%prep
%setup -n %oname-%version

find . \( -name .gitignore -o -name .placeholder \) -delete

find ceilometer -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

rm -rf ../python3
cp -a . ../python3

%build
PYTHONPATH=. oslo-config-generator --config-file=etc/ceilometer/ceilometer-config-generator.conf
%python_build
python setup.py compile_catalog -d build/lib/ceilometer/locale

pushd ../python3
%python3_build
popd

%install
%python_install

for f in $(ls -1 %buildroot%_bindir)
    do mv %buildroot%_bindir/$f %buildroot%_bindir/$f.py2
done

pushd ../python3
%python3_install
popd

%if_with doc
# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd doc

SPHINX_DEBUG=1 sphinx-build -b html source build/html
# Fix hidden-file-or-dir warnings
rm -fr build/html/.doctrees build/html/.buildinfo

popd
%endif

# Setup directories
install -d -m 755 %buildroot%_sharedstatedir/ceilometer
install -d -m 755 %buildroot%_cachedir/ceilometer
install -d -m 770 %buildroot%_logdir/ceilometer

# Install config files
install -d -m 755 %buildroot%_sysconfdir/ceilometer
install -d -m 755 %buildroot%_sysconfdir/ceilometer/ceilometer.conf.d
install -d -m 755 %buildroot%_sysconfdir/ceilometer/rootwrap.d
install -d -m 755 %buildroot%_sysconfdir/sudoers.d
install -d -m 755 %buildroot%_sysconfdir/ceilometer/meters.d
install -p -D -m 440 %SOURCE4 %buildroot%_sysconfdir/sudoers.d/ceilometer
install -p -D -m 644 etc/ceilometer/ceilometer.conf %buildroot%_sysconfdir/ceilometer/ceilometer.conf
install -p -D -m 644 etc/ceilometer/{polling.yaml,polling_all.yaml} %buildroot%_sysconfdir/ceilometer/
install -p -D -m 644 etc/ceilometer/rootwrap.conf %buildroot%_sysconfdir/ceilometer/rootwrap.conf
install -p -D -m 644 etc/ceilometer/rootwrap.d/ipmi.filters %buildroot%_sysconfdir/ceilometer/rootwrap.d/ipmi.filters
install -p -D -m 640 ceilometer/pipeline/data/pipeline.yaml %buildroot%_sysconfdir/ceilometer/pipeline.yaml
install -p -D -m 640 ceilometer/pipeline/data/event_pipeline.yaml %buildroot%_sysconfdir/ceilometer/event_pipeline.yaml
install -p -D -m 640 ceilometer/pipeline/data/event_definitions.yaml %buildroot%_sysconfdir/ceilometer/event_definitions.yaml
install -p -D -m 640 ceilometer/publisher/data/gnocchi_resources.yaml %buildroot%_sysconfdir/ceilometer/gnocchi_resources.yaml
install -p -D -m 640 ceilometer/data/meters.d/meters.yaml %buildroot%_sysconfdir/ceilometer/meters.d/meters.yaml

# Install initscripts for services
install -p -D -m 644 %SOURCE12 %buildroot%_unitdir/%name-compute.service
install -p -D -m 644 %SOURCE13 %buildroot%_unitdir/%name-central.service
install -p -D -m 644 %SOURCE16 %buildroot%_unitdir/%name-notification.service
install -p -D -m 644 %SOURCE17 %buildroot%_unitdir/%name-ipmi.service
install -p -D -m 644 %SOURCE18 %buildroot%_unitdir/%name-polling.service
install -p -D -m 644 %SOURCE20 %buildroot%_tmpfilesdir/%name.conf

install -p -D -m 755 %SOURCE112 %buildroot%_initdir/%name-compute
install -p -D -m 755 %SOURCE113 %buildroot%_initdir/%name-central
install -p -D -m 755 %SOURCE116 %buildroot%_initdir/%name-notification
install -p -D -m 755 %SOURCE117 %buildroot%_initdir/%name-ipmi
install -p -D -m 755 %SOURCE117 %buildroot%_initdir/%name-polling

# Install logrotate
install -p -D -m 644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name
# Install pid directory
install -d -m 755 %buildroot%_runtimedir/ceilometer

# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %buildroot%_datadir
rm -f %buildroot%python_sitelibdir/ceilometer/locale/*/LC_*/ceilometer*po
rm -f %buildroot%python_sitelibdir/ceilometer/locale/*pot
mv %buildroot%python_sitelibdir/ceilometer/locale %buildroot%_datadir/locale

# Find language files
%find_lang ceilometer --all-name

install -D -m 644 %SOURCE5 %buildroot%_datadir/polkit-1/rules.d/11-openstack-ceilometer.rules

# Remove unneeded in production stuff
rm -f %buildroot%_bindir/ceilometer-debug
rm -f %buildroot/usr/share/doc/ceilometer/README*
rm -fr %buildroot/usr/etc

%define ceilometer_conf %buildroot%_sysconfdir/ceilometer/ceilometer.conf.d/010-ceilometer.conf
crudini --set %ceilometer_conf DEFAULT log_dir %_logdir/ceilometer
crudini --set %ceilometer_conf DEFAULT state_path /var/lib/ceilometer
crudini --set %ceilometer_conf oslo_concurrency lock_path %_runtimedir/ceilometer

%pre
# 166:166 for ceilometer (openstack-ceilometer)
%_sbindir/groupadd -r -g 166 -f ceilometer 2>/dev/null ||:
%_sbindir/useradd -r -u 166 -g ceilometer -G ceilometer,nobody  -c 'OpenStack Ceilometer Daemons' \
        -s /sbin/nologin  -d %_sharedstatedir/ceilometer ceilometer 2>/dev/null ||:


%post compute
%post_service %name-compute

%post notification
%post_service %name-notification

%post central
%post_service %name-central

%post ipmi
%post_service %name-ipmi

%post polling
%post_service %name-polling

%preun compute
%preun_service %name-compute

%preun notification
%preun_service %name-notification

%preun central
%preun_service %name-central

%preun ipmi
%preun_service %name-ipmi

%preun polling
%preun_service %name-polling

%files -f ceilometer.lang
%doc LICENSE
%dir %_sysconfdir/ceilometer
%dir %_sysconfdir/ceilometer/ceilometer.conf.d
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/ceilometer.conf
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/ceilometer.conf.d/010-ceilometer.conf
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/polling_all.yaml
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/polling.yaml
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/pipeline.yaml
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/gnocchi_resources.yaml
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %attr(0770, root, ceilometer) %_logdir/ceilometer
%dir %attr(0775, root, ceilometer) %_runtimedir/ceilometer
%_tmpfilesdir/%name.conf

%dir %attr(0755, ceilometer, ceilometer) %_sharedstatedir/ceilometer
%dir %attr(0755, ceilometer, ceilometer) %_cachedir/ceilometer

%files -n python-module-%oname
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files -n python-module-%oname-tests
%python_sitelibdir/%oname/tests

%files -n python3-module-%oname
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests

%if_with doc
%files doc
%doc doc/build/html
%endif

%files compute
%_unitdir/%name-compute.service
%_initdir/%name-compute
%_datadir/polkit-1/rules.d/11-openstack-ceilometer.rules

%files notification
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/event_pipeline.yaml
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/event_definitions.yaml
%dir %_sysconfdir/ceilometer/meters.d
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/meters.d/meters.yaml
%_unitdir/%name-notification.service
%_initdir/%name-notification

%files central
%_unitdir/%name-central.service
%_initdir/%name-central

%files ipmi
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/rootwrap.conf
%config(noreplace) %attr(0640, root, ceilometer) %_sysconfdir/ceilometer/rootwrap.d/ipmi.filters
%_sysconfdir/sudoers.d/ceilometer
%_unitdir/%name-ipmi.service
%_initdir/%name-ipmi

%files polling
%_unitdir/%name-polling.service
%_initdir/%name-polling

%changelog
* Fri Jan 11 2019 Alexey Shabalin <shaba@altlinux.org> 1:11.0.1-alt1
- 11.0.1 Rocky release
- switch to python3

* Thu Aug 10 2017 Alexey Shabalin <shaba@altlinux.ru> 1:8.1.0-alt1
- 8.1.0

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.2-alt1
- 8.0.2

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.1-alt2
- drop signing_dir from default config

* Fri Jun 09 2017 Alexey Shabalin <shaba@altlinux.ru> 1:8.0.1-alt1
- 8.0.1 Ocata release

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.3-alt1
- 7.0.3

* Fri Jan 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.1-alt1
- 7.0.1

* Fri Nov 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.0-alt2
- backport patches from stable/newton
- fix logrotate

* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1:7.0.0-alt1
- 7.0.0

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1:5.0.1-alt1
- 5.0.1

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1:5.0.0-alt1
- 5.0.0 Liberty Release
- add apache2 config for ceilometer-api

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.2-alt1
- 2015.1.2

* Fri Aug 28 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.1-alt1
- 2015.1.1
- drop common package
- drop dist config in datadir

* Wed May 20 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0 Kilo Release

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt0.b2.0
- 2015.1.0.b2

* Fri Aug 22 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt2
- Requires: python-module-pymongo >= 2.5.2

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 2014.1.1-alt1
- First build for ALT (based on Fedora 2014.1.1-3.fc21.src)
