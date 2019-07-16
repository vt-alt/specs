# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define oldname python-pycxx
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if (0%{?rhel} >= 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif
%global modname pycxx

# Specify '--without=python3' to NOT build the python 3 RPM
%if 0%{?rhel} && 0%{?rhel} <= 6
# el6 has no python3 packages
%global with_python3 0
%else
%global with_python3 %{?_without_python3:0} %{?!_without_python3:1}
%endif

%global svn_rev 280
%global download_date 20130805
%global vcs_rel %{download_date}svn%{svn_rev}

Name:           python-module-pycxx
Version:        7.1.3
Release:        alt1
Summary:        Write Python extensions in C++

Group:          Development/Other
License:        BSD
URL:            http://CXX.sourceforge.net/

BuildArch:      noarch

# SVN version contains updates for Python3
Source0:        http://downloads.sourceforge.net/cxx/%{modname}-%{version}.tar.gz
#Source0:        http://sourceforge.net/code-snapshots/svn/c/cx/cxx/code/cxx-code-%{svn_rev}-trunk.zip
# Patch0:  remove unnecessary 'Src/' directory from include path in sources
Patch0:         %{oldname}-6.2.8-change-include-paths.patch

BuildRequires:  python-devel
%if %{with_python3}
BuildRequires:  python3-devel
%endif


%description
PyCXX is a set of classes to help create extensions of Python in the
C++ language. The first part encapsulates the Python C API taking care
of exceptions and ref counting. The second part supports the building
of Python extension modules in C++.


%package -n python-module-pycxx-devel
Summary:        PyCXX header and source files
Group:          Development/Other
Requires:       python

%description -n python-module-pycxx-devel
PyCXX is a set of classes to help create extensions of Python in the
C++ language. The first part encapsulates the Python C API taking care
of exceptions and ref counting. The second part supports the building
of Python extension modules in C++.

The %{oldname}-devel package provides the header and source files
for Python 2.  There is no non-devel package needed.


%package -n python3-module-pycxx-devel
Summary:        PyCXX header and source files
Group:          Development/Other
Requires:       python3

%description -n python3-module-pycxx-devel
PyCXX is a set of classes to help create extensions of Python in the
C++ language. The first part encapsulates the Python C API taking care
of exceptions and ref counting. The second part supports the building
of Python extension modules in C++.

The python3-%{modname}-devel package provides the header and source files
for Python 3.  There is no non-devel package needed.


%prep
# SVN version .zip file unpacks differently
#setup -q -n cxx-code-%{svn_rev}-trunk/CXX
%setup -q -n %{modname}-%{version}
%patch0 -p1 -b .change-include-paths


%build
python setup.py build


%install
INSTALL='setup.py install
        --root=%{buildroot}
        --prefix=%{_prefix}
        --install-headers=%{_includedir}/CXX
        --install-data=%{_usrsrc}'

%{__python} $INSTALL

%if %{with_python3}
%{__python3} $INSTALL
%endif

# Write pkg-config PyCXX.pc file
mkdir -p %{buildroot}%{_datadir}/pkgconfig
cat > %{buildroot}%{_datadir}/pkgconfig/PyCXX.pc <<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
includedir=%{_includedir}
srcdir=%{_usrsrc}/CXX

Name: PyCXX
Description: Write Python extensions in C++
Version: %{version}
Cflags: -I\${includedir}
EOF


%files -n python-module-pycxx-devel
%doc README.html COPYRIGHT Doc/Python2/ 
%dir %{_includedir}/CXX
%{_includedir}/CXX/*.hxx
%{_includedir}/CXX/*.h
%{_includedir}/CXX/Python2
%{python_sitelibdir_noarch}/CXX*
%dir %{_usrsrc}/CXX
%{_usrsrc}/CXX/*.cxx
%{_usrsrc}/CXX/*.c
%{_usrsrc}/CXX/Python2
%{_datadir}/pkgconfig/PyCXX.pc


%if %{with_python3}
%files -n python3-module-pycxx-devel
%doc README.html COPYRIGHT Doc/Python3/ 
%dir %{_includedir}/CXX
%{_includedir}/CXX/*.hxx
%{_includedir}/CXX/*.h
%{_includedir}/CXX/Python3
%{python3_sitelibdir_noarch}/CXX*
%dir %{_usrsrc}/CXX
%{_usrsrc}/CXX/*.cxx
%{_usrsrc}/CXX/*.c
%{_usrsrc}/CXX/Python3
%{_datadir}/pkgconfig/PyCXX.pc
%endif


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion PyCXX)" = "%{version}"


%changelog
* Wed Jul 10 2019 Grigory Ustinov <grenka@altlinux.org> 7.1.3-alt1
- Build new version.

* Wed Apr 17 2019 Grigory Ustinov <grenka@altlinux.org> 7.1.2-alt1
- Initial build for Sisyphus.

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 6.2.8-alt1_4
- update to new release by fcimport

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 6.2.8-alt1_2
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_12.20130805svn280
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_10.20130805svn280
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_9.20130805svn280
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_7.20130805svn280
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_5
- update to new release by fcimport

* Sat Jan 05 2013 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_3
- initial fc import

