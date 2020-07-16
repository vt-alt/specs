%def_enable tui
%def_disable check
%def_with python

# Currently gdbserver does not support RISC-V
%ifarch riscv64
%def_disable gdbserver
%else
%def_enable gdbserver
%endif

Name: gdb
Version: 8.2.50.20180917
Release: alt4.1

Summary: A GNU source-level debugger for C, C++ and other languages
License: GPLv3+
Group: Development/Debuggers
Url: http://www.gnu.org/software/gdb/

# ftp://sourceware.org/pub/gdb/snapshots/current/gdb-%version.tar.xz
Source: gdb-%version.tar
# Cleanup any leftover testsuite processes as it may stuck hasher builds.
Source2: gdb-orphanripper.c
# Man page for gstack(1).
Source3: gdb-gstack.man

Patch1: gdb-alt-testsuite-version.patch
Patch2: gdb-alt-readline.patch
Patch3: gdb-alt-bfd.patch

### Fedora patches
# Match the Fedora's version info.
#=fedora
Patch1001: gdb-6.3-rh-testversion-20041202.patch

# VLA (Fortran dynamic arrays) from Intel + archer-jankratochvil-vla tests.
#=push
Patch1002: gdb-vla-intel-fortran-strides.patch

#=push
Patch1003: gdb-vla-intel-fortran-vla-strings.patch

#=push+jan
Patch1004: gdb-vla-intel-stringbt-fix.patch

# Better parse 64-bit PPC system call prologues.
#=push: Write new testcase.
Patch1005: gdb-6.3-ppc64syscall-20040622.patch

# Include the pc's section when doing a symbol lookup so that the
# correct symbol is found.
#=push: Write new testcase.
Patch1006: gdb-6.3-ppc64displaysymbol-20041124.patch

# Add a wrapper script to GDB that implements pstack using the
# --readnever option.
#=push
Patch1007: gdb-6.3-gstack-20050411.patch

# VSYSCALL and PIE
#=fedoratest
Patch1008: gdb-6.3-test-pie-20050107.patch

# Get selftest working with sep-debug-info
#=fedoratest
Patch1009: gdb-6.3-test-self-20050110.patch

# Test support of multiple destructors just like multiple constructors
#=fedoratest
Patch1010: gdb-6.3-test-dtorfix-20050121.patch

# Fix to support executable moving
#=fedoratest
Patch1011: gdb-6.3-test-movedir-20050125.patch

# Test sibling threads to set threaded watchpoints for x86 and x86-64
#=fedoratest
Patch1012: gdb-6.3-threaded-watchpoints2-20050225.patch

# Notify observers that the inferior has been created
#=fedoratest
Patch1013: gdb-6.3-inferior-notification-20050721.patch

# Verify printing of inherited members test
#=fedoratest
Patch1014: gdb-6.3-inheritancetest-20050726.patch

# Add readnever option
#=push
Patch1015: gdb-6.3-readnever-20050907.patch

# Support TLS symbols (+`errno' suggestion if no pthread is found) (BZ 185337).
#=push+jan: It should be replaced by Infinity project.
Patch1016: gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch

# Fix TLS symbols resolving for shared libraries with a relative pathname.
# The testsuite needs `gdb-6.5-tls-of-separate-debuginfo.patch'.
#=fedoratest: One should recheck if it is really fixed upstream.
Patch1017: gdb-6.5-sharedlibrary-path.patch

# Improved testsuite results by the testsuite provided by the courtesy of BEA.
#=fedoratest: For upstream it should be rewritten as a dejagnu test, the test of no "??" was useful.
Patch1018: gdb-6.5-BEA-testsuite.patch

# Testcase for deadlocking on last address space byte; for corrupted backtraces.
#=fedoratest
Patch1019: gdb-6.5-last-address-space-byte-test.patch

# Fix readline segfault on excessively long hand-typed lines.
#=fedoratest
Patch1020: gdb-6.5-readline-long-line-crash-test.patch

# Fix bogus 0x0 unwind of the thread's topmost function clone(3) (BZ 216711).
#=fedora
Patch1021: gdb-6.5-bz216711-clone-is-outermost.patch

# Test sideeffects of skipping ppc .so libs trampolines (BZ 218379).
#=fedoratest
Patch1022: gdb-6.5-bz218379-ppc-solib-trampoline-test.patch

# Fix lockup on trampoline vs. its function lookup; unreproducible (BZ 218379).
#=fedora
Patch1023: gdb-6.5-bz218379-solib-trampoline-lookup-lock-fix.patch

# Find symbols properly at their original (included) file (BZ 109921).
#=fedoratest
Patch1024: gdb-6.5-bz109921-DW_AT_decl_file-test.patch

# Update PPC unwinding patches to their upstream variants (BZ 140532).
#=fedoratest
Patch1025: gdb-6.3-bz140532-ppc-unwinding-test.patch

# Testcase for exec() from threaded program (BZ 202689).
#=fedoratest
Patch1026: gdb-6.3-bz202689-exec-from-pthread-test.patch

# Testcase for PPC Power6/DFP instructions disassembly (BZ 230000).
#=fedoratest
Patch1027: gdb-6.6-bz230000-power6-disassembly-test.patch

# Allow running `/usr/bin/gcore' with provided but inaccessible tty (BZ 229517).
#=fedoratest
Patch1028: gdb-6.6-bz229517-gcore-without-terminal.patch

