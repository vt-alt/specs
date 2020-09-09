%define installdir %webserver_webappsdir/%name
%define otrs_user otrs

Name: otrs
Version: 6.0.29
Release: alt1

Summary: Open source Ticket Request System
Group: Networking/WWW
License: GPL-3.0-only
Url: http://www.otrs.org/

Source0: https://ftp.otrs.org/pub/otrs/%name-%version.tar.bz2
Source1: README.ALT.rus
Source2: otrs-hold.conf
Source3: apache2.conf

BuildArch: noarch

BuildRequires(pre): rpm-macros-webserver-common rpm-macros-apache2 >= 3.9

Requires: webserver-common perl-CGI perl-DBI perl-DBD-mysql

# requires for start httpd2
Requires: perl-DateTime perl-Template

# is needed (found in /var/log/httpd2/error_log)
Requires: perl-Unicode-Collate perl-Moo

# hard requires by otrs.CheckModules.pl
Requires: perl-Archive-Tar perl-Archive-Zip perl-TimeDate perl-Net-DNS perl-YAML-LibYAML

# some of soft requires by otrs.CheckModules.pl
Requires: perl-Crypt-Eksblowfish perl-Crypt-SSLeay perl-JSON-XS perl-Mail-IMAPClient perl-IO-Socket-SSL perl-Text-CSV_XS perl-XML-LibXSLT perl-XML-Parser

# is needed for DBUpdate-to-6.pl
Requires: perl-CPAN-Meta

