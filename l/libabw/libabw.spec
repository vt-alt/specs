Name: libabw
Version: 0.1.3
Release: alt1
Summary: A library for import of AbiWord files

Group: System/Libraries
License: MPLv2.0
Url: https://wiki.documentfoundation.org/DLP/Libraries/libabw
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(zlib)

BuildRequires: doxygen help2man
BuildRequires: gperf perl

%description
%name is a library for import of AbiWord files.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform AbiWord files into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform AbiWord files into other formats. Currently
supported: XHTML, raw, text.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%makeinstall_std
make install DESTDIR=%buildroot
# we install API docs directly from build
rm -rf %buildroot/%_docdir/%name

# generate and install man pages
export LD_LIBRARY_PATH=%buildroot%_libdir${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in abw2html abw2raw abw2text; do
    help2man -N -S '%name %version' -o ${tool}.1 %buildroot%_bindir/${tool}
done
install -m 0755 -d %buildroot%_man1dir
install -m 0644 abw2*.1 %buildroot%_man1dir

%files
%doc CREDITS COPYING.MPL README
%_libdir/*.so.*

%files devel
%doc ChangeLog NEWS
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files doc
%doc COPYING.MPL
%doc docs/doxygen/html

%files tools
%_bindir/abw2*
%_man1dir/abw2*

%changelog
* Mon Aug 26 2019 Alexey Shabalin <shaba@altlinux.org> 0.1.3-alt1
- new version 0.1.3

* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.1.2-alt1
- new version 0.1.2

* Thu Aug 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt3
- Fixed build with new boost.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Fixed build with new toolchain

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.1.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.1.1-alt1
- Autobuild version bump to 0.1.1

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.0.2-alt1
- Autobuild version bump to 0.0.2

* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.0.1-alt1
- Initial build from FC

* Mon Feb 10 2014 David Tardon <dtardon@redhat.com> - 0.0.2-1
- new upstream release 0.0.2
- generate man pages for the tools

* Wed Jan 15 2014 David Tardon <dtardon@redhat.com> - 0.0.1-1
- new upstream release

* Mon Jan 13 2014 David Tardon <dtardon@redhat.com> - 0.0.0-1
- initial import