# Avoid too long timeouts on failing cases of "annota1.exp annota3.exp".
#=fedoratest
Patch1029: gdb-6.6-testsuite-timeouts.patch

# Support for stepping over PPC atomic instruction sequences (BZ 237572).
#=fedoratest
Patch1030: gdb-6.6-bz237572-ppc-atomic-sequence-test.patch

# Make upstream `set scheduler-locking step' as default.
#=push+jan: How much is scheduler-locking relevant after non-stop?
Patch1031: gdb-6.6-scheduler_locking-step-is-default.patch

# Test kernel VDSO decoding while attaching to an i386 process.
#=fedoratest
Patch1032: gdb-6.3-attach-see-vdso-test.patch

# Test leftover zombie process (BZ 243845).
#=fedoratest
Patch1033: gdb-6.5-bz243845-stale-testing-zombie-test.patch

# New locating of the matching binaries from the pure core file (build-id).
#=push+jan
Patch1034: gdb-6.6-buildid-locate.patch

# Fix loading of core files without build-ids but with build-ids in executables.
# Load strictly build-id-checked core files only if no executable is specified
# (Jan Kratochvil, RH BZ 1339862).
#=push+jan
Patch1035: gdb-6.6-buildid-locate-solib-missing-ids.patch

#=push+jan
Patch1036: gdb-6.6-buildid-locate-rpm.patch

# Fix displaying of numeric char arrays as strings (BZ 224128).
#=fedoratest: But it is failing anyway, one should check the behavior more.
Patch1037: gdb-6.7-charsign-test.patch

# Test PPC hiding of call-volatile parameter register.
#=fedoratest
Patch1038: gdb-6.7-ppc-clobbered-registers-O2-test.patch

# Testsuite fixes for more stable/comparable results.
#=fedoratest
Patch1039: gdb-6.7-testsuite-stable-results.patch

# Test ia64 memory leaks of the code using libunwind.
#=fedoratest
Patch1040: gdb-6.5-ia64-libunwind-leak-test.patch

# Test hiding unexpected breakpoints on intentional step commands.
#=fedoratest
Patch1041: gdb-6.5-missed-trap-on-step-test.patch

# Test gcore memory and time requirements for large inferiors.
#=fedoratest
Patch1042: gdb-6.5-gcore-buffer-limit-test.patch

# Test GCORE for shmid 0 shared memory mappings.
#=fedoratest: But it is broken anyway, sometimes the case being tested is not reproducible.
Patch1043: gdb-6.3-mapping-zero-inode-test.patch

# Test a crash on `focus cmd', `focus prev' commands.
#=fedoratest
Patch1044: gdb-6.3-focus-cmd-prev-test.patch

# Test various forms of threads tracking across exec() (BZ 442765).
#=fedoratest
Patch1045: gdb-6.8-bz442765-threaded-exec-test.patch

# Silence memcpy check which returns false positive (sparc64)
#=push: But it is just a GCC workaround, look up the existing GCC PR for it.
Patch1046: gdb-6.8-sparc64-silence-memcpy-check.patch

# Test a crash on libraries missing the .text section.
#=fedoratest
Patch1047: gdb-6.5-section-num-fixup-test.patch

# Fix register assignments with no GDB stack frames (BZ 436037).
#=push+jan: This fix is incorrect.
Patch1048: gdb-6.8-bz436037-reg-no-longer-active.patch

# Test the watchpoints conditionals works.
#=fedoratest
Patch1049: gdb-6.8-watchpoint-conditionals-test.patch

# Fix resolving of variables at locations lists in prelinked libs (BZ 466901).
#=fedoratest
Patch1050: gdb-6.8-bz466901-backtrace-full-prelinked.patch

# New test for step-resume breakpoint placed in multiple threads at once.
#=fedoratest
Patch1051: gdb-simultaneous-step-resume-breakpoint-test.patch

# Fix GNU/Linux core open: Can't read pathname for load map: Input/output error.
# Fix regression of undisplayed missing shared libraries caused by a fix for.
#=fedoratest: It should be in glibc: libc-alpha: <20091004161706.GA27450@.*>
Patch1052: gdb-core-open-vdso-warning.patch

# Fix syscall restarts for amd64->i386 biarch.
#=push+jan
Patch1053: gdb-x86_64-i386-syscall-restart.patch

# Fix stepping with OMP parallel Fortran sections (BZ 533176).
#=push+jan: It requires some better DWARF annotations.
Patch1054: gdb-bz533176-fortran-omp-step.patch

# Fix regression by python on ia64 due to stale current frame.
#=push+jan
Patch1055: gdb-follow-child-stale-parent.patch

# Workaround ccache making lineno non-zero for command-line definitions.
#=fedoratest: ccache is rarely used and it is even fixed now.
Patch1056: gdb-ccache-workaround.patch

#=push+jan: May get obsoleted by Tom's unrelocated objfiles patch.
Patch1057: gdb-archer-pie-addons.patch

#=push+jan: Breakpoints disabling matching should not be based on address.
Patch1058: gdb-archer-pie-addons-keep-disabled.patch

# Testcase for "Do not make up line information" fix by Daniel Jacobowitz.
#=fedoratest
Patch1059: gdb-lineno-makeup-test.patch

# Test power7 ppc disassembly.
#=fedoratest
Patch1060: gdb-ppc-power7-test.patch

