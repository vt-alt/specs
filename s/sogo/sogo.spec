%def_without openchange
%define sogo_user _sogo

Summary:      SOGo is a very fast and scalable modern collaboration suite (groupware)
Name:         sogo
Version:      4.3.2
Release:      alt1

License:      GPL-2.0+ and LGPL-2.1+
URL:          https://sogo.nu/
# VCS:        https://github.com/inverse-inc/sogo
# Do not forget to update angular submodule and 
# update CSS as describe in https://sogo.nu/files/docs/SOGoDevelopersGuide.pdf
#  git submodule init
#  git submodule update
#  cd UI/WebServerResources
#  npm install
#  ./node_modules/grunt/bin/grunt build

Group:        Communications
Packager:     Andrey Cherepanov <cas@altlinux.org>

Source:       SOGo-%version.tar
Source1:      sogo.init
Source2:      angular-material.tar
Patch1: sogo-alt-fix-enter-letters-in-address-field.patch
Patch2: sogo-alt-fixes.patch
Patch3: sogo-angular-css-update.patch
Patch4: sogo-alt-fix-timeZoneWithAbbreviation.patch

Requires:      stmpclean
Requires:      tzdata
Requires:      zip
Conflicts:     sogo2
Provides:      sogo3 = %EVR
Obsoletes:     sogo3 < %EVR

%filter_from_requires /^\/usr\/%_lib\/samba-dc\/lib/d
%{!?sogo_major_version: %global sogo_major_version %(/bin/echo %version | /bin/cut -f 1 -d .)}

BuildRequires: gnustep-make-devel
BuildRequires: gnustep-base-devel
BuildRequires(pre): rpm-build-apache2
# To ignore a patched submodule:
BuildPreReq: patchutils
BuildRequires: gcc-objc
BuildRequires: sope-appserver-devel sope-core-devel sope-ldap-devel sope-mime-devel sope-xml-devel sope-gdl1-devel sope-sbjson-devel
BuildRequires: libcurl-devel
BuildRequires: libffi-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgmp-devel
BuildRequires: libgnutls-devel
BuildRequires: libicu-devel
BuildRequires: liblasso-devel
BuildRequires: libmemcached-devel
BuildRequires: libnanomsg-devel
BuildRequires: libobjc-devel
BuildRequires: libssl-devel
BuildRequires: libwbxml-devel
%if_with openchange
BuildRequires: openchange-devel
%endif
BuildRequires: zlib-devel
BuildRequires: python3-module-samba

%description
SOGo is a groupware server built around OpenGroupware.org (OGo) and
the SOPE application server.  It focuses on scalability.

The Inverse edition of this project has many feature enhancements:
- CalDAV and GroupDAV compliance
- full handling of vCard as well as vCalendar/iCalendar formats
- support for folder sharing and ACLs

The Web interface has been rewritten in an AJAX fashion to provided a
faster UI for the users, consistency in look and feel with the Mozilla
applications, and to reduce the load of the transactions on the server.

%package apache2
Summary: SOGo configuration for Apache2
Group: System/Servers
Requires:  %name = %EVR
Provides:  sogo3-apache2 = %EVR
Obsoletes: sogo3-apache2 < %EVR

%description apache2
SOGo configuration for Apache2

%package -n task-sogo
Summary: SOGo is a groupware server (version 3.x)
Group: System/Servers
Requires: %name
Requires: %name-activesync
Requires: %name-tool
Requires: sope-cards
Requires: %name-apache2
Requires: apache2-base
Requires: apache2-mod_ngobjweb
Requires: apache2-mod_wsgi
Requires: memcached 
Requires: sope-gdl1-postgresql
Requires: postgresql-server
Requires: postfix
Requires: postfix-dovecot
Requires: postfix-ldap
Requires: postfix-tls
Requires: dovecot
Requires: dovecot-pigeonhole
Requires: cadaver
Requires: libpst-tools
Requires: vixie-cron
Requires: openldap-clients

Provides:  task-sogo3 = %EVR
Obsoletes: task-sogo3 < %EVR

%description -n task-sogo
SOGo is a groupware server built around OpenGroupware.org (OGo) and
the SOPE application server.  It focuses on scalability.

The Inverse edition of this project has many feature enhancements:
- CalDAV and GroupDAV compliance
- full handling of vCard as well as vCalendar/iCalendar formats
- support for folder sharing and ACLs