%add_findreq_skiplist */bin/*
%add_findreq_skiplist */Kernel/*
%add_findreq_skiplist */scripts/*
%add_findreq_skiplist */examples/*

%description
OTRS is an Open source Ticket Request System (also well known
as trouble ticket system) with many features to manage customer
telephone calls and e-mails. The system is built to allow your
support, sales, pre-sales, billing, internal IT, helpdesk, e.t.c.
departments to react quickly to inbound inquiries.

%package apache2
Summary: Apache 2.x web-server configuration for %name
Group: Networking/WWW
Requires: %name = %version-%release, apache2, apache2-mod_perl perl-Apache-DBI
%description apache2
Apache 2.x web-server configuration for %name

%prep
%setup

%install
# install apache config
install -pD -m0644 %SOURCE3 %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf

# install apt's hold file
install -pD -m0644 %SOURCE2 %buildroot%_sysconfdir/apt/apt.conf.d/%name-hold.conf

# install otrs
mkdir -p %buildroot%installdir
cp -rp * %buildroot%installdir/

#install docs
install -pD -m0644 %SOURCE1 README.ALT.rus

#replace '/opt/otrs' to '/var/www/webapps/otrs' in all files
find %buildroot%installdir -type f -exec sed -i -e "s/\/opt\/otrs/\/var\/www\/webapps\/otrs/g" {} \;

# remove files
find %buildroot%installdir -name *.spec -delete
find %buildroot%installdir -name *.conf -delete

#install default config
cp %buildroot%installdir/Kernel/Config.pm.dist %buildroot%installdir/Kernel/Config.pm
# cd %buildroot%installdir/Kernel/Config/
# for foo in *.dist; do cp $foo `basename $foo .dist`; done
cd %buildroot%installdir/var/cron/
for foo in *.dist; do cp $foo `basename $foo .dist`; done

# all needed files packaged from %%builddir
rm -f %buildroot%installdir/ARCHIVE
rm -f %buildroot%installdir/AUTHORS.md
rm -f %buildroot%installdir/CHANGES.md
rm -f %buildroot%installdir/CONTRIBUTING.md
rm -f %buildroot%installdir/COPYING
rm -f %buildroot%installdir/COPYING-Third-Party
rm -f %buildroot%installdir/INSTALL.md
rm -f %buildroot%installdir/README.md
rm -f %buildroot%installdir/SECURITY.md
rm -f %buildroot%installdir/UPDATING.md
rm -f %buildroot%installdir/Custom/README

%pre
if id %otrs_user >/dev/null 2>&1; then
    # update groups
    usermod -g %webserver_group %otrs_user
    # update home dir
    usermod -d %installdir %otrs_user
else
   %_sbindir/useradd -r  -g %webserver_group -c 'OTRS User' -d %installdir -s '/dev/null' %otrs_user >/dev/null 2>&1 ||:
fi

%post
cd %installdir/bin/
./otrs.SetPermissions.pl \
    --otrs-user=%otrs_user \
    --web-user=root \
    --otrs-group=%webserver_group \
    --web-group=%webserver_group \
    --skip-regex="Config.pm" \
    %installdir >/dev/null 2>&1
#./Cron.sh start %otrs_user >/dev/null 2>&1

%postun
#rm -rf %_docdir/%name-%version/

%post apache2
%post_apache2_rpma2chkconfigfile

%postun apache2
%post_apache2_rpma2chkconfigfile

%files
%doc ARCHIVE
%doc AUTHORS.md
%doc CHANGES.md
%doc CONTRIBUTING.md
%doc COPYING
%doc COPYING-Third-Party
%doc INSTALL.md
%doc README.md
%doc README.ALT.rus
%doc SECURITY.md
%doc UPDATING.md
%doc Custom/README
%defattr(0775,root, %webserver_group)
%dir %installdir
%config(noreplace) %attr(0660,root,%webserver_group) %installdir/Kernel/Config.pm
#config(noreplace) %attr(0660,root,%webserver_group) %installdir/Kernel/Config/GenericAgent.pm
%installdir/bin
%installdir/Kernel
%installdir/scripts
%installdir/doc
%installdir/var
%installdir/i18n
%installdir/RELEASE

%config(noreplace) %attr(0644,root,root) %_sysconfdir/apt/apt.conf.d/%name-hold.conf

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%changelog
* Fri Aug 21 2020 Sergey Y. Afonin <asy@altlinux.org> 6.0.29-alt1
- New version
- updated License tag to SPDX syntax
- updated README.ALT.rus

* Fri Oct 25 2019 Sergey Y. Afonin <asy@altlinux.org> 6.0.23-alt1
- New version (ALT #37331)
- changed License (GAGPLv3 to GPLv3)
- updated Apache 2 configuration
- updated README.ALT.rus
- removed otrs-InnoDBLogFileSize.patch
- updated Requires
- removed Packager field

* Fri Nov 10 2017 Sergey Y. Afonin <asy@altlinux.ru> 5.0.23-alt1
- New version

* Thu May 04 2017 Sergey Y. Afonin <asy@altlinux.ru> 5.0.17-alt1
- New version
- added */examples/* to findreq_skiplist
- updated description for Apache 2.4 in README.ALT.rus

* Tue May 31 2016 Sergey Y. Afonin <asy@altlinux.ru> 5.0.10-alt1
- New version
- added description for Apache 2.4 to README.ALT.rus

* Mon Mar 14 2016 Sergey Y. Afonin <asy@altlinux.ru> 5.0.7-alt1
- New version

* Fri Feb 05 2016 Sergey Y. Afonin <asy@altlinux.ru> 5.0.6-alt1
- New version

* Fri Oct 23 2015 Sergey Y. Afonin <asy@altlinux.ru> 5.0.1-alt1
- New version
- updated otrs-InnoDBLogFileSize.patch
- updated README.ALT.rus

* Fri Oct 16 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.0.13-alt1
- New version
- fixed otrs-hold.conf

* Wed Sep 16 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.0.12-alt1
- New version
- added perl-Archive-Tar to Requires
- updated README.ALT.rus

* Mon Aug 03 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.0.10-alt1
- New version
- added mpm_itk_module section to configuration of apache2

* Tue Jun 09 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.0.8-alt1
- New version

* Sat Apr 25 2015 Sergey Y. Afonin <asy@altlinux.ru> 4.0.7-alt1
- New version

* Sat Nov 08 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.3.10-alt1
- New version (ALT #30453)

* Tue Sep 02 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.3.8-alt1
- New version

* Tue Mar 18 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.3.5-alt2
- added to Requires: perl-Time-Piece

* Wed Mar 12 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.3.5-alt1
- New version

* Fri May 17 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.2.6-alt2
- added to Requires:
  perl-Term-ANSIColor perl-TimeDate perl-YAML-LibYAML
- added apt's hold file for the package otrs

* Fri May 17 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.2.6-alt1
- New version (ALT #28490)

* Sun Mar 10 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.2.2-alt1
- New version
- disabled doc-admin-de-pdf subpackage (missed in this release)

* Tue Oct 09 2012 Sergey Y. Afonin <asy@altlinux.ru> 3.1.10-alt1
- New version
   Warning: OTRS 3.1 supports only UTF-8 as internal character set.
            Non-UTF-8 installations of OTRS must switch to UTF-8.
- added perl-Unicode-Normalize to Requires
- described GenericAgent.pm as %%config
- used %%post_apache2_rpma2chkconfigfile instead of "httpd2 condreload"

* Tue Feb 07 2012 Pavel Zilke <zidex at altlinux dot org> 2.4.11-alt1.2
- spec fixes

* Fri Sep 30 2011 Pavel Zilke <zidex at altlinux dot org> 2.4.11-alt1.1
- spec fixes

* Thu Sep 29 2011 Pavel Zilke <zidex at altlinux dot org> 2.4.11-alt1
- Security fixes:
  + Vulnerabilities in OTRS-Core allows read access to any file on local file system;
    CVE-2011-2746 (ALT #26186)

* Mon Oct 25 2010 Pavel Zilke <zidex at altlinux dot org> 2.4.9-alt1
- Security fixes:
  + AgentTicketZoom is vulnerable to XSS attacks from HTML e-mails;
    OSA-2010-03 (ALT #24419)

* Wed Sep 22 2010 Pavel Zilke <zidex at altlinux dot org> 2.4.8-alt1
- New version 2.4.8

* Sun Feb 21 2010 Pavel Zilke <zidex at altlinux dot org> 2.4.7-alt1
- Security fixes:
  + Vulnerability in OTRS-Core allows SQL-Injection;
    CVE-2010-0438 (ALT #22947)

* Thu Jan 21 2010 Pavel Zilke <zidex at altlinux dot org> 2.4.6-alt1
- Initial build for ALT Linux

