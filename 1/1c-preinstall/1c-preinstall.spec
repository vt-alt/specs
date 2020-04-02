%def_disable hacks
%define tested_version 8.3.7.1949

Name:    1c-preinstall
Version: 8.3
Release: alt12

Summary: Set correct environment for 1C:Enterprise client
License: GPL
Group:   System/Libraries
URL:     http://1c.ru/
Packager: Andrey Cherepanov <cas@altlinux.org>

%if_enabled hacks
BuildRequires: libImageMagick
%endif
BuildArch: noarch

Requires: file
Requires: fontconfig
Requires: glib2
Requires: glibc-pthread
Requires: libSM
Requires: libX11
Requires: libatk
Requires: libcairo
Requires: libcom_err
Requires: libcups
Requires: libfreetype
Requires: libgcc1
Requires: libgdk-pixbuf
Requires: libgio
Requires: libgperftools
Requires: libgsf
Requires: libgtk+2
Requires: libkrb5
Requires: libnsl1
Requires: libpango
Requires: libsoup
Requires: libstdc++6
Requires: libwebkitgtk2
Requires: libwebkitgtk3
Requires: zlib

Source1:  xdg-current-desktop.sh 

%description
This metapackage is intend to deploy correct environment for
1C:Enterprise client installation.

Tested with 1C:Enterprise client version %tested_version

%package full
Summary:  Set correct environment for 1C:Enterprise client with Microsoft (tm) fonts
Group:    System/Libraries
BuildArch: noarch
Requires: %name
Requires: fonts-ttf-ms

%description full
This metapackage is intend to deploy correct environment for
1C:Enterprise client installation. This package also install
Microsoft (tm) fonts are needed by 1C:Enterprise client and haspd
for HASP key support.

%install
%if_enabled hacks
mkdir -p %buildroot%_libdir
cp -a %_libdir/libMagickWand-*.so.1.* %buildroot%_libdir/
ln -rs %buildroot%_libdir/libMagickWand-*.so.1.* \
       %buildroot%_libdir/libWand.so.1
ln -rs %buildroot%_libdir/libMagickWand-*.so.1.* \
       %buildroot%_libdir/libWand.so
install -m 0755 -D %SOURCE1 %buildroot%_x11sysconfdir/profile.d/xdg-current-desktop.sh
mkdir -p %buildroot%_datadir/fonts/ttf/ms
ln -rs %buildroot%_datadir/fonts/ttf/ms %buildroot%_datadir/fonts/msttcorefonts
%else
mkdir -p %buildroot
%endif

%files
%if_enabled hacks
%_libdir/libWand.so.1
%_libdir/libWand.so
%exclude %_libdir/libMagickWand*
%_x11sysconfdir/profile.d/*.sh
%endif

%files full
%if_enabled hacks
%_datadir/fonts/msttcorefonts
%exclude %_datadir/fonts/ttf/ms
%endif

%changelog
* Thu Mar 26 2020 Andrey Cherepanov <cas@altlinux.org> 8.3-alt12
- Requires file package (ALT #31214).
- Requires libnsl1 (ALT #37176).
- Requires libwebkitgtk3 (ALT #37905).
- Requires libgperftool (ALT #37912).

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 8.3-alt11
- Return libgsf requirement for support save to XLS (ALT #33298)

* Wed May 04 2016 Andrey Cherepanov <cas@altlinux.org> 8.3-alt10
- Remove all hacks
- Add all required external packages for 8.3.7.1949

* Thu Apr 03 2014 Andrey Cherepanov <cas@altlinux.org> 8.3-alt9
- Rebuild with new version of ImageMagick

* Tue Mar 18 2014 Andrey Cherepanov <cas@altlinux.org> 8.3-alt8
- Require libgsf for support save to XLS

* Fri Nov 29 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt7
- New version of 1C:Enterprise wants libWand.so

* Fri Nov 08 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt6
- Make system Microsoft TTF fonts available for 1C client (ALT #29560)

* Thu Oct 03 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt5
- Set XDG_CURRENT_DESKTOP based on current DE (thanks sem@)
- New metapackage 1c-preinstall-full with fonts-ttf-ms

* Wed Jul 10 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt4
- Pack symlink libWand.so.1 as file, disable triggers

* Tue Jul 09 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt3
- Correct detect library path on x86_64 (ALT #29161)

* Fri Jun 21 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt2
- Force create symbolic link

* Wed Jun 19 2013 Andrey Cherepanov <cas@altlinux.org> 8.3-alt1
- Initial build in Sisyphus