The Web interface has been rewritten in an AJAX fashion to provided a
faster UI for the users, consistency in look and feel with the Mozilla
applications, and to reduce the load of the transactions on the server.

It supports MAPI access for Microsoft Outlook.

See http://altlinux.org/SOGo for more information about deployment and
configuration.

%package tool
Summary:      Command-line toolsuite for SOGo
Group:        Communications
Requires:     %name = %EVR
Provides:     sogo3-tool = %EVR
Obsoletes:    sogo3-tool < %EVR

%description tool
Administrative tool for SOGo that provides the following internal
commands:
- backup          - backup user folders
- restore         - restore user folders
- remove-doubles  - remove duplicate contacts from the user addressbooks
- check-doubles   - list user addressbooks with duplicate contacts

%package slapd-sockd
Summary:      SOGo backend for slapd and back-sock
Group:        Communications
Provides:     sogo3-slapd-sockd = %EVR
Obsoletes:    sogo3-slapd-sockd < %EVR

%description slapd-sockd
SOGo backend for slapd and back-sock, enabling access to private
addressbooks via LDAP.

%package ealarms-notify
Summary:      SOGo utility for executing email alarms
Group:        Communications
Provides:     sogo3-ealarms-notify = %EVR
Obsoletes:    sogo3-ealarms-notify < %EVR

%description ealarms-notify
SOGo utility executed each minute via a cronjob for executing email
alarms.

%package activesync
Summary:      SOGo module to handle ActiveSync requests
Group:        Communications
Requires:     %name = %EVR
Provides:     sogo3-activesync = %EVR
Obsoletes:    sogo3-activesync < %EVR

%description activesync
SOGo module to handle ActiveSync requests

%package devel
Summary:      Development headers and libraries for SOGo
Group:        Development/Objective-C
Provides:     sogo3-devel = %EVR
Obsoletes:    sogo3-devel < %EVR

%description devel
Development headers and libraries for SOGo. Needed to create modules.

%package -n sope-gdl1-contentstore
Summary:      Storage backend for folder abstraction.
Group:        Development/Objective-C
Requires:     sope-gdl1
Conflicts:    sope-gdl1-contentstore-sogo2
Provides:     sope-gdl1-contentstore-sogo3 = %EVR
Obsoletes:    sope-gdl1-contentstore-sogo3 < %EVR

%description -n sope-gdl1-contentstore
The storage backend implements the "low level" folder abstraction, which
is basically an arbitary "BLOB" containing some document.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package -n sope-gdl1-contentstore-devel
Summary:      Development files for the GNUstep database libraries
Group:        Development/Objective-C
Requires:     sope-gdl1
Conflicts:    sope-gdl1-contentstore-devel
Provides:     sope-gdl1-contentstore-sogo3-devel = %EVR
Obsoletes:    sope-gdl1-contentstore-sogo3-devel < %EVR

%description -n sope-gdl1-contentstore-devel
This package contains the header files for SOPE's GDLContentStore
library.

SOPE is a framework for developing web applications and services. The
name "SOPE" (SKYRiX Object Publishing Environment) is inspired by ZOPE.

%package -n sope-cards
Summary:      SOPE versit parsing library for iCal and VCard formats
Group:        Development/Objective-C
Conflicts:    sope-cards-sogo2
Provides:     sope-cards-sogo3 = %EVR
Obsoletes:    sope-cards-sogo3 < %EVR

%description -n sope-cards
SOPE versit parsing library for iCal and VCard formats

%package -n sope-cards-devel
Summary:      SOPE versit parsing library for iCal and VCard formats
Group:        Development/Objective-C
Requires:     sope-cards
Provides:     sope-cards-sogo3-devel = %EVR
Obsoletes:    sope-cards-sogo3-devel < %EVR

%description -n sope-cards-devel
SOPE versit parsing library for iCal and VCard formats

%if_with openchange
%package openchange-backend
Summary:      SOGo backend for OpenChange
Group:        Communications
Requires:     samba-DC-libs
Provides:     sogo3-openchange-backend = %EVR
Obsoletes:    sogo3-openchange-backend < %EVR

%description openchange-backend
SOGo backend for OpenChange
%endif

%prep
%setup -q -n SOGo-%version
tar xf %SOURCE2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Set correct python2 executable in shebang                                                                                                                                                    
subst 's|#!.*python$|#!%__python|' $(grep -Rl '#!.*python$' *)

