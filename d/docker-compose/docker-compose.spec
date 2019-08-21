%define oname compose

Name: docker-%oname
Version: 1.24.1
Release: alt1

Summary: Run multi-container applications with Docker

License: %asl
Group: Development/Python
Url: https://github.com/docker/compose

Source: %oname-%version.tar
Patch: %oname-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python3
Requires: python3-module-dockerpty

%description
Compose is a tool for defining and running multi-container applications
with Docker. With Compose, you define a multi-container application in a
single file, then spin your application up in a single command which does
everything that needs to be done to get it running.

%prep
%setup -n %oname-%version
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE README.md
%_bindir/docker-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.org> 1.24.1-alt1
- 1.24.1
- switch to Python 3

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.org> 1.24.0-alt1
- 1.24.0

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.org> 1.23.2-alt1
- 1.23.2

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.org> 1.22.0-alt1
- 1.22.0

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.org> 1.21.2-alt1
- 1.21.2

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.org> 1.20.1-alt1
- 1.20.1

* Wed Jan 17 2018 Vladimir Didenko <cow@altlinux.org> 1.18.0-alt1
- 1.18.0

* Wed Jul 5 2017 Vladimir Didenko <cow@altlinux.org> 1.14.0-alt1
- 1.14.0

* Tue May 16 2017 Vladimir Didenko <cow@altlinux.org> 1.13.0-alt1
- 1.13.0

* Mon Apr 7 2017 Vladimir Didenko <cow@altlinux.org> 1.12.0-alt1
- 1.12.0

* Mon Mar 6 2017 Vladimir Didenko <cow@altlinux.org> 1.11.2-alt1
- 1.11.2

* Fri Feb 10 2017 Vladimir Didenko <cow@altlinux.ru> 1.11.1-alt1
- 1.11.1

* Wed Jan 25 2017 Vladimir Didenko <cow@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Wed Oct 26 2016 Vladimir Didenko <cow@altlinux.ru> 1.8.1-alt2
- add dockerpty to requires

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Wed Aug 3 2016 Vladimir Didenko <cow@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Fri Mar 11 2016 Vladimir Didenko <cow@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Fri Nov 6 2015 Vladimir Didenko <cow@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Oct 13 2015 Vladimir Didenko <cow@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 1.4.0-alt1
- 1.4.0
