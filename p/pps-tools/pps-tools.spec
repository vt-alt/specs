Name: pps-tools
Version: 1.0.2
Release: alt1

Summary: Userspace tools for kernel PPS
License: GPLv2
Group: System/Configuration/Other
Url: https://github.com/redlab-i/pps-tools
Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

%description
Userspace tools for kernel PPS

%package devel
Summary: Development package that includes the %name header files
Group: Development/C

%description devel
The devel package contains the include files

%prep
%setup
%patch0 -p1

%build
%make

%install
%makeinstall_std

%files
%doc COPYING
%_bindir/*

%files devel
%_includedir/sys/*

%changelog
* Wed Mar 10 2021 Alexei Takaseev <taf@altlinux.org> 1.0.2-alt1
- Initial build for ALT Linux Sisyphus.
