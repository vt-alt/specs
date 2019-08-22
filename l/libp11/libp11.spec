
%define engines_dir $(pkg-config --variable=enginesdir --silence-errors libcrypto)

Name: libp11
Version: 0.4.10
Release: alt1

Summary: Library for using PKCS#11 modules
Group: System/Libraries
License: LGPLv2+

Url: https://github.com/OpenSC/libp11/wiki
Source: %name-%version.tar

Provides: openssl-engine_pkcs11 = %version-%release
Obsoletes: openssl-engine_pkcs11 < %version-%release

BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: libssl-devel >= 0.9.8
BuildRequires: doxygen xsltproc

# needed for testsuite
BuildRequires: softhsm opensc

%description
Libp11 is a library implementing a small layer on top of PKCS#11 API
to make using PKCS#11 implementations easier.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release
Requires: libssl-devel

%description devel
Development files for %name.

%prep
%setup
cat > README.ALT <<EOF
In ALTLinux, the engine file has been placed in the
%_libdir/openssl/engines directory instead of the default
%_libdir/engines. This was done so in order to match our openssl
installation.

Considering this new path, below is the suggested change to openssl.cnf
in order to use this engine:

openssl_conf = openssl_def

[openssl_def]
engines = engine_section

[engine_section]
pkcs11 = pkcs11_section

[pkcs11_section]
engine_id = pkcs11
dynamic_path = %engines_dir/pkcs11.so
MODULE_PATH = %_libdir/opensc-pkcs11.so
init = 0

EOF

chmod 0644 README.ALT

%build
%autoreconf
%configure \
        --disable-static \
        --enable-api-doc \
        --with-enginesdir=%engines_dir

%make_build

%install
%makeinstall_std


# Cleanup
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%engines_dir/*.la
rm -rf %buildroot%_docdir/%name

%files
%doc COPYING NEWS README.md README.ALT
%_libdir/*.so.*
%_libdir/openssl/*/*.so*

%files devel
%_libdir/libp11.so
%_pkgconfigdir/*.pc
%_includedir/*

%changelog
* Wed Aug 21 2019 Alexey Shabalin <shaba@altlinux.org> 0.4.10-alt1
- new version 0.4.10

* Wed Aug 29 2018 Alexey Shabalin <shaba@altlinux.org> 0.4.8-alt1
- 0.4.8
- build with openssl-1.1

* Mon May 29 2017 Michael Shigorin <mike@altlinux.org> 0.4.6-alt1
- 0.4.6

* Wed Jun 15 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0
- merge engine_pkcs11

* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 0.3.0-alt1
- 0.3.0
- recreated gear repo to use upstream git
- applied fedora patch and spec bits for API docs

* Mon Sep 21 2015 Michael Shigorin <mike@altlinux.org> 0.2.8-alt1
- 0.2.8
- updated Url:
- reverted Group: (it's not legacy but rather a layer)
- dropped API docs
- minor spec cleanup

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1.qa3
- Moved this version into System/Legacy libraries

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.7-alt1.qa2
- NMU: rebuilt for debuginfo.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.2.7-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Jun 29 2010 Alexey I. Froloff <raorn@altlinux.org> 0.2.7-alt1
- [0.2.7]

* Wed Sep 09 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.6-alt2
- devel subpackage should require libssl-devel

* Fri Aug 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.6-alt1
- [0.2.6] (closes: #21289)
- Developer docs moved to devel subpackage
- Packaged API documentation

* Wed Dec 03 2008 Lebedev Sergey <barabashka@altlinux.org> 0.2.4-alt1
- initial build

