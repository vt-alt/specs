
Name: acpica
Version: 20190509
Release: alt1
Summary: ACPICA tools for the development and debug of ACPI tables

Group: System/Kernel and hardware
License: GPLv2
Url: https://www.acpica.org/

#vcs-git https://github.com/acpica/acpica.git
Source: %name-%version.tar
Source3: iasl.1
Source4: acpibin.1
Source5: acpidump.1
Source6: acpiexec.1
Source7: acpihelp.1
Source8: acpinames.1
Source9: acpisrc.1
Source10: acpixtract.1
Source11: acpiexamples.1
Source12: badcode.asl.result
Source13: grammar.asl.result
Source14: converterSample.asl.result
Source15: run-misc-tests.sh

Patch0: big-endian.patch
Patch1: unaligned.patch
Patch2: OPT_LDFLAGS.patch
Patch3: int-format.patch
Patch4: f23-harden.patch
Patch5: template.patch
Patch6: ppc64le.patch
Patch7: arm7hl.patch
Patch8: big-endian-v2.patch
Patch9: simple-64bit.patch
Patch10: mips-be-fix.patch
Patch11: cve-2017-13693.patch
Patch12: cve-2017-13694.patch
Patch13: cve-2017-13695.patch
Patch14: str-trunc-warn.patch
Patch15: ptr-cast.patch
Patch16: aslcodegen.patch
Patch17: facp.patch

BuildRequires: bison flex

Provides: %name-tools = %version-%release

# The previous iasl package contained only a very small subset of these tools
# and it produced only the iasl package listed below; further, the pmtools
# package -- which provides acpidump -- also provides a /usr/sbin/acpixtract
# that we don't really want to collide with
Provides: acpixtract = %version-%release
Provides: iasl = %version-%release
Obsoletes: iasl < %version-%release

# The pmtools package provides an obsolete and deprecated version of the
# acpidump command from lesswatts.org which has now been taken off-line.
# ACPICA, however, is providing a new version and we again do not want to
# conflict with the command name.
Provides: acpidump = %version-%release
Provides: pmtools = %version-%release
Obsoletes: pmtools < %version-%release

%description
The ACPI Component Architecture (ACPICA) project provides an OS-independent
reference implementation of the Advanced Configuration and Power Interface
Specification (ACPI).  ACPICA code contains those portions of ACPI meant to
be directly integrated into the host OS as a kernel-resident subsystem, and
a small set of tools to assist in developing and debugging ACPI tables.

This package contains only the user-space tools needed for ACPI table
development, not the kernel implementation of ACPI.  The following commands
are installed:
   -- iasl: compiles ASL (ACPI Source Language) into AML (ACPI Machine
      Language), suitable for inclusion as a DSDT in system firmware.
      It also can disassemble AML, for debugging purposes.
   -- acpibin: performs basic operations on binary AML files (e.g.,
      comparison, data extraction)
   -- acpidump: write out the current contents of ACPI tables
   -- acpiexec: simulate AML execution in order to debug method definitions
   -- acpihelp: display help messages describing ASL keywords and op-codes
   -- acpinames: display complete ACPI name space from input AML
   -- acpisrc: manipulate the ACPICA source tree and format source files
      for specific environments
   -- acpixtract: extract binary ACPI tables from acpidump output (see
      also the pmtools package)

This version of the tools is being released under GPLv2 license.

%prep
%setup

%patch0 -p1 -b .big-endian
%patch1 -p1 -b .unaligned
%patch2 -p1 -b .OPT_LDFLAGS
%patch3 -p1 -b .int-format
%patch4 -p1 -b .f23-harden
# do not preserve a backup for this patch; it alters the results
# of the template test case and forces it to fail
%patch5 -p1
%patch6 -p1 -b .ppc64le
%patch7 -p1 -b .arm7hl
%patch8 -p1 -b .big-endian-v2
%patch9 -p1 -b .simple-64bit
%patch10 -p1 -b .mips-be-fix
%patch11 -p1 -b .cve-2017-13693
%patch12 -p1 -b .cve-2017-13694
%patch13 -p1 -b .cve-2017-13695
%patch14 -p1 -b .str-trunc-warn
%patch15 -p1 -b .ptr-cast
%patch16 -p1 -b .aslcodegen
%patch17 -p1 -b .facp

