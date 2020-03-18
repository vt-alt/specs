Name: libopus
Version: 1.3.1
Release: alt2

Summary: Opus Audio Codec library
License: BSD
Group: System/Libraries
Url: http://opus-codec.org/
# http://downloads.xiph.org/releases/opus/%name-%version.tar.gz
Source: opus-%version.tar

%def_disable static

%description
The Opus codec is designed for interactive speech and audio transmission
over the Internet. It is designed by the IETF Codec Working Group and
incorporates technology from Skype's SILK codec and Xiph.Org's CELT codec.

%package devel
Summary: Development files for libopus
Group: Development/C
PreReq: %name = %version-%release
BuildRequires: doxygen

%description devel
This package contains the header files and documentation needed
to develop applications with libopus.

%package devel-static
Summary: Static libraries for libopus
Group: Development/C
PreReq: %name-devel = %version-%release

%description devel-static
This package contains development libraries required for packaging
statically linked libopus-based software.

%prep
%setup -n opus-%version

%build
%autoreconf
%configure \
	--enable-intrinsics \
	--enable-ambisonics \
	--enable-check-asm \
%ifarch x86_64
	--disable-rtcd \
%endif
	%{subst_enable static}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/*.so.*
%doc AUTHORS README COPYING

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc
%_aclocaldir/*.m4
%_man3dir/*
%dir %_docdir/opus/
%_docdir/opus/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Thu Mar 12 2020 Oleg Solovyov <mcpain@altlinux.org> 1.3.1-alt2
- fix unknown version in opus.pc (Closes: 38210)

* Sun Mar 08 2020 L.A. Kostis <lakostis@altlinux.ru> 1.3.1-alt1
- 1.3.1.

* Tue Sep 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.2.1-alt1.1
- disable run-time cpu detection only on x86_64.

* Tue Sep 05 2017 L.A. Kostis <lakostis@altlinux.ru> 1.2.1-alt1
- 1.2.1.
- enable checks.
- enable check-asm (to test correctness for asm optimisation).
- enable experimental Ambisonics support.

* Mon Jun 06 2016 L.A. Kostis <lakostis@altlinux.ru> 1.1.2-alt1
- 1.1.2 (closes #31585).
- enabled intrinsics asm optimizations.

* Thu Jul 16 2015 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- 1.1

* Wed Mar 04 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Sat Mar 02 2013 L.A. Kostis <lakostis@altlinux.ru> 1.0.2-alt1
- 1.0.2 (closes #28622).

* Sat Aug 25 2012 L.A. Kostis <lakostis@altlinux.ru> 1.0.1-alt0.1.rc2
- 1.0.1rc2.

* Mon Jul 23 2012 L.A. Kostis <lakostis@altlinux.ru> 0.9.14-alt1
- Updated to 0.9.14;
- initial build for ALTLinux.

