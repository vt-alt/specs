%global _unpackaged_files_terminate_build 1

Summary: OCI runtime written in C
Name: crun
Version: 0.9.1
Release: alt1
Group: Development/Other
License: GPLv3+
Url: https://github.com/containers/crun

Source0: %name-%version.tar
# git submodules
Source11: libocispec.tar
Source12: image-spec.tar
Source13: runtime-spec.tar

BuildRequires: libcap-devel
BuildRequires: libsystemd-devel
BuildRequires: libyajl-devel
BuildRequires: libseccomp-devel
BuildRequires: libselinux-devel
BuildRequires: go-md2man
BuildRequires: python3
Provides: oci-runtime = 2

%description
crun is a runtime for running OCI containers

%prep
%setup
tar -xf %SOURCE11 -C libocispec
tar -xf %SOURCE12 -C libocispec/image-spec
tar -xf %SOURCE13 -C libocispec/runtime-spec

%build
%autoreconf
%configure --disable-silent-rules
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/*.a

%files
%doc COPYING
%_bindir/%name
%_man1dir/*

%changelog
* Mon Sep 23 2019 Alexey Shabalin <shaba@altlinux.org> 0.9.1-alt1
- 0.9.1

* Fri Sep 13 2019 Alexey Shabalin <shaba@altlinux.org> 0.9-alt1
- Initial build

