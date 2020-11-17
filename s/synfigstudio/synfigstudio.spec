%def_without build_docs

Name:    synfigstudio
Version: 1.4.0
Release: alt1

Summary: Synfig studio - animation program
License: GPLv2+
Group:   Office

Url:     http://www.synfig.org
#Source: https://github.com/synfig/synfig.git
Source:  %name-%version.tar
Patch:   %name-%version-%release.patch

# FIXME: would be nice on aarch64 as well
ExclusiveArch: %ix86 x86_64 %e2k

BuildRequires(pre): rpm-build-xdg
BuildRequires(pre): rpm-build-python3
BuildPreReq: fonts-ttf-liberation
BuildRequires: gcc-c++
BuildRequires: /proc
BuildRequires: ImageMagick-tools
BuildRequires: apt
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: fontconfig-devel
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: intltool
BuildRequires: libImageMagick-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXt-devel
BuildRequires: libavformat-devel
BuildRequires: libcairo-devel
BuildRequires: libdirectfb-devel
BuildRequires: libfftw3-devel
BuildRequires: libfreetype-devel
BuildRequires: libgtkmm3-devel
BuildRequires: libjasper-devel
BuildRequires: libjpeg-devel
BuildRequires: libltdl7-devel
BuildRequires: libmlt++-devel
BuildRequires: libmng-devel
BuildRequires: libpango-devel
BuildRequires: libpng-devel
BuildRequires: libsigc++2-devel
BuildRequires: libswscale-devel
BuildRequires: libtiff-devel
BuildRequires: libxml++2-devel
BuildRequires: openexr-devel
BuildRequires: libjack-devel
BuildRequires: libavcodec-devel
BuildRequires: libdv-devel
%if_with build_docs
BuildRequires: docbook-style-dsssl-utils
BuildRequires: openjade
#BuildRequires: ldp-docbook-dsssl
%endif

Requires: lib%name = %version-%release

%add_python3_compile_include %_datadir/synfig/plugins

# internal dependency
%add_python3_req_skip common

%description
Synfig Animation Studio is a powerful, industrial-strength vector-based
2D animation software, designed from the ground-up for producing
feature-film quality animation with fewer people and resources.
It is designed to be capable of producing feature-film quality
animation. It eliminates the need for tweening, preventing the
need to hand-draw each frame. Synfig features spatial and temporal
resolution independence (sharp and smoothat any resolution or
framerate), high dynamic range images, and a flexible plugin system.

%package -n lib%name
Summary: Library for Synfig studio
Group: Development/C++
Provides:  libetl = %version-%release
Obsoletes: libetl < %version-%release
Provides:  libsynfig = %version-%release
Obsoletes: libsynfig < %version-%release

%description -n lib%name
Library for Synfig studio.

%package -n lib%name-devel
Summary: Header files for Synfig studio
Group: Development/C++
Requires: lib%name = %version-%release
Provides:  libetl-devel = %version-%release
Obsoletes: libetl-devel < %version-%release
Provides:  libsynfig-devel = %version-%release
Obsoletes: libsynfig-devel < %version-%release

%description -n lib%name-devel
Header files for Synfig studio.

%prep
%setup
%patch -p1
mkdir local-pkg-config
%ifarch %e2k
# -lgcov not there yet...
find -name subs.m4 | xargs sed -i 's, -pg,,;s, -fprofile-arcs,,'
%endif

%build
%add_optflags -fpermissive -std=c++11 -I%_includedir/sigc++-2.0 -I%_libdir/sigc++-2.0/include
export PKG_CONFIG_PATH=../local-pkg-config:$PKG_CONFIG_PATH
%undefine _configure_gettext
%define rpm_synfig_dir %_builddir/%name-%version/synfig-core/src/synfig/.libs

# Build ETL
pushd ETL
%autoreconf
%configure
%make_build
cp ETL.pc ../local-pkg-config
subst 's,^includedir=.*,includedir=%_builddir/%name-%version/ETL,' ../local-pkg-config/ETL.pc
popd

