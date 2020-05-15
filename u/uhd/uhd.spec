# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

# NEON support is by default disabled on ARMs
# building with --with=neon will enable auto detection
%def_with neon

%ifarch %arm aarch64
%if ! %{with neon}
%global have_neon -DHAVE_ARM_NEON_H=0
%endif
%endif

Name: uhd
Url: https://github.com/EttusResearch/uhd
Version: 3.15.0.0
Release: alt1
License: GPLv3+
Group: Engineering
Summary: Universal Hardware Driver for Ettus Research products
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: %name-limits.conf
# Download command firmware:
# uhd_images_downloader --types "(fpga|fw)_default" -i images
Source2: images.tar

Patch: uhd-0.14.1.1-python3-fix.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: ctest cmake
BuildRequires: boost-interprocess-devel gcc-c++ boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-program_options-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-polygon-devel boost-program_options-devel boost-python3-devel boost-signals-devel boost-wave-devel libusb-devel libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel libgps-devel libudev-devel
BuildRequires: libnumpy-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-Cheetah
BuildRequires: python3-module-docutils doxygen libpcap-devel
BuildRequires: python3-module-mako
Requires(pre): shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils
Requires: tkinter

%description
The UHD is the universal hardware driver for Ettus Research products.
The goal of the UHD is to provide a host driver and API for current and
future Ettus Research products. It can be used standalone without GNU Radio.

%package firmware
Group: Engineering
Summary: Firmware files for UHD
Requires: %name = %EVR
BuildArch: noarch

%description firmware
Firmware files for the Universal Hardware driver (UHD).

%package devel
Group: Development/Other
Summary: Development files for UHD
Requires: %name = %EVR

%description devel
Development files for the Universal Hardware Driver (UHD).

%package doc
Group: Documentation
Summary: Documentation files for UHD
BuildArch: noarch

%description doc
Documentation for the Universal Hardware Driver (UHD).

%package tools
Group: Engineering
Summary: Tools for working with / debugging USRP device
Requires: %name = %EVR

%description tools
Tools that are useful for working with and/or debugging USRP device.

%package -n python3-module-%name
Group: Development/Python3
Summary: Python 3 API for %name
Requires: %name = %EVR

%description -n python3-module-%name
Python 3 API for %name

%prep
%setup
sed -i 's|/usr/bin/env python|%__python3|' host/python/setup.py.in

%patch -p1

# fix python shebangs
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%__python3|' {} \;

%build
pushd host
%cmake %{?have_neon} \
        -DENABLE_GPSD=ON \
        -DENABLE_E300=ON \
        -DENABLE_PYTHON3=ON \
        -DENABLE_PYTHON_API=ON
%cmake_build
popd

# tools
pushd tools/uhd_dump
%make_build
popd

%check
pushd host/BUILD
%make_build test
popd

%install
pushd host
%cmakeinstall_std
popd

# Fix udev rules and use dynamic ACL management for device
%__subst 's/BUS==/SUBSYSTEM==/;s/SYSFS{/ATTRS{/;s/MODE:="0666"/MODE:="0660", ENV{ID_SOFTWARE_RADIO}="1"/' %buildroot%_libdir/uhd/utils/uhd-usrp.rules
mkdir -p %buildroot%_udevrulesdir
mv %buildroot%_libdir/uhd/utils/uhd-usrp.rules %buildroot%_udevrulesdir/10-usrp-uhd.rules

# Remove tests, examples binaries
rm -rf %buildroot%_libdir/uhd/{tests,examples}

