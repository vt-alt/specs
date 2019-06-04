Name: rpminstall-tests
Version: 1.1.3
Release: alt4

Summary: Tests for rpm: how it interprets packages when installing

BuildRequires(pre): rpm-build-licenses
License: %gpl2plus
Group: Development/Tools
Url: http://git.altlinux.org/people/imz/packages/rpminstall-tests.git

BuildArch: noarch

Requires: make rpm-build tmpdir.sh
%{?!_without_check:%{?!_disable_check:BuildRequires: make rpm-build tmpdir.sh}}

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

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%name
install -m0644 Makefile HELPER *.mk -t %buildroot%_datadir/%name/
install -m0755 makeme.sh -t %buildroot%_datadir/%name/

%check
# To pass the usual parallelism flags etc:
%global _make_bin ./makeme.sh
%make_build %{?opts}
# Also test with "Epoch: 0" instead of no Epoch:
%make_build %{?opts} clean
%make_build %{?opts} minimal_epoch=0

%files
%_datadir/%name

%files checkinstall

%pre checkinstall -p %_sbindir/sh-safely
%_datadir/%name/makeme.sh %{?opts}
%_datadir/%name/makeme.sh %{?opts} clean
%_datadir/%name/makeme.sh %{?opts} minimal_epoch=0

%changelog
* Tue Jun  4 2019 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt4
- To catch more errors:
  + upgradable.mk strictly_newer_* helpers:
    a special reason for xfailing just the asymmetry test.
  (The tests failing for other reasons will just fail rather than xfail.)

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


