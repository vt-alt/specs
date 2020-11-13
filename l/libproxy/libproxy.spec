# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libpcre)
# END SourceDeps(oneline)
%def_without gnome
%def_with gnome3
%def_with kde
%def_with networkmanager
%def_with mozjs
%def_without webkit
%def_with webkit3
%def_without dotnet
%def_without python2
%def_with python3
%define _libexecdir %_prefix/libexec

Name: libproxy
Version: 0.4.15
Release: alt5
Summary: A library handling all the details of proxy configuration

Group: System/Libraries
License: %gpllgpl2plus
Url: http://libproxy.github.io/libproxy

# https://github.com/libproxy/libproxy
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-licenses
BuildPreReq: cmake ctest gcc-c++ zlib-devel

%{?_with_python2:BuildRequires: python-devel}
%{?_with_python3:BuildRequires: python3-devel}
# gnome
%{?_with_gnome:BuildRequires: pkgconfig(gconf-2.0) pkgconfig(gobject-2.0)}
# gnome3
%{?_with_gnome3:BuildRequires: pkgconfig(gio-2.0) >= 2.26 pkgconfig(gobject-2.0)}
# kde4
%{?_with_kde:BuildPreReq: /usr/bin/kreadconfig5}
# libmozjs
%{?_with_mozjs:BuildRequires: pkgconfig(mozjs-60)}
# webkit (gtk)
%{?_with_webkit:BuildRequires: pkgconfig(webkit-1.0)}
%{?_with_webkit3:BuildRequires: pkgconfig(javascriptcoregtk-4.0)}
# NetworkManager
%{?_with_networkmanager:BuildRequires: pkgconfig(libnm) pkgconfig(dbus-1)}
# dotnet
%{?_with_dotnet:BuildPreReq: mono-devel >= 2.0.0 /proc rpm-build-mono mono-mcs}

%define modilesdir %_libdir/%name/%version/modules/
%description
libproxy offers the following features:

    * extremely small core footprint (< 35K)
    * no external dependencies within libproxy core
      (libproxy plugins may have dependencies)
    * only 3 functions in the stable external API
    * dynamic adjustment to changing network topology
    * a standard way of dealing with proxy settings across all scenarios
    * a sublime sense of joy and accomplishment

%package tools
Summary: A sample & test application to test what libproxy will reply
Group: Networking/Other
Requires: %name = %version-%release

%description tools
A simple application that will use libproxy to give the results you can expect from.
other applications. Great to debug what would happen.

%package -n python-module-%name
Summary: Python bindings for %name
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description -n python-module-%name
Allows for the usage of libproxy from python applications

%package -n python3-module-%name
Summary: Python3 bindings for %name
Group: Development/Python3
BuildArch: noarch
Requires: %name = %version-%release

%description -n python3-module-%name
Allows for the usage of libproxy from python3 applications

%package gnome
Summary: Libproxy module for gnome configuration
Group: System/Libraries
Requires: %name = %version-%release

%description gnome
A module to extend libproxy with capabilities to query gnome/gconf about the proxy settings

%package gnome3
Summary: Libproxy module for gnome3 configuration
Group: System/Libraries
Requires: %name = %version-%release

%description gnome3
A module to extend libproxy with capabilities to query gnome/gsettings about the proxy settings

%package kde
Summary: Libproxy module for kde configuration
Group: System/Libraries
Requires: %name = %version-%release
#Requires: /usr/bin/kreadconfig5
Provides: %name-kde4 = %version-%release
Obsoletes: %name-kde4 < %version-%release

%description kde
A module to extend libproxy with capabilities to query KDE4 about proxy settings

%package mozjs
Summary: Libproxy module to support wpad/pac parsing via Mozilla JavaScript Engine
Group: System/Libraries
Requires: %name = %version-%release

%description mozjs
A module to extend libproxy with capabilities to pass addresses to a WPAD/PAC Script
to have it parse for the correct proxy. PAC requires JavaScript Engine in the back.

%package webkit
Summary: Libproxy module to support webkit
Group: System/Libraries
Requires: %name = %version-%release

%description webkit
The %name-webkit package contains the %name plugin for
WebKit.

%package networkmanager
Summary: Libproxy module for networkmanager configuration
Group: System/Libraries

%description networkmanager
A module to extend libproxy with capabilities to query NetworkManager about proxy settings

%package sharp
Summary:  Mono bindings for %name
Group: Development/Other
Requires: %name = %version-%release

%description sharp
Allows for the usage of libproxy from mono applications

%package sharp-devel
Summary:  Mono bindings for %name
Group: Development/Other
Requires: %name-sharp = %version-%release

%description sharp-devel
Development files for %name-sharp-devel

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q
%patch -p1

%build
%cmake \
	-DLIBEXEC_INSTALL_DIR=%_libexecdir \
	-DMODULE_INSTALL_DIR=%modilesdir \
%if_without gnome
	-DWITH_GNOME2=OFF \
%endif
%if_without python2
	-DWITH_PYTHON2=OFF \
%endif
%if_without python3
	-DWITH_PYTHON3=OFF \
%endif
	-DWITH_WEBKIT3=ON \
	-DWITH_PERL=OFF

%cmake_build

%install
%cmakeinstall_std

#In case all modules are disabled
mkdir -p %buildroot%modilesdir

%check
pushd BUILD
%make test
popd

