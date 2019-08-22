
Summary: Management tools for Virtual Data Optimizer
Name: vdo
Version: 6.2.1.134
Release: alt1
Group: System/Base
License: GPLv2
Source: %name-%version.tar
Patch: %name-%version.patch

Url: http://github.com/dm-vdo/vdo
ExclusiveArch: x86_64 aarch64 ppc64le ppc64 s390 s390x

Requires: lvm2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libdevmapper-devel libdevmapper-event-devel
BuildRequires: libuuid-devel
BuildRequires: zlib-devel

%description
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space management tools for VDO.

%prep
%setup
%patch -p1

%build
%make

%install
%make install DESTDIR=%buildroot INSTALLOWNER= bindir=%_bindir \
  defaultdocdir=%_defaultdocdir name=%name \
  python3_sitelib=/%python3_sitelibdir mandir=%_mandir \
  unitdir=%_unitdir presetdir=%_presetdir sysconfdir=%_sysconfdir

%post
%post_service vdo

%preun
%preun_service vdo

%files
%_bindir/*

%python3_sitelibdir/*
%_unitdir/vdo.service
%_presetdir/97-vdo.preset
%dir %_defaultdocdir/%name
%doc %_defaultdocdir/%name/COPYING
%_defaultdocdir/%name/examples
%_man8dir/*
%_sysconfdir/bash_completion.d/vdo*

%changelog
* Sun Aug 11 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.1.134-alt1
- 6.2.1.134

* Thu Feb 21 2019 Alexey Shabalin <shaba@altlinux.org> 6.2.0.293-alt1
- initial build for ALT