# Fix i386+x86_64 rwatch+awatch before run, regression against 6.8 (BZ 541866).
# Fix i386 rwatch+awatch before run (BZ 688788, on top of BZ 541866).
#=push+jan: It should be fixed properly instead.
Patch1061: gdb-bz541866-rwatch-before-run.patch

# Workaround non-stop moribund locations exploited by kernel utrace (BZ 590623).
#=push+jan: Currently it is still not fully safe.
Patch1062: gdb-moribund-utrace-workaround.patch

# Fix follow-exec for C++ programs (bugreported by Martin Stransky).
#=fedoratest
Patch1063: gdb-archer-next-over-throw-cxx-exec.patch

# Backport DWARF-4 support (BZ 601887, Tom Tromey).
#=fedoratest
Patch1064: gdb-bz601887-dwarf4-rh-test.patch

#=push+jan
Patch1065: gdb-6.6-buildid-locate-core-as-arg.patch

# Workaround librpm BZ 643031 due to its unexpected exit() calls (BZ 642879).
#=push+jan
Patch1066: gdb-6.6-buildid-locate-rpm-librpm-workaround.patch

# [delayed-symfile] Test a backtrace regression on CFIs without DIE (BZ 614604).
#=fedoratest
Patch1067: gdb-test-bt-cfi-without-die.patch

# Out of memory is just an error, not fatal (uninitialized VLS vars, BZ 568248).
#=push+jan: Inferior objects should be read in parts, then this patch gets obsoleted.
Patch1068: gdb-bz568248-oom-is-error.patch

# Verify GDB Python built-in function gdb.solib_address exists (BZ # 634108).
#=fedoratest
Patch1069: gdb-bz634108-solib_address.patch

# New test gdb.arch/x86_64-pid0-core.exp for kernel PID 0 cores (BZ 611435).
#=fedoratest
Patch1070: gdb-test-pid0-core.patch

# [archer-tromey-delayed-symfile] New test gdb.dwarf2/dw2-aranges.exp.
#=fedoratest
Patch1071: gdb-test-dw2-aranges.patch

# [archer-keiths-expr-cumulative+upstream] Import C++ testcases.
#=fedoratest
Patch1072: gdb-test-expr-cumulative-archer.patch

# Fix regressions on C++ names resolving (PR 11734, PR 12273, Keith Seitz).
#=fedoratest
Patch1073: gdb-physname-pr11734-test.patch

# Fix regressions on C++ names resolving (PR 11734, PR 12273, Keith Seitz).
#=fedoratest
Patch1074: gdb-physname-pr12273-test.patch

# Toolchain on sparc is slightly broken and debuginfo files are generated
# with non 64bit aligned tables/offsets.
# See for example readelf -S ../Xvnc.debug.
#
# As a consenquence calculation of sectp->filepos as used in
# dwarf2_read_section (gdb/dwarf2read.c:1525) will return a non aligned buffer
# that cannot be used directly as done with MMAP.
# Usage will result in a BusError.
#
# While we figure out what's wrong in the toolchain and do a full archive
# rebuild to fix it, we need to be able to use gdb :)
#=push
Patch1075: gdb-7.2.50-sparc-add-workaround-to-broken-debug-files.patch

# Test GDB opcodes/ disassembly of Intel Ivy Bridge instructions (BZ 696890).
#=fedoratest
Patch1076: gdb-test-ivy-bridge.patch

# Hack for proper PIE run of the testsuite.
#=fedoratest
Patch1077: gdb-runtest-pie-override.patch

# Print reasons for failed attach/spawn incl. SELinux deny_ptrace (BZ 786878).
#=push+jan
Patch1078: gdb-attach-fail-reasons-5of5.patch

# Workaround PR libc/14166 for inferior calls of strstr.
#=fedora: Compatibility with RHELs (unchecked which ones).
Patch1079: gdb-glibc-strstr-workaround.patch

# Include testcase for `Unable to see a variable inside a module (XLF)' (BZ 823789).
#=fedoratest
Patch1080: gdb-rhel5.9-testcase-xlf-var-inside-mod.patch

# Testcase for `Setting solib-absolute-prefix breaks vDSO' (BZ 818343).
#=fedoratest
Patch1081: gdb-rhbz-818343-set-solib-absolute-prefix-testcase.patch

# Fix `GDB cannot access struct member whose offset is larger than 256MB'
# (RH BZ 795424).
#=push
Patch1082: gdb-rhbz795424-bitpos-20of25.patch

# Fix `GDB cannot access struct member whose offset is larger than 256MB'
# (RH BZ 795424).
#=push
Patch1083: gdb-rhbz795424-bitpos-21of25.patch

# Fix `GDB cannot access struct member whose offset is larger than 256MB'
# (RH BZ 795424).
#=push
Patch1084: gdb-rhbz795424-bitpos-22of25.patch

# Fix `GDB cannot access struct member whose offset is larger than 256MB'
# (RH BZ 795424).
#=push
Patch1085: gdb-rhbz795424-bitpos-23of25.patch

# Fix `GDB cannot access struct member whose offset is larger than 256MB'
# (RH BZ 795424).
#=push
Patch1086: gdb-rhbz795424-bitpos-25of25.patch

# Fix `GDB cannot access struct member whose offset is larger than 256MB'
# (RH BZ 795424).
#=push
Patch1087: gdb-rhbz795424-bitpos-25of25-test.patch

# Fix `GDB cannot access struct member whose offset is larger than 256MB'
# (RH BZ 795424).
#=push
Patch1088: gdb-rhbz795424-bitpos-lazyvalue.patch

