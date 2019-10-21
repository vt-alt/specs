%define module fedora-rawhide-altlinux-sisyphus

Name: distromap-%module
Version: 0.443
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
destdir=%buildroot/usr/share/distromap/fedora/rawhide/altlinux/sisyphus
for type in binary source group-strict group-approx; do
    if [ -d $type ] && stat -t $type/* >/dev/null 2>&1 ; then
	install -m755 -d $destdir/$type
	install -m644 $type/* $destdir/$type/
    fi
done
ln -s rawhide %buildroot/usr/share/distromap/fedora/default
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
* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.443-alt1
- db update

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.442-alt1
- db update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.441-alt1
- db update

* Fri Jul 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.440-alt1
- db updates

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.439-alt1
- db updates

* Sat Apr 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.438-alt1
- db updates

* Wed Mar 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.437-alt1
- db updates

* Mon Mar 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.436-alt1
- db updates

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.435-alt1
- db updates

* Tue Jan 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.434-alt1
- db updates

* Sat Dec 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.433-alt1
- db updates

* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.432-alt1
- db updates

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.431-alt1
- db updates

* Sun Sep 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.430-alt1
- db updates

* Mon Jul 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.429-alt1
- db updates

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.428-alt1
- db updates

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.427-alt1
- db updates

* Mon Jun 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.426-alt1
- db updates

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.425-alt1
- db updates

* Fri May 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.424-alt1
- db updates

* Sat May 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.423-alt1
- db updates

* Tue Apr 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.422-alt1
- db updates

* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.421-alt1
- db updates

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.420-alt1
- added rename for clac thanks to obirvalger@

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.419-alt1
- db updates

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.418-alt1
- db updates

* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.417-alt1
- db updates

* Wed Dec 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.416-alt1
- db updates

* Tue Dec 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.415-alt1
- db updates

* Sun Dec 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.414-alt1
- db updates

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.413-alt1
- db updates

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.412-alt1
- db updates

* Thu Oct 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.411-alt1
- db updates

* Sat Sep 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.410-alt1
- db updates

* Thu Feb 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.409-alt1
- db updates

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.408-alt1
- db updates

* Mon Jan 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.407-alt1
- db updates

* Fri Dec 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.406-alt1
- db updates

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.405-alt1
- db updates

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.404-alt1
- db updates

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.403-alt1
- db updates

* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.402-alt1
- db updates

* Fri Oct 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.401-alt1
- db updates

* Wed Oct 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.400-alt1
- db updates (Jubilee)
