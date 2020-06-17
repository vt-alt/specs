Name:          libdmtx
Version:       0.7.5
Release:       alt1
Summary:       Library for working with Data Matrix 2D bar-codes
Group:         System/Libraries
License:       BSD-2-Clause
Url:           https://www.openhub.net/p/libdmtx
Vcs:           https://github.com/dmtx/libdmtx.git

Source:        %name-%version.tar

%description
libdmtx is open source software for reading and writing Data Matrix 2D
bar-codes on Linux, Unix, OS X, Windows, and mobile devices. At its core
libdmtx is a shared library, allowing C/C++ programs to use its capabilities
without restrictions or overhead.

The included utility programs, dmtxread and dmtxwrite, provide the official
interface to libdmtx from the command line, and also serve as a good reference
for programmers who wish to write their own programs that interact with
libdmtx.


%package       devel
Summary:       Development files for %name
Group:         Development/C
Requires:      %name = %version-%release

%description   devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make install DESTDIR=%buildroot INSTALL_ROOT=%buildroot

%check
# make check

%files
%doc AUTHORS LICENSE ChangeLog KNOWNBUG NEWS README README.linux TODO
%_libdir/%name.so.*

%files         devel
%doc
%_includedir/*
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_mandir/man3/%name.3*
%_libdir/%name.a

%changelog
* Thu Apr 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt1
- > another library source on github
- ^ 0.7.2 -> 0.7.5
- - support for ruby, python, vala, and mtdx utils

* Thu Mar 07 2019 Anton Farygin <rider@altlinux.ru> 0.7.2-alt8
- removed php-5 bindings

* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 0.7.2-alt7
- rebuild with new libImageMagick

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt6.3
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt6.2
- Rebuild with Ruby 2.5.0

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt6.1
- Rebuild with Ruby 2.4.1

* Fri Aug 18 2017 Anton Farygin <rider@altlinux.ru> 0.7.2-alt6
- rebuild with new libImageMagick

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.2-alt5.2
- Rebuild with new %%ruby_sitearchdir location

* Thu Sep 22 2016 Fr. Br. George <george@altlinux.ru> 0.7.2-alt5.1
- Rebuilt with ruby.git-2.3.1

* Mon Apr 07 2014 Anton Farygin <rider@altlinux.ru> 0.7.2-alt5
- Rebuild with new libImageMagick

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.7.2-alt4.1
- Rebuilt with ruby-2.0.0-alt1

* Thu Jun  6 2013 Fr. Br. George <george@altlinux.ru> 0.7.2-alt4
- Fix build

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 0.7.2-alt3
- Rebuild with new libImageMagick

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.7.2-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.7.2-alt2
- Rebuild with new libImageMagick

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1
- Rebuild with Python-2.7

* Thu May 12 2011 Fr. Br. George <george@altlinux.ru> 0.7.2-alt1
- Initial build from FC

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 17 2010 Dan Horák <dan[at]danny.cz> 0.7.2-3
- updated license for the php subpackage
- run few tests

* Sat May 29 2010 Dan Horák <dan[at]danny.cz> 0.7.2-2
- added language bindigs

* Wed Feb  3 2010 Dan Horák <dan[at]danny.cz> 0.7.2-1
- initial Fedora version
