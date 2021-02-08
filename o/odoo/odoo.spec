%define  snapshot  20210112
%define  addonsdir %python_sitelibdir/odoo/addons

Name: 	 odoo
Version: 14.0
Release: alt1.%snapshot

Summary: Odoo is a suite of web based open source business apps
License: LGPL-3.0
Group:   System/Servers
URL:     http://www.odoo.com/
# Git: https://github.com/odoo/odoo (branch: 14.0)

Source0: %name.tar
Source1: odoo.service
Source2: odoo.init
Source3: README.ALT

Patch1: %name-alt-fix-openerp-import.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: rsync
BuildRequires: unzip 
BuildRequires: python3-devel 
BuildRequires: python3-module-setuptools
 
Provides:  tinyerp-server = %version-%release 
Obsoletes: tinyerp-server < %version-%release 
Provides:  openerp-server = %version-%release 
Obsoletes: openerp-server < %version-%release 
Provides:  openerp-web = %version-%release 
Obsoletes: openerp-web < %version-%release 
Provides:  openerp = %version-%release
Obsoletes: openerp < %version-%release
Provides:  openerp-httpd-fonts-access = %version-%release
Obsoletes: openerp-httpd-fonts-access < %version-%release

%filter_from_requires /python3(xmlrpclib)/d
%filter_from_requires /python3(odoo.addons.hw_drivers.tools)/d
%py3_requires feedparser gevent mako mock ofxparse PIL psutil pydot ldap pyparsing serial usb qrcode vatnumber vobject xlsxwriter xlwt num2words phonenumbers sassc
Requires: python3-module-suds
Requires: wkhtmltopdf
Requires: lessjs >= 3.0.0

%description
Server package for OpenERP.

OpenERP is a free Enterprise Resource Planning and Customer Relationship
Management software. It is mainly developed to meet changing needs.

The main functional features are: CRM & SRM, analytic and financial
accounting, double-entry stock management, sales and purchases
management, tasks automation, help desk, marketing campaign, ... and
vertical modules for very specific businesses.

Technical features include a distributed server, flexible work-flows, an
object database, dynamic GUIs, custom reports, NET-RPC and XML-RPC
interfaces, ...

For more information, please visit: http://www.openerp.com

This server package contains the core (server) of OpenERP system and all
additions of the official distribution. You may need the GTK client to
connect to this server, or the web-client which serves to HTML browsers.
You can also find more additions (aka. modules) for this ERP system in:
http://www.openerp.com/ or  http://apps.openerp.com/

%prep
%setup -q -n %name
%patch1 -p1
cp %SOURCE3 .

%build
NO_INSTALL_REQS=1 %python3_build

%install
%python3_install

