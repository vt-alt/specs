
Summary: A suite of tools for manipulating the metadata of the dm-thin device-mapper target.
Name: thin-provisioning-tools
Version: 0.8.1
Release: alt1
License: GPLv3+
Group: System/Base
Url: https://github.com/jthornber/thin-provisioning-tools
Source: %name-%version.tar
Patch: device-mapper-persistent-data-avoid-strip.patch

# add provides for RH compat
Provides: device-mapper-persistent-data = %EVR

BuildRequires: gcc-c++
BuildRequires: libexpat-devel libaio-devel boost-devel-headers

%description
thin-provisioning-tools contains check,dump,restore,repair,rmap
and metadata_size tools to manage device-mapper thin provisioning
target metadata devices; cache check,dump,metadata_size,restore
and repair tools to manage device-mapper cache metadata devices
are included and era check, dump, restore and invalidate to manage
snapshot eras

%prep
%setup
%patch -p1

echo %version > VERSION

%build
%autoreconf
%configure --with-optimisation=""
%make_build

%install
%makeinstall_std BINDIR=%buildroot%_sbindir

%files
%doc COPYING README.md
%_man8dir/*
%_sbindir/*

%changelog
* Wed May 15 2019 Alexey Shabalin <shaba@altlinux.org> 0.8.1-alt1
- 0.8.1

* Fri Aug 24 2018 Alexey Shabalin <shaba@altlinux.org> 0.7.6-alt1
- 0.7.6

* Tue Jan 09 2018 Alexey Shabalin <shaba@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Thu Jul 13 2017 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Fri Dec 30 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Mon Jun 20 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Thu Sep 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.6-alt1
- 0.5.6

* Fri Jul 17 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.3-alt1
- Initial build
