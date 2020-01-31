Name: perl
Version: 5.28.2
Release: alt2
Epoch: 1

Summary: Practical Extraction and Report Language
License: Artistic-1.0 OR GPL-2.0-or-later
Group: Development/Perl
URL: http://www.perl.org
Packager: Perl Maintainers Team <cpan@packages.altlinux.org>

Source: perl-%version.tar

Patch01: perl-5.28.0-alt-644-at-ExtUtils-Install.patch
Patch02: perl-5.24.0-alt-644-at-installperl.patch
Patch03: perl-5.22.0-alt-644-viy-ExtUtils-Install-fix-test.patch
Patch04: perl-5.26.1-alt-at-MM_Unix-link-xs-with-libperl.patch
Patch05: perl-5.24.1-alt-at-MM_Unix-shabang.patch
Patch06: perl-5.28.1-alt-at-Storable-no-early-dep-on-Log-Agent.patch
Patch07: perl-5.24.0-alt-at-debian-Errno_pm.patch
Patch08: perl-5.26.1-alt-at-disable-Cpan-Meta-under-rpm.patch
Patch09: perl-5.24.0-alt-at-libperl-soname.patch
Patch10: perl-5.24.1-alt-at-no-rpath-for-std-libs.patch
Patch11: perl-5.20.1-alt-at-perl5db-findreq-cleanup.patch
Patch12: perl-5.20.1-alt-at-perlbug-findreq-cleanup.patch
Patch13: perl-5.20.1-alt-at-skip-deprecation-warning.patch
Patch14: perl-5.20.1-alt-crux-Cwd-use-realpath.patch
# or hsh with --mountpoints=/proc
Patch15: perl-5.20.1-alt-crux-fix-test-without-proc.patch
Patch16: perl-5.20.1-alt-ldv-support-for-alt-gcc-wrapper.patch
Patch17: perl-5.26.1-alt-viy-Unicode-Normalize-fix-deps.patch
# hack - sensitive test can fail transaction - see maintainers notes for 5.24.1
Patch18: perl-5.24.1-alt-viy-disable-Time-HiRes-itimer.t.patch
Patch19: perl-5.28.1-alt-viy-no-check-sums-in-customized.t.patch
# temporary quick hack; should be replaced by a proper surgery
# not installing version::regex will live perl.req's unmets
Patch20: perl-5.24.1-alt-viy-installperl-ExtUtils-MakeMaker-version.patch
# mail from Oleg Solovyov; see patch body
Patch21: perl-5.24.3-alt-solovyov.patch
Patch22: perl-5.28.1-alt-viy-caretx-chroot-support.patch
Patch23: perl-5.22.3-alt-mcpain-trust-mode.patch
Patch24: perl-5.28.2-fix-Time-Local-test-2020.patch

# cpan update patches here. use format below:
#Patch50: cpan-update-Socket-2.013-to-Socket-2.016.diff
Patch51: cpan-update-Test-Simple-1.302133-to-Test-Simple-1.302141.patch

# ------ inserted with srpm-spec-inject-patches(1) -------
# BeginPatches(fedora)[shift=300]: -----------------------

# Document Math::BigInt::CalcEmu requires Math::BigInt, rhbz#959096,
# CPAN RT#85015
Patch310:        perl-5.18.1-Document-Math-BigInt-CalcEmu-requires-Math-BigInt.patch

# Make *DBM_File desctructors thread-safe, bug #1107543, RT#61912
Patch311:        perl-5.18.2-Destroy-GDBM-NDBM-ODBM-SDBM-_File-objects-only-from-.patch

# Fix executing arybase::_tie_it() in Safe compartement, RT#131588,
# not yet accepted by upstream
Patch313:        perl-5.26.0-perl-131588-be-a-little-more-careful-in-arybase-_tie.patch

# Link XS modules to pthread library to fix linking with -z defs,
# <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/3RHZEHLRUHJFF2XGHI5RB6YPDNLDR4HG/>
Patch314:        perl-5.27.8-hints-linux-Add-lphtread-to-lddlflags.patch

# Fix printing a warning about a wide character when matching a regular
# expression while ISO-8859-1 locale is in effect, in upstream after 5.29.0
Patch317:        perl-5.29.0-regexec.c-Call-macro-with-correct-args.patch

# Fix invoking a check for wide characters while ISO-8859-1 locale is in effect,
# in upstream after 5.29.0
Patch318:        perl-5.29.0-perl.h-Add-parens-around-macro-arguments.patch

# Fix build conditions in locale.c, in upstream after 5.29.0
Patch320:        perl-5.29.0-locale.c-Fix-conditional-compilation.patch

# Fix a file descriptor leak in in-place edits, RT#133314,
# in upstream after 5.29.1
Patch321:        perl-5.29.1-perl-133314-test-for-handle-leaks-from-in-place-edit.patch

# Fix a buffer overrun in deprecated S_is_utf8_common(),
# in upstream after 5.29.1
Patch323:        perl-5.29.1-utf8.c-Make-safer-a-deprecated-function.patch

# Fix a time race in Time-HiRes/t/itimer.t test, in upstream after 5.29.1
Patch324:        perl-5.29.1-Time-HiRes-t-itimer.t-avoid-race-condition.patch

# Fix Time::Piece to handle objects in overloaded methods correctly,
# in upstream after 5.29.1
Patch326:        perl-5.29.1-Update-Time-Piece-to-CPAN-version-1.33.patch

# Fix an assignment to a lexical variable in multiconcatenation expressions,
# RT#133441, in upstream after 5.29.2
Patch327:        perl-5.29.2-multiconcat-mutator-not-seen-in-lex.patch

# Fix a spurious warning about uninitialized value in warn, RT#132683,
# in upstream after 5.29.2
Patch328:        perl-5.29.2-perl-132683-don-t-try-to-convert-PL_sv_placeholder-i.patch

# Pass the correct CFLAGS to dtrace
Patch330:        perl-5.28.0-Pass-CFLAGS-to-dtrace.patch

# Fix PathTools tests to cope with ESTALE error, RT#133534,
# in upstream after 5.29.3
Patch333:        perl-5.29.3-Accept-also-ESTALE-fix-for-RT-133534.patch

# Fix an undefined behaviour in S_hv_delete_common(), in upstream after 5.29.5
Patch334:        perl-5.29.5-S_hv_delete_common-avoid-undefined-behaviour.patch

# Fix compiling regular expressions that contain both compile- and run-time
# compiled code blocks, RT#133687, in upstream after 5.29.5
Patch338:        perl-5.29.5-handle-code-mixed-compile-and-runtime.patch