# Install all addons
/bin/cp -a addons/* %buildroot%python3_sitelibdir/odoo/addons/

# Remove posbox and account_check_printing test
rm -rf %buildroot%python3_sitelibdir/odoo/addons/point_of_sale/tools/posbox \
       %buildroot%python3_sitelibdir/odoo/addons/account_check_printing/tests

# Install config file
mkdir -p %buildroot%_sysconfdir/odoo
cat > %buildroot%_sysconfdir/odoo/odoo.conf <<END.
[options]
admin_passwd = rbz
db_host = False
db_port = False
db_user = odoo
db_password = False
addons_path = %python3_sitelibdir/odoo/addons
# logging. Accepted values of log_level: info, debug_rpc, warn, test, critical, debug_sql, error, debug, debug_rpc_answer, notset
log_level = info
data_dir = /var/lib/odoo
END.

install -D -m 644 %SOURCE1 %buildroot%_unitdir/odoo.service
install -D -m 755 %SOURCE2 %buildroot%_initdir/odoo

install -d %buildroot%_logdir/odoo
install -d %buildroot%_spooldir/odoo
install -d %buildroot%_runtimedir/odoo
install -d %buildroot%_sharedstatedir/odoo

# Disable python2 requirement
subst 's|^#!.*env python2$|#!%__python3|' %buildroot%python3_sitelibdir/odoo/addons/mail/static/scripts/odoo-mailgate.py

%pre
getent group odoo > /dev/null || /usr/sbin/groupadd -r odoo
getent passwd _odoo > /dev/null || \
%_sbindir/useradd -M -r -g odoo -c 'Odoo Server' \
     -d %_sharedstatedir/odoo -s /sbin/nologin _odoo 2> /dev/null ||:

%post
%post_service odoo

%preun
%preun_service odoo

%files
%doc COPYRIGHT LICENSE *.md 
%doc README.ALT
%_bindir/*
%_unitdir/odoo.service
%_initdir/odoo
%python3_sitelibdir/odoo
%python3_sitelibdir/%name-*.egg-info
%_spooldir/odoo
%attr(0755,_odoo,odoo) %_logdir/odoo
%attr(0755,_odoo,odoo) %_runtimedir/odoo
%attr(0755,_odoo,odoo) %_sharedstatedir/odoo
%attr(0755,root,odoo) %dir %_sysconfdir/odoo
%attr(0660,root,odoo) %config(noreplace) %_sysconfdir/odoo/odoo.conf
#%%attr(-,openerp,openerp) %ghost %_logdir/openerp/openerp-server.log

%changelog
* Tue Jan 12 2021 Andrey Cherepanov <cas@altlinux.org> 14.0-alt1.20210112
- New version.
- Disable python2 requirement (ALT #39287).

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 12.0-alt3.20190424
- NMU: requires: s/suds-jurko/suds/

* Tue Apr 30 2019 Andrey Cherepanov <cas@altlinux.org> 12.0-alt2.20190424
- Fix license.

* Thu Apr 25 2019 Andrey Cherepanov <cas@altlinux.org> 12.0-alt1.20190424
- New version (ALT #36679).

* Tue May 15 2018 Andrey Cherepanov <cas@altlinux.org> 11.0-alt1.20180514
- New version.
- Require lessjs >= 3.0.0.
- Fix hard-coded 54px width and height in CSS.

* Fri Apr 27 2018 Andrey Cherepanov <cas@altlinux.org> 11.0-alt1.20180426
- New version.

* Wed Apr 04 2018 Andrey Cherepanov <cas@altlinux.org> 11.0-alt1.20180329
- New version.

* Wed Oct 19 2016 Andrey Cherepanov <cas@altlinux.org> 9.0c-alt1.20161004
- New version
- Renamed to Odoo since 9.0
- Remove all additional components

* Thu Apr 03 2014 Andrey Cherepanov <cas@altlinux.org> 7.0-alt3.20140326
- Use bundled fonts for icons on buttons
- Remove LibreOffice plugin from server distribution

* Fri Mar 28 2014 Andrey Cherepanov <cas@altlinux.org> 7.0-alt2.20140326
- Add missing requires
- Do not remove compiled Python files
- Place pixmaps to main directory

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1.20140326
- New version 7.0 (ALT #27570) syncronized with Mageia and Fedora
- Rename package and service to openerp
- Package some additional components (thanks Mageia) in openerp-full

* Tue Jan 22 2013 Andrey Cherepanov <cas@altlinux.org> 6.1.1-alt1
- New version 6.1
- Obsoletes openerp-web
- Run daemon under user _openerp privileges
- Add daemon script to run levels

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.0.14-alt2.1
- Rebuild with Python-2.7

* Tue Feb 22 2011 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt2
- update russian translation for modules
- fix default config path

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 5.0.14-alt1
- new version 5.0.14
- fix install run script (ALT bug #20460)
- fix requires (ALT bug #20497)

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.0-alt3.1
- Rebuilt with python 2.6

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 5.0.0-alt3
- add config and init script files

* Sat Mar 14 2009 Denis Klimov <zver@altlinux.org> 5.0.0-alt2
- new version 5.0.0-3
- remove neeless -q option from setup marcos
- change source url
- add requires to python-module-PyXML
- remove pychart from skip requires
- add sed command for replace needless buildroot item of path in 
  startup script
- add two python command before python_build macros as in 
  rpminstall_sh.txt
- add egg-info file to package

* Sun Jan 04 2009 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- rename package
- new version 5.0.0-rc3

* Thu Feb 21 2008 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt1
- new version 4.2.2 (with rpmrb script)
- build as noarch

* Fri Jan 18 2008 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- new version 4.2.1 (with rpmrb script)

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2
- update buildreq

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 3.5.0-alt0.1
- new version (3.5.0)

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 3.2.1-alt0.1
- new version

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 3.2.0-alt0.1
- initial build for ALT Linux Sisyphus
