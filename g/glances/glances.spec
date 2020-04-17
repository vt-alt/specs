Name: glances
Version: 2.11.1
Release: alt2

Summary: CLI curses based monitoring tool
License: GPLv3
Group: Monitoring
Url: https://github.com/nicolargo/glances
BuildArch: noarch

# Repacked %url/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Requires: python3-module-%name = %EVR

%add_python3_req_skip bernhard
%add_python3_req_skip bottle
%add_python3_req_skip cassandra
%add_python3_req_skip cassandra.cluster
%add_python3_req_skip cassandra.util
%add_python3_req_skip couchdb
%add_python3_req_skip couchdb.mapping
%add_python3_req_skip docker
%add_python3_req_skip elasticsearch
%add_python3_req_skip influxdb
%add_python3_req_skip influxdb.client
%add_python3_req_skip influxdb.influxdb08
%add_python3_req_skip influxdb.influxdb08.client
%add_python3_req_skip kafka
%add_python3_req_skip matplotlib
%add_python3_req_skip netifaces
%add_python3_req_skip nvidia-ml-py3
%add_python3_req_skip pika
%add_python3_req_skip potsdb
%add_python3_req_skip prometheus_client
%add_python3_req_skip py-cpuinfo
%add_python3_req_skip pymdstat
%add_python3_req_skip pysnmp
%add_python3_req_skip pystache
%add_python3_req_skip zmq
%add_python3_req_skip zmq.utils.strtypes
%add_python3_req_skip requests
%add_python3_req_skip scandir
%add_python3_req_skip statsd
%add_python3_req_skip wifi
%add_python3_req_skip zeroconf

%{?!_without_check:%{?!_disable_check:BuildRequires: /proc python3-module-psutil}}


%description
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%package -n python3-module-%name
Summary: CLI curses based monitoring tool
Group: Development/Python3

%description -n python3-module-%name
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%_bindir/glances
%_man1dir/glances.1*

%files -n python3-module-%name
%doc AUTHORS COPYING README.rst NEWS
%python3_sitelibdir/%name/
%python3_sitelibdir/Glances-%version-py%_python3_version.egg-info/


%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.11.1-alt2
- build for python2 disabled

* Wed Oct 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.11.1-alt1
- Initial build.
