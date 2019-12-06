Name: openscad
Version: 2019.05
Release: alt1
Summary: The Programmers Solid 3D CAD Modeller
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License: GPLv2 with exceptions and CC0
Group: Engineering
Url: http://www.%name.org/

Source0: %name-%version.tar
#Source-url: https://github.com/%name/%name/releases/download/%name-%version/%name-%version.src.tar.gz
Patch: openscad-polyclipping.patch

BuildRequires(pre): rpm-macros-cmake rpm-build-python3
BuildRequires: cmake
BuildRequires: cgal libcgal-devel libcgal-qt5-devel
BuildRequires: ImageMagick-tools
BuildRequires: xorg-xvfb xvfb-run
BuildRequires: boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires: desktop-file-utils
BuildRequires: eigen3
BuildRequires: libfreetype-devel >= 2.4
BuildRequires: fontconfig-devel >= 2.10
BuildRequires: libGLEW-devel >= 1.6
BuildRequires: glib2-devel libgio libgio-devel
BuildRequires: libgmp-devel libgmpxx-devel
BuildRequires: libharfbuzz-devel libharfbuzz-utils
BuildRequires: libxml2-devel
BuildRequires: libdouble-conversion-devel
BuildRequires: libzip-devel
BuildRequires: libmpfr-devel >= 3.0.0
BuildRequires: opencsg-devel >= 1.3.2
BuildRequires: libpolyclipping-devel >= 6.1.3
BuildRequires: procps sysvinit-utils
BuildRequires: qt5-base-devel qt5-designer
BuildRequires: qt5-multimedia-devel
BuildRequires: flex
BuildRequires: libqscintilla2-qt5-devel
Requires: font(liberationmono)
Requires: font(liberationsans)
Requires: font(liberationserif)
Requires: %name-MCAD = %EVR
%add_python3_path %_datadir/%name/libraries/MCAD

%description
OpenSCAD is a software for creating solid 3D CAD objects.
Unlike most free software for creating 3D models (such as the famous
application Blender) it does not focus on the artistic aspects of 3D
modeling but instead on the CAD aspects. Thus it might be the application
you are looking for when you are planning to create 3D models of machine
parts but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

###############################################
%package MCAD
Group: Engineering
Summary: OpenSCAD Parametric CAD Library
License: LGPLv2+ and LGPLv2 and LGPLv3+ and (GPLv3 or LGPLv2) and (GPLv3+ or LGPLv2) and (CC-BY-SA or LGPLv2+) and (CC-BY-SA or LGPLv2) and CC-BY and BSD and MIT and Public Domain
Url: https://www.github.com/openscad/MCAD
Requires: %name = %version-%release
BuildArch: noarch

%description MCAD
This library contains components commonly used in designing and moching up
mechanical designs. It is currently unfinished and you can expect some API
changes, however many things are already working.

%prep
%setup
%patch -p1

# Remove unwanted things from MCAD, such as nonworking Python tests
pushd libraries/MCAD
for FILE in *.py; do
  rm -r $FILE
done
mv bitmap/README bitmap-README
popd

# Tests cmake check for MCAD by probing libraries/MCAD/__init__.py
# But we've just removed it
sed -i 's@MCAD/__init__.py@MCAD/gears.scad@' tests/CMakeLists.txt

%build
%qmake_qt5 PREFIX=%prefix  VERSION=%version CONFIG-=debug
%make_build

# tests
pushd tests
cmake -DPYTHON_EXECUTABLE:STRING=%__python3
%make_build
popd

%install
%makeinstall_std INSTALL_ROOT=%buildroot
rm -r %buildroot%_datadir/%name/fonts
%find_lang %name

for FILE in lgpl-2.1.txt README.markdown TODO bitmap-README; do
  rm %buildroot%_datadir/%name/libraries/MCAD/$FILE
done

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop

# tests
pushd tests
ctest || : # let the tests fail, as they probably won't work in hasher
popd

%files -f %name.lang
%doc COPYING
%doc README.md RELEASE_NOTES.md
%attr(755,root,root) %_bindir/%name
%_datadir/metainfo/*.xml
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_datadir/mime/packages/%name.xml
%dir %_datadir/%name
%_datadir/%name/examples
%_datadir/%name/color-schemes
%_datadir/%name/locale
%dir %_datadir/%name/libraries
%_man1dir/*

%files MCAD
%doc libraries/MCAD/lgpl-2.1.txt
%doc libraries/MCAD/README.markdown libraries/MCAD/TODO
%_datadir/%name/libraries/MCAD

%changelog
* Wed Nov 27 2019 Anton Midyukov <antohami@altlinux.org> 2019.05-alt1
- New version 2019.05
- switch to gear

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2015.03.3-alt2_12.1
- NMU: rebuilt with boost-1.67.0

* Thu Apr 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2015.03.3-alt2_12
- Rebuilt with new boost.

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 2015.03.3-alt1_12
- new version

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2015.03.2-alt3_4
- Rebuilt with qscintilla2 2.10.1.

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2015.03.2-alt2_4
- Rebuilt with CGAL 4.10
- Enabled tests

* Fri Feb 26 2016 Igor Vlasenko <viy@altlinux.ru> 2015.03.2-alt1_4
- new version
- TODO: disabled tests - need fixes for x86_64
        'No rule to make target /usr/lib/libCGAL.so'

* Mon Apr 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2014.03-alt2.2
- Rebuilt with CGAL 4.6

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2014.03-alt2.1
- rebuild with boost 1.57.0

* Wed Dec 24 2014 Dmitry Derjavin <dd@altlinux.org> 2014.03-alt2
- Revision up

* Thu May 08 2014 Igor Vlasenko <viy@altlinux.ru> 2014.03-alt1_1
- converted for ALT Linux by srpmconvert tools
- TODO: fixes for No rule to make target /usr/lib/libCGAL.so