# Import regression test for `gdb/findvar.c:417: internal-error:
# read_var_value: Assertion `frame' failed.' (RH BZ 947564) from RHEL 6.5.
#=fedoratest
Patch1089: gdb-rhbz947564-findvar-assertion-frame-failed-testcase.patch

# Fix crash of -readnow /usr/lib/debug/usr/bin/gnatbind.debug (BZ 1069211).
#=push+jan
Patch1090: gdb-gnat-dwarf-crash-3of3.patch

# Fix 'memory leak in infpy_read_memory()' (RH BZ 1007614)
#=fedoratest
Patch1091: gdb-rhbz1007614-memleak-infpy_read_memory-test.patch

# Fix 'gdb gives highly misleading error when debuginfo pkg is present,
# but not corresponding binary pkg' (RH BZ 981154).
#=push+jan
Patch1092: gdb-6.6-buildid-locate-misleading-warning-missing-debuginfo-rhbz981154.patch

#=fedoratest
Patch1093: gdb-archer-vla-tests.patch

#=fedoratest
Patch1094: gdb-vla-intel-tests.patch

# Continue backtrace even if a frame filter throws an exception (Phil Muldoon).
#=push
Patch1095: gdb-btrobust.patch

# Display Fortran strings in backtraces.
#=fedoratest
Patch1096: gdb-fortran-frame-string.patch

# Fix Python GIL with gdb.execute("continue") (Phil Muldoon, BZ 1116957).
#=push
Patch1097: gdb-python-gil.patch

# Testcase for '[SAP] Recursive dlopen causes SAP HANA installer to
# crash.' (RH BZ 1156192).
#=fedoratest
Patch1098: gdb-rhbz1156192-recursive-dlopen-test.patch

# Fix jit-reader.h for multi-lib.
#=push+jan
Patch1099: gdb-jit-reader-multilib.patch

# Fix '`catch syscall' doesn't work for parent after `fork' is called'
# (Philippe Waroquiers, RH BZ 1149205).
#=fedoratest
Patch1100: gdb-rhbz1149205-catch-syscall-after-fork-test.patch

# Fix 'backport GDB 7.4 fix to RHEL 6.6 GDB' [Original Sourceware bug
# description: 'C++ (and objc): Internal error on unqualified name
# re-set', PR 11657] (RH BZ 1186476).
#=fedoratest
Patch1101: gdb-rhbz1186476-internal-error-unqualified-name-re-set-test.patch

# Test 'info type-printers' Python error (RH BZ 1350436).
#=fedoratest
Patch1102: gdb-rhbz1350436-type-printers-error.patch

# Fix '[ppc64] and [s390x] wrong prologue skip on -O2 -g code' (Jan
# Kratochvil, RH BZ 1084404).
#=fedoratest
Patch1103: gdb-rhbz1084404-ppc64-s390x-wrong-prologue-skip-O2-g-3of3.patch

# Never kill PID on: gdb exec PID (Jan Kratochvil, RH BZ 1219747).
#=push+jan
Patch1104: gdb-bz1219747-attach-kills.patch

# Force libncursesw over libncurses to match the includes (RH BZ 1270534).
#=push+jan
Patch1105: gdb-fedora-libncursesw.patch

# Test clflushopt instruction decode (for RH BZ 1262471).
#=fedoratest
Patch1106: gdb-opcodes-clflushopt-test.patch

# [rhel6] DTS backward Python compatibility API (BZ 1020004, Phil Muldoon).
#=fedora
Patch1107: gdb-dts-rhel6-python-compat.patch

# [SCL] Skip deprecated .gdb_index warning for Red Hat built files (BZ 953585).
#=push+jan
Patch1108: gdb-6.6-buildid-locate-rpm-scl.patch

# Work around readline-6.2 incompatibility not asking for --more-- (BZ 701131).
#=fedora
Patch1109: gdb-readline62-ask-more-rh.patch

# Make the GDB quit processing non-abortable to cleanup everything properly.
#=fedora: It was useful only after gdb-6.8-attach-signalled-detach-stopped.patch .
Patch1110: gdb-6.8-quit-never-aborts.patch

# [aarch64] Fix hardware watchpoints (RH BZ 1261564).
#=fedoratest
Patch1111: gdb-rhbz1261564-aarch64-hw-watchpoint-test.patch

# Add messages suggesting more recent RHEL gdbserver (RH BZ 1321114).
#=fedora
Patch1112: gdb-container-rh-pkg.patch

# New test for Python "Cannot locate object file for block" (for RH BZ 1325795).
#=fedoratest
Patch1113: gdb-rhbz1325795-framefilters-test.patch

# [dts+el7] [x86*] Bundle linux_perf.h for libipt (RH BZ 1256513).
#=fedora
Patch1114: gdb-linux_perf-bundle.patch

# Fix gdb-headless /usr/bin/ executables (BZ 1390251).
#=fedora
Patch1115: gdb-libexec-add-index.patch

# New testcase for: Fix <tab>-completion crash (Gary Benson, RH BZ 1398387).
#=fedoratest
Patch1116: gdb-rhbz1398387-tab-crash-test.patch

# [testsuite] Fix false selftest.exp FAIL from system readline-6.3+ (Patrick Palka).
#=fedoratest
Patch1117: gdb-testsuite-readline63-sigint.patch