# Build synfig-core
pushd synfig-core
%autoreconf
%configure --with-dv --enable-profiling --enable-profile-arcs
rm libltdl/config-h.in
cp %_datadir/libtool/libltdl/config-h.in libltdl/config-h.in
%make_build
cp synfig.pc ../local-pkg-config
subst 's,^libdir=.*,libdir=%rpm_synfig_dir,;s,^includedir=.*,includedir=%_builddir/%name-%version/synfig-core/src,' ../local-pkg-config/synfig.pc
export PATH=%_builddir/%name-%version/synfig-core/src/tool/.libs:$PATH
export LD_LIBRARY_PATH=%rpm_synfig_dir:$LD_LIBRARY_PATH
mkdir -p $HOME/.local/share/synfig
cp src/modules/synfig_modules.cfg $HOME/.local/share/synfig
cp src/modules/*/.libs/lib*.so %rpm_synfig_dir
popd

# Build main executable
pushd synfig-studio
%autoreconf
%configure
%make_build
popd

%if_with build_docs
# Build docs
pushd synfig-docs
%make_build
popd
%endif

%install
for dir in ETL synfig-core synfig-studio; do
pushd $dir
%makeinstall_std
popd
done

%if_with build_docs
# Install docs
pushd synfig-docs
%makeinstall_std
popd
%endif

# Remove generated mime database
find %buildroot%_xdgmimedir/ -maxdepth 1 -a -type f -delete

# Remove .la files
rm -f %buildroot%_libdir/synfig/modules/*.la

# Add python3 shebang to all python files
subst '/^#!\/usr\/bin\/env python$/d' `find %buildroot -name \*.py`
subst '1i#!%__python3' `find %buildroot -name \*.py`

%find_lang synfig
%find_lang %name
cat synfig.lang >> %name.lang

%files -f %name.lang
%doc synfig-studio/AUTHORS synfig-studio/NEWS synfig-studio/README synfig-studio/TODO
%_bindir/*
%config(noreplace) %_sysconfdir/synfig_modules.cfg
%exclude %_bindir/synfig
%_pixmapsdir/*
%_iconsdir/*/*/*/*.png
%_iconsdir/*/*/*/*.svg
%_desktopdir/*.desktop
%_datadir/synfig/
%_datadir/mime-info/*
%_datadir/appdata/*.appdata.xml
%_xdgmimedir/application/x-sif.xml
%_xdgmimedir/packages/*.xml

%files -n lib%name
%_bindir/synfig
%_libdir/lib*.so.*
%_libdir/synfig/modules

%files -n lib%name-devel
%_libdir/lib*.so
%_includedir/*/*
%_pkgconfigdir/*.pc

%changelog
* Mon Nov 16 2020 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt2
- NMU: skip internal python dependency 'common'

* Sat Aug 08 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.16-alt1
- New version.

* Tue Jul 21 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.15-alt1
- New version.

* Thu Jun 25 2020 Michael Shigorin <mike@altlinux.org> 1.3.14-alt2
- E2K: avoid profiling (no -lgcov just yet).

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.14-alt1
- New version.

* Thu Mar 19 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.13-alt1
- New version.

* Mon Feb 03 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.12-alt1
- New version.

* Mon Apr 22 2019 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt2
- Fix build (ALT #36651).

* Sun Feb 17 2019 Andrey Cherepanov <cas@altlinux.org> 1.3.11-alt1
- New version.

* Tue Sep 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.10-alt1
- New version.

* Tue Jun 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.9-alt1
- New version.
- Build only for i586 and x86_64.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.8-alt2.1
- NMU: rebuilt with boost-1.67.0

* Tue May 29 2018 Anton Farygin <rider@altlinux.ru> 1.3.8-alt2
- Rebuilt for new ImageMagick.

* Mon May 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.8-alt1
- New version.

* Tue Feb 13 2018 Alexandr Antonov <aas@altlinux.org> 1.3.5-alt1
- New version.

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.4-alt2
- Rebuilt for new ImageMagick.

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.4-alt1
- New version

* Fri May 12 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt2
- Rebuild with new libmng

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1
- New version

* Thu Apr 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- New version

* Wed Apr 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version

* Fri Jan 13 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Jul 03 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.10-alt1
- New version
- Build all libraries from one package

* Sun Jun 05 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- New version

* Mon Oct 05 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version

* Fri Jul 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Apr 29 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version

* Thu Mar 19 2015 Andrey Cherepanov <cas@altlinux.org> 0.64.3-alt2
- Apply patches from Fedora
- Drop obsoleted patches

* Fri Dec 26 2014 Andrey Cherepanov <cas@altlinux.org> 0.64.3-alt1
- New version

* Mon Nov 17 2014 Andrey Cherepanov <cas@altlinux.org> 0.64.2-alt1
- New version
- Fix project URL

* Fri Nov 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.64.1-alt1
- New version

* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 0.64.0-alt1
- New version

* Mon Feb 11 2013 Andrey Cherepanov <cas@altlinux.org> 0.63.05-alt1
- New version 0.63.05

* Mon Jun 20 2011 Yuriy Shirokov <yushi@altlinux.org> 0.63.00-alt1
- new version 0.63.00

* Sat Dec 18 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.02-alt1
- new version 0.62.02

* Sun Nov 07 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.01-alt2
- patch for gcc-4.5

* Sun Jun 6 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.01-alt1
- new version 0.62.01

* Wed Apr 07 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.00-alt2
- spec cleanup

* Tue Mar 23 2010 Yuriy Shirokov <yushi@altlinux.org> 0.62.00-alt1
- new version 0.62.00

* Wed Oct 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.09-alt1
- new version 0.61.09 (with rpmrb script)

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.61.08-alt1
- new version 0.61.08 (with rpmrb script)

* Fri Oct 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.07-alt1
- new version 0.61.07 (with rpmrb script)

* Sun Sep 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.06-alt2
- enable update/clean menus

* Sun Jul 01 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.06-alt1
- new version 0.61.06 (with rpmrb script)
- add dejavu font as needed during build

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.61.05-alt0.1
- initial build for ALT Linux Sisyphus

* Sun Dec 24 2006 - Manfred.Tremmel@iiv.de
- update to svn (Revision 229), seems, a lot of bugs where fixed inbetween
* Thu Dec 21 2006 - Manfred.Tremmel@iiv.de
- added --enable-optimization=1 to make it compile on SUSE 10.2
* Sat May 06 2006 - Manfred.Tremmel@iiv.de
- use -fno-inline with SUSE 10.1, because of a compiler bug in gcc 4.1
* Wed Mar 01 2006 - Manfred.Tremmel@iiv.de
- update to 0.61.05
* Mon Jan 23 2006 - Manfred.Tremmel@iiv.de
- recompile with new libffmpeg version
* Sun Jan 15 2006 - Manfred.Tremmel@iiv.de
- update to 0.61.04
* Thu Dec 15 2005 - Manfred.Tremmel@iiv.de
- first packman build, based on the spec-file
  from Robert B. Quattlebaum Jr. <darco@bigfoot.com>
