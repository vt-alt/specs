Name: rpminstall-tests
Version: 1.1.3
Release: alt7

Summary: Tests for rpm: how it interprets packages when installing

BuildRequires(pre): rpm-build-licenses
License: %gpl2plus
Group: Development/Tools
Url: http://git.altlinux.org/people/imz/packages/rpminstall-tests.git

BuildArch: noarch

%global REQS make tmpdir.sh rpm-build rpm
Requires: %REQS
# For %%check, whcih is called %%build in this pkg because of the e2k Girar:
BuildRequires: %REQS

Source: %name-%version.tar

%description
Tests for rpm: how it interprets packages when installing.

Now, it tests how various forms of constraints (Requires, Conflicts, Obsoletes)
are interpreted when they are installed together with packages with
various forms of matching Provides.

More tests can appear.

%package checkinstall
Summary: Immediately run %name when installing this package
Group: Other
Requires(pre): %name

%description checkinstall
Immediately run %name when installing this package.

They test rpm (applied to the results of rpm-build).

%package archcompat-checkinstall
Summary: Immediately run arch_compat %name when installing this package
Group: Other
Requires(pre): %name

%description archcompat-checkinstall
Immediately run a few arch_compat RPM tests when installing this package.

They test rpm -i, applied to the results of rpmbuild, which is used
to build packages without explicitly specifying the architecture, so
that their architecture is derived automatically based on `uname -m`.

%package archcompat-with-proc-checkinstall
Summary: Immediately run arch_compat %name when installing this package (with /proc)
Group: Other
Requires(pre): /proc
# to be sure:
Requires: /proc
Requires(pre): %name

%description archcompat-with-proc-checkinstall
Immediately run a few arch_compat RPM tests when installing this package
(with /proc).

They test rpm -i, applied to the results of rpmbuild, which is used
to build packages without explicitly specifying the architecture, so
that their architecture is derived automatically based on `uname -m`.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name
install -m0644 Makefile HELPER *.mk -t %buildroot%_datadir/%name/
install -m0755 makeme.sh -t %buildroot%_datadir/%name/

# Normally, this would be %%check,
# but it's convenient for me to do this check also in the e2k Girar,
# where --without check is enabled. Turn this back into %%check in future.
%build
# We don't use %%make_build to pass the usual parallelism flags
# to avoid parallelism with possible nasty races
# (until a good implementation is in place in our makefiles):
%global _makeme ./makeme.sh

%define simple_test \
echo 'Simple test (to fail fast):'\
%_makeme %{?opts} TESTS=dummy_installable\
%_makeme %{?opts} clean\
%nil

%define archcompat_test \
echo 'Simple arch_compat tests (between `uname -m`, rpmbuild, and rpm -i):'\
echo 'diagnostics'\
uname -a ||:\
cat /proc/cpuinfo ||:\
LD_SHOW_AUXV=1 /bin/echo ||:\
cat %_sysconfdir/rpm/platform ||:\
rpm --eval %%_host_cpu ||:\
rpm --eval %%_arch ||:\
\
system_arch="$(rpm -q rpm --qf='%%{ARCH}')"\
echo "...with a package built for the system rpm's arch ($system_arch):"\
%_makeme %{?opts} TESTS=dummy_installable minimal_arch= TESTS_TARGET="$system_arch"\
%_makeme %{?opts} clean\
\
default_arch="$(rpmbuild --eval %%_arch ||:)"\
echo "...with a package built for the machine's default arch ($default_arch):"\
%_makeme %{?opts} TESTS=dummy_installable minimal_arch= ||\
    case "$default_arch" in\
        arm*)\
            echo 'ARM arch detection is not ideal in rpm-build;'\
            echo 'IGNORING THE FAILURE until better times.'\
            ;;\
        *)\
            false\
            ;;\
    esac\
%_makeme %{?opts} clean\
%nil

%define all_tests \
echo 'Main tests:'\
%_makeme %{?opts}\
echo 'Now test also with "Epoch: 0" instead of no Epoch:'\
%_makeme %{?opts} clean\
%_makeme %{?opts} minimal_epoch=0\
%nil

%simple_test
%archcompat_test
%all_tests

%files
%_datadir/%name

# Set this value for all scritplets that follow:
%global _makeme %_datadir/%name/makeme.sh

%files checkinstall

%pre checkinstall -p %_sbindir/sh-safely
set -x
%simple_test
%all_tests

%files archcompat-checkinstall

%pre archcompat-checkinstall -p %_sbindir/sh-safely
set -x
%archcompat_test
%simple_test

