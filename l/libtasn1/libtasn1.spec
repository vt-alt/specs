Name: libtasn1
Version: 4.14
Release: alt1

Summary: The ASN.1 library used in GNUTLS
Group: System/Libraries
License: LGPLv2.1+
URL: http://www.gnu.org/software/libtasn1/
# git://git.altlinux.org/gears/l/libtasn1.git
Source: %name-%version.tar
Patch1: fix-for-werror.patch

BuildRequires: gtk-doc texinfo

%description
This is GNU Libtasn1, a library that provides Abstract Syntax Notation
One (ASN.1, as specified by the X.680 ITU-T recommendation) parsing and
structures management, and Distinguished Encoding Rules (DER, as per
X.690) encoding and decoding functions.

This package contains libtasn1 runtime library.

%package devel
Summary: Files for development of applications which will use libtasn1
Group: Development/C
License: LGPLv2.1+
Requires: %name = %version-%release

%description devel
This is GNU Libtasn1, a library that provides Abstract Syntax Notation
One (ASN.1, as specified by the X.680 ITU-T recommendation) parsing and
structures management, and Distinguished Encoding Rules (DER, as per
X.690) encoding and decoding functions.

This package contains files for development of applications
which will use libtasn1.

%package utils
Summary: Some ASN.1 tools
Group: Text tools
License: GPLv3+
Requires: %name = %version-%release

%description utils
This is GNU Libtasn1, a library that provides Abstract Syntax Notation
One (ASN.1, as specified by the X.680 ITU-T recommendation) parsing and
structures management, and Distinguished Encoding Rules (DER, as per
X.690) encoding and decoding functions.

This package contains simple tools that can decode and encode ASN.1 data.

%package devel-doc
Summary: libtasn1 development documentation
Group: Development/Documentation
License: LGPLv2.1+
Conflicts: %name-devel < %version
BuildArch: noarch

%description devel-doc
This is GNU Libtasn1, a library that provides Abstract Syntax Notation
One (ASN.1, as specified by the X.680 ITU-T recommendation) parsing and
structures management, and Distinguished Encoding Rules (DER, as per
X.690) encoding and decoding functions.

This package contains libtasn1 development documentation.

%prep
%setup
%patch1 -p1

%build
%def_enable Werror
%add_optflags -Wno-error=format-truncation
%autoreconf
%configure --disable-static --disable-silent-rules
touch doc/stamp_docs
%make_build

%install
%makeinstall_std

