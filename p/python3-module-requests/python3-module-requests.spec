%define _unpackaged_files_terminate_build 1
%define pkgname requests

%def_disable check

Name:           python3-module-%pkgname
Version:        2.23.0
Release:        alt1
Summary:        HTTP library, written in Python, for human beings
Group:          Development/Python3

License:        ASL 2.0
URL:            https://pypi.io/project/requests
Source0:        %pkgname-%version.tar
# Explicitly use the system certificates in ca-certificates.
# https://bugzilla.redhat.com/show_bug.cgi?id=904614
Patch0:         patch-requests-certs.py-to-use-the-system-CA-bundle.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1450608
Patch2:         Remove-tests-that-use-the-tarpit.patch

# Use 127.0.0.1 not localhost for socket.bind() in the Server test
# class, to fix tests in Koji's no-network environment
# This probably isn't really upstreamable, because I guess localhost
# could technically be IPv6 or something, and our no-network env is
# a pretty odd one so this is a niche requirement.
Patch3:         requests-2.12.4-tests_nonet.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1567862
Patch4:         Don-t-inject-pyopenssl-into-urllib3.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1653223
Patch5:         requests-2.20.0-no-py2-httpbin.patch

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-chardet
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-urllib3
%{?_enable_check:BuildRequires: python3-module-httpbin}
%py3_requires json

%description
Most existing Python modules for sending HTTP requests are extremely verbose and
cumbersome. Python's built-in urllib2 module provides most of the HTTP
capabilities you should need, but the API is thoroughly broken. This library is
designed to make HTTP requests easy for developers.

%prep
%setup -n %pkgname-%version

%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Unbundle the certificate bundle from mozilla.
rm -rf requests/cacert.pem

%build
%python3_build

%install
%python3_install

%files
%doc AUTHORS.rst HISTORY.md README.md
%python3_sitelibdir/*

%changelog
* Thu Mar 19 2020 Alexey Shabalin <shaba@altlinux.org> 2.23.0-alt1
- 2.23.0
- build as python3 module

* Sat Oct 05 2019 Anton Farygin <rider@altlinux.ru> 2.22.0-alt1
- 2.22.0

* Mon Dec 24 2018 Alexey Shabalin <shaba@altlinux.org> 2.21.0-alt1
- 2.21.0

* Fri Jul 06 2018 Dmitry V. Levin <ldv@altlinux.org> 2.19.1-alt1
- Emergency NMU: 2.18.4 -> 2.19.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.18.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.18.4-alt1
- New version

* Wed Sep 27 2017 Andrey Cherepanov <cas@altlinux.org> 2.12.4-alt5
- Do not remove bundled chardet and urllib3 libraries

* Mon Feb 27 2017 Michael Shigorin <mike@altlinux.org> 2.12.4-alt4
- BOOTSTRAP: introduce check knob (*off* by default),
  put (unused) BR: python-module-httpbin under it

* Mon Jan 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt3
- removed bundled idna

* Mon Jan 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt2
- updated urllib3 patches

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.12.4-alt1
- automated PyPI update

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.0-alt1.git20150719.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.0-alt1.git20150719.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.7.0-alt1.git20150719.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20150719
- Version 2.7.0

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.git20150316
- Version 2.6.0

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20150204
- New snapshot

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20150109
- New snapshot

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20141223
- Version 2.5.1

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20141216
- Version 2.5.0

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2.git20141107
- New snapshot

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt2.git20141101
- I took it

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.3-alt1.git20141101
- Version 2.4.3 (ALT #30439)

* Tue Jul 22 2014 Lenar Shakirov <snejok@altlinux.ru> 2.3.0-alt1
- New version (based on Fedora - 2.3.0-2.fc21.src)
- Unbundle urllib3 and chardet packages (use system modules)

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.12.1-alt1.1
- Rebuild with Python-3.3

* Fri May 18 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.1-alt1
- initial