# Adjust tests to gdbm-1.15, RT#133295, in upstream after 5.29.5
Patch339:        perl-5.28.1-ext-GDBM_File-t-fatal.t-handle-non-fatality.patch
Patch340:        perl-5.29.5-Correct-spelling-error-in-skip-message.patch
Patch341:        perl-5.29.5-Avoid-Use-of-uninitialized-value-res-in-numeric-eq-w.patch

# Fix reporting a line number for non-terminated prototypes, RT#133524,
# in upstream after 5.29.6
Patch344:        perl-5.28.1-perl-133524-report-line-number-for-Prototype-not-ter.patch

# Fix first eof() return value, RT#133721, in upstream after 5.29.6
Patch345:        perl-5.29.6-perl-133721-TODO-test-for-eof-with-no-LAST_FH.patch
Patch346:        perl-5.29.6-First-eof-should-return-true.patch

# Prevent long jumps from clobbering local variables, RT#133575,
# in upstream after 5.29.6
Patch349:        perl-5.29.6-perl-133575-prevent-set-longjmp-clobbering-locals-in.patch

# Fix a mismatch with a case-insesitive regular expression on a text with
# ligatures, RT#133756, in upstream after 5.29.6
Patch350:        perl-5.29.6-PATCH-perl-133756-Failure-to-match-properly.patch

# Fix setting magic when changing $^R, RT#133782, in upstream after 5.29.7
Patch353:        perl-5.28.1-perl-133782-set-magic-when-changing-R.patch

# Fix a race when loading XS modules, in upstream after 5.29.7
Patch354:        perl-5.29.7-Perl_my_cxt_init-fix-potential-race-condition.patch

# Fix a leak when compiling a typed hash dereference, in upstream after 5.29.8
Patch356:        perl-5.28.1-fix-leak-when-compiling-typed-hash-deref.patch
Patch357:        perl-5.29.8-fix-blead-on-non-threaded-builds.patch

# Fix a buffer overread when handling a scope error in qr/\(?{/, RT#133879,
# in upstream after 5.29.8
Patch358:        perl-5.29.8-handle-scope-error-in-qr.patch

# Fix a buffer overread when parsing a regular expression with an unknown
# character name, RT#133880, in upstream after 5.29.9
Patch359:        perl-5.28.1-PATCH-perl-133880-assertion-failure.patch

# Fix mbstate_t initialization in POSIX::mblen, RT#133928,
# in upstream after 5.29.9
Patch360:        perl-5.28.1-Fix-POSIX-mblen-mbstate_t-initialization-on-threaded.patch

# Fix a memory leak when cloning a regular expression, in upstream after 5.29.9
Patch361:        perl-5.29.9-fix-leak-in-cloned-regexes.patch

# Fix a memory leak when spawning threads in a BEGIN phase,
# in upstream after 5.29.9
Patch362:        perl-5.29.9-fix-leak-in-BEGIN-threads-new.patch

# Fix a memory leak when assigning a regular expression to a non-copy-on-write
# string, in upstream after 5.29.9
Patch363:        perl-5.29.9-avoid-leak-assigning-regexp-to-non-COW-string.patch

# Fix a memory leak when assignig to a localized ${^WARNING_BITS},
# in upstream after 5.29.9
Patch364:        perl-5.29.9-fix-leak-with-local-WARNING_BITS.patch

# Fix a memory leak when parsing misindented here-documents,
# in upstream after 5.29.9
Patch365:        perl-5.28.1-fix-a-leak-with-indented-heredocs.patch

# Fix a memory leak in package name lookup, RT#133977, in upstream after 5.29.9
Patch366:        perl-5.29.9-fix-leak-in-package-name-lookup.patch
Patch367:        perl-5.29.9-Fix-recent-double-free-in-S_parse_gv_stash_name.patch

# Fix a memory leak when deletion in a tied hash dies, in upstream after 5.29.9
Patch368:        perl-5.29.9-avoid-leak-with-local-h-foo-a-n.patch

# Fix a crash when matching case insensitively, RT#133892,
# in upstream after 5.29.9
Patch369:        perl-5.28.1-perl-133892-coredump-in-Perl_re_intuit_start.patch

# Fix a memory leak when warning about malformed UTF-8 string
Patch370:        perl-5.29.9-fix-leak-in-Perl__force_out_malformed_utf8_message.patch
# EndPatches(fedora): --------------------------------------

# there's a problem with strict.pm
%add_findreq_skiplist */strict.pm
# the failure for bytes_heavy.pl is normal, it's not self-contained
%add_findreq_skiplist */bytes_heavy.pl
# skip Compress::Zlib and Encode dependencies
%add_findreq_skiplist */DBM_Filter/*.pm
# Data::Dumper uses B::Deparse (on demand) to store coderefs
%add_findreq_skiplist */Data/Dumper.pm
# open.pm requires Encode in certain cases
%add_findreq_skiplist */open.pm
# Pod::Html requires Pod::Simple
%add_findreq_skiplist */Pod/Html.pm
%add_findreq_skiplist */pod2html
# It requires Encode which we split out
%add_findreq_skiplist */ExtUtils/MakeMaker.pm
%add_findreq_skiplist */ExtUtils/MakeMaker/Locale.pm
# It requires Term::Readline which is moved to Term-Readline-Gnu
%add_findreq_skiplist */perl5db.pl