%define docdir %_docdir/%name
mkdir -p %buildroot%docdir
install -pm644 AUTHORS NEWS README.md THANKS %buildroot%docdir/
ln -s %_licensedir/LGPL-2.1 %buildroot%docdir/COPYING.LIB
install -pm644 doc/*.html doc/*.pdf %buildroot%docdir/
mkdir -p %buildroot%docdir/reference/html
install -pm644 doc/reference/html/* %buildroot%docdir/reference/html/

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files
%_libdir/*.so.*
%dir %docdir
%docdir/[ACNRT]*

%files utils
%_bindir/asn1*
%_man1dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files devel-doc
%_infodir/*
%_man3dir/*
%dir %docdir
%docdir/*.html
%docdir/*.pdf
%docdir/reference/

%changelog
* Thu Aug 08 2019 Mikhail Efremov <sem@altlinux.org> 4.14-alt1
- Enabled LFS support.
- Updated fix-for-werror.patch.
- Updated to 4.14.

* Thu Mar 15 2018 Mikhail Efremov <sem@altlinux.org> 4.13-alt2
- Fix build with gcc-7.

* Thu Jan 25 2018 Mikhail Efremov <sem@altlinux.org> 4.13-alt1
- Updated to 4.13.

* Thu Jun 15 2017 Mikhail Efremov <sem@altlinux.org> 4.12-alt1
- Updated fix-for-werror.patch.
- Updated to 4.12.

* Thu Feb 02 2017 Mikhail Efremov <sem@altlinux.org> 4.10-alt1
- Set -Werror explicitly.
- Fix build with -Werror.
- Updated to 4.10.

* Tue Jul 26 2016 Mikhail Efremov <sem@altlinux.org> 4.9-alt1
- Updated to 4.9.

* Mon Apr 11 2016 Mikhail Efremov <sem@altlinux.org> 4.8-alt1
- Updated to 4.8.

* Thu Dec 03 2015 Mikhail Efremov <sem@altlinux.org> 4.7-alt2
- Add texinfo to BR.

* Wed Oct 28 2015 Mikhail Efremov <sem@altlinux.org> 4.7-alt1
- Updated to 4.7.

* Wed May 27 2015 Mikhail Efremov <sem@altlinux.org> 4.5-alt1
- Updated to 4.5.

* Wed Apr 29 2015 Mikhail Efremov <sem@altlinux.org> 4.4-alt1
- Updated to 4.4.

* Wed Mar 11 2015 Mikhail Efremov <sem@altlinux.org> 4.3-alt1
- Updated to 4.3.

* Thu Oct 30 2014 Mikhail Efremov <sem@altlinux.org> 4.2-alt1
- Updated to 4.2.

* Wed Mar 05 2014 Dmitry V. Levin <ldv@altlinux.org> 3.4-alt1
- Updated to 3.4.

* Wed Apr 10 2013 Dmitry V. Levin <ldv@altlinux.org> 3.3-alt1
- Updated to 3.3.

* Sun Dec 16 2012 Dmitry V. Levin <ldv@altlinux.org> 2.14-alt1
- Updated to 2.14.

* Sat Sep 01 2012 Dmitry V. Levin <ldv@altlinux.org> 2.13-alt1
- Updated to 2.13.

* Fri Mar 23 2012 Dmitry V. Levin <ldv@altlinux.org> 2.12-alt1
- Updated to 2.12 (fixes CVE-2012-1569).

* Thu Dec 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.11-alt1
- Updated to 2.11.
- Rewritten specfile.

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 2.9-alt2
- rebuilt for pkgconfig
- made libtasn1-devel-doc noarch

* Sun Dec 19 2010 Afanasov Dmitry <ender@altlinux.org> 2.9-alt1
- 2.9

* Tue Oct 19 2010 Afanasov Dmitry <ender@altlinux.org> 2.8-alt1
- 2.8

* Fri Nov 06 2009 Afanasov Dmitry <ender@altlinux.org> 2.3-alt1
- 2.3

* Fri May 22 2009 Afanasov Dmitry <ender@altlinux.org> 2.2-alt1
- 2.2
- remove %%install_info's invocations

* Fri Apr 17 2009 Afanasov Dmitry <ender@altlinux.org> 2.1-alt1
- 2.1
- minor changes:
  + Fix compilation failure

* Tue Apr 14 2009 Afanasov Dmitry <ender@altlinux.org> 2.0-alt1
- 2.0
  + The libtasn1-config tool has been removed (see NEWS for details)

* Mon Jan 26 2009 Afanasov Dmitry <ender@altlinux.org> 1.8-alt1
- 1.8

* Tue Dec 02 2008 Afanasov Dmitry <ender@altlinux.org> 1.7-alt2
- change packager.
- merge shaba@ updates.
- remove libtasn1.m4. it was removed in v1.6 and using pkg-config was
  offered (see NEWS for details)

* Wed Nov 26 2008 Alexey Shabalin <shaba@altlinux.ru> 1.7-alt1
- 1.7
- remove ldconfig from %%post

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt1
- 1.5 release.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.1-alt1
- 1.1 release.

* Tue May 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.10-alt1
- 0.3.10 release.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.9-alt1
- 0.3.9 release.

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.3.8-alt1
- 0.3.8 release.
- Minor spec cleanup.
- Fixed BuildRequires.
- Hacked the configure.in to use autoconf 2.59.
- Added onceonly.m4 file to source tree to be able to use macros
  appeared in autoconf 2.60.

* Sat Sep 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.6-alt1
- Updated to 0.3.6

* Tue May 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.3.4-alt1
- Updated to 0.3.4
- Added libtasn1-utils package
- Buildreq

* Sat Feb 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.18-alt1
- 0.2.18, fixes SA18794

* Tue Nov 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.17-alt1
- Updated to 0.2.17
- Moved documentation to the devel-doc subpackage

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.15-alt1
- Updated to 0.2.15

* Mon Jan 03 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.13-alt1
- Updated to 0.2.13
- Serialized make

* Tue May 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.10-alt1
- Updated to 0.2.10
- Added configure scripts to the file list

* Sat Mar 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.7-alt1
- New upstream release

* Fri Jan 02 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.2.6-alt1
- Initial release for Sisyphus
