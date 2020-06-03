Name: strace
Version: 5.7
Release: alt1

Summary: Tracks and displays system calls associated with a running process
# The test suite is GPLv2+, all the rest is LGPLv2.1+.
License: LGPL-2.1-or-later and GPL-2.0-or-later
Group: Development/Debuggers
Url: https://strace.io

# http://git.altlinux.org/gears/s/strace.git
Source: %name-%version-%release.tar

# due to use of deprecated -k option
Conflicts: rpm-utils <= 0:0.9.11-alt1

# for -k option
BuildRequires: libdw-devel binutils-devel
# for test suite
%{?!_without_check:%{?!_disable_check:BuildRequires: /proc /dev/kvm}}

# The default is --enable-mpers=yes, but
# some architectures may need --enable-mpers=check instead.
%define mpers_check %nil
%define architectures_need_mpers_check aarch64
%ifarch %architectures_need_mpers_check
%define mpers_check --enable-mpers=check
%endif

%description
The strace program intercepts and records the system calls called and
the signals received by a running process.  strace can print a record of
each system call, its arguments and its return value.  strace is useful
for diagnosing problems and debugging, as well as for instructional
purposes.

%prep
%setup -n %name-%version-%release
echo -n %version-%release > .tarball-version
echo -n 2019 > .year
date +%%Y-%%m-%%d > .strace.1.in.date

%build
echo 'BEGIN OF BUILD ENVIRONMENT INFORMATION'
uname -a |head -1
libc="$(ldd /bin/sh |sed -n 's|^[^/]*\(/[^ ]*/libc\.so[^ ]*\).*|\1|p' |head -1)"
$libc |head -1
file -L /bin/sh
gcc --version |head -1
ld --version |head -1
kver="$(printf '%%s\n%%s\n' '#include <linux/version.h>' 'LINUX_VERSION_CODE' | gcc -E -P -)"
printf 'kernel-headers %%s.%%s.%%s\n' $(($kver/65536)) $(($kver/256%%256)) $(($kver%%256))
echo 'END OF BUILD ENVIRONMENT INFORMATION'

./bootstrap -sv
mkdir build
cd build
%define _configure_script ../configure
CFLAGS_FOR_BUILD="$RPM_OPT_FLAGS"; export CFLAGS_FOR_BUILD
%configure %mpers_check #--enable-maintainer-mode
%make_build

%install
%makeinstall_std -C build
%set_verify_elf_method strict

%check
%buildroot%_bindir/strace -V
export SLEEP_A_BIT='sleep 0.5' VERBOSE=1
%make_build -k check -C build VERBOSE=1

echo 'BEGIN OF TEST SUITE INFORMATION'
tail -n 99999 -- build/tests*/test-suite*.log build/tests*/ksysent.gen.log
find build/tests* -type f -name '*.log' -print0 |
	xargs -r0 grep -H '^KERNEL BUG:' -- ||:
echo 'END OF TEST SUITE INFORMATION'

