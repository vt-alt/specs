%def_with readline
%def_with xml

Summary: Mozilla SpiderMonkey (JavaScript-C) Engine
Name: js
%define lname lib%name
Version: 1.7.0
Release: alt9
License: %lgpl2only
URL: http://www.mozilla.org/%name/spidermonkey/
Group: Development/Other
Source: ftp://ftp.mozilla.org/pub/mozilla.org/%name/%name-%version.tar
Patch: %name-%version-%release.patch
Requires: %lname = %version-%release
Conflicts: libmozjs-tools
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
%{?_with_readline:BuildRequires: libreadline-devel}
BuildRequires: libnspr-devel

%description
SpiderMonkey is the code-name for the Mozilla's C implementation of
JavaScript.


%package -n %lname
Summary: Shared library of SpiderMonkey
Group: System/Libraries

%description -n %lname
Shared library of SpiderMonkey.


%package -n %lname-devel
Summary: Development files for SpiderMonkey
Group: Development/C
Requires: %lname = %version-%release
Requires: libnspr-devel
Conflicts: libmozjs

%description -n %lname-devel
Header and library files for doing development with %lname.


%package -n %lname-devel-static
Summary: Static library of SpiderMonkey
Group: Development/C
Requires: %lname-devel = %version-%release
Conflicts: libmozjs-devel

%description -n %lname-devel-static
Static library of SpiderMonkey.


%prep
%setup -c
cd %name
%patch -p1

sed -E -i '/^LIBDIR\s*:=/ s,\w+$,%_lib,' src/config.mk

%build
%add_optflags %optflags_shared
export CFLAGS="-DJS_C_STRINGS_ARE_UTF8"
%make -C %name/src -f Makefile.ref \
    LD=%__cc \
    XCFLAGS="%optflags $(nspr-config --cflags)" \
    BUILD_OPT=1 \
    JS_HAS_FILE_OBJECT=1 \
    JS_NO_THIN_LOCKS=1 \
    JS_THREADSAFE=1 \
%if_with xml
    JS_HAS_XML_SUPPORT=1 \
%else
    JS_HAS_XML_SUPPORT=0 \
%endif
%if_with readline
    JS_READLINE=1 \
%else
    JS_READLINE=0 \
%endif
    XMKSHLIBOPTS="-Wl,-soname,%lname.so.1" \
    VERSION=%version \
    all export


%install
install -d -m 0755 %buildroot{%_bindir,%_libdir,%_includedir/%name}
install -m 0755 dist/bin/* %buildroot%_bindir/
install -m 0644 dist/%_lib/* %buildroot%_libdir/
ln -sf %lname.so.%version %buildroot%_libdir/%lname.so
install -m 0644 dist/include/* %name/src/jsutil.h %buildroot/%_includedir/%name/



%files
%_bindir/*


%files -n %lname
%_libdir/*.so.*


%files -n %lname-devel
%doc %name/src/README*
%_includedir/%name
%_libdir/*.so


%files -n %lname-devel-static
%_libdir/*.a


%changelog
* Tue Jun 25 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.7.0-alt9
- Fixed build on architectures with %%_lib != lib .

* Thu Feb 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt8
- Rebuild with readline7.

* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.0-alt7
- rebuild for debuginfo (ALT #25234)

* Mon Jan 31 2011 Sergey Alembekov <rt@altlinux.ru> 1.7.0-alt6
- Close: #24997

* Tue Nov 09 2010 Sergey Alembekov <rt@altlinux.ru> 1.7.0-alt5
- utf-8 support added

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.0-alt4
- Rebuilt for soname set-versions

* Tue Feb 24 2009 Led <led@altlinux.ru> 1.7.0-alt3
- fixed build for non-x86 arches (thanx sbolshakov@)
- added missed requires to %lname-devel

* Sun Feb 01 2009 Led <led@altlinux.ru> 1.7.0-alt2
- cleaned up spec

* Tue Feb 12 2008 Led <led@altlinux.ru> 1.7.0-alt1
- initial build (based on legion@'s libmozjs spec)
