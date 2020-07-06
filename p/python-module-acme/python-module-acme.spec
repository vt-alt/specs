%define modulename acme

%def_with python3
%def_without python2

Name: python-module-acme
Version: 1.5.0
Release: alt1

Summary: Python library for the ACME protocol

License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/acme

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/a/%modulename/%modulename-%version.tar.gz
Source: %modulename-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools
#BuildRequires: python-sphinx
#BuildRequires: python-sphinxcontrib-programoutput
#BuildRequires: python-sphinx_rtd_theme
#BuildRequires: python-pyrfc3339
#BuildRequires: python-werkzeug

# requires list checked 06.10.2017 with https://pypi.python.org/pypi/acme
# requests[security] is requests with extra pyOpenSSL cryptography idna
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-OpenSSL >= 0.14
BuildRequires: python-module-cryptography >= 1.3.4
BuildRequires: python-module-idna >= 2.0.0
BuildRequires: python-module-cffi >= 1.7
BuildRequires: python-module-requests >= 2.10
BuildRequires: python-module-pytz
#BuildRequires: python-module-pyrfc3339

Requires: python-module-six >= 1.9.0
Requires: python-module-OpenSSL >= 0.14
Requires: python-module-cryptography >= 1.3.4
Requires: python-module-idna >= 2.0.0
Requires: python-module-cffi >= 1.7
Requires: python-module-requests >= 2.10
Requires: python-module-josepy >= 1.0.0
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
#BuildRequires: python3-sphinx
#BuildRequires: python3-sphinxcontrib-programoutput

# requests[security] is requests with extra pyOpenSSL cryptography idna
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-OpenSSL >= 0.14
BuildRequires: python3-module-cryptography >= 1.3.4
BuildRequires: python3-module-idna >= 2.0.0
BuildRequires: python3-module-cffi >= 1.7
BuildRequires: python3-module-requests >= 2.10
BuildRequires: python3-module-pytz
#BuildRequires: python3-module-pyrfc3339
#BuildRequires: python3-werkzeug
%endif

# Required for testing
#BuildRequires: python-ndg_httpsclient
#BuildRequires: python-nose
#BuildRequires: python-tox
#BuildRequires: python-mock
#BuildRequires: pytz

#%if_with python3
#BuildRequires: python3-ndg_httpsclient
#BuildRequires: python3-nose
#BuildRequires: python3-tox
#BuildRequires: python3-mock
#BuildRequires: python3-pytz
#%endif

BuildArch: noarch

%description
Python libraries implementing the Automatic Certificate Management Environment
(ACME) protocol. It is used by the Certbot Project.

#%package -n python-module-acme
#Group: Development/Python
#Summary: %summary
#Requires: python-cryptography
#Requires: python-ndg_httpsclient
#Requires: python-pyasn1
#Requires: pyOpenSSL >= 0.13
#Requires: python-pyrfc3339
#Requires: pytz
#Requires: python-requests
#Requires: python-six
#Requires: python-werkzeug
#%if_with python3
# Recommends not supported by rpm on EL7
#Recommends: python-acme-doc
#%endif

#%description -n python-module-acme
#Python 2 library for use of the Automatic Certificate Management Environment
#protocol as defined by the IETF. It's used by the Let's Encrypt project.

%if_with python3
%package -n python3-module-acme
Group: Development/Python
Summary: %summary

Requires: python3-module-OpenSSL >= 0.14
Requires: python3-module-cryptography >= 1.3.4
Requires: python3-module-idna >= 2.0.0
Requires: python3-module-cffi >= 1.7
Requires: python3-module-requests >= 2.10
#Requires: python3-ndg_httpsclient
#Requires: python3-pyasn1
#Requires: python3-pyOpenSSL
#Requires: python3-pyrfc3339
#Requires: python3-pytz
#Requires: python3-requests
#Requires: python3-six
#Requires: python3-werkzeug
#Recommends: python-acme-doc

%description -n python3-module-acme
Python 3 library for use of the Automatic Certificate Management Environment
protocol as defined by the IETF. It's used by the Certbot Project.
%endif

%package doc
Group: Development/Python
#Provides: bundled(jquery)
#Provides: bundled(underscore)
#Provides: bundled(inconsolata-fonts)
#Provides: bundled(lato-fonts)
#Provides: bundled(robotoslab-fonts)
#Requires: fontawesome-fonts fontawesome-fonts-web
Summary: Documentation for python-acme libraries

%description doc
Documentation for the ACME python libraries

%prep
%setup -n %modulename-%version

