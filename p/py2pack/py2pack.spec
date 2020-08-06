%define oname py2pack

Name:       py2pack
Version:    0.8.4
Release:    alt2

Summary:    Generate distribution packages from Python packages on PyPI
License:    GPL-2.0+
Group:      Development/Python3
Url:        http://github.com/saschpe/py2pack
Packager:   Andrey Cherepanov <cas@altlinux.org>

BuildArch:  noarch

Source:     %name-%version.tar
Patch1:     py2pack-alt-spec-support.patch
Patch2:     py2pack-alt-spec-default.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jinja2 python3-module-six
BuildRequires: python3-module-cssselect python3-module-lxml
BuildRequires: python3-module-requests
BuildRequires: python3-module-pbr

Requires: python3-module-py2pack = %version-%release

%description
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%package -n python3-module-py2pack
Summary: General purpose template engine
Group: Development/Python3
%py3_requires pbr

%description -n python3-module-py2pack
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and change logs making it an
universal tool to package Python modules.

%prep
%setup -n %oname-%version
%patch1 -p1
%patch2 -p1

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install

%files
%_bindir/%oname

%files -n python3-module-py2pack
%python3_sitelibdir/%{oname}*

%changelog
* Fri Jul 31 2020 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt2
- Require python3(pbr) for correct version show.
- Add ALT spec template (ALT #38761).
- Use alt.spec template by default.

* Fri Jul 24 2020 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt1
- New version (ALT #38757).
- Fix License tag according to SPDX.
- Build from upstream tag.
- Change maintainer.

* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.4-alt2
- Porting on Python3.

* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6.4-alt1
- new version 0.6.4 (with rpmrb script) from github sources

* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt2
- initial build for ALT Linux Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_4
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_3
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_2
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.17-alt1_4
- update to new release by fcimport

* Sun Dec 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.17-alt1_3
- initial fc import

