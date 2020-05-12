%define oname pyrax

Name: python3-module-%oname
Version: 1.9.8
Release: alt1

Summary: Python language bindings for OpenStack Clouds

License: ASL 2.0
Group: Development/Python3
Url: https://github.com/rackspace/pyrax
BuildArch: noarch

Source: http://imcleod.fedorapeople.org/src/pyrax/pyrax-%version.tar
Patch0: 0001-rename-keyword.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-mock


%description
A library for working with most OpenStack-based cloud deployments, though it
originally targeted the Rackspace public cloud. For example, the code for
cloudfiles contains the ability to publish your content on Rackspace's CDN
network, even though CDN support is not part of OpenStack Swift. But if you
don't use any of the CDN-related code, your app will work fine on any
standard Swift deployment.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A library for working with most OpenStack-based cloud deployments, though it
originally targeted the Rackspace public cloud. For example, the code for
cloudfiles contains the ability to publish your content on Rackspace's CDN
network, even though CDN support is not part of OpenStack Swift. But if you
don't use any of the CDN-related code, your app will work fine on any
standard Swift deployment.

This package contains tests for %oname.

%prep
%setup -n pyrax-%version
%patch0 -p2

%build
sed -i -e 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
       -e 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%python3_build

%install
%python3_install

%files
%doc *.rst LICENSE docs/
%python3_sitelibdir/*


%changelog
* Tue Oct 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.8-alt1
- Version updated to 1.9.8
- python2 -> python3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt2.qa1
- NMU: applied repocop patch

* Thu Jun 16 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt2
- Actually do build me. (%%python_build had been forgotten.)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 29 2014 Ian McLeod <imcleod@redhat.com> - 1.9.0-3
- SPEC change to add missing macros for EPEL 6 builds

* Mon Jul 28 2014 Ian McLeod <imcleod@redhat.com> - 1.9.0-2
- Remove obsolete httplib requirement from SPEC file
- Remove #! execution headers for non-executable components [BZ1123044]
- add inline license for slugify() function to satisfy 3-clause BSD requirements from django [BZ1123044]
- misc additional SPEC change to comply with Fedora package guidelines [BZ1123044]

* Thu Jul 24 2014 Ian McLeod <imcleod@redhat.com> - 1.9.0-1
- Pull in upstream 1.9.0 release

* Fri Sep 6 2013 Greg Swift <gregswift@gmail.com> - 1.5.0-1
- Initial spec