%build
%if_with python2
%python_build
%endif
%if_with python3
%python3_build
%endif

%install
%if_with python3
# Do python3 first so bin ends up from py2
%python3_install
#  it is better do not to require argparse on python >= 2.7.
%__subst "s|^argparse$||" \
    %buildroot%python3_sitelibdir/%modulename-%{version}*.egg-info/requires.txt
%endif

%if_with python2
%python_install
#  it is better do not to require argparse on python >= 2.7.
%__subst "s|^argparse$||" \
    %buildroot%python2_sitelibdir/%modulename-%{version}*.egg-info/requires.txt
%endif


%check
#__python setup.py test
#if_with python3
#__python3 setup.py test
#endif

%if_with python2
%files
%doc LICENSE.txt
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%{version}*.egg-info
%endif

%if_with python3
%files -n python3-module-acme
%doc LICENSE.txt
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%{version}*.egg-info
%endif

#%files doc
#%doc LICENSE.txt
#%doc README.rst
#%doc docs/_build/html

%changelog
* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Fri Feb 14 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)
- disable python2 module build

* Sat Oct 26 2019 Vitaly Lipatov <lav@altlinux.ru> 0.39.0-alt1
- new version 0.39.0 (with rpmrb script)

* Tue Sep 17 2019 Vitaly Lipatov <lav@altlinux.ru> 0.38.0-alt1
- new version 0.38.0 (with rpmrb script)

* Fri Aug 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.37.2-alt1
- new version 0.37.2 (with rpmrb script)

* Fri Aug 16 2019 Vitaly Lipatov <lav@altlinux.ru> 0.37.1-alt1
- new version 0.37.1 (with rpmrb script)

* Fri Jun 28 2019 Vitaly Lipatov <lav@altlinux.ru> 0.35.1-alt1
- new version 0.35.1 (with rpmrb script)

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 0.34.2-alt1
- new version 0.34.2 (with rpmrb script)

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 0.32.0-alt1
- new version 0.32.0 (with rpmrb script)

* Sat Feb 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.31.0-alt1
- new version 0.31.0 (with rpmrb script)

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 0.30.2-alt1
- new version 0.30.2 (with rpmrb script)

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 0.29.1-alt1
- new version 0.29.1 (with rpmrb script)

* Sat Nov 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.28.0-alt1
- new version 0.28.0 (with rpmrb script)

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 0.27.1-alt1
- new version 0.27.1 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.26.1-alt1
- new version 0.26.1 (with rpmrb script)

* Fri Jun 22 2018 Vitaly Lipatov <lav@altlinux.ru> 0.25.1-alt1
- new version 0.25.1 (with rpmrb script)

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 0.24.0-alt1
- new version 0.24.0 (with rpmrb script)

* Sat Mar 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.22.2-alt1
- new version 0.22.2 (with rpmrb script)

* Thu Mar 15 2018 Vitaly Lipatov <lav@altlinux.ru> 0.22.0-alt1
- new version 0.22.0 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.21.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt1
- new version 0.21.0 (with rpmrb script)

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.19.0-alt1
- new version 0.19.0 (with rpmrb script)

* Tue Aug 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.2-alt1
- new version 0.14.2 (with rpmrb script)

* Sat Aug 05 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt4
- add missed cffi requires

* Wed Aug 02 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt3
- improve requires according to new python module requires

* Fri Jul 28 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt2
- improve require requires[security]

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt1
- new version 0.14.1 (with rpmrb script)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Fri Mar 10 2017 Terechkov Evgenii <evg@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Fri Oct 07 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version (0.9.1) with rpmgs script

* Thu Aug 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1

* Thu Apr 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Fri Mar 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- new version 0.4.2 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 16 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 11 2016 Nick Bebout <nb@fedoraproject.org> - 0.4.0-1
- Upgrade to 0.4.0
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Nick Bebout <nb@fedoraproject.org> - 0.3.0-1
- Upgrade to 0.3.0
* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-1
- Upgrade to 0.2.0
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- Upgrade to 0.1.1
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-3
- Restore missing dependencies causing a FTBFS with py3 tests
- Add the man pages
* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.1.0-4
- Specify more of the EPEL dependencies
* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 0.1.0-3
- epel7: Only build python2 package
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Fix up the removal of the dev release snapshot
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Mon Nov 30 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3-dev20151123
- Update spec with comments from review
* Sat Nov 28 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec with comments from review
- Add python3 library
* Fri Nov 27 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-1.dev20151123
- initial packaging