%build
. /usr/share/GNUstep/Makefiles/GNUstep.sh
./configure \
            --enable-saml2
#           --enable-ldap-config

%make_build CC="cc" LDFLAGS="$ldflags" messages=yes

# OpenChange
%if_with openchange
pushd OpenChange
subst 's@-Wall@-Wall -fobjc-exceptions@' GNUmakefile
export LD_LIBRARY_PATH=../SOPE/NGCards/obj:../SOPE/GDLContentStore/obj
make GNUSTEP_INSTALLATION_DOMAIN=SYSTEM CC="cc" LDFLAGS="$ldflags" messages=yes
popd
%endif

%install
export QA_SKIP_BUILD_ROOT=1

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM 

install -d %buildroot/etc/sysconfig
install -d %buildroot/var/lib/sogo
install -d %buildroot/var/log/sogo
install -d %buildroot/var/run/sogo
install -d %buildroot/var/spool/sogo

install -d -m 750 %buildroot/etc/sogo
install -D -m 640 Scripts/sogo.conf %buildroot/etc/sogo/sogo.conf

# Apache2 configuration
install -Dm0644 -p Apache/SOGo.conf %buildroot%apache2_sites_available/SOGo.conf
subst "s@/lib/@/%_lib/@g" %buildroot%apache2_sites_available/SOGo.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/SOGo.conf

install -Dm 600 Scripts/sogo.cron %buildroot/etc/cron.d/sogo
subst 's, sogo, %sogo_user,g' %buildroot/etc/cron.d/sogo
install -Dm 755 Scripts/tmpwatch %buildroot/etc/cron.daily/sogo-tmpwatch
subst 's/user sogo/user %sogo_user/' %buildroot/etc/cron.daily/sogo-tmpwatch
install -Dm 644 Scripts/logrotate %buildroot%_logrotatedir/sogo
sed -i '1 a\su %sogo_user %sogo_user' %buildroot%_logrotatedir/sogo
install -Dm 644 Scripts/sogo-systemd-redhat %buildroot%_unitdir/sogo.service
subst "s/^User=.*/User=%sogo_user/" %buildroot%_unitdir/sogo.service
install -Dm 644 Scripts/sogo-systemd.conf %buildroot%_tmpfilesdir/sogo.conf
subst "s/ sogo/ %sogo_user/g" %buildroot%_tmpfilesdir/sogo.conf
install -Dm 755 %SOURCE1 %buildroot%_initdir/sogo

cp Scripts/sogo-default %buildroot/etc/sysconfig/sogo
echo "USER=%sogo_user" >> %buildroot/etc/sysconfig/sogo

rm -rf %buildroot%_bindir/test_quick_extract

export LD_LIBRARY_PATH=%buildroot%_libdir

# OpenChange
%if_with openchange
pushd OpenChange
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM
popd
%endif

# ActiveSync
pushd ActiveSync
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM 
install -Dm0644 LICENSE %buildroot%_defaultdocdir/sogo-activesync-%version/LICENSE
install -Dm0644 README  %buildroot%_defaultdocdir/sogo-activesync-%version/README
popd

