Name:     libvzsock
Version:  7.0.3
Release:  alt4

Summary:  libvzsock is a helper library for networking connections code generalization.
License:  LGPLv2.1+
Group:    Other
# git-vsc https://src.openvz.org/scm/ovz/libvzsock.git
Url:      https://openvz.org/

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-%version.patch

ExclusiveArch: x86_64

BuildRequires: libssl-devel openssl libkrb5-devel

%description
%summary

%package devel
Summary: Virtuozzo socket development library
Group: Development/C
Requires: %name = %version-%release

%description devel
Virtuozzo socket development library

%prep
%setup
%patch -p1

%build
%add_optflags %optflags_shared
%make_build CFLAGS="$RPM_OPT_FLAGS"
make CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall_std
rm -f %buildroot%_libdir/%name.a

%files
%_libdir/*.so.*
%_datadir/%name

%files devel
%_libdir/%name.so
# dir %_includedir/vz
%_includedir/vz/*.h

%changelog
* Thu Sep 12 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.3-alt4
- spec cleanup

* Fri Aug 23 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.3-alt3
- fix lib permission
- remove static lib

* Mon Aug 19 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.3-alt2
- preserve debug info

* Thu Aug 01 2019 Andrew A. Vasilyev <andy@altlinux.org> 7.0.3-alt1
- Initial build for Sisyphus
