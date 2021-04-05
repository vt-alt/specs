Name: cgreen
Version: 1.0
Release: alt3

Summary: Framework for unit testing, written in C
License: LGPL-2.1+
Group: Development/C
Url: http://www.lastcraft.com/cgreen.php

Source0: %name-%version.tar

%define _unpackaged_files_terminate_build 1

%description 
What is it? It's a framework for unit testing, written in C. A tool
for C developers writing tests of their own code.

If you have used JUnit, or any of the xUnit clones, you will find
the concept familiar. In particular the tool supports a range of
assertions, composable test suites and setup/teardown facilities.
Because of the peculiarities of C programming, each test function
is normally run in it's own process.

NOTE: this package includes a slightly modified version of cgreen. Check
http://git.altlinux.ru/people/voins/packages/?p=cgreen.git for list of changes


%prep
%setup -q

%build
make

%install
mkdir -p $RPM_BUILD_ROOT{%_includedir{,/cgreen},%_libdir}
install -s -m644 libcgreen.so.0.1 $RPM_BUILD_ROOT%_libdir
ln -s libcgreen.so.0.1 $RPM_BUILD_ROOT%_libdir/libcgreen.so.0
ln -s libcgreen.so.0 $RPM_BUILD_ROOT%_libdir/libcgreen.so
install -m644 cgreen/cgreen.h $RPM_BUILD_ROOT%_includedir
install -m644 cgreen/assertions.h cgreen/constraint.h cgreen/memory.h \
    cgreen/mocks.h cgreen/reporter.h cgreen/text_reporter.h cgreen/unit.h \
    $RPM_BUILD_ROOT%_includedir/cgreen/


%files
%doc README VERSION documentation samples
%_includedir/*
%_libdir/*.so*


%changelog
* Tue Mar 30 2021 Mikhail Efremov <sem@altlinux.org> 1.0-alt3
- Fix License tag.
- Use _unpackaged_files_terminate_build.
- Fix packaging on 32bit arches.

* Mon Jun 16 2014 Mikhail Efremov <sem@altlinux.org> 1.0-alt2
- Fix build.

* Mon Jan 07 2008 Alexey Voinov <voins@altlinux.ru> 1.0-alt1
- initial build