%files
%_libdir/*.so.*
%dir %_libdir/%name
%dir %_libdir/%name/%version
%dir %modilesdir

%doc AUTHORS README

%files tools
%_bindir/proxy

%if_with python2
%files -n python-module-%name
%python_sitelibdir_noarch/*
%endif

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir_noarch/*
%endif

%if_with gnome
%files gnome
%modilesdir/config_gnome.so
%_usr/libexec/pxgconf
%endif

%if_with gnome3
%files gnome3
%modilesdir/config_gnome3.so
%_usr/libexec/pxgsettings
%endif

%if_with kde
%files kde
%modilesdir/config_kde.so
%endif

%if_with mozjs
%files mozjs
%modilesdir/pacrunner_mozjs.so
%endif

%if_with webkit3
%files webkit
%modilesdir/pacrunner_webkit.so
%endif

%if_with networkmanager
%files networkmanager
%modilesdir/network_networkmanager.so
%endif

%if_with dotnet
%files sharp
%_monodir/%name-sharp
%_monogacdir/*
%exclude %_libdir/%name/%version/libproxy-sharp.dll

%files sharp-devel
%_pkgconfigdir/libproxy-sharp-1.0.pc
%endif

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/libproxy-1.0.pc
%_datadir/cmake/Modules/Findlibproxy.cmake

%changelog
* Wed Nov 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.15-alt5
- Fixed python2 and python3 switches.

* Wed Nov 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.15-alt4
- Applied security fixes from upstream (Fixes: CVE-2020-25219, CVE-2020-26154)

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.15-alt3.1
- NMU: applied logoved fixes

* Sat Apr 20 2019 Alexey Shabalin <shaba@altlinux.org> 0.4.15-alt3
- fixed build with python-3.7
- build with mozjs-60

* Wed Oct 03 2018 Alexey Shabalin <shaba@altlinux.org> 0.4.15-alt2
- backport patches for build with mozjs-52

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 0.4.15-alt1
- 0.4.15

* Fri Jan 20 2017 Alexey Shabalin <shaba@altlinux.ru> 0.4.14-alt1
- 0.4.14
- add python3 package

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.13-alt1
- 0.4.13

* Wed Mar 16 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.12-alt1
- 0.4.12

* Tue Jan 29 2013 Alexey Shabalin <shaba@altlinux.ru> 0.4.11-alt1
- 0.4.11

* Fri Oct 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.10-alt1
- 0.4.10

* Tue Jan 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.7-alt3
- disable build with RPATH

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.7-alt2.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.7-alt2
- build svn snapshot (20110903)
- rebuild with new libwebkitgtk-1.6.1
- build with libmozjs

* Mon Aug 22 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.7-alt1
- 0.4.7
- build without mozjs support
- build without gnome and webkitgtk support (but with gnome3 and webkitgtk3)

* Thu May 05 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt3
- pre 0.4.7
- add gnome3 subpackage
- build gnome2 and gnome3 support
- build python binding as noarch
- build with xulrunner-2.0

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt2
- rebuild with new libwebkitgtk

* Tue Oct 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6
- run tests

* Wed May 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Fri May 07 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt3
- fix upstream bug #108 (http://code.google.com/p/libproxy/issues/detail?id=108)

* Thu Apr 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt2
- svn snapshot r659
- enable build with RPATH

* Thu Mar 11 2010 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0 + svn snapshot r622
- disable mono binding

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.1
- Rebuilt with python 2.6

* Thu Oct 29 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Sep 23 2009 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0
- networkmanager package
- .Net bindings package
- update descriptions
- add versioning

* Tue May 05 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt2.r334
- svn r334
- update spec for build from git.alt

* Fri Apr 10 2009 Alexey Shabalin <shaba@altlinux.ru> 0.2.3-alt1.1
- rebuild with webkit-1.1.4

* Tue Feb 03 2009 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- adapted for Sisyphus

* Thu Jan 22 2009 kwizart < kwizart at gmail.com > - 0.2.3-8
- Merge NetworkManager module into the main libproxy package
- Main Requires the -python and -bin subpackage
 (splitted for multilibs compliance).

* Fri Oct 24 2008 kwizart < kwizart at gmail.com > - 0.2.3-7
- Disable Gnome/KDE default support via builtin modules.
 (it needs to be integrated via Gconf2/neon instead).

* Tue Oct 21 2008 kwizart < kwizart at gmail.com > - 0.2.3-6
- Disable Obsoletes.
- Requires ev instead of evr for optionnals sub-packages.

* Tue Oct 21 2008 kwizart < kwizart at gmail.com > - 0.2.3-5
- Use conditionals build.

* Mon Sep 15 2008 kwizart < kwizart at gmail.com > - 0.2.3-4
- Remove plugin- in the name of the packages

* Mon Aug  4 2008 kwizart < kwizart at gmail.com > - 0.2.3-3
- Move proxy.h to libproxy/proxy.h
  This will prevent it to be included in the default include path
- Split main to libs and util and use libproxy to install all

* Mon Aug  4 2008 kwizart < kwizart at gmail.com > - 0.2.3-2
- Rename binding-python to python
- Add Requires: gecko-libs >= %%{gecko_version}
- Fix some descriptions
- Add plugin-webkit package

* Fri Jul 11 2008 kwizart < kwizart at gmail.com > - 0.2.3-1
- Convert to Fedora spec

* Fri Jun 6 2008 - dominique-rpm@leuenberger.net
- Updated to version 0.2.3
* Wed Jun 4 2008 - dominique-rpm@leuenberger.net
- Extended spec file to build all available plugins
* Tue Jun 3 2008 - dominique-rpm@leuenberger.net
- Initial spec file for Version 0.2.2

