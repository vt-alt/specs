%define pear_name Net_SMTP

Name: pear-Net_SMTP
Version: 1.9.0
Release: alt1

Summary: An implementation of the SMTP protocol

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Net_SMTP

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_SMTP-%version.tar

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

Requires: pear-Net_Socket >= 1.0.7

%description
Provides an implementation of the SMTP protocol using PEAR's Net_Socket
class.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_testdir/Net_SMTP/
%pear_dir/Net
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Tue Jan 28 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Sat Dec 02 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- new version 1.7.3 (with rpmrb script)

* Mon Jul 18 2016 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script)

* Fri Feb 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- new version 1.7.1 (with rpmrb script)

* Sun Oct 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version (1.4.2) import in git (ALT bug #24047)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.10-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.10-alt1
- initial build for ALT Linux Sisyphus

