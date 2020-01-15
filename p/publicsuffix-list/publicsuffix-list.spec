%def_enable dafsa

Name: publicsuffix-list
Version: 20200106
Release: alt1
Summary: Cross-vendor public domain suffix database
License: MPL-2.0
Group: Networking/DNS
Url: https://publicsuffix.org/
Vcs: https://github.com/publicsuffix/list.git
Source0: public_suffix_list.dat
Source1: LICENSE
Source2: test_psl.txt
BuildArch: noarch

%{?_enable_dafsa:BuildRequires: psl-make-dafsa}

%description
A "public suffix" is one under which Internet users can (or historically could)
directly register names. Some examples of public suffixes are .com, .co.uk and
pvt.k12.ma.us. The Public Suffix List is a list of all known public suffixes.

%package dafsa
Group: Networking/DNS
Summary: Cross-vendor public domain suffix database in DAFSA form

%description dafsa
A "public suffix" is one under which Internet users can (or historically could)
directly register names. Some examples of public suffixes are .com, .co.uk and
pvt.k12.ma.us. The Public Suffix List is a list of all known public suffixes.

This package includes a DAFSA representation of the Public Suffix List
for runtime loading.

%prep
%setup -c -T
cp -a %SOURCE1 COPYING
%if_enabled dafsa
cp -a %SOURCE0 .

%build
LC_CTYPE=C.UTF-8 \
	psl-make-dafsa --output-format=binary \
	  %SOURCE0 public_suffix_list.dafsa
%endif

%install
install -pDm644  %SOURCE0 %buildroot%_datadir/publicsuffix/public_suffix_list.dat
install -pDm644  %SOURCE2 %buildroot%_datadir/publicsuffix/test_psl.txt
ln -s public_suffix_list.dat %buildroot%_datadir/publicsuffix/effective_tld_names.dat
%if_enabled dafsa
install -pDm644 public_suffix_list.dafsa %buildroot%_datadir/publicsuffix/public_suffix_list.dafsa
%endif

%files
%doc COPYING
%dir %_datadir/publicsuffix/
%_datadir/publicsuffix/*
%if_enabled dafsa
%exclude %_datadir/publicsuffix/public_suffix_list.dafsa

%files dafsa
%doc COPYING
%dir %_datadir/publicsuffix/
%_datadir/publicsuffix/public_suffix_list.dafsa
%endif

%changelog
* Thu Jan 09 2020 Mikhail Efremov <sem@altlinux.org> 20200106-alt1
- Use Vcs tag.
- New snapshot.

* Fri Nov 08 2019 Mikhail Efremov <sem@altlinux.org> 20191108-alt1
- New snapshot.

* Mon Aug 26 2019 Mikhail Efremov <sem@altlinux.org> 20190823-alt1
- Use C.UTF-8 for dafsa generation.
- New snapshot.

* Mon Apr 01 2019 Mikhail Efremov <sem@altlinux.org> 20190329-alt1
- New snapshot.

* Wed Nov 07 2018 Mikhail Efremov <sem@altlinux.org> 20181106-alt1
- New snapshot.

* Fri Apr 27 2018 Mikhail Efremov <sem@altlinux.org> 20180420-alt1
- New snapshot.

* Wed Mar 14 2018 Mikhail Efremov <sem@altlinux.org> 20180312-alt1
- New snapshot.

* Thu Nov 23 2017 Mikhail Efremov <sem@altlinux.org> 20171028-alt1
- New snapshot.

* Wed Oct 18 2017 Mikhail Efremov <sem@altlinux.org> 20170910-alt1
- New snapshot.

* Mon Jul 31 2017 Mikhail Efremov <sem@altlinux.org> 20170713-alt1
- New snapshot.

* Tue Jul 04 2017 Mikhail Efremov <sem@altlinux.org> 20170704-alt1
- New snapshot.

* Sun Apr 09 2017 Mikhail Efremov <sem@altlinux.org> 20170404-alt2
- Add changlog from old fcimport spec.

* Fri Apr 07 2017 Mikhail Efremov <sem@altlinux.org> 20170404-alt1
- Initial build.

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 20160713-alt1_1
- update to new release by fcimport

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 20151208-alt1_1
- to Sisyphus
