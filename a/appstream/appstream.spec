%def_without docs

Name:    appstream
Version: 0.13.1
Release: alt0.1.b9
Summary: Utilities to generate, maintain and access the AppStream Xapian database 

# lib LGPLv2+, tools GPLv2+
License: GPLv2+ and LGPLv2+
Group:   System/Configuration/Packaging
URL:     http://www.freedesktop.org/wiki/Distributions/AppStream/Software
Source0: appstream-%{version}.tar
# VCS:   https://github.com/ximion/appstream
Patch1:  appstream-no-Wno-deprecated-copy.patch

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: ctest
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: gperf
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: liblmdb-devel
BuildRequires: libprotobuf-lite-devel
BuildRequires: libstemmer-devel
BuildRequires: libxapian-devel
BuildRequires: libxml2-devel
BuildRequires: libyaml-devel
BuildRequires: ninja-build
BuildRequires: protobuf-compiler
%if_with docs
BuildRequires: daps
%endif
BuildRequires: qt5-base-devel
BuildRequires: xmlto
BuildRequires: gtk-doc
BuildRequires: libsoup-devel
BuildRequires: /proc

#Requires: appstream-data

%description
AppStream-Core makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%package devel
Summary:  Development files for %{name}
Group:	  Development/C
Requires: %name = %version-%release

%description devel
%{summary}.

%package qt
Summary: Qt bindings for %{name}
Group:	  System/Libraries
Requires: %name = %version-%release

%description qt
%{summary}.

%package qt-devel
Summary:  Development files for %{name}-qt bindings
Group:	  Development/KDE and QT
Requires: %name-qt = %version-%release

%description qt-devel
%{summary}.

%package doc
Summary:  Documenation for development using %{name}
Group:	  Development/Documentation
BuildArch: noarch

%description doc
%{summary}.

%prep
%setup
%patch1 -p1

%build
%meson  -Dqt=true \
%if_with docs
	-Ddocs=true \
%else
	-Ddocs=false \
%endif
	-Dstemming=true
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/app-info/{icons,xmls}
mkdir -p %{buildroot}/var/cache/app-info/{icons,xapian,xmls}
touch %{buildroot}/var/cache/app-info/cache.watch

%find_lang appstream

%check
#%%meson_test

%files -f appstream.lang
%doc AUTHORS LICENSE.GPLv2 LICENSE.LGPLv2.1 MAINTAINERS NEWS README.md RELEASE
%config(noreplace) %_sysconfdir/appstream.conf
%_bindir/appstreamcli
%_libdir/girepository-1.0/AppStream-1.0.typelib
%_libdir/libappstream.so.*
%dir %_datadir/app-info/
%dir %_datadir/app-info/icons
%dir %_datadir/app-info/xmls
%ghost %_cachedir/app-info/cache.watch
%dir %_cachedir/app-info
%dir %_cachedir/app-info/icons
%dir %_cachedir/app-info/xapian
%dir %_cachedir/app-info/xmls
%_man1dir/appstreamcli.1.*
%_datadir/gettext/its/metainfo.*
%_datadir/metainfo/org.freedesktop.appstream.cli.*.xml

%files devel
%_includedir/appstream/
%_libdir/libappstream.so
%_libdir/pkgconfig/appstream.pc
%_datadir/gir-1.0/AppStream-1.0.gir

%files qt
%_libdir/libAppStreamQt.so.*

%files qt-devel
%_includedir/AppStreamQt/
%_libdir/cmake/AppStreamQt/
%_libdir/libAppStreamQt.so

%files doc
%_defaultdocdir/%name
%_datadir/gtk-doc/html/%name

%changelog
* Mon Dec 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.13.1-alt0.1.b9
- Do not use unsupported option -Wno-deprecated-copy.

* Tue Dec 01 2020 Andrey Cherepanov <cas@altlinux.org> 0.13.1-alt1
- New version.

* Fri Nov 20 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.11-alt2
- Do not build API documentation because both daps and publican are not build for i586.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.11-alt1
- New version.
- Use daps instead of publican for documentation build.

* Fri Jan 24 2020 Andrey Cherepanov <cas@altlinux.org> 0.12.10-alt1
- New version.

* Mon Dec 16 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.9-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.8-alt1
- New version.

* Sun Jun 23 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.7-alt1
- New version.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.6-alt1
- New version.

* Sun Jan 27 2019 Andrey Cherepanov <cas@altlinux.org> 0.12.5-alt1
- New version.

* Mon Dec 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.4-alt1
- New version.

* Wed Oct 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.3-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt2.qa1
- NMU: applied repocop patch

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt2
- Disable tests.

* Fri Aug 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.2-alt1
- New version.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.1-alt1
- New version.

* Thu Apr 05 2018 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- New version.

* Fri Jan 26 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.8-alt1
- New version.

* Mon Oct 23 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.7-alt1
- New version

* Sat Oct 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.6-alt1
- New version

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.5-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.4-alt1
- New version
- Use meson and ninja-build for build
- Package development documentation

* Sun Aug 06 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.3-alt1
- New version

* Wed Jul 19 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.2-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.1-alt1.gita6f9e55
- New version

* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.6-alt1
- new version 0.10.6

* Wed Dec 21 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.4-alt1
- new version 0.10.4

* Mon Nov 07 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.3-alt1
- new version 0.10.3

* Tue Sep 20 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- New version 0.10.1

* Tue Aug 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- New version

* Mon May 16 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- New version

* Mon Mar 28 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.3-alt1
- New version

* Wed Dec 16 2015 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version

* Mon Sep 14 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.4-alt1
- New version

* Mon Sep 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.3-alt1
- New version

* Tue Jun 30 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.2-alt1
- New version
- appstream-qt contains libraries only for Qt5

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt2
- Rebuild with new version of xapian-core

* Sat Feb 07 2015 Andrey Cherepanov <cas@altlinux.org> 0.8.0-alt1
- New version

* Sun Jan 25 2015 Andrey Cherepanov <cas@altlinux.org> 0.7.6-alt1
- New version

* Mon Dec 15 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.5-alt1
- New version

* Tue Oct 28 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.3-alt1
- Import from Fedora
- Disable tests
