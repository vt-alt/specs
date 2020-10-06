%define module fedora-compat
Name: rpm-macros-%module
Summary: Fedora compatibility set of macro
Version: 0.159
Release: alt1
License: LGPLv2+
Group: System/Base
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: %name-%version.tar
Requires: rpm-macros-generic-compat
Requires: rpm-macros-kde-common-devel
#set separately in Fedora2ALT
#Requires: rpm-build-kf5

%description
%summary

%prep
%setup

%install
install -D -m644 %module -p %buildroot%_rpmmacrosdir/%module-base
for ext in cmake cmake-compat kde4 kf5 qt4 perl systemd; do
    install -D -m644 alt/macros.$ext -p %buildroot%_rpmmacrosdir/%module-$ext
done

%files
%_rpmmacrosdir/*

%changelog
* Sat Sep 19 2020 Igor Vlasenko <viy@altlinux.ru> 0.159-alt1
- introduced fedora_v2_cmake + added compat fedora_cmake

* Sat Sep 19 2020 Igor Vlasenko <viy@altlinux.ru> 0.158-alt1
- systemd updated
- kf5 updated
- perl updated

* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.157-alt1
- cmake updated

* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.156-alt1
- added build_ldflags

* Fri Jan 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.155-alt1
- added %%_metainfodir %%_datadir/metainfo

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.154-alt1
- updated %%GNAT_arches

* Thu Oct 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.153-alt1
- defined %%_userunitdir as /usr/lib/systemd/user
  (/lib/systemd/user does not work, see alt#35520)
  (closes: #35551)

* Tue Jun 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.152-alt1
- added %%py2/3_build/install

* Sun Jun 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.151-alt1
- added _rundir

* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- new version

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- Requires: rpm-macros-generic-compat

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- initial kf5 support

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added %%__isa_bits and %%qt5_qtwebengine_arches

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added perl_testdir

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- updated systemd

* Fri Oct 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added _jsdir

* Mon Dec 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt5
- added GNAT_arches

* Thu Dec 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt4
- added _cups_serverbin

* Wed Oct 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt3
- fc sugar macros fix

* Tue Oct 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- added sugar libdir

* Wed Oct 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added sugar activity dir

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- fixes in systemd macros

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added __python3

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added fc systemd compat macros

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added fc compatible kde4 macros

* Fri Jun 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4
- dropped unitdir (in main rpm now)

* Fri Jun 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3
- added _datarootdir

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- added __id_u

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added perl compat macros

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- more fc macros

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added qt4 compat macros

* Thu Jul 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build for ALT Linux Sisyphus
