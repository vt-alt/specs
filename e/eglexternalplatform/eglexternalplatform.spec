
Name:           eglexternalplatform
Version:        1.1
Release:        alt1
Summary:        EGL External Platform Interface headers
Group:		System/Libraries

License:        MIT
URL:            https://github.com/NVIDIA
Source0:        %name-%version.tar

BuildArch:      noarch

%description
%summary

%package        devel
Group: System/Libraries
Summary:        Development files for %{name}

%description    devel
The %{name}-devel package contains the header files for
developing applications that use %{name}.


%prep
%setup -q


%build

%install
mkdir -p %{buildroot}%{_includedir}/
install -p -m 0644 interface/eglexternalplatform.h %{buildroot}%{_includedir}/
install -p -m 0644 interface/eglexternalplatformversion.h %{buildroot}%{_includedir}/
mkdir -p %{buildroot}%{_datadir}/pkgconfig/
install -p -m 0644 eglexternalplatform.pc %{buildroot}%{_datadir}/pkgconfig/

%files devel
%doc README.md samples
%doc --no-dereference COPYING
%{_includedir}/*
%{_datadir}/pkgconfig/eglexternalplatform.pc




%changelog
* Fri Jul 12 2019 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- new version

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0
- new version
