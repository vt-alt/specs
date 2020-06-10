# rt-tests is taken by perl tests for RT
Name:     linux-rt-tests
Version:  1.8
Release:  alt1

Summary:  Programs that test various rt-linux features
License:  GPL-2.0-or-later
Group:    System/Kernel and hardware
# git://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git
Url:      https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/rt-tests

Source:   %name-%version.tar
BuildRequires: libnuma-devel rpm-build-python3

%description
rt-tests is a test suite, that contains programs (such as cyclictest,
hwlatdetect, hackbench) to test various Real Time Linux features.

%prep
%setup

%build
%make_build prefix=/usr

%install
%makeinstall_std prefix=/usr

rm -f %buildroot/usr/bin/hwlatdetect \
      %buildroot/usr/lib/python3/site-packages/hwlatdetect.py
install -D src/hwlatdetect/hwlatdetect.py %buildroot/usr/sbin/hwlatdetect

%files
%_bindir/cyclicdeadline
%_bindir/cyclictest
%_bindir/deadline_test
%_bindir/determine_maximum_mpps.sh
%_bindir/get_cpuinfo_mhz.sh
%_bindir/hackbench
%_bindir/pi_stress
%_bindir/pip_stress
%_bindir/pmqtest
%_bindir/ptsematest
%_bindir/queuelat
%_bindir/rt-migrate-test
%_bindir/signaltest
%_bindir/sigwaittest
%_bindir/ssdd
%_bindir/svsematest
%_sbindir/hwlatdetect
%_man8dir/*.8*
%doc COPYING MAINTAINERS README.markdown src/hwlatdetect/hwlat.txt

%changelog
* Fri Mar 27 2020 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- Update version to v1.8.

* Fri Mar 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.7.0.11.gf240656-alt1
- Update to v1.7-11-gf240656.

* Wed Dec 04 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt4
- Return of the --numa option (for rteval).

* Sun Sep 15 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt3
- Make it compile on other arches.

* Sun Sep 08 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt2
- Add hwlatdetect (required python3).

* Fri Sep 06 2019 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- First build of rt-tests.
