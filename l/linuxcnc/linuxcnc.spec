# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%python_req_hier

%def_without docs
%def_without static
%set_verify_elf_method unresolved=relaxed
Name: linuxcnc
Version: 2.8.1
Release: alt1

Summary: LinuxCNC controls CNC machines
Summary(ru_RU.UTF-8): Программа управления ЧПУ станков
License: GPLv2+ and LGPLv2
Group: Engineering
Url: https://github.com/LinuxCNC/linuxcnc

ExclusiveArch: aarch64 alpha %arm ia64 %ix86 x86_64

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Patch1: fix-dir-path.patch
#Patch2: linuxcnc-upstream-accommodate-systems-without-io.h.patch
#Patch3: linuxcnc-upstream-fix-undefined-symbols-1.patch
#Patch4: linuxcnc-upstream-fix-undefined-symbols-2.patch
#Patch5: linuxcnc-upstream-fix-undefined-symbols-3.patch
Patch6: qtvcp_import_fix.patch
Patch7: not_require_dpkg.patch
Buildrequires(pre): rpm-build-tcl rpm-build-python
BuildRequires: gcc-c++ pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libXaw-devel libXinerama-devel libXmu-devel libXt-devel xorg-cf-files
BuildRequires: pkgconfig(libmodbus)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libudev)
BuildRequires: libncurses-devel libreadline-devel
BuildRequires: libtirpc-devel
BuildRequires: kmod
BuildRequires: man-db
BuildRequires: python-modules-tkinter python-modules-unittest
BuildRequires: python-module-yapps2
BuildRequires: boost-devel-headers boost-python-devel
BuildRequires: pkgconfig(pygtk-2.0)
BuildRequires: tcl-devel tk-devel tcl-img tclx bwidget
#BuildRequires: tcl-blt-devel
BuildRequires: intltool
#BuildRequires: pkgconfig(libgnomeprintui-2.2)
%if_with docs
BuildPreReq: asciidoc-a2x ghostscript-common ghostscript-utils source-highlight graphviz groff-ps
%endif
BuildPreReq: desktop-file-utils ImageMagick-tools

%if_with docs
Requires: %name-doc = %version
%endif

Requires: %name-data = %version
Requires: lib%name = %version
Requires: tclx tcl-blt
%py_requires Xlib
%py_requires PyQt5.Qsci
%add_python_req_skip emccanon
%add_python_req_skip interpreter
%add_python_req_skip gtk.gdk

%filter_from_requires s/^.*rip-environment//

# replace requres python-module-gst -> python-module-gst1.0
# see https://github.com/LinuxCNC/linuxcnc/commit/fe2483ceb06a1ae93669e0f98657eb8fa1638915
%add_python_req_skip gst
Requires: python-module-gst1.0

%description
LinuxCNC is software that runs on Linux, on most standard PCs, that can
interpret G-code and run a CNC machine. It was originally developed on a
milling machine, but support was added for lathes and many other types of
machine. It can be used with mills, lathes, plasma cutters, routers, robots,
and so on. 

%description -l ru_RU.UTF-8
LinuxCNC это программа, которая работает на ОС Linux на большинстве стандартных
ПК, которые могут интерпретировать G-код и запустить станок с ЧПУ. Изначально он
был разработан для фрезерного станка, но поддержка была добавлена и для токарных
станков и многих других типов машин. Он может быть использован с токарными
станками, станками плазменной резки, роботами и так далее.

%package -n liblinuxcnc-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description -n liblinuxcnc-devel
Development files for %name

%package -n liblinuxcnc-devel-static
Summary: Static version of linuxcnc libraries
Group: Development/C++
Requires: %name-devel = %version-%release

%description -n liblinuxcnc-devel-static
Static version of linuxcnc libraries

%package data
Summary: Data files for %name
Group: Engineering
Conflicts: linuxcnc-doc < 2.7.12

%description data
Data files for %name

%package -n lib%name
Summary: Library for %name
Group: Engineering

