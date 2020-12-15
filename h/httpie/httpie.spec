%define py3bdir ../%name-%version-python3-build
%define realversion 2.3.0

Name: httpie
Version: 2.3.0
Release: alt3

Summary: A Curl-like tool for humans
Group: Networking/WWW
License: BSD
Url: http://httpie.org
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-Pygments python3-module-requests
BuildRequires: help2man

Requires: python3-module-requests >= 2.11.0
Requires: python3-module-Pygments >= 2.1.3
Requires: python3-module-socks

Obsoletes: httpie-python3 < %EVR

%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%__python3 setup.py build

%install
%__python3 setup.py install --skip-build --root %buildroot

mkdir -p %buildroot/%_man1dir

export PYTHONPATH=%buildroot%python3_sitelibdir
help2man --no-discard-stderr %buildroot/%_bindir/http > %buildroot/%_man1dir/http.1
help2man --no-discard-stderr %buildroot/%_bindir/https > %buildroot/%_man1dir/https.1

%files
%_bindir/http
%_bindir/https
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%{realversion}*
%_man1dir/http.1*
%_man1dir/https.1*
%doc LICENSE README.rst


%changelog
* Mon Dec 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt3
- Updated runtime dependencies.

* Fri Dec 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt2
- Updated obsoletes.
- Stopped renaming binaries and man pages.

* Wed Dec 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0 (Fixes: CVE-2019-10751).

* Sat Dec 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.9-alt2
- build for python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1.qa1
- NMU: applied repocop patch

* Fri Sep 21 2018 Terechkov Evgenii <evg@altlinux.org> 0.9.9-alt1
- 0.9.9

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.8-alt3
- Fixed FTBFS (Add BR python3-module-setuptools).

* Wed Jul 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.8-alt2
- Update requires
- Added patch - fixed import 'urllib3'

* Wed Jul 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.8-alt1
- Build new version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Sep  6 2014 Terechkov Evgenii <evg@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux Sisyphus
