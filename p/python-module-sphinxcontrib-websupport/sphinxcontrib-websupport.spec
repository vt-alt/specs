%define _unpackaged_files_terminate_build 1

%define oname sphinxcontrib-websupport

%def_disable check

Name:           python-module-%oname
Version:        1.0.1
Release:        alt5
Summary:        Sphinx API for Web Apps
License:        BSD
Group:          Development/Python
BuildArch:      noarch
URL:            http://sphinx-doc.org/

# https://github.com/sphinx-doc/sphinxcontrib-websupport.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-docutils python-module-jinja2 python-module-mock python-module-pytest
BuildRequires: python-module-setuptools python-module-six python-module-sphinx python2.7(sqlalchemy)
BuildRequires: python-module-whoosh python-module-xapian

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%prep
%setup

%build
%python_build

%install
%python_install

%check
py.test tests/

%files
%doc LICENSE README.rst
%python_sitelibdir/sphinxcontrib/websupport
%python_sitelibdir/sphinxcontrib_websupport-%{version}*-py?.?-*.pth
%python_sitelibdir/sphinxcontrib_websupport-%{version}*-py?.?.egg-info

%changelog
* Tue Sep 24 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt5
- Rebuild without support for python-3.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4.qa1
- NMU: remove rpm-build-ubt from BR:

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3.qa1
- NMU: applied repocop patch

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt3
- (NMU) rebuild with python3.6

* Wed Mar 21 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2
- Rebuild with new setuptools to fix namespace package

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.

* Wed Oct 11 2017 Troy Dawson <tdawson@redhat.com> - 1.0.1-3
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Javier Peña <jpena@redhat.com> - 1.0.1-1
- Initial package.