# Move the utils stuff to libexec dir
mkdir -p %buildroot%_libexecdir/uhd
mv %buildroot%_libdir/uhd/utils/* %buildroot%_libexecdir/uhd

# Package base docs to base package
mkdir _tmpdoc
mv %buildroot%_docdir/%name/{LICENSE,README.md} _tmpdoc

install -m 644 -D %SOURCE1 %buildroot%_sysconfdir/security/limits.d/99-usrp.conf

# firmware
tar -xf %SOURCE2 -C %buildroot%_datadir/uhd/

# remove win stuff
rm -rf %buildroot%_datadir/uhd/images/winusb_driver

# convert hardlinks to symlinks (to not package the file twice)
pushd %buildroot%_bindir
for f in uhd_images_downloader usrp2_card_burner
do
  unlink $f
  ln -s ../..%_libexecdir/uhd/${f}.py $f
done
popd

# tools
install -Dpm 0755 tools/usrp_x3xx_fpga_jtag_programmer.sh %buildroot%_bindir/usrp_x3xx_fpga_jtag_programmer.sh
install -Dpm 0755 tools/uhd_dump/chdr_log %buildroot%_bindir/chdr_log

%files
%exclude %_docdir/%name/doxygen
%exclude %_datadir/uhd/images
%doc _tmpdoc/*
%_bindir/*
%exclude %_bindir/usrp_x3xx_fpga_jtag_programmer.sh
%exclude %_bindir/chdr_log
%_udevrulesdir/10-usrp-uhd.rules
%config(noreplace) %_sysconfdir/security/limits.d/*.conf
%_libdir/lib*.so.*
%_libexecdir/uhd
%_man1dir/*.1*
%_datadir/uhd

%files firmware
%_datadir/uhd/images

%files devel
%_includedir/*
%_libdir/lib*.so
%dir %_libdir/cmake/uhd
%_libdir/cmake/uhd/*.cmake
%_pkgconfigdir/*.pc

%files doc
%doc %_docdir/%name/doxygen

%files tools
%doc tools/README.md
%_bindir/usrp_x3xx_fpga_jtag_programmer.sh
%_bindir/chdr_log

%files -n python3-module-%name
%python3_sitelibdir/%name/

%changelog
* Sat Jan 11 2020 Anton Midyukov <antohami@altlinux.org> 3.15.0.0-alt1
- New version 3.15.0.0

* Wed Dec 25 2019 Anton Midyukov <antohami@altlinux.org> 3.14.1.1-alt3
- fix python3 shebang and syntax for utils
- fix Group

* Tue Dec 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 3.14.1.1-alt2
- Fixed shebang for installed scripts.
- Rebuilt with boost-1.71.0.

* Sat Oct 19 2019 Anton Midyukov <antohami@altlinux.org> 3.14.1.1-alt1.1
- fix shebang for setup.py

* Thu Oct 17 2019 Anton Midyukov <antohami@altlinux.org> 3.14.1.1-alt1
- New version 3.14.1.1
- fix Url
- switch to python 3 (thanks Aleksey Borisenkov)

* Sat Sep 21 2019 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt5
- add BuildRequires: python-module-setuptools (Fix FTBFS)

* Tue Apr 09 2019 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt4
- update buildrequires

* Sun Jan 20 2019 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt3
- rebuild with new wireshark-devel (fix FTBFS)

* Tue Jan 01 2019 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt2
- Update firmaware (Closes: 35831)
- Enable Python API

* Sat Dec 29 2018 Anton Midyukov <antohami@altlinux.org> 3.13.0.2-alt1
- New version 3.13.0.2

* Fri Aug 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.0.0-alt5
- NMU: updated build dependencies.

* Thu Aug 09 2018 Anton Farygin <rider@altlinux.ru> 3.11.0.0-alt4
- build for aarch64

* Wed Jun 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.0.0-alt3
- NMU: rebuilt with boost-1.67.0.

* Fri Mar 30 2018 Anton Midyukov <antohami@altlinux.org> 3.11.0.0-alt2
- Fix buildrequires

* Sun Mar 18 2018 Anton Midyukov <antohami@altlinux.org> 3.11.0.0-alt1
- new version 3.11.0.0

* Sun Oct 22 2017 Anton Midyukov <antohami@altlinux.org> 3.10.2.0-alt1
- Initial build ALT Sisyphus.
