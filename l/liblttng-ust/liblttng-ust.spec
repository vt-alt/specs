Name: liblttng-ust
Version: 2.10.4
Release: alt1

Summary: Linux Trace Toolkit Userspace Tracer library

License: GPLv2
Group: Development/C++
Url: http://lttng.org/lttng2.0

# Source-url: http://lttng.org/files/lttng-ust/lttng-ust-%version.tar.bz2
Source: %name-%version.tar
Patch100: lttng-gen-tp-shebang.patch
Patch101: 0001-Fix-namespace-our-gettid-wrapper.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libuserspace-rcu-devel
BuildRequires: libuuid-devel

# for man pages
BuildRequires: asciidoc xmlto

%description
This library may be used by user space applications to generate tracepoints within the kernel LTT subsystem.

%package devel

Summary: Linux Trace Toolkit Userspace Tracer library
Group: Development/C++
Requires: %name = %version-%release
Requires: libuserspace-rcu-devel

%description devel
This library provides support for developing programs using LTTng userspace tracing.

%package docs

Summary: Linux Trace Toolkit Userspace Tracer Documentation
Group: Development/C++
Requires: %name = %version-%release

%description docs
This package includes documentation and examples for developing programs using LTTng userspace tracing.

%prep
%setup
%patch100 -p1
%patch101 -p1

%build
# to fix rpath
%autoreconf
%configure --docdir=%_docdir/%name --disable-static --disable-maintainer-mode
%make_build

%install
%makeinstall_std
rm -vf %buildroot%_libdir/*.la
rm -rf %buildroot/tmp/lttng-ust-divert

%files
%_libdir/*.so.*

%files devel
%_bindir/lttng-gen-tp
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/lttng-ust*.pc

%files docs
%dir %_docdir/%name/
%_docdir/%name/ChangeLog
%_docdir/%name/README.md
#_docdir/%name/COPYING
%dir %_docdir/%name/examples
%_docdir/%name/examples/*
%_docdir/%name/java-agent.txt
%_man1dir/lttng-gen-tp.1.*
%_man3dir/lttng-ust.3.*
%_man3dir/lttng-ust-cyg-profile.3.*
%_man3dir/lttng-ust-dl.3.*
%_man3dir/do_tracepoint.3.*
%_man3dir/tracef.3.*
%_man3dir/tracelog.3.*
%_man3dir/tracepoint.3.*
%_man3dir/tracepoint_enabled.3.*

%changelog
* Wed Jun 05 2019 Alexey Shabalin <shaba@altlinux.org> 2.10.4-alt1
- 2.10.4
- switch to use python3

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.10.2-alt2
- drop ExclusiveArch (ALT bug 35661)

* Sat Nov 24 2018 Vitaly Lipatov <lav@altlinux.ru> 2.10.2-alt1
- new version 2.10.2 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.10.1-alt1
- new version 2.10.1 (with rpmrb script)

* Sun Nov 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.8.3-alt1.1
- autorebuild with libuserspace-rcu.git=0.10.0-alt1

* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 2.8.3-alt1
- new version 2.8.3 (with rpmrb script)
- fix dl linking (see https://github.com/lttng/lttng-ust/pull/48)

* Mon Apr 10 2017 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- new version 2.8.0 (with rpmrb script)

* Mon Apr 10 2017 Vitaly Lipatov <lav@altlinux.ru> 2.7.0-alt1
- initial build for ALT Linux Sisyphus