cp -p %SOURCE3 iasl.1
cp -p %SOURCE4 acpibin.1
cp -p %SOURCE5 acpidump.1
cp -p %SOURCE6 acpiexec.1
cp -p %SOURCE7 acpihelp.1
cp -p %SOURCE8 acpinames.1
cp -p %SOURCE9 acpisrc.1
cp -p %SOURCE10 acpixtract.1
cp -p %SOURCE11 acpiexamples.1
cp -p %SOURCE12 badcode.asl.result
cp -p %SOURCE13 grammar.asl.result
cp -p %SOURCE14 converterSample.asl.result
cp -p %SOURCE15 tests/run-misc-tests.sh
chmod a+x tests/run-misc-tests.sh

%build
CWARNINGFLAGS="\
    -std=c99 \
    -Wall \
    -Wbad-function-cast \
    -Wdeclaration-after-statement \
    -Werror \
    -Wformat=2 \
    -Wmissing-declarations \
    -Wmissing-prototypes \
    -Wstrict-aliasing=0 \
    -Wstrict-prototypes \
    -Wswitch-default \
    -Wpointer-arith \
    -Wundef \
    -Waddress \
    -Waggregate-return \
    -Winit-self \
    -Winline \
    -Wmissing-declarations \
    -Wmissing-field-initializers \
    -Wnested-externs \
    -Wold-style-definition \
    -Wno-format-nonliteral \
    -Wredundant-decls \
    -Wempty-body \
    -Woverride-init \
    -Wlogical-op \
    -Wmissing-parameter-type \
    -Wold-style-declaration \
    -Wtype-limits"

OPT_CFLAGS="%optflags $CWARNINGFLAGS"
export OPT_CFLAGS

%make HOST=_LINUX

%install
# Install the binaries
mkdir -p %buildroot%_bindir
install -pD -m0755 generate/unix/bin*/* %buildroot%_bindir/

# Install the man pages
mkdir -p %buildroot%_man1dir
install -pD -m0644 *.1 %buildroot%_man1dir/

%check
cd tests

# ASL tests
./aslts.sh                         # relies on non-zero exit
[ $? -eq 0 ] || exit 1

# misc tests
./run-misc-tests.sh %buildroot%_bindir %version

# Template tests
cd templates
make
if [ -f diff.log ]
then
    if [ -s diff.log ]
    then
        exit 1                  # implies errors occurred
    fi
fi
cd ..


%files
%doc documents/changes.txt source/compiler/new_table.txt
%_bindir/*
%_man1dir/*

%changelog
* Thu Aug 01 2019 Alexey Shabalin <shaba@altlinux.org> 20190509-alt1
- 20190509

* Wed Jan 16 2019 Alexey Shabalin <shaba@altlinux.org> 20181213-alt1
- 20181213

* Fri Aug 24 2018 Alexey Shabalin <shaba@altlinux.org> 20180810-alt1
- 20180810

* Wed May 23 2018 Alexey Shabalin <shaba@altlinux.ru> 20180508-alt1
- 20180508

* Mon Apr 02 2018 Alexey Shabalin <shaba@altlinux.ru> 20180209-alt1
- 20180209
- Fixes:
  + CVE-2017-13693
  + CVE-2017-13694
  + CVE-2017-13695

* Wed Feb 07 2018 Alexey Shabalin <shaba@altlinux.ru> 20180105-alt1
- 20180105
- Pulled in a mips32/BE patch from Debian, for completeness sake

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 20171110-alt1
- 20171110
- Add patch for mips64el build, should it ever be needed; it also cleans
  up all 64-bit arches, so nice to have regardless
- Add new patch for a TPM2 big-endian issue.

* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 20170929-alt1
- 20170929

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 20170728-alt1
- 20170728

* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 20161222-alt1
- 20161222

* Tue Aug 23 2016 Alexey Shabalin <shaba@altlinux.ru> 20160729-alt1
- 20160729

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 20160527-alt1
- 20160527

* Fri May 13 2016 Alexey Shabalin <shaba@altlinux.ru> 20160422-alt1
- 20160422

* Thu Dec 10 2015 Alexey Shabalin <shaba@altlinux.ru> 20150930-alt1
- Initial build
- Replace iasl and pmtools packages
