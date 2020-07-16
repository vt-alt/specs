Group: File tools
%filter_from_requires /.usr.xpg4.bin.sh/d
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%global bashcompdir %(pkg-config --variable=completionsdir bash-completion)

Name:           lynis
Version:        3.0.0
Release:        alt2
Summary:        Security and system auditing tool
License:        GPLv3
URL:            https://cisofy.com/lynis/
Source0:        https://cisofy.com/files/%name-%version.tar.gz
BuildArch:      noarch
BuildRequires:  bash-completion-util-linux
BuildRequires:  git-core
BuildRequires:  procps
Requires:       audit
Requires:       e2fsprogs
Requires:       module-init-tools

%description
Lynis is an auditing and hardening tool for Unix/Linux and you might even call
it a compliance tool. It scans the system and installed software. Then it 
performs many individual security control checks. It determines the hardening 
state of the machine, detects security issues and provides suggestions to 
improve the security defense of the system.

%prep
%setup -q -n %name


%build
# Empty build.

%install
mkdir -p %buildroot%_sysconfdir/%name
install -p default.prf %buildroot%_sysconfdir/%name

mkdir -p %buildroot%_bindir
install -p lynis %buildroot%_bindir

mkdir -p %buildroot%_mandir/man8
install -p lynis.8 %buildroot%_mandir/man8

mkdir -p  %buildroot%_datadir/%name/include/
# Forced by upstream. Otherwise these scripts can't be executed.
install -p include/* %buildroot%_datadir/%name/include/
chmod 644 %buildroot%_datadir/%name/include/*

mkdir -p  %buildroot%_datadir/%name/plugins/
install -p plugins/* %buildroot%_datadir/%name/plugins/

cp -pR db/ %buildroot%_datadir/%name/

mkdir -p %buildroot%bashcompdir
install -p extras/bash_completion.d/lynis %buildroot%bashcompdir/

mkdir -p %buildroot%_localstatedir/log/
touch %buildroot%_localstatedir/log/lynis.log
touch %buildroot%_localstatedir/log/lynis-report.dat
for rpm404_ghost in %_localstatedir/log/lynis.log %_localstatedir/log/lynis-report.dat
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done


%check
# Sanity check
./lynis audit system --quick 

%files
%doc CHANGELOG* CONTRIBUTORS* FAQ* README*
%doc extras/systemd/
%doc --no-dereference LICENSE
%_bindir/lynis
%bashcompdir/*
%_datadir/lynis/
%_mandir/man8/lynis.8*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/default.prf
%ghost %_localstatedir/log/lynis.log
%ghost %_localstatedir/log/lynis-report.dat

%changelog
* Tue Jul 14 2020 Pavel Vasenkov <pav@altlinux.org> 3.0.0-alt2
- initial build for sisyphus

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_1
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_5
- update to new release by fcimport

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_4
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_2
- update to new release by fcimport

* Mon Jul 01 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.5-alt1_1
- update to new release by fcimport

* Tue Mar 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.9-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.6-alt1_1
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.4-alt1_1
- update to new release by fcimport

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_1
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1_1
- update to new release by fcimport

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.9-alt1_1
- update to new release by fcimport

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.8-alt1_1
- update to new release by fcimport

* Tue Dec 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.7-alt1_1
- update to new release by fcimport

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.6-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_6
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.9-alt1_5
- initial fc import

