BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: desktop-file-utils
# Automatically added by buildreq on Tue Jun 27 2017
# optimized out: libqt5-core python-base python-modules python3 python3-base python3-module-setuptools
BuildRequires: python3-dev python3-module-PyQt5 python3-module-sip
BuildRequires: python3-module-keyring python3-module-dbus
BuildRequires: python3-module-psutil
BuildRequires: /proc

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
Name:           nagstamon
Version:        3.4.1
Release:        alt3
Summary:        Nagios status monitor for the desktop
License:        GPLv2
Group:          Monitoring
Url:            http://nagstamon.ifw-dresden.de/
Source:         %name-%version.tar
%py3_requires   secretstorage sip keyring requests_gssapi gssapi
BuildArch:      noarch
Patch1:         %name-%version-init-translator.patch
Patch2:         nagstamon-3.0.1-alt-default-values-in-config.patch
Patch3:         %name-%version-system-config.patch
Patch4:         %name-%version-abstract-socket.patch
Source44:       import.info
Source1:        all.ts
Source2:        all.qm

%description
Nagstamon is a Nagios status monitor which takes place in systray or on desktop
(GNOME, KDE, Windows) as floating statusbar to inform you in realtime about the
status of your Nagios and derivatives monitored network. It allows to connect
to multiple Nagios, Icinga, Opsview, Op5, Check_MK/Multisite and Centreon
servers.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

cp %SOURCE1 %SOURCE2 Nagstamon/QUI/

%build
python3 setup.py build

%install
python3 setup.py install \
    --root=%buildroot \
    --install-lib=%python3_sitelibdir_noarch

mv %buildroot/%_bindir/nagstamon.py %buildroot/%_bindir/nagstamon
#i18n ru_RU
install -D -m 644 Nagstamon/QUI/all.qm %buildroot/%python3_sitelibdir_noarch/Nagstamon/translate/ru_RU.qm


# desktop stuff
mkdir -p %buildroot%_datadir/applications,pixmaps
install -m 644 Nagstamon/resources/nagstamon.svg \
    %buildroot%_datadir/pixmaps/nagstamon.svg
install -m 644 Nagstamon/resources/nagstamon.desktop \
    %buildroot/%_datadir/applications/nagstamon.desktop

desktop-file-install \
  --dir=%buildroot%_datadir/applications \
  %buildroot/%_datadir/applications/nagstamon.desktop

%files
%doc ChangeLog COPYRIGHT LICENSE
%_datadir/pixmaps/nagstamon.svg
%_datadir/applications/nagstamon.desktop
%python3_sitelibdir_noarch/Nagstamon
%python3_sitelibdir_noarch/Nagstamon/translate/*.qm
%_bindir/nagstamon
%_mandir/man1/nagstamon.1*
%python3_sitelibdir_noarch/*.egg-info


%changelog
* Thu Jun 04 2020 Paul Wolneykien <manowar@altlinux.org> 3.4.1-alt3
- Fix: Require python3-module-requests-gssapi (closes: 38577).

* Wed Feb 12 2020 Paul Wolneykien <manowar@altlinux.org> 3.4.1-alt2
- Fix: Require python module 'gssapi'.
- Fix: Require python module 'keyring'.
- Added fixed version of the ALT translation initialization patch.
- Added abstract-socket patch (thx Denis Medvedev).
- Read partial configs from /etc/nagstamon/<subject> directory.

* Wed Feb 05 2020 Grigory Ustinov <grenka@altlinux.org> 3.4.1-alt1
- new version 3.4.1
- Cleanup spec file

* Thu Dec 20 2018 Grigory Ustinov <grenka@altlinux.org> 3.2-alt1
- new version 3.2

* Tue May 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt3
- Fix default values (Closes: #33585).

* Thu Apr 05 2018 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.1-alt2
- fix rebuild (add BuildReq to python3-module-dbus)

* Sat Oct 21 2017 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.1-alt1
- new version 3.0.1

* Mon Jul 24 2017 Mikhail Gordeev <obirvalger@altlinux.org> 2.1-alt0.20170723.1
- new version 2.1

* Wed Mar 01 2017 Denis Medvedev <nbr@altlinux.org> 2.0.1-alt5
- More strings translated

* Thu Feb 02 2017 Denis Medvedev <nbr@altlinux.org> 2.0.1-alt4
- rudimentary translation to Russian

* Tue Jan 31 2017 Denis Medvedev <nbr@altlinux.org> 2.0.1-alt3
- Fixed version of requests

* Tue Jan 31 2017 Denis Medvedev <nbr@altlinux.org> 2.0.1-alt2
- fixed dependencies

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- converted for ALT Linux by srpmconvert tools

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_3
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_2
- update to new release by fcimport

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_3
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_2
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_9
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_8
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_7
- initial fc import

