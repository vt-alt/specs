Name: fuse3
Version: 3.10.2
Release: alt1

Summary: a tool for creating virtual filesystems
License: GPL
Group: System/Kernel and hardware

Url: https://github.com/libfuse/

Source: %name-%version.tar
Source1: fuserumount3
Patch: %name-%version-alt.patch

Requires(pre): fuse-common >= 1.1.1

BuildRequires: meson ninja-build libudev-devel

%description
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort
as well as for using them.

%package -n lib%name
Group: System/Kernel and hardware
Summary: tool for creating virtual filesystems
Requires: %name = %version-%release

%description -n lib%name
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort.

This package contains shared libraries.

%package -n lib%name-devel
Group: System/Kernel and hardware
Summary: tool for creating virtual filesystems
Requires: lib%name = %version-%release

%description -n lib%name-devel
FUSE (Filesystem in USErspace), an excellent tool
for creating custom filesystems with minimal effort.

This package contains development headers.

%prep
%setup
%patch -p1

%build
%meson -Duseroot=false
%meson_build

%install
%meson_install

mkdir -p %buildroot/%_lib
mv %buildroot%_libdir/lib%name.so.* %buildroot/%_lib/
ln -sf ../../%_lib/lib%name.so.%version %buildroot%_libdir/lib%name.so

rm -fr %buildroot%_sysconfdir/init.d

install -pD %SOURCE1 %buildroot%_bindir/fuserumount3

%pre
if [ $1 -ge 2 -o -e %_bindir/fusermount ]; then
    %_sbindir/control-dump fusermount
fi

%post
if [ $1 -ge 2 -o -e %_bindir/fusermount ]; then
    %_sbindir/control-restore fusermount
else
    %_sbindir/control fusermount fuseonly
fi

%files
%doc AUTHORS README.md doc/README.NFS doc/kernel.txt
/usr/sbin/mount.fuse3
%attr(4710,root,fuse) %_bindir/fusermount3
%attr(0755,root,root) %_bindir/fuserumount3
%_man1dir/*
%_man8dir/*

# fuse-common-1.1.1-alt1 contains /etc/fuse.conf
%exclude %_sysconfdir/fuse.conf
# fuse-common-1.1.0-alt2 contains /lib/udev/rules.d/60-fuse.rules
%exclude %_udevrulesdir/99-%name.rules

%files -n lib%name
/%_lib/lib%name.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Sun Mar 28 2021 Evgeny Sinelnikov <sin@altlinux.org> 3.10.2-alt1
- update to latest release requires by newest gvfs from gnome project (fixes: 39759)

* Sun Mar 28 2021 Evgeny Sinelnikov <sin@altlinux.org> 3.4.1-alt3
- update build with upstream history

* Mon Feb 04 2019 Rustem Bapin <rbapin@altlinux.org> 3.4.1-alt2
- added fuserumount3 script
- added pre- and postinstall scriptlets that take account mode of already installed fuse package

* Mon Jan 14 2019 Evgeny Sinelnikov <sin@altlinux.org> 3.4.1-alt1
- update to latest release

* Tue Jul 25 2017 Denis Smirnov <mithraen@altlinux.ru> 3.1.0-alt1
- first build for Sisyphus (ALT#33529)
