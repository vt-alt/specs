%define oname urlgrabber

%def_with python3

Name: python-module-urlgrabber
Version: 4.0.0
Release: alt2

Summary: High-level cross-protocol url-grabber

License: LGPL
Group: Development/Python
URL: http://urlgrabber.baseurl.org/

# Source-url: https://pypi.io/packages/source/u/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

Patch: python-urlgrabber-2.9.6-reget.patch

BuildArch: noarch

Provides: urlgrabber

BuildRequires: python-devel python-modules-compiler python-modules-email python-modules-logging

BuildRequires: python-module-pycurl python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pycurl python3-module-rfc822py3 python3-module-six
#BuildRequires: python-tools-2to3
%endif

%description
python-urlgrabber is a high-level cross-protocol url-grabber for python
supporting HTTP, FTP and file locations. Features include keepalive, byte
ranges, throttling, authentication, proxies and more.

%package -n python3-module-%oname
Summary: High-level cross-protocol url-grabber
Group: Development/Python3

%description -n python3-module-%oname
python-urlgrabber is a high-level cross-protocol url-grabber for python
supporting HTTP, FTP and file locations. Features include keepalive, byte
ranges, throttling, authentication, proxies and more.

%prep
%setup
#patch0 -p1 -b .reget

%if_with python3
cp -fR . ../python3
#find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

# Set correct python2 executable in shebang and scripts
subst 's|#!.*python$|#!%__python|' $(grep -Rl '#!.*python$' *)

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install --prefix="%_prefix"
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install --prefix="%_prefix"
mv %buildroot/usr/libexec/urlgrabber-ext-down %buildroot%_bindir/

%files
%doc ChangeLog README TODO
%_docdir/%oname-%version/*
%_bindir/%oname
%_bindir/urlgrabber-ext-down
%python_sitelibdir/%oname/
%python_sitelibdir/%oname-*.egg-info/

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README TODO
%_bindir/%oname.py3
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-*.egg-info/
%endif

%changelog
* Fri Apr 17 2020 Pavel Vasenkov <pav@altlinux.org> 4.0.0-alt2
- Set correct python2 executable in shebang and scripts

* Wed May 08 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version (4.0.0) with rpmgs script
- cleanup spec, enable python3 module build

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.1-alt1.git20140204
- Version 3.10.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.0-alt1.1.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.1
- Rebuilt with python 2.6

* Tue Apr 29 2008 Mikhail Pokidko <pma@altlinux.org> 3.1.0-alt1
- Version up

* Mon Dec 17 2007 Mikhail Pokidko <pma@altlinux.org> 2.9.7-alt1
- Initial ALT build
