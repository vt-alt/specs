# vim: set ft=spec: -*- rpm-spec -*-
# hey Emacs, its -*- rpm-spec -*-

%define macrosname apache2

# do we need to co-exist with apache-ru ?
%def_enable apache_ru_compat

Name: rpm-macros-%macrosname
Version: 3.13.1
Release: alt1

Summary: RPM macros to Apache2 Web server
Summary(ru_RU.UTF-8): RPM макросы для веб-сервера Apache2
License: %asl
Group: Development/Other
BuildArch: noarch

# rpm macro definitions
Source1: %macrosname.rpm-macros
Source2: %macrosname-compat.rpm-macros

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm >= 4.0.4-alt96.13
BuildPreReq: rpm-macros-webserver-common >= 1.3

Conflicts: rpm-macros-webserver-common < 1.4
Conflicts: apache2-devel <= 2.2.16-alt1
Requires: rpm-macros-webserver-common >= 1.4

%description
The package provide a set of macros for packaging Web applications
according to the ALT Linux Web Packaging Policy.

%description -l ru_RU.UTF-8
Макросы для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.


%package compat
Summary: RPM macros to Apache2 Web server
Summary(ru_RU.UTF-8): RPM макросы для веб-сервера Apache2
Group: Development/Other

Conflicts: apache-devel <= 1.3.41rusPL30.23-alt4.2
Conflicts: apache2-devel <= 2.2.9-alt2
Conflicts: rpm-macros-apache
Requires: %name >= %version

%description compat
The package provide a set of macros for packaging Web applications
according to the ALT Linux Web Packaging Policy.

%description compat -l ru_RU.UTF-8
Макросы для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.


%install
install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%macrosname
install -pD -m644 %SOURCE2 %buildroot%_rpmmacrosdir/%macrosname-compat

%if_disabled apache_ru_compat
find %buildroot%_rpmmacrosdir/ -type f -print0 \
	| xargs -r0 sed -ri "
/^[[:space:]]*%%apache2_branch[[:space:]]/s/^([[:space:]]*%%apache2_branch[[:space:]]+)[^[:space:]].*$/\1%%nil/
"
%endif

%files
%_rpmmacrosdir/%macrosname

%files compat
%_rpmmacrosdir/%macrosname-compat

%changelog
* Fri May 21 2021 Anton Farygin <rider@altlinux.ru> 3.13.1-alt1
- returned back macro %post_apache2conf

* Mon May 17 2021 Anton Farygin <rider@altlinux.ru> 3.13-alt1
- removed all macros, which is suitable for post-script in rpm specfile
- removed branch suffix for release/version (is not needed anymore)

* Thu Mar 31 2016 Sergey Alembekov <rt@altlinux.ru> 3.12-alt2
- fix apxs path
- fix htcacheclean binary name
- fix htcacheclean_cachepath

* Tue Feb 05 2013 Aleksey Avdeev <solo@altlinux.ru> 3.12-alt1
- Add new macros:
  + %%apache2_docdir_prefix
  + %%apache2_libapr_name
  + %%apache2_libapr_evr
  + %%apache2_libaprutil_name
  + %%apache2_libaprutil_evr

* Sat Jan 26 2013 Aleksey Avdeev <solo@altlinux.ru> 3.11-alt1
- Fix macros %%apache2_libssl_soname
- Add new macros:
  + %%apache2_ssldir
  + %%apache2_sslcertsdir
  + %%apache2_sslkeysdir
  + %%apache2_sslcertname
  + %%apache2_sslcertext
  + %%apache2_sslcertificatefile
  + %%apache2_sslcertificatekeyfile
  + %%apache2_sslrootcertfilename
  + %%apache2_sslcertsh
  + %%apache2_sslcertshfunctions

* Fri Jan 11 2013 Aleksey Avdeev <solo@altlinux.ru> 3.10-alt1
- Add new macros %%post_apache2_rpmrenamevarinconfig

* Thu Oct 11 2012 Aleksey Avdeev <solo@altlinux.ru> 3.9-alt1
- Add new macros:
  + %%apache2_create_rpmfiletriggerdir
  + %%post_apache2_rpmhttpdrestartfile
  + %%post_apache2_rpmhtcachecleanrestartfile
  + %%post_apache2_rpma2chkconfigfile

