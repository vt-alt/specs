# TODO: botocore

%def_with plugins
%def_without dns_route53

Name: certbot
Version: 1.5.0
Release: alt2

Summary: A free, automated certificate authority client

License: ASL 2.0
Group: Networking/Other
Url: https://certbot.eff.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# #Source-url: https://pypi.python.org/packages/source/l/%name/%name-%version.tar.gz
# Source-url: https://github.com/certbot/certbot/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python3-devel python3-module-setuptools
BuildRequires(pre): rpm-build-python3 rpm-build-intro

%define acme_version %version

Requires: python3-module-zope.component
Requires: python3-module-zope.interface >= 4.1.0
Requires: python3-module-pyasn1 >= 0.1.8
Requires: python3-module-cffi >= 1.4.2
# missed by autoreq
Requires: python3-module-future

#Provides: python-module-%name = %EVR
#Obsoletes: python-module-%name < %EVR

# Due Prior to Python 2.7.9 the stdlib SSL module did not allow a user to configure
# See /usr/lib/python2.7/site-packages/acme/client.py
#Requires: python-base >= 2.7.9

# Required for documentation
#BuildRequires: python-sphinx
#BuildRequires: python-sphinx_rtd_theme
#BuildRequires: python-repoze-sphinx-autointerface
#BuildRequires: python-sphinxcontrib-programoutput

%py3_use acme >= %acme_version
%py3_use cryptography >= 1.2.3
%py3_use distro >= 1.0.1
%py3_use josepy >= 1.1.0
%py3_use parsedatetime >= 1.3

Provides: letsencrypt = %version
Obsoletes: letsencrypt

%define certbotdir %_datadir/%name
#add_python_req_skip certbot
%py3_provides certbot

# https://lists.altlinux.org/pipermail/devel/2012-March/193598.html
# https://lists.altlinux.org/pipermail/devel/2019-October/208661.html
%add_python3_path %certbotdir
%allow_python3_import_path %certbotdir

#add_python3_lib_path %certbotdir/certbot_nginx
#add_python3_lib_path %certbotdir/certbot_apache
#add_python3_lib_path %certbotdir/certbot_dns-rfc2136
#add_python3_lib_path %certbotdir/certbot_dns-route53
#add_python3_lib_path %certbotdir/certbot_postfix

%description
Let's Encrypt is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

# TODO: move to /usr/share/%name
%package -n python3-module-%name
Group: Networking/Other
Requires: python3-module-configargparse >= 0.10.0
# already in core python
#Requires: python-module-argparse
Requires: python3-module-psutil >= 2.1.0
Requires: python3-module-acme >= %acme_version
#Recommends: letsencrypt-doc
Summary: Python 3 libraries used by %name

Provides: python3-module-letsencrypt = %version
#Obsoletes: python-module-letsencrypt


%description -n python3-module-%name
The python2 libraries to interface with %name.

# TODO
%if_with plugins
%package apache
Group: Networking/Other
Summary: Certbot Apache plugin
AutoProv: no
Requires: %name = %EVR
# ALT bug 37004
Requires: python3-module-augeas

%description apache
Certbot Apache plugin.

%package nginx
Group: Networking/Other
Summary: Certbot nginx plugin
AutoProv: no
Requires: %name = %EVR

%description nginx
Certbot nginx plugin.

%package postfix
Group: Networking/Other
Summary: Certbot postfix plugin
AutoProv: no
Requires: %name = %EVR

%description postfix
Certbot postfix plugin.


%package dns_rfc2136
Group: Networking/Other
Summary: Certbot dns_rfc2136 plugin
AutoProv: no
Requires: %name = %EVR

%description dns_rfc2136
Certbot dns-rfc2136 plugin.

%package dns_route53
Group: Networking/Other
Summary: Certbot dns_route53 plugin
AutoProv: no
Requires: %name = %EVR

%description dns_route53
Certbot dns_route53 plugin.

%endif

%prep
%setup

%build
cd certbot
%python3_build

