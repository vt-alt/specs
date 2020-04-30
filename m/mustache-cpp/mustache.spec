Group: Development/C++
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-ninja-build
# END SourceDeps(oneline)
%define oldname mustache
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global appname Mustache

Name: mustache-cpp
Version: 4.0
Release: alt1_2

License: Boost
Summary: Mustache text templates for modern C++

URL: https://github.com/kainjow/%{appname}
Source0: %{url}/archive/v%{version}.tar.gz#/%{oldname}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: ctest cmake
BuildRequires: gcc

BuildArch: noarch
Source44: import.info

%description
Text templates implementation for modern C++ (requires C++11).

%package devel
Group: Development/C++
Summary: Development files for %{oldname}
Provides: %{oldname}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{oldname} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{oldname}-devel package contains C++ headers for developing
applications that use %{oldname}.

%prep
%setup -q -n %{appname}-%{version}

mkdir -p %{_target_platform}
sed -e '/-Werror/d' -i CMakeLists.txt

%build
pushd %{_target_platform}
    %{fedora_cmake} -G Ninja \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 -p %{oldname}.hpp %{buildroot}%{_includedir}

%files devel
%doc README.md
%doc --no-dereference LICENSE
%{_includedir}/%{oldname}.hpp

%changelog
* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2
- update to new release by fcimport

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_2
- new version

