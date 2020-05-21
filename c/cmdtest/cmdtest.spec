
Name: cmdtest
Version: 0.30
Release: alt1.1.p9

Summary: Black-box testing for Unix command line tools

License: GPLv3+
Group: Development/Python
Url: http://liw.fi/%name/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://code.liw.fi/debian/pool/main/c/%name/%{name}_%version.orig.tar
Source44: import.info

BuildArch: noarch

# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
# END SourceDeps(oneline)

#BuildRequires: python-module-coverage-test-runner
BuildRequires: python-module-cliapp
BuildRequires: python-module-markdown
BuildRequires: python-module-ttystatus

Conflicts: yarn
Conflicts: hadoop-yarn

%description
cmdtest black box tests Unix command line tools. Roughly, it is given
a command line and input files, and the expected output, and it
verifies that the command line produces the expected output. If not,
it reports a problem, and shows the differences.

%prep
%setup

%build
%python_build

%install
%python_install

%check
exit 0
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
%__python setup.py check

%files
%doc COPYING NEWS README README.yarn
%_bindir/cmdtest
%_bindir/yarn
%_man1dir/cmdtest.1*
%_man1dir/yarn.1*
%python_sitelibdir_noarch/*

%changelog
* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.1.p9
- Add conflict to yarn.

* Sat Oct 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.30-alt1
- new version 0.30 (with rpmrb script)

* Sat Dec 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.27-alt1
- new version 0.27 (with rpmrb script)

* Sat Jan 02 2016 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt1
- new version 0.16 (with rpmrb script)

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt2
- human build for ALT Linux Sisyphus

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_2
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.3-alt1_1
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_1
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_4
- update to new release by fcimport

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 0.3-alt2_3
- rebuild to get rid of unmets

* Sat Jan 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_3
- initial fc import

