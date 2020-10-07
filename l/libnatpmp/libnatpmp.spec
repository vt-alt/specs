# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 1
%define libname libnatpmp%{major}
%define develname libnatpmp-devel

Summary: Direct concurrent to the UPnP IGD specification
Name: libnatpmp
Version: 20150609
Release: alt1_4
License: LGPLv2+
Group: System/Libraries
URL: http://miniupnp.free.fr/
Source: http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
Source44: import.info

%description
libnatpmp is an attempt to make a portable and fully compliant
implementation of the protocol for the client side. It is based on non
blocking sockets and all calls of the API are asynchronous. It is
therefore very easy to integrate the NAT-PMP code to any event driven code.

%package -n %{libname}
Summary: Direct concurrent to the UPnP IGD specification
Group: System/Libraries

%description -n %{libname}
libnatpmp is an attempt to make a portable and fully compliant
implementation of the protocol for the client side. It is based on non
blocking sockets and all calls of the API are asynchronous. It is
therefore very easy to integrate the NAT-PMP code to any event driven code.

%package -n %{develname}
Summary: Header files, libraries and development documentation for libnatpmp
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname} 
This package contains the header files and development documentation for
libnatpmp. If you like to develop programs using miniupnpc, you will need
to install libnatpmp-devel.

%prep
%setup -q

%build
%make_build \
	LDFLAGS="" \
	CFLAGS="-fPIC -Wall -DENABLE_STRNATPMPERR %{optflags}" \
	EXTRA_LD="%{?__global_ldflags}"

%install
make install \
	INSTALLPREFIX=%{buildroot}%{_prefix} \
	INSTALLDIRLIB=%{buildroot}%{_libdir} \
	INSTALLDIRINC="%{buildroot}%{_includedir}" \
	INSTALLDIRBIN="%{buildroot}%{_bindir}"

rm -f %{buildroot}%{_libdir}/*.a

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*.h


%changelog
* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 20150609-alt1_4
- update by mgaimport

* Sun May 06 2018 Igor Vlasenko <viy@altlinux.ru> 20150609-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 20140401-alt1_4
- new version