%files
%_bindir/strace
%_bindir/strace-log-merge
%_mandir/man?/*
%doc COPYING CREDITS NEWS README README-linux-ptrace

%changelog
* Mon Jun 01 2020 Dmitry V. Levin <ldv@altlinux.org> 5.7-alt1
- v5.6 -> v5.7.

* Tue Apr 07 2020 Dmitry V. Levin <ldv@altlinux.org> 5.6-alt1
- v5.5 -> v5.6.

* Thu Feb 06 2020 Dmitry V. Levin <ldv@altlinux.org> 5.5-alt1
- v5.4-7-ga41d025fa -> v5.5.

* Tue Dec 03 2019 Dmitry V. Levin <ldv@altlinux.org> 5.4.0.7.a41d0-alt1
- v5.4 -> v5.4-7-ga41d025fa.
- Removed -utils subpackage that contained unsupported strace-graph utility.

* Thu Nov 28 2019 Dmitry V. Levin <ldv@altlinux.org> 5.4-alt1
- v5.3 -> v5.4.

* Wed Sep 25 2019 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt1
- v5.2 -> v5.3.

* Fri Jul 12 2019 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- v5.1 -> v5.2.

* Wed May 22 2019 Dmitry V. Levin <ldv@altlinux.org> 5.1-alt1
- v5.0 -> v5.1.

* Tue Mar 19 2019 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt1
- v4.26 -> v5.0.

* Wed Dec 26 2018 Dmitry V. Levin <ldv@altlinux.org> 4.26-alt1
- v4.25 -> v4.26.

* Tue Oct 30 2018 Dmitry V. Levin <ldv@altlinux.org> 4.25-alt1
- v4.24-85-g9eeab9844 -> v4.25.

* Sun Sep 16 2018 Dmitry V. Levin <ldv@altlinux.org> 4.24.0.85.9eea-alt1
- v4.24 -> v4.24-85-g9eeab9844.

* Tue Aug 14 2018 Dmitry V. Levin <ldv@altlinux.org> 4.24-alt1
- v4.23 -> v4.24.

* Thu Jun 14 2018 Dmitry V. Levin <ldv@altlinux.org> 4.23-alt1
- v4.22-55-g2e5167c -> v4.23.

* Thu Apr 12 2018 Dmitry V. Levin <ldv@altlinux.org> 4.22.0.55.2e51-alt1
- v4.22 -> v4.22-55-g2e5167c.
- Use libdw-based unwinder for stack tracing.

* Thu Apr 05 2018 Dmitry V. Levin <ldv@altlinux.org> 4.22-alt1
- v4.21 -> v4.22.

* Wed Feb 14 2018 Dmitry V. Levin <ldv@altlinux.org> 4.21-alt2
- aarch64: configure with --enable-mpers=check.

* Tue Feb 13 2018 Dmitry V. Levin <ldv@altlinux.org> 4.21-alt1
- v4.20 -> v4.21.

* Mon Nov 13 2017 Dmitry V. Levin <ldv@altlinux.org> 4.20-alt1
- v4.19 -> v4.20.

* Tue Sep 05 2017 Dmitry V. Levin <ldv@altlinux.org> 4.19-alt1
- v4.18-252-g23941 -> v4.19.

* Wed Aug 16 2017 Dmitry V. Levin <ldv@altlinux.org> 4.18.0.252.23941-alt1
- v4.18-134-g805d6ea -> v4.18-252-g23941.

* Thu Jul 27 2017 Dmitry V. Levin <ldv@altlinux.org> 4.18.0.134.805d-alt1
- v4.18 -> v4.18-134-g805d6ea.

* Wed Jul 05 2017 Dmitry V. Levin <ldv@altlinux.org> 4.18-alt1
- v4.17 -> v4.18.

* Wed May 24 2017 Dmitry V. Levin <ldv@altlinux.org> 4.17-alt1
- v4.16-121-g87607b9 -> v4.17.

* Fri Apr 14 2017 Dmitry V. Levin <ldv@altlinux.org> 4.16.0.121.8760-alt1
- v4.16-63-g722c73a -> v4.16-121-g87607b9.

* Sun Mar 19 2017 Dmitry V. Levin <ldv@altlinux.org> 4.16.0.63.722c-alt1
- v4.16 -> v4.16-63-g722c73a.

* Tue Feb 14 2017 Dmitry V. Levin <ldv@altlinux.org> 4.16-alt1
- v4.15-343-g8663bfb -> v4.16.

* Wed Feb 08 2017 Dmitry V. Levin <ldv@altlinux.org> 4.15.0.343.8663b-alt1
- v4.15-237-gf73c5cf -> v4.15-343-g8663bfb.

* Thu Dec 29 2016 Dmitry V. Levin <ldv@altlinux.org> 4.15.0.237.f73c-alt1
- v4.15 -> v4.15-237-gf73c5cf.

* Tue Dec 13 2016 Dmitry V. Levin <ldv@altlinux.org> 4.15-alt1
- v4.14-214-gab28d7f -> v4.15.

* Wed Dec 07 2016 Dmitry V. Levin <ldv@altlinux.org> 4.14.0.214.ab28-alt1
- v4.14-100-g622af42 -> v4.14-214-gab28d7f.

* Wed Nov 16 2016 Dmitry V. Levin <ldv@altlinux.org> 4.14.0.100.622a-alt1
- v4.14 -> v4.14-100-g622af42.

* Tue Oct 04 2016 Dmitry V. Levin <ldv@altlinux.org> 4.14-alt1
- v4.13-110-ge31e2c0 -> v4.14.

* Wed Aug 31 2016 Dmitry V. Levin <ldv@altlinux.org> 4.13.0.110.e31e-alt1
- v4.13-81-g6fc5338 -> v4.13-110-ge31e2c0.

* Wed Aug 24 2016 Dmitry V. Levin <ldv@altlinux.org> 4.13.0.81.6fc5-alt1
- v4.13 -> v4.13-81-g6fc5338.

* Tue Jul 26 2016 Dmitry V. Levin <ldv@altlinux.org> 4.13-alt1
- v4.12-167-g3b6bc9b -> v4.13.

* Wed Jul 20 2016 Dmitry V. Levin <ldv@altlinux.org> 4.12.0.167.3b6b-alt1
- v4.12-139-g64a8a4c -> v4.12-167-g3b6bc9b.

* Thu Jul 14 2016 Dmitry V. Levin <ldv@altlinux.org> 4.12.0.139.64a8-alt1
- v4.12-110-gbf2698a -> v4.12-139-g64a8a4c.

* Sun Jul 03 2016 Dmitry V. Levin <ldv@altlinux.org> 4.12.0.110.bf26-alt1
- v4.12 -> v4.12-110-gbf2698a.

* Tue May 31 2016 Dmitry V. Levin <ldv@altlinux.org> 4.12-alt1
- v4.11-735-g0cf24d9 -> v4.12.

* Tue May 24 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.735.0cf2-alt1
- v4.11-684-gff2b853 -> v4.11-735-g0cf24d9.

* Wed May 18 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.684.ff2b-alt1
- v4.11-641-gc0db59b -> v4.11-684-gff2b853.

* Sat May 14 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.641.c0db-alt1
- v4.11-567-g1e9c966 -> v4.11-641-gc0db59b.

* Fri Apr 29 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.567.1e9c-alt1
- v4.11-515-g67c2f67 -> v4.11-567-g1e9c966.

* Tue Apr 26 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.515.67c2-alt1
- v4.11-373-g9c1a72c -> v4.11-515-g67c2f67.

* Sat Apr 16 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.373.9c1a-alt2
- v4.11-350-g5b2d257 -> v4.11-373-g9c1a72c.

* Wed Apr 06 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.350.5b2d-alt1
- v4.11-272-g0cb245a -> v4.11-350-g5b2d257.

* Sun Feb 21 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.272.0cb2-alt1
- v4.11-257-g669f8cf -> v4.11-272-g0cb245a.

* Sun Feb 14 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.257.669f-alt1
- v4.11-209-g7469e25 -> v4.11-257-g669f8cf.

* Fri Feb 05 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.209.7469e-alt1
- v4.11-183-gfa8c286 -> v4.11-209-g7469e25.

* Fri Jan 22 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.183.fa8c-alt1
- v4.11-163-g972018f -> v4.11-183-gfa8c286.

* Fri Jan 15 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.163.9720-alt1
- v4.11-123-g1eabdb3 -> v4.11-163-g972018f.

* Thu Jan 07 2016 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.123.1eabd-alt1
- v4.11-16-gaef5e14 -> v4.11-123-g1eabdb3.

* Tue Dec 29 2015 Dmitry V. Levin <ldv@altlinux.org> 4.11.0.16.595a0-alt1
- Updated to v4.11-16-gaef5e14.

* Wed Dec 23 2015 Dmitry V. Levin <ldv@altlinux.org> 4.11-alt2
- Enabled experimental -k option for x86 and x86_64.

* Mon Dec 21 2015 Dmitry V. Levin <ldv@altlinux.org> 4.11-alt1
- Updated to v4.11.

* Sun Dec 20 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.583.7405-alt1
- Updated to v4.10-583-g7405b12.

* Thu Dec 10 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.566.bab4e-alt1
- Updated to v4.10-566-gbab4ef4.

* Thu Nov 26 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.484.bb74-alt1
- Updated to v4.10-484-gbb746ff.

* Sat Sep 19 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.421.3b731-alt1
- Updated to v4.10-421-g3b73194.

* Fri Aug 28 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.363.e2a33-alt1
- Updated to v4.10-363-ge2a3370.

* Thu Aug 20 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.325.d8ef-alt1
- Updated to v4.10-325-gd8ef5e7.

* Tue Aug 04 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.301.30ac0-alt1
- Updated to v4.10-301-g30ac062.

* Sun Aug 02 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.292.baaa4-alt1
- Updated to v4.10-292-gbaaa41c.

* Thu Jul 30 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.277.d9fb-alt1
- Updated to v4.10-277-gd9fb450.

* Thu Jul 23 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.258.f8b49-alt1
- Updated to v4.10-258-gf8b4913.

* Tue Jun 30 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.95.4b80f-alt1
- Updated to v4.10-95-g4b80f34.

* Fri May 22 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.74.8c20-alt1
- Updated to v4.10-74-g8c20d89.

* Tue Mar 31 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10.0.58.87af-alt1
- Updated to v4.10-58-g87af193.

* Fri Mar 06 2015 Dmitry V. Levin <ldv@altlinux.org> 4.10-alt1
- Updated to v4.10.

* Wed Mar 04 2015 Dmitry V. Levin <ldv@altlinux.org> 4.9.0.377.6a63-alt1
- Updated to v4.9-377-g6a63bfa.

* Sun Feb 22 2015 Dmitry V. Levin <ldv@altlinux.org> 4.9.0.314.5b081-alt1
- Updated to v4.9-314-g5b0819e.

* Mon Jan 26 2015 Dmitry V. Levin <ldv@altlinux.org> 4.9.0.241.73e9-alt1
- Updated to v4.9-241-g73e9880.

* Thu Jan 22 2015 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt8
- Updated to v4.9-222-gdf7aa2b.

* Tue Jan 13 2015 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt7
- Updated to v4.9-196-ged7ada2.

* Thu Jan 08 2015 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt6
- Updated to v4.9-153-g9e6a7bf.

* Tue Dec 30 2014 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt5
- Updated to v4.9-135-ge00a957.

* Fri Nov 28 2014 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt4
- Updated to v4.9-44-gf548067.

* Tue Nov 11 2014 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt3
- Updated to v4.9-38-gfafc71f.

* Thu Sep 18 2014 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt2
- Updated to v4.9-10-g2f6510c.

* Fri Aug 15 2014 Dmitry V. Levin <ldv@altlinux.org> 4.9-alt1
- Updated to v4.9.

* Wed Jun 04 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt10
- Updated to v4.8-208-gd04bb2b.

* Fri May 30 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt9
- Updated to v4.8-201-g9682107.

* Thu Apr 17 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt8
- Updated to v4.8-161-ge51ce47.

* Thu Mar 20 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt7
- Updated to v4.8-148-g0160e16.

* Tue Mar 04 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt6
- Updated to v4.8-140-g7a28f7f.

* Fri Feb 07 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt5
- Updated to v4.8-128-gb0c2a9d.

* Fri Feb 07 2014 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt4
- Updated to v4.8-124-g900ec1b.

* Tue Nov 19 2013 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt3
- Updated to v4.8-95-g5b35147.

* Thu Jun 20 2013 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt2
- Updated to v4.8-16-gfdfa47a.

* Mon Jun 03 2013 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt1
- Updated to v4.8.

* Wed May 15 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt20
- Updated to v4.7-226-g1d2435b.

* Sun May 05 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt19
- Updated to v4.7-190-g2f99788.

* Tue Apr 30 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt18
- Updated to v4.7-163-g149d7de.

* Wed Mar 27 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt17
- Updated to v4.7-159-gb6593de.

* Mon Mar 18 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt16
- Updated to v4.7-150-gb787b10.

* Fri Mar 15 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt15
- Updated to v4.7-142-g3ec134b.

* Tue Mar 05 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt14
- Updated to v4.7-136-gdafba9b.

* Sat Mar 02 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt13
- Updated to v4.7-126-g1694092.

* Sat Feb 09 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt12
- Updated to v4.7-58-g338c069.

* Wed Feb 06 2013 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt11
- Updated to v4.7-47-g88eafd8.

* Sat Dec 08 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt10
- Updated to v4.7-35-g1f21513.

* Sun Oct 28 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt8
- Updated to v4.7-29-g17e3860.

* Fri Sep 28 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt7
- Updated to v4.7-24-g85c2178.

* Fri Aug 24 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt6
- Updated to v4.7-19-g508279c.

* Fri Aug 17 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt5
- Updated to v4.7-17-gad232c6.

* Fri Jul 13 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt4
- Updated to v4.7-16-gcf53436.

* Tue Jul 10 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt3
- Updated to v4.7-15-g26bc060.

* Tue May 15 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt2
- Updated to v4.7-7-gd376c92.

* Wed May 02 2012 Dmitry V. Levin <ldv@altlinux.org> 4.7-alt1
- Updated to v4.7.

* Tue May 01 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt14
- Updated to v4.6-398-ga5fd66b.

* Thu Apr 19 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt13
- Updated to v4.6-382-gebee04c.

* Sun Apr 08 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt12
- Updated to v4.6-373-g0cbed35.

* Mon Mar 26 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt11
- Updated to v4.6-369-g4372cc9.

* Mon Mar 26 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt10
- Updated to v4.6-364-g378f9c5.

* Fri Mar 16 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt9
- Updated to v4.6-318-g4a0ffea.

* Mon Mar 12 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt8
- Updated to v4.6-285-g328bf25.

* Wed Feb 08 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt7
- Updated to v4.6-228-gbdec9cb.

* Wed Jan 18 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt6
- Updated to v4.6-193-g7d55801.

* Sun Jan 08 2012 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt5
- Updated to v4.6-182-gf1e6903.

* Tue Oct 11 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt4
- Updated to v4.6-148-gd99e48c.

* Sat Jun 25 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt3
- Updated to v4.6-60-g9015cd9.

* Fri Apr 08 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt2
- Updated to v4.6-2-g8a08277 (adds new strace options: -y and -P).

* Tue Mar 15 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt1
- Updated to v4.6.

* Mon Mar 14 2011 Dmitry V. Levin <ldv@altlinux.org> 4.6-alt0.1
- Updated to v4.5.20-109-g50e69cb.

* Sun Mar 06 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt10
- Updated to v4.5.20-102-g6c0e2fc.

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt9
- Updated to v4.5.20-89-ga6ca968.

* Thu Feb 17 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt8
- Updated to v4.5.20-64-g65c1a81.
- Built with libaio-devel for better decoding of io_* syscalls.

* Mon Jan 31 2011 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt7
- Updated to v4.5.20-61-g50a218d.

* Tue Dec 07 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt6
- Updated to v4.5.20-42-g8044bc1 (closes: #24705).

* Fri Dec 03 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt5
- Updated to v4.5.20-41-gbdafa1a.

* Fri Sep 17 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt4
- Updated to v4.5.20-33-gdcd3a6f.

* Sun Aug 29 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt3
- Packaged strace-utils subpackage as noarch.

* Sun Aug 29 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt2
- Updated to v4.5.20-17-g21b8db4.

* Wed Apr 14 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.20-alt1
- Updated to v4.5.20 release.

* Wed Apr 07 2010 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt3
- Updated to v4.5.19-37-gae4db5e.

* Fri Nov 06 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt2
- Updated to v4.5.19-8-g9906e6d.

* Wed Oct 21 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt1
- Updated to v4.5.19 release.

* Sat Oct 10 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt0.2
- Updated to v4.5.18-137-g76ac37d from
  git://strace.git.sourceforge.net/gitroot/strace/strace

* Sat Sep 19 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.19-alt0.1
- Updated to v4.5.18-111-gfbfed22 from
  git://strace.git.sourceforge.net/gitroot/strace/strace

* Thu Sep 03 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt8
- Updated to v4.5.18-102-g99c8569 from
  git://strace.git.sourceforge.net/gitroot/strace/strace

* Tue Jul 07 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt7
- Updated to v4.5.18-96-geb9e2e8 from
  git://strace.git.sourceforge.net/gitroot/strace

* Mon Jun 01 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt6
- Updated to cvs snapshot 20090601.

* Fri Jan 02 2009 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt5
- Updated to cvs snapshot 20090101.

* Mon Nov 10 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt4
- sock_ioctl: Parse more SIOCS* ioctls.
- Fixed several corner cases in printpathn() and printstr().
- Updated capability flags and prctl values from linux-2.6.27.

* Thu Oct 23 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt3
- Implemented parsers for socket type flags introduced in linux 2.6.27.
- Implemented parsers for new syscalls introduced in linux 2.6.27.

* Mon Sep 29 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt2
- strace: exit/kill with traced child's exitcode/signal.
  This change makes -k option obsolete.

* Sat Aug 30 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.18-alt1
- Updated to cvs snapshot 20080828.

* Thu Jul 24 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.17-alt2
- Fix -F option backwards compatibility.

* Wed Jul 23 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.17-alt1
- Updated to cvs snapshot 20080722.

* Sat Apr 19 2008 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt5
- Updated to cvs snapshot 20080326 with tcb changes reverted.
- Implemented timeout decoders for interrupted syscalls.
- Fixed and enabled prctl decoder.
- Updated errnoent.h
- Applied several fixes submitted to strace-devel.

* Sun Oct 14 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt4
- Updated to cvs snapshot 20071014.

* Mon Sep 24 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt3
- net.c (printsock): Output AF_UNIX socket address using
  printstr() to avoid unprintable characters in output.
- stream.c (decode_poll): Rearrange parser to decode input and
  output parameters separately.
- Reworked struct timespec decoders for better multiarch support.
- desc.c (sys_pselect6): Decode signal mask when entering syscall.

* Sat Sep 22 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt2
- Updated to cvs snapshot 20070712.
- Reverted attach/detach changes from Jan Kratochvil for a while
  because they introduced too many regressions.

* Mon Aug 06 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.16-alt1
- Updated to 4.5.16 release.

* Mon Jul 16 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.15-alt4
- Updated to cvs snapshot 20070711.

* Fri Mar 30 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.15-alt3
- Added linux SG_IO ioctl parser, based on patch from Vladimir Nadvornik.
- Add MAP_32BIT support, based on patch from Kirill A. Shutemov.

* Tue Jan 16 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.15-alt2
- Updated to cvs snapshot 20070113:
  Enhanced mount parser (ldv).

* Sat Jan 13 2007 Dmitry V. Levin <ldv@altlinux.org> 4.5.15-alt1
- Updated to cvs snapshot 20070113:
  Fixed adjtimex modes parser (ldv);
  Enhanced umount parser (ldv);
  Fixed open(2) flags parser (ldv, RH#222385);
  Bumped version to 4.5.15 (roland).
- Enhanced sock_ioctl parser (ldv).

* Thu Dec 21 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt8
- Further biarch fixes for counts and internal syscalls.

* Sat Dec 16 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt7
- Updated to cvs snapshot 20061213:
  Fixed -ff -o behaviour (ldv, RH#218435);
  Enhanced fix for piping trace output (ldv, RH#204950);
  Fixed biarch for readv/writev (jj, RH#218433);
  Fixed biarch for time related functions (ldv, RH#171626, RH#173050);
  Enhanced adjtimex parser (ldv).
- Enhanced mount and umount parsers (ldv).
- Fixed biarch for -c (ldv, RH#192193)
- Fixed biarch for internal syscalls (ldv, RH#179740).

* Mon Dec 04 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt6
- Updated to cvs snapshot 20061204:
  Fix build against 2.6.18+ headers (jj).

* Tue Oct 17 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt5
- Updated to cvs snapshot 20061016:
  Merge fixes made in 4.5.14-alt{2..4};
  Merge my enhanced quotactl parser.

* Fri Oct 06 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt4
- Fixed build with new glibc headers.

* Fri Sep 01 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt3
- Updated to cvs snapshot 20060822.
- Fixed memory corruption bug in print_xattr_val() (ldv, RH#200621).
- Fixed handling of untraced processes in trace() (ldv, RH#204950).
- Added hooks for new syscalls in 2.6.1[67] kernels,
  added decoders for *at, inotify*, pselect6, ppoll and unshare
  syscalls (RH#178633).

* Wed Mar 29 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt2
- Fixed race condition in tcb allocation code.

* Tue Jan 17 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.14-alt1
- Updated to 4.5.14.

* Fri Jan 13 2006 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt5
- Updated to cvs snapshot 20060112.
- Merged upstream patches:
  alt-mount (RH#165377)
  owl-man (RH#165375)
  drepper-x86_64-ipc (RH#164755)
  drepper-msgrcv (RH#164757)
  alt-qual_syscall (RH#174798)
  alt-qual_flags (RH#173986)

* Thu Nov 17 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt4
- Implemented qual_flags support for each personality.

* Tue Nov 15 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt3
- Implemented numeric syscall qualifier specification handling.

* Sat Oct 22 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt2
- Updated to cvs snapshot 20051021, to fix for potential
  buffer overflow in printpathn().

* Mon Aug 08 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.13-alt1
- Updated to 4.5.13.
- Applied few ipc patches from Ulrich Drepper.
- Rediffed patches.

* Thu Aug 04 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt4
- Updated to cvs snapshot 20050719.
- Merged upstream patches:
  alt-TF (RH#159340)
  alt-TD (RH#159400)

* Sat Jul 16 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt3
- Corrected mount(2) deparser (RH#165377).

* Sat Jun 18 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt2
- Rewritten quotactl(2) deparser (RH#118696).

* Fri Jun 10 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.12-alt1
- Updated to 4.5.12.
- Merged upstream patches:
  alt-static (RH#159688).
- Rediffed other patches.

* Sat Jun 04 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt6
- Updated to cvs snapshot 20050607.
- Merged upstream patches:
  alt-linkage (RH#158488)
  alt-mem-fixes (RH#159196)
  alt-oom (RH#159308)
  alt-printflags (RH#159310)
- Minor namespace cleanup (RH#159688).
- Rediffed other patches.

* Wed Jun 01 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt5
- Removed TRACE_FILE flag from those syscalls
  which have no filename argument (RH#159340).
- Introduced "-e trace=desc" (RH#159400).

* Mon May 30 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt4
- Fixed several MM issues (RH#159196).
- Unitized OOM errors reporting (RH#159308).
- Enhanced printflags() semantics (RH#159310).

* Sun May 29 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt3
- Updated to cvs snapshot 20050526.

* Sun May 22 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt2
- Updated to cvs snapshot 20050509.
- Fixed to build with default kernel headers.

* Thu Mar 24 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.11-alt1
- Updated to 4.5.11.

* Tue Mar 15 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.10-alt1
- Updated to 4.5.10.

* Thu Feb 24 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.9-alt2
- Updated to cvs snapshot 20050204.
- Merged upstream patches:
  alt-fake_execve (RH#143365)

* Sat Feb 05 2005 Dmitry V. Levin <ldv@altlinux.org> 4.5.9-alt1
- Updated to 4.5.9.
- Merged upstream patches:
  alt-qual (RH#143362)
  alt-call_summary (RH#143369)
  alt-gnu_source (RH#143370)

* Mon Dec 20 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.8-alt2
- Fixed multiply qualifying expression bugs.
- Fixed "strace -i" misbehaviour.
- Fixed segfault in "strace -c".
- Fixed GNU_SOURCE handling.

* Mon Oct 25 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.8-alt1
- Updated to 4.5.8.
- Merged upstream patches:
  alt-ioctl-scsi (RH#129808)
  rh-printmsghdr-scm (RH#131689)
  alt-ioctl-rtc (RH#58606)

* Mon Sep 13 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.7-alt3
- Improved rtc ioctls handling.

* Mon Sep 13 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.7-alt2
- Added SCSI ioctl names.
- Improved sendmsg/recvmsg handling.

* Tue Aug 31 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.7-alt1
- Updated to 4.5.7.
- Merged upstream patches:
  alt-parse_sigset (RH#128091)

* Sat Jul 17 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.6-alt1
- Updated to 4.5.6.

* Mon Jul 12 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.5-alt2
- Fixed signal parser.

* Wed Jun 30 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.5-alt1
- Updated to 4.5.5.

* Fri Jun 04 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.4-alt1
- Updated to 4.5.4.
- Merged upstream patches:
  alt-linux-ioctlent (RH#122257)

* Sun May 02 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt2
- Added more ioctl names.
- Regenerated ioctl list from linux-2.6.5.

* Sun Apr 18 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.3-alt1
- Updated to 4.5.3.
- Merged upstream patches:
  alt-quotactl-fix (RH#118694)

* Thu Mar 18 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.2-alt2
- Fixed output of the quotactl command parser.

* Thu Mar 04 2004 Dmitry V. Levin <ldv@altlinux.org> 4.5.2-alt1
- Updated to 4.5.2.
- Merged upstream patches:
  alt-trace-coredump (RH#112117)

* Mon Dec 15 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5.1-alt1
- Updated to 4.5.1.
- Merged upstream patches:
  owl-ioctl (RH#105358)
  alt-output (except line buffering for piped output)
  alt-ugid32_syscalls (RH#105359)
- Rediffed:
  owl-alt-fixes
  owl-man
  alt-pipe-setlinebuf
  alt-trace-coredump
  alt-keep_status

* Tue Oct 21 2003 Dmitry V. Levin <ldv@altlinux.org> 4.5-alt1
- Updated to 4.5.

* Sat Sep 06 2003 Dmitry V. Levin <ldv@altlinux.org> 4.4.99-alt1
- Updated to 4.4.99.
- Reviewed patches:
  + merged upstream or obsolete:
    all RH patches.
  + reworked:
    owl-alt-fixes
    owl-man
    owl-ioctl
    alt-output
    alt-keep_status
    alt-ugid32_syscalls
- Updated build dependencies.

* Fri Sep 05 2003 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt6
- Corrected strace behaviour in case of piped output redirection.

* Sun Nov 24 2002 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt5
- Fixed kernel-2.4.x specific uid32 syscalls handling.

* Wed Oct 30 2002 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt4
- Reverted signal.c back to revision 1.31 (as in strace-4.4);
  this should fix strace hangups (#0001326).
- Merged RH patches (4.4-8):
  + fixed modify_ldt handling;
  + added/fixed handing for the following syscalls:
    getpmsg, putpmsg, lchown32, getuid32, readahead, sendfile64,
    setxattr, fsetxattr, getxattr, fgetxattr, listxattr, flistxattr,
    removexattr, fremovexattr, sched_setaffinity, sched_getaffinity,
    futex, set_thread_area, get_thread_area;
  + added SA_RESTORER handling.

* Tue Jun 11 2002 Dmitry V. Levin <ldv@altlinux.org> 4.4-alt3
- Updated to current CVS version (post-4.4) with an additional fix for
  displaying all possible ioctl names when there's more than one match,
  some build fixes, and a RH-derived patch for detaches from
  multi-threaded programs (Owl).
- Changed group tag to "Development/Debuggers".

* Thu May 23 2002 Stanislav Ievlev <inger@altlinux.ru> 4.4-alt2
- Added subpackage to remove deps on perl-base in main package.

* Thu Aug 30 2001 Dmitry V. Levin <ldv@altlinux.ru> 4.4-alt1
- 4.4

* Tue Oct 24 2000 Dmitry V. Levin <ldv@fandra.org> 4.2-ipl3mdk
- Enabled all LFS patches and rebuilt with LFS-aware kernel-headers.

* Tue Oct 17 2000 Dmitry V. Levin <ldv@fandra.org> 4.2-ipl2mdk
- Added fcntl64 patch.

* Tue Oct 03 2000 Dmitry V. Levin <ldv@fandra.org> 4.2-ipl1mdk
- Merged in RH patches.
- Added keep_status feature.

* Tue Mar 28 2000 Dmitry V. Levin <ldv@fandra.org>
- 4.2

* Sat Nov 27 1999 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions

* Fri Nov 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 4.1.

* Mon Nov 08 1999 John Buswell <johnb@mandrakesoft.com>
- Commented out KERN_SECURELVL from system.c (this is not in sysctl.h in
  2.2.13 kernel)
- Build Release

* Mon Jul 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 4.00.

* Wed Apr 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update to 3.99.

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binary

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 16)

* Tue Feb  9 1999 Jeff Johnson <jbj@redhat.com>
- vfork est arrive!

* Tue Feb  9 1999 Christopher Blizzard <blizzard@redhat.com>
- Add patch to follow clone() syscalls, too.

* Sun Jan 17 1999 Jeff Johnson <jbj@redhat.com>
- patch to build alpha/sparc with glibc 2.1.

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- patch to build on ARM

* Wed Sep 30 1998 Jeff Johnson <jbj@redhat.com>
- fix typo (printf, not tprintf).

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- fix compile problem on sparc.

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot

* Mon Jul 20 1998 Cristian Gafton <gafton@redhat.com>
- added the umoven patch from James Youngman <jay@gnu.org>
- fixed build problems on newer glibc releases

* Mon Jun 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
