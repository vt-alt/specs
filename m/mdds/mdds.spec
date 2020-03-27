Name: mdds
Version: 1.5.0
Release: alt1
Summary: A collection of multi-dimensional data structures and indexing algorithms

Group: Development/C++
License: MIT
Url: https://gitlab.com/mdds/mdds
# http://kohei.us/files/%%name/src/%%name-%%version.tar.bz2
Source0: %name-%version.tar.bz2
Patch: mdds-1.5.0-python3.patch

BuildRequires: boost-devel
# Automatically added by buildreq on Mon Dec 02 2019
# optimized out: libstdc++-devel perl python-module-sphinx python-modules python2-base python3 python3-base python3-module-OpenSSL python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-packaging python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-six python3-module-sphinx python3-module-urllib3 sh4 xz
BuildRequires: ctags doxygen gcc-c++ python3-module-alabaster python3-module-breathe python3-module-sphinx_rtd_theme python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-jsmath python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml

%description
A collection of multi-dimensional data structures and indexing algorithms.

It implements the following data structures:
* segment tree
* flat segment tree
* rectangle set
* point quad tree
* multi type matrix
* multi type vector

See README for a brief description of the structures.

%package devel
Group: Development/C++
Summary: Headers for %name
BuildArch: noarch
Requires: boost-devel
Provides: %name-static = %version-%release

%package doc
Group: Development/C++
Summary: Docs for %name
BuildArch: noarch
Provides: %name-static = %version-%release

%description devel
Headers for %name.

%description doc
Docs for %name.

%prep
%setup
%patch -p0
# this is only used in tests
%autoreconf
sed -i -e '/^CPPFLAGS_NODEBUG=/s/=.*/="%optflags"/' configure

%build
%configure --enable-docs
%make_build all html

%check
%make check

%install
%makeinstall

ln -sr %buildroot/%_includedir/%name-*/%name  %buildroot/%_includedir/%name

ln -sr %buildroot/%_datadir/pkgconfig/%name-*pc %buildroot/%_datadir/pkgconfig/%name.pc

install -dm 755 %buildroot/%_docdir/%name-%version

cp -a ./doc/_build %buildroot/%_docdir/%name-%version/html
cp -a ./example %buildroot/%_docdir/%name-%version/

%files doc
%_docdir/%name-%version/*
%exclude %_docdir/%name

%files devel
%doc *.md CHANGELOG AUTHORS
%_includedir/*
%_datadir/pkgconfig/*

%changelog
* Mon Dec 02 2019 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Autobuild version bump to 1.5.0
- Switch to python3 sphinx

* Mon Sep 17 2018 Fr. Br. George <george@altlinux.ru> 1.4.2-alt1
- Autobuild version bump to 1.4.2

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Autobuild version bump to 1.3.1

* Fri Jun 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.3-alt1
- Updated to version 1.2.3

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 1.2.2-alt1
- Autobuild version bump to 1.2.2

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Autobuild version bump to 1.2.1
- Build documentation

* Wed Apr 13 2016 Fr. Br. George <george@altlinux.ru> 1.0.0-alt2
- Add ABI-depended include simlink

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Autobuild version bump to 1.0.0

* Sun Nov 08 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.0-alt1
- Version 1.00

* Wed Sep 16 2015 Fr. Br. George <george@altlinux.ru> 0.12.1-alt1
- Autobuild version bump to 0.12.1

* Wed Feb 11 2015 Fr. Br. George <george@altlinux.ru> 0.12.0-alt1
- Autobuild version bump to 0.12.0

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 0.11.2-alt1
- Autobuild version bump to 0.11.2

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 0.11.1-alt1
- Autobuild version bump to 0.11.1

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 0.11.0-alt1
- Autobuild version bump to 0.11.0

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 0.10.3-alt1
- Autobuild version bump to 0.10.3

* Thu Feb 20 2014 Fr. Br. George <george@altlinux.ru> 0.10.2-alt1
- Autobuild version bump to 0.10.2

* Thu Feb 20 2014 Fr. Br. George <george@altlinux.ru> 0.10.1-alt1
- Initial build for ALT

* Thu Feb 13 2014 David Tardon <dtardon@redhat.com> - 0.10.2-1
- new bugfix release

* Thu Jan 09 2014 David Tardon <dtardon@redhat.com> - 0.10.1-1
- new upstream release

* Tue Jan 07 2014 David Tardon <dtardon@redhat.com> - 0.10.0-1
- new upstream release

* Wed Nov 06 2013 David Tardon <dtardon@redhat.com> - 0.9.1-1
- new upstream release

* Wed Sep 04 2013 David Tardon <dtardon@redhat.com> - 0.8.1-5
- run tests on all platforms

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.8.1-3
- Rebuild for boost 1.54.0

* Mon Jun 10 2013 David Tardon <dtardon@redhat.com> - 0.8.1-2
- trivial changes

* Tue May 21 2013 David Tardon <dtardon@redhat.com> - 0.8.1-1
- new release

* Tue May 14 2013 David Tardon <dtardon@redhat.com> - 0.8.0-1
- new release

* Mon Mar 18 2013 David Tardon <dtardon@redhat.com> - 0.7.1-1
- new release

* Thu Feb 28 2013 David Tardon <dtardon@redhat.com> - 0.7.0-1
- new release

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.1-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.1-2
- Rebuild for Boost-1.53.0

* Tue Sep 18 2012 David Tardon <dtardon@redhat.com> - 0.6.1-1
- new version

* Sat Jul 28 2012 David Tardon <dtardon@redhat.com> - 0.6.0-2
- rebuilt for boost 1.50

* Mon Jul 23 2012 David Tardon <dtardon@redhat.com> - 0.6.0-1
- new version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 David Tardon <dtardon@redhat.com> - 0.5.4-1
- new version

* Thu Jul 14 2011 David Tardon <dtardon@redhat.com> - 0.5.3-1
- new version

* Wed Mar 30 2011 David Tardon <dtardon@redhat.com> - 0.5.2-2
- install license

* Tue Mar 29 2011 David Tardon <dtardon@redhat.com> - 0.5.2-1
- new version

* Thu Mar 24 2011 David Tardon <dtardon@redhat.com> - 0.5.1-3
- Resolves: rhbz#680766 fix a crash and two other bugs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 08 2011 David Tardon <dtardon@redhat.com> - 0.5.1-1
- new version

* Tue Dec 21 2010 David Tardon <dtardon@redhat.com> - 0.4.0-1
- new version

* Tue Nov 16 2010 David Tardon <dtardon@redhat.com> - 0.3.1-1
- new version

* Wed Jul 07 2010 Caolán McNamara <caolanm@redhat.com> - 0.3.0-2
- rpmlint warnings

* Wed Jun 30 2010 David Tardon <dtardon@redhat.com> - 0.3.0-1
- initial import
