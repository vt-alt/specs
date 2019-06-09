%define  modulename umsgpack
%define  srcname u-msgpack-python

%python_req_hier

Name:    python-module-%modulename
Version: 2.5.1
Release: alt1

Summary: A portable, lightweight MessagePack serializer and deserializer
License: MIT
Group:   Development/Python
URL:     https://github.com/vsergeev/u-msgpack-python

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

BuildArch: noarch

Source:  %srcname-%version.tar

%description
u-msgpack-python is a lightweight MessagePack serializer and deserializer
module written in pure Python, compatible with both Python 2 and 3, as
well CPython and PyPy implementations of Python. u-msgpack-python is fully
compliant with the latest MessagePack specification. In particular, it
supports the new binary, UTF-8 string, application-defined ext, and
timestamp types.


%package -n python3-module-%modulename
Summary: A portable, lightweight MessagePack serializer and deserializer
Group: Development/Python3

%description -n python3-module-%modulename
u-msgpack-python is a lightweight MessagePack serializer and deserializer
module written in pure Python, compatible with both Python 2 and 3, as
well CPython and PyPy implementations of Python. u-msgpack-python is fully
compliant with the latest MessagePack specification. In particular, it
supports the new binary, UTF-8 string, application-defined ext, and
timestamp types.
Python 3 version.


%prep
%setup -n %srcname-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/%modulename.py*
%python_sitelibdir/*.egg-info

%files -n python3-module-%modulename
%python3_sitelibdir/%modulename.py*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/*.egg-info

%changelog
* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 2.5.1-alt1
- new version 2.5.1

* Tue Aug 21 2018 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
