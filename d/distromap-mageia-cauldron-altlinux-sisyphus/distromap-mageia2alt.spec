%define orepo mageia
%define obranch cauldron
%define module %orepo-%obranch-altlinux-sisyphus

Name: distromap-%module
Version: 0.046
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module DistroMap database
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
Url: http://repocop.altlinux.org/

Requires: distromap-generic-default-altlinux-sisyphus
Requires: distrodb-static-altlinux-sisyphus

%description
%summary

%prep
%setup

%build

%install
destdir=%buildroot/usr/share/distromap/%orepo/%obranch/altlinux/sisyphus
for type in source binary group-strict group-approx; do
    if [ -d $type ] && stat -t $type/* >/dev/null 2>&1 ; then
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
    fi
done
ln -s %obranch %buildroot/usr/share/distromap/%orepo/default
for type in binary source ; do
    for flag in flags/$type/* ; do
	if [ -d $flag ] && stat -t $flag/* >/dev/null 2>&1 ; then
	    install -m755 -d $destdir/$flag
	    install -m644 $flag/* $destdir/$flag/
	fi
    done
done

%files
/usr/share/distromap/*

%changelog
* Fri Sep 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1
- db update

* Fri Jul 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.045-alt1
- db update

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- db update

* Sat Apr 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.043-alt1
- db update

* Wed Mar 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1
- db update

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.041-alt1
- db update

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- db update

* Tue Jan 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1
- db update

* Sat Dec 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- db update

* Wed Dec 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.037-alt1
- db update

* Sat Oct 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- db update

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.035-alt1
- db update

* Sun Sep 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.034-alt1
- db update

* Mon Jul 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.033-alt1
- db update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- db update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1
- db update

* Mon Jun 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- db update

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1
- db update

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- fixes for cas packages

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.027-alt1
- db update

* Sat May 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- db update

* Tue Apr 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- db update

* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- db update

* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- db update

* Wed Mar 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- db update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- db update

* Sat Feb 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- db update

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- db update

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- db update

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- db update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- db update

* Thu Oct 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- db update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- db update

* Mon Feb 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- db update

* Mon Jan 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- db update

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- db update

* Thu Nov 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- db update
