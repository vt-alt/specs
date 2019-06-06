# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libkdtree++
Version:        0.7.0
Release:        alt2_21
Summary:        C++ template container implementation of kd-tree sorting
URL:            http://libkdtree.alioth.debian.org/
License:        Artistic 2.0
BuildRequires:  gcc-c++
BuildRequires:  autoconf automake python3-devel swig

Source0:        http://alioth.debian.org/frs/download.php/2702/libkdtree++-0.7.0.tar.bz2

# patch to make GCC 4.7 happy (fixed in upstream git, not yet in release):
Patch0:         libkdtree++-0.7.0-pedantic.patch
# patch to make pkgconfig file (.pc) (submitted to upstream mailing list
# on 29-Sep-2012):
Patch1:         libkdtree++-0.7.0-pkgconfig.patch
# patch to build examples/test with optflags
Patch2:         libkdtree++-0.7.0-examples-optflags.patch
# patch to build with GCC 5 or later, from Debian bug 777951
Patch3:         libkdtree++-0.7.0-gcc5.patch
# patch for Python 3 compatibility, portions from Debian
Patch4:         libkdtree++-0.7.0-py3.patch
Source44: import.info

%description
%{summary}.


%package devel
Group: Development/C
Summary:        C++ template container implementation of kd-tree sorting
Provides:       libkdtree++-static = %{version}
BuildArch:      noarch

%description devel
%{summary}.


%package -n python3-module-libkdtree++
Group: System/Libraries
Provides: %{name}-python3 = %{version}-%{release}
Summary:        Python3 language bindings for libkdtree++

%description -n python3-module-libkdtree++
%{summary}.


%package examples
Group: Development/C
Summary:        Examples for libkdtree++
BuildArch:      noarch

%description examples
%{summary}.


%prep
%setup -q -n %{name}_%{version}
%patch0 -p1 -b .pkgconfig
%patch1 -p1 -b .pkgconfig
%patch2 -p1 -b .examples-optflags
%patch3 -p1 -b .gcc5
%patch4 -p1 -b .py3

# convert files from ISO-8859-1 to UTF-8 encoding
for f in README
do
  iconv -fiso88591 -tutf8 $f >$f.new
  touch -r $f $f.new
  mv $f.new $f
done


%build
autoreconf -f -i
%configure
make

cd python-bindings
make CPPFLAGS="%{optflags} -fPIC `pkg-config --cflags python3`"
cd ..

%check
cd examples
make %{?_smpflags} CPPFLAGS="%{optflags}"
./test_kdtree
./test_hayne
cd ..

cd python-bindings
python3 py-kdtree_test.py
cd ..

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{python3_sitelibdir}
install -pm 0755 python-bindings/_kdtree.so %{buildroot}%{python3_sitelibdir}/
install -d %{buildroot}%{python3_sitelibdir_noarch}
install -pm 0644 python-bindings/kdtree.py %{buildroot}%{python3_sitelibdir_noarch}/

%files devel
%doc COPYING AUTHORS README NEWS TODO ChangeLog
%{_includedir}/kdtree++/
%{_datadir}/pkgconfig/*.pc

%files -n python3-module-libkdtree++
%doc COPYING AUTHORS README NEWS TODO ChangeLog
%{python3_sitelibdir}/_kdtree.so
%{python3_sitelibdir_noarch}/kdtree.py
%{python3_sitelibdir_noarch}/__pycache__/*

%files examples
%doc examples/CMakeLists.txt
%doc examples/Makefile
%doc examples/test*.cpp

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_21
- update to new release by fcimport

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_8
- fixed build

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- initial fc import

