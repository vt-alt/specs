%define  oname precis_i18n

Name:    python3-module-%oname
Version: 1.0
Release: alt1

Summary: Python3 implementation of PRECIS framework (RFC 8264, RFC 8265, RFC 8266)

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/precis-i18n
# https://github.com/byllyfish/precis_i18n

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
If you want your application to accept unicode user names and passwords,
you must be careful in how you validate and compare them. The PRECIS framework
makes internationalized user names and passwords safer for use by applications.
PRECIS profiles transform unicode strings into a canonical form,
suitable for comparison.

This module implements the PRECIS Framework as described in:

- PRECIS Framework: Preparation, Enforcement, and Comparison of
Internationalized Strings in Application Protocols (RFC 8264)
- Preparation, Enforcement, and Comparison of Internationalized Strings
Representing Usernames and Passwords (RFC 8265)
- Preparation, Enforcement, and Comparison of Internationalized Strings
Representing Nicknames (RFC 8266)

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Thu Jun 20 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1
- Initial build for Sisyphus (Closes: #36707).
