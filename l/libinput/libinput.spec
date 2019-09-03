%def_disable snapshot

%define _libexecdir %_prefix/libexec
%def_enable libwacom
%def_enable debug_gui
%def_disable documentation
%def_enable tests
%def_enable install_tests

Name: libinput
Version: 1.14.1
Release: alt1

Summary: Input devices library
Group: System/Libraries
License: MIT
Url: http://www.freedesktop.org/wiki/Software/libinput/

%if_disabled snapshot
Source: http://www.freedesktop.org/software/%name/%name-%version.tar.xz
%else
#VCS: git://anongit.freedesktop.org/wayland/libinput
Source: %name-%version.tar
%endif

%add_python3_path %_libexecdir/%name

%define mtdev_ver 1.1.0
%define evdev_ver 0.4

BuildRequires(pre): meson rpm-build-python3
# for %%valgrind_arches
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: gcc-c++
BuildRequires: libmtdev-devel >= %mtdev_ver libevdev-devel >= %evdev_ver
BuildRequires: libudev-devel libsystemd-devel
BuildRequires: libcheck-devel
%{?_enable_libwacom:BuildRequires: libwacom-devel}
%{?_enable_debug_gui:BuildRequires: libgtk+3-devel}
%{?_enable_documentation:BuildRequires: doxygen graphviz}
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc gdb python3-module-pyparsing
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
}}

%description
libinput is a library that handles input devices for display servers and
other applications that need to directly deal with input devices.

It provides device detection, device handling, input device event
processing and abstraction so minimize the amount of custom input code
the user of libinput need to provide the common set of functionality
that users expect.

Input event processing includes scaling touch coordinates, generating
pointer events from touchpads, pointer acceleration, etc.

%package devel
Summary: libinput development package
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%package tools
Summary: tools for %name
Group: Development/Tools
Requires: %name = %version-%release

%description tools
This package contains commandline tools from %name package.

%package tools-gui
Summary: libinput visual debug helper
Group: Development/Tools
Requires: %name = %version-%release
Requires: %name-tools = %version-%release

%description tools-gui
This package contains visual debug helper for %name.

%prep
%setup

%build
%meson %{?_enable_libwacom:-Dlibwacom=true} \
       %{?_enable_debug_gui:-Ddebug-gui=true} \
       %{?_disable_documentation:-Ddocumentation=false} \
       %{?_disable_tests:-Dtests=false} \
       %{?_enable_install_tests:-Dinstall-tests=true} \
       -Dudev-dir=/lib/udev
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/%name.so.*
/lib/udev/%name-device-group
/lib/udev/%name-fuzz-override
%_datadir/%name/
%_udevrulesdir/80-%name-device-groups.rules
%_udevrulesdir/90-%name-fuzz-override.rules
%doc COPYING README*

%files devel
%_includedir/%name.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%files tools
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/*
%{?_enable_debug_gui:%exclude %_libexecdir/%name/%name-debug-gui}
%_man1dir/%name.1.*
%_man1dir/%name-debug-events.1.*
%_man1dir/%name-list-devices.1.*
%_man1dir/%name-measure.1.*
%_man1dir/%name-measure-fuzz.1.*
%_man1dir/%name-measure-touchpad-pressure.1.*
%_man1dir/%name-measure-touchpad-tap.1.*
%_man1dir/%name-measure-touch-size.1.*
%_man1dir/%name-quirks.1.*
%_man1dir/%name-quirks-list.1.*
%_man1dir/%name-quirks-validate.1.*
%_man1dir/%name-record.1.*
%_man1dir/%name-replay.1.*
%{?_enable_tests:%_man1dir/%name-test-suite.1.*}

%if_enabled debug_gui
%files tools-gui
%_libexecdir/%name/%name-debug-gui
%_man1dir/%name-debug-gui.1.*
%endif


%changelog
* Mon Aug 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Thu Aug 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Fri Jun 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.4-alt1
- 1.13.4

* Tue Jun 25 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.13.3-alt2
- Fixed build with disabled check.
- Enabled build of testsuite by default.

* Mon Jun 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.3-alt1
- 1.13.3

* Thu Jun 20 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt3
- glebfm@: Fixed testsuite on architectures not supported by valgrind,
           dropped redundant BR: libvalgrind-devel

* Wed Jun 19 2019 Michael Shigorin <mike@altlinux.org> 1.13.2-alt2
- move to rpm-macros-valgrind

* Thu May 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.2-alt1
- 1.13.2

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.1-alt1
- 1.13.1

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1.13.0-alt1
- 1.13.0

* Mon Jan 21 2019 Yuri N. Sedunov <aris@altlinux.org> 1.12.6-alt1
- 1.12.6

* Mon Jan 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1.12.5-alt1
- 1.12.5

* Tue Dec 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Wed Nov 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- updated to 1.12.3-6-g4e469291

* Wed Oct 24 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Thu Oct 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Tue Sep 11 2018 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Jul 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.3-alt1
- 1.11.3

* Tue Jul 03 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- 1.11.2

* Tue Jun 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- 1.11.1

* Tue Jun 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.7-alt1
- 1.10.7

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.6-alt1
- 1.10.6

* Thu Apr 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.5-alt1
- 1.10.5

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Wed Mar 07 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.4-alt1
- 1.9.4

* Tue Nov 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.3-alt1
- 1.9.3

* Wed Nov 15 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Thu Oct 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Thu Sep 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Jul 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Jul 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0
- new tools-gui subpackage

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Tue Apr 25 2017 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Feb 21 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Thu Feb 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Fri Jan 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Jan 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Sun Dec 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sun Nov 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Sun Nov 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Wed Sep 14 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Tue Aug 30 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Aug 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Jun 24 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Sun Jun 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Tue Apr 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Mon Feb 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Feb 23 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Feb 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- 1.1.8

* Wed Feb 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.7-alt1
- 1.1.7

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Wed Jan 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Tue Dec 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Nov 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Oct 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Oct 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Sep 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Aug 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Aug 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.99.1-alt1
- 0.99.1

* Wed Aug 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Thu Jul 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Jul 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Thu Jun 04 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0

* Wed Jun 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Tue May 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Wed Apr 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Fri Mar 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Dec 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Sep 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Jul 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Jul 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu May 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Tue Mar 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus



