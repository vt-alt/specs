%define includedir %_includedir/%name

Name: p7zip
Version: 16.02
Release: alt5

Summary: 7zip unofficial port - a file-archiver with highest compression ratio
License: Freely distributable
Group: Archiving/Compression

Url: http://p7zip.sourceforge.net/
Source: %{name}_%{version}_src_all.tar
# debian patches
Patch1: 12-CVE-2016-9296.patch
Patch2: 13-CVE-2017-17969.patch
Patch3: 06-CVE-2018-5996.patch
Patch4: CVE-2018-10115.patch

# Automatically added by buildreq on Sat Oct 08 2011
# optimized out: libstdc++-devel
BuildRequires: gcc-c++
%ifarch %ix86
BuildRequires: nasm
%endif
%ifarch x86_64
BuildRequires: yasm
%endif

%description
p7zip is a port of 7-Zip for Unix. 7-Zip is a file archiver
with a very high compression ratio.

%package standalone
Summary: Standalone p7zip executable without plugins
Group: Archiving/Compression
License: LGPLv2.1+
Requires: p7zip

%description standalone
p7zip is a port of 7-Zip for Unix. 7-Zip is a file archiver
with a very high compression ratio.

This package contains standalone version of p7zip.
It handles less archive formats than plugin capable version.

%package devel
Summary: Development package of p7zip that includes the header files
Group: Development/C
License: Public domain
BuildArch: noarch

Requires: %name = %EVR

%description devel
The devel package contains the p7zip include files.

%prep
%setup -n p7zip_%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%ifarch %e2k
# _LITTLE_ENDIAN gets defined but not checked for
%add_optflags -D__LITTLE_ENDIAN__
# -ffast is faster but its -floop-apb-conditional-loads is potentially dangerous
%add_optflags -fcache-opt
%endif

# Make p7zip looks for plugins in fixed directory. Upstream behavior was to
# look in current directory by default (when environment variable P7ZIP_HOME_DIR
# is not set)
find . -name '*.cpp' -exec \
subst 's@getenv("P7ZIP_HOME_DIR")@"%_libdir/p7zip/"@g' {} \;

%ifarch %ix86
cp -f makefile.linux_x86_asm_gcc_4.X makefile.machine
%endif
%ifarch x86_64
cp -f makefile.linux_amd64_asm makefile.machine
%endif

# NB: 'all' is not default target in this makefile
%make_build OPTFLAGS="%optflags" all2

# NB: Someday I probably should build and package 7zG (7z GUI), but for now
# this GUI is far from useful.

%install
./install.sh %_bindir %_libdir/p7zip %_mandir %_docdir/%name-%version %buildroot
# Install script put shell wrappers in /usr/bin/ instead of executables.
# We don't want this, see comments to inline patch above to get idea of our way.
mv -f %buildroot%_libdir/p7zip/{7z,7za} %buildroot%_bindir/

# Install C/*.h files
mkdir -p %buildroot%includedir
find C -maxdepth 1 -mindepth 1 -name '*.h' -a -not \( -name Threads.h -o -name LzFindMt.h -o -name MtCoder.h \) -print0 | \
xargs -0 install -pm644 -t %buildroot%includedir/

%files
%doc README ChangeLog DOC
%_bindir/7z
%dir %_libdir/p7zip
%_libdir/p7zip/*.so
%_libdir/p7zip/*.sfx
%_libdir/p7zip/Codecs
%_man1dir/7z.*
%exclude %_man1dir/7zr.*

%files standalone
%_bindir/7za
%_man1dir/7za.*

%files devel
%includedir

%changelog
* Thu Apr 23 2020 Andrey Cherepanov <cas@altlinux.org> 16.02-alt5
- build with asssembler code (ex. for benchmarking AES256CBC:2)

* Sun Nov 04 2018 Michael Shigorin <mike@altlinux.org> 16.02-alt4
- E2K: fix FTBFS; tune optflags a bit

* Sun Nov 04 2018 Michael Shigorin <mike@altlinux.org> 16.02-alt3
- applied debian security patches
  (Fixes: CVE-2016-9296, CVE-2017-17969, CVE-2018-5996, CVE-2018-10115)
- avoid tarball compression
- minor spec cleanup

* Tue Jan 03 2017 Aleksey Avdeev <solo@altlinux.org> 16.02-alt2
- Add devel subpackage

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 16.02-alt1
- Autobuild version bump to 16.02

* Sun Jan 03 2016 Fr. Br. George <george@altlinux.ru> 15.09-alt1
- Autobuild version bump to 15.09

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 9.20.1-alt1
- 9.20.1
- minor spec cleanup

* Mon Mar 14 2011 Victor Forsiuk <force@altlinux.org> 9.20-alt1
- 9.20

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 9.13-alt1
- 9.13

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 9.04-alt1
- 9.04

* Sun Feb 15 2009 Victor Forsyuk <force@altlinux.org> 4.65-alt1
- 4.65

* Mon Jun 09 2008 Victor Forsyuk <force@altlinux.org> 4.58-alt1
- 4.58

* Mon Dec 17 2007 Victor Forsyuk <force@altlinux.org> 4.57-alt1
- 4.57

* Mon Sep 17 2007 Victor Forsyuk <force@altlinux.org> 4.55-alt1
- 4.55
- Patch to make p7zip always look in specified directory for plugins
  (codecs and sfx stubs).
- Apply %%optflags.
- Build with SFX archives support.
- Build "7z with plugins" as main package instead of 7za. Package 7za
  as p7zip-standalone.

* Thu May 24 2007 Victor Forsyuk <force@altlinux.org> 4.45-alt1
- 4.45

* Tue Sep 26 2006 Andrey Semenov <mitrofan@altlinux.ru> 4.43-alt1
- 4.43

* Tue May 30 2006 Andrey Semenov <mitrofan@altlinux.ru> 4.42-alt1
- 4.42

* Wed Apr 19 2006 Andrey Semenov <mitrofan@altlinux.ru> 4.39-alt1
- 4.39

* Sat Feb 11 2006 Andrey Semenov <mitrofan@altlinux.ru> 4.33-alt1
- 4.33

* Mon Nov 28 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.30-alt1
- new version

* Wed Oct 12 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.29-alt1
- 4.29

* Sat Sep 24 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.27-alt1
- 4.27

* Thu Sep 15 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.20-alt2
- add man pages

* Mon Jun 06 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.20-alt1
- release version

* Fri May 13 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.18-alt1
- 4.18

* Fri Apr 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.16-alt1
- 4.16

* Wed Feb 02 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.14.01-alt1
- 4.14.01

* Sun Jan 23 2005 Andrey Semenov <mitrofan@altlinux.ru> 4.14-alt1
- 4.14

* Tue Dec 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 4.13-alt1
- 4.13

* Sun Nov 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 4.12-alt1
- 4.12

* Mon Oct 25 2004 Andrey Semenov <mitrofan@altlinux.ru> 4.10-alt1
- new version

* Sat Aug 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.91-alt1
- new version
- add support for FreeBSD 5.2.1
- add support of filesystem that support case sensitive filenames

* Wed Jul 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.90-alt1
- First version of RPM package
