
Name: libseccomp
Version: 2.4.2
Release: alt1
Summary: High level interface to the Linux Kernel's seccomp filter
License: LGPLv2.1+
Group: System/Libraries
Url: https://github.com/seccomp/libseccomp

#https://github.com/seccomp/libseccomp.git
Source: %name-%version.tar
Patch1: %name-%version.patch

%description
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF based
syscall filter language and present a more conventional function-call
based filtering interface that should be familiar to, and easily adopted
by application developers.

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %EVR

%description devel
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF based
syscall filter language and present a more conventional function-call
based filtering interface that should be familiar to, and easily adopted
by application developers.

This package contains development files of %name.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure --disable-static --enable-silent-rules
%make_build

%install
%makeinstall_std

# Relocate shared library from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
        t=$(readlink -v "$f")
        ln -rsnf %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%files
%doc CHANGELOG CREDITS README.md
%_bindir/*
/%_lib/lib*.so.*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%changelog
* Fri Dec 13 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.2-alt1
- new version 2.4.2

* Wed Apr 24 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Mar 22 2019 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt1
- 2.4.0
- do not build python bindings
- Fixes for the following security vulnerabilities:
  + CVE-2019-9893 64-bit argument comparisons do not work correctly

* Tue Jan 22 2019 Alexey Shabalin <shaba@altlinux.org> 2.3.3-alt2
- Removed ubt macros.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.3-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Fri Dec 15 2017 Alexey Shabalin <shaba@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.3-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Dec 17 2015 Alexey Shabalin <shaba@altlinux.ru> 2.2.3-alt1
- 2.2.3
- relocate shared libraries from %_libdir/ to /%_lib/.

* Thu Aug 27 2015 Afanasov Dmitry <ender@altlinux.org> 2.1.1-alt2.git20141021
- fix version in pkg-config file

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20141021
- Initial build for Sisyphus

