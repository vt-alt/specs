Name: wavpack
Version: 5.3.0
Release: alt1

Summary: Open audio compression codec
License: BSD
Group: Sound
Url: http://www.wavpack.com/

# Source-url:http://www.wavpack.com/%name-%version.tar.bz2
Source: %name-%version.tar
Patch: wavpack-fc-pkgconfig.patch

Requires: lib%name = %version-%release
BuildRequires: gcc-c++

%def_disable static

%description
WavPack is a completely open audio compression format providing lossless,
high-quality lossy, and a unique hybrid compression mode.  Although the
technology is loosely based on previous versions of WavPack, the new
version 4 format has been designed from the ground up to offer
unparalleled performance and functionality.

%package -n lib%name
Summary: WavPack library
Group: System/Libraries

%description -n lib%name
This package contains WavPack shared library.

%package -n lib%name-devel
Summary: Development files for WavPack library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains development files for WavPack library.

%prep
%setup
#patch -p1

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%files -n lib%name
%doc COPYING ChangeLog README.md
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/wavpack/
%_pkgconfigdir/*.pc

%changelog
* Wed May 06 2020 Vitaly Lipatov <lav@altlinux.ru> 5.3.0-alt1
- new version 5.3.0 (with rpmrb script)

* Wed Jan 29 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script)

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 4.80.0-alt1
- new version 4.80.0 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 4.75.2-alt1
- new version 4.75.2 (with rpmrb script)

* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 4.70.0-alt1
- new version (4.70.0) with rpmgs script

* Tue Jun 28 2011 Dmitry V. Levin <ldv@altlinux.org> 4.60.1-alt1
- Updated to 4.60.1.
- Packaged documentation.
- Cleaned up specfile.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 4.50.1-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 4.50.1-alt1
- new version 4.50 (with rpmrb script)

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 4.41.0-alt1
- new version 4.41.0 (with rpmrb script)

* Mon Jan 15 2007 Vitaly Lipatov <lav@altlinux.ru> 4.40.0-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