# Python patches of: http://sourceware.org/gdb/wiki/ProjectArcher
#=push
Patch1118: gdb-archer.patch

# Revert upstream commit 469412dd9ccc4de5874fd3299b105833f36b34cd
Patch1119: gdb-vla-intel-fix-print-char-array.patch

# [s390x] Backport arch12 instructions decoding (RH BZ 1553104).
# =fedoratest
Patch1120: gdb-rhbz1553104-s390x-arch12-test.patch

# This patch is needed to compile GDB after -Werror=narrowing has
# been enabled by default.
# Author: Sergio Durigan Junior.
Patch1121: gdb-rhbz795424-bitpos-arrayview.patch


BuildRequires(pre): rpm-build-python3
BuildRequires: flex libreadline-devel libexpat-devel liblzma-devel zlib-devel
BuildRequires: gcc-c++
BuildRequires: makeinfo
BuildRequires: %{?_with_python:python3-devel} %{?_enable_tui:libncursesw-devel}
%{?!_without_check:%{?!_disable_check:BuildRequires: dejagnu glibc-devel-static gcc-c++ gcc-fortran gcc-objc prelink valgrind /proc /dev/pts}}
Requires: gdb-common = %version-%release

%description
GDB is a full featured, command driven debugger.  GDB allows you to
trace the execution of programs and examine their internal state at
any time.  The debugger is most effective when used together with a
supported compiler, such as those from the GNU Compiler Collection.

%package -n gdbserver
Summary: A standalone server for GDB (the GNU source-level debugger)
Group: Development/Debuggers

%description -n gdbserver
GDB, the GNU debugger, allows you to debug programs written in C, C++,
Java, and other languages, by executing them in a controlled fashion and
printing their data.
This package provides a program that allows you to run GDB on a
different machine than the one which is running the program being
debugged.


%package light
Summary: A GNU source-level debugger for C, C++ and other languages (light build)
Group: Development/Debuggers
Requires: gdb-common = %version-%release
Conflicts: gdb < 7.5.0.20121002-alt5

%description light
GDB is a full featured, command driven debugger.  GDB allows you to
trace the execution of programs and examine their internal state at
any time.  The debugger is most effective when used together with a
supported compiler, such as those from the GNU Compiler Collection.
This package contains light build of GDB without expat, python and
tui support.

%package common
Summary: GDB common files
Group: Development/Debuggers
BuildArch: noarch
Conflicts: gdb < 7.5.0.20121002-alt5

%description common
This package contains common GDB files.

%package -n libgdb-devel
Summary: GDB static libraries
Group: Development/C
Conflicts: libbfd-devel libiberty-devel

%description -n libgdb-devel
This package contains static GDB libraries required to build other debuggers.

%prep
%setup
# Remove generated bison and flex parser files.
egrep -lZ 'A (Bison parser, made by GNU Bison|lexical scanner generated by flex)' gdb/*.c |
	xargs -r0 rm --
# Remove generated info files.
rm */doc/*.info*
# Somehow readline/doc is needed to build other docs.
mv readline/doc readline-doc

### Fedora patches
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1
%patch1010 -p1
%patch1011 -p1
%patch1012 -p1
%patch1013 -p1
%patch1014 -p1
%patch1015 -p1
%patch1016 -p1
%patch1017 -p1
%patch1018 -p1
%patch1019 -p1
%patch1020 -p1
%patch1021 -p1
%patch1022 -p1
%patch1023 -p1
%patch1024 -p1
%patch1025 -p1
%patch1026 -p1
%patch1027 -p1
%patch1028 -p1
%patch1029 -p1
%patch1030 -p1
%patch1031 -p1
%patch1032 -p1
%patch1033 -p1
%patch1034 -p1
%patch1035 -p1
# %%patch1036 -p1 # TODO: apt support
%patch1037 -p1
%patch1038 -p1
%patch1039 -p1
%patch1040 -p1
%patch1041 -p1
%patch1042 -p1
%patch1043 -p1
%patch1044 -p1
%patch1045 -p1
%patch1046 -p1
%patch1047 -p1
%patch1048 -p1
%patch1049 -p1
%patch1050 -p1
%patch1051 -p1
%patch1052 -p1
%patch1053 -p1
%patch1054 -p1
%patch1055 -p1
%patch1056 -p1
%patch1057 -p1
%patch1058 -p1
%patch1059 -p1
%patch1060 -p1
%patch1061 -p1
%patch1062 -p1
%patch1063 -p1
%patch1064 -p1
%patch1065 -p1
# %%patch1066 -p1 # TODO: apt support
%patch1067 -p1
%patch1068 -p1
%patch1069 -p1
%patch1070 -p1
%patch1071 -p1
%patch1072 -p1
%patch1073 -p1
%patch1074 -p1
%patch1075 -p1
%patch1076 -p1
%patch1077 -p1
%patch1078 -p1
%patch1079 -p1
%patch1080 -p1
%patch1081 -p1
%patch1082 -p1
%patch1083 -p1
%patch1084 -p1
%patch1085 -p1
%patch1086 -p1
%patch1087 -p1
%patch1088 -p1
%patch1089 -p1
%patch1090 -p1
%patch1091 -p1
%patch1092 -p1
%patch1093 -p1
%patch1094 -p1
%patch1095 -p1
%patch1096 -p1
%patch1097 -p1
%patch1098 -p1
%patch1099 -p1
%patch1100 -p1
%patch1101 -p1
%patch1102 -p1
%patch1103 -p1
%patch1104 -p1
%patch1105 -p1
%patch1106 -p1
%patch1107 -p1
# %%patch1108 -p1 # TODO: apt support
%patch1109 -p1
%patch1110 -p1
%patch1111 -p1
%patch1112 -p1
%patch1113 -p1
%patch1114 -p1
%patch1115 -p1
%patch1116 -p1
%patch1117 -p1
%patch1118 -p1
%patch1119 -p1
%patch1120 -p1
%patch1121 -p1

# ALT patches
%patch1 -p1
%patch2 -p1
%patch3 -p1

# We want to use these as system libraries.
rm -r readline zlib

find -type f -name \*.orig -delete
xz -9k gdb/{MAINTAINERS,NEWS}

%build
echo '%version-%release (%distribution)' >gdb/version.in

for f in */configure.in; do
	pushd "${f%%/*}"
		[ configure.in -nt configure ] && autoconf
	popd
