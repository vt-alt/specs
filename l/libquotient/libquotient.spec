%define oname Quotient

Name: libquotient
Version: 0.6.1
Release: alt1

Summary: A Qt5 library to write cross-platfrom clients for Matrix

License: LGPLv2.1
Group: System/Libraries
Url: https://github.com/quotient-im/libQuotient

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/quotient-im/libQuotient/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses rpm-macros-qt5 rpm-macros-cmake

#BuildRequires(pre): rpm-build-compat >= 2.1.5
#BuildRequires(pre): rpm-build-intro >= 2.1.5
# use no more than system_memory/3000 build procs (see https://bugzilla.altlinux.org/show_bug.cgi?id=35112)
#_tune_parallel_build_by_procsize 3000

BuildRequires: cmake gcc-c++ libstdc++-devel

BuildRequires: qt5-base-devel libqt5-gui libqt5-network qt5-multimedia-devel

Provides: libqmatrixclient = %version
Obsoletes: libqmatrixclient < %version

%description
libQuotient is a Qt5-based library to make IM clients for the Matrix protocol.
It is the backbone of Quaternion, Spectral and some other projects.

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %EVR

Provides: libqmatrixclient-devel = %version
Obsoletes: libqmatrixclient-devel < %version

%description devel
Header files for %EVR.

%prep
%setup
%__subst "s|add_library(\${PROJECT_NAME} \${lib_SRCS} \${api_SRCS})|add_library(\${PROJECT_NAME} SHARED \${lib_SRCS} \${api_SRCS})|" CMakeLists.txt

%build
%cmake_insource
%make_build

%install
%makeinstall_std
rm -rf %buildroot/usr/share/ndk-modules/

%files
%doc README.md CONTRIBUTING.md
%_libdir/lib%oname.so.*

%files devel
%_bindir/quotest
%_libdir/lib%oname.so
%_includedir/%oname/
%_libdir/cmake/%oname/
%_pkgconfigdir/%oname.pc

%changelog
* Thu Sep 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- new version 0.6.1 (with rpmrb script)
- library, includes and conf files changed to Quotient
- replace Conflicts with Obsoletes (thanks, zerg@)

* Thu Jun 13 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)
- rename libmatrixclient to libquotient (as upstream)

* Mon Jan 21 2019 Vitaly Lipatov <lav@altlinux.ru> 0.4.2.1-alt1
- initial build for ALT Sisyphus
