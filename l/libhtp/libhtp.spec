%define _unpackaged_files_terminate_build 1

Name: libhtp
Epoch: 1
Version: 0.5.36
Release: alt1
Summary: LibHTP is a security-aware parser for the HTTP protocol and the related bits and pieces
License: BSD-3-Clause
Group: Security/Networking
Url: https://github.com/OISF/libhtp

Source0: %name-%version.tar

BuildRequires: zlib-devel

%description
This is a security-aware parser for the HTTP protocol and the related bits
and pieces. The goals of the project, in the order of importance, are as
follows:

 1. Completeness of coverage; LibHTP must be able to parse virtually all
    traffic that is found in practice.

 2. Permissive parsing; LibHTP must never fail to parse a stream that would
    be parsed by some other web server.

 3. Awareness of evasion techniques; LibHTP must be able to detect and
    effectively deal with various evasion techniques, producing, where
    practical, identical or practically identical results as the web
    server processing the same traffic stream.

 4. Performance; The performance must be adequate for the desired tasks.
    Completeness and security are often detrimental to performance. Our
    idea of handling the conflicting requirements is to put the library
    user in control, allowing him to choose the most desired library
    characteristic.

%package devel
Summary: Development headers and libraries for %name
Requires: %name = %EVR
Group: Development/C

%description devel
Development headers and libraries for %name.

%package devel-static
Summary: Static libraries for %name
Requires: %name-devel = %EVR
Group: Development/C

%description devel-static
Static libraries for %name.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/%{name}*.so.*

%files devel
%_libdir/%name.so
%_includedir/htp
%_libdir/pkgconfig/htp.pc

%files devel-static
%_libdir/*.a

%changelog
* Mon Dec 21 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.5.36-alt1
- new version 0.5.36

* Tue Oct 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.5.35-alt1
- Updated to upstream version 0.5.35 (Fixes: CVE-2019-17420).

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.5.25-alt1.qa1
- NMU: applied repocop patch

* Thu Jul 21 2017 Starostin Nikita <stark@altlinux.org> 1:0.5.25-alt1
- initial build
