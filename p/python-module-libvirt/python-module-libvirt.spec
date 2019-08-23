
Summary: Python bindings for the libvirt library
Name: python-module-libvirt
Version: 5.6.0
Release: alt1
Url: http://libvirt.org
#git://libvirt.org/libvirt-python.git
Source: %name-%version.tar
License: LGPLv2+
Group: Development/Python

Requires: libvirt-client
BuildRequires: libvirt-devel >= 2.0.0
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: python-devel python3-devel

Obsoletes: libvirt-python < %version-%release
Provides: libvirt-python = %version-%release

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%package -n python3-module-libvirt
Summary: The libvirt virtualization API python3 binding
License: LGPLv2+
Group: Development/Python3
Obsoletes: libvirt-python3 < %version-%release
Provides: libvirt-python3 = %version-%release

%description -n python3-module-libvirt
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep
%setup -q

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/*
%doc  NEWS README COPYING COPYING.LESSER examples

%files -n python3-module-libvirt
%python3_sitelibdir/*
%doc  NEWS README COPYING COPYING.LESSER examples

%changelog
* Sat Aug 24 2019 Alexey Shabalin <shaba@altlinux.org> 5.6.0-alt1
- new version 5.6.0

* Mon Jul 08 2019 Alexey Shabalin <shaba@altlinux.org> 5.5.0-alt1
- 5.5.0

* Tue Jun 04 2019 Alexey Shabalin <shaba@altlinux.org> 5.4.0-alt1
- 5.4.0

* Sat Apr 06 2019 Alexey Shabalin <shaba@altlinux.org> 5.2.0-alt1
- 5.2.0

* Sun Mar 24 2019 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- 5.1.0

* Thu Jan 31 2019 Alexey Shabalin <shaba@altlinux.org> 5.0.0-alt1
- new version 5.0.0

* Wed Jan 02 2019 Alexey Shabalin <shaba@altlinux.org> 4.10.0-alt1
- 4.10.0

* Tue Oct 09 2018 Alexey Shabalin <shaba@altlinux.org> 4.8.0-alt1
- new version 4.8.0

* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 4.7.0-alt1%ubt
- 4.7.0

* Sun Aug 12 2018 Alexey Shabalin <shaba@altlinux.org> 4.6.0-alt1%ubt
- 4.6.0

* Wed Jul 11 2018 Alexey Shabalin <shaba@altlinux.ru> 4.5.0-alt1%ubt
- 4.5.0

* Tue Jun 05 2018 Alexey Shabalin <shaba@altlinux.ru> 4.4.0-alt1%ubt
- 4.4.0

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.0-alt2%ubt
- (NMU) Rebuilt with python-3.6.4.

* Sun Apr 01 2018 Alexey Shabalin <shaba@altlinux.ru> 4.2.0-alt1%ubt
- 4.2.0

* Wed Feb 07 2018 Alexey Shabalin <shaba@altlinux.ru> 4.0.0-alt1%ubt
- 4.0.0

* Fri Dec 08 2017 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1%ubt
- 3.10.0

* Mon Sep 04 2017 Alexey Shabalin <shaba@altlinux.ru> 3.7.0-alt1%ubt
- 3.7.0

* Wed Aug 09 2017 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1%ubt
- 3.6.0

* Wed Jul 12 2017 Alexey Shabalin <shaba@altlinux.ru> 3.5.0-alt1
- 3.5.0

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Fri Apr 14 2017 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Thu Mar 09 2017 Alexey Shabalin <shaba@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Fri Jan 27 2017 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Wed Dec 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sat Nov 05 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Fri Oct 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Aug 25 2016 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Wed Jun 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Wed May 25 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Dec 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Fri Nov 06 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.21-alt1
- 1.2.21

* Thu Oct 22 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.20-alt1
- 1.2.20

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.18-alt1
- 1.2.18

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.13-alt1
- 1.2.13

* Fri Jul 04 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Jun 10 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Thu Apr 03 2014 Alexey Shabalin <shaba@altlinux.ru> 1.2.3-alt1
- 1.2.3
- add python3 package

* Mon Dec 02 2013 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- initial build; split off from main libvirt package
