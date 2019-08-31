Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global shortname listSerialPortsC

Name:		arduino-%{shortname}
Version:	1.4.0
Release:	alt1_4
Summary:	Simple multiplatform program to list serial ports with vid/pid/iserial fields
License:	LGPLv3+
URL:		http://www.arduino.cc
Source0:	https://github.com/arduino/listSerialPortsC/archive/%{version}.tar.gz#/%{shortname}-%{version}.tar.gz
BuildRequires:	libserialport-devel, java-devel
BuildRequires:	gcc
Source44: import.info

%description
Simple environment to test libserialport in a single build machine fashion.

%prep
%setup -q -n %{shortname}-%{version}

%build
gcc `pkg-config --cflags libserialport` %{optflags} main.c `pkg-config --libs libserialport` -o listSerialC
gcc `pkg-config --cflags libserialport` %{optflags} jnilib.c -I/usr/lib/jvm/java/include/ -I/usr/lib/jvm/java/include/linux -shared -fPIC `pkg-config --libs libserialport` -o liblistSerialsj.so

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 listSerialC %{buildroot}%{_bindir}
# Yes, this is not normal, but this isn't really a useful lib, it's only for arduino.
mkdir -p %{buildroot}%{_libdir}/arduino/
install -m755 liblistSerialsj.so %{buildroot}%{_libdir}/arduino/

%files
%doc --no-dereference LICENSE.md
%doc README.md
%{_bindir}/listSerialC
%{_libdir}/arduino/liblistSerialsj.so

%changelog
* Fri Jul 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_4
- aarch64 build

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- new version