done
for f in */Makefile.am; do
	pushd "${f%%/*}"
		[ Makefile.am -nt Makefile.in ] && automake
	popd
done

%define _configure_script ../configure
%define configure_opts \\\
	--with-gdb-datadir=%_datadir/gdb \\\
	--with-separate-debug-dir=/usr/lib/debug \\\
	--with-auto-load-dir='$debugdir:%_libdir/gdb/auto-load:$datadir/auto-load' \\\
	--enable-gdb-build-warnings=,-Wno-unused \\\
	--enable-ubsan=no \\\
	--disable-werror \\\
	--disable-sim \\\
	--disable-rpath \\\
	--with-system-readline \\\
	--with-lzma \\\
	--without-libexpat-prefix \\\
	--without-rpm \\\
	--without-libunwind \\\
	--enable-64-bit-bfd \\\
	--with-system-zlib \\\
	%nil
export \
	ac_cv_have_x=${ac_cv_have_x='have_x=yes ac_x_includes=%_x11includedir ac_x_libraries=%_x11libdir'} \
	%{?!_enable_tui:ac_cv_search_tgetent='none required'} \
	#

%define buildtarget build-%_target
rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

%configure \
	%configure_opts \
	%{subst_enable tui} \
%if_with python
	--with-python=python3 \
%endif
#
%make_build
%make_build -C gdb libgdb.a
%make_build info MAKEINFOFLAGS=--no-split

popd #%buildtarget

rm -rf light
mkdir light
pushd light

%configure %configure_opts --disable-tui --without-expat --without-python
%make_build

popd #light

%install
%makeinstall_std -C %buildtarget
install -pm755 light/gdb/gdb %buildroot%_bindir/gdb-light

install -pm644 %_sourcedir/gdb-gstack.man %buildroot%_man1dir/gstack.1

# These files are already packaged as a part of binutils.
rm %buildroot%_infodir/bfd*
rm %buildroot%_datadir/locale/*/LC_MESSAGES/{bfd,opcodes}.mo

pushd %buildtarget
mkdir -p %buildroot%_libdir
install -pm644 */lib*.a %buildroot%_libdir/
popd #%buildtarget

mkdir -p %buildroot%_datadir/gdb/auto-load

rm %buildroot/%_datadir/gdb/system-gdbinit/elinos.py
rm %buildroot/%_datadir/gdb/system-gdbinit/wrs-linux.py
rmdir %buildroot/%_datadir/gdb/system-gdbinit

# contained in gdb binary
%add_python3_req_skip _gdb
%add_python3_path %_datadir/gdb/python

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
pushd %buildtarget/gdb
%__cc %optflags -o orphanripper %_sourcedir/gdb-orphanripper.c -lutil
./orphanripper make -k -j%__nprocs check ||:
popd

%pre
# gdb-8.2.50.20180917-alt1 switched from a symlink (to Python2 site-libdir)
# to a normal directory (with Python3 code). Give way to the directory:
l=%_datadir/gdb/python/gdb
if [ -L "$l" ]; then
    rm -v "$l"
fi

