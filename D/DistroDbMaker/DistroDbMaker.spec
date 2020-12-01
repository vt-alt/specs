%define oname DistroDbMaker

Name: %oname
Version: 0.030
Release: alt1
Summary: DistroDb Maker tools
License: LGPLv2+
Group: Development/Python
Url: https://www.altlinux.org/Packaging_Automation/DistroDb

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
Requires: python3-module-rpm

Conflicts: distrodb-utils < 0.21
Conflicts: python-module-DistroDbMaker < 0.027
Obsoletes: python-module-DistroDbMaker < 0.027

%description
%summary

%package -n python3-module-%oname
Summary: DistroDb Maker tools
Group: Development/Python3
#py3_provides %oname

%description -n python3-module-%oname
%summary

%prep
%setup

%build
sed -i 1s,/usr/bin/python,/usr/bin/python3, *.py
%python3_build_debug

%install
%python3_install

%files
%_bindir/*

%files -n python3-module-%oname
%python3_sitelibdir/*

%changelog
* Thu Nov 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- new version

* Wed Nov 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1
- dropped python2 support

* Tue Nov 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- python3 bugfixes

* Sat Nov 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1
- switched to python3

* Fri Nov 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- python3 support

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- new version

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- new version

* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- new version

* Sat Dec 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- new version

* Wed Dec 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- new version

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- new version

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- new version

* Sat May 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- new version

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- new version

* Sat May 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- new version

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- new version

* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- added ocaml,erlang,nodejs

* Tue Mar 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- added festival,mate,nagios,golang

* Mon Mar 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- added gimp and cups

* Fri Mar 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- added mono.raw

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- added shared-data.raw

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- cmake fixes

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- filtered out mageia multiarch dir

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- added filters

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- added java.raw

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- exclude doc from texmf

* Sun Feb 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- mageia texlive support

* Fri Feb 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- alt support

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- xz list support

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- Initial build for Sisyphus