# do not provide auxiliary unicore libraries
%add_findprov_skiplist */unicore/*/*

BuildRequires: /proc

%package base
Summary: Pathologically Eclectic Rubbish Lister
Group: System/Base
Provides: perl = %epoch:%version
Obsoletes: perl < %epoch:%version
Provides: perl-PerlIO = %epoch:%version perl-Storable = %epoch:%version
Obsoletes: perl-PerlIO < %epoch:%version perl-Storable < %epoch:%version
Provides: perl-version = 0.99
Obsoletes: perl-version < 0.99
Provides: perl-Digest-MD5 = 2.55
Obsoletes: perl-Digest-MD5 < 2.55
Provides: perl-Time-HiRes = 1.9741
Obsoletes: perl-Time-HiRes < 1.9741
Provides: perl-MIME-Base64 = 3.15
Obsoletes: perl-MIME-Base64 < 3.15
Provides: perl-IPC-SysV = 2.07
Obsoletes: perl-IPC-SysV < 2.07-alt2

%package devel
Summary: Perl header files and development modules
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release
Provides: perl-Test-Tester = 0.114
Obsoletes: perl-Test-Tester < 0.114
Conflicts: perl-Test-Tester < 0.114
Provides: perl-Test-use-ok = 0.12
Obsoletes: perl-Test-use-ok < 0.12
Conflicts: perl-Test-use-ok < 0.12
Provides: perl-Test2 = 0.000045
Obsoletes: perl-Test2 < 0.000045
Conflicts: perl-Test2 < 0.000045

BuildRequires: libdb4-devel libgdbm-devel
# perl IO-AIO module pass perl link options to configure.
# without those devel libs configure fails.
Requires: libdb4-devel libgdbm-devel

%package pod
Summary: Perl documentation
Group: Development/Documentation
Requires: perl-base = %epoch:%version
Provides: perl-doc = %epoch:%version
BuildArch: noarch

%package threads
Summary: Perl thread modules
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release

%package unicore
Summary: Perl Unicode library
Group: Development/Perl
Requires: perl-Unicode-Normalize = %epoch:%version-%release
BuildArch: noarch

%package DBM
Summary: Perl modules for accessing DBM databases
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release
Provides:  perl-DB_File
Obsoletes: perl-DB_File

%package Unicode-Normalize
Summary: Unicode normalization forms
Group: Development/Perl
Requires: perl-base = %epoch:%version-%release

%description
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications (and what it excels
at) are probably system administration utilities and web programming.
A large proportion of the CGI scripts on the web are written in Perl.

%description base
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications (and what it excels
at) are probably system administration utilities and web programming.
A large proportion of the CGI scripts on the web are written in Perl.

This package provides Perl interpreter and a subset of the standard
library required to perform basic tasks.

%description devel
This package contains Perl header files and development modules.
Most perl packages will need to install perl-devel to build.

%description pod
This package provides standard Perl documentation in Pod format.

%description threads
This package provides Perl modules for thread programming.  The threads
module provides interface to interpreter-based threading implementation
(ithreads).  The threads::shared module enables data sharing between
threads.  Thread::Queue and Thread::Semaphore provide thread-safe
synchronization primitives.

%description unicore
This package provides extended Unicode support for Perl (full support
for Unicode properties in regular expressions, Unicode Character Database,
the Unicode::UCD module, and the charnames pragma).

%description DBM
This package provides Perl modules for accessing DBM databases.
AnyDBM_File provides a framework for multiple DBM implementations
(DB_File, NDBM_File, GDBM_File, and SDBM_File). DBM_Filter allows
filtering DBM keys/values by user-defined code.

%description Unicode-Normalize
This module provides support for normalized forms of Unicode text,
as described in Unicode Standard Annex #15.  With these forms,
equivalent text will have identical binary representations.

%prep
%setup -q
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch51 -p1

# ------ inserted with srpm-spec-inject-patches(1) -------
# BeginPatches(fedora): ------------------------------------
%patch310 -p1
%patch311 -p1
%patch313 -p1
%patch314 -p1
%patch317 -p1
%patch318 -p1
%patch320 -p1
%patch321 -p1
%patch323 -p1
%patch324 -p1
%patch326 -p1
%patch327 -p1
%patch328 -p1
%patch330 -p1
%patch333 -p1
%patch334 -p1
%patch338 -p1
%patch339 -p1
%patch340 -p1
%patch341 -p1
%patch344 -p1
%patch345 -p1
%patch346 -p1
%patch349 -p1
%patch350 -p1
%patch353 -p1
%patch354 -p1
%patch356 -p1
%patch357 -p1
%patch358 -p1
%patch359 -p1
%patch360 -p1
%patch361 -p1
%patch362 -p1
%patch363 -p1
%patch364 -p1
%patch365 -p1
%patch366 -p1
%patch367 -p1
%patch368 -p1
%patch369 -p1
%patch370 -p1
# EndPatches(fedora): --------------------------------------

# .orig files can break some test
# at least t/porting/readme.t :
# Failed test 39 - Maintainers.pl.orig is mentioned in Porting/README.pod at porting/readme.t line 36
find -name '*.orig' -delete

%build
%define ver %(v=%version IFS=.; set $v; echo $1.$2)
%define privlib /usr/share/perl5
%define archlib %_libdir/perl5
%define autolib %archlib/auto
%define site_prefix %_prefix/local
%define site_privlib %site_prefix/share/perl/%ver
%define site_archlib %site_prefix/%_lib/perl/%ver

%ifarch %e2k
# mcst#2279
%add_optflags -D_FORTIFY_SOURCE=0
%endif

sh Configure -ders \
	-Duse64bitint \
	-Dusethreads -Duseithreads -Duselargefiles \
	-Duseshrplib -Dlibperl=libperl-%ver.so \
	-Dcc=gcc -Doptimize="%optflags" -DDEBUGGING=maybe \
	-Dprefix=%_prefix -Dprivlib=%privlib -Darchlib=%archlib \
	-Dvendorprefix=%_prefix -Dvendorlib=%privlib -Dvendorarch=%archlib \
	-Dsiteprefix=%site_prefix -Dsitelib=%site_privlib -Dsitearch=%site_archlib \
	-Dotherlibdirs=/etc/perl5:/usr/lib/perl5/vendor_perl \
	-Dinc_version_list=none \
	-Dpager='%_bindir/less -isR' \
	-Dman1dir=%_man1dir -Dman3dir=none \
	-Dcf_by='%vendor' -Dcf_email='%packager' \
	-Dmyhostname=localhost -Dperladmin=root@localhost

%ifarch %e2k
# before lcc-1.23
cc --version | grep -q '^lcc:1.21' && echo '-lcxa' >> ./ext.libs
%endif

# kill rpath
sed -i 's@ -Wl,-rpath,%archlib/CORE@@g' config.sh [Mm]akefile myconfig

# fixup man1ext and man3ext
sed -i '/man1ext/{s/0/1/}' config.sh [Mm]akefile
sed -i '/man3ext/{s/0/3pm/}' config.sh [Mm]akefile

# make -lperl symlink
ln -snf libperl-%ver.so libperl.so

# build the rest (SMP incompatible)
make

%check
export LD_LIBRARY_PATH=$PWD LD_BIND_NOW=1 PERL_DL_NONLAZY=1
# for perl 5.26.2; hack around t/porting/regen.t
%global build_privlib     %buildroot%{_prefix}/share/perl5
%global build_archlib     %buildroot%{_libdir}/perl5
%global build_bindir      %buildroot%{_bindir}
%global new_perl LD_PRELOAD="%{build_archlib}/CORE/libperl.so" LD_LIBRARY_PATH="%{build_archlib}/CORE" PERL5LIB="%{build_archlib}:%{build_privlib}" %{build_bindir}/perl
%new_perl -I/lib regen/lib_cleanup.pl
pushd t
%new_perl -I../lib porting/customized.t --regen
popd
# end hack
#make test
make test_harness

%install
%make_install install.perl DESTDIR=%buildroot

# use symlinks instead of hardlinks
ln -snf perl%version %buildroot%_bindir/perl
ln -snf perl%version %buildroot%_bindir/perl5

# skeleton
mkdir -p %buildroot%privlib/auto
mkdir -p %buildroot/etc/perl5
mkdir -p %buildroot/usr/lib/perl5/vendor_perl

# relocate libperl
mv %buildroot%archlib/CORE/libperl-%ver.so %buildroot%_libdir/
ln -snf `relative %_libdir/libperl-%ver.so %archlib/CORE/libperl.so` %buildroot%archlib/CORE/libperl.so
ln -snf `relative %_libdir/libperl-%ver.so %archlib/CORE/libperl-%ver.so` %buildroot%archlib/CORE/libperl-%ver.so

# relocate Config.pod and POSIX.pod
mv %buildroot{%archlib,%privlib}/Config.pod
mv %buildroot{%archlib,%privlib}/POSIX.pod

# cleanup modules which we package separately
rm -r %buildroot%privlib/Archive/Tar* %buildroot%_bindir/ptar*
rm -r %buildroot%privlib/autodie* %buildroot%privlib/Fatal.pm
rm -r %buildroot%privlib/Attribute/Handlers*
rm %buildroot%privlib/B/Debug.pm
rm -r %buildroot%privlib/CPAN* %buildroot%privlib/App/Cpan.pm %buildroot%_bindir/cpan*
rm -r %buildroot{%privlib,%archlib,%autolib}/Compress
rm %buildroot%privlib/Devel/SelfStubber.pm
rm -r %buildroot{%archlib,%autolib}/Digest/SHA* %buildroot%_bindir/shasum
rm -r %buildroot{%privlib,%archlib,%autolib}/Encode*
rm %buildroot%archlib/encoding.pm %buildroot%_bindir/{enc2xs,encguess,piconv}
rm %buildroot%privlib/encoding/warnings.pm
rm %buildroot%privlib/experimental.pm
rm -r %buildroot%privlib/ExtUtils/CBuilder*
rm -r %buildroot%privlib/Filter*
rm %buildroot%privlib/File/Fetch.pm
rm -r %buildroot{%archlib,%autolib}/Filter*
rm %buildroot%privlib/HTTP/Tiny.pm
rm -r %buildroot%privlib/JSON* %buildroot%_bindir/json*
rm -r %buildroot%privlib/I18N/LangTags*
rm %buildroot%privlib/I18N/Collate.pm
rm -r %buildroot%privlib/IO/{Compress,Uncompress} %buildroot%privlib/File/GlobMapper.pm
rm %buildroot%privlib/IO/Socket/IP.pm
rm -r %buildroot%privlib/IO/Zlib.pm
rm %buildroot%privlib/IPC/Cmd.pm
#rm -r %buildroot{%archlib,%autolib}/IPC/SysV* %buildroot%archlib/IPC/{Msg,Semaphore,SharedMem}.pm
find %buildroot%privlib/Net/* -not -name '*ent.*' -print -delete
rm %buildroot%_bindir/libnetcfg
rm -r %buildroot%privlib/Locale
rm -r %buildroot{%privlib,%archlib,%autolib}/Math/Big* %buildroot%privlib/big*.pm
rm -r %buildroot%privlib/Math/{Complex,Trig}.pm
rm -r %buildroot%privlib/Memoize*
rm -r %buildroot%privlib/Module/Load*
rm -r %buildroot%privlib/Module/CoreList* %buildroot%_bindir/corelist
rm %buildroot%privlib/Module/Metadata.pm
rm %buildroot%privlib/NEXT.pm
rm %buildroot%privlib/Params/Check.pm
rm %buildroot%privlib/Parse/CPAN/Meta.pm
rm %buildroot%privlib/Perl/OSType.pm
rm %buildroot%privlib/Pod/Escapes.pm
rm %buildroot%privlib/Pod/{Checker,Find,InputObjects,ParseUtils,Parser,PlainText,Select,Usage}.pm
rm %buildroot%_bindir/{pod2usage,podchecker,podselect}
rm -r %buildroot%privlib/Pod/{Man,ParseLink,Text}*
rm %buildroot%_bindir/{pod2man,pod2text}
rm -r %buildroot%privlib/Pod/Perldoc* %buildroot%_bindir/perldoc
rm -r %buildroot%privlib/Pod/Simple*
rm %buildroot%privlib/Term/ANSIColor.pm
rm %buildroot%privlib/Term/Cap.pm
rm %buildroot%privlib/Term/ReadLine.pm
rm -r %buildroot%privlib/Text/Balanced*
rm %buildroot%privlib/Tie/File.pm
rm %buildroot%privlib/Tie/RefHash.pm
rm -r %buildroot{%archlib,%autolib}/Time/Piece* %buildroot%archlib/Time/Seconds.pm
rm -r %buildroot{%privlib,%archlib,%autolib}/Unicode/Collate*

rm %buildroot%_bindir/zipdetails
rm %buildroot%privlib/perlfaq.pm

# cleanup Perl4-CoreLibs
grep -lZ '^warn "Legacy library' %buildroot%privlib/*.pl |xargs -r0 rm -fv --

# further cleanup #"
rm %buildroot%archlib/File/Spec/{Cygwin,Epoc,Mac,OS2,VMS,Win32}.pm
rm %buildroot%privlib/ExtUtils/MM_{AIX,BeOS,Cygwin,Darwin,DOS,MacOS,NW5,OS2,QNX,UWIN,VMS,VOS,Win32,Win95}.pm
rm %buildroot%_bindir/perlivp

mkdir -p %buildroot%_rpmlibdir
cat <<EOF >%buildroot%_rpmlibdir/perl-base-files.req.list
# perl-base dirlist for %_rpmlibdir/files.req
/usr/lib/perl5	perl-base
/usr/lib64/perl5	perl-base
/usr/share/perl5	perl-base
/etc/perl5	perl-base
/usr/lib/perl5/vendor_perl	perl-base
EOF

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/substitute.d/
echo perl >%buildroot%_sysconfdir/buildreqs/packages/substitute.d/perl-base

%files	base
%doc	Artistic AUTHORS README
	%_bindir/perl
	%_bindir/perl5*
	%_libdir/libperl-%ver.so
# skeleton
%dir	%privlib
%dir	%privlib/auto
%dir	%archlib
%dir	%autolib
%dir	/etc/perl5
%dir	/usr/lib/perl5/vendor_perl
%config %_rpmlibdir/perl-base-files.req.list
%config %_sysconfdir/buildreqs/packages/substitute.d/perl-base
# pragma
	%archlib/arybase.pm
	%autolib/arybase
	%archlib/attributes.pm
	%autolib/attributes
	%privlib/autouse.pm
	%privlib/base.pm
	%privlib/bytes*
	%privlib/constant.pm
	%privlib/deprecate.pm
	%privlib/feature.pm
	%privlib/fields.pm
	%privlib/filetest.pm
	%privlib/if.pm
	%privlib/integer.pm
	%privlib/less.pm
	%archlib/lib.pm
	%privlib/locale.pm
	%privlib/meta_notation.pm
	%archlib/mro.pm
	%autolib/mro
	%privlib/open.pm
	%archlib/ops.pm
	%privlib/overload*
	%archlib/re.pm
	%autolib/re
	%privlib/sigtrap.pm
	%privlib/sort.pm
	%privlib/strict.pm
	%privlib/subs.pm
	%privlib/utf8*
	%privlib/vars.pm
	%privlib/version.pm
%doc	%privlib/version.pod
%dir	%privlib/version
	%privlib/version/regex.pm
#	%privlib/version/vpp.pm
%doc	%privlib/version/Internals.pod
	%privlib/vmsish.pm
	%privlib/warnings*
# module loaders
	%privlib/AutoLoader.pm
	%archlib/DynaLoader.pm
	%privlib/SelfLoader.pm
	%privlib/XSLoader.pm
# data utils
%dir	%archlib/Hash
	%archlib/Hash/Util*
%dir	%autolib/Hash
	%autolib/Hash/Util*
%dir	%archlib/List
	%archlib/List/Util*
%dir	%autolib/List
	%autolib/List/Util*
%dir	%archlib/Scalar
	%archlib/Scalar/Util*
%dir	%archlib/Sub
	%archlib/Sub/Util*
# initial unicode support
%dir	%privlib/unicore
	%privlib/unicore/Heavy.pl
%dir	%privlib/unicore/To
	%privlib/unicore/To/Digit.pl
	%privlib/unicore/To/Fold.pl
	%privlib/unicore/To/Lower.pl
	%privlib/unicore/To/Title.pl
	%privlib/unicore/To/Upper.pl
	%privlib/unicore/To/Cf.pl
	%privlib/unicore/To/Lc.pl
	%privlib/unicore/To/Tc.pl
	%privlib/unicore/To/Uc.pl
%dir	%privlib/unicore/lib
%dir	%privlib/unicore/lib/Alpha
	%privlib/unicore/lib/Alpha/Y.pl
%dir	%privlib/unicore/lib/Cased
	%privlib/unicore/lib/Cased/Y.pl
%dir	%privlib/unicore/lib/Gc
	%privlib/unicore/lib/Gc/Nd.pl
	%privlib/unicore/lib/Gc/P.pl
%dir	%privlib/unicore/lib/Hex
	%privlib/unicore/lib/Hex/Y.pl
%dir	%privlib/unicore/lib/Lower
	%privlib/unicore/lib/Lower/Y.pl
%dir	%privlib/unicore/lib/Nt
	%privlib/unicore/lib/Nt/Di.pl
	%privlib/unicore/lib/Nt/Nu.pl
%dir	%privlib/unicore/lib/Perl
	%privlib/unicore/lib/Perl/_PerlIDS.pl
	%privlib/unicore/lib/Perl/Alnum.pl
	%privlib/unicore/lib/Perl/Blank.pl
	%privlib/unicore/lib/Perl/Graph.pl
	%privlib/unicore/lib/Perl/Print.pl
	%privlib/unicore/lib/Perl/Word.pl
%dir	%privlib/unicore/lib/Upper
	%privlib/unicore/lib/Upper/Y.pl
# modules
	%privlib/Carp*
	%archlib/Config.pm
	%archlib/Config_heavy.pl
	%archlib/Config_git.pl
%dir	%privlib/Config
	%privlib/Config/Extensions.pm
%dir	%privlib/Config/Perl
	%privlib/Config/Perl/V.pm
%dir	%privlib/Class
	%privlib/Class/Struct.pm
	%archlib/Cwd.pm
	%autolib/Cwd
%dir	%archlib/Data
	%archlib/Data/Dumper.pm
%dir	%autolib/Data
	%autolib/Data/Dumper
	%privlib/Digest.pm
%dir	%privlib/Digest
	%privlib/Digest/base.pm
	%privlib/Digest/file.pm
%dir	%archlib/Digest
	%archlib/Digest/MD5.pm
%dir	%autolib/Digest
	%autolib/Digest/MD5
	%privlib/English.pm
	%archlib/Errno.pm
	%privlib/Exporter*
	%archlib/Fcntl.pm
	%autolib/Fcntl
%dir	%privlib/File
	%privlib/File/Basename.pm
	%privlib/File/Compare.pm
	%privlib/File/Copy.pm
	%privlib/File/Find.pm
	%privlib/File/Path.pm
	%privlib/File/stat.pm
	%privlib/File/Temp.pm
	%privlib/FileHandle.pm
%dir	%archlib/File
	%archlib/File/Glob.pm
	%archlib/File/DosGlob.pm
%dir	%autolib/File
	%autolib/File/Glob
	%autolib/File/DosGlob
	%archlib/File/Spec*
	%privlib/FindBin.pm
%dir	%privlib/Getopt
	%privlib/Getopt/Long.pm
	%privlib/Getopt/Std.pm
	%archlib/IO.pm
%dir	%archlib/IO
	%archlib/IO/Dir.pm
	%archlib/IO/File.pm
	%archlib/IO/Handle.pm
	%archlib/IO/Pipe.pm
	%archlib/IO/Poll.pm
	%archlib/IO/Seekable.pm
	%archlib/IO/Select.pm
	%archlib/IO/Socket*
%dir	%autolib/IO
	%autolib/IO/IO.so
%dir	%privlib/IPC
	%privlib/IPC/Open2.pm
	%privlib/IPC/Open3.pm
%dir	%archlib/MIME
	%archlib/MIME/Base64.pm
	%archlib/MIME/QuotedPrint.pm
%dir	%autolib/MIME
	%autolib/MIME/Base64
	%privlib/PerlIO*
	%archlib/PerlIO*
	%autolib/PerlIO*
	%archlib/POSIX.pm
	%autolib/POSIX
	%privlib/SelectSaver.pm
	%archlib/Socket.pm
	%autolib/Socket
	%archlib/Storable.pm
%dir	%archlib/Storable
	%archlib/Storable/Limit.pm
	%autolib/Storable
	%privlib/Symbol.pm
%dir	%archlib/Sys
	%archlib/Sys/Hostname.pm
	%archlib/Sys/Syslog.pm
%dir	%autolib/Sys
	%autolib/Sys/Hostname
	%autolib/Sys/Syslog
%dir	%privlib/Text
	%privlib/Text/Abbrev.pm
	%privlib/Text/ParseWords.pm
	%privlib/Text/Tabs.pm
	%privlib/Text/Wrap.pm
%dir	%privlib/Tie
	%privlib/Tie/Array.pm
	%privlib/Tie/Handle.pm
	%privlib/Tie/Hash*
%dir	%archlib/Tie
	%archlib/Tie/Hash*
%dir	%autolib/Tie
	%autolib/Tie/Hash*
	%privlib/Tie/Memoize.pm
	%privlib/Tie/Scalar.pm
	%privlib/Tie/StdHandle.pm
	%privlib/Tie/SubstrHash.pm
%dir	%privlib/Time
	%privlib/Time/gmtime.pm
	%privlib/Time/localtime.pm
	%privlib/Time/tm.pm
	%privlib/Time/Local.pm
%dir	%archlib/Time
	%archlib/Time/HiRes.pm
%dir	%autolib/Time
	%autolib/Time/HiRes
	%privlib/UNIVERSAL.pm
# required for perl.req and perl.prov
	%archlib/B.pm
%dir	%autolib/B
	%autolib/B/B.so
	%archlib/O.pm
	%archlib/Opcode.pm
	%autolib/Opcode
	%privlib/Safe.pm
# IPC-SysV: required for Test-Simple in perl-devel
%dir	%archlib/IPC
	%archlib/IPC/Msg.pm
	%archlib/IPC/Semaphore.pm
	%archlib/IPC/SharedMem.pm
	%archlib/IPC/SysV.pm
%dir	%autolib/IPC
%dir	%autolib/IPC/SysV
	%autolib/IPC/SysV/SysV.so
# rarely used but part of perl
	%privlib/Benchmark.pm
%doc	%privlib/CORE.pod
	%privlib/DirHandle.pm
	%privlib/Env.pm
	%privlib/FileCache.pm
%dir	%archlib/I18N
	%archlib/I18N/Langinfo.pm
%dir	%autolib/I18N
	%autolib/I18N/Langinfo
%dir	%privlib/Net
	%privlib/Net/*ent.pm
%dir	%privlib/Pod
	%privlib/Pod/Functions.pm
%dir	%privlib/Search
	%privlib/Search/Dict.pm
%dir	%privlib/Term
	%privlib/Term/Complete.pm
%dir	%privlib/User
	%privlib/User/*ent.pm
# in separate package perl-parent; required in buildroot for tests
%exclude %privlib/parent.pm

%files	devel
	%_bindir/h2xs
	%_bindir/instmodsh
	%_bindir/perlbug
	%_bindir/perlthanks
	%_bindir/prove
	%_bindir/splain
	%_bindir/xsubpp
# perl4-compat scripts
	%_bindir/h2ph
	%_bindir/pl2pm
	%privlib/blib.pm
	%privlib/diagnostics.pm
	%privlib/dumpvar.pl
	%privlib/perl5db.pl
	%privlib/Dumpvalue.pm
%dir	%archlib/CORE
	%archlib/CORE/*.h
	%archlib/CORE/libperl*.so
# perl-devel modules
	%privlib/AutoSplit.pm
	%privlib/B
	%archlib/B
	%autolib/B
%exclude %autolib/B/B.so
	%privlib/DB.pm
%dir	%archlib/Devel
	%archlib/Devel/Peek.pm
	%archlib/Devel/PPPort.pm
%dir	%autolib/Devel
	%autolib/Devel/Peek
	# explicitly ignored in installperl
	#%autolib/Devel/PPPort
%dir	%privlib/ExtUtils
	%privlib/ExtUtils/Command*
	%privlib/ExtUtils/Constant*
	%privlib/ExtUtils/Embed.pm
	%privlib/ExtUtils/Install.pm
	%privlib/ExtUtils/Installed.pm
	%privlib/ExtUtils/Liblist*
	%privlib/ExtUtils/MakeMaker.pm
%dir	%privlib/ExtUtils/MakeMaker
	%privlib/ExtUtils/MakeMaker/*.pm
	# explicitly ignored in installperl; returned by tmp hack (Patch18)
%dir	%privlib/ExtUtils/MakeMaker/version
	%privlib/ExtUtils/MakeMaker/version/*.pm
%doc	%privlib/ExtUtils/MakeMaker/*.pod
	%privlib/ExtUtils/MM.pm
	%privlib/ExtUtils/MM_Any.pm
	%privlib/ExtUtils/MM_Unix.pm
	%privlib/ExtUtils/MY.pm
	%privlib/ExtUtils/MANIFEST.SKIP
	%privlib/ExtUtils/Manifest.pm
	%privlib/ExtUtils/Miniperl.pm
	%privlib/ExtUtils/Mkbootstrap.pm
	%privlib/ExtUtils/Mksymlists.pm
	%privlib/ExtUtils/Packlist.pm
%dir	%privlib/ExtUtils/ParseXS
	%privlib/ExtUtils/ParseXS/*.pm
	%privlib/ExtUtils/ParseXS.pm
%doc	%privlib/ExtUtils/ParseXS.pod
%dir	%privlib/ExtUtils/Typemaps
	%privlib/ExtUtils/Typemaps/*.pm
	%privlib/ExtUtils/Typemaps.pm
	%privlib/ExtUtils/testlib.pm
	%privlib/ExtUtils/typemap
	%privlib/ExtUtils/xsubpp
%dir	%privlib/Pod
	%privlib/Pod/Html.pm
	%_bindir/pod2html
	%privlib/Test.pm
%dir	%privlib/Test
%doc	%privlib/Test/Tutorial.pod
%dir	%privlib/pod
# perldiag.pod is NOT a doc; it used by diagnostics.pm
	%privlib/pod/perldiag.pod
# Test-Simple pieces
	%privlib/ok.pm
	%privlib/Test/Builder*
	%privlib/Test/More.pm
	%privlib/Test/Simple.pm
%dir	%privlib/Test/use
	%privlib/Test/use/ok.pm
	%privlib/Test/Tester.pm
%dir	%privlib/Test/Tester
	%privlib/Test/Tester/Capture.pm
	%privlib/Test/Tester/CaptureRunner.pm
	%privlib/Test/Tester/Delegate.pm
	%privlib/Test2.pm
%dir	%privlib/Test2
	%privlib/Test2/API.pm
%dir	%privlib/Test2/API
	%privlib/Test2/API/Breakage.pm
	%privlib/Test2/API/Context.pm
	%privlib/Test2/API/Instance.pm
	%privlib/Test2/API/Stack.pm
	%privlib/Test2/Event.pm
%dir	%privlib/Test2/Event
	%privlib/Test2/Event/Bail.pm
	%privlib/Test2/Event/Diag.pm
	%privlib/Test2/Event/Encoding.pm
	%privlib/Test2/Event/Exception.pm
	%privlib/Test2/Event/Fail.pm
	%privlib/Test2/Event/Generic.pm
	%privlib/Test2/Event/Note.pm
	%privlib/Test2/Event/Ok.pm
	%privlib/Test2/Event/Pass.pm
	%privlib/Test2/Event/Plan.pm
	%privlib/Test2/Event/Skip.pm
	%privlib/Test2/Event/Subtest.pm
%dir	%privlib/Test2/Event/TAP
	%privlib/Test2/Event/TAP/Version.pm
	%privlib/Test2/Event/V2.pm
	%privlib/Test2/Event/Waiting.pm
	%privlib/Test2/EventFacet.pm
%dir	%privlib/Test2/EventFacet
	%privlib/Test2/EventFacet/About.pm
	%privlib/Test2/EventFacet/Amnesty.pm
	%privlib/Test2/EventFacet/Assert.pm
	%privlib/Test2/EventFacet/Control.pm
	%privlib/Test2/EventFacet/Error.pm
	%privlib/Test2/EventFacet/Hub.pm
	%privlib/Test2/EventFacet/Info.pm
	%privlib/Test2/EventFacet/Meta.pm
	%privlib/Test2/EventFacet/Parent.pm
	%privlib/Test2/EventFacet/Plan.pm
	%privlib/Test2/EventFacet/Render.pm
	%privlib/Test2/EventFacet/Trace.pm
	%privlib/Test2/Formatter.pm
%dir	%privlib/Test2/Formatter
	%privlib/Test2/Formatter/TAP.pm
	%privlib/Test2/Hub.pm
%dir	%privlib/Test2/Hub
	%privlib/Test2/Hub/Interceptor.pm
%dir	%privlib/Test2/Hub/Interceptor
	%privlib/Test2/Hub/Interceptor/Terminator.pm
	%privlib/Test2/Hub/Subtest.pm
	%privlib/Test2/IPC.pm
%dir	%privlib/Test2/IPC
	%privlib/Test2/IPC/Driver.pm
%dir	%privlib/Test2/IPC/Driver
	%privlib/Test2/IPC/Driver/Files.pm
%dir	%privlib/Test2/Tools
	%privlib/Test2/Tools/Tiny.pm
	%privlib/Test2/Transition.pod
	%privlib/Test2/Util.pm
%dir	%privlib/Test2/Util
	%privlib/Test2/Util/ExternalMeta.pm
	%privlib/Test2/Util/Facets2Legacy.pm
	%privlib/Test2/Util/HashBase.pm
	%privlib/Test2/Util/Trace.pm
# Test-Harness pieces
%dir	%privlib/App
	%privlib/App/Prove*
	%privlib/TAP
	%privlib/Test/Harness.pm

%files	pod
%dir	%privlib/pod
%doc	%privlib/pod/perl*.pod
%exclude %privlib/pod/perldiag.pod
%exclude %privlib/pod/perldbmfilter.pod
%doc	%privlib/Config.pod
%doc	%privlib/POSIX.pod
%doc	%privlib/Internals.pod

%files	threads
	%privlib/Thread*
	%archlib/threads*
	%autolib/threads

%files	unicore
	%privlib/charnames.pm
	%privlib/_charnames.pm
%dir	%privlib/Unicode
	%privlib/Unicode/UCD.pm
%dir	%privlib/unicore
	%privlib/unicore/version
	%privlib/unicore/Name.pm
	%privlib/unicore/Name.pl
	%privlib/unicore/UCD.pl
	%privlib/unicore/lib/

%exclude %privlib/unicore/lib/Alpha/Y.pl
%exclude %privlib/unicore/lib/Cased/Y.pl
%exclude %privlib/unicore/lib/Gc/Nd.pl
%exclude %privlib/unicore/lib/Gc/P.pl
%exclude %privlib/unicore/lib/Hex/Y.pl
%exclude %privlib/unicore/lib/Lower/Y.pl
%exclude %privlib/unicore/lib/Nt/Di.pl
%exclude %privlib/unicore/lib/Nt/Nu.pl
%exclude %privlib/unicore/lib/Perl/_PerlIDS.pl
%exclude %privlib/unicore/lib/Perl/Alnum.pl
%exclude %privlib/unicore/lib/Perl/Blank.pl
%exclude %privlib/unicore/lib/Perl/Graph.pl
%exclude %privlib/unicore/lib/Perl/Print.pl
%exclude %privlib/unicore/lib/Perl/Word.pl
%exclude %privlib/unicore/lib/Upper/Y.pl
	%privlib/unicore/To/
%exclude %privlib/unicore/To/Digit.pl
%exclude %privlib/unicore/To/Fold.pl
%exclude %privlib/unicore/To/Lower.pl
%exclude %privlib/unicore/To/Title.pl
%exclude %privlib/unicore/To/Upper.pl
%exclude %privlib/unicore/To/Cf.pl
%exclude %privlib/unicore/To/Lc.pl
%exclude %privlib/unicore/To/Tc.pl
%exclude %privlib/unicore/To/Uc.pl
# required to build Unicode::Normalize
	%privlib/unicore/CombiningClass.pl
	%privlib/unicore/Decomposition.pl
# required for Unicode::UCD
	%privlib/unicore/Blocks.txt
	%privlib/unicore/SpecialCasing.txt
# not required
	%privlib/unicore/NamedSequences.txt

%files	DBM
	%privlib/AnyDBM_File.pm
	%archlib/DB_File.pm
	%autolib/DB_File
	%archlib/NDBM_File.pm
	%autolib/NDBM_File
	%archlib/GDBM_File.pm
	%autolib/GDBM_File
	%archlib/SDBM_File.pm
	%autolib/SDBM_File
	%privlib/DBM_Filter*
%dir	%privlib/pod
%doc	%privlib/pod/perldbmfilter.pod

%files	Unicode-Normalize
%dir	%archlib/Unicode
	%archlib/Unicode/Normalize.pm
	%autolib/Unicode

%changelog
* Thu Jan 23 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1:5.28.2-alt2
- Licence tag fixed
- build in year 2020 fixed (Time-Local)
- 'trust mode' implemented by mcpain@

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:5.28.2-alt1
- 5.28.1 -> 5.28.2

* Thu Apr 04 2019 Michael Shigorin <mike@altlinux.org> 1:5.28.1-alt2
- E2K: fix build with lcc-1.23

* Fri Jan 04 2019 Igor Vlasenko <viy@altlinux.ru> 1:5.28.1-alt1
- 5.26.2 -> 5.28.1

* Tue Aug 21 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.26.2-alt2
- added Requires: libdb4-devel libgdbm-devel to support perl-IO-AIO

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:5.26.2-alt1
- 5.26.1 -> 5.26.2

* Thu Feb 01 2018 Dmitry V. Levin <ldv@altlinux.org> 1:5.26.1-alt4
- Rebuilt with new glibc (without -lnsl).

* Fri Dec 29 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.26.1-alt3
- cpan update Test-Simple-1.302073 to Test-Simple-1.302120

* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.26.1-alt2
- Rebuilt with new glibc.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.26.1-alt1
- 5.24.3 -> 5.26.1
- build with -Duse64bitint
- include IPC-SysV

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.24.3-alt2
- added patch21 from Oleg Solovyov

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.24.3-alt1
- 5.24.2 -> 5.24.3

* Wed Aug 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.24.2-alt1
- 5.24.1 -> 5.24.2 (CVE-2016-1238)

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.24.1-alt1
- 5.22.3 -> 5.24.1
- build with -Duse64bitint on %%{ix86}

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:5.22.3-alt1
- 5.22.2 -> 5.22.3

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:5.22.2-alt2
- cpan-update-Scalar-List-Utils-1.41-to-Scalar-List-Utils-1.41-1.46

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:5.22.2-alt1
- 5.22.1 -> 5.22.2

* Sun Apr 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:5.22.1-alt2
- added buildreqs substitute.d perl-base -> perl

* Wed Dec 16 2015 Igor Vlasenko <viy@altlinux.ru> 1:5.22.1-alt1
- 5.22.0 -> 5.22.1

* Sun Nov 29 2015 Igor Vlasenko <viy@altlinux.ru> 1:5.22.0-alt2
- added Provides/Conflicts on perl-Test-use-ok (now in perl-devel)

* Tue Nov 10 2015 Igor Vlasenko <viy@altlinux.ru> 1:5.22.0-alt1
- 5.20.3 -> 5.22.0

* Wed Oct 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:5.20.3-alt1
- Updated to 5.20.3.

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.20.1-alt2
- cpan update: Socket-2.013 to Socket-2.016

* Fri Nov 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.20.1-alt1
- 5.18.2 -> 5.20.1

* Wed Jan 08 2014 Vladimir Lettiev <crux@altlinux.ru> 1:5.18.2-alt1
- 5.18.1 -> 5.18.2

* Tue Aug 20 2013 Vladimir Lettiev <crux@altlinux.ru> 1:5.18.1-alt1
- 5.16.3 -> 5.18.1
- Version::Requirements removed from core
- File::DosGlob moved to archlib
- Updated Text::Tabs to 2013.0523

* Tue Mar 12 2013 Vladimir Lettiev <crux@altlinux.ru> 1:5.16.3-alt1
- 5.16.2 -> 5.16.3
- Fixed CVE-2013-1667: memory exhaustion with arbitrary hash keys

* Tue Nov 06 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.16.2-alt1
- 5.16.1 -> 5.16.2

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1:5.16.1-alt3
- Storable.pm: restored patch to avoid early dependency on Log::Agent
- ExtUtils/MM_Any.pm: disabled CPAN::Meta under rpm
- moved unicore/lib/Perl/_PerlIDS.pl to perl-base, for constant.pm
- moved unicore/To/Tc.pl to perl-base, required for ucfirst()

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.16.1-alt2
- unicore database files moved to perl-base:
  * unicore/To/Cf.pl (format control characters)
  * unicore/To/Lc.pl (lowercase)
  * unicore/To/Uc.pl (uppercase)

* Thu Aug 23 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.16.1-alt1
- 5.14.2 -> 5.16.1
- Devel::DProf, Shell moved from core
- added new arybase pragma

* Fri Jan 20 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.14.2-alt4
- updated Digest 1.16 -> 1.17 (fixed CVE-2011-3597)

* Sat Jan 14 2012 Vladimir Lettiev <crux@altlinux.ru> 1:5.14.2-alt3
- updated Safe.pm 2.29 -> 2.30 (closes: #26802)

* Wed Nov 02 2011 Alexey Tourbin <at@altlinux.ru> 1:5.14.2-alt2
- moved unicore/Cased/Y.pl to perl-base

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1:5.14.2-alt1
- 5.12.4 -> 5.14.2
- perl-pod: packaged OS-specific docs (e.g. perlaix.pod) as they are
  referenced in perl.pod and perltoc.pod
- packaged perl-Unicode-Normalize subpackage as it is now required in
  perl-unicore by Unicode::UCD
- perl4-compat is replaced by separate CPAN distribution Perl4-CoreLibs
- new modules packaged as separate CPAN distributions: HTTP-Tiny,
  Perl-OSType, Module-Metadata, Version-Requirements, JSON-PP
- older modules packaged as separate CPAN distributions: File-CheckTree,
  I18N-Collate, Devel-DProf, Devel-SelfStubber
- another coming of static_XS.patch

* Mon Sep 12 2011 Dmitry V. Levin <ldv@altlinux.org> 1:5.12.4-alt2
- Fixed regression on x86-64 introduced in 5.12.4 (closes: #26249).

* Sat Sep 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1:5.12.4-alt1
- 5.12.3 -> 5.12.4
- Updated MIME::Base64 3.08 -> 3.13 (Closes: #25646)

* Mon Apr 18 2011 Dmitry V. Levin <ldv@altlinux.org> 1:5.12.3-alt4
- Reverted the change in XS functions prototypes introduced in previous
  release, due to massive build breakage (closes: #23793).

* Tue Apr 05 2011 Alexey Tourbin <at@altlinux.ru> 1:5.12.3-alt3
- overhauled static_XS.patch - all XS functions are now static by default
- updated ExtUtil-ParseXS to CPAN version 2.2206
- updated Test-Simple to CPAN version 0.98
- deprecate.pm: disabled warning for vendor directories

* Fri Feb 11 2011 Alexey Tourbin <at@altlinux.ru> 1:5.12.3-alt2
- rebuilt for debuginfo
- revived static_XS.patch - auto-generated XS functions static by default

* Mon Jan 24 2011 Alexey Tourbin <at@altlinux.ru> 1:5.12.3-alt1
- 5.12.2 -> 5.12.3
- merged perl-PerlIO and perl-Storable into perl-base
- moved some files from unicore library to perl-base (closes: #24733)
- moved Config.pod and POSIX.pod from perl-devel to perl-pod

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1:5.12.2-alt02
- redefined default sitelib paths

* Sun Nov 14 2010 Vladimir Lettiev <crux@altlinux.ru> 1:5.12.2-alt01
- re.so moved from perl-devel to perl-base (Closes: #24561)

* Thu Sep 16 2010 Alexey Tourbin <at@altlinux.ru> 1:5.12.2-alt00
- packaged from scratch