%files
%_bindir/*
%if_with python
%_datadir/gdb/python
%endif
%exclude %_bindir/gdb-light
%if_enabled gdbserver
%exclude %_bindir/gdbserver

%files -n gdbserver
%_bindir/gdbserver
# no ipa_obj for arm* and mips*
%ifnarch %arm %mips
%_libdir/libinproctrace.so
%endif
%endif

%files light
%_bindir/gdb-light

%files common
%_man1dir/*
%_infodir/*
%_datadir/gdb
%doc gdb/{MAINTAINERS,NEWS}.xz
%exclude %_datadir/gdb/python

%files -n libgdb-devel
%_includedir/*
%_libdir/lib*.a

%changelog
* Tue Jul 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.2.50.20180917-alt4.1
- ubsan renders gdb unusable on arm and adds no benefit in general, disable it

* Thu Jun 27 2019 Ivan Zakharyaschev <imz@altlinux.org> 8.2.50.20180917-alt4
- %%pre: corrected the old symlink path in 8.2.50.20180917-alt3.

* Wed Jun 26 2019 Ivan Zakharyaschev <imz@altlinux.org> 8.2.50.20180917-alt3
- %%pre: rm symlink to upgrade from gdb < 8.2.50.20180917-alt1. This works
  for rpm-4.0.4 (when upgrading from p8 to Sisyphus or p9), not for rpm-4.13.

* Wed Nov 21 2018 Nikita Ermakov <arei@altlinux.org> 8.2.50.20180917-alt2
- Disabled gdbserver for RISC-V (riscv64) architecture (not supported yet).

* Mon Oct 08 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 8.2.50.20180917-alt1
- Updated to 8.2.50.20180917, synced with Fedora 8.2.50.20181006-4.

* Mon Jun 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 7.9-alt4
- Fix build with modern glibc by syncing header definitions

* Mon Aug 29 2016 Andrey Cherepanov <cas@altlinux.org> 7.9-alt3
- Do not distribute desktop file for console program

* Thu Dec 10 2015 Andrey Cherepanov <cas@altlinux.org> 7.9-alt2
- Fix configure by adding makeinfo to build requirements
- Rebuild fixes redundant repl_strstr function in libgdb.a

* Tue Sep 08 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.9-alt1
- 7.9 released, synced with fedora 7.9-11

* Thu Jan 30 2014 Evgeny Sinelnikov <sin@altlinux.ru> 7.5.0.20121002-alt5
- Built with python support (closes: #29759).
- Added separate subpackages gdb-common and gdb-light.
- Changed default auto-load path to /usr/share/gdb directory.

* Tue Nov 19 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.5.0.20121002-alt4
- Fixed build with readline6.

* Fri Feb 15 2013 Dmitry V. Levin <ldv@altlinux.org> 7.5.0.20121002-alt3
- Packaged a lightweigted build of gdb as %_bindir/gdb-light.

* Wed Oct 10 2012 Dmitry V. Levin <ldv@altlinux.org> 7.5.0.20121002-alt2
- Disabled few patches that appeared to be too Fedora specific (closes: #27818).

* Fri Oct 05 2012 Dmitry V. Levin <ldv@altlinux.org> 7.5.0.20121002-alt1
- Updated to 7.5.0.20121002, synced with Fedora and Debian.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 7.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 03 2011 Dmitry V. Levin <ldv@altlinux.org> 7.2-alt2
- Updated desktop categories.

* Tue Feb 01 2011 Dmitry V. Levin <ldv@altlinux.org> 7.2-alt1
- Updated to 7.2, synced with FC gdb-7.2-40 and Debian gdb-7.2-1.
- Changed debug dir from %%_libdir/debug to /usr/lib/debug.

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 7.0.1-alt3
- Set gdb_datadir to %%_libdir/gdb to move auto-load directory out
  of /usr/share.
- Drop libstdc++ helpers: packaged from gcc now.

* Sun Apr 11 2010 Dmitry V. Levin <ldv@altlinux.org> 7.0.1-alt2
- libgdb-devel: Packaged libdecnumber.a.
- Fixed "gdb --version" output.

* Sun Mar 07 2010 Dmitry V. Levin <ldv@altlinux.org> 7.0.1-alt1
- Updated to 7.0.1 (closes: #19417, #20569, #21761).
- Imported bunch of patches from FC gdb-7.0.1-33.
- Imported bunch of patches from Debian gdb-7.0.1-2.

* Mon Mar 03 2008 Dmitry V. Levin <ldv@altlinux.org> 6.6-alt3
- Fixed build with fresh makeinfo.

* Fri Nov 16 2007 Dmitry V. Levin <ldv@altlinux.org> 6.6-alt2
- Packaged static gdb libraries into libgdb-devel subpackage (at@, #8899).

* Sun Apr 01 2007 Dmitry V. Levin <ldv@altlinux.org> 6.6-alt1
- Updated to 6.6.
- Imported bunch of patches from FC gdb-6.6-8.
- Imported bunch of patches from Debian gdb-6.6.dfsg-1.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 6.3-alt2.1
- Rebuilt with libreadline.so.5.

* Sun May 29 2005 Dmitry V. Levin <ldv@altlinux.org> 6.3-alt2
- Imported bunch of patches from Debian.
- Applied upstream fix to BFD library (CAN-2005-1704).
- Applied fix for .gdbinit issue (CAN-2005-1705).

* Mon Dec 20 2004 Dmitry V. Levin <ldv@altlinux.org> 6.3-alt1
- Updated to 6.3, updated patches.

* Wed Aug 04 2004 Dmitry V. Levin <ldv@altlinux.org> 6.2-alt1
- Updated to 6.2, updated patches.

* Tue Apr 06 2004 Dmitry V. Levin <ldv@altlinux.org> 6.1-alt1
- Updated to 6.1, updated patches.
- Applied patches from RH's gdb-6.0post-0.20040223.8
- Build with bundled libbfd, libopcodes and libiberty.
- Packaged gcore script.
- Enabled tui by default.

* Sun Aug 10 2003 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt2
- Rebuilt with libbfd-2.14.90.0.5.

* Fri Jun 20 2003 Dmitry V. Levin <ldv@altlinux.org> 5.3-alt1
- Updated to 5.3, rediffed patches.
- Merged with gdb-5.3-23mdk (8 patches added).

* Tue Oct 08 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt2
- Avoid build dependencies on XFree86-* (#0001376).
- Fixed build with new rpm-build.

* Mon Aug 26 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2.1-alt1
- 5.2.1
- Patched to link with libtinfo.
- Applied "rh-misc" patch from rh gdb-5.2.1-3.

* Mon Jun 17 2002 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- 5.2
- Built with system libreadline, libbfd, libopcodes and libiberty.

* Thu Feb 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 5.1.1-alt1
- Added menu entry.
- Moved mmaloc to separate subpackage.
- Usual ALT adaptions.

* Thu Jan 24 2002 Trond Eivind Glomsrød <teg@redhat.com> 5.1.1-1
- 5.1.1
- add URL

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Dec 10 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.1-2
- Fix some thread+fpu problems

* Mon Nov 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.1-1
- 5.1

* Mon Nov 19 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.94-0.71
- 5.0.94. Almost there....

* Mon Nov 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.93-2
- Add patch from jakub@redhat.com to improve handling of DWARF

* Mon Nov 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.93-1
- 5.0.93
- handle missing info pages in post/pre scripts

* Wed Oct 31 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.92-1
- 5.0.92

* Fri Oct 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0.91rh-1
- New snapshot
- Use the 5.0.91 versioning from the snapshot

* Wed Oct 17 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-17
- New snapshot

* Thu Sep 27 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Wed Sep 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-16
- New snapshot

* Mon Aug 13 2001 Trond Eivind Glomsrød <teg@redhat.com> 5.0rh-15
- Don't buildrequire compat-glibc (#51690)

* Thu Aug  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot, from the stable branch eventually leading to gdb 5.1

* Mon Jul 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Add texinfo to BuildRequires

* Mon Jun 25 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Fri Jun 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot
- Add ncurses-devel to buildprereq
- Remove perl from buildprereq, as gdb changed the way
  version strings are generated

* Thu Jun 14 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Wed May 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot - this had thread fixes for curing #39070
- New way of specifying version

* Tue May  1 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New tarball
- Kevin's patch is now part of gdb

* Mon Apr  9 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add patch from kevinb@redhat.com to fix floating point + thread
  problem (#24310)
- remove old workarounds
- new snapshot

* Thu Apr  5 2001 Trond Eivind Glomsrød <teg@redhat.com>
- New snapshot

* Sat Mar 17 2001 Bill Nottingham <notting@redhat.com>
- on ia64, there are no old headers :)

* Fri Mar 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- build with old headers, new compiler

* Wed Mar 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Feb 26 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot which should fix some more IA64 problems (#29151)
- remove IA64 patch, it's now integrated

* Wed Feb 21 2001 Trond Eivind Glomsrød <teg@redhat.com>
- add IA64 and Alpha patches from Kevin Buettner <kevinb@redhat.com>
- use perl instead of patch for fixing the version string

* Tue Feb 20 2001 Trond Eivind Glomsrød <teg@redhat.com>
- don't use kgcc anymore
- mark it as our own version
- new snapshot

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Link with ncurses 5.x even though we're using kgcc.
  No need to drag in requirements on ncurses4 (Bug #24445)

* Fri Jan 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Thu Dec 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Dec 04 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot
- new alpha patch - it now compiles everywhere. Finally.

* Fri Dec 01 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new snapshot

* Mon Nov 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- new CVS snapshot
- disable the patches
- don't use %%configure, as it confuses the autoconf script
- enable SPARC, disable Alpha

* Wed Aug 09 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added patch from GDB team for C++ symbol handling

* Mon Jul 25 2000 Trond Eivind Glomsrød <teg@redhat.com>
- upgrade to CVS snapshot
- excludearch SPARC, build on IA61

* Wed Jul 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul 02 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Fri Jun 08 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%configure, %%makeinstall, %%{_infodir}, %%{_mandir},
  and %%{_tmppath}
- the install scripts  for info are broken(they don't care about
  you specify in the installstep), work around that.
- don't build for IA64

* Mon May 22 2000 Trond Eivind Glomsrød <teg@redhat.com>
- upgraded to 5.0 - dump all patches. Reapply later if needed.
- added the NEWS file to the %%doc files
- don't delete files which doesn't get installed (readline, texinfo)
- let build system handle stripping and gzipping
- don't delete libmmalloc
- apply patch from jakub@redhat.com to make it build on SPARC

* Fri Apr 28 2000 Matt Wilson <msw@redhat.com>
- rebuilt against new ncurses

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Tue Feb  8 2000 Jakub Jelinek <jakub@redhat.com>
- fix core file handling on i386 with glibc 2.1.3 headers

* Fri Jan 14 2000 Jakub Jelinek <jakub@redhat.com>
- fix reading registers from core on sparc.
- hack around build problems on i386 with glibc 2.1.3 headers

* Thu Oct 7 1999 Jim Kingdon
- List files to install in /usr/info specifically (so we don't pick up
things like info.info from GDB snapshots).

* Thu Oct 7 1999 Jim Kingdon
- Update GDB to 19991004 snapshot.  This eliminates the need for the
sigtramp, sparc, xref, and threads patches.  Update sparcmin patch.

* Mon Aug 23 1999 Jim Kingdon
- Omit readline manpage.

* Tue Aug 7 1999 Jim Kingdon
- Remove H.J. Lu's patches (they had been commented out).
- Add sigtramp patch (from gdb.cygnus.com) and threads patch (adapted
from code fusion CD-ROM).

* Wed Apr 14 1999 Jeff Johnson <jbj@redhat.com>
- merge H.J. Lu's patches into 4.18.

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- updated the kern22 patch with stuff from davem

* Thu Apr  1 1999 Jeff Johnson <jbj@redhat.com>
- sparc with 2.2 kernels no longer uses sunos ptrace (davem)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Mon Mar  8 1999 Jeff Johnson <jbj@redhat.com>
- Sparc fiddles for Red Hat 6.0.
