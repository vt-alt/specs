# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/guile /usr/bin/indent libreadline-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# spec file for package libctl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libctl
Version:        4.2.0
Release:        alt1_1.4
%define somajor 7
Summary:        A guile Library for Scientific Simulations
License:        GPL-2.0-or-later
Group:          Development/Other
Url:            http://ab-initio.mit.edu/wiki/index.php/Libctl
Source0:        https://github.com/stevengj/libctl/releases/download/v%{version}/libctl-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-fortran
BuildRequires:  guile22-devel
BuildRequires:  libtool
BuildRequires:  libnlopt-devel
BuildRequires:  pkg-config
Source44: import.info

%description
libctl is a free Guile-based library implementing flexible control files
for scientific simulations. It was written to support MIT Photonic Bands
and Meep software, but has proven useful in other programs too.

%package -n     %{name}%{somajor}
Summary:        A guile Library for Scientific Simulations
Group:          System/Libraries

%description -n %{name}%{somajor}
libctl is a free Guile-based library implementing flexible control files
for scientific simulations. It was written to support MIT Photonic Bands
and Meep software, but has proven useful in other programs too.

%package        devel
Summary:        Libraries and header files for libctl library
Group:          Development/Other
Requires:       %{name}%{somajor} = %{version}
Requires:     %{name}-doc = %{version}

%description    devel
libctl is a free Guile-based library implementing flexible control files
for scientific simulations. It was written to support MIT Photonic Bands
and Meep software, but has proven useful in other programs too.

This package contains libraries and header files for developing
applications that use libctl.

%package        doc
Summary:        Documentation for libctl library
Group:          Documentation
BuildArch: noarch

%description    doc
libctl is a free Guile-based library implementing flexible control files
for scientific simulations. It was written to support MIT Photonic Bands
and Meep software, but has proven useful in other programs too.

This package contains documentation for libctl library.

%prep
%setup -q

%build
autoreconf -fi
%configure --enable-shared --disable-static --disable-rpath F77=gfortran
make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -delete -print

install -d %{buildroot}%{_docdir}/%{name}/
install -m 644 {AUTHORS,COPYING,NEWS.md,README.md} %{buildroot}%{_docdir}/%{name}/
cp -r doc/ %{buildroot}%{_docdir}/%{name}/

%files -n %{name}%{somajor}
%{_libdir}/libctl*.so.*

%files devel
%{_bindir}/gen-ctl-io
%{_libdir}/libctl*.so
%{_datadir}/libctl/
%{_includedir}/*
%{_mandir}/man1/gen-ctl-io.1*

%files doc
%{_docdir}/%{name}/

%changelog
* Sat Jul 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_1.4
- new version

* Fri Sep 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.2-alt2_3
- NMU: updated build dependencies.

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.2-alt1_3
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 3.2.2-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_2
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_1
- update to new release by fcimport

* Tue Oct 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.1-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_1
- initial import by fcimport