cd ../certbot-apache
%python3_build
cd ../certbot-nginx
%python3_build
#cd ../certbot-postfix
#python_build
cd ../certbot-dns-route53
%python3_build
cd ../certbot-dns-rfc2136
%python3_build


%install
cd certbot
%python3_install --install-purelib=%certbotdir

cd ../certbot-apache
%python3_install --install-purelib=%certbotdir
cd ../certbot-nginx
%python3_install --install-purelib=%certbotdir
#cd ../certbot-postfix
#python_install --install-purelib=%certbotdir
%if_with dns_route53
cd ../certbot-dns-route53
%python3_install --install-purelib=%certbotdir
%endif
cd ../certbot-dns-rfc2136
%python3_install --install-purelib=%certbotdir
cd -

# TODO: remove compat dirs
mkdir -p %buildroot%_sysconfdir/letsencrypt
ln -s letsencrypt %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_sharedstatedir/letsencrypt
ln -s letsencrypt %buildroot%_sharedstatedir/%name
mkdir -p %buildroot%_logdir/letsencrypt
ln -s letsencrypt %buildroot%_logdir/%name

ln -s %name %buildroot%_bindir/letsencrypt

rm -rfv %buildroot%certbotdir/certbot*/tests/
rm -rfv %buildroot%certbotdir/certbot/*/*_test*
rm -rfv %buildroot%certbotdir/certbot/*_test*
rm -rfv %buildroot%certbotdir/*/*_test*
rm -rfv %buildroot%certbotdir/certbot/certbot_compatibility_test/

#  it is better do not require argparse on python >= 2.7.
#__subst "s|^argparse$||" %buildroot%python_sitelibdir/%name-%{version}*.egg-info/requires.txt

%__subst 's|^__requires__.*|\
# ALT: use own package dir\
import site\
site.addsitedir("%certbotdir")|' %buildroot%_bindir/%name

%check
#python_test

%files
%doc LICENSE.txt
%doc README.rst CHANGELOG.md CONTRIBUTING.md
%_bindir/%name
#%doc %attr(0644,root,root) %_man1dir/%{name}*
%dir %_sysconfdir/%name/
%dir %_sharedstatedir/%name/
%dir %_logdir/%name/
# compats
%_bindir/letsencrypt
%dir %_sysconfdir/letsencrypt/
%dir %_sharedstatedir/letsencrypt/
%dir %_logdir/letsencrypt/

#files -n python-module-%name
#doc LICENSE.txt
%dir %certbotdir/
%certbotdir/%name/
%certbotdir/%name-%{version}*.egg-info

%if_with plugins
%files nginx
%doc LICENSE.txt
%certbotdir/certbot_nginx/
%certbotdir/certbot_nginx-%{version}*.egg-info

%files apache
%doc LICENSE.txt
%certbotdir/certbot_apache/
%certbotdir/certbot_apache-%{version}*.egg-info

#files postfix
#doc LICENSE.txt
#certbotdir/certbot_postfix/
#certbotdir/certbot_postfix-*.egg-info

%files dns_rfc2136
%doc LICENSE.txt
%certbotdir/certbot_dns_rfc2136/
%certbotdir/certbot_dns_rfc2136-%{version}*.egg-info

%if_with dns_route53
%files dns_route53
%doc LICENSE.txt
%certbotdir/certbot_dns_route53/
%certbotdir/certbot_dns_route53-%{version}*.egg-info
%endif
%endif

%changelog
* Tue Jun 23 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- build without dns-route53 (AWS Route 53) plugin

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Fri Feb 14 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Sat Oct 26 2019 Vitaly Lipatov <lav@altlinux.ru> 0.39.0-alt1
- new version 0.39.0 (with rpmrb script)

* Tue Sep 17 2019 Vitaly Lipatov <lav@altlinux.ru> 0.38.0-alt1
- new version 0.38.0 (with rpmrb script)
- switch to python3

* Fri Aug 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.37.2-alt1
- new version 0.37.2 (with rpmrb script)

* Fri Aug 16 2019 Vitaly Lipatov <lav@altlinux.ru> 0.37.1-alt1
- new version 0.37.1 (with rpmrb script)

