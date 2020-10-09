%define _unpackaged_files_terminate_build 1

%def_with python3
# dane_ta_usage requires openssl >= 1.1.0
%def_without dane_ta_usage

Name: ldns
Version: 1.7.1
Release: alt1.git.e99accb9
License: BSD
Url: http://www.nlnetlabs.nl/%name/
Group: System/Libraries
Summary: Lowlevel DNS(SEC) library with API

# https://github.com/NLnetLabs/ldns.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libssl-devel doxygen perl libpcap-devel
%if_with python3
BuildRequires: python3-devel swig
%endif

%description
ldns is a library with the aim to simplify DNS programing in C. All
lowlevel DNS/DNSSEC operations are supported. We also define a higher
level API which allows a programmer to (for instance) create or sign
packets.

%package -n drill
Summary: Drill  is a tool to designed to get all sorts of information out of the DNS
Group: Networking/DNS

%description -n drill
Drill  is a tool to designed to get all sorts of information out of the DNS. 
It is specificly designed to be used with DNSSEC

The name drill is a pun on dig. With drill you should be able get  even
more information than with dig.

%package -n lib%name
Summary: Lowlevel DNS(SEC) library with API
Group: System/Libraries
Provides: %name = %EVR

%description -n lib%name
libldns is a library with the aim to simplify DNS programing in C. All
lowlevel DNS/DNSSEC operations are supported. We also define a higher
level API which allows a programmer to (for instance) create or sign
packets.

%package -n lib%name-devel-static
Summary: Lowlevel DNS(SEC) static library with API
Group: System/Libraries

%description -n lib%name-devel-static
libldns is a static library with the aim to simplify DNS programing in C. 
All lowlevel DNS/DNSSEC operations are supported. We also define a higher
level API which allows a programmer to (for instance) create or sign
packets.

%package -n lib%name-devel
Summary: Development package that includes the ldns header files
Group: Development/C
Requires: lib%name = %EVR
Requires: libssl-devel

%description -n lib%name-devel
The devel package contains the ldns library and the include files

%package -n lib%name-examples
Summary: Examples for library
Group: Development/C

%description -n lib%name-examples
Examples for library

%if_with python3
%package -n python3-module-%name
Summary: Python extensions for ldns
Group: Development/Python3

%description -n python3-module-%name
Python extensions for ldns
%endif

%prep
%setup

%build
%autoreconf
%configure --disable-rpath --with-drill --with-examples \
	--enable-rrtype-ninfo --enable-rrtype-rkey --enable-rrtype-cds --enable-rrtype-uri --enable-rrtype-ta \
%if_with python3
	--with-pyldns \
	PYTHON=$(which python3) \
%endif
%if_without dane_ta_usage
	--disable-dane-ta-usage \
%endif

%make_build
%make doc

%install
%make DESTDIR=%buildroot install
%make DESTDIR=%buildroot install-doc


# don't package building script in doc
rm doc/doxyparse.pl
#remove doc stubs
rm -rf doc/.svn
#remove double set of man pages
rm -rf doc/man
# remove .la files
rm -rf %buildroot%python3_sitelibdir/*.la
rm -rf %buildroot%python3_sitelibdir/*.a

install -pD -m644 packaging/libldns.pc %buildroot%_pkgconfigdir/libldns.pc
install -pD -m644 libdns.vim %buildroot%_sysconfdir/vim/libldns

%check
#make test

%files -n drill
%_bindir/drill
%_mandir/man1/drill*

%files -n lib%name
%_libdir/libldns*.so.*
%doc README LICENSE

%files -n lib%name-devel-static
%_libdir/libldns.a

%files -n lib%name-devel
%_bindir/ldns-config
%_man1dir/ldns-config*
%_includedir/ldns
%_pkgconfigdir/*
%_libdir/libldns*so
%doc doc Changelog README
%_man3dir/*
%_sysconfdir/vim/*

%files -n lib%name-examples
%_bindir/ldns-*
%_bindir/ldnsd
%_man1dir/ldns-*
%_man1dir/ldnsd*

%exclude %_bindir/ldns-config
%exclude %_man1dir/ldns-config*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*.py
%python3_sitelibdir/*.so*
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Thu Feb 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.1-alt1.git.e99accb9
- Updated to current upstream snapshot
- Switched to python-3

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt3
- NMU: remove %%ubt from release

* Tue Sep 04 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.0-alt2
- Rebuilt with openssl 1.1.

* Wed Sep 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.0-alt1
- Updated to upstream release version 1.7.0.
- Added %%ubt macro to release.

* Sat Jan 11 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.17-alt1
- 1.6.17

* Sat Nov 17 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.16-alt1
- 1.6.16

* Mon May 21 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.13-alt1
- 1.6.13

* Fri Feb 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.12-alt1
- 1.6.12

* Thu Sep 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.11-alt1
- 1.6.11
- enable sha2
- add python module
- add ldns-config and libldns.pc
- add /etc/vim/libldns
- gzip mans

* Sun Jul 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.10-alt1
- 1.6.10

* Thu Mar 31 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.9-alt1
- 1.6.9
- disable tests

* Thu Feb 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.8-alt1
- 1.6.8

* Sat Nov 13 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.7-alt1
- 1.6.7

* Tue Oct 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.6-alt2
- Rebuild with new libcrypt

* Fri Aug 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.6-alt1
- 1.6.6

* Tue Jun 22 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.5-alt1
- 1.6.5

* Wed Feb 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.4-alt1
- 1.6.4

* Mon Dec 14 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Nov 17 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.2-alt1
- 1.6.2

* Sat Aug 15 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.1-alt2
- Rename lib%name-static to lib%name-devel-static
- Move links to libs to devel package

* Sat Aug 15 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon May 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.5.1-alt2
- Update spec for fix build with new toolchain

* Thu Mar 26 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.0_pre_20080715-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Thu Aug 07 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.3.0_pre_20080715-alt1
- New version

* Sun May 25 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.3.0_pre_20080229-alt1
- New version

* Sun May 25 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.2.2-alt1
- Build for ALT