%files
%doc CHANGELOG.md README.md Scripts/*sh Scripts/updates.php Apache/SOGo-apple-ab.conf
%config(noreplace) %attr(0640, root, %sogo_user) %_sysconfdir/sogo/sogo.conf
%config(noreplace) %_logrotatedir/sogo
%config(noreplace) %_sysconfdir/cron.d/sogo
%config(noreplace) %_sysconfdir/sysconfig/sogo
%_unitdir/sogo.service
%_tmpfilesdir/sogo.conf
%_initdir/sogo
%_sysconfdir/cron.daily/sogo-tmpwatch
%dir %attr(0700, %sogo_user, %sogo_user) %_var/lib/sogo
%dir %attr(0700, %sogo_user, %sogo_user) %_logdir/sogo
%dir %attr(0755, %sogo_user, %sogo_user) %_runtimedir/sogo
%dir %attr(0700, %sogo_user, %sogo_user) %_spooldir/sogo
%dir %attr(0750, root, %sogo_user) %_sysconfdir/sogo
%_sbindir/sogod
%dir %_libdir/sogo
%_libdir/sogo/libSOGo.so.*
%_libdir/sogo/libSOGoUI.so.*
%_libdir/GNUstep/SOGo/AdministrationUI.SOGo
%_libdir/GNUstep/SOGo/Appointments.SOGo
%_libdir/GNUstep/SOGo/CommonUI.SOGo
%_libdir/GNUstep/SOGo/Contacts.SOGo
%_libdir/GNUstep/SOGo/ContactsUI.SOGo
%_libdir/GNUstep/SOGo/MailPartViewers.SOGo
%_libdir/GNUstep/SOGo/Mailer.SOGo
%_libdir/GNUstep/SOGo/MailerUI.SOGo
%_libdir/GNUstep/SOGo/MainUI.SOGo
%_libdir/GNUstep/SOGo/PreferencesUI.SOGo
%_libdir/GNUstep/SOGo/SchedulerUI.SOGo
%_libdir/GNUstep/Frameworks/SOGo.framework/Resources
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/libSOGo.so.*
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/Resources
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/Current
%_libdir/GNUstep/SOGo/Templates
%_libdir/GNUstep/SOGo/WebServerResources
%_libdir/GNUstep/OCSTypeModels
%_libdir/GNUstep/WOxElemBuilders-*

%files apache2
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf

%files tool
%{_sbindir}/sogo-tool

%files ealarms-notify
%{_sbindir}/sogo-ealarms-notify

%files slapd-sockd
%{_sbindir}/sogo-slapd-sockd

%files activesync
%doc %_defaultdocdir/sogo-activesync-%version
%_libdir/GNUstep/SOGo/ActiveSync.SOGo

%files devel
%_includedir/SOGo
%_includedir/SOGoUI
%_libdir/sogo/libSOGo.so
%_libdir/sogo/libSOGoUI.so
%_libdir/GNUstep/Frameworks/SOGo.framework/Headers
%_libdir/GNUstep/Frameworks/SOGo.framework/sogo/libSOGo.so
%_libdir/GNUstep/Frameworks/SOGo.framework/sogo/SOGo
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/Headers
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/libSOGo.so
%_libdir/GNUstep/Frameworks/SOGo.framework/Versions/%{sogo_major_version}/sogo/SOGo

%files -n sope-gdl1-contentstore
%_libdir/sogo/libGDLContentStore*.so.*

%files -n sope-gdl1-contentstore-devel
%_includedir/GDLContentStore
%_libdir/sogo/libGDLContentStore*.so

%files -n sope-cards
%_libdir/sogo/libNGCards.so.*
%_libdir/GNUstep/SaxDrivers-*
%_libdir/GNUstep/SaxMappings
%_libdir/GNUstep/Libraries/Resources/NGCards

%files -n sope-cards-devel
%_includedir/NGCards
%_libdir/sogo/libNGCards.so

%if_with openchange
%files openchange-backend
%_libdir/GNUstep/SOGo/*.MAPIStore
%_libdir/mapistore_backends/*
%endif

%files -n task-sogo

%pre
if ! id %sogo_user >& /dev/null; then
  /usr/sbin/useradd -d %{_var}/lib/sogo -c "SOGo daemon" -s /sbin/nologin -M -r %sogo_user
fi

%post
%post_service sogo

%preun
%preun_service sogo

%changelog
* Thu May 07 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version.
- Build afrom upstream tag and separate patch files.
- Move /var/run/sogo to /run/sogo.

* Sat May 02 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version.

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt2
- Returned to Sisyphus.

* Mon Jan 27 2020 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Wed Dec 18 2019 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version.
- Fix license tag.

* Fri Nov 01 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.1-alt1
- New version.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- New version.

* Mon Jul 22 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.8-alt1
- New version.

* Tue Jun 25 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt4
- Do not restrict architecture.

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt3
- Fix provides.

* Sat Mar 30 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt2
- Do not require openchange-devel if build without openchange (ALT #36464).

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt1
- New version.

* Thu Feb 21 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.6-alt1
- New version.

* Wed Jan 09 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.5-alt1
- New version.

* Mon Oct 29 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.4-alt1
- New version.

* Thu Oct 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.3-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.2-alt1
- New version.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.1-alt1
- New version.
- Package angular/material from submodule.
- Drop OpenChange support by upstream.

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.10.20171010-alt3
- Rename to sogo.
- Require PostgreSQL server with any version.
- Fix grant rules for Apache2 new version.

* Thu Jan 25 2018 Ivan Zakharyaschev <imz@altlinux.org> 3.2.10.20171010-alt2
- Fixed entering some letters (for example, Cyrillic Be or Zhe) in the
  address fields (like To:) of the message editor so that they do not act as
  "separator" keys (like comma or semicolon) any more; this error's cause
  was that these letters and the separators are on the same physical keys.
  (Thanks Volker Braun for implementing the underlying feature
  for this fix in the old angular-material.) (ALT#34336)

* Wed Oct 11 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.2.10.20171010-alt1
- Build the current "nightly" revision to correctly handle top-level
  non-ASCII folder names in ActiveSync (ALT: #33721) as suggested
  in https://lists.inverse.ca/sogo/arc/users/2017-09/msg00011.html
  and https://sogo.nu/bugs/view.php?id=4240 not to wait for the 3.3 release.

* Fri Jul 21 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.10-alt2
- Fix project URL (ALT #33669)

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.10-alt1
- New version

* Wed Jun 21 2017 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.9-alt2.S1
- Add universal build tag (aka ubt macros)

* Fri Jun 09 2017 Evgeny Sinelnikov <sin@altlinux.ru> 3.2.9-alt2
- Rebuild with splited samba-DC-libs

* Tue May 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1
- New version

* Tue Mar 28 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.8-alt1
- New version

* Wed Feb 15 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.7-alt1
- new version 3.2.7

* Wed Jan 11 2017 Andrey Cherepanov <cas@altlinux.org> 3.2.5-alt1
- new version 3.2.5

* Tue Dec 06 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- new version 3.2.4

* Thu Nov 24 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- new version 3.2.2

* Wed Nov 09 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt3
- Disable native spell checker (because it is only available for a
  limited set of languages)
- Provides task-sogo

* Thu Nov 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt2
- Add tzdata to requirements

* Thu Nov 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version 3.2.1 (https://sogo.nu/news/2016/article/sogo-v321-released.html)

* Tue Oct 04 2016 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version 3.2.0 (https://sogo.nu/news/2016/article/sogo-v320-released.html)
- New features:
  * [web] added IMAP folder subscriptions management
  * [web] keyboard shortcuts
  * [eas] initial support for server-side mailbox search operations

* Thu Sep 29 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt1.git.M80P.1
- Backport new version to p8 branch

* Thu Sep 29 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.5-alt2.git
- Fix timezone shift for calendar entries

* Mon Aug 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.5-alt1.git
- Latest fixes:
  + [eas] properly generate the BusyStatus for normal events
  + [web] restored functionality to save unknown recipient emails to
    address book on send
  + [core] strip protocol value from proxyAddresses attribute (#3182)
- 3.1.5

* Tue Jul 19 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.4-alt2
- Fix the unrecognized selector exception in the fresh pieces of the EAS
  implementation (by writing the queries analoguously to the other ones).

* Thu Jul 14 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.4-alt1
- New version 3.1.4
- Build sogo3-apache2 as arch-dependent

* Tue Jul 12 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt3
- Add dovecot-pigeonhole to task-sogo3

* Tue Jul 12 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt2
- Add more requirements to task-sogo3

* Thu Jun 23 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt1
- New version
- Add sope-gdl1-postgresql to task-sogo3

* Wed Jun 15 2016 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt3
- Fix user name in tmpwatch and logrotate rules
- Add dlinklist.h from Samba
- Rebuild with Apache 2.4

* Thu Mar 10 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt2
- Rebuild with new rpm

* Tue Mar 08 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version

* Fri Mar 04 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt3
- New package sogo3 (ALT #31854)

* Fri Feb 26 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt2
- Rebuild with new icu

* Tue Feb 16 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version

* Tue Feb 02 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Fix permission of /etc/logrotate.d/sogo (ALT #31750)

* Thu Jan 28 2016 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Tue Jan 26 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.7-alt1
- New version
- Move apache bindings to package sogo-apache2

* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.6-alt1
- New version
- Move memcached requirement to task-sogo

* Tue Jan 12 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- New version

* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.4-alt2
- Add metapackage task-sogo for completely install SOGo
- Spec cleanup

* Thu Dec 17 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.4-alt1
- New version

* Mon Nov 23 2015 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt1
- Initial build in Sisyphus (spec is based on upstream spec file)

