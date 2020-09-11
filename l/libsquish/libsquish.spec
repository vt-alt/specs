%define _unpackaged_files_terminate_build 1

Name: libsquish
Version: 1.15
Release: alt1
Summary: Open source DXT compression library
Group: System/Libraries
License: MIT
URL: https://sourceforge.net/projects/libsquish/

# http://download.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
Source: %name-%version.tar
Patch1: %name-fedora-cmake_install.patch

BuildRequires: gcc-c++ cmake

%package devel
Summary: Development files for Open source DXT compression library
Group: Development/Other
Requires: %name = %EVR

%description
The libSquish library compresses images with the DXT standard
(also known as S3TC). This standard is mainly used by OpenGL and
DirectX for the lossy compression of RGBA textures.

%description devel
The libsquish-devel package contains files needed for developing or compiling
applications which use DXT compression.

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_SQUISH_WITH_SSE2:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE.txt
%doc README.txt
%doc ChangeLog.txt
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Mon Apr 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15-alt1
- Initial build for ALT.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15-2
- Review fixes.

* Mon Apr 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.15-1
- Initial package.
