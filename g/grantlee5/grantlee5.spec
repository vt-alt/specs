
%define sover 5
%define libtemplates libgrantlee_templates%sover
%define libtextdocument libgrantlee_textdocument%sover

Name: grantlee5
Version: 5.2.0
Release: alt3

Group: System/Libraries
Summary: Qt string template engine based on the Django template system
#Url: http://www.gitorious.org/grantlee/pages/Home
Url: https://github.com/steveire/grantlee
License: LGPLv2+

Source: %name-%version.tar
# FC
Patch1: grantlee-5.2.0-install_headers_into_versioned_directory.patch

# Automatically added by buildreq on Mon Aug 10 2015 (-bi)
# optimized out: cmake-modules elfutils fontconfig fonts-bitmap-misc libEGL-devel libGL-devel libqt5-core libqt5-gui libqt5-script libstdc++-devel libwayland-client libwayland-server python-base python3 python3-base qt5-base-devel ruby ruby-stdlibs
#BuildRequires: cmake doxygen fonts-bitmap-terminus fonts-otf-stix fonts-ttf-dejavu fonts-ttf-google-droid-kufi fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif fonts-type1-urw fonts-type1-xorg gcc-c++ graphviz libdb4-devel python-module-google qt5-script-devel rpm-build-python3 rpm-build-ruby
BuildRequires: cmake doxygen gcc-c++ graphviz
BuildRequires: qt5-base-devel qt5-declarative-devel rpm-build-kf5

%description
Grantlee is a plug-in based String Template system written
using the Qt framework. The goals of the project are to make it easier for
application developers to separate the structure of documents from the
data they contain, opening the door for theming.

The syntax is intended to follow the syntax of the Django template system,
and the design of Django is reused in Grantlee.
Django is covered by a BSD style license.

Part of the design of both is that application developers can extend
the syntax by implementing their own tags and filters. For details of
how to do that, see the API documentation.

For template authors, different applications using Grantlee will present
the same interface and core syntax for creating new themes. For details of
how to write templates, see the documentation.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
#BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package -n %libtemplates
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libtemplates
%name library.

%package -n %libtextdocument
Summary: %name library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libtextdocument
%name library.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Group: Development/Documentation
Summary: Grantlee API documentation
Requires: %name-common
BuildArch: noarch
%description doc
This package includes the Grantlee API documentation in HTML
format for easy browsing.

%prep
%setup -q
%patch1 -p1
sed -i 's| -ansi ||' CMakeLists.txt

%build
%K5build \
  -DBUILD_TESTS=OFF \
  #
%K5make docs

%install
%K5install
rm -rf  %buildroot/%_K5link/

for f in %buildroot/%_K5lib/lib*.so.%sover ; do
    base_name=`basename $f`
    short_name=`basename $f | sed 's|\.so\..*|.so|'`
    ln -s $base_name %buildroot/%_K5lib/$short_name
done
mkdir -p %buildroot%_docdir/HTML/en/grantlee5-apidocs
cp -prf BUILD*/apidox/* %buildroot%_docdir/HTML/en/grantlee5-apidocs

%files common
%doc AUTHORS CHANGELOG README*
%dir %_libdir/grantlee/
%dir %_libdir/grantlee/*/

%files -n %libtemplates
%_libdir/libGrantlee_TextDocument.so.%sover
%_libdir/libGrantlee_TextDocument.so.*
%_libdir/grantlee/*/grantlee_*.so

%files -n %libtextdocument
%_libdir/libGrantlee_Templates.so.%sover
%_libdir/libGrantlee_Templates.so.*

%files devel
%_includedir/Grantlee5/
#%_includedir/grantlee_*.h
%_libdir/libGrantlee_*.so
%_libdir/cmake/Grantlee5/

%files doc
%doc %_docdir/HTML/en/grantlee5-apidocs/

%changelog
* Fri Jul 24 2020 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt3
- return 5.2
- fix build requries

* Fri Jul 24 2020 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt2
- temporaty rollback to 5.1

* Wed Jul 22 2020 Sergey V Turchin <zerg@altlinux.org> 5.2.0-alt1
- new version

* Tue Oct 22 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt4
- fix compile flags

* Fri Jun 14 2019 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt3
- dont use ubt macro

* Thu Apr 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt2
- install headers into versioned directory

* Fri Aug 19 2016 Sergey V Turchin <zerg@altlinux.org> 5.1.0-alt1
- new version

* Fri Aug 07 2015 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- new version
- build with Qt5

* Tue Jun 23 2015 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- new version

* Fri Mar 28 2014 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt0.M70P.1
- built for M70P

* Fri Mar 28 2014 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- new version

* Wed Dec 12 2012 Sergey V Turchin <zerg@altlinux.org> 0.3.0-alt1
- new version

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt0.M60P.1
- build for M60P

* Tue Apr 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- 0.2.0 release (ALT#27236)

* Wed Sep 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt0.0.M60P.1
- built for M60P

* Wed Sep 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt0.1
- initial build of 0.2.0-rc1
