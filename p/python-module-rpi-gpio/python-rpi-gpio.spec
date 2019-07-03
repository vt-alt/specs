Group: Development/Python
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
# END SourceDeps(oneline)
%define oldname python-rpi-gpio
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname RPi.GPIO

%global __provides_exclude_from ^(%{python3_sitelibdir}/.*\\.so)$

Name:           python-module-rpi-gpio
Version:        0.6.5
Release:        alt1_1
Summary:        A class to control the GPIO on a Raspberry Pi

License:        MIT
URL:            https://sourceforge.net/projects/raspberry-gpio-python/
Source0:        http://sourceforge.net/projects/raspberry-gpio-python/files/RPi.GPIO-%{version}.tar.gz

ExclusiveArch:  %{arm} aarch64

BuildRequires:  gcc
Source44: import.info

%description
Python library for GPIO access on a Raspberry Pi.

%package -n python3-module-RPi.GPIO
Group: Development/Python
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-module-distribute
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-module-RPi.GPIO
Python 3 library for GPIO access on a Raspberry Pi.

%prep
%setup -q -n %{srcname}-%{version}


%build
%python3_build

%install
%python3_install

%files -n python3-module-RPi.GPIO
%doc README.txt
%doc --no-dereference LICENCE.txt
%{python3_sitelibdir}/RPi*

%changelog
* Mon Jul 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.5-alt1_1
- new version

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1a-alt1_2
- update to new release by fcimport

* Tue Jan 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1a-alt1_1
- initial fc import