* Wed Oct 03 2012 Aleksey Avdeev <solo@altlinux.ru> 3.8-alt2
- Fix macros %%post_apache2conf and %%postun_apache2conf:
  use /sbin/service

* Tue Aug 14 2012 Aleksey Avdeev <solo@altlinux.ru> 3.8-alt1
- Remove repocop-unittest-data-%%name subpackage (Closes: #26076)
- Add new macros:
  + %%apache2_apachectl_name
  + %%apache2_apachectl
  + %%apache2_apxs_name
  + %%apache2_envconf

* Fri Jul 15 2011 Aleksey Avdeev <solo@altlinux.ru> 3.7-alt1
- Add new macros %%apache2_rpmhtcachecleanrestartfile

* Wed Jul 06 2011 Aleksey Avdeev <solo@altlinux.ru> 3.6-alt1
- Add new macros:
  + %%apache2_htcacheclean_dname
  + %%apache2_htcacheclean_cachepath
  + %%apache2_htcacheclean_lockdir
  + %%apache2_htcacheclean_piddir

* Sun Jun 05 2011 Aleksey Avdeev <solo@altlinux.ru> 3.5-alt1
- Add new macros %%triggerun_apache2_rpmhttpdstartfile

* Fri Jun 03 2011 Aleksey Avdeev <solo@altlinux.ru> 3.4-alt1
- Add new macros %%apache2_httpdlockfile

* Fri Jun 03 2011 Aleksey Avdeev <solo@altlinux.ru> 3.3-alt1
- Add new macros %%apache2_rpmhttpdstartfile

* Fri May 27 2011 Aleksey Avdeev <solo@altlinux.ru> 3.2-alt1
- Add new macros:
  + %%apache2_rpmfiletriggerdir
  + %%apache2_rpmhttpdrestartfile
  + %%apache2_rpma2chkconfigfile

* Wed Oct 20 2010 Aleksey Avdeev <solo@altlinux.ru> 3.1-alt1
- Add new macros %%apache2_confdir_inc

* Wed Oct 20 2010 Aleksey Avdeev <solo@altlinux.ru> 3.0-alt1
- Remove %%apache2_distr_switch macros
- Set Conflicts: apache2-devel <= 2.2.16-alt1
- Add new macros:
  + %%apache2_uploadsdir
  + %%apache2_uploadslink
  + %%apache2_lockdir
  + %%apache2_locklink

* Wed Dec 10 2008 Aleksey Avdeev <solo@altlinux.ru> 2.1-alt1
- Fix %%apache2_apr_buildreq sets (Closes: #18167)

* Wed Nov 12 2008 Aleksey Avdeev <solo@altlinux.ru> 2.0-alt1
- Remove %%name-%%apache2_libdb_name provides and %%apache2_libdb* macros
- Add Conflicts: apache2-devel < 2.2.9-alt12.1

* Fri Aug 15 2008 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt2
- Use libdb4.4-devel by default

* Thu Aug 14 2008 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt1
- Fix %%apache2_libssl* macros sets

* Thu Aug 14 2008 Aleksey Avdeev <solo@altlinux.ru> 1-alt1
- Add libdb and distr switchers (%%nil by default)
- Add new macros:
  + %%apache2_libdb*
  + %%apache2_distr_switch
  + %%apache2_libdb_soname
- Add new provides: %%name-%%apache2_libdb_name = %%apache2_libdb_soname
- Turn back conditional libdb4-devel default, libdb4.4-devel (for M40 and M41),
  libdb4.3-devel (for M30) or libdb4.2-devel (for M24) build

* Tue Aug 05 2008 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt2
- Fix Requires/Conflicts

* Tue Aug 05 2008 Aleksey Avdeev <solo@altlinux.ru> 0.3-alt1
- Create repocop-unittest-data-%%name subpackage for repocop tests
- Add new macros:
  + %%apache2_manualaddonsdir
  + %%apache2_compat_manualaddonsdir
- Remove %%apache2_compat_htdocsaddondir macros (move to %%name-compat
  subpackage)

* Sat Aug 02 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt2
- Add conflict with the package rpm-macros-apache

* Sat Aug 02 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add macros for pid file

* Fri Aug 01 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Add apache_ru_compat switcher (enabled by default)

* Tue Jul 15 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt0.1
- First build for ALT Linux
