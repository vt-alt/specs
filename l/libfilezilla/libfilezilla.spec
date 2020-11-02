%define _unpackaged_files_terminate_build 1

Name: libfilezilla
Version: 0.25.0
Release: alt1
Summary: Small and modern C++ library
License: GPLv2+
Group: System/Libraries
Url: https://lib.filezilla-project.org/

# Repacked https://download.filezilla-project.org/libfilezilla/%name-%version.tar.bz2
Source: %name-%version.tar

BuildRequires: cppunit-devel doxygen gcc-c++ graphviz libnettle-devel
BuildRequires: libgnutls-devel

Conflicts: libfilezilla0 < %EVR
Obsoletes: libfilezilla0 < %EVR
Provides:  libfilezilla0 = %EVR

%description
libfilezilla is a free, open source C++ library, offering some basic
functionality to build high-performing, platform-independent programs.
Some of the highlights include:

* A typesafe, multi-threaded event system that's very simple to use yet
  extremely efficient.
* Timers for periodic events.
* A datetime class that not only tracks timestamp but also their
  accuracy, which simplifies dealing with timestamps originating from
  different sources.
* Simple process handling for spawning child processes with redirected
  I/O.

%package devel
Summary: Development package for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
Header files for development with %name.

%prep
%setup

%build
%ifarch mipsel
export LIBS=-latomic
%endif

%configure \
	--disable-static \
	%nil

%make_build

pushd doc
make html
popd

%install
%makeinstall_std

find %buildroot -name '*.la' -delete

%find_lang %name

%check
LC_ALL=en_US.UTF-8 make check

%files -f %name.lang
%doc COPYING
%doc AUTHORS ChangeLog NEWS README
%_libdir/%name.so.*

%files devel
%doc doc/doxygen-doc/*
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Mon Oct 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.25.0-alt1
- Updated to upstream version 0.25.0.

* Mon Aug 31 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.24.1-alt1
- Updated to upstream version 0.24.1.

* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23.0-alt1
- Updated to upstream version 0.23.0.

* Thu Jun 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.22.0-alt1
- Updated to upstream version 0.22.0.

* Mon Apr 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.20.2-alt1
- Updated to upstream version 0.20.2.

* Mon Sep 02 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.18.1-alt1
- Updated to upstream version 0.18.1.

* Wed Jul 24 2019 Ivan A. Melnikov <iv@altlinux.org> 0.17.1-alt2
- Fix build on mipsel.

* Thu Jul 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17.1-alt1
- Updated to upstream version 0.17.1.

* Tue Feb 19 2019 Egor Zotov <egorz@altlinux.org> 0.15.1-alt1
- Updated to upstream version 0.15.1.

* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.2-alt1
- Updated to upstream version 0.11.2.

* Thu Jun 08 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.2-alt1
- Updated to 0.9.2.

* Wed Feb 22 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.1-alt1
- Updated to 0.9.1.

* Thu Dec 22 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.0-alt1
- Updated to 0.9.0.

* Thu Sep 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.6.1-alt1
- Updated to 0.6.1.

* Mon Jun 27 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.3-alt1
- Updated to 0.5.3.

* Thu Jun 02 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.2-alt1
- Updated to 0.5.2.

* Wed May 04 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.0-alt1
- Updated to 0.5.0.

* Wed Mar 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.0.1-alt1
- Initial build.