%files archcompat-with-proc-checkinstall

%pre archcompat-with-proc-checkinstall -p %_sbindir/sh-safely
set -x
%archcompat_test
%simple_test

%changelog
* Sat Aug 29 2020 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt7
- Removed the buildtime nprocs value from the *-checkinstall package scriptlets:
  it would make no sense at runtime.

* Fri Jul  3 2020 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt6
- Run additionally a test with a package built for system rpm's ARCH
  (i.e., with rpmbuild --target set to it).
- Ignore an arch_compat test on ARM (the one introduced in 1.1.3-alt5:
  with the default arch on this machine) until better times, because
  the ARM arch detection in rpm-build (<= 4.0.4-alt141) is not ideal yet.

* Tue Jun 30 2020 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt5
- Also test the compatibility between `uname -m`, rpmbuild, and rpm -i.
  (A separate archcompat-checkinstall subpkg does this.)
- First, run a simple test (to fail fast).

* Tue Jun  4 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt4
- To catch more errors:
  + in upgradable.mk strictly_newer_* helpers, separated the xfail reasons:
    a special reason for xfailing just the asymmetry test
    (i.e., a pair of pkgs non-upgradable in bad direction),
    and another one for xfailing just the upgrade test
    (i.e., the same pair of pkgs upgradable in good direction).
  (Now, the tests failing for one of the two reasons which is not marked as xfail
  will just fail rather than xfail. Previously, we couldn't distinguish them
  and could overlook a real unexpected failure.)

* Fri Apr 26 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt3
- To catch more errors (evidenced by file conflicts during rpm -U),
  now the package template includes a file with a unique value.
  (This runs more slowly.) (Suggested by Vladimir Seleznev.)

* Wed Mar 27 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt2
- (.spec) Factored out /usr/sbin/sh-safely (checkinstall-helper-sh-safely pkg)
  from %%pre of the checkinstall subpkg.
- In the tests, used the common /bin/tmpdir.sh (from tmpdir.sh pkg).

* Wed Mar 13 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt1
- New tests for disttag comparison with the obsolete (.) and current format (+)
  (Correct comparison would rely on a fix or a new feature in rpm:
  %%_priority_distbranch.)
- New tests for the %%_priority_distbranch feature in normal situation.
- The reasons of the currently XFAILing tests (with rpm-4.13.0.1-alt6):
  1. upgrade w.r.t. buildtime is not a strict order;
  2. upgrade w.r.t. disttag:
    2a. not a strict order;
    2b. %%_priority_distbranch not honored;
    2c. unrecognized disttag format is not "older"
        than a disttag with a recognized branch prefix;
  3. upgrade w.r.t. disttag fails in non-standard configuration
     without honor_buildtime;
  4. obsoleting an exact disttag (which is an unrealistic situation)
     doesn't work;
  5. mishandled elusive dep with a release but no epoch.

* Thu Feb 28 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt1
- Tests for upgradability according to the disttag. (XFAIL: incorrect
  behavior in rpm-4.13.0.1-alt5, but different in 4.0.4-alt101.M80P.5;
  XFAIL: fails in non-standard configuration without honor_buildtime.)
- Extended the tests for the overlapping of constraints and packages
  with cases of "elusive deps" (a dependency with a release, but no epoch:
  should it match any epoch? Marked XFAIL for now.)

* Wed Feb 27 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1
- More complete set of tests of the upgradability order
  (for different releases and buildtimes, not yet disttags).

* Mon Feb 25 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1
- Test the upgradable order
  (a package can be upgraded only to a more fresh release or buildtime).
- Marked one of the new tests XFAIL: strict buildtime-based
  upgradability order is broken at least in rpm-4.13.0.1-alt5.

* Thu Feb 21 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt4
- In disttag, use xxx (instead of zzz), because rpm-build-4.0.4-alt127
  now uses z as the "maximal" disttag. This makes the tests more
  appropriate for testing an "old" disttag-unaware rpm with packages
  built by the "new" rpm-build.

* Mon Feb 11 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt3
- Unmarked XFAIL: cases with underspecified Provides
  (the error should be gone with rpm-4.13-alt6).
- Marked XFAIL: non-critical unrealistic cases when obsoleting an exact disttag.
 (Of course, this requires a fix, but this is not critical.)

* Sun Feb 10 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2
- Additionally test the same things, but provided as virtual Provides
  (dummy = ...).
- Implemented a checkinstall subpackage that runs these tests immediately.
- Fixed running the tests from another working dir.

* Tue Feb  5 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1
- initial build for ALT Linux Sisyphus.


