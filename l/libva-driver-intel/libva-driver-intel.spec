Name: libva-driver-intel
Version: 2.4.0
Release: alt1

Summary: VA-API (Video Acceleration API) user mode driver for Intel GEN Graphics family
License: GPLv2
Group: System/Libraries
Url: http://cgit.freedesktop.org/vaapi/intel-driver/

Conflicts: libva < 1.1.0

Source: %name-%version.tar

BuildRequires: intel-gen4asm
BuildRequires: libdrm-devel libX11-devel libGL-devel libEGL-devel python3 rpm-build-python3
BuildRequires: libva-devel >= 1.7.0
ExclusiveArch: %ix86 x86_64

%description
Video decode driver for Intel chipsets.

%prep
%setup

%build
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS NEWS
%_libdir/dri/*.so

%changelog
* Mon Jan 13 2020 Anton Farygin <rider@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Mon Feb 18 2019 Anton Farygin <rider@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Sat Jul 21 2018 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Mon Jun 04 2018 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Jan 24 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- up to 2.0.0

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.8.3-alt2
- fixed summary (closes: #33639)

* Thu Jul 06 2017 Anton Farygin <rider@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Thu Jun 01 2017 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- new version

* Sun Oct 30 2016 L.A. Kostis <lakostis@altlinux.ru> 1.7.2-alt1
- 1.7.2.

* Thu Jul 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- 1.7.1 released

* Tue Nov 18 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Fri Jan 24 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu Jun 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.18-alt1
- 1.0.18
