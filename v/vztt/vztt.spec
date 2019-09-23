
%define _libexecdir /usr/libexec
%define confdir /etc/vztt
%define vztempldir /var/lib/vz/template
%define vzconfdir %vztempldir/conf/%name
%define vztt_conf %confdir/vztt.conf
%define nojquota_conf %confdir/nojquota.conf
%define url_map %vzconfdir/url.map
%define url_map_link %confdir/url.map
%define vztmp /var/lib/vz/tmp
%define tmp_url_map %vztmp/tmp_url_map
%define tmp_vztt_conf %vztmp/tmp_vztt_conf

Name: vztt
Version: 7.0.65
Release: alt4
Summary: OpenVZ EZ template management tools
Source: %name-%version.tar
Patch: %name-%version.patch
License: GPLv2
Group: System/Configuration/Other
# git-vsc https://src.openvz.org/scm/ovzl/vztt.git
Url: https://openvz.org/

ExclusiveArch: x86_64

Requires: lib%name = %version-%release
Requires: libploop >= 6.1.0
Requires: attr
Requires: vztt_checker
#Requires: vzctl >= 5.0.0
Requires: lz4 gzip tar
Requires: e2fsprogs

BuildRequires: libattr-devel
BuildRequires: glibc-devel-static
BuildRequires: libuuid-devel
BuildRequires: libploop-devel >= 6.1.0
BuildRequires: libvzctl-devel >= 7.0.16
BuildRequires: libe2fs-devel

%description
OpenVZ EZ template management tools are used for software installation
inside Containers.

%package -n lib%name
Summary: OpenVZ EZ template management API library
Group: System/Libraries
License: GPLv2 or LGPLv2.1

%description -n lib%name
OpenVZ EZ template management API library

%package -n lib%name-devel
Summary: OpenVZ EZ template management API development library
Group: Development/C
License: GPLv2 or LGPLv2.1
Requires: lib%name = %version-%release

%description -n lib%name-devel
OpenVZ EZ template management library and include files

%prep
%setup
%patch -p1

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std LIBDIR=%buildroot%_libdir

# create logrotate config
mkdir -p %buildroot%_logrotatedir
echo "/var/log/vztt.log {
        compress
        missingok
}" > %buildroot%_logrotatedir/vztt
rm -f %buildroot%_libdir/lib%name.a

%files
%_sbindir/vzpkg
%dir %_libdir/%name
%_libdir/%name/myinit
%_man8dir/vzpkg.8.*
%dir %confdir
%dir %vztempldir
%dir %vztempldir/conf
%dir %vzconfdir
%config(noreplace) %vztt_conf
%config(noreplace) %nojquota_conf
%config(noreplace) %url_map
%url_map_link
%config(noreplace)  %_logrotatedir/vztt
%_libexecdir/*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/vz/*.h
%_libdir/lib%name.so

%changelog
* Thu Sep 12 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.65-alt4
- spec cleanup

* Thu Sep 12 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.65-alt3
- add distribution name to config in template converter

* Fri Aug 23 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.65-alt2
- remove static lib
- package_manager file should not be empty

* Mon Aug 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.65-alt1
- 7.0.65

* Sun Nov 04 2018 Alexey Shabalin <shaba@altlinux.org> 7.0.60-alt1
- 7.0.60

* Mon Feb 26 2018 Alexey Shabalin <shaba@altlinux.ru> 7.0.57-alt1
- initial build for ALT
