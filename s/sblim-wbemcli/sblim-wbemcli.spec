Name: sblim-wbemcli
Version: 1.6.3
Release: alt2

Summary: SBLIM WBEM Command Line Interface

License: EPL-1.0
Group: System/Base
Url: https://sourceforge.net/projects/sblim/

# Source-url: http://downloads.sourceforge.net/sblim/%name-%version.tar.bz2
Source: %name-%version.tar

Patch: sblim-wbemcli-1.5.1-gcc43.patch
Patch1: sblim-wbemcli-1.6.2-https-segfaults.patch
Patch2: sblim-wbemcli-1.6.1-ssl-proto-option.patch
Patch3: sblim-wbemcli-1.6.3-fix-exit-status.patch
Patch4: sblim-wbemcli-1.6.3-covscan-fixes.patch

BuildRequires: %_bindir/swig libghttp-devel swig
BuildRequires: curl-devel >= 7.9.3
BuildRequires: binutils-devel >= 2.17.50.0.3
BuildRequires: autoconf automake libtool
BuildRequires: gcc-c++
Requires: curl >= 7.9.3
Source44: import.info

%description
WBEM Command Line Interface is a standalone, command line WBEM client. It is
specially suited for basic systems management tasks as it can be used in
scripts.

%prep
%setup
%autoreconf
%patch0 -p1 -b .gcc43
%patch1 -p1 -b .https-segfaults
%patch2 -p1 -b .ssl-proto-option
%patch3 -p1 -b .fix-exit-status
%patch4 -p1 -b .covscan-fixes

%build
%configure CACERT=/etc/pki/Pegasus/client.pem
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/%name/

%files
%doc --no-dereference COPYING
%_bindir/wbem*
%_man1dir/*
%_datadir/%name/

%changelog
* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt2
- manually build for ALT Sisyphus

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_18
- update to new release by fcimport

* Wed Apr 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_17
- update

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_16
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_15
- update to new release by fcimport

* Thu May 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_14
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_13
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_12
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_10
- update to new release by fcimport

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_9
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_7
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_6
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_5
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_4
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_13
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_12
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_11
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_10
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_8
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_7
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_6
- initial fc import

