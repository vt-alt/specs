# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           GeoLite2-Country
Version: 20191008
Release: alt1
Summary:        Free IP geolocation %name database
License:        CC-BY-SA
Group:          Sciences/Geosciences
URL:            https://dev.maxmind.com/geoip/geoip2/geolite2/
Source0:        https://geolite.maxmind.com/download/geoip/database/%{name}_%{version}.tar.gz
BuildArch:      noarch

# recommends
# Requires:     geoipupdate

%description 
GeoLite2 country database is a free IP geolocation database comparable to, but less
accurate than, MaxMind's GeoIP2 database.

This product includes GeoLite2 data created by MaxMind,
available from http://www.maxmind.com.

%prep
%setup -q -n %{name}_%{version}


%install
install -D -p -m 0644 %{name}.mmdb %{buildroot}%{_datadir}/GeoIP/%{name}.mmdb

%files
%doc --no-dereference COPYRIGHT.txt LICENSE.txt
%dir %{_datadir}/GeoIP
# to allow updates using geoipupdate
%verify(not md5 size mtime) %{_datadir}/GeoIP/%{name}.mmdb

%changelog
* Thu Oct 10 2019 Cronbuild Service <cronbuild@altlinux.org> 20191008-alt1
- repocop cronbuild 20191010. At your service.

* Wed Oct 02 2019 Cronbuild Service <cronbuild@altlinux.org> 20191001-alt1
- repocop cronbuild 20191002. At your service.

* Tue Sep 24 2019 Cronbuild Service <cronbuild@altlinux.org> 20190924-alt1
- repocop cronbuild 20190924. At your service.

* Sun Sep 08 2019 Cronbuild Service <cronbuild@altlinux.org> 20190903-alt1
- repocop cronbuild 20190908. At your service.

* Sat Aug 31 2019 Cronbuild Service <cronbuild@altlinux.org> 20190827-alt1
- repocop cronbuild 20190831. At your service.

* Fri Aug 23 2019 Cronbuild Service <cronbuild@altlinux.org> 20190820-alt1
- repocop cronbuild 20190823. At your service.

* Thu Aug 15 2019 Cronbuild Service <cronbuild@altlinux.org> 20190813-alt1
- repocop cronbuild 20190815. At your service.

* Wed Aug 07 2019 Cronbuild Service <cronbuild@altlinux.org> 20190806-alt1
- repocop cronbuild 20190807. At your service.

* Tue Jul 30 2019 Cronbuild Service <cronbuild@altlinux.org> 20190730-alt1
- repocop cronbuild 20190730. At your service.

* Mon Jul 22 2019 Cronbuild Service <cronbuild@altlinux.org> 20190716-alt1
- repocop cronbuild 20190722. At your service.

* Sun Jul 14 2019 Cronbuild Service <cronbuild@altlinux.org> 20190709-alt1
- repocop cronbuild 20190714. At your service.

* Sat Jul 06 2019 Cronbuild Service <cronbuild@altlinux.org> 20190702-alt1
- repocop cronbuild 20190706. At your service.

* Fri Jun 28 2019 Cronbuild Service <cronbuild@altlinux.org> 20190625-alt1
- repocop cronbuild 20190628. At your service.

* Thu Jun 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190618-alt1
- repocop cronbuild 20190620. At your service.

* Wed Jun 12 2019 Cronbuild Service <cronbuild@altlinux.org> 20190611-alt1
- repocop cronbuild 20190612. At your service.

* Tue Jun 04 2019 Cronbuild Service <cronbuild@altlinux.org> 20190604-alt1
- repocop cronbuild 20190604. At your service.

* Mon May 27 2019 Cronbuild Service <cronbuild@altlinux.org> 20190521-alt1
- repocop cronbuild 20190527. At your service.

* Sun May 19 2019 Cronbuild Service <cronbuild@altlinux.org> 20190514-alt1
- repocop cronbuild 20190519. At your service.

* Sat May 11 2019 Cronbuild Service <cronbuild@altlinux.org> 20190507-alt1
- repocop cronbuild 20190511. At your service.

* Fri May 03 2019 Cronbuild Service <cronbuild@altlinux.org> 20190430-alt1
- repocop cronbuild 20190503. At your service.

* Thu Apr 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20190423-alt1
- repocop cronbuild 20190425. At your service.

* Wed Apr 17 2019 Cronbuild Service <cronbuild@altlinux.org> 20190416-alt1
- repocop cronbuild 20190417. At your service.

* Tue Apr 09 2019 Cronbuild Service <cronbuild@altlinux.org> 20190409-alt1
- repocop cronbuild 20190409. At your service.

* Mon Apr 01 2019 Cronbuild Service <cronbuild@altlinux.org> 20190402-alt1
- repocop cronbuild 20190401. At your service.

* Sun Mar 24 2019 Cronbuild Service <cronbuild@altlinux.org> 20190319-alt1
- repocop cronbuild 20190324. At your service.

* Sat Mar 16 2019 Cronbuild Service <cronbuild@altlinux.org> 20190312-alt1
- repocop cronbuild 20190316. At your service.

* Fri Mar 08 2019 Cronbuild Service <cronbuild@altlinux.org> 20190305-alt1
- repocop cronbuild 20190308. At your service.

* Thu Feb 28 2019 Cronbuild Service <cronbuild@altlinux.org> 20190226-alt1
- repocop cronbuild 20190228. At your service.

* Wed Feb 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190219-alt1
- repocop cronbuild 20190220. At your service.

* Tue Feb 12 2019 Cronbuild Service <cronbuild@altlinux.org> 20190212-alt1
- repocop cronbuild 20190212. At your service.

* Mon Feb 04 2019 Cronbuild Service <cronbuild@altlinux.org> 20190129-alt1
- repocop cronbuild 20190204. At your service.

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 20180925-alt1
- new version