* Fri Jun 28 2019 Vitaly Lipatov <lav@altlinux.ru> 0.35.1-alt1
- new version 0.35.1 (with rpmrb script)

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 0.34.2-alt1
- new version 0.34.2 (with rpmrb script)

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 0.32.0-alt1
- new version 0.32.0 (with rpmrb script)

* Sat Mar 02 2019 Vitaly Lipatov <lav@altlinux.ru> 0.31.0-alt2
- add dns_rfc2136, dns_route53 and postfix plugins
- provide python2.7(cerbot)

* Sat Feb 09 2019 Vitaly Lipatov <lav@altlinux.ru> 0.31.0-alt1
- new version 0.31.0 (with rpmrb script)

* Tue Feb 05 2019 Vitaly Lipatov <lav@altlinux.ru> 0.30.2-alt1
- new version 0.30.2 (with rpmrb script)

* Fri Dec 14 2018 Vitaly Lipatov <lav@altlinux.ru> 0.29.1-alt1
- new version 0.29.1 (with rpmrb script)

* Sat Nov 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.28.0-alt1
- new version 0.28.0 (with rpmrb script)

* Sat Oct 06 2018 Vitaly Lipatov <lav@altlinux.ru> 0.27.1-alt1
- new version 0.27.1 (with rpmrb script)

* Thu Aug 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.26.1-alt1
- new version 0.26.1 (with rpmrb script)

* Fri Jun 22 2018 Vitaly Lipatov <lav@altlinux.ru> 0.25.1-alt1
- new version 0.25.1 (with rpmrb script)

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 0.24.0-alt1
- new version 0.24.0 (with rpmrb script)

* Sat Mar 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.22.2-alt1
- new version 0.22.2 (with rpmrb script)

* Thu Mar 15 2018 Vitaly Lipatov <lav@altlinux.ru> 0.22.0-alt1
- new version 0.22.0 (with rpmrb script) (ALT bug 34643)

* Sun Jan 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt1
- new version 0.21.0 (with rpmrb script)

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.19.0-alt1
- new version 0.19.0 (with rpmrb script)
- drop python-module-cerbot subpackage
- pack nginx and apache plugins

* Tue Aug 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.2-alt1
- new version 0.14.2 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt1
- new version 0.14.1 (with rpmrb script)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Fri Mar 10 2017 Terechkov Evgenii <evg@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Fri Oct 07 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Thu Aug 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- rename to certbot, build version 0.8.1

* Thu Apr 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Fri Mar 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- new version 0.4.2 (with rpmrb script)
- fix requires

* Wed Feb 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 11 2016 Nick Bebout <nb@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Nick Bebout <nb@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
* Sat Jan 23 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.2.0-4
- Use acme dependency version consistently and add psutil min version
* Fri Jan 22 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-3
- Update the configargparse version in other places
* Fri Jan 22 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-2
- Update python-configargparse version requirement
* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-1
- Apache plugin support for non-Debian based systems
- Relaxed PyOpenSSL version requirements
- Resolves issues with the Apache plugin enabling redirect
- Improved error messages from the client
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-2
- Fix packaging issues
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- fix a confusing UI path that caused some users to repeatedly renew their
- certs while experimenting with the client, in some cases hitting issuance rate limits
- numerous Apache configuration parser fixes
- avoid attempting to issue for unqualified domain names like "localhost"
- fix --webroot permission handling for non-root users
* Tue Dec 08 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.0-3
- Add python-sphinx_rtd_theme build requirement
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Add documentation from upstream
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-5.dev20151123
- Add missing build requirements that slipped through
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-4.dev20151123
- The python2 library should have the dependencies and not the bindir one
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3.dev20151123
- Separate out the python libraries from the application itself
- Enable python tests
* Tue Dec 01 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec to account for the runtime dependencies discovered
- Update spec to sit inline with current python practices
* Sun Apr 26 2015 Torrie Fischer <tdfischer@hackerbots.net> 0-1.git1d8281d.fc20
- Initial package