%description -n lib%name
Library for %name

%package doc
Summary: Documementation for %name
Buildarch: noarch
Group: Documentation

%description doc
Documementation for %name

%package doc-fr
Summary: French documementation for %name
Buildarch: noarch
Group: Documentation
Requires: %name-doc = %version

%description doc-fr
French documementation for %name

%package doc-es
Summary: Spanish documementation for %name
Buildarch: noarch
Group: Documentation
Requires: %name-doc = %version

%description doc-es
Spanish documementation for %name

%prep
%setup
%patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p1
#patch5 -p1
%patch6 -p1
%patch7 -p1

sed -i 's|lib/tcltk/linuxcnc|%_lib/tcl/linuxcnc|' lib/python/rs274/options.py
sed -i 's|INCLUDES := .|INCLUDES := . /usr/include/tirpc|' src/Makefile
sed -i 's|LDFLAGS := |LDFLAGS := -ltirpc |' src/Makefile

#fix make install
sed 's/ -o root//g' -i src/Makefile

# explicitly set python-2
find . -type f -name *.py | xargs sed -i \
	-e '1s:^#!/usr/bin/env python$:#!/usr/bin/python%__python_version:' \
	-e '1s:^#!/usr/bin/python$:#!/usr/bin/python%__python_version:' \
	-e '1s:^#!/usr/bin/python3$:#!/usr/bin/python%__python_version:' \
	%nil

%build
pushd src
%autoreconf
%configure \
    --enable-non-distributable=yes \
    --with-realtime=uspace \
    --with-python=$(which python2) \
    %if_with docs
    --enable-build-documentation=pdf
    %endif

%make_build
popd

%install
pushd src
%makeinstall_std
popd

install -d -m755 %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-latency.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-pncconf.desktop %buildroot%_desktopdir
cp debian/extras/usr/share/applications/linuxcnc-stepconf.desktop %buildroot%_desktopdir

#fix desktop Name
pushd %buildroot%_desktopdir
sed 's/Name=/Name=LinuxCNC /g' -i linuxcnc-pncconf.desktop \
    linuxcnc-stepconf.desktop linuxcnc-latency.desktop
popd

#fix desktop categories
desktop-file-install --dir %buildroot%_desktopdir \
        --remove-key=Version \
        --remove-category=X-CNC \
        --add-category=Development \
        --add-category=Engineering \
        %buildroot%_desktopdir/*.desktop

### == desktop file documentation
cat>%buildroot%_desktopdir/%name-documentation.desktop<<END
[Desktop Entry]
Name=LinuxCNC Documentation
Name[ru_RU]= LinuxCNC Документация 
Exec=%_bindir/xdg-open %_docdir/%name
Icon=linuxcncicon
Terminal=false
Type=Application
Categories=Development;Engineering;
END

#install rules
mkdir -p %buildroot%_udevrulesdir
cp debian/extras/lib/udev/rules.d/* %buildroot%_udevrulesdir

# convert and install icon files
for x in 16 32 48; do
    mkdir -p %buildroot%_iconsdir/hicolor/$x'x'$x/apps
    convert linuxcncicon.png -resize $x'x'$x \
            %buildroot%_iconsdir/hicolor/$x'x'$x/apps/linuxcncicon.png
done

#fix uncompressed manual pages
pushd %buildroot%_mandir
xz `find -name *.?`
popd

%find_lang %name gmoccapy --output=%name.lang

%files
%_bindir/*
%_libexecdir/%name
%_sysconfdir/%name
%_initdir/realtime
%_udevrulesdir/*.rules
%_desktopdir/*.desktop
%_sysconfdir/X11/app-defaults/*
%_datadir/axis
%exclude %_datadir/axis/images
%_datadir/%name/hallib
%_datadir/%name/ncfiles
%_tcllibdir/%name
%python_sitelibdir/*

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/*.a

%files -n lib%name-devel
%_includedir/%name
%_libdir/*.so

%if_with static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files data -f %name.lang
%_datadir/%name
%exclude %_datadir/%name/hallib
%exclude %_datadir/%name/ncfiles
%dir %_datadir/axis
%_datadir/axis/images
%_datadir/glade3
%_datadir/gmoccapy
%_datadir/gscreen
%_datadir/gtksourceview-2.0/*
%_datadir/qtvcp/*
%_liconsdir/*
%_niconsdir/*
%_miconsdir/*
%_mandir/man?/*
%_docdir/%name
%if_with docs
%exclude %_docdir/%name/*.pdf
%endif

%if_with docs
%files doc
%_docdir/%name/*.pdf
%exclude %_docdir/%name/*_??.pdf

%files doc-fr
%_docdir/%name/*_fr.pdf

%files doc-es
%_docdir/%name/*_es.pdf
%endif

%changelog
* Sun Dec 06 2020 Anton Midyukov <antohami@altlinux.org> 2.8.1-alt1
- New version 2.8.1

* Thu Sep 17 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.15-alt3
- Fixed build on armh and rebuilt with new boost.

* Thu Mar 12 2020 Anton Midyukov <antohami@altlinux.org> 2.7.15-alt2
- Fixed tcl dir again

* Fri Mar 06 2020 Anton Midyukov <antohami@altlinux.org> 2.7.15-alt1
- New version 2.7.15

* Thu Mar 5 2020 Anton Midyukov <antohami@altlinux.org> 2.7.14-alt5
- Fixed tcl dir
- Enabled hierarchical dependency search for python2
- Update buildrequires
- Added missing requires

* Mon Dec 16 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.14-alt4
- Rebuilt with boost-1.71.0.

* Tue Oct 01 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.7.14-alt3
- Added ExclusiveArch tag to limit architectures to aarch64, alpha, %%arm,
  ia64, %%ix86, and x86_64.
- Removed noarch from %%name-data subpackage.

* Sat May 25 2019 Anton Midyukov <antohami@altlinux.org> 2.7.14-alt2
- Add io.h for aarch64 (dummy) instead of without-sys-io.h-for-no-x86.patch
- Build with libtirpc

* Tue Jul 03 2018 Anton Midyukov <antohami@altlinux.org> 2.7.14-alt1
- new version 2.7.14

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.13-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 2.7.13-alt1
- new version 2.7.13

* Tue Mar 06 2018 Anton Midyukov <antohami@altlinux.org> 2.7.12-alt2
- replace requres python-module-gst -> python-module-gst1.0
- disable build docs

* Tue Jan 30 2018 Anton Midyukov <antohami@altlinux.org> 2.7.12-alt1
- new version 2.7.12
- Fix pathdir

* Wed Aug 30 2017 Anton Midyukov <antohami@altlinux.org> 2.7.11-alt1
- New version 2.7.11
- Added missing requires 

* Sun Jul 30 2017 Anton Midyukov <antohami@altlinux.org> 2.7.10-alt2
- Fix desktop categories.

* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 2.7.10-alt1
- new version 2.7.10

* Sun Jun 11 2017 Anton Midyukov <antohami@altlinux.org> 2.7.9-alt1
- New version 2.7.9
- Remove fix_build_for_i586.patch

* Fri Mar 24 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.7.8-alt1.qa1
- Rebuilt against Tcl/Tk 8.6

* Sat Feb 04 2017 Anton Midyukov <antohami@altlinux.org> 2.7.8-alt1
- New version 2.7.8
- Fix build with libmodbus3.1.4
- Fix build for i586
- Remove subpackage python-module-linuxcnc and tcl-linuxcnc

* Fri Jul 22 2016 Anton Midyukov <antohami@altlinux.org> 2.7.5-alt1
- New version 2.7.5
- Fix repocop warning.

* Thu May 12 2016 Anton Midyukov <antohami@altlinux.org> 2.7.4-alt1.20160506.1
- Initial build for Alt Linux Sisyphus.
